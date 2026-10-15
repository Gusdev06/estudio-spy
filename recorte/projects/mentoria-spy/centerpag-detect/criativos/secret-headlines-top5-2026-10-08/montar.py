#!/usr/bin/env python3
# montar.py — remonta uma peça Secret Revealed a partir do molde LIMPO da mãe (clipe Pruna + karaokê do whisper da mãe) com uma faixa vermelha nova.
# Custo zero. É o montar.py de secret-hook-agressivo-2026-09-23 / remontar-secret.py de 10/09 (mesmo desenho, mesmos parâmetros), com 3 mudanças:
#  1. o whisper NÃO roda de novo: lê a cópia do JSON da mãe (molde/whisper-<mae>.json) → karaokê com os mesmos tempos e palavras da mãe;
#  2. o vídeo é renderizado SEM áudio e o áudio entra num 2º passo copiado (stream copy) da própria peça-mãe → áudio bit a bit igual
#     (e livra do bug de 07/10, em que o -frames:v sob carga fechava o arquivo com o áudio 8 s mais curto, sem erro);
#  3. --selo-orig reproduz a faixa da 77 por RECORTE do anúncio original (só pra provar a receita; as peças novas usam a faixa redesenhada).
# Uso (de projects/mentoria-spy/): python3 montar.py <mae: 77|112|121> <saida.mp4> (--selo faixa.png | --selo-orig)
import argparse, json, os, re, shutil, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
ap=argparse.ArgumentParser(); ap.add_argument('mae'); ap.add_argument('out'); ap.add_argument('--selo'); ap.add_argument('--selo-orig',action='store_true'); A=ap.parse_args()
L=os.path.dirname(os.path.abspath(sys.argv[0])); C='centerpag-detect/criativos'; P='CRIATIVOS-PRONTOS'
MAES={'77': dict(th=f'{C}/variacoes-30-2026-09-19/secret/clipes/s07.mp4', fonte_audio=f'{C}/zap-secret-revealed-avatar-2026-09-10/audio/audio-original.m4a',
                 dur_de='centerpag-detect/anuncios/secret-revealed-934941213003855.mp4', mais=0.0, mp4=f'{P}/77-ZAP-secret-revealed-filipino-jovem-moletom.mp4'),
      '112':dict(th=f'{C}/secret-hook-agressivo-2026-09-23/clipes/v01.mp4', fonte_audio=f'{C}/secret-hook-agressivo-2026-09-23/audio/v01-ritmo.wav',
                 dur_de=f'{C}/secret-hook-agressivo-2026-09-23/audio/v01-ritmo.wav', mais=0.25, mp4=f'{P}/112-ZAP-secret-hook-ela-te-trai-voce-nao-quer-ver.mp4'),
      '121':dict(th=f'{C}/secret-hook-agressivo-2026-09-23/clipes/v10.mp4', fonte_audio=f'{C}/secret-hook-agressivo-2026-09-23/audio/v10-ritmo.wav',
                 dur_de=f'{C}/secret-hook-agressivo-2026-09-23/audio/v10-ritmo.wav', mais=0.25, mp4=f'{P}/121-ZAP-secret-hook-ela-disse-que-e-amiga.mp4')}
m=MAES[A.mae]; FPS=30; W,H=1080,1920; K=1.5
probe=lambda f,*a: subprocess.run(['ffprobe','-v','error',*a,'-of','csv=p=0',f],capture_output=True,text=True).stdout.strip()
# ---- karaokê: mesmo desenho do molde (Arial Rounded Bold 86, tracking 7, topo das capitais em y 1248), palavras e tempos do whisper da mãe ----
words=[(w['word'].strip(),w['start'],w['end']) for s in json.load(open(f'{L}/molde/whisper-{A.mae}.json'))['segments'] for w in s['words'] if w['word'].strip()]
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf',86); TRACK=7; CH=140; YCAP=1248
def render(txt):
    adv=[font.getlength(c) for c in txt]; wtot=sum(adv)+TRACK*(len(txt)-1); x0=(1080-wtot)/2
    im=Image.new('RGBA',(1080,CH),(0,0,0,0)); sh=Image.new('RGBA',(1080,CH),(0,0,0,0)); d=ImageDraw.Draw(sh); bb=font.getbbox('H'); ytop=(CH-(bb[3]-bb[1]))//2-bb[1]
    x=x0
    for c,a_ in zip(txt,adv): d.text((x+4,ytop+5),c,font=font,fill=(0,0,0,150)); x+=a_+TRACK
    sh=sh.filter(ImageFilter.GaussianBlur(3)); im.alpha_composite(sh); d=ImageDraw.Draw(im); x=x0
    for c,a_ in zip(txt,adv): d.text((x,ytop),c,font=font,fill=(0,0,0,110),stroke_width=4,stroke_fill=(0,0,0,110)); x+=a_+TRACK
    x=x0
    for c,a_ in zip(txt,adv): d.text((x,ytop),c,font=font,fill=(255,255,255,255),stroke_width=2,stroke_fill=(255,255,255,255)); x+=a_+TRACK
    return im
DUR=float(probe(m['dur_de'],'-show_entries','format=duration'))+m['mais']; TOTAL=int(round(DUR*FPS))
KF=f'{L}/molde/kf-{A.mae}'
if not os.path.exists(f'{KF}/{TOTAL-1:04d}.png'):          # o karaokê é o mesmo pra todas as filhas da mesma mãe: gera uma vez
    shutil.rmtree(KF,ignore_errors=True); os.makedirs(KF); seq=[]; cache={}; Image.new('RGBA',(1080,CH),(0,0,0,0)).save(f'{KF}/vazio.png')
    for i,(w,st,en) in enumerate(words):
        txt=re.sub(r"[^A-Za-z0-9'\-]","",w).upper()
        if not txt: continue
        t0=max(0,st); t1=words[i+1][1] if i+1<len(words) else en+0.6; seq.append((t0,t1,txt))
        if txt not in cache: cache[txt]=f'{KF}/w-{len(cache):03d}.png'; render(txt).save(cache[txt])
    open(f'{L}/molde/legenda-{A.mae}.tsv','w').write('# ini_s\tfim_s\tpalavra\n'+''.join(f'{a:.2f}\t{b:.2f}\t{t}\n' for a,b,t in seq))
    j=0
    for n in range(TOTAL):
        t=n/FPS
        while j<len(seq) and t>=seq[j][1]: j+=1
        os.link(cache[seq[j][2]] if j<len(seq) and seq[j][0]<=t<seq[j][1] else f'{KF}/vazio.png',f'{KF}/{n:04d}.png')
KTOP=YCAP-((CH-(font.getbbox('H')[3]-font.getbbox('H')[1]))//2)
thw,thh=[int(x) for x in probe(m['th'],'-select_streams','v:0','-show_entries','stream=width,height').split(',')]
h=round(thh*1080/thw/2)*2; th_y=(H-h)//2
base=(f"[0:v]scale=1080:-2:flags=lanczos,crop=1080:{h}:0:0,fps={FPS},tpad=stop_mode=clone:stop_duration=60,trim=end_frame={TOTAL},setpts=PTS-STARTPTS,format=yuv420p[th0];"
      f"color=black:s={W}x{H}:r={FPS}:d={DUR:.3f}[bg];[bg][th0]overlay=x=0:y={th_y}:eof_action=pass[base];")
if A.selo_orig:   # faixa da 77 recortada do anúncio original (receita de 10/09, máscara recalculada aqui)
    ORIG=m['dur_de']; SX0,SY0,SX1,SY1=85,110,632,262; EMOJI=(536,102,602,190)
    d=subprocess.run(['ffmpeg','-nostdin','-v','error','-ss','2','-i',ORIG,'-frames:v','1','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    a=np.frombuffer(d,np.uint8).reshape(1280,720,3).astype(int); red=(a[...,0]>150)&(a[...,1]<80)&(a[...,2]<80); mask=np.zeros((1280,720),bool)
    for y in range(SY0,SY1):
        xs=np.where(red[y])[0]
        if len(xs)>20: mask[y,xs.min():xs.max()+1]=True
    e=a[EMOJI[1]:EMOJI[3],EMOJI[0]:EMOJI[2]]; mask[EMOJI[1]:EMOJI[3],EMOJI[0]:EMOJI[2]]|=(e.std(2)>12)|(e.mean(2)<120)
    MS=f'{L}/molde/mask-selo-77.png'; Image.fromarray((mask[SY0:SY1,SX0:SX1]*255).astype('uint8')).resize((int((SX1-SX0)*K),int((SY1-SY0)*K)),Image.LANCZOS).save(MS)
    inputs=['-i',m['th'],'-i',ORIG,'-loop','1','-i',MS,'-framerate',str(FPS),'-i',f'{KF}/%04d.png']
    fc=base+(f"[1:v]fps={FPS},crop={SX1-SX0}:{SY1-SY0}:{SX0}:{SY0},scale={int((SX1-SX0)*K)}:{int((SY1-SY0)*K)}:flags=lanczos,format=yuva420p[s0];[2:v]format=gray,fps={FPS}[ms];[s0][ms]alphamerge[selo];"
             f"[base][selo]overlay=x={int(SX0*K)}:y={int(SY0*K)}:eof_action=pass[v1];[3:v]format=rgba[kar];[v1][kar]overlay=x=0:y={KTOP}:eof_action=pass[v]")
else:
    inputs=['-i',m['th'],'-loop','1','-i',A.selo,'-framerate',str(FPS),'-i',f'{KF}/%04d.png']
    fc=base+f"[1:v]format=rgba,fps={FPS}[selo];[base][selo]overlay=x=0:y=0:eof_action=pass[v1];[2:v]format=rgba[kar];[v1][kar]overlay=x=0:y={KTOP}:eof_action=pass[v]"
tmp=A.out[:-4]+'.video.mp4'
cmd=['ffmpeg','-nostdin','-v','error','-y']+inputs+['-filter_complex',fc,'-map','[v]','-an','-frames:v',str(TOTAL),'-t',f'{DUR:.3f}',
 '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',tmp]
subprocess.run(cmd,check=True)
# 2º passo: áudio copiado (sem recodificar) da peça-mãe
subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-i',tmp,'-i',m['mp4'],'-map','0:v','-map','1:a','-c','copy','-movflags','+faststart',A.out],check=True); os.remove(tmp)
nf=int(probe(A.out,'-select_streams','v','-count_packets','-show_entries','stream=nb_read_packets'))
dv=float(probe(A.out,'-select_streams','v','-show_entries','stream=duration')); da=float(probe(A.out,'-select_streams','a','-show_entries','stream=duration'))
dm=float(probe(m['mp4'],'-select_streams','a','-show_entries','stream=duration'))
assert nf==TOTAL, f'{nf} frames, esperado {TOTAL}'
assert abs(da-dm)<0.01 and abs(dv-da)<0.35, f'vídeo {dv:.2f}s · áudio {da:.2f}s · áudio da mãe {dm:.2f}s'
print(f'ok -> {A.out} · {nf} fr · vídeo {dv:.2f}s · áudio {da:.2f}s (mãe {dm:.2f}s)')
