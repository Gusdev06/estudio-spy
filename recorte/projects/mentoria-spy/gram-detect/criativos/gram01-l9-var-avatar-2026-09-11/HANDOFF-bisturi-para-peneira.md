# HANDOFF · Bisturi → Peneira · 2026-09-11 · lote gram01-l9-var-avatar

Não é erro no casting — é a decisão de montagem que a seção 2 do casting deixou comigo, com a
medição que a sustenta. Os 5 prompts entraram **literais** exceto a frase "Framing: …", que
troquei pelos números abaixo (`base/avatar-avN-prompt.txt`; diff = só essa frase).

## O que medi (Haar, OpenCV 4.14 — caixa, não contorno; 12 frames)

| | olhos (y) | caixa Haar (largura) | queixo |
|---|---|---|---|
| head panel (7 fr) | mediana **47,4 %** (43–60) | 61–65 % da largura | ~86 % |
| cauda (5 fr) | **44,2 %** (43–45) | 58–66 % | 61–63 % |

Bate com os seus (olhos 47,3 % / 44,2 %; sua largura 47,9 % é contorno — Haar dá ~1,3× isso).

## A decisão: olhos a 44 % da imagem 9:16, não 27 %

Com os olhos a **44 %** (563 px de 1280) e o recorte do head começando em **OY = 220**
(`crop=704:730:0:220` → ×1,662), os olhos caem em (563−220)/730 = **47 %** do head — igual ao
controle — e a **cauda** sai de `crop=592:1280:56:0` → ×1,977 com olhos em **44 %** e queixo em
~62 %, **sem preencher topo nenhum**. Sua opção "escalar pela largura + descer 544 px" exigia 544 px
de fundo sintético em cima; a "escalar pela altura" deixava os olhos em 27 % na cauda. Esta troca
casa olhos e queixo nos dois blocos; o único desvio é a largura do rosto na cauda: 48 % × 1,977/1,662
= **57 %** (controle 48,5 %) por 1,17 s. Aceito.

Consequência pros seus critérios de aceite da imagem (seção 2 → "o que o Bisturi confere"):
olhos **42–46 %** (alvo 44), queixo **58–66 %**, topo da cabeça **≥ 15 % de folga**, largura do
rosto igual à sua (44–51 % contorno / ~57–66 % Haar). O OY é medido por imagem (OY = olhos − 343),
não fixo — fica no README.

Nomes: `pecas/gram01-l9-en-01-av1-branca-25-quarto.mp4` … (av = avatar; `V2` colidia com o `v2`
do controle no APFS). Imagens em `base/avatar-avN.png`, slugs seus em `base/slugs.tsv`.
