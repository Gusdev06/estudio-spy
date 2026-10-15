#!/usr/bin/env bash
# Remove pausas de cada clipe, remonta e refaz a edicao com o novo ponto de corte.
# Nao gera nada novo no Kling -- tudo local, custo zero.
set -uo pipefail
cd "$(dirname "$0")"

REF="../../escalados/instagram/10-sophia-jones-1541537987137161.mp4"
RP=~/.claude/skills/clonar-edicao/scripts/remover_pausas.py
MC=~/.claude/skills/clonar-edicao/scripts/montar_composto.py
TOPO=279; CORTE_REF=8.66; ESCALA=0.70

for slug in m1-loira-29 m2-morena-45 m3-negra-34 h1-jovem-27 h2-grisalho-52; do
  echo "=========== $slug ==========="
  mkdir -p "$slug/fluido/clipes"

  for n in 01 02 03; do
    src="$slug/clipes/b-${n}.mp4"; dst="$slug/fluido/clipes/b-${n}.mp4"
    [[ -s "$dst" ]] && { echo "  = b-${n} ja fluido"; continue; }
    python3 "$RP" "$src" "$dst" 2>&1 | sed 's/^/  /'
  done

  # O ponto de corte da montagem e a nova duracao do clipe 1: e ali que a fala
  # muda de "where to look" para "You don't need to guess", que e onde o
  # original corta. Sem recalcular, o split screen cairia no lugar errado.
  novo_corte=$(ffprobe -v error -show_entries format=duration -of csv=p=0 \
               "$slug/fluido/clipes/b-01.mp4")
  echo "  novo ponto de corte: ${novo_corte}s"

  bash ~/.claude/skills/trocar-avatar/scripts/montar.sh "$slug/fluido" 2>&1 | grep -E "versao-B|ATENCAO"

  python3 "$MC" --ref "$REF" --avatar "$slug/fluido/versao-B-voz-kling.mp4" \
    --topo $TOPO --corte-ref $CORTE_REF --corte "$novo_corte" --escala $ESCALA \
    -o "fluido-${slug}.mp4" 2>&1 | grep -E "^ok|AVISO|ERRO"
  echo
done

echo "=========== COMPARATIVO ==========="
for slug in m1-loira-29 m2-morena-45 m3-negra-34 h1-jovem-27 h2-grisalho-52; do
  a=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "final-${slug}.mp4" 2>/dev/null)
  b=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "fluido-${slug}.mp4" 2>/dev/null)
  printf "%-18s %5.1fs -> %5.1fs\n" "$slug" "${a:-0}" "${b:-0}"
done
