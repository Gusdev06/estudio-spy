#!/bin/bash
# Vídeo da Bia (Seedance 2.5, sem texto) + texto redesenhado + áudio original; mesma duração do original (5,067 s).
cd "$(dirname "$0")"
ffmpeg -hide_banner -loglevel error -y -i clipes/bia.mp4 -i original/original-h264.mp4 -i legendas/texto.png \
 -filter_complex "[0:v]trim=0:5.067,setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1,format=yuv420p[v0];[v0][2]overlay[v]" \
 -map "[v]" -map 1:a -c:v libx264 -crf 17 -preset slow -profile:v high -c:a aac -b:a 128k -ar 44100 -shortest -movflags +faststart final/bia-lily5-replica.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 final/bia-lily5-replica.mp4
