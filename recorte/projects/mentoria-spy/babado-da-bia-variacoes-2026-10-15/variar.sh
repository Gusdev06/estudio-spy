#!/bin/zsh
# uso: variar.sh <base> <frase> <saida.mp4>   (roda da pasta mentoria-spy)
B=$1; T=$2; OUT=$3; DIR=$(dirname $0)
read CLIP AUD CY <<< $(python3 -c "import json,sys;b=json.load(open('$DIR/bases.json'))['$B'];print(b['clip'],b['audio'],b['cy'])")
PNG=$DIR/legendas-png/$(basename $OUT .mp4).png
python3 -c "
import sys
from PIL import Image, ImageDraw, ImageFont
t,saida,cy=sys.argv[1],sys.argv[2],int(sys.argv[3])
p='/System/Library/Fonts/HelveticaNeue.ttc'
idx=next(i for i in range(14) if ImageFont.truetype(p,60,index=i).getname()[1]=='Medium')
f=ImageFont.truetype(p,78,index=idx)
L=[];c=''
for w in t.split():
  s=(c+' '+w).strip()
  if f.getbbox(s)[2]-f.getbbox(s)[0]<=800: c=s
  else: L.append(c); c=w
L.append(c)
im=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im); a=f.getbbox('E')[1]; top=cy-(len(L)*97)//2
for i,l in enumerate(L):
  b=f.getbbox(l); d.text(((1080-(b[2]-b[0]))//2-b[0], top+i*97-a), l, font=f, fill=(249,240,167,255))
im.save(saida)
" "$T" $PNG $CY
ffmpeg -v error -y -i $CLIP -i $PNG -i $AUD -filter_complex "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1[v];[v][1:v]overlay=0:0[o]" -map "[o]" -map 2:a -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart $OUT && echo "ok $OUT"
