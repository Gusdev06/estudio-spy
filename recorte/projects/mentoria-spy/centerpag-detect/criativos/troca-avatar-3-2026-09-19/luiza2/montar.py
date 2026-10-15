#!/usr/bin/env python3
# Luiza Cristina 2140730963322005 (360x640, podcast full-frame + caixa de legenda fixa) → avatar novo, saída 1080x1920.
# Look: o original é 360p; o clipe do Pruna passa por 360p e volta (mesma suavidade) + ruído leve. Caixa "# A woman records video…" redesenhada.
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
L='centerpag-detect/criativos/troca-avatar-3-2026-09-19/luiza2'; CLIPE=sys.argv[1]; OUT=sys.argv[2]
REF=f'{L}/REFERENCIA-original.mp4'; AUD=f'{L}/audio/original.m4a'; DUR=26.40; W,H=1080,1920
FP='gram-detect/scripts/fonts/Poppins-Bold.ttf'
# caixa (medida no original ×3): '#' x 0-267 · texto x 303-1080 · y 1512-1731, preto, cantos r=36, texto branco 3 linhas centrado
ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
d.rounded_rectangle([-40,1512,267,1731],radius=36,fill=(8,8,8,235)); d.rounded_rectangle([303,1512,W+40,1731],radius=36,fill=(8,8,8,235))
fh=ImageFont.truetype(FP,150); d.text((133,1615),'#',font=fh,fill='white',anchor='mm')
ft=ImageFont.truetype(FP.replace('Bold','Medium') if os.path.exists(FP.replace('Bold','Medium')) else FP,44)
for i,t in enumerate(['A woman records video','talking about a spy app that','has been gaining popularity!']): d.text((691,1560+i*54),t,font=ft,fill='white',anchor='mm')
ov.save(f'{L}/molde/caixa.png')
vf=(f"[0:v]scale={W}:-2:flags=lanczos,fps=30,crop={W}:{H}:0:(ih-{H})/2,scale=360:640:flags=bicubic,scale={W}:{H}:flags=bicubic,"
    f"eq=saturation=0.95:contrast=0.98,noise=alls=6:allf=t+u[th];[th][1:v]overlay=0:0[v]")
cmd=['ffmpeg','-hide_banner','-v','error','-y','-i',CLIPE,'-i',f'{L}/molde/caixa.png','-i',AUD,'-filter_complex',vf,'-map','[v]','-map','2:a','-c:a','copy','-t',str(DUR),
     '-c:v','libx264','-preset','slow','-crf','20','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT]
subprocess.run(cmd,check=True); print('ok ->',OUT)
