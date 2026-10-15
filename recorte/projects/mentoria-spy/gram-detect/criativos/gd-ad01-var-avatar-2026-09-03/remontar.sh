#!/bin/bash
# remontar.sh — reconstrói a edição do GD-AD01 (8 blocos, seções 5/6 do teardown) em cima de um talking head novo.
#   bash gram-detect/criativos/gd-ad01-var-avatar-2026-09-03/remontar.sh <talking-head.mp4> [saida.mp4]
# O talking head pode ser mudo ou com áudio: o áudio da saída é SEMPRE o do campeão (voz original).
# Painéis, card, story, caixa do gancho e setas são RECORTADOS do próprio GD-AD01.mp4 nos mesmos instantes;
# o karaokê branco é re-queimado (Inter Bold 69 px, glow escuro) a partir de molde/karaoke.tsv nos estados
# em que ele fica sobre o rosto (C, D1, bloco 8). Nos estados A, B e E ele já vem dentro do recorte do campeão.
# Custo zero. Teste do molde: passar o próprio GD-AD01.mp4 como talking head → saída ≈ campeão.
set -euo pipefail
cd "$(dirname "$0")/../../.."
TH="${1:?uso: remontar.sh talking-head.mp4 [saida.mp4]}"
OUT="${2:-gram-detect/criativos/gd-ad01-var-avatar-2026-09-03/GD-AD01-D-remontado.mp4}"
CH=criativos-crus/spy-gram/ads-en/GD-AD01.mp4
M=gram-detect/criativos/gd-ad01-var-avatar-2026-09-03/molde
F=gram-detect/scripts/fonts/Inter-Bold.ttf
# Janela vertical do rosto por bloco. O talking head pode ser uma TELA ALTA (1080 x H, H >= 1920): cada bloco recorta
# uma janela 1080x1920 a partir de OFF_* px do topo. O campeão enquadra o rosto mais alto quando há painel embaixo
# (olhos a ~19% da altura no A, ~24% no D1, ~22% no bloco 8, contra ~37% nos blocos C de rosto cheio), então
# OFF_A > OFF_D1, OFF_8 > OFF_C. Tudo zero = rosto como veio (teste do molde com o campeão 1080x1920).
OFF_C="${OFF_C:-0}"; OFF_A="${OFF_A:-0}"; OFF_D1="${OFF_D1:-0}"; OFF_8="${OFF_8:-0}"

# ---- Geometria medida no campeão (1080x1920, 30 fps, 978 frames) ----
# Blocos (frame): A 0-233 | B 234-320 | C1 321-491 | E 492-590 | C2 591-665 | D1 666-776 | C3 777-875 | 8 876-977
# A : rosto até ~1160; caixa rosa x106-973 y862-1058; painel do app entra por degradê ~1150-1230; karaokê base y1209 (topo 1160),
#     re-queimado por cima porque o degradê deixa o karaokê do recorte translúcido
# B : card Gram Detect x89-990 y240-1679 sobre o rosto desfocado; karaokê dentro do card
# C : rosto cheio; karaokê base y1521 (topo do ascendente 1472)
# E : story bloqueado em quadro cheio (recorte inteiro do campeão)
# D1: rosto 0-957; fundo pêssego + pill + painel do campeão de 957 pra baixo; karaokê base y984 (topo 935), montado na costura
# 8 : rosto cheio; card escuro flutuante (escuro em x102-977, y1101-1849) com glitch + setas, recortado x96-983 y1098-1773
#     com cantos arredondados (mask-8.png) pra não trazer o moletom do campeão; karaokê base y1102 (topo 1053)
# Karaokê: Inter Bold 69 px (7 larguras medidas, erro 0,4%), branco #FCFCFC, glow escuro ~5 px

# máscara do degradê do estado A: 1080x770 = y 1150-1919; alpha 0→255 nas 80 primeiras linhas
python3 - "$M" <<'PY'
import sys; from PIL import Image; import numpy as np
M=sys.argv[1]; a=np.full((770,1080),255,np.uint8); a[:80]=np.linspace(0,255,80).astype(np.uint8)[:,None]
Image.fromarray(a,'L').save(f'{M}/mask-A.png')
# máscara do card do bloco 8: 888x676 com cantos arredondados (r=40) — recorte x 96-983, y 1098-1773 (a sombra cinza abaixo do card fica de fora); fora do card fica o rosto novo
from PIL import ImageDraw
m=Image.new('L',(888,676),0); ImageDraw.Draw(m).rounded_rectangle([0,0,887,675],radius=40,fill=255); m.save(f'{M}/mask-8.png')
PY

# karaokê → cadeia de drawtext (2 passadas: glow + texto com contorno fino)
KAR=$(python3 - "$M" "$F" <<'PY'
import sys,os
M,F=sys.argv[1],sys.argv[2]; os.makedirs(f'{M}/k',exist_ok=True)
Y={'A':1160,'C':1472,'D1':935,'D2':1053}   # topo do ascendente = base - 49 (calibrado no drawtext); A re-queimado porque o recorte com degradê deixa o karaokê do campeão translúcido
out=[]
for i,l in enumerate(open(f'{M}/karaoke.tsv')):
    if l.startswith('#') or not l.strip(): continue
    a,b,st,txt=l.rstrip('\n').split('\t')[:4]
    if st not in Y: continue
    p=f'{M}/k/{i:02d}.txt'; open(p,'w').write(txt)
    c=f"drawtext=fontfile={F}:textfile={p}:fontsize=69:x=(w-text_w)/2:y={Y[st]}:enable='between(n\\,{a}\\,{int(b)-1})'"
    out.append(f"{c}:fontcolor=0x000000@0.0:borderw=9:bordercolor=0x000000@0.35")
    out.append(f"{c}:fontcolor=0xFCFCFC:borderw=4:bordercolor=0x0C0B0C@0.95")
print(','.join(out))
PY
)

ffmpeg -v error -y -i "$TH" -i "$CH" -loop 1 -i "$M/mask-A.png" -loop 1 -i "$M/mask-8.png" -filter_complex "\
[0:v]scale=1080:-2:flags=lanczos,pad=1080:'max(ih\,1920)':0:0,fps=30,tpad=stop_mode=clone:stop_duration=40,trim=end_frame=978,setpts=PTS-STARTPTS,format=yuv420p,split=4[th0][thA0][thD0][th80];\
[th0]crop=1080:1920:0:${OFF_C},split=2[th][thb];\
[thA0]crop=1080:1920:0:${OFF_A}[thA];\
[thD0]crop=1080:1920:0:${OFF_D1}[thD];\
[th80]crop=1080:1920:0:${OFF_8}[th8];\
[thb]boxblur=luma_radius=25:luma_power=2:chroma_radius=12:chroma_power=2[blur];\
[1:v]fps=30,format=yuv420p,split=6[c1][c2][c3][c4][c5][c6];\
[2:v]fps=30,format=gray[mA];\
[3:v]fps=30,format=gray[m8];\
[c1]crop=1080:770:0:1150,format=yuva420p[cA0];[cA0][mA]alphamerge[cA];\
[c2]crop=868:197:106:862[box];\
[c3]crop=902:1440:89:240[cardB];\
[c5]crop=1080:963:0:957[cD1];\
[c6]crop=888:676:96:1098,format=yuva420p[cD20];[cD20][m8]alphamerge[cD2];\
[th][thA]overlay=eof_action=pass:enable='lt(n,234)'[v0a];\
[v0a][thD]overlay=eof_action=pass:enable='between(n,666,776)'[v0b];\
[v0b][th8]overlay=eof_action=pass:enable='gte(n,876)'[v0];\
[v0][blur]overlay=eof_action=pass:enable='between(n,234,320)'[v1];\
[v1][cA]overlay=y=1150:eof_action=pass:enable='lt(n,234)'[v2];\
[v2][box]overlay=x=106:y=862:eof_action=pass:enable='lt(n,234)'[v3];\
[v3][cardB]overlay=x=89:y=240:eof_action=pass:enable='between(n,234,320)'[v4];\
[v4][c4]overlay=eof_action=pass:enable='between(n,492,590)'[v5];\
[v5][cD1]overlay=y=957:eof_action=pass:enable='between(n,666,776)'[v6];\
[v6][cD2]overlay=x=96:y=1098:eof_action=pass:enable='gte(n,876)'[v7];\
[v7]${KAR}[v]" \
  -map "[v]" -map 1:a -c:a copy \
  -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -movflags +faststart "$OUT"
echo "ok -> $OUT"
