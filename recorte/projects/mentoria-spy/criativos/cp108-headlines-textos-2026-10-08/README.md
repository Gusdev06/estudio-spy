# CP108: 5 headlines novas, fundo preto (08/10/2026) → peças 189–193

**Pedido do Gusta:** "faça mais 25 variações dos campeões, mas só mudando headlines e textos no vídeo". Esta pasta é a parte do CP108 (5 peças).
**Mãe:** `CRIATIVOS-PRONTOS/108-ZAP-podcast-wpp-copy-nova-branca-ruiva-x-negra-afro.mp4` (720×1280, 30 fps, 1470 frames, 49 s). Atenção: o `REFERENCIA-108.mp4` do lote de 06/10 não é o mesmo arquivo (md5 de áudio e vídeo diferentes); aqui a base é a de CRIATIVOS-PRONTOS.

## Molde medido na 108
- Faixa de cima (y 0–345) é estática do frame 0 ao 1008 (diferença ≤ 11 níveis, só compressão): preto puro + caixa (244,244,244 decodificado) x 17–703, y 139–271, raio ~22.
- Texto: Montserrat ExtraBold, corpo 35 (larguras 610/638 px contra 613/641 do original), 2 linhas centradas em y 182 e 227. Encolhe só se uma linha passar de 650 px (só a 191 foi a 34).
- O CTA em quadro cheio começa no frame 1009 (33,633 s).

## Como é montada (`montar.py`)
A faixa inteira (preto + caixa + headline nova, opaca, `titulos/<nº>.png`) é redesenhada e cobre y 0–345 nos frames 0–1008. Janela (y 346), karaokê (y 935) e CTA são os da própria 108. Áudio copiado. Metadados limpos. Custo: US$ 0,00 (ffmpeg/PIL).

| nº | gatilho | headline |
|---|---|---|
| 189 | curiosidade | THE CHATS YOUR PARTNER / NEVER WANTED YOU TO SEE |
| 190 | prova | I TYPED HIS NUMBER / AND SAW EVERY CHAT |
| 191 | pergunta | WHAT DOES YOUR PARTNER SEND / AT 2 IN THE MORNING? |
| 192 | tempo | ALL YOUR PARTNER'S CHATS / ON YOUR PHONE IN 60 SECONDS |
| 193 | apagadas | YOUR PARTNER'S DELETED CHATS / ARE STILL THERE TO READ |

## CTA: não trocado
O texto amarelo "CLICK THE LINK BELOW / AND SEE THE TRUTH NOW." está queimado no b-roll do criativo da Ad Library (`centerpag-detect/.../podcast-wpp-57s-copy-nova-2026-09-23/REFERENCIA-original.mp4`, 41,4–56,8 s) e muda de posição no meio. Não existe no disco versão limpa desse b-roll (procurei nos lotes podcast-wpp de 13/09, 23/09 e 07/10, e nos moldes de CTA da emilly, ad02-h2 e super-zap: todos usam CTA queimado ou outro b-roll). Pela regra do pedido, só as headlines mudaram. Textos de CTA propostos para quando houver um b-roll limpo: 189 TAP THE LINK BELOW / AND READ THE CHATS YOURSELF · 190 TYPE THE NUMBER BELOW / AND SEE IT WITH YOUR OWN EYES · 191 TAP BELOW / AND FIND OUT TONIGHT · 192 TAP THE LINK BELOW / IT TAKES 60 SECONDS · 193 TAP THE LINK BELOW / AND SEE WHAT WAS DELETED.

## Conferência (`conferir.py`, decodifica tudo)
- As 5: decodificam inteiras sem erro, 720×1280, 30 fps, 1470 frames, 49,0 s. md5 do stream de áudio igual ao da 108 (`fea5ec0d…`).
- Janela + karaokê (y 346–1279, frames 0–1008): diferença média de 0,50 nível contra a 108 (máx. 0,81), ou seja, só recompressão. CTA (frames 1009–1469): média de 0,43 (máx. 0,79).
- Faixa de cima contra o PNG redesenhado: média de 0,75 (máx. 0,83) em todos os frames 0–1008. Nada do título antigo aparece.
- `conferencia/final-5.jpg`: topo (frame 150) e CTA (frame 1100) de cada peça.
