# Apaga o texto fixo do original antes do Seedance (lição de 16/10: o Seedance às vezes mantém o texto queimado).
# Máscara estática: texto fixo = pixel que fica claro (mínimo temporal) ou escuro (máximo temporal) o vídeo todo,
# dentro da caixa do texto; dilatada e aplicada com inpaint Telea em cada frame.
# uso: python3 apagar-texto.py <pasta> <x0> <y0> <x1> <y1> <claro|escuro> <limiar>
import cv2, numpy as np, subprocess, sys
pasta,x0,y0,x1,y1,modo,lim=sys.argv[1],*map(int,sys.argv[2:6]),sys.argv[6],int(sys.argv[7])
src,dst=f'{pasta}/original/original-h264.mp4',f'{pasta}/original/original-semtexto-v.mp4'
cap=cv2.VideoCapture(src); fr=[]
while True:
    ok,f=cap.read()
    if not ok: break
    fr.append(f)
a=np.stack(fr)[:,y0:y1,x0:x1]
est=(a.min(0).min(2)>lim) if modo=='claro' else (a.max(0).max(2)<lim)
h,w=fr[0].shape[:2]; m=np.zeros((h,w),np.uint8); m[y0:y1,x0:x1]=est.astype(np.uint8)*255
m=cv2.dilate(m,np.ones((11,11),np.uint8)); cv2.imwrite(f'{pasta}/original/mascara.png',m)
p=subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{w}x{h}','-r','30','-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',dst],stdin=subprocess.PIPE)
for f in fr: p.stdin.write(cv2.inpaint(f,m,7,cv2.INPAINT_TELEA).tobytes())
p.stdin.close(); p.wait()
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',dst,'-i',src,'-map','0:v','-map','1:a?','-c','copy',f'{pasta}/original/original-semtexto.mp4'])
cv2.imwrite(f'{pasta}/original/semtexto-frame.png',cv2.inpaint(fr[15],m,7,cv2.INPAINT_TELEA))
print(pasta,len(fr),'frames, pixels na máscara',int((m>0).sum()))
