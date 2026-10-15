---
tipo: entidade
tags: [campanha, bid-cap, es, cbo, meta-ads, esteira]
fontes: [[fonte-leitura-esteira-20-08-es-2026-08-21]]
---

# Campanha — HOTM - BIDCAP — ES — ESTEIRA 20/08

CBO com R$ 6.000/dia armado que **não conseguiu gastar R$ 64 em 2 dias** por causa do bid cap de R$ 50 — caso puro de [[estrangulamento-de-entrega-por-bid-cap]].

| | |
|---|---|
| ID | `52549590537334` |
| Conta | CA - DZD (`act_2383339602144432`) |
| Criada | 2026-08-20 |
| Estrutura | CBO · OUTCOME_SALES · `LOWEST_COST_WITH_BID_CAP` · bid R$ 50 · R$ 6.000/dia |
| Conjuntos | 10 × `ESTEIRA ES 20/08 - N (bid50)`, 3 ads cada = 30 |
| Origem | clone da `HOTM - BIDCAP — ES` (`52523946982934`), conjunto `+300 UGC ES 06/08 - 1` |
| Destino | `gusta.promptsgoat.com/2` · CTA Ver detalles · pixel `1223791793200733` |

## Performance (20–21/08, dia 21 parcial)

| Gasto | Impr | CTR | CPC | CPM | LPV | IC | Compras | ROAS |
|---|---|---|---|---|---|---|---|---|
| R$ 63,96 | 932 | 13,63% | R$ 0,50 | R$ 68,63 | 94 | 10 | **0** | **0** |

Em 21/08 o `budget_remaining` marcava 598.531 de 600.000 centavos: **gastou 0,25% do budget do dia.**

## Leitura

- O CTR de 13,63% mostra que a arte **para o scroll**; o funil quebra depois (94 LPV → 10 IC → 0 compra).
- Não é teste de criativo válido: a campanha mal foi ao leilão. Ver [[estrangulamento-de-entrega-por-bid-cap]].
- ⚠️ Herda página `/2`, copy e preço da [[campanha-ca-dzd-hotm-bidcap-en|ES original]], que rodava
  ROAS 0,44. Destravar o bid aqui = liberar R$ 6.000/dia pra 30 criativos com ROAS 0,77 medido
  (ver [[campanha-abo-es-quiz-20-08]]) numa página com histórico ruim. Risco alto, evidência nenhuma a favor.
- Recomendação registrada em 2026-08-21: **pausar**, não subir o bid.

Relacionado: [[bid-cap]] · [[folga-de-bid]] · [[oferta-300-prompts]]
