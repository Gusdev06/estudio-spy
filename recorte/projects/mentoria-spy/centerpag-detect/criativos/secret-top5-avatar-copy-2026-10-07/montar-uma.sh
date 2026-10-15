#!/bin/bash
# Monta UMA peça (karaokê estoura a RAM em série — memória montagem-karaoke-estoura-memoria). Uso: bash montar-uma.sh v164
cd "$(dirname "$0")/../../.."; N=centerpag-detect/criativos/secret-top5-avatar-copy-2026-10-07; v=$1; n=${v#v}
S=$(python3 -c "import json;print(json.load(open('$N/copys.json'))['$v']['slug'])")
python3 $N/montar.py $N/clipes/$v.mp4 $N/pecas/$n-ZAP-secret-$S.mp4 --audio $N/audio/$v-ritmo.mp3 --selo $N/molde/selo-$v.png
