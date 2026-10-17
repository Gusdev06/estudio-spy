#!/bin/bash
# Vídeo da Bia (Seedance 2.5, sem texto) + texto da série + áudio original; mesma duração do original.
# uso: bash montar.sh <pasta> <nome-saida>
P="$1"; N="$2"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$P/original/original-h264.mp4")
ffmpeg -hide_banner -loglevel error -y -i "$P/clipes/bia.mp4" -i "$P/original/original-h264.mp4" -i "$P/legendas/texto.png" \
 -filter_complex "[0:v]setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1,format=yuv420p,tpad=stop_mode=clone:stop_duration=1[v0];[v0][2]overlay,trim=0:$DUR[v]" \
 -map "[v]" -map 1:a -c:v libx264 -crf 17 -preset slow -profile:v high -c:a aac -b:a 128k -ar 44100 -t "$DUR" -movflags +faststart "$P/final/$N.mp4"
echo "$N $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$P/final/$N.mp4") s (original $DUR s)"
