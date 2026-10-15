# Molde do GD-AD01 — `remontar.sh` (2026-09-03, Bisturi)

Reconstrói a edição do campeão em cima de um talking head novo. Uso, a partir de qualquer pasta:

```
bash gram-detect/criativos/gd-ad01-var-avatar-2026-09-03/remontar.sh <talking-head.mp4> [saida.mp4]
```

Entrada: rosto 9:16 (qualquer resolução; é escalado/cortado pra 1080×1920 e forçado a 30 fps; se for mais curto que 32,6 s o último frame é clonado, se mais longo é cortado). Mudo ou com áudio, tanto faz: **o áudio da saída é sempre o do GD-AD01** (`-map 1:a -c:a copy`). Custo zero.

## O que vem de onde

| Bloco (frame a 30 fps) | Rosto novo | Recortado do GD-AD01.mp4 no mesmo instante | Re-queimado |
|---|---|---|---|
| A 0–233 (0–7,8 s) | quadro inteiro | painel do app de y 1150 pra baixo com degradê alfa em 1150–1230 (o original funde o painel no rosto); caixa rosa x 106–973 · y 862–1058 | — (karaokê já está no recorte, y 1160–1222) |
| B 234–320 (7,8–10,7 s) | desfocado (boxblur) como fundo | card Gram Detect x 89–990 · y 240–1679 | — (karaokê dentro do card) |
| C 321–491 · 591–665 · 777–875 | quadro inteiro | — | karaokê, base y 1521 |
| E 492–590 (16,4–19,7 s) | — | quadro inteiro (story bloqueado) | — |
| D1 666–776 (22,2–25,9 s) | y 0–957 | de y 957 pra baixo (fundo pêssego, pill, painel LIVE INTERCEPTION) | karaokê, base y 984 (montado na costura, cobre o do recorte) |
| 8 876–977 (29,2–32,6 s) | quadro inteiro | card escuro com glitch + setas: x 80–1000 · y 1096–1860 | karaokê, base y 1102 |

Karaokê: `molde/karaoke.tsv` (35 blocos lidos do próprio campeão: troca de bloco por XOR da máscara branca a 30 fps, texto por OCR da Vision do macOS; entre blocos o original apaga o texto por 3–4 frames e o molde repete isso). Fonte **Inter Bold 69 px** (calibrada por 7 larguras medidas, erro médio 0,4%; `gram-detect/scripts/fonts/Inter-Bold.ttf`), branco #FCFCFC, glow escuro em duas passadas (borda 9 px a 35% + borda 4 px #0C0B0C). O topo do ascendente fica em base−49.

Palavras com tempo (whisper local, `mlx-community/whisper-small.en-mlx`, via `uvx --from mlx-whisper`): `molde/audio-16k.json`. Não foram necessárias pro karaokê porque o tempo dos blocos veio do vídeo, mas ficam pra quem precisar.

## Teste do molde (campeão como talking head)

`python3 gram-detect/criativos/gd-ad01-var-avatar-2026-09-03/conferir-molde.py` compara `conferencia/molde/teste-molde-campeao.mp4` com o GD-AD01 frame a frame (978 frames, cinza):

| bloco | diff média (0–255) | pior frame |
|---|---|---|
| A | 1,08 | 1,83 |
| B | **4,38** | 6,63 |
| C1 / C2 / C3 | 1,54 / 1,72 / 1,54 | 2,61 / 2,78 / 2,76 |
| E | 0,98 | 1,64 |
| D1 | 1,56 | 2,56 |
| 8 | 1,37 | 2,02 |

Tudo entre 1 e 1,7 é ruído de reencode. Frames lado a lado em `conferencia/molde/lado-a-lado-t*.png` e `folha-molde.png`.

## Diferenças que sobram (o que o molde NÃO reproduz)

1. **Transições do bloco B.** O original entra no card com um glitch RGB (7,8–8,1 s) e sai com arrasto + motion blur (10,5–10,7 s). O molde corta seco nos dois lados. São os 10 piores frames da comparação (diff 5–6,6).
2. **Fundo do bloco B.** No original o fundo é o rosto desfocado com a transição; no molde é o rosto novo desfocado (boxblur 25). Só aparece nas margens do card (~90 px de cada lado, 240 px em cima e embaixo).
3. **Jump cut em 27,3 s.** O original reenquadra o rosto; o talking head novo não vai ter isso.
4. **Karaokê é uma aproximação.** Inter Bold 69 reproduz largura e posição; o contorno do original é uma sombra suave, o do molde é glow em duas passadas. No estado D1 o karaokê novo é queimado por cima do karaokê que vem no recorte (mesma palavra, mesma posição), então qualquer erro de ≤2 px aparece como franja fina.
5. **Costuras.** Estado A: o degradê alfa em 1150–1230 mistura o painel com o rosto novo (no original é a mesma pessoa). D1: corte reto em y 957. Bloco 8: recorte x 80–1000 mostra ~10 px do moletom cinza do campeão de cada lado do card. Com rosto/roupa diferentes essas faixas podem denunciar.
6. **Blocos A e E trazem o karaokê do campeão** dentro do recorte, portanto não são re-queimáveis com outro texto sem mexer no script.
