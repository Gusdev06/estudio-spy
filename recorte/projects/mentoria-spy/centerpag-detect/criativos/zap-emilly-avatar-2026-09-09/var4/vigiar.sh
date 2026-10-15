#!/bin/bash
# vigiar.sh — monta cada talking-head-vN.mp4 que cair em var4/clipes/ (tamanho estável por 20 s) e ainda não tiver peça. Uso: bash var4/vigiar.sh (de projects/mentoria-spy/)
cd "$(dirname "$0")/../../../.."; V=centerpag-detect/criativos/zap-emilly-avatar-2026-09-09/var4
for v in v3 v6 v7 v8; do c="$V/clipes/talking-head-$v.mp4"; [[ -f "$c" ]] || continue; ls "$V"/pecas/zap-emilly-avatar-$v-*.mp4 >/dev/null 2>&1 && continue
  s1=$(stat -f%z "$c"); sleep 20; s2=$(stat -f%z "$c"); [[ "$s1" == "$s2" && "$s1" -gt 1000000 ]] || { echo "$v ainda escrevendo"; continue; }
  ffprobe -v error -show_entries format=duration -of csv=p=0 "$c" >/dev/null 2>&1 || { echo "$v incompleto"; continue; }
  echo "== montando $v =="; SCRATCH="${SCRATCH:-/tmp}" python3 "$V/montar-var4.py" "$v"; done
