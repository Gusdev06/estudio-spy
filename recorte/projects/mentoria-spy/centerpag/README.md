---
tipo: swipe
atualizado: 2026-08-22
tags: [swipe, ad-library, centerpag, whatsapp, instagram, espionagem]
---

# centerpag — swipe da Ad Library (go.centerpag.com)

Anúncios ativos que apontam pra **go.centerpag.com**, baixados em 22/08/2026 e separados por
plataforma-alvo. Mesma categoria do `../gram-detect` (espionagem de conta de parceiro), mas aqui
o ângulo dominante é **clonar/ler WhatsApp**, não Instagram.

> 📌 **Existe uma coleta mais nova e mais completa desse mesmo domínio:** `../centerpag-detect/`
> (27/08/2026, 87 anúncios, no formato do `../gram-detect` — com tiers, escalados ranqueados,
> transcrições e criativos tratados). Só 3 dos 44 anúncios deste swipe ainda estavam ativos lá.
> Use este aqui como registro histórico do estado da biblioteca em 22/08.

## Números

- Busca `keyword_unordered` retornou ~180; **59 renderizaram**, **44 realmente apontam pra
  centerpag** (resto = ruído da busca não-exata). Todos os 44 baixados.
- **37 de WhatsApp · 7 de Instagram** (1 classificado como incerto).
- 32 vídeos + 12 estáticos. Nenhum marcado "baixo volume" pela Meta — **todos rodando**.
- **Escalado de verdade:** o topo tem **31,2 dias no ar** (Alberto Souza), contra os 3,2 dias
  máximos do gram-detect. Aqui existe criativo validado.

## Estrutura

- `whatsapp/` — os 37 de WhatsApp (mídia + `.txt` por peça + `galeria.html`).
- `instagram/` — os 7 de Instagram (idem).
- `anuncios/` — todos os 44 juntos (fonte).
- `manifest.json` — 1 entrada por anúncio, com `plataforma`, `plataforma_confianca` e
  `plataforma_evidencia` (o sinal visual usado pra classificar cada uma).

## Como classifiquei WhatsApp vs Instagram

A copy da Meta **não** cita a plataforma (0 menções a WhatsApp em 44). O sinal está no **texto na
tela e na UI do vídeo**, então olhei peça a peça:
- **WhatsApp** = app verde, "CLONE WHATSAPP", "WHAT THEIR WHATSAPP IS HIDING", dashboard
  "WhatsApp Monitoring", chat verde "message deleted", ou "read your partner's text messages".
- **Instagram** = UI/branding do Instagram (watchdog_app, live_shield "New Instagram follower",
  proof_alert perfil privado, authentic.kate story, ou copy "@username / Instagram activity").
- 1 peça (Emilly Bredoff, ID 1319335…) ficou **incerta** — frame só de cabeça-falante, sem UI;
  ficou em `instagram/` porque a página é majoritariamente IG, mas está marcada no manifest.

## WhatsApp — top por dias no ar

| Dias | Página | Formato | Headline |
|---|---|---|---|
| 31.2 | Alberto Souza | video | See this before it's too late... |
| 31.2 | Alberto Souza | video | See this before it's too late... |
| 31.2 | Alberto Souza | video | See this before it's too late... |
| 31.2 | Alberto Souza | video | See this before it's too late... |
| 12.2 | Alberto Souza | video | See today everything that happens... 🤫 |
| 12.2 | Alberto Souza | video | See today everything that happens... 🔥 |
| 11.2 | Esther Vicman | video | Free Test ✅ |
| 11.2 | Emilly Bredoff | video | Free Test ✅ |

## Instagram — todos

| Dias | Página | Formato | Confiança | Evidência |
|---|---|---|---|---|
| 16.2 | Emilly Bredoff | imagem | alta | estático "What you see vs what really happens" com |
| 11.2 | Emilly Bredoff | imagem | alta | story proof_alert perfil Instagram privado (Secret |
| 7.2 | Emilly Bredoff | imagem | alta | story live_shield "LIVE MONITORING — New Instagram |
| 6.2 | Emilly Bredoff | video | incerta | INCERTO: frame só cabeça-falante; página Emilly é  |
| 5.2 | Emilly Bredoff | imagem | alta | story watchdog_app "HIS ACTIVITY LOG" — UI Instagr |
| 3.2 | Kendall Godfrey Stephanie | imagem | alta | story authentic.kate "Ask me anything" formato Ins |
| 1.2 | Mia Davis | video | alta | copy FR "activité Instagram... @nom d’utilisateur" |

## Leitura rápida

- **11 páginas anunciando pro mesmo destino** (Mia Davis 11, Alberto Souza 6, Emilly Bredoff 6, Nelma Miranda 5, Charlotte Miller 4, Maria Carmen 3, Helena Alves 3, Inêz Cunha 2, Kendall Godfrey Stephanie 2, Esther Vicman 1, Sophia Jones 1) — operação multi-conta, mesmo padrão do gram-detect.
- **Alberto Souza é o dono da escala:** 6 anúncios, 4 com 31 dias no ar. Criativo mais validado do
  lote — ver primeiro.
- **Ângulo campeão = "mensagem apagada":** quase toda peça mostra "This message was deleted / 147
  deleted messages recovered / recover deleted". A promessa não é ler o que está lá, é recuperar o
  que a pessoa apagou pra esconder.
- **Charlotte Miller, Sophia Jones e a UI "live_shield/LIVE MONITORING" são reaproveitados do
  gram-detect** — a mesma central roda os dois produtos (zappdetect + centerpag).

## Ressalvas

- **Performance não verificada** — Ad Library não expõe gasto/CTR/ROAS; proxy é dias no ar.
- **keyword_unordered inclui ruído** — filtrei pros 44 que citam centerpag; os ~180 brutos = outra coleta.
- Ângulo de altíssimo risco de compliance (clonar WhatsApp, ler mensagem de parceiro, "brute-force
  login"). No gram-detect a Meta baniu a página Quinn por isso. Swipe de estrutura, não de claim.

