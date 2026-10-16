#!/bin/bash
# Vídeo da Bia (Seedance 2.5, sem texto) + texto redesenhado + áudio original; mesma duração do original (5,067 s = 152 frames a 30 fps).
# O áudio do original tem 5,038 s: apad completa com silêncio até o fim do vídeo.
cd "$(dirname "$0")"
# O Seedance deixou o texto do original no clipe: apagar por inpainting antes do overlay (gera clipes/bia-limpo.mp4).
[ -f clipes/bia-limpo.mp4 ] || python3 limpar-texto.py
ffmpeg -hide_banner -loglevel error -y -i clipes/bia-limpo.mp4 -i original/original-h264.mp4 -i legendas/texto.png \
 -filter_complex "[0:v]trim=0:5.0667,setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1,format=yuv420p[v0];[v0][2]overlay[v];[1:a]apad[a]" \
 -map "[v]" -map "[a]" -t 5.0667 -c:v libx264 -crf 17 -preset slow -profile:v high -c:a aac -b:a 128k -ar 44100 -movflags +faststart final/bia-lily7-replica.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 final/bia-lily7-replica.mp4
