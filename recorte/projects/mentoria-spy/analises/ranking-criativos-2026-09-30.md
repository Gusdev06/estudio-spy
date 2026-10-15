# Ranking de criativos spy — 01/08 a 29/09/2026

Fonte: MCP da UTMify (`get_meta_ad_objects`, nível anúncio, dashboard Mentoria) agregado **por peça** via vínculos do
Spy Hub (export do Gerenciador + código no nome) e chargebacks do webhook da Perfect Pay. Corte: peça com gasto ≥ R$ 400
(25 de 110 peças). Multa CB a US$ 30 × 5,24.

**Cobertura:** R$ 71,2 mil de gasto no período; **R$ 35,5 mil (50%) em anúncios sem peça vinculada** (contas 1, 5, CA1,
CA4, CA5 não exportadas + conta Noel). Inclui o "CTV 5 - VIDEO" (CA5), dono de 16 dos 52 chargebacks. Ranking vale pra metade ligada.

Métricas (definição UTMify): hook = 3 s / impressões · body = 75% / vídeos iniciados · hold = 75% / impressões ·
CTA = cliques / 75% · body→compra = vendas / 75%.

## Campeão
**CP77 — `77-ZAP-secret-revealed-filipino-jovem-moletom`** (Secret Revealed, avatar filipino jovem de moletom, lote 71–100 de 20/09).
R$ 3.147 gasto · 50 vendas · CPA R$ 63 · ROAS 3,84 · lucro R$ 8.925 · 0 chargeback. Rodou em 3 contas (7518, 2587, Noel) e vendeu em todas.

## Por métrica (só peças com vendas)
| Pergunta | Peça | Número | Contexto |
|---|---|---|---|
| Melhor hook | CP60 `ad02-h2-whatsapp-avatar-escandinavo` | 50,5% | 18 vendas, ROAS 2,23 (vídeo longo) |
| Melhor hook + body juntos | CP121 `secret-hook-ela-disse-que-e-amiga` | hook 44,6% | 23 vendas, ROAS 4,56 |
| Melhor body | CP121 | 9,9% (hold 9,4%) | mesma peça: segura e converte |
| CPA mais barato | CP22 `secret-revealed-v3-homem-branco-loiro` | R$ 47 | 20 vendas, ROAS 5,60 |
| 2º CPA | CP100 `podcast-wpp-clone-coreana-x-indiana` | R$ 49 | 12 vendas, ROAS 5,69 |
| Mais lucro | CP77 | R$ 8.925 | ver campeão |
| 2º lucro | CP108 `podcast-wpp-copy-nova-branca-ruiva-x-negra-afro` | R$ 7.051 | 28 vendas, ROAS 4,37 |

## Leituras
- **Família Secret Revealed/Secret Hook domina:** CP77, CP121, CP22 e CP112 no top de lucro/CPA. Podcast WPP (CP108, CP100) vem logo atrás.
- **CP118 `secret-hook-ela-troca-de-senha`:** melhor body do período (10,2%), hook 40%, mas **0 vendas em R$ 704**. Retém e não converte — o gancho promete outra coisa que a oferta.
- **CP60 / CP63 (AD02-H2 transplantado pro WhatsApp):** hook altíssimo (51–52%, o CP60 é o melhor hook entre as que vendem) mas quase ninguém chega a 75% — vídeo longo; body/CTA por 75% não comparam. (Correção 30/09: a 1ª versão desta análise tirou os dois do ranking de hook por engano.) CP60 vendeu (18, ROAS 2,23, 2 CB); CP63 não (ROAS 0,73).
- **CP112** tem o maior gasto dos secret hooks (R$ 2.722) com ROAS só 2,06 — abaixo dos irmãos 121/77.
- Amostras pequenas (12–50 vendas por peça): ordem entre CP22/CP100/CP121 pode trocar com mais gasto; CP77 é o único com volume pra chamar de campeão.

## Próximos passos sugeridos
1. Escalar CP77 e CP121; variar o CP77 (mesmo roteiro, avatares novos — já é o molde do lote 71–100).
2. Testar o gancho do CP121 ("ela disse que é amiga") no corpo do CP77.
3. Exportar CA1/CA4/CA5/1/5 no Gerenciador pra fechar os 50% sem peça (inclui o CTV 5 dos chargebacks).
