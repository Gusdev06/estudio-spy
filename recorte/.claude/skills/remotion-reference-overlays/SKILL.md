---
name: remotion-reference-overlays
description: Workflow pra montar um vídeo talking-head em Remotion no estilo de uma referência — cortar a gravação crua (retakes, gaguejos, ar morto) sem picar palavra, legendas palavra-a-palavra e motion graphics/B-roll sincronizados à fala, tudo como código (cortes.ts, legendas.ts, beats.ts). Use quando o usuário mandar uma gravação nova pra editar no template mandarimvideo (ou cópia), pedir "edita esse vídeo no mesmo estilo", legendas + gráficos sincronizados, ou quando pedir pra copiar o estilo de edição de um Reel de referência. Reconstruída em 2026-09-16; o pipeline exato mora no overlays/CLAUDE.md do template.
---

# Remotion reference overlays — talking head + legendas + gráficos sincronizados

Este skill é o roteador do pipeline do template **mandarimvideo**
(`~/Downloads/mandarimvideo` ou cópia). A fonte de verdade do passo a passo é
**`overlays/CLAUDE.md` dentro do template — leia ele inteiro antes de
qualquer edição**. Este arquivo só diz a ordem e o que carregar.

## Ordem (cada passo depende do anterior — não pule)

1. **Preparar a mídia** — `public/source.mov` (hard link do original) +
   `proxy.mp4` 1080p via ffmpeg. Nunca apague o master.
2. **Transcrever do zero, palavra a palavra** — skill `video-use`
   (`transcribe.py <video> --model turbo`, local mlx-whisper). Nunca reaproveite
   transcrição antiga. Se um trecho voltar vazio/curto demais, re-transcreva a
   janela isolada e emende por timestamp.
3. **Cortes** — `src/cortes.ts` em segundos do **original**; `paraCortado()`
   deriva a timeline. Varredura sistemática: retakes (n-grams repetidos),
   gaguejos (tokens 2–3× longos), silêncios. Nunca no meio de palavra.
   Método: skill `edicao-precisa`.
4. **Legendas** — `src/legendas.ts`, ancoradas no tempo original, sempre
   centralizadas. Legendas primeiro.
5. **Beats / motion graphics** — `src/beats.ts`, na **mesma passada** das
   legendas. Zona de gráfico nunca vazia; gráfico nunca repete o texto da
   legenda; entra com movimento.
6. **B-roll real** — reuse `public/clipes/` quando não houver gerador
   conectado; senão gere imagem → vídeo (image-to-video) e corte letterbox
   com ffmpeg `cropdetect`. Nada estático.
7. **Push-in contínuo** no rosto, sem reset nos cortes; tela cheia nos blocos
   definidos em `modos.ts`.
8. **Verificar** — `npx remotion still` nos pontos de risco e olhar; preview
   1080p; render final `--crf=14/16`.

## Geometria e estilo

Tudo em `src/palco.ts` (split-screen: zona de gráfico em cima, faixa de
legenda, card da pessoa embaixo), `modos.ts` (quando vai pra tela cheia) e
`motion.ts`. **Nunca hardcode coordenada num componente.** A referência de
estilo (@growithfyn) já está medida e embutida — não busque referência nova
pra manter o estilo.

## Skills que este workflow usa

- `video-use` — transcrição word-level local.
- `edicao-precisa` — método de feedback sem regressão.
- `remotion-best-practices` → `remotion-markup`, `remotion-captions`,
  `remotion-multimedia`, `remotion-studio`, `remotion-render`, `remotion-docs`.
