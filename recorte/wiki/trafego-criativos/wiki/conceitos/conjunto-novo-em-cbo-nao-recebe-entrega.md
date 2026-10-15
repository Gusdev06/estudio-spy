---
tipo: conceito
tags: [cbo, entrega, teste, video, armadilha]
fontes: [[fonte-fr-primeiro-dia-2026-08-23]]
---

# Conjunto novo em CBO não recebe entrega

Criar conjunto novo dentro de uma **campanha CBO que já tem conjuntos com histórico** não
garante entrega nenhuma — a Meta aloca o budget pra quem ela já prevê que converte, e o
recém-nascido pode ficar em **zero impressões** indefinidamente.

## O caso (22–23/08, BIDCAP FR 17/08)

10 conjuntos `VIDEO FR 20/08` criados em 22/08 e ligados no mesmo dia, dentro de um CBO que já
tinha 24 conjuntos. Resultado em ~1 dia:

| | Gasto | Impressões | Compras |
|---|---|---|---|
| 24 conjuntos de estática (1 dia mais velhos) | R$ 529,66 | 3.134 | 9 |
| **10 conjuntos de vídeo (novos)** | **R$ 0,00** | **0** | **0** |

Mesma campanha, mesmo budget, mesmo bid, mesma segmentação, mesma copy. A única diferença é
**idade do conjunto** (e o formato).

## Por que isso quebra teste A/B

Um teste "formato A vs formato B" montado como *conjuntos novos ao lado de conjuntos velhos
no mesmo CBO* não testa formato — testa **quem chegou primeiro**. O resultado é
indistinguível de "o formato B é ruim", quando na verdade o formato B nunca foi servido.

## Como montar o teste direito

1. **Campanha ABO separada** com budget fixo por conjunto — garante entrega ao novo.
2. Ou colocar a variante **dentro de um conjunto que já entrega** e ler no nível do anúncio
   (perde isolamento de público, ganha entrega garantida).
3. Nunca: conjunto novo em CBO maduro esperando que "a Meta distribua".

Relacionado: [[estrangulamento-de-entrega-por-bid-cap]],
[[piso-de-volume-antes-de-julgar-criativo]], [[animar-estatico-preservando-legenda]].
