#!/bin/bash
# TTS das copys agressivas (voz masculina, o avatar é homem) + corte de pausas ≥0,4 s. Uso: bash gerar-audio.sh v01 v02 …
set -e; cd "$(dirname "$0")/../../.."; N=centerpag-detect/criativos/secret-hook-agressivo-2026-09-23
for v in "$@"; do (
  TXT=$(python3 -c "import json;print(json.load(open('$N/copys.json'))['$v']['txt'])")
  wavespeed run minimax/speech-2.6-hd -i "text=$TXT" -i voice_id=Casual_Guy -i speed=1.06 -i emotion=neutral -i language_boost=English -i english_normalization=true -i format=mp3 -i sample_rate=44100 -i bitrate=128000 -i channel=1 --json --download $N/audio/$v.mp3 > $N/audio/$v.json 2> $N/audio/$v.log
  python3 centerpag-detect/criativos/ad02-h2-zap-2026-09-17/cortar-pausas-audio.py $N/audio/$v.mp3 $N/audio/$v-ritmo.wav >/dev/null
  ffmpeg -hide_banner -v error -y -i $N/audio/$v-ritmo.wav -c:a libmp3lame -b:a 160k $N/audio/$v-ritmo.mp3
  echo "ok $v $(ffprobe -v error -show_entries format=duration -of csv=p=0 $N/audio/$v-ritmo.wav | cut -c1-5)s"
) & done; wait
