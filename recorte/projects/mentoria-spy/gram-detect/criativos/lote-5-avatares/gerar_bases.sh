#!/usr/bin/env bash
# Gera as 5 imagens-base com GPT Image 2, no mesmo molde validado do avatar homem-38.
set -uo pipefail
cd "$(dirname "$0")"
MODEL="openai/gpt-image-2/text-to-image"

# Molde comum: e o que casa com a gramatica visual do criativo original
# (nivel de olho, plano medio, sala clara, maos fora do quadro).
molde() {
cat <<EOF
A vertical 9:16 UGC-style video frame shot on an iPhone propped on a tripod across the room. MEDIUM SHOT - the subject's head occupies only the upper third of the frame, torso and lap visible, clear space above the head and on both sides. Camera at TRUE EYE LEVEL, perfectly level, NOT tilted.

SUBJECT: $1 Sitting relaxed on a sofa, leaning back slightly, looking directly into the lens. Expression is calm, serious and low-energy - the face of someone quietly telling you something you need to hear. Mouth relaxed and slightly parted mid-sentence, not smiling.

WARDROBE: $2

SKIN: Visible pores across the T-zone, faint expression lines, natural oil catching light on the forehead. Light shadow under the eyes. No filter, no foundation, no retouching.

FRAMING: Wide enough to show chest, shoulders and the top of the lap. Hands rest below the frame edge and are NOT visible.

CAMERA: Native phone lens, 26mm equivalent, mild barrel softness at the edges.

LIGHTING: BRIGHT and AIRY. Strong soft daylight from a large window camera-left filling the whole room. Overall exposure light and clean, not moody, not dark. Gentle natural falloff. Subtle ISO grain 400-600.

BACKGROUND: $3 Softly out of focus. Lived-in but tidy. Plenty of visible wall around the subject.
EOF
}

gerar() {
  local slug="$1" sujeito="$2" roupa="$3" fundo="$4"
  if [[ -s "base-${slug}.png" ]]; then echo "  = ${slug} ja existe"; return 0; fi
  echo "  -> ${slug}"
  molde "$sujeito" "$roupa" "$fundo" > "prompt-${slug}.txt"
  for t in 1 2 3; do
    wavespeed run "$MODEL" -i aspect_ratio="9:16" -i resolution="2k" \
      -i quality="high" -i output_format="png" \
      -p "$(cat "prompt-${slug}.txt")" \
      --download "base-${slug}.png" --json > "base-${slug}.json" 2>&1
    [[ -s "base-${slug}.png" ]] && { echo "     ok"; return 0; }
    echo "     tentativa $t falhou"; sleep 10
  done
  echo "  !! DESISTIU de ${slug}"; tail -3 "base-${slug}.json"; return 1
}

gerar m1-loira-29 \
  "A 29-year-old white woman with fair skin, light blue eyes, straight shoulder-length dirty-blonde hair tucked behind one ear, light freckles across the nose." \
  "soft oatmeal-coloured knit sweater, crew neck." \
  "A bright living room with an off-white wall, a small framed print, and a pale linen curtain at the edge of frame."

gerar m2-morena-45 \
  "A 45-year-old Latina woman with warm olive skin, dark brown eyes, straight dark hair to the collarbone with a few greys at the temple, visible smile lines." \
  "plain charcoal grey long-sleeve top." \
  "A bright kitchen-diner with pale cabinets far behind and a light wall, a mug on the counter."

gerar m3-negra-34 \
  "A 34-year-old Black woman with deep brown skin, dark brown eyes, short natural coily hair, high cheekbones, a small stud earring." \
  "muted terracotta crew-neck t-shirt." \
  "A bright home office with a white wall, the corner of a bookshelf, and a plant just out of frame edge."

gerar h1-jovem-27 \
  "A 27-year-old Brazilian man with light-tan skin, brown eyes, messy short dark hair, patchy light stubble along the jaw." \
  "faded olive-green crew-neck t-shirt." \
  "A bright bedroom-office with a plain white wall, a desk edge and a monitor corner far behind."

gerar h2-grisalho-52 \
  "A 52-year-old white man with weathered fair skin, grey-blue eyes, short salt-and-pepper hair receding slightly, a neat grey beard, deep expression lines." \
  "plain slate-blue button-down shirt, collar open, sleeves not visible." \
  "A bright living room with a pale wall, a framed photograph and a lamp far behind."

echo
ls -la base-*.png 2>/dev/null | awk '{printf "%-26s %6.1f MB\n", $9, $5/1048576}'
