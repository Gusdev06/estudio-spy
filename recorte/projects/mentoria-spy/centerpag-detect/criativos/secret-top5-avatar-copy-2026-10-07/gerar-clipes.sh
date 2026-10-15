#!/bin/bash
# Lipsync de cada variação: avatar novo + copy nova (pose em positivo, identidade travada). Uso: bash gerar-clipes.sh v01 v02 …
cd "$(dirname "$0")/../../.."; N=centerpag-detect/criativos/secret-top5-avatar-copy-2026-10-07
for v in "$@"; do (
  sobe(){ for t in 1 2 3 4 5; do U=$(wavespeed upload "$1" --json 2>/dev/null | python3 -c "import json,sys
try: print(json.load(sys.stdin)['url'])
except Exception: pass"); [ -n "$U" ] && { echo "$U"; return 0; }; sleep 5; done; return 1; }   # a WaveSpeed falha upload por rede; 5 tentativas
  IMG=$(sobe $N/base/$v.png) || { echo "FALHOU upload imagem $v"; exit 0; }
  AUD=$(sobe $N/audio/$v-ritmo.mp3) || { echo "FALHOU upload audio $v"; exit 0; }
  python3 - "$v" "$IMG" "$AUD" <<'PY'
import json,sys
v,img,aud=sys.argv[1:4]; N='centerpag-detect/criativos/secret-top5-avatar-copy-2026-10-07'
d=open(f'{N}/elencos/{v}.txt').read().strip()
tom=('relaxed and confident, like explaining a useful trick to a friend' if json.load(open(f'{N}/copys.json'))[v]['mae']=='77' else 'serious and direct, like telling a hard truth')
p=(f"The man in the image — {d} — stays EXACTLY the same person from the first frame to the last: same face, same hair, same clothes, same framing and distance from the camera. "
   "Selfie-style webcam recording, camera locked off at eye level; the camera never moves and the room behind him stays the same. Both of his arms hang relaxed at his sides, completely out of frame, for the whole clip, and nothing is held in front of him or shown to the camera. "
   "SOLO SHOT, exactly one person; nothing ever enters the frame from the edges. He talks straight into the lens, " + tom + ", with small natural head movements only.")
json.dump({'image':img,'audio':aud,'resolution':'720p','video_prompt':p,'seed':21},open(f'{N}/clipes/{v}.req.json','w'))
PY
  wavespeed run pruna-ai/p-video/avatar --input-file $N/clipes/$v.req.json --json --download $N/clipes/$v.mp4 > $N/clipes/$v.out.json 2> $N/clipes/$v.log && echo "ok $v" || { echo "FALHOU $v"; tail -c 150 $N/clipes/$v.log; }
) & done; wait
