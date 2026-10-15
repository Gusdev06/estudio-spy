#!/usr/bin/env python3
# remontar-secret.py — edição do Zap "secret revealed" (934941213003855, 720x1280, 32,23 s) por cima de um talking head novo, 1080x1920 30 fps.
# Reaproveita por RECORTE do original o selo vermelho fixo do topo (duas caixas #B40000 + emoji 📱, x 90–627 · y 116–257 no 720x1280) com alfa
# só nas caixas + emoji; a legenda de 1 palavra (branca, ~y 832–874, centrada) é REPRODUZIDA por drawtext com os tempos por palavra do whisper
# do áudio original (não dá pra recortar: fica sobre a camiseta/mãos). Sem CTA, rosto cheio o vídeo inteiro. Áudio = audio/audio-original.m4a.
# Uso (de projects/mentoria-spy/): python3 remontar-secret.py <talking-head.mp4> <saida.mp4> [--th-y N] [--th-x N] [--zoom F] [--off-head N]
#   [--fonte caminho.ttf] [--tamanho 66] [--y 1248] [--atraso -0.10]
import argparse, json, os, re, subprocess, sys
import numpy as np
from PIL import Image
ap=argparse.ArgumentParser(); ap.add_argument('th'); ap.add_argument('out'); ap.add_argument('--audio',required=True); ap.add_argument('--selo',required=True)
ap.add_argument('--th-y',type=int,default=None); ap.add_argument('--th-x',type=int,default=0); ap.add_argument('--zoom',type=float,default=1.0); ap.add_argument('--off-head',type=int,default=0)
ap.add_argument('--fonte',default='/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf',help='rosto arredondado pesado; cap 63 px @1080 (original 42 px @720)'); ap.add_argument('--tamanho',type=int,default=86); ap.add_argument('--tracking',type=int,default=7,help='espaço extra entre letras (px): BOYFRIENDS do original mede 634 px, Arial Rounded 86 sem tracking dá 568')
ap.add_argument('--y',type=int,default=1248,help='topo das capitais (original y 832 ×1,5)'); ap.add_argument('--atraso',type=float,default=0.0,help='deslocamento dos tempos do whisper (s); medido no original: legenda − whisper = +0,03 s')
A=ap.parse_args()
L=os.path.dirname(os.path.abspath(sys.argv[0])); M=f'{L}/molde'; os.makedirs(M,exist_ok=True)
ORIG='centerpag-detect/anuncios/secret-revealed-934941213003855.mp4'; AUD=A.audio; FPS=30; W,H=1080,1920; K=1.5
# ---- selo: recorte x 85–632 · y 110–262 (720x1280) com alfa = caixas vermelhas preenchidas + emoji ----
SX0,SY0,SX1,SY1=85,110,632,262; EMOJI=(536,102,602,190)
d=subprocess.run(['ffmpeg','-nostdin','-v','error','-ss','2','-i',ORIG,'-frames:v','1','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
a=np.frombuffer(d,np.uint8).reshape(1280,720,3).astype(int); red=(a[...,0]>150)&(a[...,1]<80)&(a[...,2]<80)
mask=np.zeros((1280,720),bool)
for y in range(SY0,SY1):
    xs=np.where(red[y])[0]
    if len(xs)>20: mask[y,xs.min():xs.max()+1]=True
mask[EMOJI[1]:EMOJI[3],EMOJI[0]:EMOJI[2]]|=(a[EMOJI[1]:EMOJI[3],EMOJI[0]:EMOJI[2]].std(2)>12)|(a[EMOJI[1]:EMOJI[3],EMOJI[0]:EMOJI[2]].mean(2)<120)   # emoji: pixels que não são a parede bege
sub=mask[SY0:SY1,SX0:SX1]; Image.fromarray((sub*255).astype('uint8')).resize((int((SX1-SX0)*K),int((SY1-SY0)*K)),Image.LANCZOS).save(f'{M}/mask-selo.png')
# ---- legenda: 1 palavra por vez, tempos do whisper ----
M=os.path.dirname(A.out)+'/molde-'+os.path.basename(A.out).split('.')[0]; os.makedirs(M,exist_ok=True)
js=f'{M}/audio-16k.json'
if not os.path.exists(js):
    subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-i',AUD,'-ac','1','-ar','16000',f'{M}/audio-16k.wav'],check=True)
    subprocess.run(['uvx','--from','mlx-whisper','mlx_whisper',f'{M}/audio-16k.wav','--model','mlx-community/whisper-small.en-mlx','--word-timestamps','True','--output-dir',M,'--output-format','json','--language','en'],check=True,capture_output=True)
words=[(w['word'].strip(),w['start'],w['end']) for s in json.load(open(js))['segments'] for w in s['words'] if w['word'].strip()]
# faixa de legenda como sequência de PNGs (30 fps): PIL desenha cada palavra com tracking, sombra e contorno — drawtext não tem tracking
from PIL import ImageDraw, ImageFilter, ImageFont
FPS_=30; font=ImageFont.truetype(A.fonte,A.tamanho); CH=140
def render(txt):
    adv=[font.getlength(c) for c in txt]; wtot=sum(adv)+A.tracking*(len(txt)-1); x0=(1080-wtot)/2
    im=Image.new('RGBA',(1080,CH),(0,0,0,0)); sh=Image.new('RGBA',(1080,CH),(0,0,0,0)); d=ImageDraw.Draw(sh); bb=font.getbbox('H'); ytop=(CH-(bb[3]-bb[1]))//2-bb[1]
    x=x0
    for c,a_ in zip(txt,adv): d.text((x+4,ytop+5),c,font=font,fill=(0,0,0,150)); x+=a_+A.tracking
    sh=sh.filter(ImageFilter.GaussianBlur(3)); im.alpha_composite(sh); d=ImageDraw.Draw(im); x=x0
    for c,a_ in zip(txt,adv): d.text((x,ytop),c,font=font,fill=(0,0,0,110),stroke_width=4,stroke_fill=(0,0,0,110)); x+=a_+A.tracking   # borda escura fina e suave
    x=x0
    for c,a_ in zip(txt,adv): d.text((x,ytop),c,font=font,fill=(255,255,255,255),stroke_width=2,stroke_fill=(255,255,255,255)); x+=a_+A.tracking   # traço engrossado (peso do original)
    return im
DUR=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',AUD],capture_output=True,text=True).stdout)+0.25; TOTAL=int(round(DUR*FPS))
import shutil; KF=f'{M}/kf'; shutil.rmtree(KF,ignore_errors=True); os.makedirs(KF)
seq=[]; cache={}; empty=Image.new('RGBA',(1080,CH),(0,0,0,0)); empty.save(f'{KF}/vazio.png')
for i,(w,st,en) in enumerate(words):
    txt=re.sub(r"[^A-Za-z0-9'\-]","",w).upper()
    if not txt: continue
    t0=max(0,st+A.atraso); t1=(words[i+1][1]+A.atraso) if i+1<len(words) else en+0.6; seq.append((t0,t1,txt))
    if txt not in cache: cache[txt]=f'{KF}/w-{len(cache):03d}.png'; render(txt).save(cache[txt])
open(f'{M}/legenda.tsv','w').write('# ini_s\tfim_s\tpalavra\n'+''.join(f'{a:.2f}\t{b:.2f}\t{t}\n' for a,b,t in seq))
j=0
for n in range(TOTAL):
    t=n/FPS
    while j<len(seq) and t>=seq[j][1]: j+=1
    src=cache[seq[j][2]] if j<len(seq) and seq[j][0]<=t<seq[j][1] else f'{KF}/vazio.png'
    os.link(src,f'{KF}/{n:04d}.png') if not os.path.exists(f'{KF}/{n:04d}.png') else None
KTOP=A.y-((CH-(font.getbbox('H')[3]-font.getbbox('H')[1]))//2)   # topo da faixa tal que o topo das capitais caia em --y
thw,thh=[int(x) for x in subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','csv=p=0',A.th],capture_output=True,text=True).stdout.strip().split(',')]
sw=round(1080*A.zoom/2)*2; h=round(thh*sw/thw/2)*2-A.off_head; th_y=A.th_y if A.th_y is not None else (H-h)//2
print(f'talking head {thw}x{thh} → {sw}x{h+A.off_head} em x {A.th_x-(sw-1080)//2} y {th_y} · selo x {int(SX0*K)}–{int(SX1*K)} y {int(SY0*K)}–{int(SY1*K)} · {len(seq)} legendas ({len(cache)} palavras distintas, {A.fonte.split(chr(47))[-1]} {A.tamanho} tracking {A.tracking}) · total {TOTAL} fr = {DUR:.2f}s')
inputs=['-i',A.th,'-loop','1','-i',A.selo,'-i',AUD,'-framerate',str(FPS),'-i',f'{KF}/%04d.png']
fc=[f"[0:v]scale={sw}:-2:flags=lanczos,crop={sw}:{h}:0:{A.off_head},fps={FPS},tpad=stop_mode=clone:stop_duration=60,trim=end_frame={TOTAL},setpts=PTS-STARTPTS,format=yuv420p[th0];",
    f"color=black:s={W}x{H}:r={FPS}:d={DUR:.3f}[bg];[bg][th0]overlay=x={A.th_x-(sw-1080)//2}:y={th_y}:eof_action=pass[base];",
    f"[1:v]format=rgba,fps={FPS}[selo];[base][selo]overlay=x=0:y=0:eof_action=pass[v1];",
    f"[3:v]format=rgba[kar];[v1][kar]overlay=x=0:y={KTOP}:eof_action=pass[v]"]
cmd=['ffmpeg','-nostdin','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','2:a','-c:a','aac','-b:a','192k','-frames:v',str(TOTAL),'-t',f'{DUR:.3f}',
 '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',A.out]
open(f'{M}/ultimo-comando.txt','w').write(' '.join(cmd)); subprocess.run(cmd,check=True); print('ok ->',A.out)
