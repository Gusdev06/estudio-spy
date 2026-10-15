#!/bin/bash
# TTS das 9 falas de uma copy (MiniMax speech-2.6-hd, as mesmas vozes da 106/108: A Calm_Woman, B Wise_Woman).
# Uso (de projects/mentoria-spy/): bash .../gerar-tts.sh 170
D=centerpag-detect/criativos/podcast-wpp-cp108-avatar-copy-2026-10-07; k=$1; mkdir -p $D/audio/$k
while IFS=$'\t' read -r i p txt; do
  v=$([ "$p" = A ] && echo Calm_Woman || echo Wise_Woman)
  (wavespeed run minimax/speech-2.6-hd -i "text=$txt" -i "voice_id=$v" -i language_boost=English --json --download "$D/audio/$k/l$i.mp3" > "$D/audio/$k/l$i.json" 2> "$D/audio/$k/l$i.log" && echo "ok $k l$i" || echo "FALHOU $k l$i") &
done < $D/roteiro-$k.tsv; wait
