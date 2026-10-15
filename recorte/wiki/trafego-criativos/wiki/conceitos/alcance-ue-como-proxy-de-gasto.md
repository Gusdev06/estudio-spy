---
tipo: conceito
tags: [ad-library, alcance-ue, proxy, gasto, ad-radar, medicao]
fontes: [[fonte-ad-radar-resumo-semanal-2026-09-13]], [[fonte-ad-radar-resumo-semanal-2026-09-11]]
---

# Alcance UE como proxy de gasto

A Ad Library não publica gasto, CTR nem ROAS de anúncio comum — mas anúncio que mira "Worldwide" cai na transparência europeia e a Meta publica o **alcance real na UE** (`aaa_info.eu_total_reach`). É a única fatia mensurável do gasto do concorrente, de graça. O `ad-radar` usa isso como proxy de "quem está botando dinheiro".

## Como ler

- **Pouco anúncio + muito alcance = escala.** [[criativo-hill-alexis-brown-2145000496375191]]: 1 anúncio, UE 2.106, 53 % da Página.
- **Muito anúncio + pouco alcance = teste.** [[familia-criativos-zap-stop-doubting]]: 5 ids, 571 somados.
- **Por Página** ele mostra concentração: [[pagina-carol-martin]] tem 57 % do alcance da operação em 11/09 e **71 % em 12/09** ([[anunciante-centerpag]]).
- **Por dia** (histórico do radar) vira curva: alcance UE que **dobra** de um dia pro outro é um dos dois gatilhos do alerta "escalou" (o outro é cruzar 7 dias sem `<100`). Primeiro disparo em 12/09: [[criativo-victoria-bennett-1390046942586673]] (484 → 1.353) e [[criativo-patty-marisa-alexis-2682333722195512]] (301 → 934) pela dobra; [[criativo-secret-revealed-934941213003855]] pela longevidade, com alcance praticamente parado.
- **É cumulativo**: só sobe. Valor repetido ao dígito entre varreduras não é entrega zerada, é leitura suspeita ([[alcance-ue-congelado-entre-varreduras]]).

## O que ele não é

- Não é gasto: é alcance numa região que o anunciante nem mira. Serve pra comparar anúncios **entre si** dentro da mesma operação, não pra estimar orçamento.
- Não substitui dias no ar: [[criativo-dones-1056544273503851]] tem 36 d e UE 273; o recorde de longevidade da operação, [[criativo-quinn-775104445592096]], fez **103 dias com UE 77**. Longevidade e alcance são sinais **independentes** — um anúncio pode sobreviver sem escalar (a [[familia-criativos-zap-35-dias]] era #13/#17/#51 em impressões com 35 d).
- Junto com o [[carimbo-de-menos-de-100-impressoes]], forma o par de proxies do radar; o score da aba Páginas é **ordinal** (`log10(1+alcance UE)×30 + peças entregando×5 + veterano`), não métrica.

Mesma lógica de [[gasto-do-gerenciador-como-proxy-de-performance]], só que de fora: o dinheiro que sobrevive é o sinal, não a métrica de conversão.

## Conecta com

- [[anunciante-centerpag]] · [[ler-resumo-semanal-do-ad-radar]] · [[piso-de-volume-antes-de-julgar-criativo]] (UE abaixo de ~100 é ruído do mesmo jeito)
