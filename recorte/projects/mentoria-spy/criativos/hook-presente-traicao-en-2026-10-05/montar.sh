#!/bin/bash
# hook EN (44 s) + criativo, normalizado em 1080x1920/30fps, áudio -14 LUFS por segmento
set -e
cd "$(dirname "$0")/../.."
L=criativos/hook-presente-traicao-en-2026-10-05; H=$L/hook-presente-traicao-EN.mp4
V="scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black,setsar=1,fps=30,format=yuv420p"
A="aresample=44100,aformat=sample_fmts=fltp:channel_layouts=stereo,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100,aformat=sample_fmts=fltp:channel_layouts=stereo"
while IFS='|' read -r id src; do
  out="$L/pecas/hookEN-$id.mp4"
  ffmpeg -hide_banner -loglevel error -y -i "$H" -i "CRIATIVOS-PRONTOS/$src" \
    -filter_complex "[0:v]$V[v0];[1:v]$V[v1];[0:a]$A[a0];[1:a]$A[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]" \
    -map "[v]" -map "[a]" -c:v libx264 -crf 19 -preset medium -c:a aac -b:a 160k -movflags +faststart "$out" </dev/null
  echo "$id $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$out")"
done <<'E'
CP77-secret-revealed-filipino|77-ZAP-secret-revealed-filipino-jovem-moletom.mp4
CP108-podcast-ruiva-x-negra-afro|108-ZAP-podcast-wpp-copy-nova-branca-ruiva-x-negra-afro.mp4
CP121-ela-disse-que-e-amiga|121-ZAP-secret-hook-ela-disse-que-e-amiga.mp4
var5-flora|variacoes-2026-09-25/flora-959352790554428-2026-09-25/var5-flora-959352790554428.mp4
var6-lauren-walker|variacoes-2026-09-25/lauren-walker-2091863388082075-2026-09-25/var6-lauren-walker-2091863388082075.mp4
E
