#!/usr/bin/env bash
# Gera as duas cadeias de clipes. Idempotente: pula o que ja existe.
# Serial (nao paralelo) -- rodar as duas cadeias juntas derrubou chamadas
# com "fetch failed" na primeira tentativa.
set -uo pipefail
cd "$(dirname "$0")"

MODEL="kwaivgi/kling-v3.0-pro/image-to-video"
NEG="hands, fingers, gesturing, changing clothes, changing hairstyle, face morphing, identity drift, subtitles, text overlay, watermark, studio lighting, camera zoom, cut to another shot"
CFG=0.45

BASE_CACHE=".base-url"
if [[ -s "$BASE_CACHE" ]]; then
  BASE=$(cat "$BASE_CACHE")
else
  BASE=$(wavespeed upload avatar-base-v2.png --json | jq -r .url)
  [[ -n "$BASE" && "$BASE" != "null" ]] || { echo "FALHA no upload da base"; exit 1; }
  echo "$BASE" > "$BASE_CACHE"
fi
echo "[base] $BASE"

# gerar <saida> <img_url> <dur> <sound> <prompt>
gerar() {
  local saida="$1" img="$2" dur="$3" sound="$4" prompt="$5"
  if [[ -s "$saida" ]]; then
    echo "  = $saida ja existe, pulando"
    return 0
  fi
  local tent
  for tent in 1 2 3; do
    echo "  -> $saida (${dur}s, sound=$sound) tentativa $tent"
    wavespeed run "$MODEL" \
      -i image="$img" -i duration="$dur" -i sound="$sound" -i cfg_scale="$CFG" \
      -i prompt="$prompt" -i negative_prompt="$NEG" \
      --download "$saida" --json > "${saida%.mp4}.json" 2>&1
    if [[ -s "$saida" ]]; then
      echo "  ok $saida ($(ffprobe -v error -show_entries format=duration -of csv=p=0 "$saida")s)"
      return 0
    fi
    # A geracao pode ter completado e so o download falhado -- nesse caso o
    # job ja foi pago. Recupera pela prediction_id antes de re-submeter.
    local pid
    pid=$(jq -r '.prediction_id // empty' "${saida%.mp4}.json" 2>/dev/null)
    if [[ -n "$pid" ]]; then
      echo "     download falhou; recuperando prediction $pid"
      local url
      url=$(wavespeed show "$pid" --json 2>/dev/null | jq -r '.outputs[0] // empty')
      if [[ -n "$url" ]] && curl -sL --fail -o "$saida" "$url"; then
        echo "  ok $saida (recuperado)"
        return 0
      fi
    fi
    echo "     falhou, aguardando antes de repetir"
    sleep 15
  done
  echo "  !! DESISTIU de $saida"; tail -5 "${saida%.mp4}.json"; return 1
}

proximo_frame() {
  local clipe="$1" jpg="${1%.mp4}-last.jpg"
  ffmpeg -y -loglevel error -sseof -0.5 -i "$clipe" -vframes 1 -q:v 2 "$jpg"
  wavespeed upload "$jpg" --json | jq -r .url
}

A1="The man looks directly into the lens and speaks continuously, calm and serious, low energy, like someone telling a friend something difficult. He leans forward very slightly at the start, then settles back into the sofa. He blinks naturally twice. Camera is locked off. Hands stay out of frame."
A2="The man keeps speaking directly into the lens, steady and unhurried. He tilts his head slightly to his left to make a point, then straightens. One slow blink. Small shoulder shift. Camera is locked off. Hands stay out of frame."
A3="The man continues speaking directly into the lens, calm and deliberate, then slows down toward the end. He gives a small nod, holds a steady look into the lens and stops speaking, lips closing. Camera is locked off. Hands stay out of frame."

B1="The man leans forward very slightly and speaks directly into the lens.
[Marcos, calm low serious voice]: \"There's one detail on Instagram that gives almost everyone away. The problem is, hardly anyone knows where to look.\"
He settles back into the sofa and holds the look. Camera is locked off. Hands stay out of frame."
B2="The man tilts his head slightly to his left and continues.
[Marcos, calm low serious voice]: \"You don't need to guess, or argue, or secretly check someone's phone. Because when people try to hide something, they usually leave small traces behind without realizing it.\"
He straightens and blinks once. Camera is locked off. Hands stay out of frame."
B3="The man keeps his eyes on the lens and speaks steadily.
[Marcos, calm low serious voice]: \"That's why so many people uncover messages, contacts, and suspicious behavior, even when the other person thinks they deleted everything. You just need to know where to look. Access is right below, while this tool is still available.\"
He gives a small nod and holds still. Camera is locked off. Hands stay out of frame."

cadeia() {
  local pref="$1" sound="$2" p1="$3" p2="$4" p3="$5"
  echo "[$pref] iniciando"
  gerar "clipes/${pref}-01.mp4" "$BASE" 8  "$sound" "$p1" || return 1
  local f2; f2=$(proximo_frame "clipes/${pref}-01.mp4")
  gerar "clipes/${pref}-02.mp4" "$f2"   11 "$sound" "$p2" || return 1
  local f3; f3=$(proximo_frame "clipes/${pref}-02.mp4")
  gerar "clipes/${pref}-03.mp4" "$f3"   15 "$sound" "$p3" || return 1
  echo "[$pref] cadeia completa"
}

cadeia a false "$A1" "$A2" "$A3"; RA=$?
cadeia b true  "$B1" "$B2" "$B3"; RB=$?
echo "cadeia A: exit $RA | cadeia B: exit $RB"
exit $(( RA + RB ))
