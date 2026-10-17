import numpy as np
from PIL import Image, ImageFont, ImageDraw
import cv2
ref=cv2.imread('f0000.png')[:,:,1]
refc=(ref[960:1012,90:630]>160).astype(np.float32)
T1="“Girl, how do I get into my"
T2="boyfriend’s Insta without him"
F={'tiktok':'../fontes/TikTokSans.ttf','mont':'../fontes/Montserrat.ttf',
 'helvB':'/System/Library/Fonts/HelveticaNeue.ttc','arialB':'/System/Library/Fonts/Supplemental/Arial Bold.ttf',
 'sf':'/System/Library/Fonts/SFNS.ttf','avenir':'/System/Library/Fonts/Avenir Next.ttc',
 'inter':'/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/PACOTE-ESTEIRA-CRIATIVOS/fontes/Inter-Bold.ttf',
 'poppins':'/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/PACOTE-ESTEIRA-CRIATIVOS/fontes/Poppins-Bold.ttf'}
def mk(path,size,var=None,idx=0):
    f=ImageFont.truetype(path,size,index=idx)
    if var:
        try: f.set_variation_by_axes(var)
        except Exception as e: f.set_variation_by_name(var)
    return f
def score(f):
    im=Image.new('L',(800,120),0); d=ImageDraw.Draw(im); d.text((10,20),T1,font=f,fill=255)
    a=np.asarray(im)>128; ys=np.where(a.any(1))[0]; xs=np.where(a.any(0))[0]
    im2=Image.new('L',(800,120),0); d=ImageDraw.Draw(im2); d.text((10,20),T2,font=f,fill=255)
    b=np.asarray(im2)>128; xs2=np.where(b.any(0))[0]
    return xs.max()-xs.min(), xs2.max()-xs2.min(), a
import sys
for name,path in F.items():
  for var in ([None] if name not in('tiktok','mont') else ([[36,100,w,0] for w in (600,700,800)] if name=='tiktok' else [[w] for w in (600,700,800)])):
    for idx in ([0] if not path.endswith('.ttc') else range(0,12)):
      try:
        best=None
        for s in range(30,48):
          f=mk(path,s,var,idx); w1,w2,_=score(f)
          e=abs(w1-526)+abs(w2-596)
          if best is None or e<best[0]: best=(e,s,w1,w2)
        fn=ImageFont.truetype(path,20,index=idx).getname()
        print(name,idx,fn,var,best)
      except Exception as ex: pass
