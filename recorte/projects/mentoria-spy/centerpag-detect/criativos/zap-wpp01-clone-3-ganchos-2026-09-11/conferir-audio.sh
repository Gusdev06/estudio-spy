#!/bin/bash
# conferir-audio.sh <clipe.mp4> [referencia.mp3|.wav] [--ini-clipe S] [--ini-ref S] [--sem-whisper]
# O áudio do clipe (talking head Pruna, já sem pausas ou não) bate com a locução de referência? Duração, correlação de envelope
# (100 Hz, ≥0,9 e |desloc| ≤ 0,05 s = mesma locução) e texto do whisper (mlx-whisper local, custo zero).
# Lote zap-wpp01 (3 ganchos): o CORPO (blocos 2–7) é o mesmo texto/TTS nos 3, mas cada head é uma geração do Pruna, então o md5
# não se aplica — compare por envelope a partir do início do bloco 2 de cada um:
#   bash conferir-audio.sh clipes/talking-head-H2-sem-pausas.mp4 clipes/talking-head-H1-sem-pausas.mp4 --ini-clipe <B2 de H2> --ini-ref <B2 de H1>
# Padrão da referência: audio/locucao-H1.mp3 (TTS concatenado h1+corpo).
set -euo pipefail; D="$(cd "$(dirname "$0")" && pwd)"; cd "$D/../../.."; L=centerpag-detect/criativos/zap-wpp01-clone-3-ganchos-2026-09-11
CL="$1"; REF="${2:-$L/audio/locucao-H1.mp3}"; shift; [[ $# -gt 0 && "$1" != --* ]] && shift
IC=0; IR=0; WH=1; while [[ $# -gt 0 ]]; do case "$1" in --ini-clipe) IC="$2"; shift 2;; --ini-ref) IR="$2"; shift 2;; --sem-whisper) WH=0; shift;; *) shift;; esac; done
[[ -e "$CL" ]] || CL="$D/$CL"; [[ -e "$REF" ]] || REF="$D/$REF"
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate,duration -of compact "$CL"
A16="$L/molde/conf-clipe-16k.wav"; B16="$L/molde/conf-ref-16k.wav"
ffmpeg -nostdin -v error -y -ss "$IC" -i "$CL" -vn -ac 1 -ar 16000 "$A16"
ffmpeg -nostdin -v error -y -ss "$IR" -i "$REF" -vn -ac 1 -ar 16000 "$B16"
python3 - "$A16" "$B16" <<'PY'
import sys, wave, numpy as np
def rd(p):
    w=wave.open(p); a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float); return a
a,b=rd(sys.argv[1]),rd(sys.argv[2]); n=min(len(a),len(b))//160*160; print(f'duracao clipe {len(a)/16000:.2f} s · referencia {len(b)/16000:.2f} s (a partir dos --ini)')
env=lambda x:np.abs(x[:n]).reshape(-1,160).mean(1)   # envelope a 100 Hz
ea,eb=env(a),env(b); ea-=ea.mean(); eb-=eb.mean(); c=np.correlate(ea,eb,'full'); k=c.argmax()-len(eb)+1
print(f'correlacao de envelope {c.max()/np.sqrt((ea**2).sum()*(eb**2).sum()):.3f} · deslocamento {k/100:+.2f} s  (≥0,9 e |desloc| ≤ 0,05 s = mesma locucao)')
PY
[[ "$WH" == 1 ]] || exit 0
for W in "$A16" "$B16"; do uvx --from mlx-whisper mlx_whisper "$W" --model mlx-community/whisper-small.en-mlx --word-timestamps True --output-dir "$L/molde" --output-format json --language en >/dev/null 2>&1; done
python3 - "$L/molde/conf-clipe-16k.json" "$L/molde/conf-ref-16k.json" <<'PY'
import json,sys
w=lambda p:[x['word'].strip().lower() for s in json.load(open(p))['segments'] for x in s['words']]
a,b=w(sys.argv[1]),w(sys.argv[2]); print(f'palavras clipe {len(a)} · referencia {len(b)} · iguais: {a==b}')
if a!=b:
    import difflib; print('\n'.join(difflib.unified_diff(b,a,'referencia','clipe',lineterm='',n=0)))
PY
