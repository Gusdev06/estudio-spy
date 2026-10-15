#!/bin/bash
# uso: run_sheet.sh B01  (roda gpt-image-2/edit com _runs/shot-v2-B01.json -> shot-sheets-v2/B01.png)
cd "$(dirname "$0")/.."
k=$1
wavespeed run openai/gpt-image-2/edit --input-file _runs/shot-v2-$k.json --json --download shot-sheets-v2/$k.png > _runs/shot-v2-$k.out.json 2> _runs/shot-v2-$k.err
echo "$k exit=$? $(python3 -c "from PIL import Image;print(Image.open('shot-sheets-v2/$k.png').size)" 2>&1)"
