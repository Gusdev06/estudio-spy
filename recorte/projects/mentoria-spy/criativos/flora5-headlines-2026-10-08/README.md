# Flora var5: 5 headlines novas · 2026-10-08 → peças 194–198

Pedido do Gusta: "faça mais 25 variações dos campeões, mas só mudando headlines e textos no vídeo". Esta pasta tem a parte da Flora var5, com 5 peças. Custo US$ 0 (só ffmpeg, PIL e numpy).

Base: `CRIATIVOS-PRONTOS/variacoes-2026-09-25/flora-959352790554428-2026-09-25/var5-flora-959352790554428.mp4`. Ela tem 360×640, 30 fps, 1026 frames e 34,2 s, com o título "HOW TO READ YOUR PARTNER'S MESSAGES ON YOUR PHONE".

## Molde
`molde/headlines.py` é cópia da receita das h1–h5 de 27/09 (`centerpag-detect/criativos/var5-flora-959352790554428-2026-09-25/headlines.py`). Só mudam a lista de headlines e os caminhos.
- **Faixa de cima (y 0–167):** é redesenhada inteira sobre preto limpo. As pílulas brancas são unidas, com Montserrat 700 preta, caixa-alta ≤ 17 px, passo de 31 px e centro em y 95,5. O destaque usa o roxo do karaokê. Nada é colado por cima do título antigo.
- **Clarão laranja (n 263–270, 282–284, 618–619, 719–721, 747):** o laranja é lido no fundo fora da pílula antiga e interpolado por linha. A pílula nova entra por cima, como no original.
- **Resto do quadro (y ≥ 168):** janela, karaokê e painéis vêm frame a frame da var5. Os painéis do funil ficam só dentro da janela, e o título aparece o tempo todo na mãe também.
- **Áudio:** é copiado sem recodificar.
- **Faixas renderizadas:** em `faixas/`.

| nº | arquivo | headline (**negrito** = roxo) | gatilho |
|---|---|---|---|
| 194 | `pecas/194-ZAP-flora-quando-nao-olha.mp4` | WHAT THEIR WHATSAPP / SAYS WHEN YOU'RE / **NOT LOOKING** | curiosidade |
| 195 | `pecas/195-ZAP-flora-digitei-numero.mp4` | I TYPED THEIR NUMBER / AND SAW **EVERY** CHAT / ON MY OWN PHONE | prova do cotidiano ("just the number?") |
| 196 | `pecas/196-ZAP-flora-com-quem-fala.mp4` | WHO IS YOUR PARTNER / **REALLY** TEXTING / ON WHATSAPP? | pergunta |
| 197 | `pecas/197-ZAP-flora-poucos-segundos.mp4` | THEIR WHATSAPP CHATS / ON YOUR PHONE IN / A FEW **SECONDS** | tempo ("wait a few seconds") |
| 198 | `pecas/198-ZAP-flora-arquivadas.mp4` | EVEN THE **ARCHIVED** / AND REMOVED CHATS / SHOW UP FOR YOU | apagadas ("archived, received and removed") |

## Conferência
Feita com `molde/conferir.py`. O resultado está em `conferencia/conferencia.txt`, com as folhas `final-5.jpg` e `titulos-zoom.png`.
- **Decodificação:** as 5 decodificam inteiras com `-xerror`.
- **Formato:** 360×640, 30 fps, 1026 frames e 34,206 s, igual à mãe.
- **Áudio:** md5 do stream igual ao da mãe (`56739afc…`).
- **y ≥ 168 contra a mãe:** diferença média de 1,31 e máxima de 1,84 por frame, ou seja, só compressão.
- **Título:** a pílula nova fica em y 47–143 e x 25–334, sem encostar na borda nem na janela.
- **Resto do título antigo:** onde era a pílula antiga e não é a nova, o brilho máximo é ≤ 2. Fica preto, sem sobra.
- **Faixa de título:** só varia nos frames do clarão, como na mãe.

## Defeitos conhecidos
- O tamanho da fonte do título varia entre as peças. A caixa-alta vai de 15,2 px (197) a 17 px (198), porque o script reduz a fonte até a linha mais longa caber em 292 px. As h1–h5 tinham o mesmo comportamento.
- No clarão, o laranja interpolado ao redor da pílula tem um leve bandeado horizontal, herdado da receita de 27/09. Isso dura menos de 0,5 s.
