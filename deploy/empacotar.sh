#!/usr/bin/env bash
# Gera os dois pacotes que sobem pra VPS (rodar no Mac, da raiz do AIS-OS ou de qualquer lugar):
#   deploy/dist/estudio-spy-app.tgz  → código (site, Dockerfiles, compose); vira o contexto do build na VPS
#   deploy/dist/recorte.tgz          → recorte do AIOS (skills, wiki, método); vai pra /srv/estudio/recorte, somente leitura nos pedidos
set -euo pipefail
export COPYFILE_DISABLE=1   # sem os ._ do macOS no tar
FASE0="$(cd "$(dirname "$0")/.." && pwd)"
DIST="$FASE0/deploy/dist"; rm -rf "$DIST"; mkdir -p "$DIST"
bash "$FASE0/montar-recorte.sh" "$DIST/recorte" >/dev/null
tar -C "$DIST/recorte" -czf "$DIST/recorte.tgz" . && rm -rf "$DIST/recorte"
tar -C "$FASE0" --exclude node_modules --exclude 'deploy/dist' -czf "$DIST/estudio-spy-app.tgz" \
  package.json package-lock.json site deploy CLAUDE-recorte.md
ls -lh "$DIST"
