#!/bin/bash
# Imagem-base de cada avatar (gpt-image-2 t2i, 9:16, medium, 1k), mesmo cenário de home office da 77. Uso (de qualquer lugar): bash gerar-base.sh v164 v165 …
cd "$(dirname "$0")/../../.."; N=centerpag-detect/criativos/secret-top5-avatar-copy-2026-10-07
for v in "$@"; do (
  python3 - "$v" <<'PY'
import json,sys
v=sys.argv[1]; N='centerpag-detect/criativos/secret-top5-avatar-copy-2026-10-07'
d=open(f'{N}/elencos/{v}.txt').read().strip(); mae=json.load(open(f'{N}/copys.json'))[v]['mae']
expr=("a friendly, slightly conspiratorial half-smile, as if about to explain a secret" if mae=='77' else "a serious, direct expression, as if telling a hard truth")
p=(f"Vertical 9:16 video still, front phone camera at eye level, bright home office. {d}. He looks straight into the lens with {expr}, mouth closed. "
   "Framing: chest up, hands out of frame, subject centered, eyes at about 35% from the top. Behind him: a white upholstered chair, a light neutral wall, a bookshelf with a small plant, "
   "soft natural window daylight, slightly overexposed background like a real webcam-style recording. Realistic skin texture, mild phone-camera softness, no retouching, ordinary person, not a model. Only one person in frame.")
json.dump({'prompt':p,'aspect_ratio':'9:16','quality':'medium','resolution':'1k'},open(f'{N}/base/{v}.req.json','w'))
PY
  wavespeed run openai/gpt-image-2/text-to-image --input-file $N/base/$v.req.json --json --download $N/base/$v.png > $N/base/$v.out.json 2> $N/base/$v.log && echo "ok $v" || { echo "FALHOU $v"; tail -c 200 $N/base/$v.log; }
) & done; wait
