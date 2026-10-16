#!/bin/bash
# Abertura (Bia, 0–5,367 s) + demo original (5,367–16,133 s) + fechamento (Bia, 16,133–18,834 s); áudio original inteiro.
# O Seedance 2.5 manteve as frases de baixo da abertura (só apagou o título): ali entra só o título redesenhado; no fechamento entra a frase.
cd "$(dirname "$0")"; O=original/DdFgYKABCCN.mp4; V="scale=1080:1920:flags=lanczos,fps=30,setsar=1,format=yuv420p"
ffmpeg -hide_banner -loglevel error -y \
 -i clipes/abertura-bia.mp4 -i $O -i clipes/fechamento-bia.mp4 \
 -i legendas/titulo.png -i legendas/ab-frase1.png -i legendas/ab-frase2.png -i legendas/fe-frase.png \
 -filter_complex "\
[0:v]trim=0:5.3667,setpts=PTS-STARTPTS,$V[a0];\
[a0][3]overlay[ab];\
[1:v]trim=5.3667:16.1333,setpts=PTS-STARTPTS,$V[demo];\
[2:v]trim=0:2.7007,setpts=PTS-STARTPTS,$V[f0];[f0][6]overlay[fe];\
[ab][demo][fe]concat=n=3:v=1:a=0[v]" \
 -map "[v]" -map 1:a -c:v libx264 -crf 17 -preset slow -profile:v high -c:a aac -b:a 128k -ar 44100 -shortest -movflags +faststart final/fixado-bia.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 final/fixado-bia.mp4
