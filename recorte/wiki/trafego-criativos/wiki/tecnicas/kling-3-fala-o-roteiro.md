---
tipo: tecnica
tags: [video-ia, kling, producao, lipsync, audio-nativo]
fontes: [fonte-producao-roteiro-d-2026-08-31]
---

# Kling 3.0 fala o roteiro (áudio nativo, sem TTS)

O `kwaivgi/kling-v3.0-pro/image-to-video` com `sound=true` gera **fala com lip sync** a partir de diálogo escrito no prompt. Não precisa de TTS separado nem de etapa de lipsync — a cadeia de 3 modelos vira 1.

**Verificado em 31/08/2026:** 5 clipes gerados, todos transcritos com Whisper depois. Bateram palavra por palavra com o roteiro escrito.

## Como escrever

Formato de diálogo da skill `kling-3-prompt` — rótulo estruturado por personagem, ação física **antes** da fala (é o alvo do lip sync), tom explícito, e palavras de ligação (`Then,` / `Pause.` / `Immediately,`) pra as falas não colidirem:

```
Scene 1 (Duration: 11s):
Locked-off medium shot, camera at eye level, no camera movement, no zoom.

The anchor squares his shoulders to camera and settles both hands flat on the desk.
[Character A: Anchor, calm measured broadcast voice, unhurried, American English]: "…"

Then, he tilts his head slightly and lifts one hand in a small open gesture.
[Character A: Anchor, calm measured broadcast voice, unhurried, American English]: "…"

Pause. He holds still, blinking once.
```

## Parâmetros que funcionaram

- `duration` aceita **3 a 15s** — um bloco de fala inteiro cabe num clipe só. Não precisa picotar de 5 em 5.
- `sound=true` · `cfg_scale=0.5` · `shot_type="customize"`.
- `negative_prompt`: `text, letters, subtitles, captions, lower third, ticker, station logo, watermark, camera movement, zoom, second person in frame` — sem isso o modelo tende a inventar tarja e legenda.
- **Image-to-video**: não redescreva o personagem, a imagem já o define. Descreva só como a cena evolui. Identidade e cenário aguentaram 15s sem drift.

## Custo

~$0,168/s no Pro com som. Um criativo de 45s ≈ **$7,56** em vídeo + ~$0,76 nos frames-base do GPT Image 2. Total ~$8,32 por peça de anúncio completa, sem talento e sem set.

Fluxo completo: frames em [[gpt-image-2-para-frames-base]] → clipes aqui → costura em [[costura-de-clipes-por-tarja-persistente]].
