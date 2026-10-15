#!/usr/bin/env python3
# Redesenha o selo vermelho do Secret Revealed com uma headline nova (2 linhas). Medido no original (1080x1920):
# caixas #B40000 (180,0,1) ocupando y 176–384, x 135–939; letra branca condensada pesada, caixa alta.
# Uso: python3 fazer-selo.py "LINHA 1" "LINHA 2" saida.png
import sys
from PIL import Image, ImageDraw, ImageFont
L1,L2,OUT=sys.argv[1],sys.argv[2],sys.argv[3]
W,H=1080,1920; FONTE='gram-detect/criativos/ad02-h2-reconstrucao-2026-09-17/fontes/Anton-Regular.ttf'
TOPO,BASE=176,384; VERM=(180,0,1,255); LARG_MAX=820      # a caixa mais larga do original mede 804 px
alt_caixa=(BASE-TOPO)//2                                  # 104 px por linha
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
def fonte_para(txt):
    for sz in range(110,30,-1):
        f=ImageFont.truetype(FONTE,sz)
        if f.getlength(txt)<=LARG_MAX and (f.getbbox('H')[3]-f.getbbox('H')[1])<=alt_caixa-26: return f
    return ImageFont.truetype(FONTE,40)
linhas=[L1.upper(),L2.upper()]
f=min((fonte_para(t) for t in linhas),key=lambda x:x.size)   # mesmo corpo nas duas linhas, como no original
for i,txt in enumerate(linhas):
    lw=f.getlength(txt); bb=f.getbbox('H'); cap=bb[3]-bb[1]
    y0=TOPO+i*alt_caixa; cx=W//2
    d.rectangle([cx-lw/2-26,y0,cx+lw/2+26,y0+alt_caixa],fill=VERM)
    d.text((cx-lw/2,y0+(alt_caixa-cap)//2-bb[1]),txt,font=f,fill=(255,255,255,255))
im.save(OUT); print('ok',OUT)
