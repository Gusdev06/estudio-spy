import numpy as np, cv2
from PIL import Image, ImageFont, ImageDraw
im0=cv2.imread('f0000.png').astype(np.float32)/255
g=im0.min(2)
lines=[("“Girl, how do I get into my",(949,1004,79,641)),("boyfriend’s Insta without him",(1004,1077,42,678))]
refs=[]
for t,(y0,y1,x0,x1) in lines:
    r=g[y0+6:y1,x0+12:x1-12]; m=r>0.6; ys=np.where(m.any(1))[0]; xs=np.where(m.any(0))[0]
    refs.append((t,r[ys.min():ys.max()+1,xs.min():xs.max()+1]))
def render(f,t):
    im=Image.new('L',(900,160),0); d=ImageDraw.Draw(im); d.text((20,30),t,font=f,fill=255)
    a=np.asarray(im).astype(np.float32)/255; m=a>0.6; ys=np.where(m.any(1))[0]; xs=np.where(m.any(0))[0]
    return a[ys.min():ys.max()+1,xs.min():xs.max()+1]
def sc(f):
    tot=0
    for t,r in refs:
        a=render(f,t)
        a=cv2.resize(a,(r.shape[1],r.shape[0]),interpolation=cv2.INTER_AREA)
        tot+=np.abs(a-r).mean()
    return tot
res=[]
for name,p,axes in [('opensans','../fontes/OpenSans.ttf','ws'),('tiktok','../fontes/TikTokSans.ttf','t')]:
  for w in range(600,851,50):
    for wd in ([75,87.5,100] if name=='opensans' else [95,100,105,110,115]):
      for s in [40,42,44,46]:
        f=ImageFont.truetype(p,s)
        f.set_variation_by_axes([w,wd] if name=='opensans' else [36,wd,w,0])
        # also check native width ratio
        a=render(f,refs[0][0]); 
        res.append((sc(f),name,w,wd,s,a.shape))
res.sort()
for r in res[:12]: print(r)
print([ (t,r.shape) for t,r in refs])
