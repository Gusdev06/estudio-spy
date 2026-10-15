#!/bin/bash
# GD-AD01 — variação C: rosto/cenário (PERSONAGEM 3, cozinha) + correções por edição. Custo zero.
# Roda de qualquer lugar:  bash gram-detect/criativos/gd-ad01-var-rosto-2026-09-03/montar.sh
set -e
cd "$(dirname "$0")/../../.."
IN="criativos-personagens/AD01 - PERSONAGEM 3.mp4"      # md5 cf4d71f70c2b892456851e649f6bd8f7 · 1080x1920 · 60 fps · 29,55 s
F=gram-detect/scripts/fonts/Poppins-Bold.ttf
OUT=gram-detect/criativos/gd-ad01-var-rosto-2026-09-03/GD-AD01-C-rosto-p3.mp4
L1='I found something I wasn’t'
L2='even looking for...'
# Correções (seção 14b do teardown), todas medidas no P3:
#  (1) caixa do campeão com o texto original, CENTRADO VERTICALMENTE na caixa (ajuste do Maestro 03/09): topos das linhas em
#      y 1025 e 1100 (passo 75), bloco de texto y ≈ 1026–1162 centrado em y 1094 = centro da caixa; centro x 540. A CAIXA É MAIOR:
#      x 40–1039, y 862–1326 (1000×465). Campeão: x 106–973, y 862–1058 (868×197). Motivo (correção do Maestro 03/09):
#      a legenda cursiva do P3 ("THERE'S A detail on… always GIVES away people") desce até y 1317 (frame 208, 3,47 s)
#      e o logo do Instagram vaza pra esquerda até x 47 (y 1246–1320, 0,6–3,85 s). Texto cortado pela borda parece defeito.
#      Fecho 10 px abaixo do branco (1327) e 7 px além do logo (40), simétrico em torno de x 540. Painel do app começa em ~1330.
#      Poppins Bold 60 px, #EEFC00, contorno 2 px + sombra 5 px #2C040A. Camada RGB → bt709 → overlay.
#  (2) caixa some no frame 399 = 6,650 s = início do flash/glitch que traz o card Gram Detect no P3 (no campeão é 7,8 s).
#  (3) voz −9 dB: P3 mede −16,5 dB mean / −13,5 LUFS; campeão −25,6 dB / −22,7 LUFS.
#  (4) fade escuro final cortado: começa no frame de 29,200 s; a peça fecha em corte seco no último frame limpo (29,183 s).
#  (5) frame 0 de olhos abertos: conferido, in point mantido.
ffmpeg -v error -y -i "$IN" -t 29.2 -filter_complex "\
color=c=0xFE0553:s=1000x465:r=60:d=7,format=rgb24,\
drawtext=fontfile=${F}:fontsize=60:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:text='${L1}':x=(w-text_w)/2+5:y=163+5,\
drawtext=fontfile=${F}:fontsize=60:fontcolor=0x2C040A:borderw=2:bordercolor=0x2C040A:text='${L2}':x=(w-text_w)/2+5:y=237+5,\
drawtext=fontfile=${F}:fontsize=60:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:text='${L1}':x=(w-text_w)/2:y=163,\
drawtext=fontfile=${F}:fontsize=60:fontcolor=0xEEFC00:borderw=2:bordercolor=0x2C040A:text='${L2}':x=(w-text_w)/2:y=237,\
scale=out_color_matrix=bt709:out_range=tv,format=yuv420p[caixa];\
[0:v][caixa]overlay=x=40:y=862:eof_action=pass:enable='lt(n,399)'[v];\
[0:a]volume=-9dB[a]" \
  -map "[v]" -map "[a]" \
  -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:a aac -b:a 192k -movflags +faststart "$OUT"
echo "ok -> $OUT"
