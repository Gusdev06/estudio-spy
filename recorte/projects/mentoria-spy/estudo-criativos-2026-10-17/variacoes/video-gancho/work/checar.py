# Confere frame a frame (0-93) que a placa certa esta na tela e nada do "Done!..." (x58-660, y160-240) vaza.
import subprocess, sys, numpy as np
from PIL import Image
def frames(path, n):
    raw=subprocess.run(['ffmpeg','-v','error','-i',path,'-frames:v',str(n),'-fps_mode','passthrough','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,1280,720,3)
def mask(png):
    p=np.array(Image.open(png)); m=(p[...,3]==255)&(p[...,:3].max(-1)<5); z=np.zeros_like(m); z[160:241,58:661]=True; return m&z
video,p1,p2=sys.argv[1:4]
fr=frames(video,94); m1,m2=mask(p1),mask(p2); bad=[]
for n,f in enumerate(fr):
    m=m1 if n<50 else m2
    hits=int((f.max(-1)[m]>60).sum())
    if hits>20: bad.append((n,hits))
print(video.split('/')[-1], len(fr),'frames | frames com problema:', bad or 'nenhum')
