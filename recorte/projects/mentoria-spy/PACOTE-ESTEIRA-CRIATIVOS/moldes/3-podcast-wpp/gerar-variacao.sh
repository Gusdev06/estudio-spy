#!/bin/bash
# Gera uma variação de elenco do clone: 2 closes + 1 two-shot (gpt-image-2/edit, quality=medium) e os 5 clipes Pruna.
# Uso:  bash gerar-variacao.sh <vN> imagens   |   bash gerar-variacao.sh <vN> twoshot   |   bash gerar-variacao.sh <vN> clipes
# As descrições de cada elenco ficam em elencos/<vN>-A.txt e <vN>-B.txt. Áudio dos blocos é o mesmo para todas (do original).
set -e; cd "$(dirname "$0")/../../.."
N=centerpag-detect/criativos/podcast-wpp-clone-avatares-2026-09-13; V=$1; ACAO=$2
UA=$(cat $N/base/url-ref-close-A.txt); UB=$(cat $N/base/url-ref-close-B.txt); UTS=$(cat $N/base/url-ref-two-shot.txt 2>/dev/null || true)
ROUPA_A=$(cat $N/elencos/$V-A-roupa.txt 2>/dev/null || echo "sage-green ribbed knit top, light blue jeans")
ROUPA_B=$(cat $N/elencos/$V-B-roupa.txt 2>/dev/null || echo "plain black long-sleeve top, black trousers")
COMUM_A="Same podcast studio, same camera, same framing distance, same warm daylight, same cream sofa and background with green plants, same black podcast microphone on a boom arm entering from the left. Extend the scene vertically to a 9:16 vertical frame, keeping the original composition in the middle band. REPLACE the woman with a DIFFERENT woman:"
COMUM_B="Same podcast studio, same camera, same framing distance, same warm daylight, same cream sofa and background with green plants and a light patterned wall, same black podcast microphone on a boom arm entering from the left. Extend the scene vertically to a 9:16 vertical frame, keeping the original composition in the middle band. REPLACE the woman with a DIFFERENT woman:"
FIM_A="She sits in the same position, same posture, same distance from the microphone, head and upper chest visible, looking slightly off-camera toward the person she is talking to, mouth closed, warm confident expression. Photorealistic video still, natural skin texture with visible pores, no retouching, not a model, no text, no logos, no watermark."
FIM_B="She sits in the same position, same posture, same distance from the microphone, head and upper chest visible, turned slightly toward the person she is talking to off-camera, mouth closed, curious and skeptical expression. Photorealistic video still, natural skin texture with visible pores, no retouching, not a model, no text, no logos, no watermark."
img(){ # papel url_ref prompt
  python3 -c "
import json,sys
json.dump({'prompt':sys.argv[1],'images':[sys.argv[2]],'aspect_ratio':'9:16','quality':'medium','resolution':'1k'},open('$N/$V/base/close-$3.req.json','w'))" "$1" "$2" "$3"
  wavespeed run openai/gpt-image-2/edit --input-file $N/$V/base/close-$3.req.json --json --download $N/$V/base/close-$3.png > $N/$V/base/close-$3.json 2> $N/$V/base/close-$3.log && echo "ok $V close $3" || { echo "FALHOU $V close $3"; tail -2 $N/$V/base/close-$3.log; }
}
case "$ACAO" in
imagens)
  A=$(cat $N/elencos/$V-A.txt); B=$(cat $N/elencos/$V-B.txt)
  img "$COMUM_A $A $FIM_A" "$UA" A &
  img "$COMUM_B $B $FIM_B" "$UB" B &
  wait ;;
twoshot)
  A=$(cat $N/elencos/$V-A.txt); B=$(cat $N/elencos/$V-B.txt)
  UA2=$(wavespeed upload $N/$V/base/close-A.png 2>/dev/null | grep -o 'https://[^ ]*' | tail -1); echo "$UA2" > $N/$V/base/url-A.txt
  UB2=$(wavespeed upload $N/$V/base/close-B.png 2>/dev/null | grep -o 'https://[^ ]*' | tail -1); echo "$UB2" > $N/$V/base/url-B.txt
  P="Recreate the FIRST image exactly — same podcast studio, same cream curved sofa, same low round table, same two black podcast microphones on boom arms, same green plants, same light patterned wall, same wide two-shot framing from the same camera position and height, same warm daylight, same body language (both women seated turned toward each other, mid-conversation). ONLY REPLACE the two women: the woman on the RIGHT must be the woman from the SECOND image ($A, $ROUPA_A). The woman on the LEFT must be the woman from the THIRD image ($B, $ROUPA_B). Keep their faces, hair and clothing exactly as in those images. Photorealistic video still, natural skin texture, no retouching, no text, no logos, no watermark."
  python3 -c "
import json,sys
json.dump({'prompt':sys.argv[1],'images':[sys.argv[2],sys.argv[3],sys.argv[4]],'aspect_ratio':'9:16','quality':'medium','resolution':'1k'},open('$N/$V/base/two-shot.req.json','w'))" "$P" "$UTS" "$UA2" "$UB2"
  wavespeed run openai/gpt-image-2/edit --input-file $N/$V/base/two-shot.req.json --json --download $N/$V/base/two-shot.png > $N/$V/base/two-shot.json 2> $N/$V/base/two-shot.log && echo "ok $V two-shot" || { echo "FALHOU $V two-shot"; tail -2 $N/$V/base/two-shot.log; } ;;
clipes)
  SOLO="SOLO SHOT: exactly one person in the frame at all times. Nobody else is visible, no second person, no one enters or appears at the edges of the frame. Podcast studio, locked-off camera on a tripod. The background stays completely static and unchanged."
  A=$(cat $N/$V/base/url-A.txt); B=$(cat $N/$V/base/url-B.txt)
  TS=$(wavespeed upload $N/$V/base/two-shot.png 2>/dev/null | grep -o 'https://[^ ]*' | tail -1); echo "$TS" > $N/$V/base/url-TS.txt
  gen(){ AU=$(grep "^$1	" $N/audio/urls.txt | cut -f2)
    python3 -c "
import json,sys
json.dump({'image':sys.argv[1],'audio':sys.argv[2],'resolution':'720p','video_prompt':sys.argv[3],'seed':7},open('$N/$V/clipes/bloco-$1b.req.json','w'))" "$2" "$AU" "$3"
    wavespeed run pruna-ai/p-video/avatar --input-file $N/$V/clipes/bloco-$1b.req.json --json --download $N/$V/clipes/bloco-$1b.mp4 > $N/$V/clipes/bloco-$1b.out.json 2> $N/$V/clipes/bloco-$1b.log && echo "ok $V bloco $1" || { echo "FALHOU $V bloco $1"; tail -2 $N/$V/clipes/bloco-$1b.log; } }
  gen 1 "$TS" "Podcast studio, locked-off wide two-shot on a tripod. EXACTLY TWO women are in the frame, both seated on the cream sofa, and nobody else ever appears. Only the woman on the RIGHT ($ROUPA_A) is talking; the woman on the LEFT ($ROUPA_B) listens quietly with her mouth closed and nods slightly. The background, the table and the microphones stay completely static." &
  gen 2 "$A" "$SOLO The woman on the right ($ROUPA_A) talks to someone off-camera with a knowing, slightly amused expression, leaning in a little as she reveals something." &
  gen 3 "$B" "$SOLO The woman ($ROUPA_B) asks a question, curious and a bit skeptical, eyebrows raised, turning slightly toward someone off-camera, listening in between." &
  gen 4 "$A" "$SOLO The woman ($ROUPA_A) explains something calmly to someone off-camera, small natural head movements, hands mostly still." &
  gen 5 "$A" "$SOLO The woman ($ROUPA_A) talks straight toward the camera, warm and persuasive, inviting the viewer." &
  wait ;;
*) echo "ação inválida: use imagens | twoshot | clipes" >&2; exit 1 ;;
esac
