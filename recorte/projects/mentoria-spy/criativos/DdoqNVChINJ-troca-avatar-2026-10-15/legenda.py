# Legenda no estilo do molde (Helvetica Neue Medium, RGB 249,240,167, sem sombra; padrão 78px/pitch 97px).
# Linhas separadas por "|" pra copiar as quebras do original; args: texto saida [centro_y=1040] [tamanho=78] [pitch=97].
import sys
from PIL import Image, ImageDraw, ImageFont
texto, saida = sys.argv[1], sys.argv[2]; cy = int(sys.argv[3]) if len(sys.argv) > 3 else 1040
sz = int(sys.argv[4]) if len(sys.argv) > 4 else 78; pitch = int(sys.argv[5]) if len(sys.argv) > 5 else 97
path='/System/Library/Fonts/HelveticaNeue.ttc'
idx=next(i for i in range(14) if ImageFont.truetype(path,60,index=i).getname()[1]=='Medium')
f=ImageFont.truetype(path,sz,index=idx)
linhas=[l.strip() for l in texto.split('|')]
W,H=1080,1920; top=cy-(len(linhas)*pitch)//2
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); a=f.getbbox("E")[1]
for i,t in enumerate(linhas):
    b=f.getbbox(t); d.text(((W-(b[2]-b[0]))//2-b[0], top+i*pitch-a), t, font=f, fill=(249,240,167,255))
im.save(saida); print(linhas)
