#!/bin/bash
# Whisper local (mlx, small.en) com tempo por palavra em cada áudio TTS → audio/<nome>.json. Custo zero.
set -e; cd "$(dirname "$0")/../../.."
P=gram-detect/criativos/podcast-hook-polemico-2026-09-05
for f in "$P"/audio/*.mp3 "$P"/audio/*.wav "$P"/audio/*.m4a; do case "$f" in *-16k.*) continue;; esac;
  [ -f "$f" ] || continue; b="${f%.*}"
  ffmpeg -v error -y -i "$f" -ac 1 -ar 16000 "$b-16k.wav"
  uvx --from mlx-whisper mlx_whisper "$b-16k.wav" --model mlx-community/whisper-small.en-mlx --word-timestamps True --output-dir "$P/audio" --output-format json --language en >/dev/null 2>&1
  mv "$b-16k.json" "$b.json"; rm -f "$b-16k.wav"; echo "ok $b.json"
done
python3 "$P/molde/karaoke-tempos.py"
