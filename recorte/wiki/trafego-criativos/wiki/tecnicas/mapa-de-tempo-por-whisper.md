---
tipo: tecnica
tags: [whisper, transcricao, edicao, song-vsl, timing]
fontes: [[fonte-formato-drama-song-vsl-2026-09-28]]
---

# Mapa de tempo por Whisper

Lista de cada linha da música com segundo de início e fim, feita com Whisper local em timestamps por palavra — tempos do Whisper, palavras da letra.

## Como
- Rodar Whisper local com `word_timestamps` na música final.
- **Whisper erra palavra cantada**: alinhar os tempos dele com o texto da [[letra-cantada-como-roteiro]], nunca usar a transcrição como texto.
- O mapa decide os **chunks**: quais linhas cada clipe cobre e quanto ele dura (8 s um, 14 s outro). Duração de clipe nunca é número fixo ([[seedance-anima-shot-sheet]]).
- Na edição, cada clipe é cortado no slot exato do mapa.

## Cuidado da casa
Medir silêncio/tempo com `-hide_banner`, nunca `-v error` (engole o `silencedetect`). Relacionado: [[padding-de-silencio-no-tts]], [[beat-posicionado-na-marca]] — mesma ideia de posicionar por marca em vez de esticar.

## Conecta com
- [[formato-drama-song-vsl]] · [[shot-sheet-grade-2x2]]
