#!/usr/bin/env python3
# Antonia Nicole Vice 2627173801075681 (720x1280, layout de post: caixa branca de hook + janela 16:9 do estúdio + karaokê; depois b-roll CTA,
# contagem e card estático até 367 s) → só a janela do vídeo (y 430-849 → 645-1274 em 1080p) recebe o avatar novo nos 38,0 s de fala.
# O resto do quadro é o original escalado ×1,5. Clipes p1 (0-20,70 s) + p2 (20,70-38,0 s) emendados na fronteira de frase.
import subprocess, sys
A='centerpag-detect/criativos/troca-avatar-3-2026-09-19/antonia'; P1,P2=sys.argv[1],sys.argv[2]; OUT=sys.argv[3]
REF=f'{A}/REFERENCIA-original.mp4'; W,H=1080,1920; WY,WH=645,630; T1=20.70; T2=38.0
vf=(f"[0:v]scale={W}:{H}:flags=lanczos,fps=30[base];"
    f"[1:v]trim=end={T1},setpts=PTS-STARTPTS,fps=30[a];[2:v]trim=end={T2-T1:.2f},setpts=PTS-STARTPTS,fps=30[b];[a][b]concat=n=2:v=1:a=0,"
    f"scale=-2:{WH}:flags=lanczos,crop={W}:{WH}:(iw-{W})/2:0,gblur=sigma=0.35,eq=saturation=0.95:contrast=0.98,noise=alls=5:allf=t+u,format=rgba[th];"
    f"[base][th]overlay=0:{WY}:eof_action=pass:enable='lt(t,{T2})'[v]")
cmd=['ffmpeg','-hide_banner','-v','error','-y','-i',REF,'-i',P1,'-i',P2,'-filter_complex',vf,'-map','[v]','-map','0:a','-c:a','copy',
     '-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT]
subprocess.run(cmd,check=True); print('ok ->',OUT)
