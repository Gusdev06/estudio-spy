#!/bin/bash
# 4 clipes Pruna (a1, b, a2, a3) com o áudio ORIGINAL de cada bloco; prompt só em positivo. Os blocos não se sobrepõem na fala (medido: silêncio 3,65-4,05 e 7,40-7,60),
# então nenhum trecho precisa ir mudo. Uso (de projects/mentoria-spy/): SEED=7 BLOCOS="a1 b a2 a3" bash centerpag-detect/criativos/var6-flora-959352790554428-2026-09-25/gerar-clipes.sh
set -e; cd "$(dirname "$0")/../../.."; L=centerpag-detect/criativos/var6-flora-959352790554428-2026-09-25; S=${SEED:-7}
python3 - "$S" <<'PY'
import json,sys
L='centerpag-detect/criativos/var6-flora-959352790554428-2026-09-25'; S=int(sys.argv[1])
desc={p:open(f'{L}/base/{p}.txt').read().strip() for p in 'AB'}; url={p:open(f'{L}/base/url-{p}.txt').read().strip() for p in 'AB'}
lado={'A':'toward the right, where the other host sits off-camera','B':'toward the left, where the other host sits off-camera'}
for b,d in json.load(open(f'{L}/molde/blocos.json')).items():
    p=d['papel']; quem='woman' if p=='A' else 'man'
    vp=(f"One continuous full-frame close-up shot in a dim room at night with a large window showing blurred city lights behind; the video fills the whole frame edge to edge from the first frame to the last. "
        f"The {quem} — {desc[p]} — wearing black over-ear headphones, speaks into the black podcast microphone, alone in the shot, and stays exactly the same person the whole time: same face, same hair, same clothes, same distance from the camera. "
        f"Locked-off camera on a tripod; the background stays still. The {quem} talks {lado[p]}, "
        + ("confident and knowing, explaining something, with small natural head movements." if p=='A' else "curious and surprised, asking a question, with small natural head movements."))
    json.dump({'image':url[p],'audio':open(f'{L}/audio/url-{b}.txt').read().strip(),'resolution':'720p','video_prompt':vp,'seed':S},open(f'{L}/clipes/{b}-s{S}.req.json','w'))
PY
for b in ${BLOCOS:-a1 b a2 a3}; do
  (wavespeed run pruna-ai/p-video/avatar --input-file $L/clipes/$b-s$S.req.json --json --download $L/clipes/$b-s$S.mp4 > $L/clipes/$b-s$S.out.json 2> $L/clipes/$b-s$S.log && echo "ok $b s$S" || { echo "FALHOU $b s$S"; tail -c 200 $L/clipes/$b-s$S.log; }) &
done; wait
