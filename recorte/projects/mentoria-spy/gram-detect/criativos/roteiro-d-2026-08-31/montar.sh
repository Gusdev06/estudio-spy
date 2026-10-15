#!/bin/bash
# Monta roteiro-d-v1-45s.mp4 a partir dos clipes crus em clipes/.
#   TARJA_Y=<px>      topo da tarja (menor = mais acima; canvas 1920)
#   TICKER="..."      texto do ticker
#   PROGRAMA="..."    nome do programa
#   CTA="..."         texto do card final
set -e
cd "$(dirname "$0")"
FB="/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FK="/System/Library/Fonts/Supplemental/Arial Black.ttf"
TICKER="${TICKER:-WHY PHONE-TRACKING APPS ALMOST ALWAYS FAIL}"
PROGRAMA="${PROGRAMA:-THE SIGNAL}"
CTA="${CTA:-FIRST SEARCH IS FREE}"
STK1="${STK1:-EVERYONE FINDS OUT}"
STK2="${STK2:-THE PARTNER IS}"
STK3="${STK3:-ALWAYS LAST}"
STK_SZ="${STK_SZ:-60}"       # ~22 caracteres por linha no maximo
STK_BG="${STK_BG:-0xC8102E}" # fundo do sticker (mesmo crimson da tarja e do CTA)
STK_T="${STK_T:-3}"          # segundos que o sticker fica na tela
Y="${TARJA_Y:-1380}"; Y2=$((Y + 94)); YC=$((Y - 90))

TARJA="drawbox=x=0:y=${Y}:w=1080:h=94:color=0x0E1A2B:t=fill,\
drawbox=x=0:y=${Y2}:w=1080:h=58:color=0xF2F2F2:t=fill,\
drawbox=x=0:y=${Y}:w=12:h=152:color=0xC8102E:t=fill,\
drawtext=fontfile='$FK':text='${PROGRAMA}':fontcolor=white:fontsize=56:x=44:y=$((Y + 20)),\
drawtext=fontfile='$FB':text='${TICKER}':fontcolor=0x0E1A2B:fontsize=32:x=44:y=$((Y2 + 12))"

# card do CTA: barra crimson encostada no topo da tarja, entra em t>=2 no c5
CARD="drawbox=x=0:y=${YC}:w=1080:h=90:color=0xC8102E:t=fill:enable='gte(t,2)',\
drawtext=fontfile='$FK':text='${CTA}':fontcolor=white:fontsize=52:x=(w-tw)/2:y=$((YC + 18)):enable='gte(t,2)'"

# sticker hook: 2 linhas no topo, sai em STK_T segundos (só no c1)
STICKER="drawtext=fontfile='$FK':text='${STK1}':fontcolor=white:fontsize=${STK_SZ}:box=1:boxcolor=${STK_BG}:boxborderw=20:x=(w-tw)/2:y=200:enable='lt(t,${STK_T})',\
drawtext=fontfile='$FK':text='${STK2}':fontcolor=white:fontsize=${STK_SZ}:box=1:boxcolor=${STK_BG}:boxborderw=20:x=(w-tw)/2:y=292:enable='lt(t,${STK_T})',\
drawtext=fontfile='$FK':text='${STK3}':fontcolor=white:fontsize=${STK_SZ}:box=1:boxcolor=${STK_BG}:boxborderw=20:x=(w-tw)/2:y=384:enable='lt(t,${STK_T})'"

mkdir -p build; rm -f build/lista.txt

for c in c1 c2 c3 c5; do
  EXTRA=""; [ "$c" = "c1" ] && EXTRA=",$STICKER"; [ "$c" = "c5" ] && EXTRA=",$CARD"
  ffmpeg -v error -i clipes/$c.mp4 -vf "scale=1080:1920,setsar=1,${TARJA}${EXTRA}" \
    -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p \
    -c:a aac -b:a 192k -ar 48000 -r 30 build/$c-tarja.mp4 -y
done

# c4: dois inserts de footage real do funil sobre a fala dela (áudio segue por baixo)
#   A (2.0-4.0s)  "You enter the number"            -> digitando o número
#   B (6.2-9.6s)  "you're reading what was there"   -> mensagem recuperada do cache
ffmpeg -v error -i clipes/c4.mp4 -i insert/a-digita.mp4 -i insert/b-recuperado.mp4 \
  -filter_complex "[0:v]scale=1080:1920,setsar=1,fps=30[base];\
[1:v]setpts=PTS-STARTPTS+2/TB,fps=30,setsar=1[ia];\
[2:v]setpts=PTS-STARTPTS+6.2/TB,fps=30,setsar=1[ib];\
[base][ia]overlay=0:0:enable='between(t,2,4)'[o1];\
[o1][ib]overlay=0:0:enable='between(t,6.2,9.6)'[o2];\
[o2]${TARJA}[v]" \
  -map "[v]" -map 0:a -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 -r 30 build/c4-tarja.mp4 -y

for c in c1 c2 c3 c4 c5; do echo "file '$c-tarja.mp4'" >> build/lista.txt; done
ffmpeg -v error -f concat -safe 0 -i build/lista.txt -c copy roteiro-d-v1-45s.mp4 -y
echo "ok: roteiro-d-v1-45s.mp4 (tarja y=$Y · insert 33-35s · CTA 43-45s)"
