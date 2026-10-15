# Talking head WhatsApp com avatar indiano (2026-09-13)

Pedido do Gusta: "faça desse 2 variações priorizando personagens indianos."

**Original:** `AQPWDdPSgUI11a49WWTO-…mp4` do swipe (md5 `84c64d0e7da8330396a2a06282d934be`, 708×1274, 30 fps, **40,94 s**). Cópia em `REFERENCIA-original.mp4`. Um homem sul-asiático fala direto para a câmera numa sala com estante de livros; faixa de título fixa, karaokê queimado embaixo, b-roll de mulher chorando + CTA no final.

| | Arquivo |
|---|---|
| **Peças** | `TALKINGHEAD-WPP-i1.mp4` e `-i2.mp4` — 708×1274, 30 fps, 1224 frames, **40,80 s**. Cópias: `CRIATIVOS-PRONTOS/44` e `45` |
| Imagens | `base/i1.png` · `i2.png` (GPT Image 2 edit sobre o frame do original, quality medium) |
| Clipes | `clipes/i1.mp4` · `i2.mp4` — Pruna `p-video/avatar` 720p, **um clipe único de 32,0 s** por avatar |
| Áudio para o lipsync | `audio/vo-31.8s.mp3` — os 31,8 s de fala do original |

## Estrutura do original (medida)

Mesmo princípio do clone anterior: **layout de post sobre fundo preto**, com a legenda fora da janela de vídeo — por isso karaokê e faixa são preservados pixel a pixel.

| faixa | y | o que é |
|---|---|---|
| 113–199 | faixa de título em 2 linhas | "HOW TO SEE YOUR PARTNER'S / MESSAGES ON YOUR OWN PHONE" — fixa o vídeo inteiro |
| **298–971** | **janela de vídeo 708×674** | a única coisa que muda |
| ~1028–1154 | karaokê | caixa alta branca com palavras em vermelho e amarelo |

Diferente do podcast de mais cedo, aqui é **um plano só**: o homem fala continuamente do frame 0 ao 951. Isso permitiu gerar **um clipe único de 32 s** por avatar em vez de cinco blocos.

| frames | tempo | conteúdo | ação |
|---|---|---|---|
| 0–646 | 0,00–21,57 | homem falando | **avatar novo** |
| 647–651 | 21,57–21,73 | fade do estouro branco (5 frames) | original |
| 652–790 | 21,73–26,37 | **estouro branco**, alpha 0,851 medido | **avatar novo, estourado com o mesmo alpha** |
| 791–951 | 26,37–31,73 | homem falando | **avatar novo** |
| 952–1223 | 31,73–40,80 | b-roll da mulher + CTA com seta vermelha | original |

O estouro branco de 4,6 s é uma característica do original (o quadro inteiro lava até alpha 0,851 e o karaokê congela em "HISTORY"). Reproduzi em vez de corrigir, para não mexer na edição: o avatar passa pelo mesmo `lutrgb` de `val*0,149 + 217`.

## Elenco

| peça | avatar |
|---|---|
| **44** | homem indiano, pele castanha média, ~35, barba preta cheia e aparada, cabelo ondulado penteado para trás |
| **45** | homem indiano, pele castanha escura, ~48, cabelo grisalho nas têmporas, barba curta grisalha, óculos de armação fina |

Sala, estante de livros, microfone, camisa escura e luz de abajur: idênticos, porque as imagens saíram de um **edit do frame do próprio original**.

## Geometria

Recorte do Pruna (704×1280) para a janela (708×674, proporção 1,0505): `crop=704:670:0:380`, escalado para 708×674.

## Custo real — US$ 1,73

| item | valor |
|---|---|
| 2 imagens `gpt-image-2/edit` (quality medium) | US$ 0,133 |
| 2 clipes Pruna de 32,0 s | US$ 1,600 |
| montagem, whisper, conferência | US$ 0 |

Mais barato por peça que o podcast (US$ 0,87 contra ~US$ 1,20), porque um plano único dispensa cinco chamadas por elenco. Nenhum clipe precisou ser regerado: a trava "SOLO SHOT" com a lista do que não pode entrar funcionou de primeira nos dois.

## Reproduzir

```
# imagem nova: editar elencos/<id>.txt e rodar o mesmo edit do README (gpt-image-2/edit, quality=medium)
python3 centerpag-detect/criativos/talkinghead-wpp-indianos-2026-09-13/montar-indiano.py clipes/<id>.mp4 TALKINGHEAD-WPP-<id>.mp4
```
De `projects/mentoria-spy/`. `CROP=` por env ajusta o enquadramento. Conferência em `conferencia/`: `orig-vs-i1-i2.jpg`, `emendas-i1.jpg` (entrada e saída do estouro e fim do rosto), `varredura-2.jpg` (clipes inteiros), `calibra-recorte.jpg`.

## O que conferir no olho

- **Enquadramento:** o avatar fica um pouco mais centralizado que o original, que tem a cabeça mais à esquerda. Ajustável pelo `CROP`.
- **Resolução:** o swipe é 708×1274; a janela tem 708×674 reais. A peça sai na mesma resolução, sem ganho de nitidez.
- **Duração:** 40,80 s contra 40,94 s do original (o corte cai no último frame cheio).
