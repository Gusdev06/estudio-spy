---
tipo: tecnica
tags: [criativo, localizacao, idioma, value-stack, escala-geografica, seedream]
fontes: [[fonte-campeoes-imagem-fr-2026-08-17]]
---

# Localização de value stack

Levar um criativo campeão pra outro idioma trocando **só o bloco de texto** da imagem,
via image-to-image — a foto, o enquadramento e o [[value-stack-no-overlay]] ficam
idênticos. É como a [[oferta-300-prompts]] abre mercado novo sem produzir arte do zero.

## O que muda e o que NÃO muda

Comparando as versões EN × ES × FR que rodam da mesma arte, quase tudo é invariante:

| | EN | ES | FR |
|---|---|---|---|
| linha 1 | `+300 PROMPTS` | `+300 PROMPTS` | `+300 PROMPTS` |
| linha 2 | `Onl* F and F*anvue` | `Onl* F y F*anvue` | `Onl* F et F*anvue` |
| linha 3 (barra laranja) | `HYPER-REALISTIC AI` | `HYPER-REALISTIC AI` | `HYPER-REALISTIC AI` |
| linha 4 | `JUST $ 6,99` | `SOLO $ 6,99` | `SEULEMENT 6,99 €` |

Só mudam **a conjunção** e **o advérbio de preço**. `+300 PROMPTS` e `HYPER-REALISTIC AI`
ficam em inglês nos três — são reconhecíveis e não vale gastar tradução neles. A
[[censura-plataforma-asterisco]] (`Onl* F`) é preservada em todo idioma.

## A moeda tem que bater com o checkout

O preço no criativo precisa casar com o que o checkout daquele idioma cobra. FR usa
`6,99 €` porque o checkout FR (`PPU38CQFCDI`) é um produto em EUR. Anunciar `$ 6,99` e
cobrar em euro (ou o contrário) é o mesmo tipo de furo que matou a `/in` — ver
[[oferta-300-prompts]].

## Gotcha: o modelo preserva a conjunção do original

Gerando com Seedream edit, pedir "traduza o texto para francês" **não é suficiente** — o
modelo troca as palavras longas e mantém a conjunção curta do original (`and` / `y`
sobrevivem intactos). 2 de 4 imagens saíram erradas assim na 1ª rodada de 17/08.

Instrução que funciona: **cite a palavra atual e a substituta, explicitamente.**

> CRITICAL: the second line currently reads "Onl* F and F*anvue" — you MUST replace the
> middle word with the FRENCH word "et". Do not leave "and". Do not leave "y".

Sempre faça QA visual palavra a palavra antes de subir. Vale pra qualquer idioma novo.

## Fadiga não atravessa fronteira

Criativo fadigado no público EN não chega fadigado no público FR — fadiga é
**frequência acumulada no público que já viu**. Então dá pra localizar uma arte que já
está caindo em casa, desde que ela tenha histórico real de conversão. Ver
[[criativo-campeao-52515797525534]], que caiu pra ROAS 1,35 em EN mas serve de base FR.

Relacionadas: [[variar-uma-alavanca-por-vez]], [[throughput-de-criativo]], [[believability-reveal]].
