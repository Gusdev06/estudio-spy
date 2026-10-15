#!/usr/bin/env python3
# AD02-H2-INSTA RECONSTRUÍDO com avatar novo. Nada é recortado "com fundo" do original: cada camada é um elemento próprio.
#   hook (0-191) ......... o original, intacto
#   avatar (192-1089) .... clipe Pruna em tela cheia, zoom+offset por bloco (o editor fechou o plano), desfoque gblur 18 nos blocos de painel
#   painéis do app ....... o print do funil recortado JUSTO na borda (193,347 · 692x1224) + sombra sintética, e o card
#                          "Connecting" (147,1369 · 788x398) com máscara de cantos arredondados
#   karaokê .............. redesenhado palavra a palavra em Oswald Bold (gerar-karaoke.py), 1 PNG por frame
#   setas e CTA .......... redesenhados (assets/setas, assets/cta), frames 999-1082
# Uso (de projects/mentoria-spy/):  python3 .../montar-reconstrucao.py <clipe.mp4> <saida.mp4>
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter
P='gram-detect/criativos/ad02-h2-reconstrucao-2026-09-17'
REF=f'{P}/REFERENCIA-original.mov'
CLIPE=sys.argv[1] if len(sys.argv)>1 else f'{P}/clipes/a2.mp4'
OUT=sys.argv[2] if len(sys.argv)>2 else f'{P}/AD02-H2-reconstruido-a2.mp4'
FPS=30; W,H=1080,1920; HOOK_FIM=192; TOTAL=1090
BLUR=float(os.environ.get('BLUR','18'))
# (ini, fim, zoom, offset_y, desfoca). Gusta, 17/09: "não precisa ficar dando zoom, deixa sempre no mesmo" — enquadramento
# fixo o vídeo inteiro (Z/OY por env); só o desfoque muda nos blocos de painel.
Z=float(os.environ.get('Z','1.35')); OY=int(os.environ.get('OY','160'))
BLOCOS=[(192,312,Z,OY,False),(312,458,Z,OY,True),(458,608,Z,OY,False),(608,967,Z,OY,True),(967,1090,Z,OY,False)]
PAINEL_X,PAINEL_Y,PW,PH=193,347,692,1224
CARD_X,CARD_Y,CW,CH=147,1369,788,398
CTA_INI,CTA_FIM=999,1083
# ---- assets estáticos: sombra do painel e máscara do card ----
os.makedirs(f'{P}/assets',exist_ok=True)
M=90; sh=Image.new('RGBA',(PW+2*M,PH+2*M),(0,0,0,0)); ImageDraw.Draw(sh).rectangle([M,M,M+PW,M+PH],fill=(0,0,0,110)); sh=sh.filter(ImageFilter.GaussianBlur(28)); sh.save(f'{P}/assets/sombra-painel.png')
mk=Image.new('L',(CW,CH),0); ImageDraw.Draw(mk).rounded_rectangle([0,0,CW-1,CH-1],radius=30,fill=255); mk.save(f'{P}/assets/mascara-card.png')
shc=Image.new('RGBA',(CW+2*M,CH+2*M),(0,0,0,0)); ImageDraw.Draw(shc).rounded_rectangle([M,M,M+CW,M+CH],radius=30,fill=(0,0,0,100)); shc=shc.filter(ImageFilter.GaussianBlur(26)); shc.save(f'{P}/assets/sombra-card.png')
inputs=['-i',REF,'-i',CLIPE,
        '-i',f'{P}/assets/paineis/painel-A-perfil.mp4','-i',f'{P}/assets/paineis/painel-B-suspicious-dms.mp4','-i',f'{P}/assets/paineis/card-connecting.mp4',
        '-framerate',str(FPS),'-start_number',str(HOOK_FIM),'-i',f'{P}/karaoke/frames/%04d.png',
        '-framerate',str(FPS),'-i',f'{P}/assets/setas/%03d.png','-framerate',str(FPS),'-i',f'{P}/assets/cta/%03d.png',
        '-i',f'{P}/assets/sombra-painel.png','-i',f'{P}/assets/mascara-card.png','-i',f'{P}/assets/sombra-card.png']
# atraso por preenchimento transparente (tpad), o método que funcionou nos lotes do podcast — sem mexer em timestamps
def atrasa(ini_frame): return f"tpad=start_duration={ini_frame/FPS:.4f}:start_mode=add:color=0x00000000"
fc=[]
fc.append(f"[1:v]scale={W}:-2:flags=lanczos,fps={FPS},setsar=1,split={len(BLOCOS)}"+''.join(f'[av{i}]' for i in range(len(BLOCOS)))+';')
cur='[0:v]'
for i,(f0,f1,z,oy,blur) in enumerate(BLOCOS):
    b=f",gblur=sigma={BLUR}" if blur else ""
    fc.append(f"[av{i}]trim=start_frame={f0-HOOK_FIM}:end_frame={f1-HOOK_FIM},setpts=PTS-STARTPTS,scale={int(W*z)}:-2:flags=lanczos,crop={W}:{H}:(iw-{W})/2:{oy}{b},format=rgba,{atrasa(f0)}[c{i}];")
    fc.append(f"{cur}[c{i}]overlay=0:0:eof_action=pass:enable='between(n,{f0},{f1-1})'[s{i}];"); cur=f'[s{i}]'
# sombras estáticas viram vídeos rgba do tamanho certo, ligadas só nos frames dos seus blocos
fc.append(f"[8:v]format=rgba,loop=loop=-1:size=1:start=0,fps={FPS}[shp];[10:v]format=rgba,loop=loop=-1:size=1:start=0,fps={FPS}[shc];[9:v]format=gray,loop=loop=-1:size=1:start=0,fps={FPS}[mk];")
fc.append(f"{cur}[shc]overlay={CARD_X-M}:{CARD_Y-M}:eof_action=pass:enable='between(n,192,311)'[t0];")
fc.append(f"[4:v]fps={FPS},format=rgba[cardv];[cardv][mk]alphamerge,{atrasa(192)}[card];[t0][card]overlay={CARD_X}:{CARD_Y}:eof_action=pass:enable='between(n,192,311)'[t1];")
fc.append(f"[t1][shp]overlay={PAINEL_X-M}:{PAINEL_Y-M}:eof_action=pass:enable='between(n,312,457)+between(n,608,966)'[t2];")
fc.append(f"[2:v]fps={FPS},format=rgba,{atrasa(312)}[pA];[t2][pA]overlay={PAINEL_X}:{PAINEL_Y}:eof_action=pass:enable='between(n,312,457)'[t3];")
fc.append(f"[3:v]fps={FPS},format=rgba,{atrasa(608)}[pB];[t3][pB]overlay={PAINEL_X}:{PAINEL_Y}:eof_action=pass:enable='between(n,608,966)'[t4];")
fc.append(f"[5:v]format=rgba,{atrasa(HOOK_FIM)}[kar];[t4][kar]overlay=0:950:eof_action=pass:enable='gte(n,{HOOK_FIM})'[t5];")
fc.append(f"[6:v]format=rgba,loop=loop=-1:size=6:start=0,fps={FPS},{atrasa(CTA_INI)}[set];[t5][set]overlay=0:0:eof_action=pass:enable='between(n,{CTA_INI},{CTA_FIM-1})'[t6];")
fc.append(f"[7:v]format=rgba,loop=loop=-1:size=8:start=0,fps=15,fps={FPS},{atrasa(CTA_INI)}[cta];[t6][cta]overlay=0:130:eof_action=pass:enable='between(n,{CTA_INI},{CTA_FIM-1})'[v]")
cmd=['ffmpeg','-hide_banner','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','0:a','-c:a','copy',
     '-frames:v',str(TOTAL),'-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p',
     '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT]
os.makedirs(f'{P}/conferencia',exist_ok=True); open(f'{P}/conferencia/ultimo-comando.txt','w').write(' '.join(cmd))
subprocess.run(cmd,check=True); print('ok ->',OUT)
