#!/bin/bash
# Roteiro E — layout L1, medidas de spec-de-edicao-layouts-spy
#   HOOK1/HOOK2 = faixa amarela fixa no topo (sem apostrofo: quebra o drawtext)
set -e; cd "$(dirname "$0")"
FK="/System/Library/Fonts/Supplemental/Arial Black.ttf"
HOOK1="${HOOK1:-WITHOUT EVER TOUCHING}"
HOOK2="${HOOK2:-HIS PHONE}"
HY1=48; HY2=140          # 2,5% e 7,3% de 1920  -> faixa ocupa 2-13%
PY=1382                  # 72% de 1920 = topo do painel do funil
HOOK="drawtext=fontfile='$FK':text='${HOOK1}':fontcolor=0xF2E205:fontsize=74:borderw=9:bordercolor=black:x=(w-tw)/2:y=${HY1},\
drawtext=fontfile='$FK':text='${HOOK2}':fontcolor=0xF2E205:fontsize=74:borderw=9:bordercolor=black:x=(w-tw)/2:y=${HY2}"
mkdir -p build; rm -f build/lista.txt
for c in e1 e2 e3; do
  ffmpeg -v error -i clipes/$c.mp4 -vf "scale=1080:1920,setsar=1,fps=30,${HOOK}" \
    -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 build/$c.mp4 -y
  echo "file '$c.mp4'" >> build/lista.txt
done
ffmpeg -v error -f concat -safe 0 -i build/lista.txt -c copy build/head.mp4 -y
ffmpeg -v error -i build/head.mp4 -i painel-funil.mp4 \
  -filter_complex "[0:v][1:v]overlay=0:${PY}:shortest=1[v]" \
  -map "[v]" -map 0:a -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 -r 30 roteiro-e-v1-33s.mp4 -y
echo "ok: roteiro-e-v1-33s.mp4"
