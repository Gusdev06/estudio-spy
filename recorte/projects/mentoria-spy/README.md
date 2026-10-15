# mentoria-spy

Guarda-chuva de tudo que é **spy** — Spy Gram e Spy Zap. Projetos de produção,
biblioteca de criativos crus e material de trabalho em andamento.

Organizado em 2026-08-29 (a pasta tinha virado depósito: 7.9 GB com arquivos-raiz
do AIOS movidos por acidente e ~760 MB de duplicata).

## Estrutura

| Pasta | O que é |
|---|---|
| `hub/` | **Spy Hub** (30/09): https://spy-hub-three.vercel.app — faturamento, gasto, lucro, chargeback (alerta 1%/3%), funil, gráfico diário e criativos por anúncio com veredito escalar/manter/matar, tudo via MCP da UTMify (bate com o painel) e biblioteca das peças prontas com status de teste. Nunca lê a Meta direto (contingência). → `hub/README.md` |
| `ad-radar/` | **Vigia diária da Ad Library** (`go.centerpag.com`): painel em https://ad-radar-ten.vercel.app com mais tempo no ar, novos, quem tá botando dinheiro (alcance UE), páginas e pararam; email quando sobe anúncio novo. Estado na Apify, sem banco. → `ad-radar/README.md` |
| `gram-detect/` | Projeto Spy Gram. Anúncios captados, tratados, escalados, transcrições, galeria e o `troca-avatar-studio` (repo próprio, roda na VPS — fora deste git). |
| `zapspy/` | Projeto Spy Zap. Criativo original, variações geradas, galeria e build. |
| `criativos-crus/` | Biblioteca bruta de vídeo, por oferta e por lote. Não é entregável — é matéria-prima. |
| `criativos-crus/spy-gram/` | `ads-en/` · `16-julho/` · `26-julho/` · `ingles-com-head/` |
| `criativos-crus/spy-zap/` | `cr02/` · `cr05/` · `base-ingles/` · `23-02-spy-en-es/` · `ingles-17-08/` |
| `criativos-personagens/` | AD01, AD04, AD05 — cada anúncio em 3-4 variações de personagem. |
| `exports-0824/` | Exports de vídeo de 24/08 (6 `.mov`, ~510 MB). Brutos de editor. |
| `tratados-2026-08-28/` | Lote tratado em 28/08: 3 do Instagram (sophia-jones) + 3 do WhatsApp. O `-v1` é uma versão anterior do ig-01, md5 diferente do lote. |
| `troca-avatar/` | Saídas do studio gemini-omni (runs `jmtcqwh8z` e `jmtd66s28`): frame A1, print do prompt, vídeo com áudio + o prompt em texto. |
| `referencias-zapspy-2026-08-29/` | Referências novas de criativo puxadas em 29/08. |
| `downloads/` | Material baixado ainda não triado (snapinsta, CDN do Facebook, w1-*, geraew-ai). Esvazie: ou vira criativo, ou some. |
| `_APAGAR/` | Duplicatas verificadas byte a byte. Leia o `LEIA-ME.txt` e apague a pasta. |

## Regras

- **Mídia pesada não vai pro git** — o `.gitignore` da raiz já barra `mp4/mov/png/jpg/zip`
  dentro de `projects/**`. Só texto, JSON e HTML são versionados aqui.
- **Nada de arquivo solto na raiz desta pasta.** Se não sabe onde por, vai pra `downloads/`
  e você tria depois.
- **Nomes em kebab-case, data em `AAAA-MM-DD`.** Sem espaço, sem `:`, sem acento.
- Antes de produzir entregável, leia o contexto da oferta em `context/` do projeto certo.
