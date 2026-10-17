import numpy as np, cv2
from PIL import Image, ImageFont, ImageDraw
ref=Image.open('f0000.png').crop((60,955,660,1075))
T=["“Girl, how do I get into my","boyfriend’s Insta without him"]
C=[('../fontes/TikTokSans.ttf',0,[36,100,700,0],45),('../fontes/TikTokSans.ttf',0,[36,100,800,0],44),('/System/Library/Fonts/HelveticaNeue.ttc',1,None,43),('/System/Library/Fonts/Supplemental/Arial Bold.ttf',0,None,43),('/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/PACOTE-ESTEIRA-CRIATIVOS/fontes/Inter-Bold.ttf',0,None,42),('../fontes/Montserrat.ttf',0,[700],39)]
out=Image.new('RGB',(600,120*(len(C)+1)),'black'); out.paste(ref,(0,0))
for k,(p,i,v,s) in enumerate(C):
    f=ImageFont.truetype(p,s,index=i)
    if v: f.set_variation_by_axes(v)
    d=ImageDraw.Draw(out); y=120*(k+1)
    for j,t in enumerate(T):
        w=d.textlength(t,font=f); d.text((300-w/2,y+5+j*64),t,font=f,fill='white')
    d.text((2,y+2),str(k),fill='red')
out.save('../conferencia/_fonts.png')
