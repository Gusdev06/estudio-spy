---
tipo: conceito
tags: [funil, checkout, diagnostico, metricas, cro]
fontes: [[fonte-comparativo-mensal-jul-ago-2026-08-22]]
---

# Colapso de IC → compra

Quando **initiate checkout sobe e compra cai**, o problema não é tráfego nem criativo —
é o fim do funil. É o sinal de diagnóstico mais barato que existe: separa "leilão ruim"
de "checkout quebrado" sem precisar de nenhuma outra ferramenta.

## Como ler

A razão `compras ÷ initiate checkout` é a taxa de fechamento do checkout. Se ela cai
enquanto **CTR, CPM e frequência ficam estáveis**, o topo do funil está intacto e o
dinheiro está vazando depois do "quero comprar".

Caso registrado na [[campanha-ca-dzd-hotm-bidcap-en]] (conta CA-DZD, dias 1–22):

| | Jul | Ago | Δ |
|---|---|---|---|
| CTR | 6,72% | 6,66% | ≈ |
| CPM | R$ 57,70 | R$ 61,79 | +7% |
| Frequência | 2,87 | 2,60 | −9% |
| Initiate checkout | 1.941 | 2.714 | **+40%** |
| Compras | 807 | 439 | **−46%** |
| **IC → compra** | **41,6%** | **16,2%** | **−61%** |

Topo igual, meio melhor, fim quebrado. Subir criativo aqui é gastar produção pra alimentar
um cano furado.

**Confirmado na UTMify** (dashboard inteiro, mesma janela) — não é artefato de pixel:

| | Jul 1–22 | Ago 1–22 |
|---|---|---|
| Cliques | 24.348 | 36.998 (+52%) |
| Page views | 21.912 | 28.732 (+31%) |
| Initiate checkout | 3.413 | 4.454 (+30%) |
| PV → IC | 15,6% | 15,5% (≈) |
| **IC → venda** | **34,0%** | **18,3%** |

⚠️ **Mas atenção ao que o colapso NÃO significa:** no mesmo período o **faturamento subiu**
(R$ 55,4k → R$ 56,8k) e o lucro +13,5%, porque o ticket médio saltou 47% com a troca do
back-end. Menos gente fechando, cada uma valendo muito mais. O colapso de IC→venda aponta um
vazamento real pra tapar — não é, sozinho, sinal de que o mês foi ruim. Ver
[[pixel-subestima-quando-atribuicao-cai]].

## Causas prováveis (em ordem de custo pra checar)

1. **Recusa de cartão.** ✅ **Confirmado**: 21,9% → 25,1% de jul pra ago. Explica boa parte
   (não toda) da queda. Ver [[recusa-de-cartao-como-gargalo]]. Só a UTMify mostra; o pixel do
   Meta não distingue "recusado" de "desistiu".
2. **Mudança de mix de funil.** Um funil de quiz dispara IC pra público mais frio: mais IC,
   menos compra por IC. Pista: o **valor médio do IC muda** (R$ 29,8 → R$ 44,8 no caso acima),
   o que denuncia página/produto diferente, não piora do mesmo funil.
3. **Quebra técnica no checkout** (gateway, upsell apontando pra produto errado, moeda).
   Ver a nota de back quebrado em [[campanha-cbo-fr-17-08]].

## Regra prática

Antes de culpar criativo por queda de vendas, olhe **IC → compra**. Se caiu, a próxima ação
é abrir a UTMify (recusa/reembolso) e o checkout — **não** subir esteira nova. Relacionado:
[[arte-nova-nao-herda-validacao]], [[piso-de-volume-antes-de-julgar-criativo]].
