---
tipo: tecnica
tags: [frame-1, thumbnail, miniatura, edicao, qa]
fontes: [[fonte-escalados-proprios-spy-gram-2026-09-03]]
---

# Frame 1 sem piscar

O primeiro frame é a miniatura que a Meta mostra antes do play. Os dois perdedores do kit do campeão no Spy Gram (GD-AD03, US$ 33; GD-AD02, US$ 9) têm o apresentador **no meio de um piscar** no frame 1 — olhos fechados num, semifechados no outro. Os ganhadores abrem de olhos abertos olhando pra câmera (o GD-AD01 abre com a boca em movimento, mas olhos abertos).

Não é a causa principal (copy e avatar pesam mais), mas é a mais barata de corrigir: mover o `in point` 3–5 frames.

## Checklist de QA do frame 1
1. `ffmpeg -ss 0 -frames:v 1` e olhar. Olhos abertos, olhando pra lente.
2. Gancho escrito já legível no frame 1 (não entra com animação depois).
3. Nada tampando o botão/card (no SPY 7 a barra do Safari cobre o botão).
4. Sem typo na faixa (`infront` ficou 7 s no GD-AD03).

## Conecta com
- [[familia-criativos-spy-gram-ads-en]] — os dois casos.
- [[teste-que-pode-falhar]] — abrir a peça no tamanho original antes de aprovar.
