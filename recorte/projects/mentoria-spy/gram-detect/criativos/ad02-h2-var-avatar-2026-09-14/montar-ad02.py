#!/usr/bin/env python3
# AD02-H2-INSTA com avatar novo. O hook (frames 0-191) fica intacto. Do frame 192 ao fim, o rosto vira o avatar novo e
# TODAS as camadas queimadas do original (karaokê palavra-a-palavra, painéis do app, setas e o CTA "CLICK THE BELOW")
# são recolocadas por RECORTE do próprio original — não são recriadas, então saem pixel a pixel.
# Uso (de projects/mentoria-spy/):  python3 .../montar-ad02.py <clipe.mp4> <saida.mp4>
import os, subprocess, sys
P='gram-detect/criativos/ad02-h2-var-avatar-2026-09-14'
REF=f'{P}/REFERENCIA-original.mov'
CLIPE=sys.argv[1] if len(sys.argv)>1 else f'{P}/clipes/a1.mp4'
OUT=sys.argv[2] if len(sys.argv)>2 else f'{P}/AD02-H2-a1.mp4'
FPS=30; W,H=1080,1920
HOOK_FIM=192          # o hook do original vai do frame 0 ao 191 (corte de cena medido em 6,40 s)
# blocos do trecho do avatar: (frame_ini, frame_fim, zoom no avatar, desfoque, regiões do original a recolar)
# zoom: o editor original foi fechando o plano; o avatar é gerado no plano mais aberto e acompanha por crop central.
# regiões: (x0,y0,x1,y1) recortadas do original e coladas por cima do avatar.
KAR_ALTO=(0,1090,1080,1920)      # bloco 1: karaokê alto + card "Connecting to Instagram"
KAR=(0,1500,1080,1900)           # demais: faixa do karaokê
PAINEL=(90,250,990,1580)         # cards do app (perfil, terminal, prints)
# as setas do original são BRANCO SEMITRANSPARENTE (máx. 204 de luminância): não saem por máscara e o recorte
# retangular traria o rosto antigo junto. Foram redesenhadas em setas/*.png nas medidas do original (x 295-755,
# 3 chevrons a partir de y 545, espessura 46) e entram como overlay com alfa.
CTA=(0,130,1080,390)             # "CLICK THE BELOW"
# (frame_ini, frame_fim, zoom, offset_y do crop, desfoque, regiões do original)
# zoom e offset calibrados frame a frame contra o original: o crop mira a cabeça, que no clipe fica na metade de cima.
BLOCOS=[
 (192, 312, float(os.environ.get('Z1','1.00')), int(os.environ.get('O1','0')),   False, [KAR_ALTO]),
 (312, 336, 1.30, 140, True,  [PAINEL,KAR]),
 (336, 458, 1.30, 140, True,  [PAINEL,KAR]),
 (458, 608, float(os.environ.get('Z4','2.60')), int(os.environ.get('O4','450')), False, [KAR]),
 (608, 654, 1.90, 260, True,  [PAINEL,KAR]),
 (654, 815, 1.90, 260, True,  [PAINEL,KAR]),
 (815, 849, 1.90, 260, True,  [PAINEL,KAR]),
 (849, 967, 1.90, 260, True,  [PAINEL,KAR]),
 (967,1090, float(os.environ.get('Z9','2.80')), int(os.environ.get('O9','620')), False, [CTA,KAR]),
]
BLUR=int(os.environ.get('BLUR','26'))
fc=[]; n_in=2   # 0 = original, 1 = clipe do avatar
# avatar base: escala pra 1080 de largura mantendo proporção, corta 1080x1920 centrado
fc.append(f"[1:v]scale={W}:-2:flags=lanczos,fps={FPS},setsar=1[av];")   # sem crop aqui: cada bloco faz o seu
fc.append(f"[av]split={len(BLOCOS)}"+''.join(f'[av{i}]' for i in range(len(BLOCOS)))+';')
cur='[0:v]'
for i,(f0,f1,zoom,oy,desfoca,regioes) in enumerate(BLOCOS):
    dur=f1-f0
    z=f"scale={int(W*zoom)}:-2:flags=lanczos,crop={W}:{H}:(iw-{W})/2:{oy}"
    b=f",boxblur={BLUR}:1" if desfoca else ""
    # recorta o trecho do avatar correspondente (o clipe começa no frame 192 do original) e atrasa até o lugar certo
    fc.append(f"[av{i}]trim=start_frame={f0-HOOK_FIM}:end_frame={f1-HOOK_FIM},setpts=PTS-STARTPTS,{z}{b},format=yuv420p,"
              f"setpts=PTS+{f0}/{FPS}/TB[c{i}];")
    prox=f'[s{i}]'
    fc.append(f"{cur}[c{i}]overlay=0:0:eof_action=pass:enable='between(n,{f0},{f1-1})'{prox};")
    cur=prox
# camadas do original por cima, cada uma só nos frames do seu bloco
fc.append(f"[0:v]split={sum(len(b[5]) for b in BLOCOS)}"+''.join(f'[o{k}]' for k in range(sum(len(b[5]) for b in BLOCOS)))+';')
k=0
for i,(f0,f1,zoom,oy,desfoca,regioes) in enumerate(BLOCOS):
    for (x0,y0,x1,y1) in regioes:
        fc.append(f"[o{k}]crop={x1-x0}:{y1-y0}:{x0}:{y0},setpts=PTS,format=yuv420p[r{k}];")
        prox=f'[t{k}]'
        fc.append(f"{cur}[r{k}]overlay={x0}:{y0}:eof_action=pass:enable='between(n,{f0},{f1-1})'{prox};")
        cur=prox; k+=1
f9,f9f=BLOCOS[-1][0],BLOCOS[-1][1]
fc.append(f"[2:v]format=rgba,loop=loop=-1:size=6:start=0,fps={FPS},tpad=start_duration={f9/FPS:.4f}:start_mode=add:color=0x00000000[setas];")
prox='[v]'
fc.append(f"{cur}[setas]overlay=0:0:eof_action=pass:enable='between(n,{f9},{f9f-1})'{prox};")
fc[-1]=fc[-1].rstrip(';')
cmd=['ffmpeg','-hide_banner','-v','error','-y','-i',REF,'-i',CLIPE,'-framerate',str(FPS),'-i',f'{P}/setas/%03d.png','-filter_complex',''.join(fc),
 '-map','[v]','-map','0:a','-c:a','copy',
 '-c:v','libx264','-preset','slow','-crf','17','-pix_fmt','yuv420p',
 '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',
 '-movflags','+faststart',OUT]
os.makedirs(f'{P}/conferencia',exist_ok=True); open(f'{P}/conferencia/ultimo-comando.txt','w').write(' '.join(cmd))
subprocess.run(cmd,check=True)
print('ok ->',OUT)
