#!/bin/bash
# Monta 4a e 4b: mesma montagem da V2 "resultado primeiro" (sarah-smith 3var 17/10), so o texto da placa 1 muda.
set -e
cd "$(dirname "$0")/.."
BASE=/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/gram-detect/criativos/sarah-smith-1677505624160791-3var-2026-10-17
REF=$BASE/REFERENCIA-original.mp4
HER=$BASE/v3-quem-ele-curte/pecas/v3-quem-ele-curte.mp4
python3 work/placas.py
N=$((74 + 578 + 362)); DUR=$(python3 -c "print($N/30)"); FO=$(python3 -c "print($N/30-0.3)")
for P in 4a-without-touching:4a 4b-stopped-guessing:4b; do
 OUT=${P%%:*}; K=${P##*:}
 ffmpeg -hide_banner -loglevel error -y -i "$REF" -loop 1 -framerate 30 -i work/$K-placa1.png -loop 1 -framerate 30 -i work/placa2.png -i "$HER" -filter_complex "
[0:v]split=2[a][c];
[a]trim=start_frame=733:end_frame=807,setpts=PTS-STARTPTS[va];
[3:v]trim=start_frame=155:end_frame=733,setpts=PTS-STARTPTS[vb];
[c]trim=start_frame=733:end_frame=1095,setpts=PTS-STARTPTS[vc];
[va][vb][vc]concat=n=3:v=1:a=0,settb=1/30,setpts=N[v0];
[v0][1:v]overlay=0:0:shortest=1:enable='between(n,0,49)'[v1];
[v1][2:v]overlay=0:0:shortest=1:enable='between(n,50,93)',format=yuv420p,trim=end_frame=$N[v];
[0:a]atrim=0:$DUR,asetpts=PTS-STARTPTS,afade=t=out:st=$FO:d=0.3[aout]" \
 -map "[v]" -map "[aout]" -r 30 -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart pecas/$OUT.mp4
 echo "== $OUT"; ffprobe -v error -count_frames -show_entries stream=codec_name,pix_fmt,width,height,r_frame_rate,nb_read_frames -show_entries format=duration -of compact pecas/$OUT.mp4
done
