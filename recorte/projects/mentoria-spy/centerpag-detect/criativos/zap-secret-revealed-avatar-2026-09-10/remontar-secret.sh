#!/bin/bash
# remontar-secret.sh — edição do Zap "secret revealed" por cima de um talking head novo, 1080x1920 30 fps. Custo zero.
#   LOTE:  bash remontar-secret.sh clipes/<talking-head>.mp4 [--th-x N --zoom F --th-y N]   → pecas/zap-secret-revealed-avatar.mp4
#   GERAL: bash remontar-secret.sh <talking-head.mp4> <saida.mp4> [opções de remontar-secret.py]
# Teste do molde: bash remontar-secret.sh centerpag-detect/anuncios/secret-revealed-934941213003855.mp4 conferencia/molde/teste-original.mp4
set -euo pipefail
D="$(cd "$(dirname "$0")" && pwd)"; cd "$D/../../.."
pos=(); opts=(); while [[ $# -gt 0 ]]; do case "$1" in --th-y|--th-x|--zoom|--off-head|--fonte|--tamanho|--y|--atraso) opts+=("$1" "$2"); shift 2;; --*) opts+=("$1"); shift;; *) pos+=("$1"); shift;; esac; done
res(){ if [[ "$1" == /* || -e "$1" || -d "$(dirname "$1")" ]]; then echo "$1"; else echo "$D/$1"; fi; }
if [[ ${#pos[@]} -eq 1 ]]; then mkdir -p "$D/pecas"; set -- "$(res "${pos[0]}")" "$D/pecas/zap-secret-revealed-avatar.mp4"; else set -- "$(res "${pos[0]}")" "$(res "${pos[1]}")"; fi
exec python3 "$D/remontar-secret.py" "$@" ${opts[@]+"${opts[@]}"}
