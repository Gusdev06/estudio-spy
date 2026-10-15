#!/bin/bash
# Lipsync avatar novo. Homens usam audio/homem-ritmo.mp3 (voz+copy originais da 121); mulheres usam audio/mulher-ritmo.mp3 (voz Calm_Woman, copy flipada pro HE).
# Uso (de projects/mentoria-spy/): bash <este>.sh m1 m2 w1 w2 w3
set -e; cd "$(dirname "$0")/../../.."; N=centerpag-detect/criativos/secret-hook-avatares-2026-09-28
for v in "$@"; do (
  sobe(){ for t in 1 2 3 4 5; do U=$(wavespeed upload "$1" --json 2>/dev/null | python3 -c "import json,sys
try: print(json.load(sys.stdin)['url'])
except Exception: pass"); [ -n "$U" ] && { echo "$U"; return 0; }; sleep 5; done; return 1; }
  G=$(cut -d'|' -f1 $N/elencos/$v.txt)
  case $G in man) AUD_F=$N/audio/homem-ritmo.mp3;; *) AUD_F=$N/audio/mulher-ritmo.mp3;; esac
  IMG=$(sobe $N/base/$v.png) || { echo "FALHOU upload imagem $v"; exit 0; }
  AUD=$(sobe $AUD_F) || { echo "FALHOU upload audio $v"; exit 0; }
  python3 - "$v" "$IMG" "$AUD" "$G" <<'PY'
import json,sys
v,img,aud,g=sys.argv[1:5]; N='centerpag-detect/criativos/secret-hook-avatares-2026-09-28'
desc=open(f'{N}/elencos/{v}.txt').read().strip().split('|')[1]
who='man' if g=='man' else 'woman'; pron='him' if g=='man' else 'her'; sub='He' if g=='man' else 'She'
p=(f"The {who} in the image — {desc} — stays EXACTLY the same person from the first frame to the last: same face, same hair, same clothes, same framing and distance from the camera. "
   "Selfie-style webcam recording, camera locked off at eye level; the camera never moves and the room behind stays the same. "
   f"Both of {pron} arms hang relaxed, completely out of frame, for the whole clip, and nothing is held in front of {pron} or shown to the camera. "
   f"SOLO SHOT, exactly one person; nothing ever enters the frame from the edges. {sub} talks straight into the lens, serious and direct, like telling a hard truth, with small natural head movements only.")
json.dump({'image':img,'audio':aud,'resolution':'720p','video_prompt':p,'seed':21},open(f'{N}/clipes/{v}.req.json','w'))
PY
  wavespeed run pruna-ai/p-video/avatar --input-file $N/clipes/$v.req.json --json --download $N/clipes/$v.mp4 > $N/clipes/$v.out.json 2> $N/clipes/$v.log && echo "ok $v" || { echo "FALHOU $v"; tail -c 150 $N/clipes/$v.log; }
) & done; wait
