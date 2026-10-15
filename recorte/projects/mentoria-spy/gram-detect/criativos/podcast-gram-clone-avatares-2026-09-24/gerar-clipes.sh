#!/bin/bash
# 4 clipes Pruna por elenco (a1, b, a2, a3), áudio ORIGINAL do bloco (no b, a fala da host fora de quadro vai muda).
# Uso (de projects/mentoria-spy/): bash gram-detect/criativos/podcast-gram-clone-avatares-2026-09-24/gerar-clipes.sh g1 [g2 …]
set -e; cd "$(dirname "$0")/../../.."; L=gram-detect/criativos/podcast-gram-clone-avatares-2026-09-24
for k in "$@"; do
  mkdir -p $L/$k/clipes
  for p in A B; do wavespeed upload $L/base/$k-$p.png --json 2>/dev/null | python3 -c "import json,sys;print(json.load(sys.stdin)['url'])" > $L/$k/url-$p.txt; done
  python3 - "$k" <<'PY'
import json,sys,os
SEED=int(os.environ.get('SEED','21'))
k=sys.argv[1]; L='gram-detect/criativos/podcast-gram-clone-avatares-2026-09-24'
desc={p:open(f'{L}/base/{k}-{p}.txt').read().strip() for p in 'AB'}; url={p:open(f'{L}/{k}/url-{p}.txt').read().strip() for p in 'AB'}
for b,d in json.load(open(f'{L}/molde/blocos.json')).items():
    p=d['papel']
    vp=(f"One continuous full-frame shot of a dark cozy podcast studio at night: the video fills the whole frame edge to edge from the first frame to the last. "
        f"The woman — {desc[p]} — sits alone in her armchair and stays exactly the same person the whole time: same face, same hair, same clothes, same headphones, same seat, same distance from the camera. "
        "Locked-off camera on a tripod; the room around her stays still and empty, only the candle flames flicker. "
        + ("She talks to the person off-camera, confident and knowing, relaxed, small natural head and hand movements." if p=='A' else
           "She reacts to the person off-camera: curious, surprised, a bit skeptical; during silences in the audio she listens with her mouth closed, nodding slightly."))
    json.dump({'image':url[p],'audio':open(f'{L}/audio/url-{b}.txt').read().strip(),'resolution':'720p','video_prompt':vp,'seed':SEED},open(f'{L}/{k}/clipes/{b}.req.json','w'))
PY
  for b in ${BLOCOS:-a1 b a2 a3}; do
    (wavespeed run pruna-ai/p-video/avatar --input-file $L/$k/clipes/$b.req.json --json --download $L/$k/clipes/$b.mp4 > $L/$k/clipes/$b.out.json 2> $L/$k/clipes/$b.log && echo "ok $k $b" || { echo "FALHOU $k $b"; tail -c 150 $L/$k/clipes/$b.log; }) &
  done; wait
done
