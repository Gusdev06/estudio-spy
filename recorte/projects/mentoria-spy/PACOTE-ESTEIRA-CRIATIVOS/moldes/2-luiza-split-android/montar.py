#!/usr/bin/env python3
# Troca de avatar no criativo "Luiza Cristina" (720x720 = talking head à esquerda, x 0-354, + funil à direita) com LOOK DE CELULAR
# ANDROID: o clipe limpo do Pruna passa por ruído de sensor, leve perda de nitidez, cor de câmera frontal barata e bitrate baixo,
# calibrados contra o original (nitidez laplaciana 5,2 · ruído p5 0,73 · 578 kbps). Direita e áudio: os do original.
# Uso (de projects/mentoria-spy/): python3 .../montar.py <clipe> <saida> [env: NOISE BLUR SHARP SAT GAMMA WARM BR]
import os, subprocess, sys
N='centerpag-detect/criativos/luiza-troca-avatar-android-2026-09-19'
CLIPE,OUT=sys.argv[1],sys.argv[2]; REF=f'{N}/REFERENCIA-original.mp4'
E=lambda k,d: os.environ.get(k,d)
NOISE=E('NOISE','11'); BLUR=E('BLUR','0.45'); SHARP=E('SHARP','0.3'); SAT=E('SAT','0.86'); GAMMA=E('GAMMA','1.02'); WARM=E('WARM','-0.02'); BR=E('BR','600k'); CONTRAST=E('CONTRAST','0.95')
ZOOM=float(E('ZOOM','1.12')); OY=int(E('OY','40'))   # o original é mais fechado no rosto que o clipe do Pruna
PW=355  # largura do painel do rosto medida (borda em x=354/355)
cw=int(round(1280*PW/720))  # recorte 1:2,03 do clipe 9:16
vf=(f"[1:v]fps=30,scale={int(704*ZOOM)}:-2,crop={cw}:1280:(iw-{cw})/2:{OY},scale={PW}:720:flags=bicubic,"
    f"gblur=sigma={BLUR},unsharp=5:5:{SHARP}:5:5:0,"
    f"eq=saturation={SAT}:gamma={GAMMA}:contrast={CONTRAST},colorbalance=rs={WARM}:bs=-{WARM}:rm={WARM}:bm=-{WARM},"
    f"noise=alls={NOISE}:allf=t+u,format=yuv420p[th];"
    f"[0:v][th]overlay=0:0:shortest=1[v]")
cmd=['ffmpeg','-hide_banner','-v','error','-y','-i',REF,'-i',CLIPE,'-filter_complex',vf,'-map','[v]','-map','0:a','-c:a','copy',
     '-c:v','libx264','-preset','medium','-profile:v','main','-b:v',BR,'-maxrate',f"{int(int(BR[:-1])*1.15)}k",'-bufsize','1200k','-g','60','-pix_fmt','yuv420p','-movflags','+faststart',OUT]
open(f'{N}/conferencia/ultimo-comando.txt','w').write(' '.join(cmd)); subprocess.run(cmd,check=True); print('ok ->',OUT)
