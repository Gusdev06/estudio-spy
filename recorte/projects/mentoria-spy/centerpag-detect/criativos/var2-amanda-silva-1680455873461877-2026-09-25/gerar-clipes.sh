#!/bin/bash
# 3 clipes Pruna com o áudio ORIGINAL em WAV. c1 = 0-24,467 s (n0-733, até o corte pro split) · c2 = 24,467-41,45 s · c3 = 40,9 s-fim.
# c2 e c3 se SOBREPÕEM 0,55 s dentro da pausa de fala 40,75-41,65 s: o montar.py escolhe ali o frame de menor salto de pose (melhoria sobre a var1,
# que emendava seco em 43,0 s). Durações abaixo do segundo inteiro (25+17+20 s = mesmo custo da var1). Prompt só em positivo.
# Uso (de projects/mentoria-spy/): SEED=7 bash centerpag-detect/criativos/var2-amanda-silva-1680455873461877-2026-09-25/gerar-clipes.sh c1 [c2 c3]
set -e; cd "$(dirname "$0")/../../.."; D=centerpag-detect/criativos/var2-amanda-silva-1680455873461877-2026-09-25; SEED=${SEED:-7}; TAG=${TAG:-}
for b in "$@"; do
  python3 - "$b" "$SEED" "$TAG" "$D" <<'PY'
import json,sys
b,seed,tag,D=sys.argv[1],int(sys.argv[2]),sys.argv[3],sys.argv[4]
pessoa=open(f'{D}/base/pessoa.txt').read().strip(); cena=open(f'{D}/base/cena.txt').read().strip()
vp=(f"One continuous horizontal full-frame shot from the first frame to the last, filmed on a phone front camera on a tripod. The woman — {pessoa} — sits alone in {cena}, "
    "and stays exactly the same person the whole time: same face, same hair, same clothes, same position in the frame, same distance from the camera. "
    "The camera stays still and the room around her stays still and calm. She talks straight into the camera, sincere and a little worried, like confiding in a friend, "
    "with small natural head movements and small nods; her shoulders stay relaxed, her face stays centered in the frame, and between sentences her head settles back "
    "into the same upright, centered, front-facing resting pose she has in the first frame.")
json.dump({'image':open(f'{D}/base/url-base.txt').read().strip(),'audio':open(f'{D}/audio/url-{b}.txt').read().strip(),'resolution':'720p','video_prompt':vp,'seed':seed},open(f'{D}/clipes/{b}{tag}.req.json','w'))
PY
  (wavespeed run pruna-ai/p-video/avatar --input-file $D/clipes/$b$TAG.req.json --json --download $D/clipes/$b$TAG.mp4 > $D/clipes/$b$TAG.out.json 2> $D/clipes/$b$TAG.log && echo "ok $b$TAG" || { echo "FALHOU $b$TAG"; tail -c 200 $D/clipes/$b$TAG.log; }) &
done; wait
