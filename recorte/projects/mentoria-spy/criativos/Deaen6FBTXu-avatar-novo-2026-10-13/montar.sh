#!/bin/zsh
# monta cada clipe: 1080x1920, legenda original por cima, áudio original
cd "$(dirname "$0")"; mkdir -p final
for c in clipes/*.mp4; do n=$(basename $c .mp4)
  ffmpeg -v error -y -i $c -i legenda.png -i audio-original.m4a \
    -filter_complex "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1[v];[v][1:v]overlay=0:0[o]" \
    -map "[o]" -map 2:a -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart final/$n.mp4 && echo "ok $n $(ffprobe -v error -show_entries format=duration -of csv=p=0 final/$n.mp4)"
done
