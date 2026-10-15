#!/bin/bash
# 4 clipes Pruna com o áudio ORIGINAL, emendados dentro dos flashes do original (n 404, 1060, 1463) pra esconder o reset de pose.
# Uso (de projects/mentoria-spy/): SEED=7 bash centerpag-detect/criativos/var4-amanda-lima-1259333446315112-2026-09-25/gerar-clipes.sh c1 [c2 …]
set -e; L=centerpag-detect/criativos/var4-amanda-lima-1259333446315112-2026-09-25; SEED=${SEED:-7}
[ -f $L/base/url-v4.txt ] || wavespeed upload $L/base/v4.png --json 2>/dev/null | python3 -c "import json,sys;print(json.load(sys.stdin)['url'])" > $L/base/url-v4.txt
for b in "$@"; do
  case $b in c1) i=0;f=404;; c2) i=404;f=1060;; c3) i=1060;f=1463;; c4) i=1463;f=1830;; esac
  a=$(python3 -c "print($i/30)"); z=$(python3 -c "print(min($f/30,60.858))")
  ffmpeg -v error -y -i $L/REFERENCIA-original.mp4 -vn -ss $a -to $z -c:a libmp3lame -q:a 2 $L/audio/$b.mp3
  wavespeed upload $L/audio/$b.mp3 --json 2>/dev/null | python3 -c "import json,sys;print(json.load(sys.stdin)['url'])" > $L/audio/url-$b.txt
  python3 - "$b" "$SEED" <<'PY'
import json,sys
b,seed=sys.argv[1],int(sys.argv[2]); L='centerpag-detect/criativos/var4-amanda-lima-1259333446315112-2026-09-25'
pessoa,cena=open(f'{L}/base/casting.txt').read().split(' | ')
vp=(f"One continuous vertical phone selfie video, full frame edge to edge from the first frame to the last. The woman, {pessoa}, sits alone in {cena}, and stays exactly the same person the whole time: same face, same hair, same clothes, same seat, same distance from the camera. "
    "The phone rests on a tripod and the camera stays still; the room around her stays still. She talks straight into the camera, sincere and a little emotional, like telling a friend a personal story, with small natural head movements and expressive hand gestures in front of her chest.")
json.dump({'image':open(f'{L}/base/url-v4.txt').read().strip(),'audio':open(f'{L}/audio/url-{b}.txt').read().strip(),'resolution':'720p','video_prompt':vp,'seed':seed},open(f'{L}/clipes/{b}.req.json','w'))
PY
  (wavespeed run pruna-ai/p-video/avatar --input-file $L/clipes/$b.req.json --json --download $L/clipes/$b.mp4 > $L/clipes/$b.out.json 2> $L/clipes/$b.log && echo "ok $b" || { echo "FALHOU $b"; tail -c 200 $L/clipes/$b.log; }) &
done; wait
