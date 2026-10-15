# Folha de conferência: original | peça lado a lado nos frames pedidos (uso: python3 folha.py saida.jpg n1 n2 ...)
import subprocess,sys,numpy as np,cv2
out=sys.argv[1]; ns=[int(x) for x in sys.argv[2:]]
def fr(p,n): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-vf',f'select=eq(n\\,{n})','-vsync','0','-frames:v','1','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout,np.uint8).reshape(720,960,3)
rows=[]
for n in ns:
    a,b=[cv2.resize(fr(p,n),(400,300)) for p in ['REFERENCIA-original.mp4','pecas/variacao.mp4']]
    r=np.hstack([a,np.full((300,6,3),255,np.uint8),b]); cv2.putText(r,f'n{n} {n/30:.2f}s',(8,28),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2); rows.append(r)
cols=2; rows+= [np.zeros_like(rows[0])]*((-len(rows))%cols)
g=np.vstack([np.hstack([rows[i+j] if j==0 else np.hstack([np.full((300,14,3),0,np.uint8),rows[i+j]]) for j in range(cols)]) for i in range(0,len(rows),cols)])
cv2.imwrite(out,g,[cv2.IMWRITE_JPEG_QUALITY,85])
