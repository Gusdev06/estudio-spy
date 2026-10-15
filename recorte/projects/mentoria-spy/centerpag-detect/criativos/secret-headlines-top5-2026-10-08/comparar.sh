#!/bin/bash
# Compara uma peça com a mãe: md5 do stream de vídeo e de áudio, e PSNR médio/mínimo do vídeo decodificado. Uso: bash comparar.sh a.mp4 b.mp4
a=$1; b=$2
for s in v a; do echo "$s md5: $(ffmpeg -nostdin -v error -i "$a" -map 0:$s -c copy -f md5 -) / $(ffmpeg -nostdin -v error -i "$b" -map 0:$s -c copy -f md5 -)"; done
ffmpeg -nostdin -hide_banner -i "$a" -i "$b" -lavfi "[0:v][1:v]psnr=stats_file=-" -f null - 2>/dev/null | awk '{for(i=1;i<=NF;i++) if($i~/^psnr_avg:/){split($i,x,":"); v=x[2]; if(v=="inf")v=99; s+=v; n++; if(min==""||v<min)min=v}} END{printf "psnr frames=%d media=%.2f min=%.2f\n",n,s/n,min}'
