#!/bin/bash
# conferir-audio.sh <clipe.mp4> — o áudio do clipe bate com audio/locucao-ex-v2.mp3? Duração, correlação de envelope e texto do whisper.
# Se não bater: refazer o karaokê → python3 karaoke-l10.py <json-do-clipe> molde/karaoke.tsv --blocos molde/karaoke-blocos.txt
set -euo pipefail; cd "$(dirname "$0")/../../.."; L=centerpag-detect/criativos/zap-ex-presente-hook-2026-09-05; CL="$1"
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate,duration -of compact "$CL"
ffmpeg -nostdin -v error -y -i "$CL" -ac 1 -ar 16000 "$L/molde/clipe-16k.wav"
python3 - "$L/molde/clipe-16k.wav" "$L/molde/locucao-ex-v2-16k.wav" <<'PY'
import sys, wave, numpy as np
def rd(p):
    w=wave.open(p); a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float); return a
a,b=rd(sys.argv[1]),rd(sys.argv[2]); n=min(len(a),len(b))//160*160; print(f'duracao clipe {len(a)/16000:.2f} s · v2 {len(b)/16000:.2f} s')
env=lambda x:np.abs(x[:n]).reshape(-1,160)[:, :].mean(1)   # envelope a 100 Hz
ea,eb=env(a),env(b); ea-=ea.mean(); eb-=eb.mean(); c=np.correlate(ea,eb,'full'); k=c.argmax()-len(eb)+1
print(f'correlacao de envelope {c.max()/np.sqrt((ea**2).sum()*(eb**2).sum()):.3f} · deslocamento {k/100:+.2f} s  (≥0,9 e |desloc| ≤ 0,05 s = mesma locucao)')
PY
uvx --from mlx-whisper mlx_whisper "$L/molde/clipe-16k.wav" --model mlx-community/whisper-small.en-mlx --word-timestamps True --output-dir "$L/molde" --output-format json --language en >/dev/null 2>&1
python3 - "$L/molde/clipe-16k.json" "$L/molde/locucao-ex-v2-16k.json" <<'PY'
import json,sys
w=lambda p:[x['word'].strip().lower() for s in json.load(open(p))['segments'] for x in s['words']]
a,b=w(sys.argv[1]),w(sys.argv[2]); print(f'palavras clipe {len(a)} · v2 {len(b)} · iguais: {a==b}')
if a!=b:
    import difflib; print('\n'.join(difflib.unified_diff(b,a,'v2','clipe',lineterm='',n=0)))
PY
