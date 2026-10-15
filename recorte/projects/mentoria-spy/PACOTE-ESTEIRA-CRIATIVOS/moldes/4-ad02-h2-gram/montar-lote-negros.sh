#!/bin/bash
# Monta as 5 variações com avatares negros, UMA POR VEZ (a montagem lê 898 PNGs de karaokê; em série estourou a memória em 13/09),
# e gera a folha de varredura de cada clipe antes. Uso (de projects/mentoria-spy/): bash montar-lote-negros.sh [n1 n2 …]
set -e; cd "$(dirname "$0")/../../.."; N=gram-detect/criativos/ad02-h2-reconstrucao-2026-09-17
IDS=${@:-n1 n2 n3 n4 n5}
for i in $IDS; do
  ffmpeg -hide_banner -v error -y -i $N/clipes-negros/$i.mp4 -vf "select='not(mod(n,45))',scale=95:-1,tile=16x1" -vsync 0 -frames:v 1 $N/conferencia/varredura-$i.jpg
  python3 $N/montar-reconstrucao.py $N/clipes-negros/$i.mp4 $N/AD02-H2-reconstruido-$i.mp4
  ffprobe -v error -show_entries stream=nb_frames,duration -of csv=p=0 $N/AD02-H2-reconstruido-$i.mp4 | head -1
done
