---
tipo: fonte
tags: [spy-zap, lote-4, locucao, montagem, karaoke, medicao]
fontes: []
---

# Fonte — produção do lote 4 spy-zap (2026-09-01)

Montagem das 4 peças do grid de atores. Rendeu três achados de método que corrigem
réguas que a esteira usava havia dois lotes.

- Cru: `raw/2026-09-01-lote4-metodo-vo-e-karaoke.md`
- Peças: `projects/mentoria-spy/centerpag-detect/criativos/lote4-grid-atores-2026-09-01/pecas/`

## O que gerou

- [[padding-de-silencio-no-tts]] — 25% do mp3 do TTS é silêncio; medir wpm no bruto
  reprovou 6 de 7 vozes por engano
- [[beat-posicionado-na-marca]] — o molde posiciona beat na marca da grade, não
  concatena com atempo global
- [[receita-do-karaoke-spy]] — Arial Black, tinta 81px travada, largura máx 1005px;
  não estava versionado em lugar nenhum

## O que corrigiu

- [[fit-de-locucao-por-tempo]] — os 156,9 wpm eram duração bruta; a fala roda a 213 wpm,
  e a janela de atempo 1,15–1,25 não é teste de aptidão de voz

## Notas de operação

- `sync/lipsync-2-pro` devolveu **1166, 1170 e 1172** de largura em três chamadas com a
  mesma entrada 1170×2532. Reescalonar de volta é obrigatório.
- Uma chamada falhou com `The upstream provider is temporarily unavailable` e **foi
  estornada** (duas linhas na fatura com o mesmo prediction id). Repetir sem mexer no
  input resolveu na primeira.

## Controle do lote (uma alavanca)

Medido nas 4 peças finais: tarja **100% opaca**, diferença entre slots de **0,012–0,030/255**
(ruído de H.264); janela da tarja idêntica nos **frames 438–588**; 4 `voice_id` distintos
registrados. O bloco gráfico difere 12–23/255 entre slots porque é **0,8% opaco** — o que
varia ali é o rosto atrás dele, por projeto.
