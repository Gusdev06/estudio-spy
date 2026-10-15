---
tipo: conceito
tags: [atribuicao, pixel, utmify, metodo, diagnostico, armadilha]
fontes: [[fonte-comparativo-mensal-jul-ago-2026-08-22]]
---

# Pixel subestima quando a atribuição cai

Queda de vendas no pixel do Meta **não é prova de queda de faturamento**. Se a atribuição
piorou no período, o pixel mostra um desabamento que não existe no caixa. Ler mês a mês só
com pixel é a armadilha mais cara do gerenciador.

## O caso que originou a página (jul → ago/2026)

Mesma janela (dias 1–22), duas réguas:

| | Pixel Meta | UTMify (caixa) |
|---|---|---|
| Receita | R$ 46.825 → R$ 28.985 (**−38%**) | R$ 55.376 → R$ 56.771 (**+2,5%**) |
| ROAS | 1,99 → 1,63 | 2,35 → **2,65** |
| Leitura | "a operação desabou" | "a operação lucrou 13,5% a mais" |

A 1ª versão da análise, feita só com pixel (UTMify estava fora do ar), concluiu que agosto
tinha caído 38%. **Estava errada.**

## O que denuncia a queda de atribuição

Sinais que apareceram no mesmo período:
- Pedidos com `utm_source = MetaAds` caíram de 881 → 506
- Pedidos **sem UTM** subiram de 77 → 200
- A receita migrou pra produtos de **back-end/assinatura**, que são os que menos carregam UTM

Ou seja: quanto mais o dinheiro vem do back-end, **menos o pixel enxerga**. Uma operação que
melhora o back-end vai *parecer* que está piorando no gerenciador.

## Regra prática

1. **Pixel serve pra comparar contas/campanhas/criativos entre si** — a distorção é a mesma
   dos dois lados, então o ranking continua válido.
2. **Pixel NÃO serve pra dizer se o mês foi bom.** Isso só a UTMify (ou o gateway) responde.
3. Antes de concluir "caiu", cheque a proporção de pedidos sem UTM. Se subiu, a queda pode
   ser só de visão.
4. Se a UTMify estiver fora, **diga que a conclusão é provisória** — não decida escala com ela.

Relacionado: [[colapso-de-ic-para-compra]], [[piso-de-volume-antes-de-julgar-criativo]].
