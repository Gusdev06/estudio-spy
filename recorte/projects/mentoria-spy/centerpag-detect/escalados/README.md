---
tipo: swipe
atualizado: 2026-08-27
tags: [swipe, ad-library, centerpag, zapspy, escalados]
---

# Criativos escalados — go.centerpag.com

As **26 peças sem carimbo de baixo volume**, tiradas dos 87 anúncios de `../anuncios/`.
Arquivo prefixado com a posição (`01-`, `02-`…), então o Finder já ordena por escala.
Abra `galeria.html` pra ver tudo com os sinais lado a lado.

## Estrutura de pastas

- `whatsapp/` — os 26 criativos escalados (todos vendem espionagem de **WhatsApp**), cada um
  com `.mp4`+poster ou `.jpg`, mais um `.txt` com o texto do anúncio, e `TRANSCRICOES.md`
  com a transcrição peça a peça (hook na tela + UI + copy).
- `instagram/` — vazia. Ver `instagram/LEIA.md`: o ângulo de Instagram existe no swipe (12
  anúncios), mas nenhum deles passou do carimbo de `<100 impressões`.
- `TRANSCRICOES.md` — transcrição completa das 26 num arquivo só.
- `galeria.html` — visualizador (aponta pra `whatsapp/`).

## Como o ranking foi montado

A Ad Library não abre gasto, CTR nem ROAS. Os quatro sinais que dá pra extrair:

| Sinal | O que é | Peso |
|---|---|---|
| **Flag de volume** | A Meta carimba "Baixo volume de impressões / <100" nos anúncios que quase não rodam. **É o único dado duro de entrega que ela publica.** | corte |
| **Rank de impressões** | A busca foi ordenada por `total_impressions desc` — a ordem em que os cards voltaram é o ranking. | desempate |
| **Dias no ar** | Anúncio que sobrevive é anúncio que paga. | ordenação |
| **Repetição** | Quantas peças a conta roda no mesmo ângulo de copy, e quantos anúncios a Página tem no total. | contexto |

**Tier A (aqui):** 26 sem flag de baixo volume. **Tier B:** 51 peças carimbadas `<100`.
**Tier C:** 8 sem criativo (Rachel Thompson, Página derrubada). **Tier D:** 2 de ruído da busca.

## O ranking

| # | Página | Formato | Dias | Rank imp. | Peças no ângulo | Ads da página | Headline |
|---|---|---|---|---|---|---|---|
| 1 | Esther Vicman | video | 16.1 | #1 | 29 | 2 | Free Test ✅ |
| 2 | Alberto Souza | video | 4.1 | #2 | 0 | 2 | See today everything that happens! |
| 3 | Emilly Bredoff | video | 16.1 | #3 | 29 | 1 | Free Test ✅ |
| 4 | Alberto Souza | video | 17.1 | #4 | 0 | 2 | See today everything that happens... 🔥 |
| 5 | Sara Oliveira | video | 4.1 | #8 | 10 | 10 | ⭐️⭐️⭐️⭐️⭐️ (4.9/5.0) |
| 6 | Isabella Walker | video | 35.1 | #13 | 0 | 1 | See this before it's too late... |
| 7 | Esther Vicman | video | 1.1 | #14 | 29 | 2 | Free Test ✅ |
| 8 | Kendall Godfrey Stephanie | video | 1.1 | #15 | 13 | 5 | Free trial: enter your partner's phone number |
| 9 | Sophia Jones | imagem | 1.1 | #16 | 29 | 4 | Free trial: enter your partner's phone number |
| 10 | Lauren Roberts | video | 35.1 | #17 | 0 | 1 | See this before it's too late... |
| 11 | Fernanda Mello | video | 0.1 | #20 | 29 | 22 | — |
| 12 | Sara Oliveira | video | 4.1 | #22 | 10 | 10 | ⭐️⭐️⭐️⭐️⭐️ (4.9/5.0) |
| 13 | Sophia Jones | video | 1.1 | #23 | 13 | 4 | Free trial: enter your partner's phone number |
| 14 | Simone Maria Braum | video | 2.1 | #25 | 0 | 1 | See this before it's too late... |
| 15 | Sophia Jones | imagem | 1.1 | #30 | 29 | 4 | Free trial: enter your partner's phone number |
| 16 | Sophia Jones | video | 1.1 | #33 | 13 | 4 | Free trial: enter your partner's phone number |
| 17 | Verônica Borges | video | 1.1 | #38 | 29 | 10 | Free Test ✅ |
| 18 | Sara Oliveira | video | 2.1 | #39 | 10 | 10 | ⭐️⭐️⭐️⭐️⭐️ (4.9/5.0) |
| 19 | Kendall Godfrey Stephanie | imagem | 1.1 | #43 | 13 | 5 | Free trial: enter your partner's phone number |
| 20 | Gonçalo Antunes | video | 35.1 | #51 | 0 | 1 | See this before it's too late... |
| 21 | Sara Oliveira | video | 2.1 | #53 | 10 | 10 | ⭐️⭐️⭐️⭐️⭐️ (4.9/5.0) |
| 22 | Kendall Godfrey Stephanie | imagem | 1.1 | #56 | 13 | 5 | Free trial: enter your partner's phone number |
| 23 | Verônica Borges | video | 1.1 | #57 | 29 | 10 | Free Test ✅ |
| 24 | Victorai Martins | video | 1.1 | #73 | 29 | 4 | Free Test ✅ |
| 25 | Sara Oliveira | video | 2.1 | #80 | 10 | 10 | ⭐️⭐️⭐️⭐️⭐️ (4.9/5.0) |
| 26 | Sara Oliveira | video | 2.1 | #84 | 10 | 10 | ⭐️⭐️⭐️⭐️⭐️ (4.9/5.0) |

## O que o ranking diz

- **Só 6 peças passaram de 15 dias no ar** — #1 e #3 (16.1d), #4 (17.1d) e #6, #10, #20 (35.1d).
  Essas três de 35 dias são o núcleo validado do swipe: rodam desde 23/jul e sobreviveram.
  O resto do Tier A subiu entre 23 e 27/ago, então é tração inicial, não campeão provado.
- **A mesma peça aparece re-subida por Páginas diferentes:** #2 = #10, #6 = #23, #7 = #24.
  São arquivos diferentes byte a byte (reupload), mesma edição e mesma duração. É o padrão
  de quem espalha o criativo vencedor por várias contas pra diluir risco de bloqueio.
- **#25 e #26 são o mesmo roteiro com atrizes diferentes** — teste de talento com script travado.
- **Formato:** 22 vídeos, 4 estáticos. Os 4 estáticos são de duas famílias: mock de painel do
  produto (#9, #15) e fake print de story do Instagram (#19, #22).
- **Distribuição do Tier A:** Sara Oliveira 6, Sophia Jones 4, Kendall Godfrey Stephanie 3,
  Esther Vicman / Alberto Souza / Verônica Borges 2 cada, e 7 Páginas com 1 peça.
- **#17 é do outro produto.** É o criativo de espionagem de Instagram (`Gram Detect`) — o mesmo
  que abre o swipe do `gram-detect`. Rodando numa conta que vende WhatsApp.
