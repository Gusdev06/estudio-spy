#!/usr/bin/env python3
# "Super criativo" Spy Zap (19/09): copy nova com os 10 elementos (curiosidade → promessa → segmentação → problema → mecanismo →
# autoridade → benefício → prova social → urgência → dupla CTA), voz feminina, avatar "gente comum no quarto" com look de celular,
# gancho escrito = matte da família A+B' do swipe Zap ("What their WhatsApp is hiding... / see this before it's too late"),
# edição = molde reconstruído do AD02-H2 Zap (card backup → mapa → rosto limpo → chats + relatório → CTA + setas), painéis do funil real.
# Uso (de projects/mentoria-spy/): python3 .../montar-super-zap.py <clipe> <saida>
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter
P='centerpag-detect/criativos/super-zap-2026-09-19'
E=lambda k,d: os.environ.get(k,d)
AUD=E('AUD',f'{P}/audio/vo10-ritmo.wav'); CLIPE=sys.argv[1]; OUT=sys.argv[2]
T=json.load(open(f'{P}/molde/timeline.json')); FPS=30; W,H=1080,1920; TOTAL=T['total']
Z=float(E('Z','1.0')); OY=int(E('OY','0')); BLURP=18
BLUR=E('BLUR','0.4'); NOISE=E('NOISE','8'); SAT=E('SAT','0.9'); GAMMA=E('GAMMA','1.02'); CONTRAST=E('CONTRAST','0.97'); WARM=float(E('WARM','-0.02'))
L1=E('CAIXA_L1',"What their WhatsApp is hiding..."); L2=E('CAIXA_L2',"see this before it's too late"); BOXSZ=int(E('BOXSZ','50')); FP='gram-detect/scripts/fonts/Poppins-Bold.ttf'
c0,c1=T['card']; a0,a1=T['painelA']; l0,l1=T['limpo']; b0,b1=T['painelB']; f0_,f1_=T['final']; CTA_INI,CTA_FIM=T['cta']; BOX_END=T['caixa_fim']; B1=120
BLOCOS=[(c0,c1,False),(a0,a1,True),(l0,l1,False),(b0,b1,True),(f0_,f1_,False)]
PAINEL_X,PAINEL_Y,PW,PH=193,347,692,1224; CW,CH=788,252; CARD_X=147; CARD_Y=1568-CH//2; M=90
os.makedirs(f'{P}/molde/k',exist_ok=True)
sh=Image.new('RGBA',(PW+2*M,PH+2*M),(0,0,0,0)); ImageDraw.Draw(sh).rectangle([M,M,M+PW,M+PH],fill=(0,0,0,110)); sh.filter(ImageFilter.GaussianBlur(28)).save(f'{P}/assets/sombra-painel.png')
mk=Image.new('L',(CW,CH),0); ImageDraw.Draw(mk).rounded_rectangle([0,0,CW-1,CH-1],radius=30,fill=255); mk.save(f'{P}/assets/mascara-card.png')
shc=Image.new('RGBA',(CW+2*M,CH+2*M),(0,0,0,0)); ImageDraw.Draw(shc).rounded_rectangle([M,M,M+CW,M+CH],radius=30,fill=(0,0,0,100)); shc.filter(ImageFilter.GaussianBlur(26)).save(f'{P}/assets/sombra-card.png')
A=f'{P}/assets/paineis'
inputs=['-i',CLIPE,'-i',f'{A}/painel-A-mapa.mp4','-i',f'{A}/painel-B1-chats.mp4','-i',f'{A}/card-backup.mp4',
        '-framerate',str(FPS),'-start_number','0','-i',f'{P}/karaoke/frames/%04d.png',
        '-framerate',str(FPS),'-i',f'{P}/assets/setas/%03d.png','-framerate',str(FPS),'-i',f'{P}/assets/cta/%03d.png',
        '-i',f'{P}/assets/sombra-painel.png','-i',f'{P}/assets/mascara-card.png','-i',f'{P}/assets/sombra-card.png','-i',AUD,'-i',f'{A}/painel-B2-relatorio.mp4']
def atrasa(ini): return f"tpad=start_duration={ini/FPS:.4f}:start_mode=add:color=0x00000000"
def segura(fr): return f"tpad=stop_mode=clone:stop_duration={fr/FPS+1:.2f}"
fc=[]
fc.append(f"[0:v]scale={W}:-2:flags=lanczos,fps={FPS},setsar=1,scale={int(W*Z)}:-2,crop={W}:{H}:(iw-{W})/2:{OY},"
          f"gblur=sigma={BLUR},unsharp=5:5:0.3:5:5:0,eq=saturation={SAT}:gamma={GAMMA}:contrast={CONTRAST},colorbalance=rs={WARM}:bs={-WARM}:rm={WARM}:bm={-WARM},noise=alls={NOISE}:allf=t+u,"
          f"split={len(BLOCOS)}"+''.join(f'[av{i}]' for i in range(len(BLOCOS)))+';')
fc.append(f"color=c=black:s={W}x{H}:r={FPS}:d={TOTAL/FPS+0.5:.2f}[base];"); cur='[base]'
for i,(f0,f1,blur) in enumerate(BLOCOS):
    b=f",gblur=sigma={BLURP}" if blur else ""
    fc.append(f"[av{i}]trim=start_frame={f0}:end_frame={f1},setpts=PTS-STARTPTS{b},format=rgba,{atrasa(f0)}[c{i}];")
    fc.append(f"{cur}[c{i}]overlay=0:0:eof_action=pass:enable='between(n,{f0},{f1-1})'[s{i}];"); cur=f'[s{i}]'
fc.append(f"[7:v]format=rgba,loop=loop=-1:size=1:start=0,fps={FPS}[shp];[9:v]format=rgba,loop=loop=-1:size=1:start=0,fps={FPS}[shc];[8:v]format=gray,loop=loop=-1:size=1:start=0,fps={FPS}[mk];")
fc.append(f"{cur}[shc]overlay={CARD_X-M}:{CARD_Y-M}:eof_action=pass:enable='between(n,{c0},{c1-1})'[t0];")
fc.append(f"[3:v]fps={FPS},{segura(c1-c0)},format=rgba[cardv];[cardv][mk]alphamerge,{atrasa(c0)}[card];[t0][card]overlay={CARD_X}:{CARD_Y}:eof_action=pass:enable='between(n,{c0},{c1-1})'[t1];")
fc.append(f"[t1][shp]overlay={PAINEL_X-M}:{PAINEL_Y-M}:eof_action=pass:enable='between(n,{a0},{a1-1})+between(n,{b0},{b1-1})'[t2];")
fc.append(f"[1:v]fps={FPS},{segura(a1-a0)},format=rgba,{atrasa(a0)}[pA];[t2][pA]overlay={PAINEL_X}:{PAINEL_Y}:eof_action=pass:enable='between(n,{a0},{a1-1})'[t3];")
fc.append(f"[2:v]fps={FPS},format=rgba,{atrasa(b0)}[pB1];[t3][pB1]overlay={PAINEL_X}:{PAINEL_Y}:eof_action=pass:enable='between(n,{b0},{b0+B1-1})'[t3b];")
fc.append(f"[11:v]fps={FPS},{segura(b1-b0-B1)},format=rgba,{atrasa(b0+B1)}[pB2];[t3b][pB2]overlay={PAINEL_X}:{PAINEL_Y}:eof_action=pass:enable='between(n,{b0+B1},{b1-1})'[t4];")
t1=f'{P}/molde/k/caixa-l1.txt'; t2=f'{P}/molde/k/caixa-l2.txt'; open(t1,'w').write(L1); open(t2,'w').write(L2)
fc.append(f"color=c=0xFE0553:s=868x197:r={FPS}:d={BOX_END/FPS+1:.2f},format=rgb24,"
 f"drawtext=fontfile={FP}:fontsize={BOXSZ}:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:textfile={t1}:x=(w-text_w)/2+5:y=42,"
 f"drawtext=fontfile={FP}:fontsize={BOXSZ}:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:textfile={t2}:x=(w-text_w)/2+5:y=114,"
 f"drawtext=fontfile={FP}:fontsize={BOXSZ}:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:textfile={t1}:x=(w-text_w)/2:y=37,"
 f"drawtext=fontfile={FP}:fontsize={BOXSZ}:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:textfile={t2}:x=(w-text_w)/2:y=109,"
 f"format=rgba[caixa];[t4][caixa]overlay=x=106:y=862:eof_action=pass:enable='lt(n,{BOX_END})'[t4b];")
fc.append(f"[4:v]format=rgba[kar];[t4b][kar]overlay=0:950:eof_action=pass[t5];")
fc.append(f"[5:v]format=rgba,loop=loop=-1:size=6:start=0,fps={FPS},{atrasa(CTA_INI)}[set];[t5][set]overlay=0:0:eof_action=pass:enable='between(n,{CTA_INI},{CTA_FIM-1})'[t6];")
fc.append(f"[6:v]format=rgba,loop=loop=-1:size=8:start=0,fps=15,fps={FPS},{atrasa(CTA_INI)}[cta];[t6][cta]overlay=0:130:eof_action=pass:enable='between(n,{CTA_INI},{CTA_FIM-1})'[v]")
cmd=['ffmpeg','-hide_banner','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','10:a','-c:a','aac','-b:a','192k',
     '-frames:v',str(TOTAL),'-c:v','libx264','-preset','slow','-crf','17','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT]
os.makedirs(f'{P}/conferencia',exist_ok=True); open(f'{P}/conferencia/ultimo-comando.txt','w').write(' '.join(cmd))
subprocess.run(cmd,check=True); print('ok ->',OUT)
