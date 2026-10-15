#!/usr/bin/env python3
"""medir-recorte.py <imagem.png|clipe.mp4> <saida.env>  (roda no venv com cv2)
Mede rosto/olhos na geometria do Pruna (704×1280: escala pela altura + corte central) e escreve o recorte do head:
  CW = largura do recorte pra que a caixa Haar do rosto vire ~62 % de 1170 como no controle (limitada a 585–704 → upscale ≤ 2,0×)
  CH = CW×1212/1170 (par) · CX centrado no rosto · OY = olhos − 0,47×CH (olhos a 47 % do painel, como no controle)."""
import sys, subprocess, numpy as np, cv2
src, out = sys.argv[1], sys.argv[2]
if src.lower().endswith(('.png','.jpg')):
    im=cv2.imread(src); h,w=im.shape[:2]; s=1280/h; im=cv2.resize(im,(int(round(w*s)),1280),interpolation=cv2.INTER_AREA)
    x0=(im.shape[1]-704)//2; im=im[:,x0:x0+704]
else:
    raw=subprocess.run(['ffmpeg','-v','error','-i',src,'-vf',"select='eq(n\\,0)'",'-vsync','0','-frames:v','1','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    im=np.frombuffer(raw,np.uint8).reshape(1280,704,3).copy()
g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
face=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
faces=face.detectMultiScale(g,1.05,5,minSize=(120,120)); assert len(faces), 'sem rosto'
x,y,w,h=max(faces,key=lambda f:f[2]*f[3])
eyes=eye.detectMultiScale(g[y:y+int(h*0.6),x:x+w],1.05,4,minSize=(w//10,w//10))
ey=float(np.median([y+e[1]+e[3]/2 for e in eyes])) if len(eyes) else y+0.37*h   # 0,37: posição dos olhos na caixa Haar do controle
frac=w/704
CW=int(round(704*frac/0.62)); CW=max(585,min(704,CW)); CW-=CW%2
CH=int(round(CW*1212/1170)); CH-=CH%2
CX=int(round(x+w/2-CW/2)); CX=max(0,min(704-CW,CX))
OY=int(round(ey-0.47*CH)); OY=max(0,min(1280-CH,OY))
print(f'{src}: rosto Haar x{x}-{x+w} ({100*frac:.1f} % de 704) y{y}-{y+h} · olhos n={len(eyes)} y={ey:.0f} ({100*ey/1280:.1f} %) · queixo {100*(y+h)/1280:.1f} % → CW={CW} CH={CH} CX={CX} OY={OY} · escala {1170/CW:.2f}× · rosto no painel {100*w*1170/CW/1170:.1f} %')
open(out,'w').write(f'CW={CW}\nCH={CH}\nCX={CX}\nOY={OY}\n')
