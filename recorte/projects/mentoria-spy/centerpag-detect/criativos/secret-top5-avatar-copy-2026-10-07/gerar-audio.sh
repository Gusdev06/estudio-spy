#!/bin/bash
# TTS MiniMax Casual_Guy 1,06× (mesma voz dos lotes 112–121) + corte de pausas ≥0,4 s → 0,25 s. Uso: bash gerar-audio.sh v164 v165 …
cd "$(dirname "$0")/../../.."; N=centerpag-detect/criativos/secret-top5-avatar-copy-2026-10-07
for v in "$@"; do (
  TXT=$(python3 -c "import json;print(json.load(open('$N/copys.json'))['$v']['txt'])")
  wavespeed run minimax/speech-2.6-hd -i "text=$TXT" -i voice_id=Casual_Guy -i speed=1.06 -i emotion=neutral -i language_boost=English -i english_normalization=true -i format=mp3 -i sample_rate=44100 -i bitrate=128000 -i channel=1 --json --download $N/audio/$v.mp3 > $N/audio/$v.json 2> $N/audio/$v.log || { echo "FALHOU $v"; tail -c 200 $N/audio/$v.log; exit 0; }
  python3 $N/cortar-pausas-audio.py $N/audio/$v.mp3 $N/audio/$v-ritmo.wav >/dev/null
  ffmpeg -hide_banner -v error -y -i $N/audio/$v-ritmo.wav -c:a libmp3lame -b:a 160k $N/audio/$v-ritmo.mp3
  echo "ok $v $(ffprobe -v error -show_entries format=duration -of csv=p=0 $N/audio/$v-ritmo.wav | cut -c1-5)s"
) & done; wait
