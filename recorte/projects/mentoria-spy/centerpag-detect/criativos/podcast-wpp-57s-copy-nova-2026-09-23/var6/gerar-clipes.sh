#!/bin/bash
# Gera os 6 clipes de fala de uma variação (mesmo áudio por bloco da peça 106, avatares novos).
# Uso (de projects/mentoria-spy/): bash var6/gerar-clipes.sh w1 [w2 …]
set -e; cd "$(dirname "$0")/../../../.."; N=centerpag-detect/criativos/podcast-wpp-57s-copy-nova-2026-09-23; V=$N/var6
for k in "$@"; do
  mkdir -p $V/$k/clipes
  for p in A B; do
    U=$(wavespeed upload $V/base/$k-$p.png --json 2>/dev/null | python3 -c "import json,sys;print(json.load(sys.stdin)['url'])"); echo "$U" > $V/$k/url-$p.txt
  done
  python3 - "$k" <<'PY'
import json,sys
k=sys.argv[1]; N='centerpag-detect/criativos/podcast-wpp-57s-copy-nova-2026-09-23'; V=f'{N}/var6'
info=json.load(open(f'{N}/molde/blocos.json'))
desc={p:open(f'{V}/base/{k}-{p}.txt').read().strip() for p in 'AB'}
url={p:open(f'{V}/{k}/url-{p}.txt').read().strip() for p in 'AB'}
for bid,d in info.items():
    p=d['papel']; base=json.load(open(f'{N}/clipes/{bid}.req.json'))
    r=dict(base); r['image']=url[p]; r['seed']=21
    r['video_prompt']=(f"The woman in the image — {desc[p]} — stays EXACTLY the same person from the first frame to the last: same face, same hair, same clothes, same seated position and distance from the camera. "
     "Podcast studio, locked-off camera on a tripod; the camera never moves and the background, sofa and microphone stay exactly the same. She is the ONLY person in the frame; her hands rest on her lap, out of the way, and nothing and nobody enters from any edge. "
     + ("She talks to someone off-camera, warm and knowing, with small natural head movements." if p=='A' else "She asks a question, curious and a bit skeptical, eyebrows slightly raised, looking at the person off-camera."))
    json.dump(r,open(f'{V}/{k}/clipes/{bid}.req.json','w'))
PY
  for b in b1 b3 b4 b5 b6 b8; do
    (wavespeed run pruna-ai/p-video/avatar --input-file $V/$k/clipes/$b.req.json --json --download $V/$k/clipes/$b.mp4 > $V/$k/clipes/$b.out.json 2> $V/$k/clipes/$b.log && echo "ok $k $b" || { echo "FALHOU $k $b"; tail -c 150 $V/$k/clipes/$b.log; }) &
  done; wait
done
