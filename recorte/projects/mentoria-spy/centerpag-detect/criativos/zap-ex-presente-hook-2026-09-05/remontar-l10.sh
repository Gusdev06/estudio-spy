#!/bin/bash
# remontar-l10.sh — molde L10 do wpp-01 (card alfa sobre plano único + matte de hook + karaokê amarelo + CTA em tela cheia).
#   LOTE:  bash remontar-l10.sh clipes/<talking-head>.mp4 [--off-head N]
#          → usa molde/blocos.tsv, molde/hooks.txt, molde/karaoke.tsv e grava pecas/zap-ex-presente-{base,A,B,C}.mp4
#   GERAL: bash remontar-l10.sh <talking-head.mp4> <blocos.tsv> <hooks.txt> <karaoke.tsv> <prefixo-saida> [--off-head N] [--rec gravacao.mp4] [--cta "L1|L2|L3|L4"]
# O talking head entra escalado a 1080 de largura; --off-head é o y do recorte 1080x1632 colado abaixo do matte (y 288).
# Karaokê: python3 karaoke-l10.py <whisper.json> <karaoke.tsv> [--blocos lista.txt]. Custo zero.
# Teste do molde: bash remontar-l10.sh centerpag-detect/escalados/whatsapp/01-esther-vicman-1762552938111855.mp4 \
#   molde/blocos-teste-wpp01.tsv molde/hooks-teste.txt molde/karaoke-teste-wpp01.tsv conferencia/molde/teste-wpp01 --off-head 288
set -euo pipefail
D="$(cd "$(dirname "$0")" && pwd)"; cd "$D/../../.."
pos=(); opts=(); while [[ $# -gt 0 ]]; do case "$1" in --off-head|--rec|--cta) opts+=("$1" "$2"); shift 2;; --*) opts+=("$1"); shift;; *) pos+=("$1"); shift;; esac; done
res(){ if [[ -e "$1" ]]; then echo "$1"; elif [[ -e "$D/$1" ]]; then echo "$D/$1"; else echo "$D/$1"; fi; }
if [[ ${#pos[@]} -eq 1 ]]; then mkdir -p "$D/pecas"; set -- "$(res "${pos[0]}")" "$D/molde/blocos.tsv" "$D/molde/hooks.txt" "$D/molde/karaoke.tsv" "$D/pecas/zap-ex-presente"
else set -- "$(res "${pos[0]}")" "$(res "${pos[1]}")" "$(res "${pos[2]}")" "$(res "${pos[3]}")" "$(res "${pos[4]}")"; fi
exec python3 "$D/remontar-l10.py" "$@" "${opts[@]}"
