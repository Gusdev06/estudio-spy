---
tipo: swipe
atualizado: 2026-08-22
tags: [swipe, ad-library, zappdetect, escalados]
---

# Criativos escalados — go.zappdetect.com

As **13 peças com volume real de impressões**, tiradas dos 27 anúncios de `../anuncios/`.
Arquivo prefixado com a posição (`01-`, `02-`…), então o Finder já ordena por escala.
Abra `galeria.html` pra ver tudo com os sinais lado a lado.

## Estrutura de pastas

- `instagram/` — os 13 criativos escalados (todos são de espionagem de Instagram), cada um
  com `.mp4`+poster ou `.jpg`, mais um `.txt` com o texto do anúncio, e `TRANSCRICOES.md`
  com a transcrição peça a peça (hook na tela + UI + copy).
- `whatsapp/` — vazia. Nenhum escalado é de WhatsApp (chequei os 27); ver `whatsapp/LEIA.md`.
- `TRANSCRICOES.md` — transcrição completa das 13 num arquivo só.
- `galeria.html` — visualizador (aponta pra `instagram/`).

## Como o ranking foi montado

A Ad Library não abre gasto, CTR nem ROAS. Os quatro sinais que dá pra extrair:

| Sinal | O que é | Peso |
|---|---|---|
| **Flag de volume** | A Meta carimba "Baixo volume de impressões / <100" nos anúncios que quase não rodam. **É o único dado duro de entrega que ela publica.** | corte |
| **Rank de impressões** | A busca foi ordenada por `total_impressions desc` — a ordem em que os cards voltaram é o ranking. | desempate |
| **Dias no ar** | Anúncio que sobrevive é anúncio que paga. | ordenação |
| **Repetição** | Quantas peças a página roda no mesmo ângulo de copy, e quantos anúncios ela tem no total. | contexto |

**Tier A (aqui):** sem flag de baixo volume. **Tier B:** 10 peças carimbadas `<100`.
**Tier C:** 4 sem criativo (Quinn, banida).

## O ranking

| # | Página | Formato | Dias | Rank imp. | Peças no ângulo | Ads da página | Headline |
|---|---|---|---|---|---|---|---|
| 1 | Sophia Jones | video | 3.2 | #1 | 6 | 5 | Analyze any @username in seconds |
| 2 | Sophia Jones | video | 3.2 | #2 | 6 | 5 | Analyze any @username in seconds |
| 3 | Sophia Jones | video | 3.2 | #3 | 6 | 5 | Analyze any @username in seconds |
| 4 | Charlotte Miller | imagem | 3.2 | #4 | 12 | 4 | Analyze any @username in seconds |
| 5 | Charlotte Miller | imagem | 3.2 | #5 | 12 | 4 | Analyze any @username in seconds |
| 6 | Sophia Jones | video | 3.2 | #6 | 6 | 5 | Analyze any @username in seconds |
| 7 | Charlotte Miller | imagem | 3.2 | #8 | 12 | 4 | Analyze any @username in seconds |
| 8 | VolutPay | video | 2.2 | #9 | 1 | 5 | Free Trial ✅ |
| 9 | Charlotte Miller | video | 3.2 | #10 | 6 | 4 | Analyze any @username in seconds |
| 10 | Sophia Jones | video | 3.2 | #11 | 6 | 5 | Analyze any @username in seconds |
| 11 | VolutPay | video | 2.2 | #12 | 4 | 5 | Free Trial ✅ |
| 12 | VolutPay | video | 2.2 | #15 | 4 | 5 | Free first analysis. No login needed. |
| 13 | VolutPay | video | 2.2 | #16 | 4 | 5 | Free Trial ✅ |

## O que o ranking diz

- **Ninguém da Gustagoat entrou.** Os 9 anúncios da sua página estão todos no Tier B,
  carimbados `<100 impressões` pela Meta. Subiram 21–22/ago; os concorrentes do topo
  subiram 19/ago. Pode ser só idade — vale reconferir em 3–4 dias.
- **Distribuição do Tier A:** Sophia Jones 5, Charlotte Miller 4, VolutPay 4.
- **Vídeo domina:** 10 de 13. Os 3 estáticos são todos da Charlotte Miller.
- **Ângulo mais escalado:** "Ever wondered what someone's Instagram activity really looks like? 👀 Our tool analyzes any…" (6 peças no Tier A).
- **A Sophia Jones ocupa 3 das 4 primeiras posições** com o mesmo ângulo de copy —
  é a página com o ângulo mais validado do grupo.

## Textos completos dos anúncios

Cada peça tem um `.txt` do lado com o texto completo + os sinais de escala (`01-sophia-jones-….txt`). Na `galeria.html` dá pra copiar o texto principal num clique.

Os 13 criativos rodam **4 ângulos de copy** distintos:

### Ângulo 1 — 6 peças (#1, #2, #3, #6, #9, #10) · Charlotte Miller, Sophia Jones

**Texto principal**

> Ever wondered what someone's Instagram activity really looks like? 👀 Our tool analyzes any public profile and shows you who they follow, what they like, and the accounts they interact with the most. Just type the @username — the first analysis is free.

| | |
|---|---|
| **Título** | Analyze any @username in seconds |
| **Descrição** | Free first analysis. No login needed. |
| **Botão** | Saiba mais |
| **Link** | `GO.ZAPPDETECT.COM` |

### Ângulo 2 — 3 peças (#4, #5, #7) · Charlotte Miller

**Texto principal**

> 2.4M people already stopped torturing themselves with 'what if.' They chose to know.👇

| | |
|---|---|
| **Título** | Analyze any @username in seconds |
| **Descrição** | Free test |
| **Botão** | Saiba mais |
| **Link** | `GO.ZAPPDETECT.COM` |

### Ângulo 3 — 1 peças (#8) · VolutPay

**Texto principal**

> I couldn't believe someone could hide so much. 😢 Every message uncovered another betrayal. My heart broke with every word. 💔

| | |
|---|---|
| **Título** | Free Trial ✅ |
| **Descrição** | Free first analysis. No login needed. |
| **Botão** | Saiba mais |
| **Link** | `GO.ZAPPDETECT.COM` |

### Ângulo 4 — 3 peças (#11, #12, #13) · VolutPay

**Texto principal**

> I couldn't believe what I was seeing! 😳 Every message revealed another lie. I never imagined the truth would be this heartbreaking. 💔

| | |
|---|---|
| **Título** | Free Trial ✅ _(×2)_ |
| **Descrição** | Free first analysis. No login needed. |
| **Botão** | Saiba mais |
| **Título** | Free first analysis. No login needed. _(×1)_ |
| **Descrição** | Free Trial ✅ |
| **Botão** | Saiba mais |
| **Link** | `GO.ZAPPDETECT.COM` |

## Ressalva

Nenhuma peça aqui passa de **3,2 dias no ar**. Isso é sinal de *tração inicial*, não de
campeão validado — um criativo só prova que paga depois de 2–3 semanas rodando (foi o
critério usado no teardown de 09/ago em `wiki/trafego-criativos/`). Reconferir a mesma
busca em 7 dias diz muito mais: o que sobreviver é o que realmente escalou.

As versões com cor tratada e metadados limpos das mesmas peças estão em `../tratados/`.
