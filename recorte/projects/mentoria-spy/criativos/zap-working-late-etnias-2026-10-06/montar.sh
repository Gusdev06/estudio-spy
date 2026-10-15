#!/bin/bash
# Cola o talking head novo (clipes/<v>.mp4, Pruna 1:1) na caixa da cabeça do original: x0 y119 336x325.
# Resto (faixas, CCTV, tela do app, karaokê) e áudio intactos (-c:a copy). Uso: bash montar.sh v1-branco v2-latino ...
cd "$(dirname "$0")"
for v in "$@"; do
  ffmpeg -hide_banner -loglevel error -y -i REFERENCIA-original.mp4 -i clipes/$v.mp4 -filter_complex \
   "[1:v]fps=30,scale=336:325:flags=lanczos,setsar=1,trim=duration=30.419,setpts=PTS-STARTPTS[h];[0:v][h]overlay=0:119:eof_action=repeat[v]" \
   -map "[v]" -map 0:a -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a copy pecas/zap-working-late-$v.mp4 && echo "ok $v"
done
