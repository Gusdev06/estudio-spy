#!/bin/bash
# 2 clipes Pruna por variação (c1 = 0–7,83 s, c2 = 15,07–16,0 s) com o áudio ORIGINAL do trecho; prompt só em positivo (lição do podcast Gram, 24/09).
# Uso (de projects/mentoria-spy/): SEED=7 bash centerpag-detect/criativos/kendall-1987478995288058-avatar-cenario-2026-09-25/gerar-clipes.sh k1 [k2 …]
set -e; cd "$(dirname "$0")/../../.."; L=centerpag-detect/criativos/kendall-1987478995288058-avatar-cenario-2026-09-25
for k in "$@"; do
  mkdir -p $L/$k/clipes
  wavespeed upload $L/base/$k.png --json 2>/dev/null | python3 -c "import json,sys;print(json.load(sys.stdin)['url'])" > $L/$k/url.txt
  python3 - "$k" <<'PY'
import json,sys,os
k=sys.argv[1]; L='centerpag-detect/criativos/kendall-1987478995288058-avatar-cenario-2026-09-25'; SEED=int(os.environ.get('SEED','7'))
pessoa,cena=open(f'{L}/base/{k}.txt').read().split(' | ')
for b in ['c1','c2']:
    vp=(f"One continuous vertical phone video, full frame edge to edge from the first frame to the last. The woman — {pessoa} — sits alone, {cena}, and stays exactly the same person the whole time: same face, same hair, same clothes, same seat, same distance from the camera. "
        "Handheld-steady phone on a tripod, the camera stays still; the room around her stays still. She talks straight into the camera, serious and caring, like warning a friend, with small natural head movements; her hands stay clasped near her knees with small gestures.")
    json.dump({'image':open(f'{L}/{k}/url.txt').read().strip(),'audio':open(f'{L}/audio/url-{b}.txt').read().strip(),'resolution':'720p','video_prompt':vp,'seed':SEED},open(f'{L}/{k}/clipes/{b}.req.json','w'))
PY
  for b in ${BLOCOS:-c1 c2}; do
    (wavespeed run pruna-ai/p-video/avatar --input-file $L/$k/clipes/$b.req.json --json --download $L/$k/clipes/$b.mp4 > $L/$k/clipes/$b.out.json 2> $L/$k/clipes/$b.log && echo "ok $k $b" || { echo "FALHOU $k $b"; tail -c 150 $L/$k/clipes/$b.log; }) &
  done; wait
done
