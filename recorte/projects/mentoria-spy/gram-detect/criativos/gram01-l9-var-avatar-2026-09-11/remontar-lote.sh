#!/bin/bash
# remontar-lote.sh — dado um clipe do Pruna (704×1280 · 24 fps · ~32,5 s, ou um stand-in na mesma geometria),
# produz head panel + cauda no enquadramento do controle e monta a peça L9 com remontar-l9.sh (custo zero).
#   bash remontar-lote.sh <n> <slug> [clipe.mp4] [OY]
#   n=1..5 · slug do casting · clipe padrão clipes/talking-head-av<n>.mp4 · OY = topo do recorte do head no clipe (padrão 220)
# Mapeamento (medido no controle — ver README "Enquadramento"):
#   head : crop CW×CH em (CX,OY) → scale 1170×1212 (1,66–2,0×) — CW/CX/OY medidos por avatar (medir-recorte.py) pra olhos a 47 % e rosto ~62 % (Haar) como no controle
#   cauda: crop 592×1280 em (56,0) → scale 1170×2532 (1,977×) — escala pela altura, corta as laterais (decisão do maestro)
#   1080p: os mesmos recortes ×1,534 (1080/704); escalas 1,13–1,29× no head, 1,29× na cauda
#   fps 24 → 30 por duplicação (fps=30), frames 0–939 = head, 940–974 = cauda — MESMA linha do tempo, corte só reenquadra.
# Saída: pecas/gram01-l9-en-01-av<n>-<slug>.mp4 + poster + conferência (regiões, faixa, 975 fr, VO md5, silêncios = 9).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; cd "$HERE"
N="${1:?n (1..5)}"; SLUG="${2:?slug}"; CLIP="${3:-clipes/talking-head-av$N.mp4}"
# recorte do head medido por avatar (medir-recorte.py → clipes/recorte-avN.env); padrão = quadro inteiro, OY 220
CW=704; CH=730; CX=0; OY=220; ENV="${RECORTE:-clipes/recorte-av$N.env}"; [ -f "$ENV" ] && . "$ENV"
PREFIX="${PREFIX:-pecas/gram01-l9-en-01-av$N-$SLUG}"
[ -f "$CLIP" ] || { echo "falta clipe: $CLIP" >&2; exit 2; }
DIM=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$CLIP")
case "$DIM" in
  704,1280) F=1 ;;                       # Pruna 720p — recorte medido nesta geometria
  1080,1920) F=1.534 ;;                  # Pruna 1080p — mesmos recortes ×1080/704 (medir-recorte.py mede sempre em 704×1280)
  *) echo "clipe não é 704x1280 nem 1080x1920 ($DIM)" >&2; exit 3 ;;
esac
ev() { python3 -c "v=int(round($1*$F)); print(v - v%2)"; }
CW=$(ev $CW); CH=$(ev $CH); CX=$(ev $CX); OY=$(ev $OY)
read TW TX TH <<< "$(python3 -c "w,h=map(int,'$DIM'.split(',')); tw=int(round(h*1170/2532)); tw-=tw%2; print(tw,(w-tw)//2,h)")"   # cauda: altura inteira, largura 1170/2532 da altura, centrada (704×1280 → 592×1280 em x 56)
mkdir -p clipes/conformado "$(dirname "$PREFIX")" conferencia
HEAD=clipes/conformado/head-av$N.mp4; TAIL=clipes/conformado/tail-av$N.mp4
# um único stream a 30 fps, prolongado (clone) até cobrir 975 frames; head = frames 0–939, cauda = 940–974
ffmpeg -v error -y -i "$CLIP" -filter_complex "\
[0:v]fps=30,tpad=stop_mode=clone:stop_duration=3,trim=end_frame=975,setpts=PTS-STARTPTS,split=2[a][b];\
[a]trim=end_frame=940,setpts=PTS-STARTPTS,crop=$CW:$CH:$CX:$OY,scale=1170:1212:flags=lanczos,format=yuv420p[head];\
[b]trim=start_frame=940:end_frame=975,setpts=PTS-STARTPTS,crop=$TW:$TH:$TX:0,scale=1170:2532:flags=lanczos,format=yuv420p[tail]" \
  -map "[head]" -an -c:v libx264 -preset medium -crf 12 -pix_fmt yuv420p "$HEAD" \
  -map "[tail]" -an -c:v libx264 -preset medium -crf 12 -pix_fmt yuv420p "$TAIL"
bash remontar-l9.sh "$HEAD" "$TAIL" "$PREFIX.mp4"
ffmpeg -v error -y -i "$PREFIX.mp4" -vf "select='eq(n,300)'" -vsync 0 -frames:v 1 -q:v 3 "$PREFIX-poster.jpg"
# conferência
C=../gram01-l9-faixa-2026-09-01
echo "recorte: CW=$CW CH=$CH CX=$CX OY=$OY"; echo "== conferência $PREFIX.mp4"
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,nb_frames,sample_rate,channels -of compact "$PREFIX.mp4"
echo "VO md5 (stream copy): $(ffmpeg -v error -i "$PREFIX.mp4" -map 0:a -c copy -f md5 - | cut -d= -f2)  controle master: $(ffmpeg -v error -i $C/vo/vo-master-en.m4a -c copy -f md5 - | cut -d= -f2)"
echo "silêncios ≥0,4 s (−35 dB): $(ffmpeg -i "$PREFIX.mp4" -af silencedetect=n=-35dB:d=0.4 -f null - 2>&1 | grep -c silence_start)  (controle: 9)"
python3 conferir-regioes.py $C/pecas/gram01-l9-en-01-v2.mp4 "$PREFIX.mp4" --json "conferencia/regioes-av$N.txt.json" | tee "conferencia/regioes-av$N.txt" | tail -8
echo "ok -> $PREFIX.mp4"
