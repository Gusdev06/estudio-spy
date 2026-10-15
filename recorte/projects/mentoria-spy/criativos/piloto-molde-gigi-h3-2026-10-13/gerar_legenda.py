# Legenda no estilo do molde: Helvetica Neue Medium 78px, cor (249,240,167), sem sombra,
# linhas de no máximo ~800px, centradas, pitch 97px, bloco centrado em y≈1040.
import sys
from PIL import Image, ImageDraw, ImageFont
texto, saida = sys.argv[1], sys.argv[2]
path='/System/Library/Fonts/HelveticaNeue.ttc'
idx=next(i for i in range(14) if ImageFont.truetype(path,60,index=i).getname()[1]=='Medium')
f=ImageFont.truetype(path,78,index=idx)
def larg(t): b=f.getbbox(t); return b[2]-b[0]
linhas=[]; cur=''
for w in texto.split():
    t=(cur+' '+w).strip()
    if larg(t)<=800: cur=t
    else: linhas.append(cur); cur=w
linhas.append(cur)
W,H=1080,1920; pitch=97; top=1040-(len(linhas)*pitch)//2
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); a=f.getbbox("E")[1]
for i,t in enumerate(linhas):
    b=f.getbbox(t); d.text(((W-(b[2]-b[0]))//2-b[0], top+i*pitch-a), t, font=f, fill=(249,240,167,255))
im.save(saida); print(linhas)
