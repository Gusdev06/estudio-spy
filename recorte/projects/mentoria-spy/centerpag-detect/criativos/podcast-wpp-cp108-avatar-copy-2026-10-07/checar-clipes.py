#!/usr/bin/env python3
# Varre clipes Pruna inteiros (4 fps): rostos por frame com YuNet score>=0,8, deriva do centro/altura do rosto vs. 1º segundo,
# e gera uma folha de 8 instantes por clipe. Uso (de projects/mentoria-spy/): python3 .../checar-clipes.py <pasta-clipes> <folha.jpg> [b1 …]
import subprocess, sys, os, numpy as np, cv2
M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
pasta, folha = sys.argv[1], sys.argv[2]; bl = sys.argv[3:] or ['b1','b3','b4','b5','b6','b8']
linhas=[]
for b in bl:
    f=f'{pasta}/{b}.mp4'
    if not os.path.exists(f): continue
    cw,ch=[int(x) for x in subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',f],capture_output=True,text=True).stdout.strip().split(',')]
    raw=subprocess.run(['ffmpeg','-hide_banner','-v','error','-i',f,'-vf','fps=4','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    n=len(raw)//(cw*ch*3); fr=np.frombuffer(raw[:n*cw*ch*3],np.uint8).reshape(n,ch,cw,3)
    det=cv2.FaceDetectorYN_create(M,'',(cw,ch),0.8,0.3,5000); cont=[]; hs=[]; cx=[]
    for x in fr:
        _,d=det.detect(np.ascontiguousarray(x)); d=[] if d is None else d
        cont.append(len(d))
        if len(d): r=max(d,key=lambda r:r[-1]); hs.append(r[3]); cx.append(r[0]+r[2]/2)
    h0=np.median(hs[:4]) if hs else 1; c0=np.median(cx[:4]) if cx else 0
    extra=[i/4 for i,c in enumerate(cont) if c>1]; zero=[i/4 for i,c in enumerate(cont) if c==0]
    print(f"{b}: {cw}x{ch} {n} amostras · rostos/frame max {max(cont) if cont else 0} · sem rosto {len(zero)} · >1 rosto em {extra[:8]} · altura x{min(hs)/h0:.2f}-{max(hs)/h0:.2f} · centro desvio max {max(abs(np.array(cx)-c0)) if cx else 0:.0f}px")
    idx=np.linspace(0,n-1,8).astype(int)
    linhas.append(np.hstack([cv2.resize(fr[i],(320,int(320*ch/cw))) for i in idx]))
if linhas:
    w=max(l.shape[1] for l in linhas); cv2.imwrite(folha, np.vstack([cv2.resize(l,(w,int(l.shape[0]*w/l.shape[1]))) for l in linhas]), [cv2.IMWRITE_JPEG_QUALITY, 80])
