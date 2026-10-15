#!/usr/bin/env python3
# remontar-emilly.py — reconstrói a edição do Zap #3 (Emilly Bredoff, 939122432559594, 360x480) por cima de um talking head novo, em 1080x1920.
# Reaproveita POR RECORTE do original: caixa verde do hook (x 43–316 · y 29–83) e o card do app (x 125–360 · y 109–407, alfa já composto).
# CTA (29,1 s → fim) refeito em tela cheia: borrão do talking head + texto amarelo 2 linhas + chevrons brancos. Áudio = audio/audio-original.m4a.
# Sem karaokê (medido: 0 px de texto branco fora do card em 14 instantes); --karaoke queima blocos do whisper se o Peneira pedir.
# Uso (de projects/mentoria-spy/): python3 remontar-emilly.py <talking-head.mp4> <saida.mp4> [--th-y N] [--off-head N] [--karaoke] [--cta "L1|L2"]
import argparse, json, os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter
ap=argparse.ArgumentParser(); ap.add_argument('th'); ap.add_argument('out')
ap.add_argument('--th-y',type=int,default=None,help='y do topo do talking head no quadro 1080x1920 (padrão: centrado; 0 pro clipe 9:16)')
ap.add_argument('--off-head',type=int,default=0,help='recorte extra no topo do talking head antes de posicionar')
ap.add_argument('--th-x',type=int,default=0,help='deslocamento horizontal do talking head (negativo = sujeito pra ESQUERDA; o card cobre x 375–1080 e tem que ler sobre fundo, não sobre o rosto)')
ap.add_argument('--zoom',type=float,default=1.0,help='escala extra do talking head antes de recortar (ex. 1.25 pra afastar o rosto do card)')
ap.add_argument('--karaoke',action='store_true'); ap.add_argument('--cta',default='CLICK THE LINK BELOW|AND SEE THE TRUTH NOW.')
A=ap.parse_args()
L=os.path.dirname(os.path.abspath(sys.argv[0])); M=f'{L}/molde'; os.makedirs(M,exist_ok=True)
ORIG='centerpag-detect/anuncios/emilly-bredoff-939122432559594.mp4'; AUD=f'{L}/audio/audio-original.m4a'
FP='gram-detect/scripts/fonts/Poppins-Bold.ttf'; FI='gram-detect/scripts/fonts/Inter-Bold.ttf'; FPS=30; W,H=1080,1920
# ---- medido no original (360x480, ×3) ----
BOX=(43,29,274,55)      # caixa verde #00FD11, 2 linhas pretas (y 35–51 / 57–78), cantos arredondados
CARD=(125,109,235,299)  # card do app: da borda esquerda suave até a borda direita do quadro, janela de conteúdo y 109–407
WIN_H=299*3             # janela de conteúdo do original ×3 = 897
CARD_Y=(H-WIN_H)//2     # 511 — janela centrada no 9:16 (decisão registrada no README)
GAP=(CARD[1]-(BOX[1]+BOX[3]))*3   # 78: distância caixa→janela no original
BOX_Y=CARD_Y-GAP-BOX[3]*3         # 268
CTA_T=28.933; FEATHER_L=30; FADE_B=150
DUR=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',AUD],capture_output=True,text=True).stdout); TOTAL=int(round(DUR*FPS))
# talking head: escala a 1080 de largura; altura h; posiciona em th_y (padrão centrado) sobre preto
thw,thh=[int(x) for x in subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','csv=p=0',A.th],capture_output=True,text=True).stdout.strip().split(',')]
sw=round(1080*A.zoom/2)*2; h=round(thh*sw/thw/2)*2-A.off_head; th_y=A.th_y if A.th_y is not None else (H-h)//2
print(f'talking head {thw}x{thh} → {sw}x{h+A.off_head} (zoom {A.zoom}, off {A.off_head}) em x {A.th_x-(sw-1080)//2} y {th_y} · caixa y {BOX_Y}–{BOX_Y+BOX[3]*3} · card x 375–1080 y {CARD_Y}–{CARD_Y+WIN_H} · CTA {CTA_T}s · total {TOTAL} fr')
# máscaras
def mask(w,hh,r,feather_l=0,fade_b=0,path=''):
    m=Image.new('L',(w,hh),0); ImageDraw.Draw(m).rounded_rectangle([0,0,w-1,hh-1],radius=r,fill=255)
    import numpy as np; a=np.array(m).astype(float)
    if feather_l: a[:, :feather_l]*=np.linspace(0,1,feather_l)[None,:]
    if fade_b: a[-fade_b:,:]*=np.linspace(1,0,fade_b)[:,None]
    Image.fromarray(a.astype('uint8')).save(path)
mask(BOX[2]*3,BOX[3]*3,15,path=f'{M}/mask-box.png'); mask(CARD[2]*3,CARD[3]*3,0,FEATHER_L,FADE_B,f'{M}/mask-card.png')
# chevrons brancos (3, como no original x 127–233 · y 315–424 → 318 px de largura), com bounce
cw,ch=318,330; im=Image.new('RGBA',(cw,ch),(0,0,0,0)); d=ImageDraw.Draw(im)
for j in range(3):
    cy=45+j*105; d.line([(20,cy-30),(159,cy+30),(298,cy-30)],fill=(255,255,255,255),width=26,joint='curve')
im.save(f'{M}/chevrons.png')
inputs=['-i',A.th,'-i',ORIG,'-loop','1','-i',f'{M}/mask-box.png','-loop','1','-i',f'{M}/mask-card.png','-loop','1','-i',f'{M}/chevrons.png','-i',AUD]
fc=[]
fc.append(f"[0:v]scale={sw}:-2:flags=lanczos,crop={sw}:{h}:0:{A.off_head},fps={FPS},tpad=stop_mode=clone:stop_duration=60,trim=end_frame={TOTAL},setpts=PTS-STARTPTS,format=yuv420p[th0];")
fc.append(f"color=black:s={W}x{H}:r={FPS}:d={DUR:.3f}[bg];[bg][th0]overlay=x={A.th_x-(sw-1080)//2}:y={th_y}:eof_action=pass,split=2[base][forblur];")
fc.append(f"[1:v]fps={FPS},split=2[o1][o2];[2:v]format=gray,fps={FPS}[mb];[3:v]format=gray,fps={FPS}[mc];")
fc.append(f"[o1]crop={BOX[2]}:{BOX[3]}:{BOX[0]}:{BOX[1]},scale={BOX[2]*3}:{BOX[3]*3}:flags=lanczos,format=yuva420p[b0];[b0][mb]alphamerge[box];")
fc.append(f"[o2]crop={CARD[2]}:{CARD[3]}:{CARD[0]}:{CARD[1]},scale={CARD[2]*3}:{CARD[3]*3}:flags=lanczos,format=yuva420p[c0];[c0][mc]alphamerge[card];")
fc.append(f"[base][card]overlay=x={W-CARD[2]*3}:y={CARD_Y}:eof_action=pass:enable='lt(t,{CTA_T})'[v1];[v1][box]overlay=x={BOX[0]*3}:y={BOX_Y}:eof_action=pass:enable='lt(t,{CTA_T})'[v2];")
# CTA: borrão do talking head entrando em 0,35 s + texto + chevrons com bounce
fc.append(f"[forblur]boxblur=30:3,format=rgba,fade=t=in:st={CTA_T}:d=0.35:alpha=1,tpad=stop_mode=clone:stop_duration=1[blur];[v2][blur]overlay=format=auto:eof_action=pass:enable='gte(t,{CTA_T})'[v3];")
dt=[]
for j,line in enumerate(A.cta.split('|')):
    p=f'{M}/cta-{j}.txt'; open(p,'w').write(line)
    dt.append(f"drawtext=fontfile={FP}:textfile={p}:fontsize=64:fontcolor=0xF2F500:borderw=3:bordercolor=black:shadowx=3:shadowy=3:shadowcolor=black@0.7:x=(w-text_w)/2:y={560+j*80}:enable='gte(t,{CTA_T+0.35})'")
fc.append(f"[v3]{','.join(dt)}[v4];[4:v]format=rgba,fps={FPS}[chev];[v4][chev]overlay=x={(W-cw)//2}:y='1180+18*sin(2*PI*t/1.2)':eof_action=pass:enable='gte(t,{CTA_T+0.35})'[v5];")
cur='v5'
if A.karaoke:   # opcional: blocos de 2–4 palavras do whisper do áudio original, branco, centro-baixo
    js=f'{M}/audio-original-16k.json'; words=[(w['word'].strip(),w['start'],w['end']) for s in json.load(open(js))['segments'] for w in s['words'] if w['word'].strip()]
    bl=[]; cur_w=[]
    for w in words:
        cur_w.append(w)
        if len(cur_w)>=3 or re.search(r'[.,!?]$',w[0]): bl.append((cur_w[0][1],cur_w[-1][2],' '.join(x[0] for x in cur_w))); cur_w=[]
    if cur_w: bl.append((cur_w[0][1],cur_w[-1][2],' '.join(x[0] for x in cur_w)))
    os.makedirs(f'{M}/k',exist_ok=True); k=[]
    for i,(a,b,t) in enumerate(bl):
        p=f'{M}/k/{i:03d}.txt'; open(p,'w').write(re.sub(r'[.,!?]','',t).upper())
        c=f"drawtext=fontfile={FI}:textfile={p}:fontsize=62:x=(w-text_w)/2:y=1500:enable='between(t,{a:.2f},{b:.2f})'"
        k.append(f"{c}:fontcolor=0xFCFCFC:borderw=4:bordercolor=0x0C0B0C@0.95")
    fc.append(f"[{cur}]{','.join(k)}[v6];"); cur='v6'
fc.append(f"[{cur}]copy[v]")
cmd=['ffmpeg','-nostdin','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','5:a','-c:a','aac','-b:a','192k','-frames:v',str(TOTAL),'-t',f'{DUR:.3f}',
 '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',A.out]
open(f'{M}/ultimo-comando.txt','w').write(' '.join(cmd)); subprocess.run(cmd,check=True); print('ok ->',A.out)
