#!/usr/bin/env bash
# Roda os 5 avatares de ponta a ponta: clipes Kling -> montagem -> edicao clonada.
# Idempotente: pula o que ja existe. Serial de proposito (paralelo derruba chamadas).
set -uo pipefail
cd "$(dirname "$0")"

REF="../../escalados/instagram/10-sophia-jones-1541537987137161.mp4"
MODEL="kwaivgi/kling-v3.0-pro/image-to-video"
NEG="hands, fingers, gesturing, changing clothes, changing hairstyle, face morphing, identity drift, subtitles, text overlay, watermark, studio lighting, camera zoom, cut to another shot"
CFG=0.45
TOPO=279; CORTE_REF=8.66; CORTE=8.042; ESCALA=0.70

L1="There's one detail on Instagram that gives almost everyone away. The problem is, hardly anyone knows where to look."
L2="You don't need to guess, or argue, or secretly check someone's phone. Because when people try to hide something, they usually leave small traces behind without realizing it."
L3="That's why so many people uncover messages, contacts, and suspicious behavior, even when the other person thinks they deleted everything. You just need to know where to look. Access is right below, while this tool is still available."

# Espera a rede voltar. Queda de internet nao se resolve em 3 tentativas de
# 15s -- se o retry gasta as chances durante o apagao, o lote morre por um
# problema que ia passar sozinho. Aqui a gente PAUSA ate voltar.
esperar_rede() {
  local t=0 espera=10
  while ! curl -s -o /dev/null --max-time 10 https://api.wavespeed.ai/ 2>/dev/null; do
    [[ $t -eq 0 ]] && echo "    [rede caiu — pausando ate voltar]"
    sleep $espera
    t=$((t + espera)); espera=$(( espera < 60 ? espera * 2 : 60 ))
    if [[ $t -gt 1800 ]]; then echo "    [30min sem rede, desistindo]"; return 1; fi
  done
  [[ $t -gt 0 ]] && echo "    [rede voltou depois de ${t}s]"
  return 0
}

gerar() {
  local saida="$1" img="$2" dur="$3" prompt="$4"
  [[ -s "$saida" ]] && { echo "    = $(basename $saida) ja existe"; return 0; }
  local t pid url
  for t in 1 2 3 4 5; do
    esperar_rede || return 1
    echo "    -> $(basename $saida) (${dur}s) tentativa $t"
    wavespeed run "$MODEL" -i image="$img" -i duration="$dur" -i sound=true \
      -i cfg_scale="$CFG" -i prompt="$prompt" -i negative_prompt="$NEG" \
      --download "$saida" --json > "${saida%.mp4}.json" 2>&1
    [[ -s "$saida" ]] && { echo "       ok"; return 0; }
    pid=$(jq -r '.prediction_id // empty' "${saida%.mp4}.json" 2>/dev/null)
    if [[ -n "$pid" ]]; then
      echo "       download falhou; recuperando $pid"
      url=$(wavespeed show "$pid" --json 2>/dev/null | jq -r '.outputs[0] // empty')
      [[ -n "$url" ]] && curl -sL --fail -o "$saida" "$url" && { echo "       ok (recuperado)"; return 0; }
    fi
    sleep 15
  done
  echo "    !! DESISTIU de $saida"; return 1
}

prox_frame() {
  # Devolve URL do ultimo frame. Com retry: um upload falho aqui faria o clipe
  # seguinte nascer de uma URL invalida e quebrar a cadeia inteira.
  local c="$1" j="${1%.mp4}-last.jpg" u t
  ffmpeg -y -loglevel error -sseof -0.5 -i "$c" -vframes 1 -q:v 2 "$j"
  for t in 1 2 3 4 5 6; do
    esperar_rede || return 1
    u=$(wavespeed upload "$j" --json 2>/dev/null | jq -r '.url // empty')
    [[ "$u" == https://* ]] && { echo "$u"; return 0; }
    sleep 20
  done
  echo ""; return 1
}

avatar() {
  local slug="$1" nome="$2" tom="$3"
  echo "=========== $slug ($nome) ==========="
  mkdir -p "$slug/clipes"

  # Validar ANTES de cachear: gravar "null" no cache envenena todo retry
  # seguinte, e o erro passa a ser permanente em vez de transitorio.
  local cache="$slug/.base-url" base="" tu
  if [[ -s "$cache" ]] && [[ "$(cat "$cache")" == https://* ]]; then
    base=$(cat "$cache")
  else
    for tu in 1 2 3 4 5 6; do
      esperar_rede || return 1
      base=$(wavespeed upload "base-${slug}.png" --json 2>/dev/null | jq -r '.url // empty')
      [[ "$base" == https://* ]] && { echo "$base" > "$cache"; break; }
      echo "  upload da base falhou (tentativa $tu), aguardando"
      base=""; sleep 20
    done
  fi
  [[ "$base" == https://* ]] || { echo "  !! upload da base falhou em definitivo"; return 1; }

  local P1 P2 P3
  P1="The person leans forward very slightly and speaks directly into the lens.
[${nome}, ${tom}]: \"${L1}\"
Then settles back and holds the look. Camera is locked off. Hands stay out of frame."
  P2="The person tilts their head slightly and continues.
[${nome}, ${tom}]: \"${L2}\"
Then straightens and blinks once. Camera is locked off. Hands stay out of frame."
  P3="The person keeps their eyes on the lens and speaks steadily.
[${nome}, ${tom}]: \"${L3}\"
Then gives a small nod and holds still. Camera is locked off. Hands stay out of frame."

  gerar "$slug/clipes/b-01.mp4" "$base" 8 "$P1" || return 1
  local f2; f2=$(prox_frame "$slug/clipes/b-01.mp4")
  [[ "$f2" == https://* ]] || { echo "  !! frame 1->2 falhou"; return 1; }
  gerar "$slug/clipes/b-02.mp4" "$f2" 11 "$P2" || return 1
  local f3; f3=$(prox_frame "$slug/clipes/b-02.mp4")
  [[ "$f3" == https://* ]] || { echo "  !! frame 2->3 falhou"; return 1; }
  gerar "$slug/clipes/b-03.mp4" "$f3" 15 "$P3" || return 1

  echo "  montando..."
  bash ~/.claude/skills/trocar-avatar/scripts/montar.sh "$slug" 2>&1 | grep -E "versao-B|ATENCAO"

  echo "  clonando edicao..."
  python3 ~/.claude/skills/clonar-edicao/scripts/montar_composto.py \
    --ref "$REF" --avatar "$slug/versao-B-voz-kling.mp4" \
    --topo $TOPO --corte-ref $CORTE_REF --corte $CORTE --escala $ESCALA \
    -o "final-${slug}.mp4" 2>&1 | grep -E "^ok|AVISO|ERRO"
  echo
}

avatar m1-loira-29    "Hannah"  "calm low confiding voice"
avatar m2-morena-45   "Claudia" "calm low serious voice, slightly husky"
avatar m3-negra-34    "Denise"  "calm low confiding voice, measured"
avatar h1-jovem-27    "Rafa"    "calm low serious voice"
avatar h2-grisalho-52 "Paulo"   "calm low serious voice, deep"

echo "=========== LOTE FINALIZADO ==========="
ls -la final-*.mp4 2>/dev/null | awk '{printf "%-34s %6.1f MB\n", $9, $5/1048576}'
