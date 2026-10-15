# Amanda Silva 1680455873461877: variação 1 com avatar e cenário novos (25/09/2026)

Esteira spy (Zap), papel Bisturi. Pedido: trocar a pessoa **e** o cenário e manter áudio, tela do app, card, CTA, ritmo e cortes.
**Original:** `~/Downloads/Amanda Silva_1680455873461877_2026-09-25.mp4` (md5 `36f93080…`), 960×720 horizontal, 30 fps, 1817 frames, vídeo 60,57 s / áudio 60,74 s, copiado para `REFERENCIA-original.mp4`. Não tem legenda queimada.

## Molde medido (`medir.py` → `molde/medidas.json`, rosto YuNet escolhido por score)
| frames | o que é | na peça |
|---|---|---|
| n 0–733 (0–24,47 s) | ela em quadro cheio, rosto cx 370 / cy 239 / h 307 | avatar nova (clipe c1) |
| n 12–26 | card "You Deserve The Truth" entra deslizando da direita | card do original, com máscara por frame (diferença contra o n11, +6 px) |
| n 27–211 | card parado em x 632–912, y 105–480 (canto reto e opaco) | card do original (retângulo x 631–913, y 104–481) |
| n 211–215 | light leak laranja (o card some no n212) | leak extraído como camada aditiva (original − n216, mediana em blocos de 40 px, blur σ25) e somado sobre a avatar |
| n 734–1816 (24,47 s até o fim) | **split fixo**: janela dela x 0–577, com o mesmo zoom e deslocada (rosto cx 291). A tela do app é opaca de x 578 a 959 e é o que muda (form, terminal, chats, "Unlock") | avatar (c2/c3) com o rosto em cx 291; tela do app original de x 578 em diante |

Nos cortes do vídeo dela não houve jump cut além do n734. Os "2º rostos" que o YuNet encontra depois do n1579 estão todos dentro da tela do app (x ≥ 601), nos avatares dos chats.

## O que foi trocado
- **Avatar:** mulher de ~27 anos, pele morena clara, cabelo castanho-escuro ondulado com pontas caramelo, argolinhas douradas e suéter creme de gola redonda. É do mesmo gênero e da mesma faixa de idade da voz.
- **Cenário:** saiu a sala com o quadro de Veneza, o castiçal e o vaso âmbar. Entrou um quarto claro com cabeceira de carvalho, travesseiros brancos, abajur de cerâmica aceso, planta e cesto de palha na parede. Não tem tela nem texto.
- Base: `base/base.png` (gpt-image-2/edit, medium, 1k, 1448×1086) sobre o frame limpo n360. Comparação em `conferencia/base-vs-ref.jpg`.

## Pipeline (de `projects/mentoria-spy/`)
1. `gerar-base.py` gera a imagem-base; `base/pessoa.txt` e `base/cena.txt` guardam o casting.
2. `SEED=7 bash .../gerar-clipes.sh c1 c2 c3` roda a Pruna com o áudio original em WAV: c1 = 0–24,467 s (até o corte pro split), c2 = 24,467–43,0 s, c3 = 43,0 s até o fim. A emenda c2|c3 cai na pausa de 43,0 s. Prompt só em positivo. Os clipes saem em 1088×832 a 24 fps, e o frame 0 (imagem parada) é pulado.
3. `checar.py c1 c2 c3`: os 3 passaram de primeira (borda ≤ 4, lateral ≤ 6, sempre 1 rosto, h 289–336). Não houve regeração.
4. `montar.py pecas/variacao.mp4` compõe frame a frame em numpy e envia para o ffmpeg. As emendas são por número de frame. Escala = 307 / h do rosto no clipe (~0,975). O áudio é copiado do original.
5. `varredura.py` e `folha.py` fazem a conferência.

## Entrega
`pecas/variacao.mp4`: 960×720, 1817 frames, 60,57 s. O md5 do stream de áudio é `8c9d0d5d…`, **idêntico ao original**, e a peça decodifica inteira.

## Varredura final (`conferencia/varredura.json`)
- Olhei os 1817 frames. Fora das áreas herdadas de propósito (card e tela do app), em média 1,9% dos pixels ficam iguais ao original (máximo 2,8%). No mapa, esses pixels aparecem espalhados no cabelo escuro e na parede, uma coincidência de cor sem forma (`conferencia/iguais-ao-original.jpg`). Não sobra frame, contorno ou reflexo da pessoa original.
- A peça tem exatamente 1 rosto fora da tela do app em todos os frames.
- Folhas: `conferencia/momentos.jpg` (12 instantes, original | peça), `conferencia/emendas.jpg` (entrada do card, leak, n733/734, n1290) e `conferencia/card-entrada.jpg` (zoom da entrada do card).
- Correção feita durante a varredura: no n12 o card é só uma lasca preta de 5 px na borda direita, que a máscara por diferença não pegava. Acrescentei uma detecção por pixel escuro na borda.

## Concessões
- Na emenda c2|c3 (n1290, 43,0 s) a avatar dá um pequeno salto de pose, porque o original não tem corte nesse ponto. Ele cai numa pausa da fala.
- A luz do leak (n211–215) é uma aproximação suavizada da luz original, não um pixel a pixel.
- Os gestos de mão do original (n205–216) não se repetem: a avatar tem a própria movimentação.

## Custo real: US$ 1,62 (teto US$ 1,80)
| prediction | o quê | US$ |
|---|---|---|
| 70359954… | gpt-image-2/edit (base) | 0,0665 |
| 2a3478f2… | Pruna c1 (25 s) | 0,625 |
| 37befa03… | Pruna c2 (19 s) | 0,475 |
| 2588e51b… | Pruna c3 (18 s) | 0,45 |
Os valores foram conferidos em `wavespeed billings`. Não houve estorno nem regeração.
