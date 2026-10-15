#!/usr/bin/env python3
# Varre a janela (y 346, 720x587) da peça a 6 fps: rostos YuNet>=0,8 por frame (>1 = pessoa extra), centro do rosto na janela,
# e karaokê (y 935-1075) encostando na borda. Uso: conferir-peca.py <peca.mp4> <linhas.json>
import subprocess,sys,json,numpy as np,cv2
M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'; f,lj=sys.argv[1],sys.argv[2]
tl=json.load(open(lj)); cta=[l['ini'] for l in tl if l['i']==9][0]
raw=subprocess.run(['ffmpeg','-hide_banner','-v','error','-t',str(cta),'-i',f,'-vf','fps=6','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
n=len(raw)//(720*1280*3); fr=np.frombuffer(raw[:n*720*1280*3],np.uint8).reshape(n,1280,720,3)
det=cv2.FaceDetectorYN_create(M,'',(720,587),0.8,0.3,5000); extra=[]; cx=[]; borda=[]
for i,x in enumerate(fr):
    w=np.ascontiguousarray(x[346:933]); _,d=det.detect(w); d=[] if d is None else d
    if len(d)>1: extra.append(round(i/6,2))
    if len(d): r=max(d,key=lambda r:r[-1]); cx.append(r[0]+r[2]/2)
    k=x[935:1075]; 
    if (k[:,:12].max()>200) or (k[:,-12:].max()>200): borda.append(round(i/6,2))
print(f'{n} frames · >1 rosto: {extra[:10]} · centro do rosto x {min(cx):.0f}-{max(cx):.0f} (janela 720) · karaokê na borda: {borda[:10]}')
