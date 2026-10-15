---
tipo: entidade
tags: [campanha, franca, fr, cbo, low-ticket, 300-prompts, nova]
fontes: [[fonte-campeoes-imagem-fr-2026-08-17]]
---

# Campanha CBO FR 17/08

🆕 Primeira campanha francesa da [[oferta-300-prompts]], criada em 17/08 e **pausada**
esperando os criativos. É o teste de abrir um 3º idioma pro funil (depois de EN e ES).

## Estrutura

Duas campanhas FR foram criadas em 17/08. A que recebeu os criativos é a **bid cap**.

| | 🟢 BIDCAP FR 17/08 (ativa no plano) | ⚪ CBO FR 17/08 (vazia) |
|---|---|---|
| Campanha | `52548438264334` | `52548421754334` |
| Conjunto | `52548438335534` — `FR - campeoes localizados (bid50)` | `52548421829934` |
| Lance | [[bid-cap]] R$50 | lowest cost |
| Budget | R$330/dia (CBO) | R$330/dia (CBO) |
| Anúncios | **4** | 0 |

Comum às duas: conta CA - DZD (`act_2383339602144432`, BRL), OUTCOME_SALES,
`OFFSITE_CONVERSIONS`/PURCHASE, pixel `1223791793200733`, atribuição 7d clique · 1d view ·
1d vídeo, público França 20–65 mobile FB+IG com Advantage Audience — espelhado do conjunto
ABO CAMPEOES, trocando só a geo.

⚠️ O **bid R$50** foi herdado do padrão da conta (os conjuntos `bid50` de EN/LATAM), não
calibrado pra França — a França tem CPM mais caro que LATAM, então é um chute educado. Sem
histórico local não dá pra medir [[folga-de-bid]]. Se não entregar, subir o teto é o 1º ajuste.

## Anúncios

| Ad | Criativo | Base |
|---|---|---|
| `52548438696734` | fr-v2-jatinho | ROAS 3,31 em 7d |
| `52548438694534` | fr-v1-campeao-morena | 112 vendas acumuladas |
| `52548438696134` | fr-v3-praia-loira | ROAS 1,92 em 30d |
| `52548438694934` | fr-v4-estadio | ROAS 2,92 em 30d |

Todos PAUSED, page `1002421492953397`, CTA `LEARN_MORE`, **todos os enhancements da Meta
OPT_OUT** — incluindo `image_text_translation` e `text_overlay_translation`, senão a Meta
reescreveria o value stack francês que foi embutido na imagem.

## Link e cloaker

Anúncio aponta pra `gusta.promptsgoat.com/fr` **+ o código FR na UTM**
(`ElSPzNUizI=tKTbAuA76U`). Sem o código o cloaker devolve a white page **em inglês** —
ele valida o parâmetro, não o path. Cada rota tem seu par código=valor; trocar o código
é o que muda a página entregue.

## Criativos

Os 4 campeões-imagem localizados em 17/08 (ver [[localizacao-de-value-stack]]):
jatinho, morena, praia-loira, estádio. Todos derivados de artes com venda comprovada em
EN/LATAM — nenhum é arte nova.

## Estado do funil FR

- Página `/fr` traduzida e no ar, checkout **próprio em EUR** (6,99 / 12,99 €) ✅
- Upsells ainda apontam pros produtos **USD** da `/en` ⚠️ — o back roda quebrado, e é no
  back que mora o lucro (front sozinho ≈ breakeven, ver [[oferta-300-prompts]])
- Pixel **compartilhado com a `/en`** ⚠️ — não dá pra ler FR separado sem separar antes

Relacionadas: [[campanha-ca-dzd-hotm-bidcap-en]], [[campanha-bm-latam-bidcap-en]].

## 📉 Atualização 2026-08-22 — primeiro resultado no leilão

Fonte: [[fonte-comparativo-mensal-jul-ago-2026-08-22]] (Meta Ads API, ago 1–22).

Uma campanha chamada `CBO FR 17/08` (id `120250788250090081`) rodou em agosto **na conta
[[conta-ca-saude-60]]** (`act_1464336718484629`, EUR) — **não** na CA-DZD:

| Gasto | Impr | CTR | CPM | LPV | IC | Compras | Receita | ROAS | CPA |
|---|---|---|---|---|---|---|---|---|---|
| € 74,79 | 5.361 | 5,84% | € 13,95 | 48 | **9** | 6 | € 51,61 | **0,69** | € 12,47 |

### ⚠️ Correção (mesma data, após olhar dia a dia)

O agregado ROAS 0,69 **não é conclusão válida** — a campanha viveu 3 dias:

| Dia | Gasto | Compras | Receita | ROAS |
|---|---|---|---|---|
| 17/08 | € 22,14 | 1 | € 11,15 | 0,50 |
| 18/08 | € 20,29 | 0 | € 0 | 0 |
| 19/08 | € 32,36 | **5** | € 40,46 | **1,25** |
| 20–22/08 | € 0 | — | — | **desligada** |

Estava em curva de subida e foi desligada no melhor dia. Ver
[[piso-de-volume-antes-de-julgar-criativo]].

### Os 4 criativos FR estão vivos mas estrangulados

Na `BIDCAP FR 17/08` (CA-DZD `52548438264334`, [[bid-cap]] R$ 50), os 4 campeões localizados
seguem ativos desde 17/08 e somam **R$ 6,34 e 51 impressões em 5 dias**:

| Dia | 17/08 | 18/08 | 19/08 | 20/08 | 21/08 | Total |
|---|---|---|---|---|---|---|
| Gasto | R$ 3,41 | R$ 1,15 | R$ 0,64 | R$ 0,67 | R$ 0,47 | **R$ 6,34** |
| Impressões | 23 | 9 | 10 | 4 | 5 | **51** |

Por anúncio (15–22/08): `fr-v2-jatinho` R$ 4,13 · 34 impr · **CTR 26,5%** · 2 IC ·
`fr-v1-campeao-morena` R$ 1,24 · 11 impr · `fr-v3-praia-loira` R$ 0,95 · 5 impr ·
`fr-v4-estadio` R$ 0,02 · 1 impr.

Mesmo [[estrangulamento-de-entrega-por-bid-cap]] da `BIDCAP ESTEIRA 20/08`.

**Status real da frente FR: não testada, não reprovada.** Pra decidir: religar a CBO em euro,
tirar a bid cap de R$ 50, e julgar só com ~R$ 300–500 gastos. Pré-requisito continua sendo
consertar o back FR (upsells apontando pra USD).

⚠️ **Contradição em aberto:** esta página registra as campanhas FR na conta **CA-DZD** (ids
`52548438264334` / `52548421754334`). A que gastou em agosto tem outro id e está na
**CA SAUDE 60+**. Ou são homônimas em contas diferentes, ou esta página está desatualizada.
Confirmar no gerenciador antes de decidir sobre a frente FR.

## 🚀 Atualização 2026-08-22 — esteira FR subida (70 criativos)

A `BIDCAP FR 17/08` (`52548438264334`, CA-DZD) tinha **23 conjuntos `ESTEIRA FR 20/08 - N`
criados vazios** em 21/08 22h35–22h38 — os criativos nunca foram subidos. Corrigido hoje:

| | |
|---|---|
| Criativos subidos | **70** (`fr2008-v01..v70`), da pasta `esteira-2026-08-20-fr/` |
| Anúncios criados | **70** — todos **PAUSADOS** |
| Distribuição | round-robin nos 23 conjuntos (3 cada; o conjunto 1 leva 4) |
| Bid cap | **R$50 → R$150** nos 24 conjuntos da campanha |

Spec do criativo clonada 1:1 do campeão `fr-v2-jatinho` (17/08): página `1002421492953397`,
link `/fr`, headline `⭐⭐⭐⭐⭐ (4.7/5)`, CTA LEARN_MORE, copy FR validada, pixel
`1223791793200733`, UTMs iguais. Detalhe em
`projects/300-prompts-hot/paid/criativos/esteira-2026-08-20-fr/README-subida-meta-2026-08-22.md`.

Relacionado: [[estrangulamento-de-entrega-por-bid-cap]], [[arte-nova-nao-herda-validacao]],
[[piso-de-volume-antes-de-julgar-criativo]], [[opt-out-de-enhancements-e-padrao-da-conta]].
