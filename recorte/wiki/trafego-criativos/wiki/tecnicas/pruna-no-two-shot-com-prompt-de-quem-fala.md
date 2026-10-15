---
tipo: tecnica
tags: [pruna, lipsync, podcast, two-shot, custo, wavespeed]
fontes: [[fonte-podcast-gram-gd-ad01-2026-09-12]]
---

# Pruna no two-shot com prompt de quem fala

`pruna-ai/p-video/avatar` (US$ 0,025/s) anima a pessoa certa numa imagem com **duas pessoas** se o `video_prompt` nomear quem fala e quem escuta: "Only the woman on the LEFT (black blazer) is talking…; the woman on the RIGHT keeps her mouth closed and nods slowly". Sonda de 12/09 (cenas 5 e 7, US$ 0,225) confirmou nos dois two-shots do podcast Gram. O medo anotado ("anima um rosto só") não se sustentou.

Custo do podcast inteiro: 7 clipes, 49 s, **US$ 1,125** — contra ≈ US$ 5 no MiniMax H3 (o pipeline do podcast Zap 06). Preço: 720p (704×1280) upscalado 1,53× pra 1080; áudio curto precisa de pad (o modelo recusa < ~2 s, como o H3).

## Conecta com
- [[lote-podcast-gram-gd-ad01]] — onde foi usado
- [[lote-gram01-l9-var-avatar-5-rostos]] — Pruna em talking head de uma pessoa
- [[fonte-formato-call-in-show-2026-08-31]] — formatos de duas vozes que ficam viáveis a esse custo
