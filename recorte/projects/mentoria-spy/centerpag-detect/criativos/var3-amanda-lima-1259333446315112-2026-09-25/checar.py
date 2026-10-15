#!/usr/bin/env python3
# Triagem dos clipes Pruna (molde Kendall/podcast Gram): decodifica inteiro (WaveSpeed trunca sem erro), moldura (borda muda vs 1º frame),
# gente entrando (faixa lateral de 70 px), 2º rosto (YuNet >= 0,86), rosto sumindo, variação do tamanho do rosto, troca de pessoa (histograma do rosto).
# Uso (de projects/mentoria-spy/): python3 .../checar.py c1 [c2 …]
import subprocess, sys, json, numpy as np, cv2
L='centerpag-detect/criativos/var3-amanda-lima-1259333446315112-2026-09-25'; M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
ruim=0
for b in sys.argv[1:]:
    c=f'{L}/clipes/{b}.mp4'
    p=subprocess.run(['ffmpeg','-v','error','-i',c,'-f','null','-'],capture_output=True,text=True)
    dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',c],capture_output=True,text=True).stdout)
    raw=subprocess.run(['ffmpeg','-v','error','-i',c,'-vf','fps=6','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    f=np.frombuffer(raw,np.uint8).reshape(-1,1280,704,3); g=f.mean(3)
    borda=np.array([max(abs(x[:10].mean()-g[0][:10].mean()),abs(x[-10:].mean()-g[0][-10:].mean()),abs(x[:,:10].mean()-g[0][:,:10].mean()),abs(x[:,-10:].mean()-g[0][:,-10:].mean())) for x in g])
    lat=np.array([max(np.abs(x[:, :70]-g[0][:, :70]).mean(),np.abs(x[:,-70:]-g[0][:,-70:]).mean()) for x in g])
    det=cv2.FaceDetectorYN_create(M,'',(704,1280),0.86,0.3,5000); n=[];h=[];hist=[]
    for x in f:
        d=det.detect(np.ascontiguousarray(x))[1]; n.append(0 if d is None else len(d))
        if d is not None and len(d):
            a=max(d,key=lambda r:r[-1]); h.append(a[3]); X,Y,W,H=[int(v) for v in a[:4]]
            roi=cv2.cvtColor(x[max(Y,0):Y+H,max(X,0):X+W],cv2.COLOR_BGR2HSV); hh=cv2.calcHist([roi],[0,1],None,[16,8],[0,180,0,256]); hist.append(cv2.normalize(hh,hh).flatten())
    prob=[]
    if p.stderr.strip(): prob.append('decode: '+p.stderr.strip()[:80])
    if borda.max()>40: prob.append(f'borda muda em {np.argmax(borda>40)/6:.1f}s ({borda.max():.0f})')
    if lat.max()>28: prob.append(f'lateral mexe em {np.argmax(lat>28)/6:.1f}s ({lat.max():.0f})')
    if max(n)>1: prob.append(f'{max(n)} rostos em {n.index(max(n))/6:.1f}s')
    if min(n)==0: prob.append(f'sem rosto em {n.index(0)/6:.1f}s')
    if h and min(h)/max(h)<0.8: prob.append(f'rosto varia x{min(h)/max(h):.2f}')
    if hist:
        cor=[cv2.compareHist(hist[0],x,cv2.HISTCMP_CORREL) for x in hist]
        if min(cor)<0.5: prob.append(f'rosto muda (hist corr {min(cor):.2f} em {np.argmin(cor)/6:.1f}s)')
    ruim+=bool(prob); print(b,f'{dur:.2f}s {len(f)} fr@6','OK' if not prob else 'PROBLEMA: '+'; '.join(prob),f'(borda {borda.max():.0f}, lateral {lat.max():.0f}, rosto h {min(h):.0f}-{max(h):.0f})')
sys.exit(1 if ruim else 0)
