# Criativos FR — campeões-imagem localizados (2026-08-17)

Variações em **francês** dos criativos-imagem campeões, geradas image-to-image a partir
das artes reais que estão rodando. Destino: campanha `CBO FR 17/08` / conjunto
`FR - 4 criativos (lowest cost)` (conta CA - DZD).

## Método

Levantamento de performance **ad-level, últimos 30 dias (18/07–16/08)** nas **6 campanhas
ativas** das 3 contas (CA-DZD, BM-LATAM, CA-SAUDE 60+) → 172 + 44 + 14 anúncios.
Filtrado `object_type` para separar imagem de vídeo (3 dos 12 finalistas eram VIDEO).
Ranking por **receita** (gasto × ROAS), deduplicado por arte.

Geração: **WaveSpeed `bytedance/seedream-v5.0-pro/edit`** (image-to-image, 4:5, 2k, ~$0,045/img).
GPT Image 2 pulado — recusa esse conteúdo (regra em `gerar-criativo-imagem`).
Texto **embutido no prompt de geração**, sem overlay (regra travada).

## Os 4 escolhidos

| Arquivo | Ad de origem | Campanha | Gasto 30d | Vendas | ROAS | Receita |
|---|---|---|---|---|---|---|
| `fr-v1-campeao-morena.jpg` | `52515797525534` | HOTM - BIDCAP — EN | R$ 2.830 | 112 | 2,06 | ~R$ 5.830 |
| `fr-v2-jatinho.jpg` | `120248299074630685` | BIDCAP EN 13/07 (LATAM) | R$ 698 | 56 | 3,15 | ~R$ 2.202 |
| `fr-v3-praia-loira.jpg` | `52537188658334` | HOTM - BIDCAP — EN | R$ 596 | 23 | 1,92 | ~R$ 1.145 |
| `fr-v4-estadio.jpg` | `120248136187530685` | BIDCAP EN 13/07 (LATAM) | R$ 350 | 29 | 2,92 | ~R$ 1.022 |

Originais em `originais/` (baixados do CDN da Meta).

## Value stack traduzido

Padrão extraído comparando as versões EN × ES que já rodam — só mudam a conjunção e o
advérbio de preço; `+300 PROMPTS` e `HYPER-REALISTIC AI` ficam em inglês nos três idiomas.

| | EN | ES | **FR** |
|---|---|---|---|
| linha 1 | `+300 PROMPTS` | `+300 PROMPTS` | `+300 PROMPTS` |
| linha 2 | `Onl* F and F*anvue` | `Onl* F y F*anvue` | `Onl* F et F*anvue` |
| linha 3 (barra laranja) | `HYPER-REALISTIC AI` | `HYPER-REALISTIC AI` | `HYPER-REALISTIC AI` |
| linha 4 | `JUST $ 6,99` | `SOLO $ 6,99` | `SEULEMENT 6,99 €` |

Preço em **euro**, batendo com o checkout FR (`PPU38CQFCDI` = 6,99 EUR).
`fr-v4-estadio` não tem linha de preço — o original também não tinha.

## QA

Conferidas as 4 uma a uma. `v2` e `v4` saíram na 1ª rodada com a conjunção errada
(manteve `and` / `y`); regeradas com instrução explícita de substituição. Aprovadas.

**Gotcha pra próxima:** o Seedream troca o idioma do bloco de texto mas tende a **preservar
a conjunção curta do original**. Sempre citar a palavra atual e a substituta no prompt
("replace `and` with the French `et`"), não só "traduza para francês".

## Reserva

`originais/c5-ruiva.jpg` (ROAS 4,10), `c6-student-proof.jpg` (2,05), `c7-antiban.jpg` (2,61) —
campeões-imagem menores, ainda não localizados. Servem pra 2ª leva se o FR pegar.
