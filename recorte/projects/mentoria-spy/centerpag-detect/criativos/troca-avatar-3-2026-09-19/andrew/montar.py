#!/usr/bin/env python3
# Andrew Smith 4680506465505714 (720x1280: bloco de citação branco no topo, janela 720x584 do vídeo em y 352-936, lower third azul 0,4-3,0 s,
# faixa vermelha de CTA embaixo; cutaways do app em quadro cheio 14,4-33,4 s; card final) → avatar novo só na janela nos dois blocos de rosto
# (0,2-14,4 s e 33,4-53,6 s), saída 1080x1920 = original ×1,5. Lower third REDESENHADO (medido: azul (3,65,165) y 754-909, barras vermelhas, texto branco 2 linhas cortado nas bordas).
import subprocess, sys
from PIL import Image, ImageDraw, ImageFont
D='centerpag-detect/criativos/troca-avatar-3-2026-09-19/andrew'; P1,P2=sys.argv[1],sys.argv[2]; OUT=sys.argv[3]
REF=f'{D}/REFERENCIA-original.mp4'; W,H=1080,1920; WY,WH=528,876
A0,A1,B0,B1=0.2,14.4,33.4,53.6; LT0,LT1=0.4,3.0
FM='gram-detect/criativos/ad02-h2-reconstrucao-2026-09-17/fontes/Montserrat-Variable.ttf'
ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
d.rectangle([0,1131,W,1364],fill=(3,65,165,255))                 # banda azul
d.rectangle([450,1102,W,1117],fill=(215,20,25,255)); d.rectangle([450,1380,W,1395],fill=(215,20,25,255)); d.rectangle([0,1102,22,1150],fill=(215,20,25,255))
f=ImageFont.truetype(FM,76); f.set_variation_by_name('ExtraBold')
d.text((-12,1150),"HOW TO SPY ON YOUR",font=f,fill='white'); d.text((-12,1246),"PARTNER'S TEXT MESSAGES",font=f,fill='white')
ov.save(f'{D}/molde/lower-third.png')
look="gblur=sigma=0.8,eq=saturation=0.95:contrast=0.98,noise=alls=8:allf=t+u"
vf=(f"[0:v]scale={W}:{H}:flags=lanczos,fps=30[base];"
    f"[1:v]trim=end={A1-A0:.2f},setpts=PTS-STARTPTS,fps=30,scale=-2:{WH}:flags=lanczos,crop={W}:{WH}:(iw-{W})/2:0,{look},format=rgba,tpad=start_duration={A0}:start_mode=add:color=0x00000000[ta];"
    f"[2:v]trim=end={B1-B0:.2f},setpts=PTS-STARTPTS,fps=30,scale=-2:{WH}:flags=lanczos,crop={W}:{WH}:(iw-{W})/2:0,{look},format=rgba,tpad=start_duration={B0}:start_mode=add:color=0x00000000[tb];"
    f"[base][ta]overlay=0:{WY}:eof_action=pass:enable='between(t,{A0},{A1})'[v1];[v1][tb]overlay=0:{WY}:eof_action=pass:enable='between(t,{B0},{B1})'[v2];"
    f"[v2][3:v]overlay=0:0:eof_action=pass:enable='between(t,{LT0},{LT1})'[v]")
cmd=['ffmpeg','-hide_banner','-v','error','-y','-i',REF,'-i',P1,'-i',P2,'-loop','1','-framerate','30','-t','3.5','-i',f'{D}/molde/lower-third.png','-filter_complex',vf,'-map','[v]','-map','0:a','-c:a','copy',
     '-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT]
subprocess.run(cmd,check=True); print('ok ->',OUT)
