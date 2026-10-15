---
tipo: conceito
tags: [ad-radar, alcance-ue, medicao, ad-library, armadilha, freshness]
fontes: [[fonte-ad-radar-resumo-semanal-2026-09-13]]
---

# Alcance UE congelado entre varreduras — valor repetido não prova entrega parada

O [[alcance-ue-como-proxy-de-gasto]] é **cumulativo**: `eu_total_reach` só sobe enquanto o anúncio entrega. Quando o mesmo número reaparece **ao dígito** numa varredura seguinte, existem duas causas possíveis e o radar não distingue: o anúncio parou de entregar, **ou** o valor não foi atualizado (cache da Ad Library, anúncio inativo que congela, ou reuso do último visto pelo coletor).

## Os dois casos de 12/09/2026

| | 11/09 | 12/09 | Situação |
|---|---|---|---|
| [[criativo-dones-1056544273503851]] | 273 | 273 | **ativo**, 36 d |
| Página `Rachel Thompson` | 770 | 770 (Δ +0) | **parou na semana anterior** |

A Rachel Thompson é o caso que denuncia: a Página saiu do ar na semana 04→11/09 ([[criativo-rachel-thompson-1472763134868396]]) e continua **na tabela de Páginas ativas** com o alcance intacto. Ou seja, a tabela mistura alcance vivo com alcance congelado de Página morta.

## Regras

1. **Δ = 0 exato é suspeito, não é dado.** Trate como "sem leitura nova", não como "entrega zerada".
2. **Não some Páginas paradas no total da operação.** Os 40.055 de alcance UE ativo de 12/09 incluem pelo menos os 770 de uma Página que já tinha parado — o denominador está inflado, e com ele as fatias percentuais.
3. **Valor que cresce é o sinal confiável.** Foi por isso que o alerta "escalou" (dobra de alcance) apanhou Páginas de verdade: [[criativo-victoria-bennett-1390046942586673]], [[criativo-patty-marisa-alexis-2682333722195512]], [[pagina-carol-martin]].
4. Antes de concluir queda de uma Página que sumiu do top, lembre que **o inverso também vale**: some do relatório quem não foi lido nesta varredura ([[churn-inflado-por-varredura-ampliada]]).

## Conecta com

- [[ler-resumo-semanal-do-ad-radar]] · [[anunciante-centerpag]] · [[piso-de-volume-antes-de-julgar-criativo]]
