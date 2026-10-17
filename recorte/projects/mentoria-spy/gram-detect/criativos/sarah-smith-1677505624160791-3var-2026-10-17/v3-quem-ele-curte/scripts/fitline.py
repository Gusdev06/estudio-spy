import numpy as np, cv2
from PIL import Image, ImageFont, ImageDraw
exec(open('../scripts/fitblock.py').read().split('T=[')[0])
T=["“Girl, how do I get into my","boyfriend’s Insta without him","knowing?”"]
yr=[(945,1015),(1005,1080),(1075,1135)]
for j,t in enumerate(T):
  R=ref[yr[j][0]:yr[j][1]]
  best=None
  for s in np.arange(38,43.1,0.5):
    for w in (650,700,750,800):
      f=ImageFont.truetype('../fontes/OpenSans.ttf',s); f.set_variation_by_axes([w,100])
      for cx in np.arange(358,362.1,0.5):
        for y in range(yr[j][0]-20,yr[j][0]+15):
          c=Image.new('L',(720,1280),0); d=ImageDraw.Draw(c); L=d.textlength(t,font=f); d.text((cx-L/2,y),t,font=f,fill=255)
          b=np.asarray(c)[yr[j][0]:yr[j][1]].astype(np.float32)/255
          e=np.abs(b-R).mean()
          if best is None or e<best[0]: best=(round(float(e),4),s,w,cx,y)
  print(j,best,flush=True)
