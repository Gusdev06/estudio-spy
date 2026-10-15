#!/usr/bin/env python3
# remontar-l10.py — molde L10 (wpp-01 Esther Vicman): plano único do talking head + card do app com ALFA por cima + matte de hook
# fixo no topo + karaokê amarelo + CTA final em tela cheia. Medidas em molde/README-l10.md (tudo medido no wpp-01, 360x640, ×3).
# Uso (de projects/mentoria-spy/):
#   python3 remontar-l10.py <talking-head.mp4> <blocos.tsv> <hooks.txt> <karaoke.tsv> <prefixo-saida> [--rec <gravacao>] [--off-head N] [--cta "L1|L2|L3|L4"]
# Saídas: <prefixo>-base.mp4 (sem hook, crf 10) e <prefixo>-<var>.mp4 por linha do hooks.txt (só o texto do matte muda). Áudio = o do talking head, copiado.
# Lote zap-wpp01-clone-3-ganchos-2026-09-11: cópia do script do lote EX (05/09), sem mudança na geometria.
import argparse, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont
ap=argparse.ArgumentParser(); ap.add_argument('th'); ap.add_argument('blocos'); ap.add_argument('hooks'); ap.add_argument('karaoke'); ap.add_argument('prefixo')
ap.add_argument('--rec',default='EDIÇÃO/EDIÇAO ANIMADA/ScreenRecording_08-13-2026 19-56-53_1.MP4')   # 1170×2532 60 fps 213,4 s · md5 08183dfe494a3120462b9f398819a165 (a cópia em 'EDIÇÃO 3/' é byte a byte a mesma)
ap.add_argument('--off-head',type=int,default=0,help='y do recorte 1080x1632 no talking head (ele entra abaixo do matte, y 288)')
ap.add_argument('--cta',default='CLICK THE LINK|BELOW AND|SEE THE TRUTH|NOW'); ap.add_argument('--so-base',action='store_true')
A=ap.parse_args()
FPS=30; W,H=1080,1920; L=os.path.dirname(os.path.abspath(sys.argv[0])); M=f'{L}/molde'
FP='gram-detect/scripts/fonts/Poppins-Bold.ttf'; AMARELO='0xEEFF00'
# ---- geometria medida no wpp-01 (nativo 360x640 → ×3) ----
MATTE=288                      # matte preta y 0–96 nativo (100 % preta), hook 2 linhas y 25–44 / 54–74 → topos 75 / 162, cap 60 px
HOOK_SIZE=86; HOOK_Y=(75,162)  # Poppins Bold 86 ≈ cap 60 px
CARD=dict(x=200,w=680,y=1230,r=45,alpha=0.85,feather=6)   # card x 65–290 · topo y 410 nativo · alfa ≈0,85 · borda suave
CHEIO=dict(x=30,y=45,w=1020,h=1830,r=45)                  # fase 3: card toma a tela (x 10–350, y 15–625 nativo), fundo preto
# área útil da gravação: y 110–2280 (sem barra de status nem Safari); a coluna crop do blocos.tsv (y0:y1) restringe por bloco (ex.: 110:1600 corta o mapa); sobra é preenchida de branco
KAR_SIZE=69; KAR_Y_CARD=1539; KAR_Y_CHEIO=927; KAR_PITCH=69   # cap 16 nativo (48 px) · topo y 513 nativo sobre o card · y 309 (50 %) nas fases cheias
CTA_SIZE=129; CTA_Y0=402; CTA_PITCH=128                   # 4 linhas cap 30 nativo (90 px), topos 134/176/219/261 nativo
SETAS=dict(x=360,y=1110,w=360,h=450)                      # chevrons amarelos em contorno, y 370–520 nativo, centro x 180
BLUR_IN=0.35                                              # CTA: a tela borra em 0,35 s e o texto entra junto
def dur(f):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout.strip())
# ---- máscaras ----
def rounded(w,h,r,feather,path):
    m=Image.new('L',(w,h),0); ImageDraw.Draw(m).rounded_rectangle([0,0,w-1,h-1],radius=r,fill=255)
    if feather: m=m.filter(ImageFilter.GaussianBlur(feather))
    m.save(path)
CARD_H=round(CARD['w']*2170/1170)//2*2; rounded(CARD['w'],CARD_H,CARD['r'],CARD['feather'],f'{M}/mask-card.png'); rounded(CHEIO['w'],CHEIO['h'],CHEIO['r'],0,f'{M}/mask-cheio.png')
# ---- blocos ----
blocos=[]
for l in open(A.blocos):
    if l.startswith('#') or not l.strip(): continue
    c=l.rstrip('\n').split('\t'); blocos.append(dict(ini=float(c[0]),fim=float(c[1]),fase=c[2],rec=float(c[3]),vel=float(c[4]),blur=c[5] if len(c)>5 else '-',crop=c[6] if len(c)>6 and c[6]!='-' else '110:2280'))
TOTAL=int(round(dur(A.th)*FPS)); TOTAL=min(TOTAL,int(round(blocos[-1]['fim']*FPS))); print(f'total {TOTAL} frames = {TOTAL/FPS:.2f} s · {len(blocos)} blocos')
fr=lambda t:int(round(t*FPS))
def fase_em(t):
    for b in blocos:
        if b['ini']<=t<b['fim']: return b['fase']
    return blocos[-1]['fase']
inputs=['-i',A.th,'-framerate',str(FPS),'-i',f'{M}/setas/%03d.png','-loop','1','-i',f'{M}/mask-card.png','-loop','1','-i',f'{M}/mask-cheio.png']
fc=[]
# talking head: 1080 de largura, recorte 1080x1632 em OFF_HEAD, colado abaixo do matte (y 288); o que sobra em cima é o matte preto
fc.append(f"[0:v]scale=1080:-2:flags=lanczos,fps={FPS},crop=1080:1632:0:{A.off_head},pad=1080:1920:0:{MATTE}:black,tpad=stop_mode=clone:stop_duration=60,trim=end_frame={TOTAL},setpts=PTS-STARTPTS,format=yuv420p[actor];")
NC=sum(1 for b in blocos if b['fase']=='card'); NF=sum(1 for b in blocos if b['fase']=='cheio')
fc.append(f"[2:v]format=gray,fps={FPS},split={max(NC,1)}"+''.join(f'[mcard{j}]' for j in range(max(NC,1)))+';')
fc.append(f"[3:v]format=gray,fps={FPS},split={max(NF,1)}"+''.join(f'[mcheio{j}]' for j in range(max(NF,1)))+';')
ic=0; icf=0
cur='actor'; n_in=4; kar_layers=[]
for i,b in enumerate(blocos):
    nf=fr(b['fim'])-fr(b['ini']); d=nf/FPS
    inputs+=['-ss',f"{b['rec']:.3f}",'-t',f'{d*b["vel"]+0.5:.3f}','-i',A.rec]; src=f'{n_in}:v'; n_in+=1
    ch=f'[{src}]'
    if b['blur']!='-':
        for j,r in enumerate(b['blur'].split(';')):
            x,y,w,h=r.split(':'); ch+=f"split=2[b{i}_{j}a][b{i}_{j}b];[b{i}_{j}b]crop={w}:{h}:{x}:{y},boxblur=luma_radius=20:luma_power=2:chroma_radius=6:chroma_power=2[b{i}_{j}c];[b{i}_{j}a][b{i}_{j}c]overlay={x}:{y},"
    y0,y1=[int(v) for v in b['crop'].split(':')]; ch+=f"setpts=PTS/{b['vel']},fps={FPS},crop=1170:{y1-y0}:0:{y0},"
    if b['fase']=='card':
        ch+=f"scale={CARD['w']}:-2:flags=lanczos,pad={CARD['w']}:'max(ih,{CARD_H})':0:0:white,crop={CARD['w']}:{CARD_H}:0:0,tpad=stop_mode=clone:stop_duration=60,trim=end_frame={nf},setpts=PTS-STARTPTS,format=yuva420p[c{i}];[c{i}][mcard{ic}]alphamerge,colorchannelmixer=aa={CARD['alpha']},tpad=start_duration={b['ini']:.4f}:start_mode=add:color=0x00000000[k{i}];"
        fc.append(ch); fc.append(f"[{cur}][k{i}]overlay=x={CARD['x']}:y={CARD['y']}:eof_action=pass:enable='between(n,{fr(b['ini'])},{fr(b['fim'])-1})'[v{i}];"); cur=f'v{i}'; ic+=1
    elif b['fase']=='cheio':
        ch+=f"scale={CHEIO['w']}:-2:flags=lanczos,pad={CHEIO['w']}:'max(ih,{CHEIO['h']})':0:0:white,crop={CHEIO['w']}:{CHEIO['h']}:0:0,tpad=stop_mode=clone:stop_duration=60,trim=end_frame={nf},setpts=PTS-STARTPTS,format=yuva420p[c{i}];[c{i}][mcheio{icf}]alphamerge[cc{i}];color=black:s={W}x{H}:r={FPS}:d={d:.3f}[bg{i}];[bg{i}][cc{i}]overlay=x={CHEIO['x']}:y={CHEIO['y']},format=rgba,tpad=start_duration={b['ini']:.4f}:start_mode=add:color=0x00000000[k{i}];"
        fc.append(ch); fc.append(f"[{cur}][k{i}]overlay=eof_action=pass:enable='between(n,{fr(b['ini'])},{fr(b['fim'])-1})'[v{i}];"); cur=f'v{i}'; icf+=1
    elif b['fase'] in ('bleed','cta'):
        ch+=f"scale={W}:-2:flags=lanczos,pad={W}:'max(ih,{H})':0:0:white,crop={W}:{H}:0:0,tpad=stop_mode=clone:stop_duration=60,trim=end_frame={nf},setpts=PTS-STARTPTS,format=yuv420p"
        if b['fase']=='bleed':
            ch+=f",format=rgba,tpad=start_duration={b['ini']:.4f}:start_mode=add:color=0x00000000[k{i}];"; fc.append(ch)
            fc.append(f"[{cur}][k{i}]overlay=eof_action=pass:enable='between(n,{fr(b['ini'])},{fr(b['fim'])-1})'[v{i}];"); cur=f'v{i}'
        else:   # cta: a mesma tela, nítida por baixo e borrada entrando por fade; texto + setas por cima
            ch+=f",split=2[s{i}a][s{i}b];[s{i}b]boxblur=30:3,format=rgba,fade=t=in:st=0:d={BLUR_IN}:alpha=1[s{i}c];[s{i}a][s{i}c]overlay=format=auto,format=rgba,tpad=start_duration={b['ini']:.4f}:start_mode=add:color=0x00000000[k{i}];"; fc.append(ch)
            fc.append(f"[{cur}][k{i}]overlay=eof_action=pass:enable='between(n,{fr(b['ini'])},{fr(b['fim'])-1})'[v{i}];"); cur=f'v{i}'
            # texto do CTA (4 linhas, cap 90 px) + setas em laço
            dt=[]
            for j,line in enumerate(A.cta.split('|')):
                p=f'{M}/cta-{j}.txt'; open(p,'w').write(line)
                dt.append(f"drawtext=fontfile={FP}:textfile={p}:fontsize={CTA_SIZE}:fontcolor={AMARELO}:borderw=6:bordercolor=black:shadowx=4:shadowy=4:shadowcolor=black@0.7:x=(w-text_w)/2:y={CTA_Y0+j*CTA_PITCH}:enable='gte(n,{fr(b['ini']+BLUR_IN)})'")
            fc.append(f"[{cur}]"+','.join(dt)+f"[v{i}t];[1:v]format=rgba,loop=loop=-1:size=36:start=0,trim=end_frame={TOTAL},setpts=PTS-STARTPTS,tpad=start_duration={b['ini']+BLUR_IN:.4f}:start_mode=add:color=0x00000000[setas];[v{i}t][setas]overlay=x={SETAS['x']}:y={SETAS['y']}:eof_action=pass:enable='gte(n,{fr(b['ini']+BLUR_IN)})'[v{i}];"); cur=f'v{i}'
# karaokê amarelo (Poppins Bold 69, contorno preto 4 + sombra), y conforme a fase do bloco
os.makedirs(f'{M}/k',exist_ok=True); kar=[]
for i,l in enumerate(open(A.karaoke)):
    if l.startswith('#') or not l.strip(): continue
    a,b,txt=l.rstrip('\n').split('\t')[:3]; a,b=float(a),float(b); fa,fb=fr(a),fr(b)
    if fa>=TOTAL: continue
    lines=txt.split('|'); y0=KAR_Y_CARD if fase_em(a)=='card' else KAR_Y_CHEIO
    if len(lines)==2: y0-=KAR_PITCH//2
    for j,line in enumerate(lines):
        p=f'{M}/k/{i:03d}-{j}.txt'; open(p,'w').write(line)
        kar.append(f"drawtext=fontfile={FP}:textfile={p}:fontsize={KAR_SIZE}:fontcolor={AMARELO}:borderw=4:bordercolor=black:shadowx=3:shadowy=3:shadowcolor=black@0.7:x=(w-text_w)/2:y={y0+j*KAR_PITCH}:enable='between(n\\,{fa}\\,{max(fa,fb-1)})'")
fc.append(f"[{cur}]"+','.join(kar)+"[v]")
base=f'{A.prefixo}-base.mp4'
cmd=['ffmpeg','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','0:a?','-c:a','copy','-frames:v',str(TOTAL),
 '-c:v','libx264','-preset','medium','-crf','10','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',base]
open(f'{M}/ultimo-comando-base.txt','w').write(' '.join(cmd)); subprocess.run(cmd,check=True); print('base ->',base)
if A.so_base: sys.exit()
# variantes: só o texto do matte muda
for l in open(A.hooks):
    if l.startswith('#') or not l.strip(): continue
    var,txt=l.rstrip('\n').split('\t')[:2]; dt=[]; lines=txt.split('|')[:2]
    # tamanho: 86 (cap 60, o do campeão) ou menor até a linha mais larga caber em 1000 px (A e C do roteiro passam de 20 caracteres)
    size=HOOK_SIZE
    while size>50 and max(ImageFont.truetype(FP,size).getlength(x) for x in lines)>1000: size-=2
    pitch=round(87*size/HOOK_SIZE); cap=round(60*size/HOOK_SIZE); top=round(MATTE/2-(pitch+cap)/2)   # bloco centrado no matte (campeão: 75/162 em 86)
    print(f'hook {var}: Poppins Bold {size} · topos {top} / {top+pitch} · {txt}')
    for j,line in enumerate(lines):
        p=f'{M}/hook-{var}-{j}.txt'; open(p,'w').write(line)
        dt.append(f"drawtext=fontfile={FP}:textfile={p}:fontsize={size}:fontcolor={AMARELO}:borderw=5:bordercolor=black:shadowx=4:shadowy=4:shadowcolor=black@0.75:x=(w-text_w)/2:y={top+j*pitch}")
    out=f'{A.prefixo}.mp4' if A.prefixo.endswith('-'+var) else f'{A.prefixo}-{var}.mp4'   # prefixo já terminado em -H1 + hooks-H1.txt → pecas/zap-wpp01-H1.mp4
    subprocess.run(['ffmpeg','-v','error','-y','-i',base,'-vf',','.join(dt),'-c:a','copy','-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',out],check=True)
    print('ok ->',out,'·',txt)
