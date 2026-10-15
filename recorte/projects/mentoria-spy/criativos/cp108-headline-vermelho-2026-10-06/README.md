# CP108: 5 headlines com fundo vermelho (06/10/2026)

**Pedido do Gusta:** "faça variações desse criativo trocando a headline e deixando com fundo vermelho, quero 5".
**Origem:** `SUBIR-ESCALA-2026-09-30/conta-1/108-ZAP-podcast-wpp-copy-nova-branca-ruiva-x-negra-afro.mp4` (copiado em `REFERENCIA-108.mp4`), 720×1280, 30 fps, 1470 frames, 49 s.

## Molde medido na 108
- Caixa da headline: (246,246,246), x 17–703, y 139–271, raio ~22. Texto em Montserrat ExtraBold preto, 2 linhas centradas em y 182 e 227, corpo 34.
- Janela de vídeo: 720×587 em y 346. Karaokê em y 935.
- A partir de 33,61 s o CTA ocupa o quadro inteiro.

## Como é montada
`montar.py` refaz cada frame: fundo vermelho #C8101E, caixa da headline redesenhada (`titulos/vN.png`) e janela recortada da 108. O karaokê vem dos PNGs RGBA do lote `centerpag-detect/criativos/podcast-wpp-57s-copy-nova-2026-09-23/karaoke/` (conferido contra a 108: diferença média de 2,5 a 4,5 níveis, só compressão). O contorno preto do karaokê, que era invisível no preto, agora aparece no vermelho. O CTA é o da 108, e o áudio é copiado (md5 do stream idêntico nas 5).

## Peças → CRIATIVOS-PRONTOS 159–163
| peça | headline |
|---|---|
| v1 | HOW TO SEE WHO YOUR / PARTNER IS REALLY TEXTING |
| v2 | HOW TO RECOVER YOUR PARTNER'S / DELETED MESSAGES |
| v3 | READ YOUR PARTNER'S WHATSAPP / WITHOUT TOUCHING THEIR PHONE |
| v4 | SEE WHAT YOUR PARTNER DELETES / BEFORE YOU WAKE UP |
| v5 | THE TRUTH IS IN THE CHATS / YOUR PARTNER DELETED |

Custo: US$ 0,00 (ffmpeg/PIL local). Conferência: `conferencia/lado-a-lado.jpg` e `conferencia/v2-folha.jpg`.
