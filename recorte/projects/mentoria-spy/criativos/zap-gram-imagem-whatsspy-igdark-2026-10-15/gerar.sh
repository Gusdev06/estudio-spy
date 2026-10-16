#!/bin/bash
# Gera as 10 variações (gpt-image-2/edit, quality high, 1k, 9:16) em paralelo. ~US$ 0,22 cada.
cd "$(dirname "$0")"
for f in out/*.input.json; do k=$(basename "$f" .input.json)
  [ -f "out/$k.png" ] && continue
  ( wavespeed run openai/gpt-image-2/edit --input-file "$f" --download "out/$k.{ext}" --json > "out/$k.out.json" 2> "out/$k.err" ) &
done; wait
echo "PNGs: $(ls out/*.png 2>/dev/null | wc -l)/$(ls out/*.input.json | wc -l)"; wavespeed balance | grep Balance
