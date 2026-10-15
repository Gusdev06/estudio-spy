# Variação avatar + cenário em 5 formatos diferentes (25/09)

O que decide a técnica é **onde a pessoa original encosta nas camadas**:
- **Janela separada do texto/legenda** (podcast Flora, split da Amanda Silva): troca só a janela; título e karaokê do original ficam intactos.
- **Card opaco por cima**: dá pra manter o interior do card com máscara erodida uns 8 px pra dentro.
- **Card translúcido, borda difusa ou flash de cor sobre a pessoa** (Amanda Lima): recortar vaza a original. Redesenhar o card (texto, hex, posição, animação medidos) e refazer o flash como filtro sobre o vídeo novo.
- **Pessoa recortada por cima de outro vídeo** (Lauren): segmentar o avatar novo (MediaPipe) e reconstruir por inpainting o que a silhueta antiga cobria.
- **Esquete sem fala** (Beatriz): image-to-video (Seedance Lite 720p, ~US$ 0,03/s) com pessoa e cenário novos.
- Sempre: emendas por número de frame; fundo borrado atrás de painel também é a pessoa original; varredura frame a frame antes de entregar.
Fonte: READMEs em `projects/mentoria-spy/centerpag-detect/criativos/var1-*-2026-09-25/` e `gram-detect/criativos/var1-beatriz-*`.
