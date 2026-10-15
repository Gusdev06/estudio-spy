#!/bin/bash
# Refaz clipes do podcast que falharam (usa o req.json já escrito): bash refazer-blocos.sh p06:1 p06:2 p09:4 …
cd "$(dirname "$0")/../../.."; P=centerpag-detect/criativos/podcast-wpp-clone-avatares-2026-09-13
for x in "$@"; do v=${x%%:*}; b=${x##*:}; (wavespeed run pruna-ai/p-video/avatar --input-file $P/$v/clipes/bloco-${b}b.req.json --json --download $P/$v/clipes/bloco-${b}b.mp4 > $P/$v/clipes/bloco-${b}b.out.json 2> $P/$v/clipes/bloco-${b}b.log && echo "ok $v bloco $b" || { echo "FALHOU $v bloco $b"; tail -c 150 $P/$v/clipes/bloco-${b}b.log; echo; }) & done; wait
