# Comparativo mensal — Julho vs Agosto/2026 (operação low ticket)

**Puxado em:** 2026-08-22 · **Janela:** dias 1–22 dos dois meses (22/08 é dia parcial)
**Fontes:** UTMify (dashboard "Principal", `6a0e585ed7bcfee27cd8aff7`, BRL, GMT-3) para
faturamento · Meta Ads API (Pipeboard MCP) para leilão e criativo.

> 🔄 **Versão 2 — revisada com dado real.** A 1ª versão desta análise rodou só com pixel do
> Meta (UTMify estava fora) e concluía que agosto tinha caído 38% em receita. **Estava errado.**
> Com a UTMify reconectada, a receita está estável e o lucro subiu. O que o pixel via era
> perda de *atribuição*, não perda de *venda*.

---

## 🟢 Resumo em uma linha

**Agosto está mais lucrativo que julho** — lucro +13,5%, ROAS 2,35 → 2,65, margem 54,8% → 60,2%,
gastando 9% menos. **Mas o low ticket em si encolheu:** as vendas do front caíram 32% e o
faturamento só ficou de pé porque a **assinatura do AI Model Lab explodiu** (9% → 51% da
receita). A operação está ganhando mais dinheiro com menos gente entrando pela porta da frente.

## 📊 Dashboard consolidado (UTMify, dias 1–22)

| Métrica | Jul 1–22 | Ago 1–22 | Δ |
|---|---|---|---|
| Faturamento bruto | R$ 55.376 | R$ 56.771 | **+2,5%** |
| Faturamento líquido | R$ 52.117 | R$ 53.810 | +3,2% |
| Investimento em ads | R$ 23.568 | R$ 21.412 | −9,2% |
| **Lucro** | R$ 28.549 | **R$ 32.398** | **+13,5%** |
| Margem | 54,8% | **60,2%** | +5,4 p.p. |
| ROAS | 2,35 | **2,65** | +12,8% |
| ROI | 2,21 | 2,51 | +13,6% |
| Lucro/dia | R$ 1.298 | **R$ 1.473** | +13,5% |
| Vendas aprovadas | 1.159 | 813 | **−29,9%** |
| Ticket médio | R$ 44,97 | **R$ 66,19** | **+47,2%** |
| CPA | R$ 20,34 | R$ 26,34 | +29,5% |
| Reembolso | 7,8% (99) | 7,7% (68) | ≈ |
| Chargeback | 8 | 4 | −50% |

**Projeção de fechamento** (ritmo atual × 31 dias): ~R$ 80.000 de bruto e ~R$ 45.700 de lucro,
contra **R$ 76.661 / R$ 39.339** de julho cheio. Agosto fecha acima de julho.

**Gasto por conta em agosto:** CA-DZD R$ 14.529 · BM-LATAM R$ 3.280 · CA SAUDE 60+ R$ 3.602
(EUR convertido pela UTMify). A queda de gasto foi só na CA-DZD; a conta em euro é nova.

## 🔀 O que realmente mudou: a composição da receita

| Produto | Jul 1–22 | Ago 1–22 | Δ |
|---|---|---|---|
| **AI MODEL LAB** (assinatura, todas as SKUs) | 43 vendas · R$ 5.411 | **216 vendas · R$ 29.145** | **+438%** |
| **AI INFLUENCER PACK** (front do low ticket) | 559 vendas · R$ 29.819 | 379 vendas · R$ 19.952 | **−33%** |
| Back/upsell antigo (Character, Voices, Keep IG, Credits…) | R$ 22.157 | R$ 7.674 | **−65%** |
| Participação do AI Model Lab na receita | 9% | **51%** | — |

Três leituras:

1. **O front do low ticket encolheu de verdade.** 559 → 379 compradores (−32%), com o **ticket
   do front estável** (R$ 53,34 → R$ 52,64). Não é mudança de preço, é menos gente comprando.
2. **O back-end foi trocado, não perdido.** O antigo (produtos avulsos de R$ 25–70) caiu 65%
   e foi substituído pela assinatura do AI Model Lab (~R$ 135/venda). Cada comprador do front
   vale muito mais agora — é isso que explica o ticket médio +47% e a margem +5 p.p.
3. **É por isso que o pixel mentiu.** A assinatura e as vendas de back não são bem atribuídas
   ao anúncio. No Meta, `MetaAds` como fonte caiu de 881 para 506 pedidos, e pedidos **sem UTM**
   subiram de 77 para 200. O pixel viu menos venda; a UTMify mostra que o dinheiro entrou.

## 🚨 O gargalo que piorou: recusa de cartão

| | Jul 1–22 | Ago 1–22 |
|---|---|---|
| Tentativas de cartão | 1.521 | 1.095 |
| Aprovadas | 1.081 | 751 |
| **Recusadas** | 333 | **275** |
| **Taxa de recusa** | **21,9%** | **25,1%** |

Confirmado: **1 em cada 4 tentativas de cartão é recusada**, e piorou 3,2 pontos no mês. São
**275 pessoas que clicaram em comprar e não conseguiram** em 22 dias. Ao ticket médio atual
(R$ 66,19), isso é ~**R$ 18,2 mil de faturamento bruto barrado no gateway**. Recuperar metade
≈ **+R$ 9 mil no mês**, sem gastar R$ 1 a mais em mídia. É a maior alavanca isolada da operação.

## 🔬 Funil (UTMify, dias 1–22)

| | Jul | Ago | Δ |
|---|---|---|---|
| Cliques | 24.348 | 36.998 | +52% |
| Page views | 21.912 | 28.732 | +31% |
| Initiate checkout | 3.413 | 4.454 | +30% |
| Vendas aprovadas | 1.159 | 813 | −30% |
| PV → IC | 15,6% | 15,5% | ≈ |
| **IC → venda** | **34,0%** | **18,3%** | **−46%** |

O topo e o meio do funil **melhoraram** (52% mais cliques, 30% mais checkouts iniciados, mesma
taxa de PV→IC). O fim quebrou: de cada 100 checkouts iniciados, julho fechava 34 e agosto
fecha 18. A recusa de cartão (25,1%) explica boa parte, mas **não toda** — sobra um pedaço que
é abandono no checkout, provavelmente ligado ao funil de quiz trazendo público mais frio.

Isso valida o achado da 1ª versão: a queda de vendas **não é problema de criativo**, é de
fim de funil. A diferença é que agora sabemos que ela não custou faturamento — o back-end
compensou.

## 🏦 Leitura de leilão por conta (Meta Ads, pixel — só pra comparar eficiência entre contas)

| Conta | ROAS pixel ago | CPA pixel ago | CPM ago | Δ CPM |
|---|---|---|---|---|
| CA-DZD (BRL) | 1,47 | R$ 33,08 | R$ 61,79 | +7,1% |
| BM-LATAM (BRL) | **2,34** | R$ 18,52 | R$ 28,52 | **−25,5%** |
| CA SAUDE 60+ (EUR) | 1,93 | **€ 5,22** | € 8,63 | — |

⚠️ ROAS de pixel subestima (a UTMify marca 2,65 no consolidado). Serve pra **comparar contas
entre si**, não como número absoluto. A BM-LATAM roda mais barato e converte melhor que a conta
principal, com 1/4 da verba.

### A frente nova em euro — CA SAUDE 60+

Saiu de € 27 (julho inteiro) para € 600 em 22 dias. Campanhas de agosto:

| Campanha | Gasto | Compras | Receita | ROAS | CPA |
|---|---|---|---|---|---|
| **24 DOL - BIDCAP - 02/08** | € 508,96 | 101 | € 1.022,35 | 2,01 | **€ 5,04** |
| CBO FR 17/08 | € 74,79 | 6 | € 51,61 | 0,69 | € 12,47 |
| CBO 1-1-1 — Cópia | € 8,38 | 6 | € 60,87 | 7,26 | € 1,40 |
| CBO 1-1-1 | € 8,21 | 2 | € 22,46 | 2,74 | € 4,11 |

A `24 DOL - BIDCAP - 02/08` é 85% do gasto e 88% das vendas da conta, rodando com **€ 23/dia**.
É a **2ª oferta candidata** do trimestre. A frente FR não engatou: ROAS 0,69, só 9 initiate
checkouts em 5.361 impressões — bate com o back FR quebrado (upsells apontando pra USD).

🔎 **Contradição pra resolver:** o wiki registra as campanhas FR na conta CA-DZD (ids
`52548438264334` / `52548421754334`), mas a `CBO FR 17/08` que gastou em agosto tem id
`120250788250090081` e está na CA SAUDE 60+.

## 🧪 Por que a esteira de criativo não trouxe volume novo

Leitura de 20–21/08 (`wiki/trafego-criativos/raw/2026-08-21-leitura-esteira-20-08-es-2dias.md`):
os **10 conjuntos novos** da esteira ES rodaram **ROAS 0,77** com R$ 239, contra **ROAS 3,37**
dos **4 conjuntos antigos validados** com praticamente a mesma verba (R$ 242). Mesmo funil,
mesma copy — só a arte muda. E a `HOTM - BIDCAP — ES — ESTEIRA 20/08` gastou **R$ 63,96 de um
budget de R$ 6.000/dia**: o bid cap de R$ 50 estrangulou a entrega e não gerou nem amostra.

## ✅ O que fazer (em ordem de retorno)

1. **Atacar a recusa de cartão (25,1%).** É R$ 18,2 mil barrados em 22 dias. Testar: 2ª
   tentativa automática, PIX/carteira no checkout (PIX hoje é só 4% da receita e tem 90% de
   aprovação), e checar se a recusa concentra em país específico. Maior alavanca da operação.
2. **Escalar a `24 DOL - BIDCAP - 02/08`.** Menor CPA da operação (€ 5,04) com € 23/dia.
   Dobrar a verba custa quase nada e é o caminho mais curto pra recuperar volume de front.
3. **Recuperar volume do front do low ticket.** −32% de compradores é a única métrica
   genuinamente ruim do mês. Hoje o faturamento depende de 51% de uma assinatura — concentração
   de risco. O front é o que alimenta o back.
4. **Realocar verba da CA-DZD pra BM-LATAM.** ROAS 2,34 vs 1,47 e CPM 25% menor, com 1/4 da verba.
5. **Parar de subir arte nova em conjunto novo.** Colocar criativo da esteira dentro dos
   conjuntos validados (3,37 vs 0,77 no split de 20/08).
6. **Consertar a atribuição.** Pedidos sem UTM subiram de 77 pra 200. Sem isso, toda decisão
   de escala fica cega — foi exatamente o que fez a 1ª versão desta análise errar.

## ⚠️ Ressalvas

- 22/08 é dia parcial — subestima levemente agosto nos dois lados da comparação.
- O dashboard "Principal" mistura o funil low ticket com a assinatura do AI Model Lab. Estão
  separados na seção de composição, mas o consolidado é dos dois juntos.
- Números de leilão por conta são de pixel (subestimam); números de dinheiro são de UTMify.
- Gasto da CA SAUDE 60+ convertido de EUR pela própria UTMify (≈ R$ 6,00/€).
