---
tipo: tecnica
tags: [criativo, teste, estatistica, meta-ads, decisao]
fontes: [[fonte-leitura-esteira-20-08-es-2026-08-21]]
---

# Piso de Volume Antes de Julgar Criativo

Antes de matar ou coroar um criativo, cheque se ele teve **volume pra ter opinião**. Abaixo de ~150 impressões, ROAS individual é ruído — use CTR, que estabiliza muito mais cedo.

## O caso que ensinou

Na [[campanha-abo-es-quiz-20-08]], o ad `quiz-es2008-v28-flash-couch-tee` fechou **ROAS 36,58**.
Parece campeão da rodada. Mas: **R$ 3,57 gastos, 22 impressões, 2 compras.** Uma venda a mais ou a
menos joga esse número de 18 pra 55. O número não descreve o criativo, descreve o acaso.

O que **é** legítimo ler dele: **CTR 22,73%, o melhor dos 30**. CTR com 22 impressões ainda é fraco,
mas é a métrica que precisa de menos volume pra virar sinal — está no topo do funil e acumula evento
a cada impressão, enquanto compra é evento raro.

## A regra prática

| Métrica | Volume mínimo pra opinar | Serve pra |
|---|---|---|
| CTR | ~150–300 impressões | matar arte fraca cedo |
| CPA / ROAS | ~3+ compras no ad | promover a escala |

Ordem de decisão numa rodada de esteira:
1. **Corte por CTR** os que ficaram muito abaixo da mediana da rodada (na 20/08 a mediana ficou
   ~10%; `v17` 3,08%, `v18` 3,90% e `v16` 0% eram corte óbvio).
2. **Não promova por ROAS** quem não tem 3 compras. Em vez disso, **dê verba** aos de CTR alto
   pra saírem do ruído e aí sim decida.
3. Só depois disso o ranking de ROAS vira decisão de escala.

## Armadilha do agregado

O inverso também vale: o split de grupo (10 conjuntos, R$ 239, 3 compras) **tem** massa suficiente
pra concluir que a rodada foi ruim — ver [[arte-nova-nao-herda-validacao]] — mesmo que nenhum ad
individual tenha. Agregue pra decidir sobre a rodada; desagregue só pra escolher sobreviventes.

Relacionado: [[variar-uma-alavanca-por-vez]] · [[throughput-de-criativo]] · [[estrangulamento-de-entrega-por-bid-cap]]
