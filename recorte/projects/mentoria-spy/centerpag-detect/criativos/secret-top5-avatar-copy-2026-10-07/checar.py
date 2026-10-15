#!/usr/bin/env python3
# Triagem dos clipes (cópia do checar.py de manuela-avatares-2026-10-06): moldura, lateral mexendo (gente entrando), 2º rosto YuNet>=0,86, rosto sumindo, tamanho do rosto variando.
# rosto sumindo e variação do tamanho do rosto (troca de pessoa/zoom). Na esquete (eA/eB) câmera é de mão: borda/lateral/sem-rosto são esperados, só vale 2º rosto.
import subprocess, sys, os, numpy as np, cv2
os.chdir(os.path.dirname(os.path.abspath(__file__))); M='/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'; ruim=0
for b in sys.argv[1:]:
    c=f'clipes/{b}.mp4'; w,h=map(int,subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',c],capture_output=True,text=True).stdout.split(','))
    raw=subprocess.run(['ffmpeg','-v','error','-i',c,'-vf',f'fps=6,scale={w//2}:{h//2}','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    w,h=w//2,h//2; f=np.frombuffer(raw,np.uint8).reshape(-1,h,w,3); g=f.mean(3)  # rosto grande: YuNet acerta em meia resolução
    borda=np.array([max(abs(x[:5].mean()-g[0][:5].mean()),abs(x[-5:].mean()-g[0][-5:].mean()),abs(x[:,:5].mean()-g[0][:,:5].mean()),abs(x[:,-5:].mean()-g[0][:,-5:].mean())) for x in g])
    lat=np.array([max(np.abs(x[:, :35]-g[0][:, :35]).mean(),np.abs(x[:,-35:]-g[0][:,-35:]).mean()) for x in g])
    det=cv2.FaceDetectorYN_create(M,'',(w,h),0.86,0.3,5000); n=[];hh=[]
    for x in f:
        d=det.detect(np.ascontiguousarray(x))[1]; n.append(0 if d is None else len(d))
        if d is not None and len(d): hh.append(max(d,key=lambda r:r[-1])[3])
    prob=[]; esq=False
    if max(n)>1: prob.append(f'{max(n)} rostos em {n.index(max(n))/6:.1f}s')
    if not esq:
        if borda.max()>40: prob.append(f'borda muda em {np.argmax(borda>40)/6:.1f}s ({borda.max():.0f})')
        if lat.max()>28: prob.append(f'lateral mexe em {np.argmax(lat>28)/6:.1f}s ({lat.max():.0f})')
        if min(n)==0: prob.append(f'sem rosto em {n.index(0)/6:.1f}s')
        if hh and min(hh)/max(hh)<0.8: prob.append(f'rosto varia x{min(hh)/max(hh):.2f}')
    ruim+=bool(prob); print(b,'OK' if not prob else 'PROBLEMA: '+'; '.join(prob),f'(borda {borda.max():.0f}, lateral {lat.max():.0f}, rostos/frame {min(n)}-{max(n)}, h {min(hh) if hh else 0:.0f}-{max(hh) if hh else 0:.0f})')
sys.exit(1 if ruim else 0)
