#!/bin/bash
# 7 clipes do podcast Gram no Pruna (pruna-ai/p-video/avatar, 720p → 704×1280 24 fps, US$ 0,025/s): imagem do plano + áudio TTS.
# Escolha do Gusta (12/09): Pruna em vez do H3 (≈ US$ 1,10 vs 5,00). Risco conhecido: no two-shot o modelo anima um rosto só.
# Uso: bash gerar-clipes-pruna.sh [cena ...]   (sem argumento = as 7, em paralelo)
set -e; cd "$(dirname "$0")/../../.."; N=gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12
P1=https://d2h7xmz5gqybh9.cloudfront.net/media/cc96ac48027e40ab8f92189bbfcd32c9/images/1788544362678888435_Z5BzYqVe.png   # two-shot
P2=https://d2h7xmz5gqybh9.cloudfront.net/media/cc96ac48027e40ab8f92189bbfcd32c9/images/1788545004271130626_7RDLU4dn.png   # close host
P3=https://d2h7xmz5gqybh9.cloudfront.net/media/cc96ac48027e40ab8f92189bbfcd32c9/images/1788545008818153992_lrSbwWyM.png   # close convidada
a(){ grep "^$1	" $N/audio/urls.txt | cut -f2; }
gen(){ # cena imagem audio prompt
  python3 -c "import json,sys;json.dump({'image':sys.argv[1],'audio':sys.argv[2],'resolution':'720p','video_prompt':sys.argv[3]},open('$N/clipes/cena-$1.json','w'))" "$2" "$3" "$4"
  wavespeed run pruna-ai/p-video/avatar --input-file $N/clipes/cena-$1.json --json --download $N/clipes/cena-$1.mp4 > $N/clipes/cena-$1.out.json 2> $N/clipes/cena-$1.log && echo "ok cena $1" || echo "FALHOU cena $1 (ver $N/clipes/cena-$1.log)"
}
c1(){ gen 1 $P2 "$(a host-1)" "Podcast studio, fixed camera. The host (woman in black blazer) is talking straight into the camera lens, firm and confident, small head movements, subtle hand gesture. Background static, no camera movement, no zoom."; }
c2(){ gen 2 $P3 "$(a guest-2)" "Podcast studio, fixed camera. The guest (woman in beige sweater) is talking toward the host off-frame left, hesitant and confessional, elbows on the table, lowers her gaze at the end. Background static, no camera movement."; }
c3(){ gen 3 $P1 "$(a guest-3)" "Podcast studio, fixed camera, two women at the table with microphones. Only the woman on the RIGHT (beige sweater) is talking, listing things; the woman on the LEFT (black blazer) listens with her mouth closed and nods slightly. Background static, no camera movement."; }
c4(){ gen 4 $P2 "$(a host-4)" "Podcast studio, fixed camera. The host (woman in black blazer) is talking, turned slightly toward the guest off-frame right, marking each point with her index finger, energetic. Background static, no camera movement."; }
c5(){ gen 5 $P3 "$(a guest-5-pad)" "Podcast studio, fixed camera. The guest (woman in beige sweater) looks straight into the camera lens while talking, calm and direct. Background static, no camera movement."; }
c6(){ gen 6 $P2 "$(a host-6)" "Podcast studio, fixed camera. The host (woman in black blazer) is talking straight into the camera lens, clear and persuasive, small hand gestures. Background static, no camera movement."; }
c7(){ gen 7 $P1 "$(a host-7)" "Podcast studio, fixed camera, two women at the table with microphones. Only the woman on the LEFT (black blazer) is talking into the camera; the woman on the RIGHT (beige sweater) keeps her mouth closed and nods slowly. Background static, no camera movement."; }
if [ $# -eq 0 ]; then set -- 1 2 3 4 5 6 7; fi
for c in "$@"; do c$c & done; wait
