#!/usr/bin/env bash
# Monta as versoes finais a partir dos clipes brutos de uma rodada.
#
#   bash montar.sh <dir-da-rodada> [--fps 30] [--altura 1920]
#
# Espera esta estrutura:
#   <dir>/clipes/a-01.mp4 a-02.mp4 ...   clipes MUDOS  (versao A)
#   <dir>/clipes/b-01.mp4 b-02.mp4 ...   clipes COM AUDIO (versao B)
#   <dir>/audio-original.m4a             audio do criativo campeao
#
# Produz:
#   <dir>/versao-A-mudo.mp4    -> entra no lipsync (passo seguinte, na skill)
#   <dir>/versao-B-voz-kling.mp4
#
# Reencoda tudo para um alvo unico antes de concatenar. O concat demuxer
# exige parametros identicos, e clipes gerados voltam com fps/resolucao
# variaveis -- concatenar sem normalizar produz audio dessincronizado ou
# um arquivo que so toca o primeiro clipe.

set -euo pipefail

DIR="${1:-}"
FPS=30
ALTURA=1920

shift || true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --fps)    FPS="$2"; shift 2 ;;
    --altura) ALTURA="$2"; shift 2 ;;
    *) echo "flag desconhecida: $1" >&2; exit 2 ;;
  esac
done

[[ -n "$DIR" && -d "$DIR" ]] || { echo "uso: bash montar.sh <dir-da-rodada>" >&2; exit 2; }
command -v ffmpeg >/dev/null || { echo "ffmpeg nao encontrado" >&2; exit 2; }

LARGURA=$(( ALTURA * 9 / 16 ))
LARGURA=$(( LARGURA - LARGURA % 2 ))   # h264 exige dimensao par
TMP="$DIR/.montagem"
mkdir -p "$TMP"

# $1 = prefixo dos clipes (a|b), $2 = saida, $3 = com_audio (sim|nao)
montar_versao() {
  local pref="$1" saida="$2" com_audio="$3"
  local clipes=( "$DIR"/clipes/${pref}-*.mp4 )

  if [[ ! -e "${clipes[0]}" ]]; then
    echo "  (sem clipes ${pref}-*.mp4, pulando)"
    return 0
  fi

  local lista="$TMP/lista-$pref.txt"
  : > "$lista"

  local i=0
  for c in "${clipes[@]}"; do
    i=$((i + 1))
    local norm
    norm="$TMP/$(printf '%s-%02d-norm.mp4' "$pref" "$i")"

    # scale+pad preserva o enquadramento e completa a borda em vez de
    # distorcer o rosto quando o clipe volta num ratio ligeiramente diferente.
    local vf="scale=${LARGURA}:${ALTURA}:force_original_aspect_ratio=decrease"
    vf="$vf,pad=${LARGURA}:${ALTURA}:(ow-iw)/2:(oh-ih)/2:color=black,fps=${FPS},setsar=1"

    if [[ "$com_audio" == "sim" ]]; then
      # Mapear explicitamente o audio DO CLIPE. Um fallback de silencio mapeado
      # sem condicao substitui a voz gerada e o arquivo sai mudo -- e como o
      # stream de audio existe, ffprobe nao acusa nada. Por isso testamos o
      # clipe antes e so entramos com anullsrc quando ele realmente nao tem som.
      if ffprobe -v error -select_streams a:0 -show_entries stream=codec_type \
           -of csv=p=0 "$c" 2>/dev/null | grep -q audio; then
        ffmpeg -y -loglevel error -i "$c" -map 0:v:0 -map 0:a:0 \
          -vf "$vf" -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p \
          -c:a aac -ar 44100 -ac 2 "$norm"
      else
        echo "     (clipe sem audio: preenchendo com silencio)"
        ffmpeg -y -loglevel error -i "$c" -f lavfi -i anullsrc=r=44100:cl=stereo \
          -map 0:v:0 -map 1:a:0 -shortest \
          -vf "$vf" -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p \
          -c:a aac -ar 44100 -ac 2 "$norm"
      fi
    else
      ffmpeg -y -loglevel error -i "$c" -an \
        -vf "$vf" -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p "$norm"
    fi

    printf "file '%s'\n" "$(cd "$(dirname "$norm")" && pwd)/$(basename "$norm")" >> "$lista"
  done

  ffmpeg -y -loglevel error -f concat -safe 0 -i "$lista" -c copy "$saida"
  local dur
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$saida")
  printf "  %-28s %s clipes · %.1fs" "$(basename "$saida")" "$i" "$dur"

  # Conferir que o audio tem CONTEUDO, nao so um stream presente. Uma trilha
  # silenciosa passa em qualquer checagem de metadado -- so o nivel denuncia.
  if [[ "$com_audio" == "sim" ]]; then
    local vol
    vol=$(ffmpeg -hide_banner -i "$saida" -af volumedetect -f null - 2>&1 \
          | sed -n 's/.*mean_volume: \(-*[0-9.]*\) dB.*/\1/p')
    printf " · audio %s dB" "${vol:-?}"
    awk -v v="${vol:--91}" 'BEGIN{ if (v < -70) print "\n  ATENCAO: trilha praticamente muda. O audio dos clipes nao entrou na montagem." }'
  fi
  echo
}

echo "montando em ${LARGURA}x${ALTURA} @ ${FPS}fps"
montar_versao a "$DIR/versao-A-mudo.mp4"       nao
montar_versao b "$DIR/versao-B-voz-kling.mp4"  sim

AUD="$DIR/audio-original.m4a"
if [[ -f "$AUD" && -f "$DIR/versao-A-mudo.mp4" ]]; then
  da=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$AUD")
  dv=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$DIR/versao-A-mudo.mp4")
  echo
  printf "audio original %.1fs · video mudo %.1fs\n" "$da" "$dv"
  awk -v a="$da" -v v="$dv" 'BEGIN{
    if (v < a - 0.3)
      print "  ATENCAO: video mais curto que o audio. O lipsync teria de dar loop,\n  e loop aparece. Gere um clipe a mais ou aumente a duracao do ultimo."
    else
      print "  ok para sync_mode=cut_off."
  }'
fi

rm -rf "$TMP"
echo
echo "proximo passo: lipsync da versao A (ver references/kling-wavespeed.md)"
