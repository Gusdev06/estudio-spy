#!/bin/bash
# Clipes Pruna de uma peça (um por bloco de fala com rosto), prompt de identidade travada da var6, áudio do bloco da copy nova.
# Uso (de projects/mentoria-spy/): bash .../gerar-clipes.sh 170 [b1 b3 …]   (sem blocos = os 6)
cd "$(dirname "$0")/../../.."; D=centerpag-detect/criativos/podcast-wpp-cp108-avatar-copy-2026-10-07; N=centerpag-detect/criativos/podcast-wpp-57s-copy-nova-2026-09-23
k=$1; shift; BL=${*:-b1 b3 b4 b5 b6 b8}; C=$D/c$k/clipes; mkdir -p $C
up(){ for t in 1 2 3; do U=$(wavespeed upload "$1" --json 2>/dev/null | python3 -c "import json,sys;print(json.load(sys.stdin)['url'])" 2>/dev/null); [ -n "$U" ] && { echo "$U"; return; }; sleep 2; done; }
for p in A B; do [ -s $D/c$k/url-$p.txt ] || [ ! -f $D/base/$k-$p.png ] || up $D/base/$k-$p.png > $D/c$k/url-$p.txt; done
for b in $BL; do [ -s $C/url-$b.txt ] || up $D/audio/$k/$b.mp3 > $C/url-$b.txt; done
python3 - "$k" $BL <<'PY'
import json,sys
k=sys.argv[1]; D='centerpag-detect/criativos/podcast-wpp-cp108-avatar-copy-2026-10-07'; N='centerpag-detect/criativos/podcast-wpp-57s-copy-nova-2026-09-23'
info=json.load(open(f'{D}/molde/{k}/blocos.json'))
import os
desc={p:open(f'{D}/base/{k}-{p}.txt').read().strip() for p in 'AB' if os.path.exists(f'{D}/base/{k}-{p}.txt')}
url={p:open(f'{D}/c{k}/url-{p}.txt').read().strip() for p in 'AB' if os.path.exists(f'{D}/c{k}/url-{p}.txt')}
for bid in sys.argv[2:]:
    p=info[bid]['papel']; au=open(f'{D}/c{k}/clipes/url-{bid}.txt').read().strip(); assert url[p] and au, 'upload vazio'
    r={'image':url[p],'audio':au,'resolution':'720p','seed':21,
       'video_prompt':(f"The woman in the image — {desc[p]} — stays EXACTLY the same person from the first frame to the last: same face, same hair, same clothes, same seated position and distance from the camera. "
     "Podcast studio, locked-off camera on a tripod; the camera never moves and the background, sofa and microphone stay exactly the same. She is the ONLY person in the frame; her hands rest on her lap, out of the way, and nothing and nobody enters from any edge. "
     + ("She talks to someone off-camera, warm and knowing, with small natural head movements." if p=='A' else "She asks a question, curious and a bit skeptical, eyebrows slightly raised, looking at the person off-camera."))}
    json.dump(r,open(f'{D}/c{k}/clipes/{bid}.req.json','w'))
PY
for b in $BL; do
  (wavespeed run pruna-ai/p-video/avatar --input-file $C/$b.req.json --json --download $C/$b.mp4 > $C/$b.out.json 2> $C/$b.log; \
   if [ -n "$(ffmpeg -v error -i $C/$b.mp4 -f null - 2>&1)" ] || [ ! -s $C/$b.mp4 ]; then echo "INVALIDO $k $b"; tail -c 200 $C/$b.log; else echo "ok $k $b"; fi) &
done; wait
