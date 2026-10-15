#!/usr/bin/env bash
# Publica o Estúdio Spy no repo PRÓPRIO e PRIVADO Gusdev06/estudio-spy (o que a VPS clona).
# Monta projects/estudio-spy/app/ = código (site, deploy, package*) + recorte/ gerado agora do AIOS,
# varre segredos e faz commit + push. Uso: bash projects/estudio-spy/fase0/deploy/publicar.sh "mensagem do commit"
set -euo pipefail
FASE0="$(cd "$(dirname "$0")/.." && pwd)"
APP="$(cd "$FASE0/.." && pwd)/app"
MSG="${1:-atualiza estúdio spy}"
mkdir -p "$APP"

rsync -a --delete --exclude node_modules --exclude 'deploy/dist' --exclude '.env' \
  "$FASE0/package.json" "$FASE0/package-lock.json" "$FASE0/CLAUDE-recorte.md" "$FASE0/docker-compose.yml" "$FASE0/.env.example" "$FASE0/site" "$FASE0/deploy" "$APP/"
rm -rf "$APP/recorte" && bash "$FASE0/montar-recorte.sh" "$APP/recorte" >/dev/null
cp "$FASE0/deploy/README.md" "$APP/README.md"
printf 'node_modules/\ndeploy/.env\n.env\n*.log\n.DS_Store\n' > "$APP/.gitignore"

# Segredos: nada de chave, token ou arquivo de credencial pode subir.
if grep -rEIl --exclude-dir=node_modules --exclude-dir=.git \
     '(wsk_[A-Za-z0-9]{16,}|sk-ant-[A-Za-z0-9_-]{20,}|gho_[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY)' "$APP"; then
  echo "ABORTADO: possível segredo nos arquivos acima." >&2; exit 1
fi
find "$APP" -name '.env*' -not -name '*.example' -not -path '*/node_modules/*' | grep -q . && { echo "ABORTADO: arquivo .env no pacote." >&2; exit 1; }

cd "$APP"
[[ -d .git ]] || { git init -q -b main; }
git add -A
git -c user.name="Gusdev06" -c user.email="coven688@gmail.com" commit -q -m "$MSG" || { echo "nada novo pra publicar"; exit 0; }
if ! git remote get-url origin >/dev/null 2>&1; then
  gh repo create Gusdev06/estudio-spy --private --source . --remote origin --push
else
  git push -q origin main
fi
echo "publicado: $(git rev-parse --short HEAD) → $(git remote get-url origin)"
