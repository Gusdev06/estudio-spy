#!/usr/bin/env python3
# Estatísticas do painel do rosto (x 0-354): nitidez laplaciana, ruído em blocos lisos, luma, contraste, saturação, média RGB. Uso: python3 medir.py a.mp4 [b.mp4 …]
import subprocess, sys, numpy as np
def med(f):
    raw=subprocess.run(['ffmpeg','-hide_banner','-v','error','-i',f,'-vf','select=not(mod(n\\,30)),crop=354:720:0:0','-vsync','0','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    c=np.frombuffer(raw,np.uint8).reshape(-1,720,354,3).astype(float); L=c.mean(axis=3)
    lap=np.abs(L[:,1:-1,1:-1]*4-L[:,:-2,1:-1]-L[:,2:,1:-1]-L[:,1:-1,:-2]-L[:,1:-1,2:]).mean()
    b=L[:,:720,:352].reshape(len(L),90,8,44,8).std(axis=(2,4))
    return dict(nitidez=round(lap,2),ruido_p5=round(np.percentile(b,5),2),ruido_med=round(np.median(b),2),luma=round(L.mean(),1),contraste=round(L.std(),1),sat=round((c.max(axis=3)-c.min(axis=3)).mean(),1),rgb=c.mean(axis=(0,1,2)).round(0).tolist())
for f in sys.argv[1:]: print(f.split('/')[-1][:28].ljust(28), med(f))
