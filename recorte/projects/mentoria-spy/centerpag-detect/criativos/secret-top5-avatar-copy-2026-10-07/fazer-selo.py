#!/usr/bin/env python3
# Redesenha o selo vermelho do Secret Revealed com uma headline nova (2 linhas). Base: fazer-selo.py de secret-hook-agressivo-2026-09-23
# (caixas #B40000 em y 176–384, largura máx. 820 px, Anton branco caixa alta, mesmo corpo nas duas linhas).
# Novo aqui: se a linha tiver 📱, o emoji (Apple Color Emoji) entra no fim dela, maior que a caixa e vazando pra cima, como na faixa da 77
# (medido no original 720p: emoji y 102–190 com caixa a partir de y 116 → ×1,5: ~130 px de altura, topo ~23 px acima da caixa).
# Uso (de projects/mentoria-spy/): python3 fazer-selo.py "LINHA 1" "LINHA 2" saida.png
import sys
from PIL import Image, ImageDraw, ImageFont
L1,L2,OUT=sys.argv[1],sys.argv[2],sys.argv[3]
W,H=1080,1920; FONTE='gram-detect/criativos/ad02-h2-reconstrucao-2026-09-17/fontes/Anton-Regular.ttf'
TOPO,BASE=176,384; VERM=(180,0,1,255); LARG_MAX=820; EMO='📱'; EMO_H=130; EMO_SOBE=23
alt_caixa=(BASE-TOPO)//2
em=ImageFont.truetype('/System/Library/Fonts/Apple Color Emoji.ttc',160); ei=Image.new('RGBA',(160,160),(0,0,0,0))
ImageDraw.Draw(ei).text((0,0),EMO,font=em,embedded_color=True); ei=ei.crop(ei.getbbox()); ei=ei.resize((round(ei.width*EMO_H/ei.height),EMO_H),Image.LANCZOS)
def partes(t):
    t=t.upper(); tem=EMO in t; return t.replace(EMO,'').strip(), tem
def larg(f,t,tem): return f.getlength(t)+((ei.width*0.8+16) if tem else 0)
def fonte_para(t,tem):
    for sz in range(110,30,-1):
        f=ImageFont.truetype(FONTE,sz)
        if larg(f,t,tem)<=LARG_MAX and (f.getbbox('H')[3]-f.getbbox('H')[1])<=alt_caixa-26: return f
    return ImageFont.truetype(FONTE,40)
linhas=[partes(L1),partes(L2)]
f=min((fonte_para(t,e) for t,e in linhas),key=lambda x:x.size)
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); emos=[]
for i,(txt,tem) in enumerate(linhas):
    tw=f.getlength(txt); lw=larg(f,txt,tem); bb=f.getbbox('H'); cap=bb[3]-bb[1]; y0=TOPO+i*alt_caixa; x0=W//2-lw/2
    d.rectangle([x0-26,y0,x0+lw+26-(ei.width*0.35 if tem else 0),y0+alt_caixa],fill=VERM)
    d.text((x0,y0+(alt_caixa-cap)//2-bb[1]),txt,font=f,fill=(255,255,255,255))
    if tem: emos.append((int(x0+tw+16),y0-EMO_SOBE))
for x,y in emos: im.alpha_composite(ei,(x,y))      # emoji por cima das duas caixas
im.save(OUT); print('ok',OUT,f.size)
