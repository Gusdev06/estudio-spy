import numpy as np, cv2
from PIL import Image, ImageFont, ImageDraw
T=cv2.imread('f0200.png').astype(np.float32)/255
R=(T.min(2)[880:945,150:560]>0.9).astype(np.float32)
TXT="Copy his @ and use"
def draw(f,t,x,y,track,d):
    for ch in t:
        d.text((x,y),ch,font=f,fill=255); x+=f.getlength(ch)+track
    return x
def width(f,t,track): return sum(f.getlength(c) for c in t)+track*(len(t)-1)
best=None
for w in (700,800,900):
  for s in np.arange(33,41,0.5):
    f=ImageFont.truetype('../fontes/Montserrat.ttf',s); f.set_variation_by_axes([w])
    for tr in (-3,-2.5,-2,-1.5,-1,-0.5):
      W=width(f,TXT,tr)
      for cx in np.arange(353,358.1,0.5):
        for y in range(880,900):
          im=Image.new('L',(720,1280),0); d=ImageDraw.Draw(im); draw(f,TXT,cx-W/2,y,tr,d)
          b=(np.asarray(im)[880:945,150:560]>128).astype(np.float32)
          e=np.abs(b-R).mean()
          if best is None or e<best[0]: best=(round(float(e),4),w,float(s),tr,float(cx),y)
  print(best,flush=True)
