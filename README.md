# Estúdio Spy — deploy na VPS (Hostinger)

Repositório **privado**: tem o recorte do método (skills, wiki, moldes). Não torne público.

Arquitetura: **1 orquestrador** (site + porta interna + chaves) e **1 container por pedido** (agente sem chave, sem internet,
só a pasta do pedido com escrita e o recorte somente leitura). O orquestrador cria os containers pelo Docker do host.

```
internet ─HTTPS─► Traefik/Caddy ─► orquestrador:4330 (site)
                                     │  chaves: ANTHROPIC_API_KEY_PRODUTO, WAVESPEED_API_KEY
                                     │  porta interna 4331 (rede estudio-interno, nunca publicada)
                                     ▼
          docker run por pedido ─► agente (rede interna sem saída) ── só fala com orquestrador:4331
                                    /w      = recorte/ deste repo (somente leitura)
                                    /w/job  = pasta do pedido (escrita)
```

## Antes
1. **VPS Hostinger** KVM com **Ubuntu 24.04 + Docker** (template "Ubuntu 24.04 with Docker"). Mínimo pra 2 pedidos ao mesmo tempo:
   **4 vCPU / 8 GB / 80 GB** (KVM 4). Cada pedido usa até 2 vCPU e 4 GB (`AGENTE_CPUS`, `AGENTE_MEMORIA`).
2. **Chave da Anthropic só do produto** (console.anthropic.com → API Keys), com limite de gasto mensal no console.
3. **Chave da WaveSpeed só do produto** (wavespeed.ai/accesskey).
4. **Domínio** com registro A apontando pro IP da VPS (ex.: `app.suamarca.com`).

## Subir (SSH na VPS, como root)
```bash
# 1. acesso ao repo privado: chave de deploy só leitura
ssh-keygen -t ed25519 -N "" -f ~/.ssh/estudio_deploy
cat ~/.ssh/estudio_deploy.pub
#   → GitHub: Gusdev06/estudio-spy → Settings → Deploy keys → Add (só leitura), cole a chave
printf 'Host github.com\n  IdentityFile ~/.ssh/estudio_deploy\n' >> ~/.ssh/config

# 2. código + pastas
mkdir -p /srv/estudio/jobs
git clone git@github.com:Gusdev06/estudio-spy.git /srv/estudio/app
chmod -R a+rX,go-w /srv/estudio/app/recorte

# 3. chaves (arquivo só do root; nunca vai pro git)
cat > /srv/estudio/app/deploy/.env <<'X'
ADMIN_EMAILS=coven688@gmail.com
ANTHROPIC_API_KEY_PRODUTO=cole-aqui
WAVESPEED_API_KEY=cole-aqui
X
chmod 600 /srv/estudio/app/deploy/.env

# 4. imagens e subida
cd /srv/estudio/app/deploy
docker compose --profile build build          # 1ª vez demora (mediapipe, ffmpeg)
docker compose up -d orquestrador
docker compose logs -f orquestrador           # espere "interno em 0.0.0.0:4331 (executor: docker)"
```

## HTTPS
O orquestrador escuta só em `127.0.0.1:4330`. Publique com um proxy na própria VPS. O mais simples é o Caddy:
```bash
apt-get install -y caddy
printf 'app.suamarca.com {\n  reverse_proxy 127.0.0.1:4330\n  request_body { max_size 600MB }\n}\n' > /etc/caddy/Caddyfile
systemctl reload caddy
```
(Se usar o painel Docker/Traefik da Hostinger em vez do Caddy, aponte o domínio pra porta 4330 do serviço `orquestrador`; não publique a 4331.)

Depois: abra o domínio, **crie a conta com o e-mail de `ADMIN_EMAILS`** e faça um pedido barato (variação de imagem).

## Atualizar
No Mac: `bash projects/estudio-spy/fase0/deploy/publicar.sh "o que mudou"` (gera o recorte novo, varre segredos e dá push).
Na VPS, com nenhum pedido rodando:
```bash
cd /srv/estudio/app && git pull && cd deploy && docker compose --profile build build && docker compose up -d orquestrador
```

## Conferir depois de subir (não deu pra testar no Mac: sem Docker e sem chave de API)
- [ ] as duas imagens constroem (pip do mediapipe, modelos, `npm ci` no Linux);
- [ ] pedido sem internet: `docker run --rm --network estudio-interno estudio-spy-agente curl -m 5 https://example.com` precisa **falhar**;
- [ ] o agente responde no 1º pedido (proxy da Anthropic com a chave do produto);
- [ ] o container do pedido não tem `ANTHROPIC_API_KEY_PRODUTO` nem `WAVESPEED_API_KEY` no ambiente;
- [ ] o agente escreve em `/w/job` e **não** consegue escrever em `/w`;
- [ ] mandar "continua" num pedido parado retoma a conversa (sessão em `/w/job/.sessao`);
- [ ] um pedido real de troca de avatar de ponta a ponta.

## Variáveis (deploy/.env)
| variável | padrão | o que é |
|---|---|---|
| `ADMIN_EMAILS` | — | e-mails admin (sem limite, creditam vídeos), separados por vírgula |
| `ANTHROPIC_API_KEY_PRODUTO` | — | chave da Anthropic (só o orquestrador vê) |
| `WAVESPEED_API_KEY` | — | chave da WaveSpeed (só o orquestrador vê) |
| `AGENTE_CPUS` / `AGENTE_MEMORIA` | 2 / 4g | recursos por pedido |
| `PREVIA_USD` | 1 | gasto de mídia permitido antes da aprovação |
| `TETO_MIDIA_POR_VIDEO_USD` | 6 | teto de mídia por vídeo aprovado |
| `TETO_TOKENS_BASE_USD` / `TETO_TOKENS_POR_VIDEO_USD` | 8 / 4 | teto de tokens por pedido |
