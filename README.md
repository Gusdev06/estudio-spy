# Estúdio Spy — deploy no EasyPanel

Repositório **privado**: tem o recorte do método (skills, wiki, moldes). Não torne público.

Arquitetura: **1 orquestrador** (site + porta interna + chaves) e **1 container por pedido** (agente sem chave, sem internet,
recorte embutido somente leitura em `/w`, só a pasta do pedido com escrita em `/w/job`). O orquestrador cria os containers pelo Docker do host.

```
internet ─HTTPS─► EasyPanel (Traefik) ─► orquestrador:4330 (site)
                                           │  chaves: ANTHROPIC_API_KEY_PRODUTO, WAVESPEED_API_KEY
                                           │  porta interna 4331 (rede estudio-interno, nunca vira domínio)
                                           ▼
             docker run por pedido ─► estudio-spy-agente (rede interna sem saída) ── só fala com orquestrador:4331
```

## Antes
1. **VPS** com EasyPanel. Mínimo pra 2 pedidos ao mesmo tempo: **4 vCPU / 8 GB / 80 GB** (cada pedido usa até 2 vCPU e 4 GB).
2. **Chave da Anthropic só do produto** (console.anthropic.com → API Keys), com limite de gasto mensal no console.
3. **Chave da WaveSpeed só do produto** (wavespeed.ai/accesskey).
4. **Domínio** com registro A apontando pro IP da VPS (ex.: `app.suamarca.com`).

## Subir no EasyPanel
1. **Projeto** → *Create Service* → **Compose**.
2. **Source → Git**
   - Repository: `git@github.com:Gusdev06/estudio-spy.git` · Branch: `main`
   - **Build Path: `/`** · Compose file: `docker-compose.yml`
   - Repo privado: o EasyPanel mostra uma **deploy key** do serviço → GitHub → `Gusdev06/estudio-spy` → *Settings → Deploy keys → Add* (só leitura) → cole.
3. **Environment**: o EasyPanel já carrega o `.env.example`. Preencha `ANTHROPIC_API_KEY_PRODUTO` e `WAVESPEED_API_KEY`, confira `ADMIN_EMAILS` e **marque "Create .env file"**.
4. **Deploy**. O 1º build demora uns minutos (ffmpeg, mediapipe, modelos). O serviço `agente` sobe e sai na hora: é normal, ele só existe pra gerar a imagem dos pedidos.
5. **Domains** → *Add Domain* → seu domínio · serviço **orquestrador** · porta **4330** · HTTPS ligado.
6. Abra o domínio, **crie a conta com o e-mail de `ADMIN_EMAILS`** e faça um pedido barato (variação de imagem).

Os pedidos ficam em `/srv/estudio/jobs` no host (o Docker cria a pasta no 1º deploy). Faça backup dessa pasta.

## Atualizar
No Mac: `bash projects/estudio-spy/fase0/deploy/publicar.sh "o que mudou"` (gera o recorte novo, varre segredos e dá push).
No EasyPanel: **Deploy** no serviço, com nenhum pedido rodando (o deploy reinicia o orquestrador e reconstrói a imagem dos pedidos).

## Conferir depois de subir (não deu pra testar no Mac: sem Docker e sem chave de API)
Rode no **Console** do EasyPanel (ou SSH no host):
- [ ] as duas imagens construíram: `docker images | grep estudio-spy`
- [ ] pedido sem internet: `docker run --rm --network estudio-interno estudio-spy-agente curl -m 5 https://example.com` precisa **falhar**
- [ ] o orquestrador subiu em modo docker: nos logs, `interno em 0.0.0.0:4331 (executor: docker)`
- [ ] o agente responde no 1º pedido (proxy da Anthropic com a chave do produto)
- [ ] o pedido não tem as chaves: `docker run --rm estudio-spy-agente env | grep -i -E 'anthropic_api_key_produto|wavespeed'` não mostra nada
- [ ] o agente não escreve no recorte: num pedido, ele consegue escrever em `/w/job` e não em `/w`
- [ ] mandar "continua" num pedido parado retoma a conversa (sessão em `/w/job/.sessao`)
- [ ] um pedido real de troca de avatar de ponta a ponta

Se algo falhar, mande o log do serviço `orquestrador` (aba Logs) e o arquivo `/srv/estudio/jobs/_servidor.log`.

## Variáveis (.env)
| variável | padrão | o que é |
|---|---|---|
| `ADMIN_EMAILS` | — | e-mails admin (sem limite, creditam vídeos), separados por vírgula |
| `ANTHROPIC_API_KEY_PRODUTO` | — | chave da Anthropic (só o orquestrador vê) |
| `WAVESPEED_API_KEY` | — | chave da WaveSpeed (só o orquestrador vê) |
| `AGENTE_CPUS` / `AGENTE_MEMORIA` | 2 / 4g | recursos por pedido |
| `PREVIA_USD` | 1 | gasto de mídia permitido antes da aprovação |
| `TETO_MIDIA_POR_VIDEO_USD` | 6 | teto de mídia por vídeo aprovado |
| `TETO_TOKENS_BASE_USD` / `TETO_TOKENS_POR_VIDEO_USD` | 8 / 4 | teto de tokens por pedido |
