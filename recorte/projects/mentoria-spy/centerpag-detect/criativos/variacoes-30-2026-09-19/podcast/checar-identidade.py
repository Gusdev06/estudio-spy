#!/usr/bin/env python3
# Detecta o "drift" do Pruna (1º frame = imagem, depois outra pessoa/enquadramento): compara o tamanho do rosto (YuNet) no 1º frame
# com a mediana do resto do clipe, e a cor média da região do rosto. Uso: python3 checar-identidade.py <clipes.mp4…>
import cv2, subprocess, sys, numpy as np
M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
def frames(clip,fps=3):
    w,h=[int(x) for x in subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',clip],capture_output=True,text=True).stdout.strip().split(',')]
    raw=subprocess.run(['ffmpeg','-hide_banner','-v','error','-i',clip,'-vf',f'select=eq(n\\,0)+not(mod(n\\,{int(24/fps)})),scale={w}:{h}','-vsync','0','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    n=len(raw)//(w*h*3); return np.frombuffer(raw[:n*w*h*3],np.uint8).reshape(n,h,w,3),w,h
for clip in sys.argv[1:]:
    fr,w,h=frames(clip); det=cv2.FaceDetectorYN_create(M,'',(w,h),0.6,0.3,5000); rs=[]
    for f in fr:
        _,d=det.detect(np.ascontiguousarray(f))
        if d is not None and len(d):
            x,y,ww,hh=[int(v) for v in max(d,key=lambda r:r[2]*r[3])[:4]]; roi=f[max(0,y):y+hh,max(0,x):x+ww]
            rs.append((hh, roi.reshape(-1,3).mean(axis=0) if roi.size else np.zeros(3)))
    if len(rs)<3: print(f'{clip}: sem rosto suficiente'); continue
    h0,c0=rs[0]; hm=np.median([r[0] for r in rs[1:]]); cm=np.median([r[1] for r in rs[1:]],axis=0)
    dz=hm/h0; dc=float(np.abs(cm-c0).mean())
    flag='DRIFT' if (dz>1.25 or dz<0.8 or dc>28) else 'ok'
    print(f'{flag:5s} {clip.split("/")[-3]}/{clip.split("/")[-1]}: rosto 1º frame {h0}px → mediana {hm:.0f}px (×{dz:.2f}) · cor Δ{dc:.0f}')
