#!/bin/bash
# Card de CTA nos ultimos segundos, no desenho do original (CR05-V1):
# amarelo caixa alta, contorno preto, 4 linhas + 3 setas descendo.
set -e; cd "$(dirname "$0")"
IN="${IN:-criativo-FINAL.mp4}"
OUT="${OUT:-criativo-FINAL-cta.mp4}"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
CTA_LEN="${CTA_LEN:-4.2}"
T0=$(python3 -c "print(round($DUR-$CTA_LEN,2))")
FK="/System/Library/Fonts/Supplemental/Arial Black.ttf"
L1="${L1:-CLICK THE LINK}"; L2="${L2:-BELOW AND}"; L3="${L3:-SEE THE TRUTH}"; L4="${L4:-NOW}"
Y1=300; SP=118; SZ=86
TXT=""
i=0
for L in "$L1" "$L2" "$L3" "$L4"; do
  Y=$((Y1 + i*SP))
  TXT="${TXT}drawtext=fontfile='$FK':text='${L}':fontcolor=0xF2E205:fontsize=${SZ}:borderw=11:bordercolor=black:x=(w-tw)/2:y=${Y}:enable='gte(t,${T0})',"
  i=$((i+1))
done

ffmpeg -v error -i "$IN" -loop 1 -i cta-setas.png -filter_complex "\
[0:v]split[a][b];\
[b]boxblur=14:2,eq=brightness=-0.22[blur];\
[a][blur]overlay=0:0:enable='gte(t,${T0})'[bg];\
[1:v]scale=520:-1,format=rgba,colorchannelmixer=aa=1.0[ch];\
[bg][ch]overlay=x=(W-w)/2:y='820+40*sin(2*PI*(t-${T0}))':enable='gte(t,${T0})'[ov];\
[ov]${TXT}format=yuv420p[v]" \
 -map "[v]" -map 0:a -c:v libx264 -preset medium -crf 19 -c:a copy -shortest "$OUT" -y
echo "ok: $OUT  (CTA a partir de ${T0}s)"
