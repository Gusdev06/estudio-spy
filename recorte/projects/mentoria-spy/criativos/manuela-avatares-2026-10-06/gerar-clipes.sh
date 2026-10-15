#!/bin/bash
# Pruna p-video/avatar, áudio ORIGINAL do trecho, seed 7, prompt só em positivo. Uso: bash gerar-clipes.sh a1 [a2 ...]  (gera s1 s2 s3 de cada)
cd "$(dirname "$0")"; mkdir -p clipes
for a in "$@"; do
python3 - "$a" <<'PY'
import json,sys
a=sys.argv[1]; u=lambda f: open(f).read().strip()
D={'a1':"a young Latina woman with warm olive-tan skin and long wavy dark-brown hair, wearing a plain black fitted top",
   'a2':"a young Black woman with deep-brown skin and shoulder-length natural curly black hair, wearing a plain white t-shirt",
   'a3':"a young woman with fair skin, light-blue eyes and straight light-blonde hair, wearing a plain light-blue knit sweater",
   'a4':"a young East Asian woman with straight shoulder-length black hair and soft curtain bangs, wearing a plain oatmeal-beige knit sweater",
   'a5':"a young woman with freckles, green eyes and wavy copper-red hair, wearing an olive-green cardigan over a white top"}[a]
vp=("One continuous vertical front-camera phone selfie video, full frame edge to edge from the first frame to the last. "
    f"The woman in the image, {D}, stays EXACTLY the same person from the first frame to the last: same face, same hairstyle, same clothes, same framing, same distance from the camera. "
    "She is alone in a bright bedroom with beige curtains behind her; the room stays still. Both of her arms hang relaxed at her sides, completely out of frame, for the whole clip; only her head, shoulders and upper chest are visible. "
    "She talks straight into the camera in a warm, serious, caring tone, like warning a close friend, with small natural head movements and natural blinking.")
for s in ['s1','s2','s3']:
    json.dump({'image':u(f'base/url-{a}.txt'),'audio':u(f'audio/url-{s}.txt'),'resolution':'720p','video_prompt':vp,'seed':7},open(f'clipes/{a}-{s}.req.json','w'))
PY
for s in s1 s2 s3; do b=$a-$s
  (wavespeed run pruna-ai/p-video/avatar --input-file clipes/$b.req.json --json --download clipes/$b.mp4 > clipes/$b.out.json 2> clipes/$b.log && echo "ok $b" || { echo "FALHOU $b"; tail -c 300 clipes/$b.log; }) &
done; done; wait
