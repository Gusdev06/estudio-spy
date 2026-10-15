---
tipo: referencia-criativo
atualizado: 2026-09-10
tags: [teardown, edicao, spy-zap, centerpag, whatsapp, ugc-talking-head, karaoke, troca-avatar]
fonte: https://www.facebook.com/ads/library/?id=934941213003855
ad_id: "934941213003855"
arquivo_peca: centerpag-detect/anuncios/secret-revealed-934941213003855.mp4
---

# Teardown de EDIÇÃO — Secret Revealed (934941213003855)

32,37s · 720×1280 (9:16) · 30fps · locução masculina em inglês (F0 ≈ 115 Hz).

Este teardown cobre **só a edição**, pra guiar a **troca de avatar** — áudio, copy **e legenda
(karaokê)** ficam idênticos ao original. O que muda é o talking head. Mesmo formato do teardown da
Emilly (`2026-09-09-teardown-edicao-emilly-bredoff.md`).

> ⚠️ **Alvo do lote:** trocar SÓ o rosto. A locução, a faixa vermelha de hook e o **karaokê**
> (fonte, cor, posição, palavras, timing) têm de ser reproduzidos IGUAIS. Só o rosto muda.

## Arquivo da peça

Caminhos **relativos a `projects/mentoria-spy/`**:

| O que | Caminho |
|---|---|
| **Vídeo (fonte)** | `centerpag-detect/anuncios/secret-revealed-934941213003855.mp4` |
| Cópia de origem (raiz) | `Secret Revealed_934941213003855_2026-09-10.mp4` (md5 idêntico) |
| Frames por fase | `centerpag-detect/referencias/frames/sr-f1..f6-*.jpg` |

`.mp4` 3.920.706 bytes, md5 `583550c62c643e2a805783e6c707d2ab` (a cópia em `anuncios/` bate byte a
byte com a da raiz). Ad Library: <https://www.facebook.com/ads/library/?id=934941213003855>

⚠️ Mídia pesada não entra no git — o portal referencia o arquivo no disco.

## O que este molde tem de diferente (leia antes)

**É o molde mais simples do acervo.** Diferente da Emilly (faixa verde + card do app rodando o
funil na direita) e do wpp-01 (matte preta + card alfa crescendo), esta peça é **UGC puro**:

- **Rosto em quadro cheio o vídeo INTEIRO** (0 → 31,9s). Nunca sai.
- **Uma faixa vermelha de hook fixa** no topo.
- **Karaokê de 1 palavra** sincronizado com a fala, sobre o rosto.
- **Nenhum card do app, nenhum funil, nenhum terminal, nenhum CTA gráfico.** A prova é 100%
  falada + a palavra do karaokê. O vídeo termina no rosto falando, sem tela de CTA.
- **9:16 nativo** (720×1280) — não precisa refazer proporção como na Emilly (que era 4:3).

**Mesma locução da Emilly, palavra por palavra** (é o mesmo roteiro/áudio, outro ator e outro
molde). A diferença entre as duas peças é puramente de edição.

---

## Layout medido (720×1280)

```
┌──────────────────────────────┐  y 0
│   ██ HOW TO READ YOUR 📱 ██   │  y ~116–188  ← faixa vermelha, linha 1 (+ emoji)
│  ██ PARTNER'S TEXT MESSAGES ██│  y ~192–260  ← faixa vermelha, linha 2 (mais larga)
│                              │              texto branco, caixa alta, fixo o vídeo todo
│      TALKING HEAD            │
│   (quadro cheio, homem       │
│    asiático de óculos,       │
│    camiseta azul, poltrona   │
│    clara, quarto bege)       │
│      olhos ≈ y 320–360       │
│                              │
│         PHOTOS               │  ← KARAOKÊ: 1 palavra, branco, caixa alta,
│      (y ~800–880)            │     contorno/sombra, centralizado, troca por beat
│                              │
└──────────────────────────────┘  y 1280
```

**Fronteiras medidas (frame de 2s + 19,6s):**

| Elemento | Medida | Método |
|---|---|---|
| **Faixa vermelha** (bbox das 2 linhas) | `x 90–627`, `y ~116–260` | cobertura de vermelho (mediana) |
| Cor da faixa | **#B40000** (vermelho escuro) | mediana dos pixels vermelhos |
| Texto da faixa | **branco** (#FFFFFF), caixa alta, bold | pixels claros dentro da faixa |
| **Karaokê** (caixa da palavra) | centralizado ~x360, `y ~800–880` (≈ 63–69% da altura) | branco > 220 na faixa y 780–1010 |
| Cor do karaokê | branco #FFFFFF com contorno/sombra escura | — |
| Rosto (olhos) | ≈ `y 320–360` | inspeção |

⚠️ O bbox bruto do vermelho deu até `y 444` porque a mão/polegar do ator tem tom avermelhado em
alguns frames — a faixa **visível** é `y 116–260` (duas barras). Não confundir.

- **Faixa vermelha de hook:** duas barras vermelhas #B40000 empilhadas. Linha 1
  `HOW TO READ YOUR` + emoji 📱 (o emoji vaza pra ~x627); linha 2 `PARTNER'S TEXT MESSAGES` (barra
  mais larga). Texto branco, caixa alta, fonte sans bold condensada (Anton/Impact-like), centrado.
  **Fixa o vídeo inteiro** (0 → 31,9s), nunca muda.
- **Talking head:** homem asiático, ~30 anos, óculos redondos, camiseta azul-clara, sentado numa
  poltrona clara, parede bege com abajur à esquerda. Enquadramento busto, rosto centralizado, olhos
  ≈ y 320–360. Olha pra câmera, gesticula muito com as mãos. **Presente 0 → 31,9s (100% da peça).**
- **Karaokê:** **1 palavra por vez**, branca, caixa alta, fonte sans bold pesada
  (Montserrat/Poppins ExtraBold-like), contorno/sombra escura pra ler sobre a camiseta e o rosto.
  Centralizado horizontalmente, baseline ≈ y 800–880. **Troca a cada palavra-chave** (~1 por
  segundo), sincronizado com a fala. **É a legenda que tem de ser reproduzida idêntica.**
- **Watermark:** nenhuma.

**Diferença estrutural pra Emilly:** lá o karaokê não existia e havia card do app na direita; aqui
é o oposto — **karaokê é o elemento central** e **não há card nenhum**. O rosto ocupa a peça toda.

---

## Fases de tela (corte medido)

**Só existe UM corte: `19,33s`** — e é um **jump cut no próprio talking head** (o ator reposiciona
levemente; a faixa e o karaokê seguem sem quebra). Não há mudança de layout em nenhum momento: é o
mesmo plano (rosto + faixa + karaokê) do início ao fim.

| Fase | Tempo | Rosto | O que está na tela | Fala por cima |
|---|---|---|---|---|
| **1 — Setup** | 0,0–~10,5 | sim | rosto + faixa vermelha + karaokê (`TO · MESSAGES · BOYFRIENDS · HUSBANDS · PHONE · PHYSICAL · PART · OUT`) | "Here's how to see text messages… no need to have physical access… she'll never find out she's being spied on" |
| **2 — Passo a passo** | ~10,5–17 | sim | idem (`ON · FIRST · NUMBER · BELOW · SECONDS · TRACKS · MESSAGES · DONE`) | "first enter your partner's number… wait a few seconds while the site tracks and clones the messages. Done!" |
| **(jump cut 19,33s)** | — | sim | leve reposicionamento do ator; sem troca de layout | — |
| **3 — Payoff** | ~17–23 | sim | idem (`ACCESS · PHOTOS · VIDEOS · LOCATION · DELETED · MESSAGES`) | "now you have access to all messages, photos, videos, real-time location, and even deleted messages" |
| **4 — Oferta/CTA falado** | ~23–32,4 | sim | idem (`BELOW · FREE · MY · ACCOUNT · IT'S · TAP · TYPE · SPY`); termina no rosto, sem tela de CTA | "I'll leave a link below where you can run a free check using my personal account, but be quick because it's limited. Tap the button below and type the number you want to spy on." |

**Não há tela de CTA gráfica.** O vídeo acaba com o ator falando "…the number you want to spy on"
em 31,9s (32,37s de arquivo). O CTA é puramente verbal.

---

## Transcrição com tempo (whisper local)

Método: áudio extraído com ffmpeg (mono 16 kHz), transcrito com `mlx-whisper`
(`whisper-small.en`). 112 palavras, **230 wpm**.

| Tempo | Fala |
|---|---|
| 0,0–5,4 | Here's how to see text messages from your boyfriend's, girlfriend's, husband's, or wife's phone using your own phone. |
| 5,6–7,5 | No need to have physical access to the phone. |
| 7,7–8,4 | And the best part? |
| 8,7–10,5 | She'll never find out she's being spied on. |
| 10,8–13,4 | Look, first enter your partner's number on the site below. |
| 13,7–16,6 | Wait a few seconds while the site tracks and clones the messages. |
| 17,0–17,2 | Done! |
| 17,6–23,1 | Now you have access to all messages, photos, videos, real-time location, and even deleted messages. |
| 23,6–28,8 | I'll leave a link below where you can run a free check using my personal account, but be quick because it's limited. |
| 28,8–31,9 | Tap the button below and type the number you want to spy on. |

⚠️ **Mesma trava de política da Emilly** — a fala diz explicitamente **"spied on"**, **"tracks and
clones the messages"**, **"the number you want to spy on"**. Áudio fica, ordem do Gusta; registrado
como o eixo mais exposto se um dia regravar.

---

## Karaokê — spec pra reproduzir IGUAL

**1 palavra por vez**, branca caixa alta, fonte sans ExtraBold, contorno/sombra escura, centralizada
em ~x360, baseline ≈ y 800–880 (65% da altura). A palavra troca na palavra-chave falada (não é toda
palavra — pega o substantivo/verbo de destaque de cada trecho, ~1 por segundo).

**Sequência observada (1 frame por segundo):**

```
0:TO  1:MESSAGES  2:BOYFRIENDS  3:HUSBANDS  4:PHONE  5:PHONE  6:PHYSICAL  7:PHONE
8:PART  9:OUT  10:ON  11:FIRST  12:NUMBER  13:BELOW  14:SECONDS  15:TRACKS
16:MESSAGES  17:DONE  18:ACCESS  19:PHOTOS  20:VIDEOS  21:LOCATION  22:DELETED
23:MESSAGES  24:BELOW  25:FREE  26:MY  27:ACCOUNT  28:IT'S  29:TAP  30:TYPE  31:SPY
```

**Pra o timing exato,** usar os onsets de palavra do whisper (já extraídos, `tx.json` no scratchpad;
principais): `messages 0.98 · boyfriends 1.78 · husbands 3.2 · phone 4.22 · physical 6.2 · part
8.12 · out 9.36 · on 10.32 · first 11.28 · number 12.36 · below 13.02 · seconds 14.16 · tracks
15.12 · messages 16.16 · done 16.98 · access 18.08 · photos 19.56 · videos 20.08 · location 21.08 ·
deleted 22.24 · messages 22.62 · below 24.18 · free 25.46 · my 26.34 · account 26.94 · it's 28.38 ·
tap 28.84 · type 30.42 · spy 31.44`. Cada palavra do karaokê entra no onset da sua palavra falada e
sai quando entra a próxima.

---

## Frames exportados por fase

Em `centerpag-detect/referencias/frames/`:

| Fase | Frame |
|---|---|
| 1 — Abertura | `sr-f1-open-0.5s.jpg` |
| 1/2 — Features | `sr-f2-features-8s.jpg` |
| 2 — Meio | `sr-f3-mid-16s.jpg` |
| pós jump-cut | `sr-f4-postcut-19.6s.jpg` |
| 4 — Oferta | `sr-f5-offer-26s.jpg` |
| fim (sem CTA gráfico) | `sr-f6-end-31s.jpg` |

---

## Reaproveitável por recorte vs. o que refazer

**Reaproveitável direto:**
- **Áudio inteiro** — locução original, ordem do Gusta.
- **Faixa vermelha de hook** (`y 116–260`, #B40000 + texto branco): gráfico chapado com texto fixo.
  Melhor **redesenhar** (2 barras vermelhas + `HOW TO READ YOUR 📱` / `PARTNER'S TEXT MESSAGES` em
  branco caixa alta) do que recortar, porque no original ela fica sobre o cabelo do ator — recortar
  traria pedaço do cabelo dele. Redesenho idêntico é limpo e é overlay independente do rosto.

**Precisa ser refeito:**
- **O talking head** (quadro cheio, **0 → 31,9s**): gerar o rosto novo 720×1280 (ou maior e
  reenquadrar) com lipsync **sobre a locução original**. ⚠️ **O rosto está presente a peça toda** —
  o lipsync cobre os ~31,9s inteiros (mais caro que a Emilly, que só tinha 26,5s de rosto). Estimar
  por `duração × preço unitário` e reportar antes de disparar. Enquadramento a bater: busto
  centralizado, olhos ≈ y 320–360, gesticulando, fundo de quarto claro.
- **O karaokê** (1 palavra, branco caixa alta, y ~800–880): **recriar como faixa de texto** sobre o
  rosto novo, usando a sequência de palavras e os onsets acima. Não dá pra recortar do original (está
  queimado sobre o ator antigo) — tem de ser regerado com a mesma fonte, cor, tamanho, posição e
  timing.

**Ordem de montagem:** rosto novo (lipsync, 0–31,9s) na base → faixa vermelha redesenhada no topo
(fixa) → karaokê recriado palavra a palavra sincronizado ao áudio. Uma alavanca do lote: **o rosto**.
Nada mais muda.

---

## O que o Bisturi precisa saber antes de montar

1. **Molde UGC puro:** 1 plano (rosto) + 2 overlays (faixa vermelha fixa + karaokê). **Sem card do
   app, sem funil, sem terminal, sem CTA gráfico** — não montar nada disso.
2. **9:16 nativo** (720×1280) — sem rebuild de proporção (diferente da Emilly).
3. **Rosto presente 100% da peça** (0–31,9s) — lipsync cobre tudo, é o item mais caro; estimar
   antes.
4. **Karaokê é obrigatório e idêntico:** 1 palavra, branco caixa alta, contorno, ~y 820, sequência
   e onsets acima.
5. **Faixa vermelha fixa** `y 116–260`, #B40000, texto branco caixa alta, com o emoji 📱 no fim da
   linha 1 — redesenhar, não recortar.
6. **Um corte só (19,33s)** e é jump cut do ator — não é troca de layout; no rosto novo pode ser um
   corte seco ou nem existir (o avatar novo é contínuo).
7. **Termina no rosto** em 31,9s, sem tela de CTA. Não adicionar chevrons/blur.
