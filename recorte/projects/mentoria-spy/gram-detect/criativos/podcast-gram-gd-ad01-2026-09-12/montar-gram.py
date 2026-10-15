#!/usr/bin/env python3
# Podcast Gram (GD-AD01 em formato podcast). Monta a peça final de uma vez: clipes por cena (MiniMax H3 768p 24 fps, áudio embutido =
# TTS com lipsync), pausas removidas (molde/timeline.py), caixa do campeão até o fim da cena 2, splits nas cenas 3/6/7 com os painéis
# recortados do próprio GD-AD01 (painel/), karaokê (molde/karaoke.tsv), trilha de suspense a 9 %. Saída 1080x1920 30 fps.
# Uso (de projects/mentoria-spy/):  python3 .../montar-gram.py [saida.mp4]   · CLIPES=<pasta>  · SEM_MUSICA=1
import json, os, subprocess, sys
P='gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12'
CL=os.environ.get('CLIPES',f'{P}/clipes'); OUT=sys.argv[1] if len(sys.argv)>1 else f'{P}/PODCAST-GRAM-gd-ad01-funil-musica.mp4'
MUS='gram-detect/criativos/podcast-hook-polemico-2026-09-05/audio/musica-7y4kJtkioFk.m4a'; MUSVOL=0.09
FP='gram-detect/scripts/fonts/Poppins-Bold.ttf'; FI='gram-detect/scripts/fonts/Inter-Bold.ttf'
L1=os.environ.get('CAIXA_L1',"I found something I wasn't"); L2=os.environ.get('CAIXA_L2','even looking for...'); BOXSZ=int(os.environ.get('BOXSZ',62))
TL=os.environ.get('TL',f'{P}/molde/timeline.json'); KARF=os.environ.get('KAR',f'{P}/molde/karaoke.tsv'); KDIR=os.environ.get('KDIR',f'{P}/molde/k')   # caixa do campeão: caixa mista, reticências (62 px: linha 1 = 844 px < 868)
SPLIT={3:int(os.environ.get('Y3',240)),6:int(os.environ.get('Y6',270)),7:int(os.environ.get('Y7',200))}   # y do recorte do rosto por cena
PY={3:1000,6:1000,7:1120}; PH={3:920,6:920,7:800}           # painel: y de entrada e altura (bloco 8 do campeão é mais baixo)
KY_FULL=1472; KY={3:890,6:890,7:1010}                        # karaokê: rosto cheio 78 %; nos splits logo acima do painel
subprocess.run(['python3',f'{P}/molde/timeline.py',CL],check=True)
subprocess.run(['python3',f'{P}/molde/karaoke-tempos.py'],check=True)
T=json.load(open(TL)); FPS=T['fps']; TOTAL=T['total_frames']; SC=T['scenes']
S=lambda i:SC[i-1]['out_start']; E=lambda i:SC[i-1]['out_start']+SC[i-1]['out_frames']
BOX_END=E(2)
# troca card → interceptação na cena 6: fim do bloco "the username"
KAR=[l.rstrip('\n').split('\t') for l in open(KARF) if not l.startswith('#') and l.strip()]
SW=[int(b) for a,b,st,t in KAR if t=='the username' and S(6)<=int(a)<E(6)][0]
print(f'total {TOTAL} fr = {TOTAL/FPS:.2f}s · caixa até {BOX_END} · splits c3 {S(3)}-{E(3)} c6 {S(6)}-{E(6)} (card→intercept no {SW}) c7 {S(7)}-{E(7)}')
inputs=[]; fc=[]; vs=[]; as_=[]
for idx,sc in enumerate(SC):
    inputs+=['-i',sc['clip']]; k=len(sc['segments'])
    fc.append(f"[{idx}:v]split={k}"+''.join(f'[v{idx}_{j}]' for j in range(k))+';')
    fc.append(f"[{idx}:a]asplit={k}"+''.join(f'[a{idx}_{j}]' for j in range(k))+';')
    for j,((s,e),fr) in enumerate(zip(sc['segments'],sc['seg_frames'])):
        fc.append(f"[v{idx}_{j}]trim=start={s}:end={e},setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,fps={FPS},tpad=stop_mode=clone:stop_duration=2,trim=end_frame={fr},setpts=PTS-STARTPTS,format=yuv420p[sv{idx}_{j}];")
        fc.append(f"[a{idx}_{j}]atrim=start={s}:end={e},asetpts=PTS-STARTPTS,aformat=sample_rates=44100:channel_layouts=stereo,apad,atrim=end_sample={fr*1470},asetpts=PTS-STARTPTS[sa{idx}_{j}];")
        vs.append(f'[sv{idx}_{j}]'); as_.append(f'[sa{idx}_{j}]')
n=len(vs); fc.append(''.join(v+a for v,a in zip(vs,as_))+f'concat=n={n}:v=1:a=1[base][voz];')
# painéis (recortes do GD-AD01) — 7 story · 8 card · 9 intercept · 10 fim
NP=len(SC); inputs+=['-i',f'{P}/painel/story.mp4','-i',f'{P}/painel/card.mp4','-i',f'{P}/painel/intercept.mp4','-i',f'{P}/painel/fim.mp4']
def panel(src,frames,start,name):   # segura o último frame até o fim do trecho; transparente até o frame de entrada
    fc.append(f"[{src}:v]fps={FPS},tpad=stop_mode=clone:stop_duration=12,trim=end_frame={frames},setpts=PTS-STARTPTS,format=rgba,tpad=start_duration={start/FPS:.4f}:start_mode=add:color=0x00000000[{name}];")
panel(NP,E(3)-S(3),S(3),'p3'); panel(NP+1,SW-S(6),S(6),'p6a'); panel(NP+2,E(6)-SW,SW,'p6b'); panel(NP+3,E(7)-S(7),S(7),'p7')
# rosto em cima nos splits: recorte da própria base, deslocado por cena
fc.append(f"[base]split=3[b0][bt1][bt2];[bt1]crop=1080:1000:0:'if(lt(n\\,{S(4)})\\,{SPLIT[3]}\\,{SPLIT[6]})'[top1];[bt2]crop=1080:1120:0:{SPLIT[7]}[top2];")
fc.append(f"[b0][top1]overlay=0:0:eof_action=pass:enable='between(n\\,{S(3)}\\,{E(3)-1})+between(n\\,{S(6)}\\,{E(6)-1})'[v0];[v0][top2]overlay=0:0:eof_action=pass:enable='gte(n\\,{S(7)})'[v1];")
fc.append(f"[v1][p3]overlay=x=0:y={PY[3]}:eof_action=pass:enable='between(n,{S(3)},{E(3)-1})'[v2];")
fc.append(f"[v2][p6a]overlay=x=0:y={PY[6]}:eof_action=pass:enable='between(n,{S(6)},{SW-1})'[v3];")
fc.append(f"[v3][p6b]overlay=x=0:y={PY[6]}:eof_action=pass:enable='between(n,{SW},{E(6)-1})'[v4];")
fc.append(f"[v4][p7]overlay=x=0:y={PY[7]}:eof_action=pass:enable='gte(n,{S(7)})'[v5];")
# caixa do gancho (campeão: x106-973 y862-1058, RGB→bt709), caixa mista com reticências
t1=f'{KDIR}/caixa-l1.txt'; t2=f'{KDIR}/caixa-l2.txt'; os.makedirs(KDIR,exist_ok=True)
open(t1,'w').write(L1); open(t2,'w').write(L2)
fc.append(f"color=c=0xFE0553:s=868x197:r={FPS}:d={BOX_END/FPS+1:.2f},format=rgb24,"
 f"drawtext=fontfile={FP}:fontsize={BOXSZ}:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:textfile={t1}:x=(w-text_w)/2+5:y=40,"
 f"drawtext=fontfile={FP}:fontsize={BOXSZ}:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:textfile={t2}:x=(w-text_w)/2+5:y=114,"
 f"drawtext=fontfile={FP}:fontsize={BOXSZ}:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:textfile={t1}:x=(w-text_w)/2:y=35,"
 f"drawtext=fontfile={FP}:fontsize={BOXSZ}:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:textfile={t2}:x=(w-text_w)/2:y=109,"
 f"scale=out_color_matrix=bt709:out_range=tv,format=yuv420p[caixa];[v5][caixa]overlay=x=106:y=862:eof_action=pass:enable='lt(n,{BOX_END})'[v6];")
# karaokê
os.makedirs(KDIR,exist_ok=True); kar=[]
def ky(f):
    for i in (3,6,7):
        if S(i)<=f<E(i): return KY[i]
    return KY_FULL
for i,(a,b,st,txt) in enumerate(KAR):
    p=f'{KDIR}/{i:02d}.txt'; open(p,'w').write(txt)
    c=f"drawtext=fontfile={FI}:textfile={p}:fontsize=69:x=(w-text_w)/2:y={ky(int(a))}:enable='between(n\\,{a}\\,{int(b)-1})'"
    kar.append(f"{c}:fontcolor=0x000000@0.0:borderw=9:bordercolor=0x000000@0.35"); kar.append(f"{c}:fontcolor=0xFCFCFC:borderw=4:bordercolor=0x0C0B0C@0.95")
fc.append('[v6]'+','.join(kar)+'[v];')
# música: 9 % por baixo da voz, fade in 1 s / out 2,5 s, sem normalizar a voz
if os.environ.get('SEM_MUSICA'): fc.append('[voz]anull[aout]')
else:
    inputs+=['-i',MUS]; MI=NP+4; dur=TOTAL/FPS
    fc.append(f"[{MI}:a]aformat=sample_rates=44100:channel_layouts=stereo,atrim=end={dur:.3f},volume={MUSVOL},afade=t=in:d=1,afade=t=out:st={dur-2.5:.3f}:d=2.5[mus];[voz][mus]amix=inputs=2:duration=first:normalize=0[aout]")
cmd=['ffmpeg','-hide_banner','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','[aout]','-frames:v',str(TOTAL),'-t',f'{TOTAL/FPS:.4f}',
 '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',
 '-c:a','aac','-b:a','192k','-movflags','+faststart',OUT]
open(f'{KDIR}/ultimo-comando.txt','w').write(' '.join(cmd))
subprocess.run(cmd,check=True); print('ok ->',OUT)
