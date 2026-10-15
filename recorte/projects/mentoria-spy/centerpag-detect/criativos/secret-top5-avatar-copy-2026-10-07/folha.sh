#!/bin/bash
# Folha de contato: 12 frames distribuídos no vídeo inteiro (pula o frame 0). Uso: bash folha.sh <video> <saida.jpg>
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$1"); T=$(mktemp -d)
for i in $(seq 0 11); do t=$(python3 -c "print(0.2+($D-0.4)*$i/11)"); ffmpeg -hide_banner -v error -y -ss $t -i "$1" -frames:v 1 -vf "scale=270:-2,drawtext=fontfile=/System/Library/Fonts/Supplemental/Arial.ttf:text='$(printf %.1f $t)s':x=8:y=8:fontsize=22:fontcolor=yellow:box=1:boxcolor=black" $T/$i.png; done
ffmpeg -hide_banner -v error -y -i $T/%d.png -vf tile=6x2 -frames:v 1 "$2"; rm -r $T
