#!/bin/bash
# 7 clipes do podcast Gram: minimax/h3/reference-to-video 768p 9:16, imagem do plano + áudio TTS de referência (lipsync nativo).
# Durações = fim da fala (whisper) + ~1 s, arredondado pro enum do H3. 50 s pedidos ≈ US$ 5 (05/09: ~US$ 0,10/s em 768p).
# Uso: bash gerar-clipes.sh [cena ...]   (sem argumento = as 7, em paralelo). 'fetch failed' é transitório: rodar de novo só a cena.
set -e; cd "$(dirname "$0")/../../.."; N=gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12
P1=https://d2h7xmz5gqybh9.cloudfront.net/media/cc96ac48027e40ab8f92189bbfcd32c9/images/1788544362678888435_Z5BzYqVe.png   # two-shot
P2=https://d2h7xmz5gqybh9.cloudfront.net/media/cc96ac48027e40ab8f92189bbfcd32c9/images/1788545004271130626_7RDLU4dn.png   # close host
P3=https://d2h7xmz5gqybh9.cloudfront.net/media/cc96ac48027e40ab8f92189bbfcd32c9/images/1788545008818153992_lrSbwWyM.png   # close convidada
a(){ grep "^$1	" $N/audio/urls.txt | cut -f2; }
gen(){ # cena imagem audio duração prompt
  python3 -c "import json,sys;json.dump({'prompt':sys.argv[4],'reference_images':[sys.argv[1]],'reference_audios':[sys.argv[2]],'aspect_ratio':'9:16','resolution':'768p','duration':int(sys.argv[3])},open('$N/clipes/cena-$1.json','w'))" "$2" "$3" "$4" "$5"
  wavespeed run minimax/h3/reference-to-video --input-file $N/clipes/cena-$1.json --json --download $N/clipes/cena-$1.mp4 > $N/clipes/cena-$1.out.json 2> $N/clipes/cena-$1.log && echo "ok cena $1" || echo "FALHOU cena $1 (ver $N/clipes/cena-$1.log)"
}
c1(){ gen 1 $P2 "$(a host-1)" 5 "Podcast studio, fixed camera, close-up of the host (woman in black blazer). She speaks the line in <Audio 1> straight into the camera lens, firm and confident, natural lip sync, small head movements, subtle hand gesture. Warm amber light, background static. No camera movement, no zoom."; }
c2(){ gen 2 $P3 "$(a guest-2)" 9 "Podcast studio, fixed camera, close-up of the guest (woman in beige sweater). She speaks the line in <Audio 1> looking toward the host off-frame left, hesitant and confessional, natural lip sync, lowers her gaze to the table at the end. Elbows on the table. Warm light, background static. No camera movement."; }
c3(){ gen 3 $P1 "$(a guest-3)" 10 "Podcast studio, fixed camera, two-shot of both women at the table with microphones. The guest on the RIGHT (beige sweater) speaks the line in <Audio 1>, listing things, natural lip sync; the host on the LEFT (black blazer) listens, nods slightly, arms on the table, mouth closed. Warm light, background static. No camera movement."; }
c4(){ gen 4 $P2 "$(a host-4)" 7 "Podcast studio, fixed camera, close-up of the host (woman in black blazer). She speaks the line in <Audio 1> turned slightly toward the guest off-frame right, marking each point with her index finger, natural lip sync, energetic. Warm light, background static. No camera movement."; }
c5(){ gen 5 $P3 "$(a guest-5-pad)" 4 "Podcast studio, fixed camera, close-up of the guest (woman in beige sweater). She turns from the host and looks straight into the camera lens while speaking the line in <Audio 1>, calm and direct, natural lip sync. Warm light, background static. No camera movement."; }
c6(){ gen 6 $P2 "$(a host-6)" 10 "Podcast studio, fixed camera, close-up of the host (woman in black blazer). She speaks the lines in <Audio 1> straight into the camera lens, clear and persuasive, natural lip sync, small hand gestures, brief pause between sentences. Warm light, background static. No camera movement."; }
c7(){ gen 7 $P1 "$(a host-7)" 5 "Podcast studio, fixed camera, two-shot of both women at the table with microphones. The host on the LEFT (black blazer) speaks the line in <Audio 1> into the camera, natural lip sync; the guest on the RIGHT (beige sweater) nods slowly, mouth closed. Warm light, background static. No camera movement."; }
if [ $# -eq 0 ]; then set -- 1 2 3 4 5 6 7; fi
for c in "$@"; do c$c & done; wait
