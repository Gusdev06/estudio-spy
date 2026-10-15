#!/bin/bash
# uso: bash full/montar.sh <clipe-B2>   (ex: B2r1)
set -e
cd "$(dirname "$0")/.."
B2C="${1:-B2}"
N="scale=1080:1920:flags=lanczos,fps=30,setsar=1"
cut(){ ffmpeg -y -v error -i criativo.mp4 -vf "trim=start=$1:end=$2,setpts=PTS-STARTPTS,$N" -an -c:v libx264 -crf 20 "full/$3.mp4"; }
cut 0  20 o1
cut 31 38 o2
cut 49 57 o3
for c in A1 A2 B1 "$B2C"; do
  ffmpeg -y -v error -i "full/$c.mp4" -an -vf "$N" -c:v libx264 -crf 20 "full/n$c.mp4"
done
printf "file 'o1.mp4'\nfile 'nA1.mp4'\nfile 'nA2.mp4'\nfile 'o2.mp4'\nfile 'nB1.mp4'\nfile 'n%s.mp4'\nfile 'o3.mp4'\n" "$B2C" > full/lista.txt
ffmpeg -y -v error -f concat -safe 0 -i full/lista.txt -c:v copy full/mudo.mp4
ffmpeg -y -v error -i full/mudo.mp4 -i criativo.mp4 -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest full/criativo-avatar-loira.mp4
echo -n "duracao final: "; ffprobe -v error -show_entries format=duration -of csv=p=0 full/criativo-avatar-loira.mp4
