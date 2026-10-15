---
tipo: fonte
tags: [fonte, campeoes, imagem, fr, localizacao, meta-ads]
data: 2026-08-17
---

# Fonte — Campeões-imagem e localização FR (17/08/2026)

Levantamento ad-level das **6 campanhas ativas** (3 contas) pra achar os criativos-imagem
campeões, e a geração das versões em francês pra abrir o mercado FR.
Cru: `raw/2026-08-17-campeoes-imagem-e-localizacao-fr.md`

## Método

Insights ad-level 30d (18/07–16/08) via Meta Ads MCP: 172 ads (CA-DZD) + 44 (BM-LATAM) +
14 (SAUDE 60+). Filtro `object_type` separou imagem de vídeo — **3 dos 12 finalistas eram
VIDEO** e foram descartados. Ranking por receita (gasto × ROAS), deduplicado por arte.
Geração: WaveSpeed `bytedance/seedream-v5.0-pro/edit`, 4:5, 2k, ~$0,045/img.

## Números (não inventados — Meta Ads, 2 janelas)

| Ad | Arte | Gasto 30d | Vd | ROAS 30d | ROAS 7d |
|---|---|---|---|---|---|
| `52515797525534` | morena cama | R$ 2.830 | 112 | 2,06 | 1,35 |
| `120248299074630685` | jatinho | R$ 698 | 56 | 3,15 | **3,31** |
| `52537188658334` | praia loira EN | R$ 596 | 23 | 1,92 | sem entrega |
| `120248136187530685` | estádio | R$ 350 | 29 | 2,92 | sem entrega |

Reserva não localizada: `120248136187480685` ruiva (ROAS 4,10), `52537191396734` antiban
(2,61), `52537191401534` student-proof (2,05).

## Divergência registrada

O `52515797525534` aparece como **maior receita acumulada em 30d** (112 vendas) mas está
com **ROAS 1,35 em 7d** — coerente com a fadiga que [[criativo-campeao-52515797525534]]
já registrava desde 31/jul. Não é contradição de dado: são **janelas diferentes**
medindo coisas diferentes (acumulado × entrega atual). Regra derivada: ao escolher
campeão pra variar, ler **as duas janelas** — 30d diz o que já provou, 7d diz o que ainda
entrega.

## Páginas geradas

- [[localizacao-de-value-stack]] — a técnica (o que traduz, o que não, e o gotcha do modelo)
- [[campanha-cbo-fr-17-08]] — a campanha francesa criada
- Atualizada: [[criativo-campeao-52515797525534]] (leitura de 7d + uso como base FR)
