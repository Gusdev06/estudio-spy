# Três trocas de avatar (Ad Library, 19/09): Luiza Cristina 2140730963322005 · Antonia Nicole Vice 2627173801075681 · Andrew Smith 4680506465505714

Pedido: "faça variação desses trocando apenas avatar". Regra aplicada nas três: **só a região do rosto muda**; o que é camada queimada por cima do rosto é redesenhado, o resto do quadro é o original (escalado pra 1080×1920). Áudio original intacto. Avatar segue o gênero da voz (as três são voz feminina). Clipe inteiro varrido antes de montar (`varredura-todos.jpg`: 5 clipes limpos).

| peça | original | layout medido | o que foi trocado / redesenhado | avatar | custo |
|---|---|---|---|---|---|
| **68** `luiza2/` | 360×640, 26,4 s, podcast em quadro cheio (mulher de boné, mic, plantas) + caixa de legenda fixa "# A woman records video…" (y 504–577, duas caixas pretas) | quadro inteiro = avatar novo (Pruna 704×1280) com **look 360p** (passa por 360×640 e volta + ruído 6) — o original é 360p; caixa redesenhada em PIL (×3) | negra ~30, box braids, sem boné, camisa branca, mesmo set | 0,07 + 0,68 |
| **69** `antonia/` | 720×1280, **367 s** (fala até 38 s; depois b-roll CTA, contagem e card estático até o fim), layout de post: caixa branca de hook + **janela 16:9 do estúdio de rádio** (y 430–849) + karaokê rosa | só a janela nos 38 s de fala: avatar 16:9 (Pruna 1280×704), clipes p1 0–20,7 s + p2 20,7–38 s emendados no fim de frase; resto do quadro original ×1,5 (hook, karaokê, b-roll, card) | mulher ~32 pele morena clara, cabelo ondulado, top preto, **estúdio sem logos** (o original mostra SiriusXM) | 0,07 + 0,98 |
| **70** `andrew/` | 720×1280, 56,8 s: citação branca no topo, **janela 720×584 (y 352–936)** com clipe de estoque (mulher de vermelho, luzes), **lower third azul 0,4–3,0 s**, faixa vermelha de CTA; cutaways do app em quadro cheio 14,4–33,4 s; card final | janela nos dois blocos de rosto (0,2–14,4 · 33,4–53,6 s): avatar 16:9 em 2 clipes; **lower third redesenhado** (azul (3,65,165) y 754–909, barras vermelhas, Montserrat ExtraBold branco cortado nas bordas como o original); cutaways e card originais | negra ~35, cabelo curto natural, suéter verde, mesmas luzes de fundo | 0,07 + 0,90 |

**Custo real do lote: US$ 2,75.** Scripts: `<peça>/montar.py` (+ `molde/*.png` das camadas redesenhadas). Conferência: `<peça>/conferencia/orig-x-novo.jpg`.

Achado: o Pruna aceita bem clipes de até ~27 s; acima de ~40 s recusou (67). Partir o áudio na fronteira de frase/bloco e emendar os clipes da mesma imagem funcionou nas 3 (a emenda cai num corte do próprio criativo ou num fim de frase).

## 21/09 — 5 variações da 68 (`luiza2/var5/`) → peças 101–105
Latina (blusa preta), asiática (bob, camisa branca), loira (camisa jeans), indiana (blusa verde), negra afro curto (camisa branca). Mesmo pipeline da 68 (edit sobre o frame + Pruna com o áudio original + look 360p + caixa redesenhada), com o prompt de **identidade travada** (lição do lote podcast); `checar-identidade.py` ok nas 5 (×1,02–1,03), varredura limpa. Custo ≈ US$ 3,75.
