#!/bin/bash
# 2 clipes Pruna com o áudio ORIGINAL do trecho (mesmo corte da var1): c1 = n 0-447 (0-14,93 s; base A → tela cheia A + recorte B) · c2 = n 448-524 (14,93-17,5 s; close C).
# Avatar e cenários em base/elenco.json. Prompt só em positivo. Uso (desta pasta): SEED=7 bash gerar-clipes.sh c1 [c2]
set -e; cd "$(dirname "$0")"; SEED=${SEED:-7}
for b in "$@"; do
  python3 - $b $SEED <<'PY'
import json,sys
b,seed=sys.argv[1],int(sys.argv[2]); e=json.load(open('base/elenco.json'))
if b=='c1':
    img=open('base/url-A.txt').read().strip(); aud=open('audio/url-a1.txt').read().strip()
    vp=(f"One continuous vertical phone selfie video, full frame edge to edge from the first frame to the last. The man — {e['p']} — sits alone in {e['a_short']}, "
        "and stays exactly the same person the whole time: same face, same hair, same clothes, same distance from the camera, his head in the lower half of the frame. "
        "The phone rests steady; the camera stays still; the room around him stays still. He talks straight into the camera, serious and confident, like telling a friend a secret, with small natural head movements and calm shoulders.")
else:
    img=open('base/url-C.txt').read().strip(); aud=open('audio/url-a2.txt').read().strip()
    vp=(f"One continuous vertical phone selfie video, full frame edge to edge from the first frame to the last. The man — {e['p']} — {e['c_short']}, close to the camera, "
        "and stays exactly the same person the whole time: same face, same hair, same clothes, same distance from the camera. The camera stays still; the place behind him stays still. "
        "He talks straight into the camera, serious and confident, with small natural head movements.")
json.dump({'image':img,'audio':aud,'resolution':'720p','video_prompt':vp,'seed':seed},open(f'clipes/{b}.req.json','w'))
PY
  (wavespeed run pruna-ai/p-video/avatar --input-file clipes/$b.req.json --json --download clipes/$b.mp4 > clipes/$b.out.json 2> clipes/$b.log && echo "ok $b" || { echo "FALHOU $b"; tail -c 200 clipes/$b.log; }) &
done; wait
