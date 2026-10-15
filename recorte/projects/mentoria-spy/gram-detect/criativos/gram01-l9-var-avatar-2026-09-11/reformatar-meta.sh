#!/usr/bin/env bash
# Reformata uma peça L9 (1170×2532, ~1:2,16) pros formatos que a Meta aceita.
#   bash reformatar-meta.sh <peca.mp4> <pasta-saida>
# Saídas: <nome>-9x16.mp4 (1080×1920, Reels/Stories) e <nome>-4x5.mp4 (1080×1350, Feed/Explorar).
# Regiões do molde L9 (README): head y0–1212 · faixa y1212–1498 · painel y1498–2532 · frames ≥940 = cauda em quadro cheio.
# 9:16 = 1170×2080 antes do scale: head 1062 (tira 40 em cima, 110 embaixo) + faixa 286 + painel 732 (tira 302 do teclado).
#        cauda: crop 2080 a partir de y150 (olhos ~44 % ficam em ~48 %).
# 4:5  = 1170×1462: head 1176 (tira 36 em cima) + faixa 286. Sem painel — o funil/b-roll não cabe em 4:5.
#        cauda: crop 1462 a partir de y456 (olhos em ~45 %).
# Áudio copiado (VO bit-idêntica). Encode = controle: x264 crf 19 preset medium yuv420p 30 fps.
set -euo pipefail
IN="${1:?peca.mp4}"; OUT="${2:?pasta-saida}"; mkdir -p "$OUT"
base="$(basename "${IN%.mp4}")"
dim="$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$IN")"
[ "$dim" = "1170,2532" ] || { echo "não é 1170x2532: $dim" >&2; exit 3; }
ENC=(-c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -r 30 -c:a copy -movflags +faststart)

ffmpeg -hide_banner -loglevel error -y -i "$IN" -filter_complex "\
[0:v]trim=end_frame=940,setpts=PTS-STARTPTS,split=3[h][f][p];\
[h]crop=1170:1062:0:40[hc];[f]crop=1170:286:0:1212[fc];[p]crop=1170:732:0:1498[pc];\
[hc][fc][pc]vstack=3[body];\
[0:v]trim=start_frame=940,setpts=PTS-STARTPTS,crop=1170:2080:0:150[tail];\
[body][tail]concat=n=2:v=1:a=0,scale=1080:1920:flags=lanczos[v]" \
  -map "[v]" -map 0:a "${ENC[@]}" "$OUT/$base-9x16.mp4"

ffmpeg -hide_banner -loglevel error -y -i "$IN" -filter_complex "\
[0:v]trim=end_frame=940,setpts=PTS-STARTPTS,split=2[h][f];\
[h]crop=1170:1176:0:36[hc];[f]crop=1170:286:0:1212[fc];\
[hc][fc]vstack=2[body];\
[0:v]trim=start_frame=940,setpts=PTS-STARTPTS,crop=1170:1462:0:456[tail];\
[body][tail]concat=n=2:v=1:a=0,scale=1080:1350:flags=lanczos[v]" \
  -map "[v]" -map 0:a "${ENC[@]}" "$OUT/$base-4x5.mp4"
echo "ok: $OUT/$base-{9x16,4x5}.mp4"
