# Spy Gram — variações em IMAGEM do "I found what he's hiding on Instagram" (2026-10-11)

Primeiro teste de criativo em imagem da oferta (a esteira-spy só faz vídeo).
Ref: `ref/original.jpeg` (enviada pelo Gusta no WhatsApp). Ainda sem dado de performance da ref.

Modelo: `openai/gpt-image-2/edit` (WaveSpeed), quality=high, 1k, 4:5, image-to-image da ref.
Custo real: US$ 2,19 pelas 10 (saldo 21,21 → 19,02). Prompts exatos em `prompts.tsv`, inputs em `out/*.input.json`.

Cada peça mexe em UMA alavanca:

| Peça | Alavanca | O que mudou |
|---|---|---|
| v01 / v02 / v03 | mulher/etnia | loira americana · negra · latina |
| v04 | headline | HE SAID HE WAS AT WORK. HIS INSTAGRAM SAID OTHERWISE. |
| v05 | headline | HIS DMs TOLD ME EVERYTHING HE HID. |
| v06 | headline | I SAW WHO HE TEXTS AT 1 AM ON INSTAGRAM. |
| v07 / v08 | cena | carro à noite · chão do banheiro |
| v09 / v10 | expressão | raiva olhando pra câmera · chorando |

Conferido a olho: texto saiu certo em todas as 10, sem erro de grafia.
Tamanhos: 4 saíram em 1024×1280 e 6 em 912×1152 (todos ~4:5).
