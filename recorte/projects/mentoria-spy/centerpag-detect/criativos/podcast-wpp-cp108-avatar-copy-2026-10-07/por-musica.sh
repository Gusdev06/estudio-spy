#!/bin/bash
# Põe trilha por baixo da peça, sem reencodar o vídeo. A trilha é normalizada para o MESMO nível da cama do original
# (mean −28,5 dB, medido no b-roll final do criativo), fade in 1 s e fade out 1,5 s antes do CTA (que tem trilha própria).
# Uso (de projects/mentoria-spy/): bash por-musica.sh <peça.mp4> <trilha> <saida.mp4> [CTA_INI] [ALVO_dB]
set -e; P="$1"; MUS="$2"; OUT="$3"; CTA=${4:-33.61}; ALVO=${5:--28.5}
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$P")
MEAN=$(ffmpeg -hide_banner -v info -t 60 -i "$MUS" -vn -af volumedetect -f null - 2>&1 | grep -o 'mean_volume: [-0-9.]*' | cut -d' ' -f2)
G=$(python3 -c "print(round($ALVO-($MEAN),2))")
echo "trilha $(basename "$MUS"): mean ${MEAN} dB → ganho ${G} dB"
ffmpeg -hide_banner -v error -y -i "$P" -stream_loop -1 -i "$MUS" -filter_complex \
 "[1:a]atrim=0:${CTA},volume=${G}dB,afade=t=in:st=0:d=1,afade=t=out:st=$(python3 -c "print(max(0,$CTA-1.5))"):d=1.5,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,apad=whole_dur=${DUR}[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -movflags +faststart "$OUT"
echo "ok -> $OUT"
