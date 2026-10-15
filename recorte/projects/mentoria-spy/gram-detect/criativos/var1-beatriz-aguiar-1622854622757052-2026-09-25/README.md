# Beatriz Aguiar 1622854622757052: variação 1 com pessoas e cenários novos (25/09/2026)

**Original:** `~/Downloads/Beatriz Aguiar_1622854622757052_2026-09-25.mp4` (md5 `1bf1e5c2…`), 720×1280, 30 fps, 1380 frames (46,0 s), copiado em `REFERENCIA-original.mp4`.
**Peça:** `pecas/variacao.mp4`, 720×1280, 30 fps, 1380 frames. O áudio foi copiado do original e o md5 do stream AAC bate com o dele (`78085d03…`).

## Molde medido (frames)
| frames | o que é | na peça |
|---|---|---|
| 0–308 | Esquete da mulher sem fala, ao som de música: o vídeo ocupa y 112–1279, com faixa preta em 0–111 e o título estático "How yo girl act / when she get caught / texting her ex" (y 111–313) | 0–214: clipe **eA** a partir de 0,87 s (plano da porta, câmera de mão; o tapa na câmera cai por volta de 3,7 s). 215–221: chicote borrado. 222–308: clipe **eB** (plano aberto). Em 215–235 a cor segue a média do original, reproduzindo o flash roxo e amarelo |
| 309–428 | Homem em close nas linhas 0–861, com a legenda em y≈734–787. O painel do app fica embaixo (linhas ≥ 862; em 426–428 ele sobe: 856/850) | Clipe **s1** (áudio 10,30–14,30). O painel vem do original |
| 429–641 | Painel do app, retângulo fixo x 128–591 e y 231–1048, sobre o homem ampliado e desfocado | Fundo refeito com o homem novo (zoom ~1,45, σ 14, ganho 0,85); o painel vem do original |
| 642–827 | Homem em tela cheia. Em 642–644 há transição borrada; em 648–672 ele se inclina para a câmera (rosto até x≈220, −13°) | Clipe **s2** (áudio 21,40–27,60), enquadrado frame a frame pelo rosto original |
| 828–1186 | Painéis sobre o homem desfocado | Mesmo tratamento de 429–641 |
| 1187–1379 | Homem em tela cheia (1187–1189 borrado). CTA a partir de 1296: "CLICK THE BELOW" cromado com glitch (y≈130–225) e 3 setas animadas | Clipe **s3** (áudio 39,567–46,0) |

A legenda é karaokê: Bebas-like branca em degradê, com a palavra ativa em ciano, contorno preto e sombra, sempre **sobre o vídeo**. Por isso ela foi redesenhada por cima do vídeo novo: copiei só os pixels do glifo (branco/ciano) e sintetizei o contorno e a sombra, sem levar nenhum fundo antigo. O título da esquete foi refeito com a máscara estática e um brilho escuro sintético. O CTA usa o corpo opaco do texto, filtrado pela paleta, com glow vermelho sintético. As setas foram desenhadas a partir do molde de forma, com deslocamento e opacidade medidos frame a frame (`molde/chevrons.json`, ciclo de ~1 s).

## Trocas
- **Homem (quem fala):** homem de ~24 anos, pele morena clara, cabelo curto escuro com degradê, barba curta, moletom cinza. Ele está sentado num sofá de sala escura à noite, com abajur quente e estante ao fundo (o original está em cadeira gamer preta, com camiseta preta e barba cheia).
- **Esquete:** mulher de ~25 anos com cabelo cacheado solto, moletom rosa e calça cinza, num corredor verde-sálvia com porta de madeira escura. O plano aberto mostra o mesmo corredor com um quarto de edredom cinza (a original tem coque, camiseta cinza "BT", portas brancas e parede bege).

## Pipeline (de `projects/mentoria-spy/`, pasta autocontida)
1. `gerar-bases.py homem mulherA`, depois `gerar-bases.py mulherB`: gpt-image-2/edit em medium/1k. O homem sai do frame limpo n700. A mulher A sai do n30, recortado da área de vídeo. A mulher B usa o n250 como enquadramento e a mulherA como identidade.
2. `gerar-clipes.sh s1 s2 s3 eA eB`: s* são Pruna p-video/avatar (720p, seed 7, prompt só em positivo, áudio ORIGINAL do trecho). eA e eB são Seedance v1 Lite i2v 720p (8 s e 3 s, 9:16, seed 7). Os 5 clipes decodificam inteiros, sem truncamento.
3. `checar.py`: YuNet em meia resolução, porque o rosto é grande demais e em resolução cheia ele erra. s1, s2 e s3 passaram (1 rosto, sem moldura nem lateral mexendo). No eA, o "2º rosto" é falso positivo no moletom; conferi a imagem.
4. `montar.py pecas/variacao.mp4`: todas as emendas por número de frame, com áudio `-c:a copy` do original.
5. `varredura.py`: marca, frame a frame, onde a peça tem pixel igual ao original fora do painel do app.

## Varredura final
- `conferencia/final-emendas.jpg` (214/215, 221/222, 308/309, 428/429, 641/642, 827/828, 1186/1187) e `conferencia/final-instantes.jpg` (11 instantes): original em cima, peça embaixo. Não aparece nenhuma pessoa original.
- `conferencia/iguais.jpg` e `iguais-segmentos.jpg`: os pixels iguais ao original são só os glifos da legenda, do título e do CTA, mais coincidência de cor (parede amarelada no flash 224–229 e sombras escuras). Nenhum pedaço do homem ou da mulher originais aparece, nem desfocado atrás do painel, nem nas transições.
- O que vem do original de propósito: o painel do app (a gravação de tela, que inclui a foto de perfil "bennet_chloe_" do próprio funil), o painel de baixo em 309–428 e o áudio.

## Custo real: US$ 1,0129 (teto US$ 1,20)
3 imagens gpt-image-2/edit custaram 0,211 (0,0665 + 0,0665 + 0,0779). Os 3 clipes Pruna custaram 0,45 (0,10 + 0,175 + 0,175) e os 2 clipes Seedance, 0,352 (0,256 + 0,096). Nada foi regerado e nenhum clipe foi descartado. Os IDs estão em `molde/prediction-ids.txt`, cruzados com `wavespeed billings`.

## Concessões
- **Split (309–428):** a Pruna entrega o homem mais afastado do que o close do original. Para cobrir 720×862 sem borda, o rosto ficou ~15% maior que no original.
- **Inclinação 648–672:** reproduzida por rotação e deslocamento do quadro, pois a Pruna não se inclina. O zoom fica um pouco maior para não expor borda.
- **Esquete:** a ação é outra, gerada por i2v. Ela grita, gesticula, dá um tapa na câmera por volta de 3,7 s (no original, 2,7 s) e depois reclama encostada no batente. A mulher não fala no áudio (é música), então não há lipsync.
- **Título da esquete:** o brilho escuro saiu um pouco mais suave que o do original.

## Hook original (25/09)
A pedido do Gusta ("manter o hook original que eu mandei"), `pecas/variacao-hook-original.mp4` usa a esquete do anúncio original nos frames 0–308 (corte seco no 308/309); do 309 em diante é a variação. A versão com a esquete gerada (`pecas/variacao.mp4`) fica guardada.
