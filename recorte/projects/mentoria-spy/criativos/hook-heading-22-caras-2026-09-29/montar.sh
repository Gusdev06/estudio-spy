#!/bin/bash
# Cola o hook da 50 (0–6,4 s: reação + HEADING "22 different guys", original AD02-H2) na frente de cada alvo.
# Hook reescalado pra resolução do alvo e com ganho casado à loudness integrada do alvo (EBU R128).
set -e
P=../../CRIATIVOS-PRONTOS
HOOK=$P/50-GRAM-ad02-h2-avatar-branco-barba.mp4
HOOK_I=-18.9
lufs(){ ffmpeg -nostdin -hide_banner -nostats -i "$1" -af ebur128 -f null - 2>&1 | grep -E "^ +I:" | tail -1 | awk '{print $2}'; }
while IFS='|' read -r src out; do
  [ -z "$src" ] && continue
  IFS=x read W H < <(ffprobe -v error -select_streams v -show_entries stream=width,height -of csv=p=0:s=x "$P/$src")
  TI=$(lufs "$P/$src"); G=$(python3 -c "print(round($TI-($HOOK_I),2))")
  ffmpeg -nostdin -v error -y -t 6.4 -i "$HOOK" -i "$P/$src" -filter_complex \
   "[0:v]scale=$W:$H:flags=lanczos,setsar=1,fps=30,format=yuv420p[hv];[0:a]volume=${G}dB,aresample=48000,aformat=channel_layouts=stereo[ha];\
    [1:v]scale=$W:$H,setsar=1,fps=30,format=yuv420p[tv];[1:a]aresample=48000,aformat=channel_layouts=stereo[ta];\
    [hv][ha][tv][ta]concat=n=2:v=1:a=1[v][a]" \
   -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k -movflags +faststart "pecas/$out"
  echo "$out  alvo ${W}x${H}  I=$TI  ganho hook=${G}dB"
done <<LIST
121-ZAP-secret-hook-ela-disse-que-e-amiga.mp4|149-ZAP-hook22-secret-ela-disse-que-e-amiga.mp4
04-ZAP-podcast-faithful-man-sem-musica.mp4|150-ZAP-hook22-podcast-faithful-man.mp4
headlines-2026-09-27/flora-959352790554428-var5/var5-flora-h1-traicao.mp4|151-ZAP-hook22-flora-h1-traicao.mp4
headlines-2026-09-27/flora-959352790554428-var5/var5-flora-h2-apagou.mp4|152-ZAP-hook22-flora-h2-apagou.mp4
headlines-2026-09-27/flora-959352790554428-var5/var5-flora-h3-escondem.mp4|153-ZAP-hook22-flora-h3-escondem.mp4
headlines-2026-09-27/flora-959352790554428-var5/var5-flora-h4-nada.mp4|154-ZAP-hook22-flora-h4-nada.mp4
headlines-2026-09-27/flora-959352790554428-var5/var5-flora-h5-sem-tocar.mp4|155-ZAP-hook22-flora-h5-sem-tocar.mp4
LIST
