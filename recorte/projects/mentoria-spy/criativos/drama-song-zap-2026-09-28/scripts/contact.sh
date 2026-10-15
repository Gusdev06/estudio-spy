#!/bin/bash
# contact sheet de 8 frames (4x2) de um clipe: contact.sh clipes-v2/B05.mp4 contact-v2/B05.png
f=$1; o=$2; d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
fps=$(python3 -c "print(8/$d)")
ffmpeg -hide_banner -v error -y -i "$f" -vf "fps=$fps,scale=240:-1,tile=4x2" -frames:v 1 "$o"
