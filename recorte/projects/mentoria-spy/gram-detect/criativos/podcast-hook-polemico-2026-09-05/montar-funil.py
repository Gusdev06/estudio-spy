#!/usr/bin/env python3
# Podcast Zap — versão COM FUNIL (Gusta, 05/09). Mesma timeline da peça (molde/timeline.json), mesmo áudio da versão com música
# (copiado sem reencode). Cenas 3, 6 e 7 viram split 50/50 (estado D do GD-AD01): rosto em cima (0-960), funil gravado embaixo
# (960-1920), recortado da gravação do go.zappdetect.com (1170x2532 60 fps) sem barra do Safari nem URL. Karaokê a y 890 nos splits
# (logo acima do painel), 1472 nos rostos cheios. Setas do campeão por cima do painel na cena 7. Corte seco entre estados. Custo zero.
# Uso (de projects/mentoria-spy/):  python3 .../montar-funil.py [saida.mp4]
import json, os, subprocess, sys
P='gram-detect/criativos/podcast-hook-polemico-2026-09-05'
OUT=sys.argv[1] if len(sys.argv)>1 else f'{P}/PODCAST-ZAP-hook-faithful-man-funil.mp4'
MUS=f'{P}/PODCAST-ZAP-hook-faithful-man-musica.mp4'
REC='EDIÇÃO 3/EDIÇAO ANIMADA/ScreenRecording_08-13-2026 19-56-53_1.MP4'
FP='gram-detect/scripts/fonts/Poppins-Bold.ttf'; FI='gram-detect/scripts/fonts/Inter-Bold.ttf'
L1='A FAITHFUL MAN HAS'; L2='NO DELETED MESSAGES.'
T=json.load(open(f'{P}/molde/timeline.json')); FPS=T['fps']; TOTAL=T['total_frames']; SC=T['scenes']
S=lambda i:SC[i-1]['out_start']; E=lambda i:SC[i-1]['out_start']+SC[i-1]['out_frames']   # frames [S,E)
BOX_END=E(2); SETAS_INI=TOTAL-90
SPLIT={3:440,6:286,7:400}   # cena -> y do recorte 1080x960 do rosto (olhos a ~30% do painel de cima)
KY_SPLIT=890; KY_FULL=1472; PY=960
print(f'total {TOTAL} · cena3 {S(3)}-{E(3)} · cena6 {S(6)}-{E(6)} · cena7 {S(7)}-{E(7)} · setas {SETAS_INI}')
# ---- gravação do funil: trechos (segundos no arquivo) ----
# cena 3 (162 fr = 5,40 s): 'Restoring deleted data' + mapa TRACKING, rec 116,0-121,4, recorte y 1110-2150 (sem o card do perfil = sem número)
# cena 6 (186 fr): a) rec 0,00-2,17 landing → toque → teclado (65 fr) · b) rec 2,0-7,0 digitando, 4,4x (34 fr, começa em 'you type' = fr 65)
#                  · c1) rec 7,0 número completo (4 fr) · c2) rec 23,6-26,4 'Accessing cloud backup' + mapa (83 fr). Campo do número desfocado em b/c1.
# cena 7 (97 fr): 'Scan Complete — Red Flags Found' + 257/19/34, frame congelado em 188,05 s, recorte y 960-2000 (a página rola rápido ali; frame salvo em molde/painel-fim-188.05.png)
FA,FB,FC1=65,34,4; FC2=SC[5]['out_frames']-FA-FB-FC1
inputs=[]
for sc in SC: inputs+=['-i',sc['clip']]                       # 0..6
inputs+=['-framerate',str(FPS),'-i',f'{P}/setas/%03d.png']       # 7
for ss,t in [(0,2.3),(2.0,5.1),(7.0,0.2),(23.6,2.95),(116.0,5.6)]: inputs+=['-ss',str(ss),'-t',str(t),'-i',REC]  # 8..12
inputs+=['-loop','1','-framerate',str(FPS),'-t','4','-i',f'{P}/molde/painel-fim-188.05.png']  # 13: frame congelado da cena 7 (ffmpeg -ss 188.05 -frames:v 1)
inputs+=['-i',MUS]                                               # 14 (áudio)
fc=[]; vs=[]; as_=[]
for idx,sc in enumerate(SC):
    k=len(sc['segments']); fc.append(f"[{idx}:v]split={k}"+''.join(f'[v{idx}_{j}]' for j in range(k))+';')
    for j,((s,e),fr) in enumerate(zip(sc['segments'],sc['seg_frames'])):
        fc.append(f"[v{idx}_{j}]trim=start={s}:end={e},setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,fps={FPS},tpad=stop_mode=clone:stop_duration=2,trim=end_frame={fr},setpts=PTS-STARTPTS,format=yuv420p[sv{idx}_{j}];")
        vs.append(f'[sv{idx}_{j}]')
fc.append(''.join(vs)+f'concat=n={len(vs)}:v=1:a=0[base];')
# rosto em cima nos splits: recorte 1080x960 da própria base, deslocado por cena
ysel=f"if(lt(n\\,{S(4)})\\,{SPLIT[3]}\\,if(lt(n\\,{S(7)})\\,{SPLIT[6]}\\,{SPLIT[7]}))"
en_split=f"between(n\\,{S(3)}\\,{E(3)-1})+between(n\\,{S(6)}\\,{E(6)-1})+gte(n\\,{S(7)})"
fc.append(f"[base]split=2[b0][bt];[bt]crop=1080:960:0:'{ysel}'[top];[b0][top]overlay=0:0:eof_action=pass:enable='{en_split}'[v0];")
# painéis do funil (1080x960, rgba, atrasados com transparência até o frame de entrada — mesma manobra das setas)
def panel(src,crop,extra,frames,start,name):
    fc.append(f"[{src}]{extra}crop={crop},scale=1080:960:flags=lanczos,fps={FPS},tpad=stop_mode=clone:stop_duration=4,trim=end_frame={frames},setpts=PTS-STARTPTS,format=rgba,tpad=start_duration={start/FPS:.4f}:start_mode=add:color=0x00000000[{name}];")
CROP_MAPA='1170:1040:0:1110'; CROP_FORM='1150:1022:10:110'; CROP_FIM='1170:1040:0:960'
BLUR="split=2[bl0][bl1];[bl1]crop=340:178:690:633,boxblur=22:2[blb];[bl0][blb]overlay=690:633,"   # campo do número (x 690-1030, y 633-811 na gravação)
panel('12:v',CROP_MAPA,'',E(3)-S(3),S(3),'p3')
fc.append(f"[8:v]crop={CROP_FORM},scale=1080:960:flags=lanczos,fps={FPS},trim=end_frame={FA},setpts=PTS-STARTPTS[p6a];")
fc.append(f"[9:v]{BLUR}crop={CROP_FORM},scale=1080:960:flags=lanczos,setpts=PTS/4.4,fps={FPS},trim=end_frame={FB},setpts=PTS-STARTPTS[p6b];")
fc.append(f"[10:v]{BLUR}crop={CROP_FORM},scale=1080:960:flags=lanczos,fps={FPS},tpad=stop_mode=clone:stop_duration=1,trim=end_frame={FC1},setpts=PTS-STARTPTS[p6c1];")
fc.append(f"[11:v]crop={CROP_MAPA},scale=1080:960:flags=lanczos,fps={FPS},tpad=stop_mode=clone:stop_duration=1,trim=end_frame={FC2},setpts=PTS-STARTPTS[p6c2];")
fc.append(f"[p6a][p6b][p6c1][p6c2]concat=n=4:v=1:a=0,format=rgba,tpad=start_duration={S(6)/FPS:.4f}:start_mode=add:color=0x00000000[p6];")
panel('13:v',CROP_FIM,'',E(7)-S(7),S(7),'p7')
fc.append(f"[v0][p3]overlay=x=0:y={PY}:eof_action=pass:enable='between(n,{S(3)},{E(3)-1})'[v1];")
fc.append(f"[v1][p6]overlay=x=0:y={PY}:eof_action=pass:enable='between(n,{S(6)},{E(6)-1})'[v2];")
fc.append(f"[v2][p7]overlay=x=0:y={PY}:eof_action=pass:enable='gte(n,{S(7)})'[v3];")
# caixa do hook (campeão: x106-973 y862-1058, RGB→bt709) — cenas 1-2
fc.append(f"color=c=0xFE0553:s=868x197:r={FPS}:d={BOX_END/FPS+1:.2f},format=rgb24,"
 f"drawtext=fontfile={FP}:fontsize=60:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:text='{L1}':x=(w-text_w)/2+5:y=42,"
 f"drawtext=fontfile={FP}:fontsize=60:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:text='{L2}':x=(w-text_w)/2+5:y=116,"
 f"drawtext=fontfile={FP}:fontsize=60:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:text='{L1}':x=(w-text_w)/2:y=37,"
 f"drawtext=fontfile={FP}:fontsize=60:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:text='{L2}':x=(w-text_w)/2:y=111,"
 f"scale=out_color_matrix=bt709:out_range=tv,format=yuv420p[caixa];[v3][caixa]overlay=x=106:y=862:eof_action=pass:enable='lt(n,{BOX_END})'[v4];")
# setas do GD-AD01 por cima do painel, últimos 3 s
fc.append(f"[7:v]format=rgba,loop=loop=2:size=94:start=0,tpad=start_duration={SETAS_INI/FPS:.4f}:start_mode=add:color=0x00000000[setas];[v4][setas]overlay=x=340:y=1290:eof_action=pass:enable='gte(n,{SETAS_INI})'[v5];")
# karaokê
os.makedirs(f'{P}/molde/k',exist_ok=True); kar=[]
def split_at(f): return (S(3)<=f<E(3)) or (S(6)<=f<E(6)) or f>=S(7)
for i,l in enumerate(open(f'{P}/molde/karaoke.tsv')):
    if l.startswith('#') or not l.strip(): continue
    a,b,st,txt=l.rstrip('\n').split('\t')[:4]; p=f'{P}/molde/k/{i:02d}.txt'; open(p,'w').write(txt)
    y=KY_SPLIT if split_at(int(a)) else KY_FULL
    c=f"drawtext=fontfile={FI}:textfile={p}:fontsize=69:x=(w-text_w)/2:y={y}:enable='between(n\\,{a}\\,{int(b)-1})'"
    kar.append(f"{c}:fontcolor=0x000000@0.0:borderw=9:bordercolor=0x000000@0.35"); kar.append(f"{c}:fontcolor=0xFCFCFC:borderw=4:bordercolor=0x0C0B0C@0.95")
fc.append('[v5]'+','.join(kar)+'[v]')
cmd=['ffmpeg','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','14:a','-c:a','copy','-frames:v',str(TOTAL),'-t',f'{TOTAL/FPS:.4f}',
 '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT]
open(f'{P}/molde/ultimo-comando-funil.txt','w').write(' '.join(cmd))
subprocess.run(cmd,check=True); print('ok ->',OUT)
