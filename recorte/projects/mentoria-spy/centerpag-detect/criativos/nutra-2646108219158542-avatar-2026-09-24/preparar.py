"""Extract opaque caption artwork without carrying the original face/background."""
from pathlib import Path
import json
import subprocess
import cv2
import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parents[2] / 'downloads/ad-2646108219158542-2026-09-24/nutra-health-2646108219158542-v1.mp4'
OUT = ROOT / 'preparo'
OUT.mkdir(exist_ok=True)
START, END, FPS = 220, 1290, 30
W, H = 360, 640

reader = subprocess.Popen(['ffmpeg','-v','error','-i',str(SOURCE),'-vf',f'trim=start_frame={START}:end_frame={END}',
    '-vsync','0','-f','rawvideo','-pix_fmt','rgb24','-'], stdout=subprocess.PIPE)
writer = subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pixel_format','rgba','-video_size','360x640',
    '-framerate','30','-i','-','-an','-c:v','qtrle',str(OUT/'legendas-alpha.mov')], stdin=subprocess.PIPE)
base = np.array(Image.open(ROOT/'avatar-base.png').convert('RGB').resize((W,H),Image.Resampling.LANCZOS))
timeline=[]
previews=[]
for n in range(START,END):
    raw=reader.stdout.read(W*H*3)
    if len(raw)!=W*H*3:
        raise RuntimeError(f'Incomplete source at frame {n}')
    f=np.frombuffer(raw,np.uint8).reshape(H,W,3)
    layer=np.zeros((H,W,4),np.uint8)
    # Reconstruct visible fine dust in non-face areas as light with transparency,
    # rather than carrying the old sweater or room pixels into the new portrait.
    gray=cv2.cvtColor(f,cv2.COLOR_RGB2GRAY)
    local=cv2.medianBlur(gray,9)
    residual=gray.astype(float)-local.astype(float)
    dust=(residual>28).astype(np.uint8)
    region=np.zeros((H,W),np.uint8)
    region[445:,:]=1
    region[110:330,:85]=1
    region[110:445,315:]=1
    dust*=region
    _,dust_labels,dust_stats,_=cv2.connectedComponentsWithStats(dust,8)
    for label,(dx,dy,dw,dh,da) in enumerate(dust_stats[1:],1):
        if da<=20 and dw<=6 and dh<=12:
            selected=dust_labels[dy:dy+dh,dx:dx+dw]==label
            target=layer[dy:dy+dh,dx:dx+dw]
            target[selected,:3]=255
            diff=residual[dy:dy+dh,dx:dx+dw][selected]
            baseline=local[dy:dy+dh,dx:dx+dw][selected].astype(float)
            target[selected,3]=np.clip(diff/np.maximum(1,255-baseline)*255,0,255).astype(np.uint8)
    # This rectangle contains only the title's opaque white artwork, no background.
    layer[28:100,11:350,:3]=f[28:100,11:350]
    layer[28:100,11:350,3]=255
    roi=f[448:565,5:355]
    lo=roi.min(2);hi=roi.max(2)
    mask=((lo>170)&((hi.astype(int)-lo)<40)).astype(np.uint8)
    count,labels,stats,centers=cv2.connectedComponentsWithStats(mask,8)
    candidates=[]
    for x,y,w,h,area in stats[1:]:
        if w>=45 and h>=18 and area>=450 and area/(w*h)>.40:
            candidates.append([int(x+5),int(y+448),int(w),int(h)])
    box=max(candidates,key=lambda b:b[2]*b[3]) if candidates else None
    if box:
        x,y,w,h=box
        layer[y:y+h,x:x+w,:3]=f[y:y+h,x:x+w]
        layer[y:y+h,x:x+w,3]=255
    writer.stdin.write(layer.tobytes())
    # Recover entry fade from the actual white title pixels. Clip settles by frame 228.
    fade=min(1.0,float(np.median(f[30:39,20:340]))/252) if n<229 else 1.0
    timeline.append({'frame':n,'time':n/FPS,'caption_bbox':box,'fade':fade})
    if n in [221,225,228,360,500,660,900,1100,1289]:
        composed=(base.astype(float)*fade).clip(0,255).astype(np.uint8)
        alpha=layer[:,:,3:4].astype(float)/255
        composed=(composed*(1-alpha)+layer[:,:,:3]*alpha).clip(0,255).astype(np.uint8)
        comparison=Image.new('RGB',(720,672),'#161616')
        comparison.paste(Image.fromarray(f),(0,32));comparison.paste(Image.fromarray(composed),(360,32))
        draw=ImageDraw.Draw(comparison)
        draw.text((12,8),f'Original | frame {n} | {n/FPS:.3f}s',fill='white')
        draw.text((372,8),'Novo avatar | previa estatica',fill='white')
        comparison.save(OUT/f'comparacao-{n}.jpg')
        previews.append((n,composed))
writer.stdin.close()
if writer.wait()!=0 or reader.wait()!=0:
    raise RuntimeError('ffmpeg failed')
(OUT/'timeline.json').write_text(json.dumps({'start_frame':START,'end_frame_exclusive':END,'fps':FPS,
    'duration':(END-START)/FPS,'frames':timeline},indent=2))
subprocess.run(['ffmpeg','-v','error','-y','-i',str(SOURCE),'-vn','-af',f'atrim=start={START/FPS}:end={END/FPS},asetpts=PTS-STARTPTS',
    '-ar','44100','-ac','1','-c:a','pcm_s16le',str(OUT/'audio-avatar.wav')],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(SOURCE),'-vn','-c:a','copy',str(OUT/'audio-original.m4a')],check=True)
print(json.dumps({'frames':len(timeline),'duration':(END-START)/FPS,'caption_frames':sum(x['caption_bbox'] is not None for x in timeline)}))
