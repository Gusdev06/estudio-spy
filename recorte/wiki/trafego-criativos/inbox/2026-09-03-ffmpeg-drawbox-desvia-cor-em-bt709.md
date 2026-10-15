---
tipo: inbox
data: 2026-09-03
origem: Bisturi, lote gd-ad01-var-gancho-2026-09-03
tags: [tecnica, ffmpeg, edicao, cor]
---

# drawbox/drawtext direto no yuv420p desviam a cor em vídeo bt709

No ffmpeg 6.0, `drawbox` e `drawtext` aplicados direto num vídeo yuv420p convertem a cor com matriz
**bt601**. Se o vídeo é **bt709** (caso dos nossos criativos 1080×1920), o matiz sai errado: a caixa
rosa do GD-AD01 (#FE0553) decodifica como #F91A51.

**Solução que funcionou:** desenhar a camada (caixa + texto) em RGB do tamanho exato, converter com
`scale=out_color_matrix=bt709:out_range=tv,format=yuv420p`, e aplicar com `overlay` na posição
medida. Resultado #FC0351 (2 níveis de diferença, invisível). Fora da camada o vídeo passa intocado.

Script reproduzível: `projects/mentoria-spy/gram-detect/criativos/gd-ad01-var-gancho-2026-09-03/montar.sh`.
Relacionado: [[clonar-edicao]], [[medir-fronteira-de-bloco-em-video]], [[catalogo-de-layouts-spy]].
