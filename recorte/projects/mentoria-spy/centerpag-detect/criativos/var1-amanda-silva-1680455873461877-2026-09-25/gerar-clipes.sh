#!/bin/bash
# 3 clipes Pruna com o áudio ORIGINAL (c1 = n0-733 · c2 = n734-1289 · c3 = n1290-fim; c1|c2 emenda no corte pro split, c2|c3 na pausa de 43,0 s).
# Prompt só em positivo. Uso (de projects/mentoria-spy/): SEED=7 bash centerpag-detect/criativos/var1-amanda-silva-1680455873461877-2026-09-25/gerar-clipes.sh c1 [c2 c3]
set -e; cd "$(dirname "$0")/../../.."; D=centerpag-detect/criativos/var1-amanda-silva-1680455873461877-2026-09-25; SEED=${SEED:-7}; TAG=${TAG:-}
for b in "$@"; do
  python3 - "$b" "$SEED" "$TAG" <<'PY'
import json,sys
b,seed,tag=sys.argv[1],int(sys.argv[2]),sys.argv[3]; D='centerpag-detect/criativos/var1-amanda-silva-1680455873461877-2026-09-25'
pessoa=open(f'{D}/base/pessoa.txt').read().strip(); cena=open(f'{D}/base/cena.txt').read().strip()
vp=(f"One continuous horizontal full-frame shot from the first frame to the last, filmed on a phone front camera on a tripod. The woman — {pessoa} — sits alone in {cena}, "
    "and stays exactly the same person the whole time: same face, same hair, same sweater, same position in the frame, same distance from the camera. "
    "The camera stays still and the room around her stays still and calm. She talks straight into the camera, sincere and a little worried, like confiding in a friend, "
    "with small natural head movements and small nods; her shoulders stay relaxed and her face stays centered in the frame.")
json.dump({'image':open(f'{D}/base/url-base.txt').read().strip(),'audio':open(f'{D}/audio/url-{b}.txt').read().strip(),'resolution':'720p','video_prompt':vp,'seed':seed},open(f'{D}/clipes/{b}{tag}.req.json','w'))
PY
  (wavespeed run pruna-ai/p-video/avatar --input-file $D/clipes/$b$TAG.req.json --json --download $D/clipes/$b$TAG.mp4 > $D/clipes/$b$TAG.out.json 2> $D/clipes/$b$TAG.log && echo "ok $b$TAG" || { echo "FALHOU $b$TAG"; tail -c 200 $D/clipes/$b$TAG.log; }) &
done; wait
