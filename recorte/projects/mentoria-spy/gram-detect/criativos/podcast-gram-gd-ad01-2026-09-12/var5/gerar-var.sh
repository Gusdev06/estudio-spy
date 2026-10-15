#!/bin/bash
# 5 variações de hook do podcast Gram: TTS + clipe da CENA 1 (Pruna) + whisper, por variante. Cenas 2-7 ficam idênticas.
# TTS 5 × centavos + Pruna 5 × ~4 s a US$ 0,025/s ≈ US$ 0,55. Uso: bash gerar-var.sh [v1 v2 ...]
set -e; cd "$(dirname "$0")/../../../.."; N=gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12; V=$N/var5
P2=https://d2h7xmz5gqybh9.cloudfront.net/media/cc96ac48027e40ab8f92189bbfcd32c9/images/1788545004271130626_7RDLU4dn.png   # close host
PROMPT="Podcast studio, fixed camera. The host (woman in black blazer) is talking straight into the camera lens, firm and confident, small head movements, subtle hand gesture. Background static, no camera movement, no zoom."
VARS=${@:-$(grep -v '^#' $V/hooks.tsv | cut -f1)}
for v in $VARS; do
 ( FALA=$(grep "^$v	" $V/hooks.tsv | cut -f5)
   echo "== $v: $FALA"
   wavespeed run minimax/speech-2.6-hd -i "text=$FALA" -i voice_id=Wise_Woman -i language_boost=English --json --download $V/audio/host-1-$v.mp3 > $V/audio/tts-$v.json 2> $V/audio/tts-$v.log
   AU=$(wavespeed upload $V/audio/host-1-$v.mp3 2>/dev/null | grep -o 'https://[^ ]*' | tail -1); echo "$v	$AU" >> $V/audio/urls.txt
   python3 -c "import json,sys;json.dump({'image':sys.argv[1],'audio':sys.argv[2],'resolution':'720p','video_prompt':sys.argv[3]},open('$V/clipes/cena-1-$v.json','w'))" "$P2" "$AU" "$PROMPT"
   wavespeed run pruna-ai/p-video/avatar --input-file $V/clipes/cena-1-$v.json --json --download $V/clipes/cena-1-$v.mp4 > $V/clipes/cena-1-$v.out.json 2> $V/clipes/cena-1-$v.log
   # whisper no áudio embutido do clipe (fonte da timeline e do karaokê)
   mkdir -p $V/audio/$v; ffmpeg -v error -y -i $V/clipes/cena-1-$v.mp4 -vn -ac 1 -ar 16000 $V/audio/$v/c1-16k.wav
   uvx --from mlx-whisper mlx_whisper $V/audio/$v/c1-16k.wav --model mlx-community/whisper-small.en-mlx --word-timestamps True --output-dir $V/audio/$v --output-format json --language en >/dev/null 2>&1
   mv $V/audio/$v/c1-16k.json $V/audio/$v/clip-cena-1.json; rm -f $V/audio/$v/c1-16k.wav
   for i in 2 3 4 5 6 7; do ln -sf ../../../audio/clip-cena-$i.json $V/audio/$v/clip-cena-$i.json; done
   mkdir -p $V/clipes/$v; ln -sf ../cena-1-$v.mp4 $V/clipes/$v/cena-1.mp4
   for i in 2 3 4 5 6 7; do ln -sf ../../../clipes/cena-$i.mp4 $V/clipes/$v/cena-$i.mp4; done
   echo "ok $v" ) &
done
wait
