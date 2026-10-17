#!/bin/bash
# Monta a V2 "resultado primeiro". Rodar de qualquer lugar.
set -e
cd "$(dirname "$0")/.."
REF=../REFERENCIA-original.mp4
# 17/10: demo com "Copy her @" vem da V3 (igual ao original fora da legenda)
HER=../v3-quem-ele-curte/pecas/v3-quem-ele-curte.mp4
python3 work/placas.py
# A = reveal f733-806 (74 fr, sem TRY IT FREE) | B = demo f155-732 (f154 ainda tem faixa do cafe na borda) | C = reveal+CTA f733-1094
N=$((74 + 578 + 362)); DUR=$(python3 -c "print($N/30)"); FO=$(python3 -c "print($N/30-0.3)")
ffmpeg -hide_banner -loglevel error -y -i "$REF" -loop 1 -framerate 30 -i work/placa1.png -loop 1 -framerate 30 -i work/placa2.png -i "$HER" -filter_complex "
[0:v]split=2[a][c];
[a]trim=start_frame=733:end_frame=807,setpts=PTS-STARTPTS[va];
[3:v]trim=start_frame=155:end_frame=733,setpts=PTS-STARTPTS[vb];
[c]trim=start_frame=733:end_frame=1095,setpts=PTS-STARTPTS[vc];
[va][vb][vc]concat=n=3:v=1:a=0,settb=1/30,setpts=N[v0];
[v0][1:v]overlay=0:0:shortest=1:enable='between(n,0,49)'[v1];
[v1][2:v]overlay=0:0:shortest=1:enable='between(n,50,93)',format=yuv420p,trim=end_frame=$N[v];
[0:a]atrim=0:$DUR,asetpts=PTS-STARTPTS,afade=t=out:st=$FO:d=0.3[aout]" \
 -map "[v]" -map "[aout]" -r 30 -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart pecas/v2-resultado-primeiro.mp4
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=width,height,r_frame_rate,nb_read_frames -show_entries format=duration -of default=nw=1 pecas/v2-resultado-primeiro.mp4
