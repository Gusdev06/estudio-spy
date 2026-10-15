#!/usr/bin/env python3
# Triagem dos clipes Pruna (herdada do Kendall 25/09): moldura (borda que muda vs o 1º frame), gente entrando (faixa lateral de 70 px mudando),
# 2º rosto (YuNet score >= 0,86), rosto sumindo, variação do tamanho do rosto e TROCA DE PESSOA (distância do recorte do rosto vs o 1º frame).
# Uso (de projects/mentoria-spy/): python3 .../checar.py a1-s7 b-s7 ...
import subprocess, sys, numpy as np, cv2
L='centerpag-detect/criativos/var5-flora-959352790554428-2026-09-25'; M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
ruim=0
for c in sys.argv[1:]:
    arq=f'{L}/clipes/{c}.mp4'
    w,h=[int(x) for x in subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',arq],capture_output=True,text=True).stdout.strip().split(',')]
    raw=subprocess.run(['ffmpeg','-v','error','-i',arq,'-vf','fps=8','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    f=np.frombuffer(raw,np.uint8).reshape(-1,h,w,3); g=f.mean(3)
    borda=np.array([max(abs(x[:10].mean()-g[0][:10].mean()),abs(x[-10:].mean()-g[0][-10:].mean()),abs(x[:,:10].mean()-g[0][:,:10].mean()),abs(x[:,-10:].mean()-g[0][:,-10:].mean())) for x in g])
    lat=np.array([max(np.abs(x[:, :70]-g[0][:, :70]).mean(),np.abs(x[:,-70:]-g[0][:,-70:]).mean()) for x in g])
    det=cv2.FaceDetectorYN_create(M,'',(w,h),0.86,0.3,5000); n=[];hs=[];idd=[];ref=None
    for x in f:
        d=det.detect(np.ascontiguousarray(x))[1]; n.append(0 if d is None else len(d))
        if d is not None and len(d):
            a=max(d,key=lambda r:r[-1]); hs.append(a[3]); X,Y,W,H=[int(v) for v in a[:4]]
            cr=cv2.resize(cv2.cvtColor(x[max(Y,0):Y+H,max(X,0):X+W],cv2.COLOR_BGR2GRAY),(48,48)).astype(float); cr=(cr-cr.mean())/(cr.std()+1e-6)
            if ref is None: ref=cr
            idd.append(float((cr*ref).mean()))
    prob=[]
    if borda.max()>40: prob.append(f'borda muda em {np.argmax(borda>40)/8:.1f}s ({borda.max():.0f})')
    if lat.max()>28: prob.append(f'lateral mexe em {np.argmax(lat>28)/8:.1f}s ({lat.max():.0f})')
    if max(n)>1: prob.append(f'{max(n)} rostos em {n.index(max(n))/8:.1f}s')
    if min(n)==0: prob.append(f'sem rosto em {n.index(0)/8:.1f}s')
    if hs and min(hs)/max(hs)<0.8: prob.append(f'rosto varia x{min(hs)/max(hs):.2f}')
    if idd and min(idd)<0.5: prob.append(f'rosto muda (corr {min(idd):.2f})')
    ruim+=bool(prob); print(c,'OK' if not prob else 'PROBLEMA: '+'; '.join(prob),f'(borda {borda.max():.0f}, lateral {lat.max():.0f}, rosto h {min(hs):.0f}-{max(hs):.0f}, corr min {min(idd):.2f})')
sys.exit(1 if ruim else 0)
