# Varredura frame a frame: onde a peça tem pixel IGUAL ao original (|dif|<8 nos 3 canais) fora das zonas que são do original de propósito
# (painel do app x128-591 y231-1048 nos trechos de painel; painel de baixo no split 309-428). Sobra esperada: só legenda/título/CTA
# (glifos copiados) e coincidência de cor em fundo escuro. Salva conferencia/iguais.jpg com os 8 piores frames (vermelho = igual).
import subprocess, numpy as np, os, json
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=720,1280
def src(p): return subprocess.Popen(['ffmpeg','-v','error','-i',p,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
A=src('REFERENCIA-original.mp4'); B=src('pecas/variacao.mp4'); res=[]; keep={}
for n in range(1380):
    a=np.frombuffer(A.stdout.read(W*H*3),np.uint8).reshape(H,W,3).astype(np.int16); b=np.frombuffer(B.stdout.read(W*H*3),np.uint8).reshape(H,W,3).astype(np.int16)
    eq=(np.abs(a-b).max(2)<8)
    z=np.zeros((H,W),bool)
    if 309<=n<=428: z[{426:856,427:850,428:850}.get(n,862):]=True
    if 429<=n<=641 or 828<=n<=1186: z[231:1049,128:592]=True
    if n<=308: z[:112]=True                      # faixa preta
    lum=a.max(2)
    e=eq&~z&(lum>40)                             # ignora preto chapado (coincidência)
    res.append(int(e.sum())); keep[n]=(e,a.astype(np.uint8),b.astype(np.uint8))
    if len(keep)>40: 
        k=min(keep,key=lambda m:res[m]); del keep[k]
json.dump(res,open('conferencia/varredura-iguais.json','w'))
r=np.array(res); print('frames:',len(r),'pixels iguais por frame: mediana',int(np.median(r)),'max',r.max(),'em n',int(r.argmax()))
for seg,(i,j) in {'esquete':(0,308),'split':(309,428),'painel1':(429,641),'homem1':(642,827),'painel2':(828,1186),'homem2':(1187,1379)}.items():
    print(seg, 'max',r[i:j+1].max(),'n',i+int(r[i:j+1].argmax()),'mediana',int(np.median(r[i:j+1])))
top=sorted(keep,key=lambda m:-res[m])[:8]; tiles=[]
for n in sorted(top):
    e,a,b=keep[n]; v=b.copy(); v[e]=(255,0,0); tiles.append(np.concatenate([a,v],0))
im=Image.fromarray(np.concatenate(tiles,1)).resize((240*len(tiles),854)); im.save('conferencia/iguais.jpg',quality=85); print('piores:',sorted(top))
