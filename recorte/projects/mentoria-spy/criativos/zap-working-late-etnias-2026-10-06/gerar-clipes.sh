#!/bin/bash
# Lipsync Pruna p-video/avatar (720p, seed 7) com o áudio ORIGINAL inteiro (30,4 s) sobre base/<v>.png. Prompt só em positivo.
# Uso: bash gerar-clipes.sh v1-branco ...  (SEED=n pra regerar um clipe podre). Valida decodificando inteiro; rebaixa se truncou.
cd "$(dirname "$0")"; SEED=${SEED:-7}
[ -s audio/url.txt ] || wavespeed upload audio/audio.m4a 2>&1 | grep -o 'https://[^ ]*' > audio/url.txt
for v in "$@"; do python3 - "$v" "$SEED" <<'PY'
import json,sys
v,S=sys.argv[1],int(sys.argv[2]); u=lambda f: open(f).read().strip()
vp=("SOLO SHOT. One continuous front-camera phone video, the same framing from the first frame to the last. "
    "The same young man in a plain black t-shirt sits on the edge of his bed and stays exactly the same person the whole time: same face, same hair, same clothes, same distance from the camera. "
    "The phone stays steady; the bedroom behind him stays still. He talks straight into the camera in a serious, confessional tone, with small natural head movements.")
json.dump({'image':u(f'base/url-{v}.txt'),'audio':u('audio/url.txt'),'resolution':'720p','video_prompt':vp,'seed':S},open(f'clipes/{v}.req.json','w'))
PY
done
for v in "$@"; do
  (wavespeed run pruna-ai/p-video/avatar --input-file clipes/$v.req.json --json --download clipes/$v.mp4 > clipes/$v.out.json 2> clipes/$v.log \
    && python3 -c "import json;j=json.load(open('clipes/$v.out.json'));open('prediction-ids.txt','a').write(j['id']+' pruna $v seed$SEED\n')" \
    && echo "ok $v" || { echo "FALHOU $v"; tail -c 300 clipes/$v.log; }) &
done; wait
for v in "$@"; do
  f=clipes/$v.mp4; [ -f clipes/$v.out.json ] && grep -q outputs clipes/$v.out.json || { echo "sem saída $v"; continue; }; e=$(ffmpeg -v error -i $f -f null - 2>&1 | wc -l); n=$(ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames -of csv=p=0 $f 2>/dev/null)
  if [ "$e" -gt 0 ] || [ -z "$n" ]; then echo "TRUNCADO $v - rebaixando"; curl -s -o $f "$(python3 -c "import json;print(json.load(open('clipes/$v.out.json'))['outputs'][0])")"
    e=$(ffmpeg -v error -i $f -f null - 2>&1 | wc -l); n=$(ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames -of csv=p=0 $f); fi
  echo "$v erros=$e frames=$n $(ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration -of csv=p=0 $f | tr '\n' ' ')"
done
