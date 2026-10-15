# Compara a saída do remontar.sh (com o campeão como talking head) contra o próprio campeão, bloco a bloco.
import subprocess, numpy as np, sys
from PIL import Image, ImageDraw, ImageFont
CH='criativos-crus/spy-gram/ads-en/GD-AD01.mp4'
OUT=sys.argv[1] if len(sys.argv)>1 else 'gram-detect/criativos/gd-ad01-var-avatar-2026-09-03/conferencia/molde/teste-molde-campeao.mp4'
D='gram-detect/criativos/gd-ad01-var-avatar-2026-09-03/conferencia/molde'; FONT='gram-detect/scripts/fonts/Poppins-Bold.ttf'
W,H=1080,1920
blocks=[(0,234,'A rosto+caixa+painel'),(234,321,'B card Gram Detect'),(321,492,'C1 rosto cheio'),(492,591,'E story'),(591,666,'C2 rosto cheio'),(666,777,'D1 split pill+painel'),(777,876,'C3 rosto cheio'),(876,978,'8 card glitch+setas')]
def stream(p): return subprocess.Popen(['ffmpeg','-v','error','-i',p,'-vf','format=gray','-f','rawvideo','-'],stdout=subprocess.PIPE)
a=stream(CH); b=stream(OUT); n=0; acc={i:[0.0,0.0,0] for i in range(len(blocks))}; worst=[]
while True:
    x=a.stdout.read(W*H); y=b.stdout.read(W*H)
    if len(x)<W*H or len(y)<W*H: break
    gx=np.frombuffer(x,np.uint8).astype(np.int16); gy=np.frombuffer(y,np.uint8).astype(np.int16)
    d=np.abs(gx-gy); bi=[i for i,(s,e,_) in enumerate(blocks) if s<=n<e][0]
    m=float(d.mean()); acc[bi][0]+=m; acc[bi][1]=max(acc[bi][1],m); acc[bi][2]+=1; worst.append((m,n)); n+=1
print(f'frames comparados {n}')
print('bloco                      | diff média (0-255) | pior frame do bloco')
for i,(s,e,name) in enumerate(blocks):
    c=acc[i]; print(f'{name:26s} | {c[0]/max(c[2],1):6.2f}             | {c[1]:6.2f}')
worst.sort(reverse=True); print('10 piores frames (diff, n, t):',[(round(m,1),k,round(k/30,2)) for m,k in worst[:10]])
# lado a lado
def grab(src,t,out): subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',src,'-frames:v','1',out],check=True)
def label(im,txt):
    d=ImageDraw.Draw(im); f=ImageFont.truetype(FONT,40); d.rectangle([0,0,im.width,64],fill=(0,0,0)); d.text((16,10),txt,font=f,fill=(255,255,255)); return im
tiles=[]
for t in [1,3,9,13,17.5,24,27.5,31]:
    grab(CH,t,f'{D}/t{t}-campeao.png'); grab(OUT,t,f'{D}/t{t}-molde.png')
    ca=label(Image.open(f'{D}/t{t}-campeao.png').convert('RGB'),f'campeao t={t}s'); mo=label(Image.open(f'{D}/t{t}-molde.png').convert('RGB'),f'molde t={t}s')
    pair=Image.new('RGB',(1080*2+16,1920),(20,20,20)); pair.paste(ca,(0,0)); pair.paste(mo,(1096,0)); pair.save(f'{D}/lado-a-lado-t{t}s.png'); tiles.append(pair.resize((544,480)))
sheet=Image.new('RGB',(544*4+30,480*2+30),(0,0,0))
for i,tl in enumerate(tiles): sheet.paste(tl,((i%4)*554,(i//4)*500))
sheet.save(f'{D}/folha-molde.png'); print('imagens em',D)
