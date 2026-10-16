# Apaga o texto fixo do original antes do Seedance (1ª rodada manteve o texto): inpaint Telea por frame,
# máscara = pixels brancos na caixa do texto (x 160-920, y 595-1145), dilatada 6 px.
import cv2, numpy as np, subprocess, sys
src,dst='original/original-h264.mp4','original/original-semtexto-v.mp4'
cap=cv2.VideoCapture(src); w,h=1080,1920
p=subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{w}x{h}','-r','30','-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',dst],stdin=subprocess.PIPE)
k=np.ones((13,13),np.uint8)
while True:
    ok,f=cap.read()
    if not ok: break
    m=np.zeros((h,w),np.uint8); roi=f[595:1145,160:920]
    m[595:1145,160:920]=(roi.min(2)>190).astype(np.uint8)*255
    m=cv2.dilate(m,k)
    p.stdin.write(cv2.inpaint(f,m,7,cv2.INPAINT_TELEA).tobytes())
p.stdin.close(); p.wait()
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',dst,'-i',src,'-map','0:v','-map','1:a','-c','copy','original/original-semtexto.mp4'])
