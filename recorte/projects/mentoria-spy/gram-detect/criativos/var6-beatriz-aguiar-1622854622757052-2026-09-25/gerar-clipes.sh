#!/bin/bash
# Clipes da peça (mesmo molde da var1, elenco de elenco.json). Pruna p-video/avatar (lipsync, áudio ORIGINAL do trecho, 720p, seed 7,
# prompt só em positivo): s1 10,30-14,30 · s2 21,40-27,60 · s3 39,567-46,0. Seedance v1 Lite i2v 720p (esquete, sem fala): eA 8 s (porta) · eB 3 s (plano aberto).
# Uso: bash gerar-clipes.sh s1 s2 s3 eA eB   (SEED=n pra regerar um clipe podre)
cd "$(dirname "$0")"; mkdir -p clipes; SEED=${SEED:-7}
python3 - "$SEED" <<'PY'
import json,sys
S=int(sys.argv[1]); u=lambda f: open(f).read().strip(); E=json.load(open('elenco.json'))
vp=(f"One continuous vertical front-camera phone video, full frame edge to edge from the first frame to the last. {E['H_CURTO']}, "
    "and stays exactly the same person the whole time: same face, same hair, same clothes, same distance from the camera. "
    "The phone is held steady at arm's length; the room behind him stays still and dim. He talks straight into the camera in a confident, conspiratorial tone, like telling a friend a secret, with small natural head movements.")
for s in ['s1','s2','s3']:
    json.dump({'image':u('base/url-homem.txt'),'audio':u(f'audio/url-{s}.txt'),'resolution':'720p','video_prompt':vp,'seed':S},open(f'clipes/{s}.req.json','w'))
json.dump({'image':u('base/url-mulherA.txt'),'duration':8,'aspect_ratio':'9:16','seed':S,'camera_fixed':False,'prompt':
  f"Shaky amateur handheld phone video filmed by her boyfriend in {E['HALL']}. {E['M_CURTO']} is dramatically outraged: "
  "she shouts and talks fast at the camera, waves her phone in one hand, gestures wildly with the other, lunges toward the camera and swats at it so the frame whips around, then stumbles back and leans against the wall, still ranting. "
  "Comedic skit energy, fast jerky handheld camera movement, natural indoor light, realistic."},open('clipes/eA.req.json','w'))
json.dump({'image':u('base/url-mulherB.txt'),'duration':3,'aspect_ratio':'9:16','seed':S,'camera_fixed':False,'prompt':
  f"Handheld amateur phone video, slightly shaky. {E['M_CURTO']} leans back against the edge of the open doorway, holding her phone, looking up at the ceiling and ranting dramatically, "
  "shaking her head and moving her free hand, comedic skit energy, the camera stays at the same wide distance. Natural indoor light, realistic."},open('clipes/eB.req.json','w'))
PY
for b in "$@"; do
  case $b in s*) M=pruna-ai/p-video/avatar;; e*) M=bytedance/seedance-v1-lite-i2v-720p;; esac
  (wavespeed run $M --input-file clipes/$b.req.json --json --download clipes/$b.mp4 > clipes/$b.out.json 2> clipes/$b.log \
     && python3 -c "import json;j=json.load(open('clipes/$b.out.json'));open('molde/prediction-ids.txt','a').write(j['id']+' $b seed$SEED\n')" \
     && echo "ok $b" || { echo "FALHOU $b"; tail -c 300 clipes/$b.log; }) &
done; wait
# validação: decodifica inteiro; se truncou, rebaixa do .out.json
for b in "$@"; do
  f=clipes/$b.mp4; e=$(ffmpeg -v error -i $f -f null - 2>&1 | wc -l); n=$(ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames -of csv=p=0 $f 2>/dev/null)
  if [ "$e" -gt 0 ] || [ -z "$n" ]; then
    echo "TRUNCADO $b ($e erros) - rebaixando"; curl -s -o $f "$(python3 -c "import json;print(json.load(open('clipes/$b.out.json'))['outputs'][0])")"
    e=$(ffmpeg -v error -i $f -f null - 2>&1 | wc -l); n=$(ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames -of csv=p=0 $f)
  fi; echo "$b decodifica: erros=$e frames=$n"
done
