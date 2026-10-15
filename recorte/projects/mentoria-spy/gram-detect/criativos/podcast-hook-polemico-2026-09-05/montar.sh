#!/bin/bash
# Wrapper: bash montar.sh [saida.mp4]  →  python3 montar.py (timeline com pausas removidas + karaokê + caixa + setas). Custo zero.
cd "$(dirname "$0")/../../.." && exec python3 gram-detect/criativos/podcast-hook-polemico-2026-09-05/montar.py "$@"
