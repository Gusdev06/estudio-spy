---
tipo: fonte
tags: [producao, video-ia, kling, gpt-image-2]
data: 2026-08-31
---

# fonte — produção do Roteiro D, 100% IA (31/08/2026)

Primeira peça de anúncio da operação produzida inteira por IA: 45s, formato breaking-news âncora + especialista, para a oferta spy zap (`go.centerpag.com`).

Saída em `projects/mentoria-spy/gram-detect/criativos/roteiro-d-2026-08-31/` (`roteiro-d-v1-45s.mp4`, 1080×1920).

## Cadeia

`GPT Image 2` (2 frames-base, 9:16 2k high) → `Kling 3.0 Pro image-to-video` (5 clipes falados, sound=true) → `ffmpeg` (tarja + concat).

## Achados

- **Kling 3.0 Pro fala o roteiro escrito.** Áudio nativo com lip sync; os 5 clipes transcritos com Whisper bateram palavra por palavra. Elimina TTS e etapa de lipsync. Ver [[kling-3-fala-o-roteiro]].
- **`duration` vai até 15s** — cada bloco de fala coube num clipe só, sem picotar.
- **Continuidade de cenário entre personagens** resolvida repetindo literalmente os blocos de cenário e luz nos dois prompts de imagem. Ver [[gpt-image-2-para-frames-base]].
- **Identidade e cenário aguentaram 15s sem drift** no image-to-video.
- **Custo total ~$8,32** por peça completa (2 imagens $0,76 + 45s de vídeo $7,56), sem talento e sem set.
- Gotcha do CLI: `wavespeed run --download` falhou com `fetch failed` mesmo com o job `completed`. A predição fica válida — recuperar com `wavespeed show <id>` e baixar por `curl`.
- Gotcha de ffmpeg: `drawbox` sobre canvas `rgba` transparente escreve a cor mas **não escreve alpha** — a barra some e só o texto aparece. Desenhar a tarja direto na cadeia de filtros de cada clipe (parâmetros idênticos) em vez de gerar PNG.

## Páginas geradas

- [[gpt-image-2-para-frames-base]]
- [[kling-3-fala-o-roteiro]]
