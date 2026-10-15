#!/bin/bash
# Lipsync das variações: bash gerar-clipes.sh secret s01 s02 …  |  bash gerar-clipes.sh luiza l01 …   (upload da imagem + Pruna com o áudio do original)
set -e; cd "$(dirname "$0")/../../.."; V=centerpag-detect/criativos/variacoes-30-2026-09-19; L=$1; shift
for id in "$@"; do (
  U=$(wavespeed upload $V/$L/base/$id.png --json 2>/dev/null | python3 -c "import json,sys;print(json.load(sys.stdin)['url'])")
  python3 -c "
import json,sys; m=json.load(open('$V/modelos-req.json'))['$L']; m['image']=sys.argv[1]; m['seed']=int(__import__('os').environ.get('SEED','78')); json.dump(m,open('$V/$L/clipes/$id.req.json','w'))" "$U"
  wavespeed run pruna-ai/p-video/avatar --input-file $V/$L/clipes/$id.req.json --json --download $V/$L/clipes/$id.mp4 > $V/$L/clipes/$id.out.json 2> $V/$L/clipes/$id.log && echo "ok $L $id" || { echo "FALHOU $L $id"; tail -c 200 $V/$L/clipes/$id.log; echo; }
) & done; wait
