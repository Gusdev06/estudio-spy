# Texto fixo da série no padrão dos virais FollowSpy: branco, Helvetica Neue Medium, centralizado no meio da tela,
# quebra automática em ~820 px, sombra mais forte que a das réplicas (fundo claro em alguns looks).
# uso: python3 texto.py <pasta>   (lê <pasta>/legendas/texto.txt, grava <pasta>/legendas/texto.png)
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
pasta=sys.argv[1]
H='/System/Library/Fonts/HelveticaNeue.ttc'
idx=next(i for i in range(14) if ImageFont.truetype(H,60,index=i).getname()[1]=='Medium')
K=2; f=ImageFont.truetype(H,58*K,index=idx); LARG=820*K; ESP=int(58*K*1.22)
linhas=[]
for par in open(f'{pasta}/legendas/texto.txt').read().strip().split('\n'):
    if not par.strip(): linhas.append(''); continue
    cur=''
    for w in par.split():
        t=(cur+' '+w).strip()
        if f.getbbox(t)[2]<=LARG: cur=t
        else: linhas.append(cur); cur=w
    linhas.append(cur)
alt=sum(ESP if l else ESP//2 for l in linhas)
y=(1920*K-alt)//2-60*K
big=Image.new('RGBA',(1080*K,1920*K),(0,0,0,0)); d=ImageDraw.Draw(big)
for l in linhas:
    if l:
        b=f.getbbox(l); d.text(((1080*K-(b[2]-b[0]))//2-b[0],y),l,font=f,fill=(255,255,255,255)); y+=ESP
    else: y+=ESP//2
txt=big.resize((1080,1920),Image.LANCZOS)
sh=Image.new('RGBA',txt.size,(0,0,0,0)); sh.putalpha(txt.getchannel('A').point(lambda a:int(a*0.85)))
sh=sh.filter(ImageFilter.GaussianBlur(4))
out=Image.new('RGBA',txt.size,(0,0,0,0)); out.alpha_composite(sh,(2,3)); out.alpha_composite(sh,(0,0)); out.alpha_composite(txt)
out.save(f'{pasta}/legendas/texto.png'); print(pasta,len(linhas),'linhas')
