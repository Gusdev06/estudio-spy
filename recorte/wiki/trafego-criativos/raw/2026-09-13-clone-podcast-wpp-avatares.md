# Clone do podcast WhatsApp com avatares novos (2026-09-13)

Pedido do Gusta: "quero fazer uma variação desse mantendo mesmo áudio, mesmo formato, edição, legenda, só quero mudar os avatares do podcast."

**Original:** arquivo do swipe `AQNYVrOoSOjFVO5Z98GZZAcnp4o2sgL_…mp4` (md5 `0c67873f635d8861b36817f9d144dd13`, 720×1280, 30 fps, **8 min 39 s**). O criativo de verdade dura **41,3 s**; o resto é um card estático ("SOME THINGS ARE HIDDEN. THE TRUTH ISN'T." + LEARN MORE!) que ocupa os outros 7 min 58 s. Cópia do trecho útil em `REFERENCIA-original-41s.mp4`.

| | Arquivo |
|---|---|
| **Peça** | `PODCAST-WPP-avatares-novos.mp4` — 720×1280, 30 fps, 1239 frames, **41,30 s**. Cópia: `CRIATIVOS-PRONTOS/40-…` |
| Imagens novas | `base/novo-close-A.png` · `novo-close-B.png` · `novo-two-shot.png` (GPT Image 2 edit sobre os frames do original) |
| Clipes | `clipes/bloco-{1b,2b,3b,4b,5b}.mp4` — Pruna `p-video/avatar` 720p (704×1280, 24 fps) |
| Áudio por bloco | `audio/bloco-N.mp3` — recortado do original, só para dirigir o lipsync |
| Referência | `REFERENCIA-original-41s.mp4` · frames em `base/ref-*.png` |

## O que o original é, por dentro (medido, não estimado)

Não é vídeo em tela cheia: é um **layout de post sobre fundo preto**. Isso é o que torna a troca de avatar limpa — a legenda e a faixa vivem fora da imagem.

| faixa | y | o que é |
|---|---|---|
| 0–138 | preto | margem |
| **139–271** | faixa branca | título fixo "HOW TO READ YOUR PARTNER'S MESSAGES ON YOUR OWN PHONE" — o vídeo inteiro |
| 272–346 | preto | margem |
| **347–933** | **janela de vídeo 720×587** | a única coisa que muda na variação |
| 934–~1060 | preto + karaokê | legenda queimada, caixa alta branca com palavra destacada em roxo/magenta |

Como o karaokê está **fora** da janela de vídeo e sobre fundo preto, ele foi preservado pixel a pixel — não precisou ser recriado nem re-sincronizado. Mesma coisa para a faixa do título, os painéis do produto, o b-roll de celular e o áudio.

## Blocos: o que foi trocado e o que foi mantido

| bloco | tempo | plano | o que se ouve | ação |
|---|---|---|---|---|
| 1 | 0,00–0,50 | two-shot no sofá | "Did you guys know" | **avatar novo** |
| 2 | 0,50–2,75 | close A | "…that you can clone your partner's WhatsApp using" | **avatar novo** |
| — | 2,75–4,25 | painel "From You / Enter the phone number to spy" | | original |
| 3 | 4,25–11,75 | close B | "What do you mean just the number?" … "it's for a friend." | **avatar novo** |
| 4 | 11,75–16,50 | close A | "Look, it's relatively new… really simple to use." | **avatar novo** |
| — | 16,50–37,50 | painéis do produto + b-roll de celular (21 s, metade do criativo) | | original |
| 5 | 37,50–41,25 | close A | "If you wanna have access, I'll leave the link below…" | **avatar novo** |

18,75 s de rosto regerados; 22,5 s de painel e b-roll reaproveitados sem tocar.

## Elenco novo

| papel | original | novo |
|---|---|---|
| A (explica, domina o criativo) | mulher negra de pele clara, cabelo ondulado com mechas, batom vermelho, blusa verde-sálvia | mulher branca ~30, cabelo castanho liso na altura do ombro, argolas finas, **mesma blusa verde-sálvia** |
| B (pergunta) | mulher negra de pele média, cabelo preso, blusa preta | mulher latina ~28, cabelo cacheado escuro solto, **mesma blusa preta** |

Estúdio, sofá creme, microfones, plantas, parede clara e luz: idênticos. As imagens foram feitas por **edit** dos frames do próprio original, não do zero — por isso o cenário bate.

## Geometria (medida)

- Pruna devolve 704×1280 a partir de uma imagem 864×1536: escala pela altura (fator 0,8333) e corta 8 px de cada lado.
- Recorte de volta para a janela: **A** `crop=650:530:42:467` · **B** `crop=704:574:0:440` · **two-shot** `crop=704:574:0:430`, todos escalados para 720×587.

## Custo real — US$ 1,75

| item | valor |
|---|---|
| 3 imagens `openai/gpt-image-2/edit` (quality high, 1k) | US$ 0,678 |
| 9 chamadas `pruna-ai/p-video/avatar` (5 finais + sonda + 3 descartadas) | US$ 1,075 |
| montagem, whisper, conferência | US$ 0 |

⚠️ O `gpt-image-2/edit` tem base price de US$ 0,07 mas cobrou **US$ 0,22–0,24 por imagem** em quality=high/1k. Sem as regerações teria dado ≈ US$ 1,20.

## A armadilha do Pruna neste formato

Na primeira leva, o Pruna **inventou um homem de barba entrando pela borda esquerda** do quadro, em dois clipes (o modelo "completa" a cena de podcast com um entrevistador). Resolvido com prompt explícito:

> SOLO SHOT: exactly one person in the frame at all times. Nobody else is visible, no second person, no one enters or appears at the edges of the frame.

No two-shot, a mesma ideia ao contrário: "EXACTLY TWO women… and nobody else ever appears", dizendo qual delas fala. Custo da lição: 3 clipes jogados fora (US$ 0,40).

## Reproduzir

```
python3 centerpag-detect/criativos/podcast-wpp-clone-avatares-2026-09-13/montar-clone.py [saida.mp4]
```
De `projects/mentoria-spy/`. Custo zero: só remonta a partir dos clipes já gerados. Conferência em `conferencia/`: `orig-vs-novo.jpg` (10 instantes lado a lado), `emendas.jpg` (frame antes/depois de cada troca), `lipsync-cmp.jpg`.

## O que conferir no olho

- **Resolução da fonte:** o swipe é 720×1280 e a janela de vídeo tem 720×587 reais. A peça sai na mesma resolução do original; não há ganho de nitidez a extrair daí.
- **Bloco 3:** em 5,70–6,78 s quem fala é a voz de A ("You don't need to touch their phone") enquanto a imagem é de B. No original B está reagindo; aqui o Pruna faz B mover a boca no texto de A. É o ponto mais visível da diferença.
- **Duração:** entregue com 41,3 s (o criativo). O card estático de 8 min do original não foi reproduzido.
