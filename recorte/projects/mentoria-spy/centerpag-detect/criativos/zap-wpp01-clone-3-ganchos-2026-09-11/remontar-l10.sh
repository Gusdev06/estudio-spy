#!/bin/bash
# remontar-l10.sh — molde L10 do wpp-01 (card alfa sobre plano único + matte de hook + karaokê amarelo + CTA em tela cheia).
# LOTE zap-wpp01-clone-3-ganchos-2026-09-11 (copiado do lote EX de 05/09; muda só o prefixo de saída e a gravação padrão).
#   LOTE:  bash remontar-l10.sh clipes/<talking-head>.mp4 [--off-head N]
#          → usa molde/blocos.tsv, molde/hooks.txt, molde/karaoke.tsv e grava pecas/zap-wpp01-{base,H1,H2,H3}.mp4
#   ⚠ neste lote cada gancho tem o próprio talking head (bloco 1 muda): rode no modo GERAL, um por variante:
#          bash remontar-l10.sh clipes/talking-head-H1-sem-pausas.mp4 molde/blocos-H1.tsv molde/hooks-H1.txt molde/karaoke-H1.tsv pecas/zap-wpp01-H1 --off-head N
#          (hooks-HN.txt tem só a linha HN; sai pecas/zap-wpp01-H1-base.mp4 + pecas/zap-wpp01-H1.mp4)
#   GERAL: bash remontar-l10.sh <talking-head.mp4> <blocos.tsv> <hooks.txt> <karaoke.tsv> <prefixo-saida> [--off-head N] [--rec gravacao.mp4] [--cta "L1|L2|L3|L4"]
# O talking head entra escalado a 1080 de largura; --off-head é o y do recorte 1080x1632 colado abaixo do matte (y 288).
# Karaokê: python3 karaoke-l10.py <whisper.json> <karaoke.tsv> [--blocos lista.txt]. Custo zero.
# Prova a custo zero (stand-in do lote EX, 11/09): bash remontar-l10.sh ../zap-ex-presente-hook-2026-09-05/clipes/talking-head-ex-omnihuman-sem-pausas.mp4 \
#   molde/blocos-standin-ex.tsv molde/hooks-standin-ex.txt molde/karaoke-standin-ex.tsv conferencia/standin-ex --off-head 240
set -euo pipefail
D="$(cd "$(dirname "$0")" && pwd)"; cd "$D/../../.."
pos=(); opts=(); while [[ $# -gt 0 ]]; do case "$1" in --off-head|--rec|--cta) opts+=("$1" "$2"); shift 2;; --*) opts+=("$1"); shift;; *) pos+=("$1"); shift;; esac; done
res(){ if [[ -e "$1" ]]; then echo "$1"; elif [[ -e "$D/$1" ]]; then echo "$D/$1"; else echo "$D/$1"; fi; }
if [[ ${#pos[@]} -eq 1 ]]; then mkdir -p "$D/pecas"; set -- "$(res "${pos[0]}")" "$D/molde/blocos.tsv" "$D/molde/hooks.txt" "$D/molde/karaoke.tsv" "$D/pecas/zap-wpp01"
else set -- "$(res "${pos[0]}")" "$(res "${pos[1]}")" "$(res "${pos[2]}")" "$(res "${pos[3]}")" "$(res "${pos[4]}")"; fi
exec python3 "$D/remontar-l10.py" "$@" "${opts[@]}"
