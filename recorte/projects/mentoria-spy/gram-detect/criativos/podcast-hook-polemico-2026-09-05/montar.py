#!/usr/bin/env python3
# Podcast Zap — hook polêmico. Monta a peça: clipes por cena (MiniMax H3, 768p 24 fps, áudio embutido = TTS com lipsync),
# pausas removidas (molde/timeline.py), caixa do hook até o fim da cena 2, karaokê (molde/karaoke.tsv), setas do GD-AD01
# nos últimos 3 s, saída 1080x1920 30 fps. Uso (de projects/mentoria-spy/):  python3 .../montar.py [saida.mp4]   · CLIPES=<pasta>
import json, os, subprocess, sys
P='gram-detect/criativos/podcast-hook-polemico-2026-09-05'
CL=os.environ.get('CLIPES',f'{P}/clipes'); OUT=sys.argv[1] if len(sys.argv)>1 else f'{P}/PODCAST-ZAP-hook-faithful-man.mp4'
FP='gram-detect/scripts/fonts/Poppins-Bold.ttf'; FI='gram-detect/scripts/fonts/Inter-Bold.ttf'
L1='A FAITHFUL MAN HAS'; L2='NO DELETED MESSAGES.'
subprocess.run(['python3',f'{P}/molde/timeline.py',CL],check=True)
subprocess.run(['python3',f'{P}/molde/karaoke-tempos.py'],check=True)
T=json.load(open(f'{P}/molde/timeline.json')); FPS=T['fps']; TOTAL=T['total_frames']
BOX_END=T['scenes'][1]['out_start']+T['scenes'][1]['out_frames']; SETAS_INI=TOTAL-90
print(f'total {TOTAL} frames = {TOTAL/FPS:.2f}s · caixa até o frame {BOX_END} ({BOX_END/FPS:.2f}s) · setas do frame {SETAS_INI} ({SETAS_INI/FPS:.2f}s)')
inputs=[]; fc=[]; vs=[]; as_=[]
for idx,sc in enumerate(T['scenes']):
    inputs+=['-i',sc['clip']]; k=len(sc['segments'])
    fc.append(f"[{idx}:v]split={k}"+''.join(f'[v{idx}_{j}]' for j in range(k))+';')
    fc.append(f"[{idx}:a]asplit={k}"+''.join(f'[a{idx}_{j}]' for j in range(k))+';')
    for j,((s,e),fr) in enumerate(zip(sc['segments'],sc['seg_frames'])):
        fc.append(f"[v{idx}_{j}]trim=start={s}:end={e},setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,fps={FPS},tpad=stop_mode=clone:stop_duration=2,trim=end_frame={fr},setpts=PTS-STARTPTS,format=yuv420p[sv{idx}_{j}];")
        fc.append(f"[a{idx}_{j}]atrim=start={s}:end={e},asetpts=PTS-STARTPTS,aformat=sample_rates=44100:channel_layouts=stereo,apad,atrim=end_sample={fr*1470},asetpts=PTS-STARTPTS[sa{idx}_{j}];")
        vs.append(f'[sv{idx}_{j}]'); as_.append(f'[sa{idx}_{j}]')
n=len(vs); fc.append(''.join(v+a for v,a in zip(vs,as_))+f'concat=n={n}:v=1:a=1[base][aout];')
# caixa do hook (campeão: x106-973 y862-1058, RGB→bt709)
fc.append(f"color=c=0xFE0553:s=868x197:r={FPS}:d={BOX_END/FPS+1:.2f},format=rgb24,"
 f"drawtext=fontfile={FP}:fontsize=60:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:text='{L1}':x=(w-text_w)/2+5:y=42,"
 f"drawtext=fontfile={FP}:fontsize=60:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:text='{L2}':x=(w-text_w)/2+5:y=116,"
 f"drawtext=fontfile={FP}:fontsize=60:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:text='{L1}':x=(w-text_w)/2:y=37,"
 f"drawtext=fontfile={FP}:fontsize=60:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:text='{L2}':x=(w-text_w)/2:y=111,"
 f"scale=out_color_matrix=bt709:out_range=tv,format=yuv420p[caixa];[base][caixa]overlay=x=106:y=862:eof_action=pass:enable='lt(n,{BOX_END})'[v1];")
# setas (94 PNG RGBA do GD-AD01) nos últimos 3 s
NS=len(T['scenes']); inputs+=['-framerate',str(FPS),'-i',f'{P}/setas/%03d.png']
fc.append(f"[{NS}:v]format=rgba,loop=loop=2:size=94:start=0,tpad=start_duration={SETAS_INI/FPS:.4f}:start_mode=add:color=0x00000000[setas];[v1][setas]overlay=x=340:y=1290:eof_action=pass:enable='gte(n,{SETAS_INI})'[v2];")
# karaokê
os.makedirs(f'{P}/molde/k',exist_ok=True); kar=[]
for i,l in enumerate(open(f'{P}/molde/karaoke.tsv')):
    if l.startswith('#') or not l.strip(): continue
    a,b,st,txt=l.rstrip('\n').split('\t')[:4]; p=f'{P}/molde/k/{i:02d}.txt'; open(p,'w').write(txt)
    y=1201 if int(a)>=T['scenes'][-1]['out_start'] else 1472   # cena 7: karaokê sobe pra cima das setas (base y 1250), senão fica branco sobre branco
    c=f"drawtext=fontfile={FI}:textfile={p}:fontsize=69:x=(w-text_w)/2:y={y}:enable='between(n\\,{a}\\,{int(b)-1})'"
    kar.append(f"{c}:fontcolor=0x000000@0.0:borderw=9:bordercolor=0x000000@0.35"); kar.append(f"{c}:fontcolor=0xFCFCFC:borderw=4:bordercolor=0x0C0B0C@0.95")
fc.append('[v2]'+','.join(kar)+'[v]')
cmd=['ffmpeg','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','[aout]','-frames:v',str(TOTAL),'-t',f'{TOTAL/FPS:.4f}',
 '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',
 '-c:a','aac','-b:a','192k','-movflags','+faststart',OUT]
open(f'{P}/molde/ultimo-comando.txt','w').write(' '.join(cmd))
subprocess.run(cmd,check=True); print('ok ->',OUT)
