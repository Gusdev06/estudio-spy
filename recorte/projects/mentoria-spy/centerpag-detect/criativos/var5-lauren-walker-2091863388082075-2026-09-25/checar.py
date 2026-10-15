#!/usr/bin/env python3
# Triagem dos clipes Pruna (adaptada do kendall, 25/09): moldura (borda que muda vs o 1º frame), gente entrando (faixa lateral de 70 px mudando),
# 2º rosto (YuNet score >= 0,86), rosto sumindo e troca de pessoa/zoom (altura do rosto variando). Uso (desta pasta): python3 checar.py c1 [c2]
import subprocess, sys, numpy as np, cv2
M='../../../gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'; ruim=0
for b in sys.argv[1:]:
    c=f'clipes/{b}.mp4'
    raw=subprocess.run(['ffmpeg','-v','error','-i',c,'-vf','fps=8','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    f=np.frombuffer(raw,np.uint8).reshape(-1,1280,704,3); g=f.mean(3)
    borda=np.array([max(abs(x[:10].mean()-g[0][:10].mean()),abs(x[-10:].mean()-g[0][-10:].mean()),abs(x[:,:10].mean()-g[0][:,:10].mean()),abs(x[:,-10:].mean()-g[0][:,-10:].mean())) for x in g])
    lat=np.array([max(np.abs(x[:, :70]-g[0][:, :70]).mean(),np.abs(x[:,-70:]-g[0][:,-70:]).mean()) for x in g])
    det=cv2.FaceDetectorYN_create(M,'',(704,1280),0.86,0.3,5000); n=[];h=[];cx=[]
    for x in f:
        d=det.detect(np.ascontiguousarray(x))[1]; n.append(0 if d is None else len(d))
        if d is not None and len(d): a=max(d,key=lambda r:r[-1]); h.append(a[3]); cx.append(a[0]+a[2]/2)
    prob=[]
    if borda.max()>40: prob.append(f'borda muda em {np.argmax(borda>40)/8:.1f}s ({borda.max():.0f})')
    if lat.max()>28: prob.append(f'lateral mexe em {np.argmax(lat>28)/8:.1f}s ({lat.max():.0f})')
    if max(n)>1: prob.append(f'{max(n)} rostos em {n.index(max(n))/8:.1f}s')
    if min(n)==0: prob.append(f'sem rosto em {n.index(0)/8:.1f}s')
    if h and min(h)/max(h)<0.8: prob.append(f'rosto varia x{min(h)/max(h):.2f}')
    ruim+=bool(prob); print(b,'OK' if not prob else 'PROBLEMA: '+'; '.join(prob),f'(borda {borda.max():.0f}, lateral {lat.max():.0f}, rosto h {min(h):.0f}-{max(h):.0f}, x {min(cx):.0f}-{max(cx):.0f})')
    # folha visual: 12 frames
    idx=np.linspace(0,len(f)-1,12).astype(int); ims=[cv2.resize(f[i],(176,320)) for i in idx]
    cv2.imwrite(f'conferencia/triagem-{b}.jpg',np.vstack([np.hstack(ims[:6]),np.hstack(ims[6:])]))
sys.exit(1 if ruim else 0)
