---
tipo: fonte
tags: [video, ltx, wavespeed, teste, fr, custo]
data: 2026-08-22
---

# Fonte — Teste de vídeo LTX 2.3 na esteira FR

Teste de 3 criativos FR animados com `wavespeed-ai/ltx-2.3/image-to-video` (720p, 5s), pra
responder duas dúvidas antes de escalar: custo e sobrevivência da legenda. Entregável em
`projects/300-prompts-hot/paid/criativos/esteira-2026-08-20-fr/_teste-video-ltx-2026-08-22/`.

## O que a fonte diz

- **Custo:** $0,10/vídeo. 70 criativos = ~$7. Não é barreira.
- **Legenda:** sobreviveu em **3/3**, nítida e inalterada até o último frame — incluindo o selo
  laranja com texto. → [[animar-estatico-preservando-legenda]]
- **Armadilha:** o modelo faz push-in mesmo com "locked-off camera, no zoom" no prompt; num dos
  testes os pés da modelo saíram do quadro. Conferir o último frame, não o primeiro.
- **Formato:** sai 832×1024 (0,8125), precisa crop+scale pra 1080×1350 (4:5).
- **Áudio:** gerado, mas silêncio digital (−90 dB).
- Testados: `fr2008-v36-flash-couch-tee`, `fr2008-v30-catwoman-latex-1`,
  `fr2008-v56-pink-bikini-pool` — os dois primeiros são as artes que pontuaram em ES em 20/08.
- ⚠️ Não responde se vídeo converte mais que estático — isso é leilão, não geração.

## Páginas geradas

[[animar-estatico-preservando-legenda]]
