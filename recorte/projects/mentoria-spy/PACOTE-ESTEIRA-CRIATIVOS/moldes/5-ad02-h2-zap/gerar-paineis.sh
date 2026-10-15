#!/bin/bash
# Painéis do funil do Spy Zap, recortados da GRAVAÇÃO REAL do go.zappdetect.com (EDIÇÃO 3/…/ScreenRecording_08-13-2026 19-56-53_1.MP4,
# 1170x2532 60 fps) — a mesma fonte do painel da peça 06. Recorte justo, sem barra do Safari, número de telefone desfocado.
# Durações vêm de molde/timeline.json. Uso (de projects/mentoria-spy/): bash .../gerar-paineis.sh
set -e; N=centerpag-detect/criativos/ad02-h2-zap-2026-09-17; R="EDIÇÃO 3/EDIÇAO ANIMADA/ScreenRecording_08-13-2026 19-56-53_1.MP4"; O=$N/assets/paineis
read CARD A B1 B2 < <(python3 -c "
import json;T=json.load(open('$N/molde/timeline.json'));b=T['painelB'][1]-T['painelB'][0];print(T['card'][1]-T['card'][0],T['painelA'][1]-T['painelA'][0],120,b-120)")
# desfoque de uma região (coordenadas da gravação): split, crop, boxblur, overlay
borra(){ echo "split[o][p];[p]crop=$3:$4:$1:$2,gblur=sigma=14:steps=2[b];[o][b]overlay=$1:$2"; }
# card "Accessing cloud backup / Locating backup files…" + barra (rec 23,6 s), 1110x355 → 788 de largura
ffmpeg -hide_banner -v error -y -ss 23.6 -i "$R" -vf "fps=30,crop=1110:355:30:1215,scale=788:-2:flags=lanczos" -frames:v $CARD -an -c:v libx264 -crf 12 -pix_fmt yuv420p $O/card-backup.mp4
# painel A: "Restoring deleted data" + mapa TRACKING (rec 116,0 s); número do perfil e campo do número desfocados
ffmpeg -hide_banner -v error -y -ss 116.0 -i "$R" -vf "fps=30,$(borra 590 330 420 90),$(borra 100 700 460 110),crop=1110:1965:30:300,scale=692:1224:flags=lanczos" -frames:v $A -an -c:v libx264 -crf 12 -pix_fmt yuv420p $O/painel-A-mapa.mp4
# painel B1: lista de chats "257 deleted messages recovered" (frame congelado em 182,6 s); número no botão desfocado
ffmpeg -hide_banner -v error -y -ss 182.6 -i "$R" -frames:v 1 -vf "$(borra 380 1995 420 70),crop=1170:2070:0:240,scale=692:1224:flags=lanczos" $O/painel-B1-chats.png
ffmpeg -hide_banner -v error -y -loop 1 -framerate 30 -i $O/painel-B1-chats.png -frames:v $B1 -c:v libx264 -crf 12 -pix_fmt yuv420p $O/painel-B1-chats.mp4
# painel B2: rolagem do relatório (deleted cache → suspicious conversations → photos → dating profiles), rec 192,0 s ao vivo
ffmpeg -hide_banner -v error -y -ss 192.0 -i "$R" -vf "fps=30,crop=1170:2070:0:240,scale=692:1224:flags=lanczos" -frames:v $B2 -an -c:v libx264 -crf 12 -pix_fmt yuv420p $O/painel-B2-relatorio.mp4
for f in $O/*.mp4; do echo -n "$f: "; ffprobe -v error -show_entries stream=width,height,nb_frames -of csv=p=0 $f; done
