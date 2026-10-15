# stats fora do flash + imagem dos piores frames com máscara "igual" em magenta
import subprocess, numpy as np, json, sys, cv2
sys.path.insert(0,'.')
from cards import Compositor
import flash
FP=json.load(open('work/flash-params.json')); comp=Compositor(); G=np.load('work/G.npy',mmap_mode='r')
p=subprocess.Popen(['ffmpeg','-v','error','-i','pecas/variacao.mp4','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
res=[];keep={}
for n in range(1822):
    x=np.frombuffer(p.stdout.read(1280*720*3),np.uint8).reshape(1280,720,3); o=G[n]
    same=(np.abs(x.astype(np.int16)-o).max(2)<10); cm=flash.cardmask(comp,n)
    if 1060<=n<=1239: cm[772:]=True
    if 1364<=n<=1460: cm[826:1202,108:612]=True
    free=~cm&~(o.min(2)>225); fr=same[free].mean()
    res.append((n,fr,str(n) in FP))
    if str(n) not in FP and n%10==0: keep[n]=(x.copy(),same&free)
r=[a for a in res if not a[2]]; v=np.array([a[1] for a in r])
print('fora do flash: média %.4f máx %.4f em n%d'%(v.mean(),v.max(),r[int(v.argmax())][0]))
worst=sorted(keep,key=lambda n:-res[n][1])[:4]
tiles=[]
for n in worst:
    x,m=keep[n]; a=cv2.cvtColor(np.ascontiguousarray(G[n]),cv2.COLOR_RGB2BGR); b=cv2.cvtColor(x,cv2.COLOR_RGB2BGR).copy(); b[m]=(255,0,255)
    t=np.vstack([a,b]); t=cv2.resize(t,(270,960)); cv2.putText(t,f'n{n} {res[n][1]:.3f}',(4,20),0,0.6,(0,255,255),2); tiles.append(t)
cv2.imwrite('conferencia/varredura-piores-fora-flash.jpg',np.hstack(tiles),[cv2.IMWRITE_JPEG_QUALITY,85])
