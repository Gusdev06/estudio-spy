#!/bin/bash
# 2 clipes Pruna com o áudio ORIGINAL do trecho: c1 = n 0-447 (0-14,93 s; plano da sala → tela cheia A + recorte B) · c2 = n 448-524 (14,93-17,5 s; close na varanda).
# Prompt só em positivo (lição do podcast Gram, 24/09). Uso (desta pasta): SEED=7 bash gerar-clipes.sh c1 [c2]
set -e; cd "$(dirname "$0")"; SEED=${SEED:-7}
PESSOA="a white man about 45 years old with short thick dark-brown hair greying at the temples and a full short dark beard, wearing a plain heather-grey crew-neck t-shirt"
for b in "$@"; do
  if [ $b = c1 ]; then IMG=$(cat base/url-A2.txt); AUD=$(cat audio/url-a1.txt)
    VP="One continuous vertical phone selfie video, full frame edge to edge from the first frame to the last. The man — $PESSOA — sits alone in a cozy living room with a bookshelf and a floor lamp behind him, and stays exactly the same person the whole time: same face, same beard, same t-shirt, same distance from the camera, his head in the lower half of the frame. The phone rests steady; the camera stays still; the room around him stays still. He talks straight into the camera, serious and confident, like telling a friend a secret, with small natural head movements and calm shoulders."
  else IMG=$(cat base/url-C.txt); AUD=$(cat audio/url-a2.txt)
    VP="One continuous vertical phone selfie video, full frame edge to edge from the first frame to the last. The man — $PESSOA — stands alone on a sunny front porch, close to the camera, and stays exactly the same person the whole time: same face, same beard, same t-shirt, same distance from the camera. The camera stays still; the porch and trees behind him stay still. He talks straight into the camera, serious and confident, with small natural head movements."
  fi
  mkdir -p clipes; python3 -c "import json,sys;json.dump({'image':sys.argv[1],'audio':sys.argv[2],'resolution':'720p','video_prompt':sys.argv[3],'seed':int(sys.argv[4])},open('clipes/$b.req.json','w'))" "$IMG" "$AUD" "$VP" $SEED
  (wavespeed run pruna-ai/p-video/avatar --input-file clipes/$b.req.json --json --download clipes/$b.mp4 > clipes/$b.out.json 2> clipes/$b.log && echo "ok $b" || { echo "FALHOU $b"; tail -c 200 clipes/$b.log; }) &
done; wait
