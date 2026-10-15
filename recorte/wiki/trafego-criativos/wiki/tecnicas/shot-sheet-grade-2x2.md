---
tipo: tecnica
tags: [storyboard, shot-sheet, video-ia, seedance, animacao-3d]
fontes: [[fonte-formato-drama-song-vsl-2026-09-28]]
---

# Shot sheet em grade 2×2

Uma imagem dividida em 4 quadros, cada um um momento sequencial do mesmo plano, usada como storyboard pro modelo de vídeo em vez de uma imagem única.

## Como montar o prompt
1. Planejar pelo [[mapa-de-tempo-por-whisper]]: cada sheet cobre as linhas cantadas no seu chunk.
2. **Descrever o cenário uma vez**; depois, para cada um dos 4 quadros, **posição da câmera + uma ação**.
3. Anexar a [[ficha-de-personagem-4-vistas]] de todos em cena (+ imagem do produto quando ele aparece).
4. **Gerar 1 sheet e conferir antes do resto.**

## Riscos
- A grade pode vazar pro vídeo (flash do sheet no 1º frame). Mitigação no prompt de vídeo ([[seedance-anima-shot-sheet]]) e na edição (aparar o início de cada clipe).
- Reusar o cenário do beat de humilhação no de vindicação: [[vindicacao-no-lugar-da-humilhacao]].

## Conecta com
- [[formato-drama-song-vsl]] · [[kling-3-fala-o-roteiro]] (outra forma de dirigir o modelo de vídeo)
