---
tipo: conceito
tags: [bid-cap, entrega, cbo, meta-ads, diagnostico]
fontes: [[fonte-leitura-esteira-20-08-es-2026-08-21]]
---

# Estrangulamento de Entrega por Bid Cap

Quando o bid cap é baixo demais pro leilão, a campanha **inteira** não gasta — e aí você não tem teste de criativo nenhum, tem uma campanha que não existe no leilão.

É diferente da auto-limpeza saudável descrita em [[bid-cap]]. Lá, ads individuais são starvados
enquanto o campeão carrega a conta — isso é o mecanismo trabalhando. Aqui o **nível campanha**
morre: nenhum ad consegue comprar volume.

## Como diagnosticar

Olhe `budget_remaining` contra `daily_budget` no `get_campaign_details`:

> [[campanha-bidcap-es-esteira-20-08]] em 21/08: `budget_remaining` 598.531 de `daily_budget`
> 600.000 (centavos). **Gastou 0,25% do budget do dia.** Em 2 dias inteiros: R$ 63,96 de R$ 12.000
> disponíveis, com bid cap R$ 50.

Sinal complementar: CPM alto com volume ínfimo (R$ 68,63 de CPM em 932 impressões) — a conta só
compra os leilões mais baratos que cabem sob o teto e ignora o resto do inventário.

## Por que importa

O erro de leitura é concluir "os criativos não funcionam". Não dá pra concluir nada: os 30 ads
somaram 932 impressões. Ver [[piso-de-volume-antes-de-julgar-criativo]].

## A decisão

Subir o bid destrava a entrega — **mas libera o budget cheio de uma vez.** Só faça isso quando
houver [[folga-de-bid]] comprovada. Sem evidência de ROAS acima do breakeven naquele funil,
destravar o bid é liberar verba alta pra uma hipótese não testada. Nesse caso, pausar é a jogada
conservadora correta.

Relacionado: [[bid-cap]] · [[folga-de-bid]] · [[throughput-de-criativo]]
