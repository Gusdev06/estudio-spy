# Secret Revealed — mais 3 avatares indianos · 2026-09-13

Pedido do Gusta: "faça variações desse priorizando indianos também, quero 3 variações", sobre a peça `CRIATIVOS-PRONTOS/23-ZAP-secret-revealed-v4-homem-indiano.mp4`.

A 23 já era o único indiano do lote de 10/09 (`../zap-secret-revealed-avatar-2026-09-10/var4`). Este lote acrescenta **mais três**, todos indianos e distintos entre si e da 23, no mesmo molde: rosto cheio, faixa vermelha recortada do original, karaokê de 1 palavra, áudio original. **Só o rosto muda.**

| peça | id | avatar | arquivo |
|---|---|---|---|
| **47** | i1 | indiano ~27, cabelo preto volumoso, **sem barba**, camiseta azul-clara | `pecas/zap-secret-revealed-i1-indiano-jovem-sem-barba.mp4` |
| **48** | i2 | indiano ~42, **grisalho**, barba grisalha aparada, óculos de armação grossa, camiseta cinza-escura | `pecas/zap-secret-revealed-i2-indiano-grisalho-oculos.mp4` |
| **49** | i3 | indiano ~34, cabelo com risca lateral, **bigode sem barba**, camiseta bordô | `pecas/zap-secret-revealed-i3-indiano-bigode.mp4` |

Para comparação, a 23 (já existente) é um indiano ~30 de barba aparada e camiseta verde-oliva. As quatro cobrem faixas de idade e de pelo facial diferentes: sem barba, bigode, barba curta e grisalho de óculos.

Todas: 1080×1920 · 30 fps · 971 frames · **32,37 s** · áudio original · 0 silêncios ≥ 0,4 s.

## Como foi feito (molde reaproveitado, nada reinventado)

O pipeline já existia no lote de 10/09 e foi usado sem alteração:

1. **Imagem-base** — `openai/gpt-image-2/text-to-image`, **quality medium**, com o mesmo prompt-molde da `var4/base/v4.json`: webcam frontal, home office claro, cadeira branca estofada, luz de janela levemente estourada, enquadramento peito pra cima com olhos a ~35 % do topo. Só a descrição da pessoa muda (`casting.tsv`).
2. **Talking head** — `pruna-ai/p-video/avatar` 720p sobre o **áudio original inteiro** (`../zap-secret-revealed-avatar-2026-09-10/audio/audio-original.m4a`, 32,25 s) → 704×1280, 24 fps, 33,04 s.
3. **Montagem** — `montar-indianos.py <id>` chama o `remontar-secret.sh` do lote de 10/09, que já traz a faixa vermelha recortada do original (x 85–632 · y 110–262 → x 127–948 · y 165–393, com emoji) e o karaokê em Arial Rounded MT Bold 86 com tracking 7, 113 palavras do whisper. Depois confere contra o original, conta silêncios, copia pra `CRIATIVOS-PRONTOS` e escreve a linha no LEIA-ME.

## Custo real — US$ 2,65

| item | valor |
|---|---|
| 3 imagens `gpt-image-2/text-to-image` (medium) | US$ 0,171 |
| 3 clipes Pruna (32,25 s cada) | US$ 2,475 |
| montagem, conferência, cópias | US$ 0,00 |

US$ 0,88 por peça, contra US$ 0,81 do lote de 10/09 (que usou imagens já feitas) e US$ 4,66 por avatar do OmniHuman da peça 20.

## Conferência

`conferencia/avatares-indianos.jpg` (os 3 novos ao lado do avatar da 23) · `clipes-check.jpg` (os 3 talking heads inteiros, varredura contra pessoa inventada) · `<id>-folha-8-instantes.jpg` (original × peça em 0,5 · 2 · 4 · 8 · 12,2 · 20 · 25 · 30 s) · `<id>-zoom-karaoke.jpg` (3 palavras, y 1210–1360) · `resumo.tsv`.

A trava "SOLO SHOT" (aprendida no clone do podcast, 13/09) entrou no `video_prompt` dos três e nenhum clipe precisou ser regerado.

## Reproduzir

```
# 1. acrescentar a linha do elenco em casting.tsv (id, slug, descrição da pessoa)
# 2. imagem + clipe: mesmo par de chamadas do README (gpt-image-2/text-to-image medium; pruna-ai/p-video/avatar)
python3 centerpag-detect/criativos/zap-secret-revealed-indianos-2026-09-13/montar-indianos.py <id>
```
De `projects/mentoria-spy/`. `NUM` no script mapeia id → número em `CRIATIVOS-PRONTOS`.

## O que conferir no olho

- **Karaokê herdado:** o molde usa as 113 palavras do whisper, então onde o original queimou "WIVES" a nossa mostra "WIFE'S". Vem da peça 20, não deste lote.
- **Memória:** montar uma peça consome bastante RAM (971 PNGs de karaokê desenhados em PIL). Em 13/09 a montagem das três em série foi morta pelo sistema por falta de memória, com a i1 e a i2 já prontas. **Rodar uma por vez.**
