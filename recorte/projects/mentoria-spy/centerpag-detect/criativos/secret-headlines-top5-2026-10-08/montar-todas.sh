#!/bin/bash
# Monta as peças UMA POR VEZ, em série (karaokê + filtergraph estouram a RAM em paralelo). Uso (de projects/mentoria-spy/): bash montar-todas.sh [nº…]
cd "$(dirname "$0")/../../.."; N=centerpag-detect/criativos/secret-headlines-top5-2026-10-08
ids=("$@"); [ ${#ids[@]} -eq 0 ] && ids=($(seq 174 188))
for k in "${ids[@]}"; do
  read mae slug < <(python3 -c "import json;v=json.load(open('$N/headlines.json'))['$k'];print(v['mae'],v['slug'])")
  python3 $N/montar.py $mae $N/pecas/$k-ZAP-secret-$slug.mp4 --selo $N/molde/selo-$k.png || echo "FALHOU $k"
done
