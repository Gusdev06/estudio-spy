import numpy as np, cv2
from PIL import Image, ImageFont, ImageDraw
im=np.asarray(Image.open('f0000.png').convert('RGB')).astype(np.float32)/255
# box mask from f0
blk=(im.max(2)<6/255).astype(np.uint8); blk[:900]=0
n,l,st,c=cv2.connectedComponentsWithStats(((im.max(2)<6/255)|(im.min(2)>200/255)).astype(np.uint8)*(np.arange(1280)[:,None]>900),8)
box=(l==l[1040,300])
box=cv2.morphologyEx(box.astype(np.uint8),cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
ref=im.min(2)*box  # white text inside box
T=["“Girl, how do I get into my","boyfriend’s Insta without him","knowing?”"]
def block(s,w,p,cx,y0,txt=T):
    c=Image.new('L',(720,1280),0); d=ImageDraw.Draw(c)
    f=ImageFont.truetype('../fontes/OpenSans.ttf',s); f.set_variation_by_axes([w,100])
    for j,t in enumerate(txt):
        L=d.textlength(t,font=f); d.text((cx-L/2,y0+j*p),t,font=f,fill=255)
    return np.asarray(c).astype(np.float32)/255
best=None
R=ref[940:1140]
for s in (39.5,40,40.5,41,41.5):
  for w in (700,725,750,775):
    for p in (61,62,63,64,65):
      for cx in (359,359.5,360,360.5,361):
        for y0 in range(938,960):
          b=block(s,w,p,cx,y0)[940:1140]
          e=np.abs(b-R).mean()
          if best is None or e<best[0]: best=(e,s,w,p,cx,y0)
  print(best,flush=True)
print('BEST',best)
