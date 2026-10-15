#!/bin/bash
# remontar-emilly.sh — edição do Zap #3 (Emilly Bredoff) por cima de um talking head novo, 1080x1920 30 fps.
#   LOTE:  bash remontar-emilly.sh clipes/<talking-head>.mp4            → pecas/zap-emilly-avatar.mp4
#   GERAL: bash remontar-emilly.sh <talking-head.mp4> <saida.mp4> [--th-y N] [--th-x N] [--zoom F] [--off-head N] [--karaoke] [--cta "L1|L2"]
# Teste do molde (o próprio original como entrada): bash remontar-emilly.sh centerpag-detect/anuncios/emilly-bredoff-939122432559594.mp4 conferencia/molde/teste-original.mp4 --th-y 185
#   (--th-y 185 põe a janela de conteúdo do original, y 109 ×3 = 327, exatamente onde o molde põe o card, y 512)
set -euo pipefail
D="$(cd "$(dirname "$0")" && pwd)"; cd "$D/../../.."
pos=(); opts=(); while [[ $# -gt 0 ]]; do case "$1" in --th-y|--th-x|--zoom|--off-head|--cta) opts+=("$1" "$2"); shift 2;; --*) opts+=("$1"); shift;; *) pos+=("$1"); shift;; esac; done
res(){ if [[ "$1" == /* || -e "$1" || -d "$(dirname "$1")" ]]; then echo "$1"; else echo "$D/$1"; fi; }
if [[ ${#pos[@]} -eq 1 ]]; then mkdir -p "$D/pecas"; set -- "$(res "${pos[0]}")" "$D/pecas/zap-emilly-avatar.mp4"; else set -- "$(res "${pos[0]}")" "$(res "${pos[1]}")"; fi
exec python3 "$D/remontar-emilly.py" "$@" ${opts[@]+"${opts[@]}"}
