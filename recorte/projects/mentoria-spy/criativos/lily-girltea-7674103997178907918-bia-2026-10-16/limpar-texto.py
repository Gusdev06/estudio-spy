# O Seedance 2.5 NÃO removeu o texto do original neste reel (ficou no clipe, no mesmo lugar, ±1 px).
# Como o texto redesenhado em Helvetica não cobre os glifos do original (fonte do TikTok) letra por letra,
# sobrava contorno fantasma. Aqui o texto do clipe é apagado por inpainting (OpenCV TELEA) antes do overlay.
# Máscara: pixels claros e estáveis em TODOS os frames do ORIGINAL (lá a camiseta é preta, então só o texto passa;
# no clipe a camisa branca da Bia também é clara e estável e entrava na máscara). O texto do clipe está no mesmo lugar (±1 px).
import subprocess, numpy as np, cv2
W,H=1080,1920
def frames(path):
    p=subprocess.Popen(['ffmpeg','-v','error','-i',path,'-vf',f'scale={W}:{H}:flags=lanczos','-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
    while True:
        b=p.stdout.read(W*H*3)
        if len(b)<W*H*3: break
        yield np.frombuffer(b,np.uint8).reshape(H,W,3)
O=list(frames('original/original-h264.mp4'))
A=np.stack(O).astype(np.int16); del O
mn=A.min(0); mx=A.max(0)
m=((mn.mean(2)>200)&((mx-mn).max(2)<70)).astype(np.uint8)*255
faixa=np.zeros_like(m); faixa[660:1070,145:945]=1; m*=faixa
m=cv2.dilate(m,np.ones((7,7),np.uint8))
F=list(frames('clipes/bia.mp4'))
cv2.imwrite('legendas/mascara-texto-clipe.png',m)
out=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','24','-i','-',
    '-c:v','libx264','-crf','12','-preset','slow','-pix_fmt','yuv420p','clipes/bia-limpo.mp4'],stdin=subprocess.PIPE)
for f in F: out.stdin.write(cv2.inpaint(np.ascontiguousarray(f),m,6,cv2.INPAINT_TELEA).tobytes())
out.stdin.close(); out.wait(); print('frames',len(F),'pixels mascara',int((m>0).sum()))
