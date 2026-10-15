#!/bin/bash
# Clipes da peça. Pruna (lipsync, áudio ORIGINAL do trecho, seed 7, prompt só em positivo): s1 10,30-14,30 · s2 21,40-27,60 · s3 39,567-46,0.
# Seedance Lite 720p (esquete, sem fala): eA 8 s (plano da porta) · eB 3 s (plano aberto). Uso: bash gerar-clipes.sh s1 s2 s3 eA eB
cd "$(dirname "$0")"; mkdir -p clipes; SEED=${SEED:-7}
python3 - "$SEED" <<'PY'
import json,sys
S=int(sys.argv[1]); u=lambda f: open(f).read().strip()
vp=("One continuous vertical front-camera phone video, full frame edge to edge from the first frame to the last. A young man with light-brown skin, short dark hair with a low fade and a short stubble beard, "
    "in a plain heather-grey sweatshirt, sits alone on a sofa in a dim living room at night and stays exactly the same person the whole time: same face, same hair, same clothes, same distance from the camera. "
    "The phone is held steady at arm's length; the room behind him stays still and dim with a warm lamp glow. He talks straight into the camera in a confident, conspiratorial tone, like telling a friend a secret, with small natural head movements.")
for s in ['s1','s2','s3']:
    json.dump({'image':u('base/url-homem.txt'),'audio':u(f'audio/url-{s}.txt'),'resolution':'720p','video_prompt':vp,'seed':S},open(f'clipes/{s}.req.json','w'))
json.dump({'image':u('base/url-mulherA.txt'),'duration':8,'aspect_ratio':'9:16','seed':S,'camera_fixed':False,'prompt':
  "Shaky amateur handheld phone video filmed by her boyfriend in a narrow hallway with sage-green walls and a dark wooden door. The young woman with long curly hair in a pink hoodie is dramatically outraged: "
  "she shouts and talks fast at the camera, waves her phone in one hand, gestures wildly with the other, lunges toward the camera and swats at it so the frame whips around, then stumbles back and leans against the wall, still ranting. "
  "Comedic skit energy, fast jerky handheld camera movement, natural indoor light, realistic."},open('clipes/eA.req.json','w'))
json.dump({'image':u('base/url-mulherB.txt'),'duration':3,'aspect_ratio':'9:16','seed':S,'camera_fixed':False,'prompt':
  "Handheld amateur phone video, slightly shaky. The young woman with long curly hair in a pink hoodie leans back against the edge of the open doorway, holding her phone, looking up at the ceiling and ranting dramatically, "
  "shaking her head and moving her free hand, comedic skit energy, the camera stays at the same wide distance. Natural indoor light, realistic."},open('clipes/eB.req.json','w'))
PY
for b in "$@"; do
  case $b in s*) M=pruna-ai/p-video/avatar;; e*) M=bytedance/seedance-v1-lite-i2v-720p;; esac
  (wavespeed run $M --input-file clipes/$b.req.json --json --download clipes/$b.mp4 > clipes/$b.out.json 2> clipes/$b.log && echo "ok $b" || { echo "FALHOU $b"; tail -c 200 clipes/$b.log; }) &
done; wait
