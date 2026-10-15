---
tipo: tecnica
tags: [enquadramento, medicao, avatar, L9, spy-gram, casting, pruna, gpt-image-2]
fontes: [[fonte-casting-gram01-var-avatar-5-rostos-2026-09-11]]
---

# Enquadramento do head L9 pra avatar gerado — meça os olhos no controle, converta pro 9:16

Pra trocar só o rosto num split L9, a imagem-base tem que nascer com os olhos no lugar que o **recorte** vai exigir — e o lugar se mede no controle sobre dezenas de frames, não num poster.

## O que foi medido (controle `gram01-l9-en-01-v2`, 11/09)

`VNDetectFaceLandmarksRequest` (Vision, macOS) em 63 frames do `head-panel.mp4` a 2 fps e 12 da
cauda a 10 fps. O detector funciona sem instalar nada; script de 40 linhas em Swift.

| Bloco | Olhos (y) | Largura do rosto | Queixo | Observação |
|---|---|---|---|---|
| Head 1170×1212 | **47,3 %** mediana (p25–p75 43,9–49,1; min–max 37,7–58,6) | **47,9 %** da largura (560 px) | 87 % | cabeça e ombros, ombros cortados nas laterais; 13 % abaixo do queixo |
| Cauda 1170×2532 | **44,2 %** (1117 px) | 48,5 % (567 px) | 63,5 % | mesma escala do head, rosto 545 px mais baixo |

A cabeça **passeia** (nariz entre 35 % e 76 % da largura em 31 s): o que se casa é a **mediana**
(posição de repouso), não um frame.

## A conversão

O gerador de talking head devolve 9:16 (Pruna: 704×1280). O head sai **recortando o topo** até a
proporção do bloco: 704×730, fator vertical **730/1280 = 0,570**.

```
olhos_9:16  = olhos_head × 0,570      → 47,3 % × 0,570 = 27,0 %  (345 px de 1280)
queixo_9:16 = 87 % × 0,570            → 49,6 %  (queixo no meio do quadro)
largura do rosto: mesmo % (o recorte não mexe em x) → 48 % de 704 = 337 px
faixa aceitável (p25–p75 do controle): 25–28 %
```

Isso vai **literal no prompt** ("eyes about 27 percent from the top, chin near the middle of the
frame, face about half the frame width") — no padrão de prompt da casa, que já escrevia "eyes
around 37 percent" no wpp-01. O número muda por molde; a conta não.

## As duas armadilhas

1. **A cauda pede outra geometria.** O rosto em quadro cheio do controle está 545 px mais baixo que no
   head, mesma escala. Escalar o clipe pela largura e descer 544 px reproduz isso, mas deixa 544 px de
   topo pra preencher; escalar pela altura não precisa de preenchimento, mas põe os olhos a 27 % e o
   rosto 57 % de largura (vs 44 % / 48,5 %). Escolha de montagem, decidida **antes** de gerar.
2. **Proporção da imagem-base.** Se o gerador de imagem devolver 2:3 em vez de 9:16, os % acima não
   valem até recortar pra 9:16.

## Precedentes na casa

- Variação D do GD-AD01 (03/09): o clipe veio com olhos a ~28 % e o campeão pedia ~35–37 % → zoom
  1,25× + recorte pelo topo. Se o prompt tivesse pedido a posição certa, o zoom (e a perda de nitidez)
  não existiria.
- Emilly (09/09): rosto do avatar 410 px contra ~300 do original — a largura do rosto também é
  número de prompt, não só a altura dos olhos.

## Conecta com

- [[lote-gram01-l9-var-avatar-5-rostos]] — onde a conta é usada
- [[medir-fronteira-de-bloco-em-video]] — a mesma regra ("meça, não herde") pra fronteira de bloco
- [[spec-de-edicao-layouts-spy]] — as medidas do L9 que definem o recorte
- [[peca-pronta-nao-e-banco-de-atores]] — a outra conta de encaixe (faixa limpa × altura do molde)
- [[frame-1-sem-piscar]] — a imagem-base é o frame 1: olhos abertos, boca fechada
