---
tipo: conceito
tags: [checkout, cro, gateway, cartao, gargalo, dinheiro-na-mesa]
fontes: [[fonte-comparativo-mensal-jul-ago-2026-08-22]]
---

# Recusa de cartão como gargalo

A maior alavanca de faturamento da operação **não está no leilão, está no gateway**: 1 em cada
4 tentativas de cartão é recusada. É gente que já clicou em comprar e não conseguiu — custo de
mídia já pago, receita zero.

## Série histórica (UTMify, dashboard Principal)

| Período | Tentativas | Aprovadas | Recusadas | **Taxa** |
|---|---|---|---|---|
| 12–18/jul/2026 | 305 | 234 | 71 | 23,3% |
| Jul 1–22 | 1.521 | 1.081 | 333 | 21,9% |
| **Ago 1–22** | 1.095 | 751 | **275** | **25,1%** |

Está **piorando** (+3,2 p.p. no mês).

## Quanto custa

275 pedidos recusados em 22 dias × ticket médio R$ 66,19 ≈ **R$ 18,2 mil de bruto barrado**.
Recuperar metade ≈ **+R$ 9 mil/mês sem gastar R$ 1 a mais em mídia** — mais do que qualquer
ganho realista de otimização de criativo no mesmo período.

## Por que o pixel não mostra

O Meta não distingue "recusado" de "desistiu": os dois aparecem como initiate checkout sem
purchase. Por isso a recusa se manifesta como [[colapso-de-ic-para-compra]] e é fácil culpar
o criativo por engano.

## O que testar (não verificado ainda)

- **2ª tentativa automática** no cartão recusado
- **PIX/carteira em destaque** — na operação o PIX é só ~4% da receita mas tem ~90% de
  aprovação contra ~71% do cartão
- **Recusa por país** — checar se concentra em mercados de baixa aprovação (a operação vende
  pra EUA, México, Índia, Espanha, Itália…)

Relacionado: [[colapso-de-ic-para-compra]], [[oferta-300-prompts]].
