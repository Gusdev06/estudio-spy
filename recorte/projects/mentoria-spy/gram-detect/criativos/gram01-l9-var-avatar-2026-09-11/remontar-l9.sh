#!/bin/bash
# remontar-l9.sh — molde L9 reconstruído (o lote-controle gram01-l9-faixa-2026-09-01 não guardou o script; build/ vazio).
#   bash remontar-l9.sh <head-panel.mp4> <tail-fullframe.mp4> <saida.mp4> [faixa.png]
# Entradas:  head  1170×1212, ≥940 frames (frames além de 940 são descartados; se tiver menos, o último é clonado)
#            cauda 1170×2532, ≥35 frames (idem, 35)
#            faixa 1170×286 png  (padrão: faixas/en-01.png do controle)
#            funil 462×1034 · b-roll 708×1034 · VO m4a — SEMPRE os do controle (só o rosto muda)
# Pilha (0–939): head y 0–1212 · painel y 1498–2532 (funil x 0–461 | b-roll x 462–1170) · faixa y 1212–1498 desenhada POR ÚLTIMO.
# Frame 940 em diante: cauda em quadro cheio. Saída 1170×2532 · 975 fr · 30 fps · x264 crf 19 preset medium yuv420p (= controle,
# lido do SEI x264 da peça) · áudio = vo-master-en.m4a copiado bit a bit (aac 44,1 kHz estéreo; o controle re-encodou o mesmo master).
# Prova: bash remontar-l9.sh C/lipsync/head-lipsync-raw.mp4 C/lipsync/tail-lipsync-raw.mp4 conferencia/standin-controle.mp4
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
C="${CONTROLE:-$HERE/../gram01-l9-faixa-2026-09-01}"
HEAD="${1:?uso: remontar-l9.sh head-panel.mp4 tail-fullframe.mp4 saida.mp4 [faixa.png]}"
TAIL="${2:?cauda 1170x2532}"
OUT="${3:?saida.mp4}"
FAIXA="${4:-$C/faixas/en-01.png}"
FUNIL="${FUNIL:-$C/funil/funil-painel.mp4}"
BROLL="${BROLL:-$C/broll/broll-painel.mp4}"
VO="${VO:-$C/vo/vo-master-en.m4a}"
CRF="${CRF:-19}"

for f in "$HEAD" "$TAIL" "$FAIXA" "$FUNIL" "$BROLL" "$VO"; do [ -f "$f" ] || { echo "falta: $f" >&2; exit 2; }; done
dim() { ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$1"; }
[ "$(dim "$HEAD")" = "1170,1212" ] || { echo "head não é 1170x1212: $(dim "$HEAD")" >&2; exit 3; }
[ "$(dim "$TAIL")" = "1170,2532" ] || { echo "cauda não é 1170x2532: $(dim "$TAIL")" >&2; exit 3; }
[ "$(dim "$FAIXA")" = "1170,286" ] || { echo "faixa não é 1170x286: $(dim "$FAIXA")" >&2; exit 3; }

mkdir -p "$(dirname "$OUT")"
ffmpeg -v error -y \
  -i "$HEAD" -i "$TAIL" -loop 1 -framerate 30 -i "$FAIXA" -i "$FUNIL" -i "$BROLL" -i "$VO" \
  -filter_complex "\
[0:v]fps=30,format=yuv420p,tpad=stop_mode=clone:stop_duration=40,trim=end_frame=940,setpts=PTS-STARTPTS[head];\
[1:v]fps=30,format=yuv420p,tpad=stop_mode=clone:stop_duration=5,trim=end_frame=35,setpts=PTS-STARTPTS[tail];\
[2:v]format=yuv420p,trim=end_frame=940,setpts=PTS-STARTPTS[faixa];\
[3:v]fps=30,format=yuv420p,trim=end_frame=940,setpts=PTS-STARTPTS[funil];\
[4:v]fps=30,format=yuv420p,trim=end_frame=940,setpts=PTS-STARTPTS[broll];\
[funil][broll]hstack=inputs=2[painel];\
color=c=black:s=1170x2532:r=30:d=31.333334,format=yuv420p,trim=end_frame=940,setpts=PTS-STARTPTS[canvas];\
[canvas][head]overlay=x=0:y=0:eof_action=pass[v1];\
[v1][painel]overlay=x=0:y=1498:eof_action=pass[v2];\
[v2][faixa]overlay=x=0:y=1212:eof_action=pass[split];\
[split][tail]concat=n=2:v=1:a=0[v]" \
  -map "[v]" -map 5:a -c:a copy \
  -c:v libx264 -preset medium -crf "$CRF" -pix_fmt yuv420p -r 30 \
  -movflags +faststart "$OUT"
n=$(ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of csv=p=0 "$OUT")
echo "ok -> $OUT ($n frames)"
[ "$n" = "975" ] || { echo "AVISO: esperado 975 frames" >&2; exit 4; }
