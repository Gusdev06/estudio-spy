import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont
F="/System/Library/Fonts/Supplemental/Arial Bold.ttf"
def shot(f, t, w=300):
    p="/tmp/_r.png"
    subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',f,'-frames:v','1','-vf',f'scale={w}:-1',p,'-y'],capture_output=True)
    return Image.open(p).convert('RGB')
outs=[]
for spec in sys.argv[2:]:
    f,t = spec.rsplit('@',1)
    im=shot(f,float(t))
    W,H=im.size
    canvas=Image.new('RGB',(W+52,H),'white'); canvas.paste(im,(52,0))
    d=ImageDraw.Draw(canvas); fnt=ImageFont.truetype(F,11)
    for pct in range(0,101,5):
        y=int(H*pct/100); y=min(y,H-1)
        big = pct%10==0
        d.line([(52,y),(W+52,y)], fill=(255,0,255) if big else (0,255,255), width=1)
        if big: d.text((4,max(0,y-6)), f"{pct}%", fill='black', font=fnt)
    d.text((4,H-14), os.path.basename(f)[:8], fill='#555', font=fnt)
    outs.append(canvas)
Wt=sum(o.width+6 for o in outs); Ht=max(o.height for o in outs)
sheet=Image.new('RGB',(Wt,Ht),'white'); x=0
for o in outs: sheet.paste(o,(x,0)); x+=o.width+6
sheet.save(sys.argv[1]); print(sheet.size)
