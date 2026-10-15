#!/bin/bash
# Tira N frames (vídeo e áudio juntos, sync preservado) de dentro de um respiro que passou de 0,5 s. Uso: bash cortar-respiro.sh <peça.mp4> <frame_ini> <n_frames>
# 167: respiro de 0,52 s em 8,42–8,94 s (fim de "over.", ruído de respiração a ~−35 dB que o corte de pausas não pegou) → tira 4 frames a partir do 258 (8,60 s).
P=$1; F0=$2; NF=$3; F1=$((F0+NF-1)); T0=$(python3 -c "print($F0/30)"); T1=$(python3 -c "print(($F1+1)/30)"); TMP=${P%.mp4}.tmp.mp4
ffmpeg -nostdin -v error -y -i "$P" -vf "select='not(between(n,$F0,$F1))',setpts=N/30/TB" -af "aselect='not(between(t,$T0,$T1))',asetpts=N/SR/TB" \
  -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -c:a aac -b:a 192k -movflags +faststart "$TMP" && mv "$TMP" "$P" && echo "ok $P sem frames $F0-$F1 ($T0-$T1 s)"
