#!/usr/bin/env python3
# AD02-H2 versão WHATSAPP: a edição do AD02-H2 reconstruído (17/09) com copy, áudio, avatar e painéis do funil do Spy Zap.
#   hook (0-191) ......... o do AD02-H2 original, intacto (clipe de reação + manchete; o áudio dele também)
#   áudio (192-fim) ...... locução nova (MiniMax Casual_Guy, pausas cortadas) — audio/vo-zap-ritmo.wav
#   avatar (192-fim) ..... clipe Pruna em tela cheia, plano fixo (Z/OY por env), gblur 18 nos blocos de painel
#   painéis .............. gravação real do go.zappdetect.com (gerar-paineis.sh): card "Accessing cloud backup" (788x252, cantos
#                          arredondados) no bloco 1; mapa TRACKING no bloco 2; chats + rolagem do relatório no bloco 4 — bbox (193,347 · 692x1224)
#   karaokê .............. gerar-karaoke-zap.py, 1 PNG por frame
#   setas e CTA .......... os mesmos assets redesenhados do AD02-H2, nos frames de molde/timeline.json
# Uso (de projects/mentoria-spy/):  python3 .../montar-zap.py <clipe.mp4> <saida.mp4>
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter
P='centerpag-detect/criativos/ad02-h2-zap-2026-09-17'
REF=f'{P}/REFERENCIA-ad02-h2-insta.mov'; VO=f'{P}/audio/vo-zap-ritmo.wav'
CLIPE=sys.argv[1]; OUT=sys.argv[2]
T=json.load(open(f'{P}/molde/timeline.json')); FPS=30; W,H=1080,1920; HOOK_FIM=T['hook_fim']; TOTAL=T['total']
BLUR=float(os.environ.get('BLUR','18')); Z=float(os.environ.get('Z','1.35')); OY=int(os.environ.get('OY','160'))
c0,c1=T['card']; a0,a1=T['painelA']; l0,l1=T['limpo']; b0,b1=T['painelB']; f0_,f1_=T['final']; CTA_INI,CTA_FIM=T['cta']
B1=120  # frames do painel B1 (chats congelado); o resto do bloco é a rolagem do relatório
BLOCOS=[(c0,c1,False),(a0,a1,True),(l0,l1,False),(b0,b1,True),(f0_,f1_,False)]
PAINEL_X,PAINEL_Y,PW,PH=193,347,692,1224
CW,CH=788,252; CARD_X=147; CARD_Y=1568-CH//2      # mesmo centro vertical do card "Connecting" do original (1369+398/2)
M=90
sh=Image.new('RGBA',(PW+2*M,PH+2*M),(0,0,0,0)); ImageDraw.Draw(sh).rectangle([M,M,M+PW,M+PH],fill=(0,0,0,110)); sh.filter(ImageFilter.GaussianBlur(28)).save(f'{P}/assets/sombra-painel.png')
mk=Image.new('L',(CW,CH),0); ImageDraw.Draw(mk).rounded_rectangle([0,0,CW-1,CH-1],radius=30,fill=255); mk.save(f'{P}/assets/mascara-card.png')
shc=Image.new('RGBA',(CW+2*M,CH+2*M),(0,0,0,0)); ImageDraw.Draw(shc).rounded_rectangle([M,M,M+CW,M+CH],radius=30,fill=(0,0,0,100)); shc.filter(ImageFilter.GaussianBlur(26)).save(f'{P}/assets/sombra-card.png')
A=f'{P}/assets/paineis'
inputs=['-i',REF,'-i',CLIPE,'-i',f'{A}/painel-A-mapa.mp4','-i',f'{A}/painel-B1-chats.mp4','-i',f'{A}/card-backup.mp4',
        '-framerate',str(FPS),'-start_number',str(HOOK_FIM),'-i',f'{P}/karaoke/frames/%04d.png',
        '-framerate',str(FPS),'-i',f'{P}/assets/setas/%03d.png','-framerate',str(FPS),'-i',f'{P}/assets/cta/%03d.png',
        '-i',f'{P}/assets/sombra-painel.png','-i',f'{P}/assets/mascara-card.png','-i',f'{P}/assets/sombra-card.png',
        '-i',f'{A}/painel-B2-relatorio.mp4','-i',VO]
def atrasa(ini_frame): return f"tpad=start_duration={ini_frame/FPS:.4f}:start_mode=add:color=0x00000000"
fc=[]
fc.append(f"[1:v]scale={W}:-2:flags=lanczos,fps={FPS},setsar=1,split={len(BLOCOS)}"+''.join(f'[av{i}]' for i in range(len(BLOCOS)))+';')
cur='[0:v]'
for i,(f0,f1,blur) in enumerate(BLOCOS):
    b=f",gblur=sigma={BLUR}" if blur else ""
    fc.append(f"[av{i}]trim=start_frame={f0-HOOK_FIM}:end_frame={f1-HOOK_FIM},setpts=PTS-STARTPTS,scale={int(W*Z)}:-2:flags=lanczos,crop={W}:{H}:(iw-{W})/2:{OY}{b},format=rgba,{atrasa(f0)}[c{i}];")
    fc.append(f"{cur}[c{i}]overlay=0:0:eof_action=pass:enable='between(n,{f0},{f1-1})'[s{i}];"); cur=f'[s{i}]'
fc.append(f"[8:v]format=rgba,loop=loop=-1:size=1:start=0,fps={FPS}[shp];[10:v]format=rgba,loop=loop=-1:size=1:start=0,fps={FPS}[shc];[9:v]format=gray,loop=loop=-1:size=1:start=0,fps={FPS}[mk];")
fc.append(f"{cur}[shc]overlay={CARD_X-M}:{CARD_Y-M}:eof_action=pass:enable='between(n,{c0},{c1-1})'[t0];")
fc.append(f"[4:v]fps={FPS},format=rgba[cardv];[cardv][mk]alphamerge,{atrasa(c0)}[card];[t0][card]overlay={CARD_X}:{CARD_Y}:eof_action=pass:enable='between(n,{c0},{c1-1})'[t1];")
fc.append(f"[t1][shp]overlay={PAINEL_X-M}:{PAINEL_Y-M}:eof_action=pass:enable='between(n,{a0},{a1-1})+between(n,{b0},{b1-1})'[t2];")
fc.append(f"[2:v]fps={FPS},format=rgba,{atrasa(a0)}[pA];[t2][pA]overlay={PAINEL_X}:{PAINEL_Y}:eof_action=pass:enable='between(n,{a0},{a1-1})'[t3];")
fc.append(f"[3:v]fps={FPS},format=rgba,{atrasa(b0)}[pB1];[t3][pB1]overlay={PAINEL_X}:{PAINEL_Y}:eof_action=pass:enable='between(n,{b0},{b0+B1-1})'[t3b];")
fc.append(f"[11:v]fps={FPS},format=rgba,{atrasa(b0+B1)}[pB2];[t3b][pB2]overlay={PAINEL_X}:{PAINEL_Y}:eof_action=pass:enable='between(n,{b0+B1},{b1-1})'[t4];")
fc.append(f"[5:v]format=rgba,{atrasa(HOOK_FIM)}[kar];[t4][kar]overlay=0:950:eof_action=pass:enable='gte(n,{HOOK_FIM})'[t5];")
fc.append(f"[6:v]format=rgba,loop=loop=-1:size=6:start=0,fps={FPS},{atrasa(CTA_INI)}[set];[t5][set]overlay=0:0:eof_action=pass:enable='between(n,{CTA_INI},{CTA_FIM-1})'[t6];")
fc.append(f"[7:v]format=rgba,loop=loop=-1:size=8:start=0,fps=15,fps={FPS},{atrasa(CTA_INI)}[cta];[t6][cta]overlay=0:130:eof_action=pass:enable='between(n,{CTA_INI},{CTA_FIM-1})'[v];")
# áudio: hook do original (0-6,40 s) + locução nova, em estéreo 44,1k
fc.append(f"[0:a]atrim=0:{HOOK_FIM/FPS:.4f},asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[ah];[12:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,apad=whole_dur={(TOTAL-HOOK_FIM)/FPS:.4f}[av];[ah][av]concat=n=2:v=0:a=1[a]")
cmd=['ffmpeg','-hide_banner','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','[a]','-c:a','aac','-b:a','192k',
     '-frames:v',str(TOTAL),'-t',f'{TOTAL/FPS:.4f}','-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p',
     '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT]
os.makedirs(f'{P}/conferencia',exist_ok=True); open(f'{P}/conferencia/ultimo-comando.txt','w').write(' '.join(cmd))
subprocess.run(cmd,check=True); print('ok ->',OUT)
