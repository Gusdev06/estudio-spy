#!/bin/bash
# gerar-heads.sh — fase C (PAGA): 5 × pruna-ai/p-video/avatar sobre a VO inteira. NÃO roda sem CONFIRMADO=1.
#   CONFIRMADO=1 bash gerar-heads.sh [720p|1080p] [av1 av2 …]
# Sem CONFIRMADO=1: imprime a estimativa e sai com código 1.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; cd "$HERE"
RES="${1:-720p}"; shift || true
AVS=("$@"); [ ${#AVS[@]} -gt 0 ] || AVS=(av1 av2 av3 av4 av5)
AUDIO_URL="$(cat audio/upload-31927.txt)"      # VO original, 31,927 s, sem pad (ceil = 32 s cobrados); o Pruna já devolve ~0,6 s de vídeo além do áudio
PROMPT="$(cat ../../roteiros/2026-09-11-gram01-var-avatar-5-rostos/video-prompt.txt)"
case "$RES" in 720p) UNIT=0.025;; 1080p) UNIT=0.045;; *) echo "resolução inválida" >&2; exit 2;; esac
SECS=32; N=${#AVS[@]}
TOTAL=$(python3 -c "print(f'{$N*$SECS*$UNIT:.3f}')")
echo "ESTIMATIVA fase C: $N avatares × ceil(31,927 s)=$SECS s × US\$ $UNIT/s ($RES) = US\$ $TOTAL   (price real 11/09: 720p 0,80 · 1080p 1,44 por avatar)"
echo "áudio: $AUDIO_URL"
echo "video_prompt: $PROMPT"
if [ "${CONFIRMADO:-0}" != "1" ]; then echo "NÃO EXECUTADO — exporte CONFIRMADO=1 depois do SIM do Gusta." >&2; exit 1; fi
mkdir -p clipes
wavespeed billings --limit 5 > clipes/billings-antes-$(date +%H%M%S).txt 2>&1 || true
for AV in "${AVS[@]}"; do
  n=${AV#av}; IMG=base/avatar-$AV.png; [ -f "$IMG" ] || { echo "falta $IMG" >&2; exit 3; }
  IMGURL=$(wavespeed upload "$IMG" --json | python3 -c 'import json,sys;d=json.load(sys.stdin);print(d["url"] if isinstance(d,dict) else d[0]["url"])')
  echo "$AV $IMGURL" >> clipes/upload.txt
  echo "== $AV → clipes/talking-head-$AV.mp4"
  wavespeed run pruna-ai/p-video/avatar -i image="$IMGURL" -i audio="$AUDIO_URL" -i resolution="$RES" -i video_prompt="$PROMPT" \
    --download "clipes/talking-head-$AV.mp4" --json > "clipes/$AV.out.json" 2> "clipes/$AV.log" || { echo "falhou $AV — ver clipes/$AV.log" >&2; exit 4; }
  ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,nb_frames,duration -of compact "clipes/talking-head-$AV.mp4"
  wavespeed billings --limit 3 2>&1 | grep -A1 pruna | head -2 || true
done
wavespeed billings --limit 10 > clipes/billings-depois-$(date +%H%M%S).txt 2>&1 || true
echo "pronto: agora bash remontar-lote.sh <n> <slug> por avatar"
