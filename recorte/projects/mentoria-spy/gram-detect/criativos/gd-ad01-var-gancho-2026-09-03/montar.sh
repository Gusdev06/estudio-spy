#!/bin/bash
# GD-AD01 — variação B: só o texto da caixa rosa do gancho (frames 0–233). Custo zero.
# Roda a partir de qualquer lugar:  bash gram-detect/criativos/gd-ad01-var-gancho-2026-09-03/montar.sh
set -e
cd "$(dirname "$0")/../../.."
IN=criativos-crus/spy-gram/ads-en/GD-AD01.mp4
F=gram-detect/scripts/fonts/Poppins-Bold.ttf
OUT=gram-detect/criativos/gd-ad01-var-gancho-2026-09-03/GD-AD01-B-caixa-supposed.mp4
L1='I wasn’t even supposed'
L2='to see this...'
# Medido no original (frame t=1 s, PNG decodificado com a tag bt709 do arquivo):
#   caixa x 106–973, y 862–1058 (868×197), cor decodificada #FE0553, some no frame 234 (7,800 s)
#   texto Poppins Bold 60 px, amarelo #EEFC00, contorno 2 px + sombra +5/+5 px em #2C040A
#   linha 1 topo y 899 (asc.), linha 2 topo y 974; centro x 540
# A caixa é uma camada RGB OPACA do tamanho exato (868×197): drawbox/drawtext em RGB (cores exatas),
# convertida pra YUV com bt709 e sobreposta em (106,862). Fora dela o vídeo passa intocado.
# (drawbox/drawtext direto no yuv420p usam matriz bt601 e desviam o matiz: #F91A51 em vez de #FE0553.)
ffmpeg -v error -y -i "$IN" -filter_complex "\
color=c=0xFE0553:s=868x197:r=30:d=8,format=rgb24,\
drawtext=fontfile=${F}:fontsize=60:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:text='${L1}':x=(w-text_w)/2+5:y=37+5,\
drawtext=fontfile=${F}:fontsize=60:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:text='${L2}':x=(w-text_w)/2+5:y=111+5,\
drawtext=fontfile=${F}:fontsize=60:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:text='${L1}':x=(w-text_w)/2:y=37,\
drawtext=fontfile=${F}:fontsize=60:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:text='${L2}':x=(w-text_w)/2:y=111,\
scale=out_color_matrix=bt709:out_range=tv,format=yuv420p[caixa];\
[0:v][caixa]overlay=x=106:y=862:eof_action=pass:enable='lt(n,234)'[v]" \
  -map "[v]" -map 0:a -c:a copy \
  -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -movflags +faststart "$OUT"
echo "ok -> $OUT"
