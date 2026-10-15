# FR — primeiro dia com entrega de verdade (22–23/08)

Fonte: Meta Ads API via Pipeboard, nível anúncio, campanha `BIDCAP FR 17/08` (`52548438264334`),
`{since: 2026-08-22, until: 2026-08-23}`.

## 🟢 O bid ERA o gargalo — confirmado

| | 17–21/08 (bid R$50) | 22–23/08 |
|---|---|---|
| Gasto | R$ 6,34 em **5 dias** | **R$ 529,66** em ~1 dia |
| Impressões | 51 | **3.134** |
| Compras | 0 | **9** |

De ~10 impressões/dia para ~3.100/dia. A frente FR nunca tinha sido testada — estava
estrangulada, exatamente como [[estrangulamento-de-entrega-por-bid-cap]] previa.

## Resultado do dia (estáticas)

**40 anúncios · R$ 529,66 · 3.134 impr · 218 LPV · 22 IC · 9 compras · R$ 472,35 · ROAS 0,89**
CPA R$ 58,85 · ticket R$ 52,48

### As que venderam

| Arte | Gasto | Impr | CTR | LPV | IC | Compras | CPA |
|---|---|---|---|---|---|---|---|
| **fr2008-v22-bedroom-wide-selfie** | R$ 31,20 | 155 | **21,94%** | 25 | 1 | **3** | **R$ 10,40** |
| **fr2008-v33-cow-barn-bell** | R$ 17,15 | 168 | 9,52% | 15 | 6 | **2** | **R$ 8,58** |
| fr-v2-jatinho *(campeão 17/08)* | R$ 40,08 | 290 | 13,10% | 17 | 6 | 1 | R$ 40,08 |
| fr2008-v10-24-1 | R$ 33,34 | 182 | 10,44% | 15 | 0 | 1 | R$ 33,34 |
| fr2008-v14-6 | R$ 4,63 | 24 | 20,83% | 4 | 1 | 1 | R$ 4,63 |
| fr2008-v04-16 | R$ 3,93 | 33 | 15,15% | 1 | 1 | 1 | R$ 3,93 |

### As que mais queimaram sem vender

| Arte | Gasto | Impr | CTR | Compras |
|---|---|---|---|---|
| fr2008-v23-blonde-bodysuit-polaroid-1 | R$ 54,35 | 271 | 10,70% | 0 |
| fr2008-v29-bw-lingerie-bed | R$ 49,42 | 210 | 10,00% | 0 |
| fr2008-v38-gamer-room-bodysuit | R$ 39,30 | 182 | 7,69% | 0 |
| fr2008-v20-beach-freckles | R$ 28,81 | 198 | 7,07% | 0 |
| fr2008-v06-20-1 | R$ 24,72 | 217 | 7,83% | 0 |

Essas 5 somam **R$ 196,60 sem uma venda** — 37% do gasto do dia.

## 🔴 Os vídeos não entregaram NADA

**0 impressões, R$ 0,00.** Ligados em 22/08 e não receberam um único impression em ~1 dia.

- 8 dos 10 anúncios seguem ACTIVE; **2 foram arquivados** (`v21-beanie-squat-boots`,
  `v22-bedroom-wide-selfie`).
- Os 10 conjuntos `VIDEO FR 20/08` estão ACTIVE.
- ⚠️ **O bid cap foi alterado de R$ 150 → R$ 35** em toda a campanha (conjuntos com
  `updated_time` 23/08 00:31). Não fui eu — foi alteração feita no gerenciador.

### Hipóteses (nenhuma verificada)

1. **CBO concentrou budget nos conjuntos com sinal.** Os 10 conjuntos de vídeo nasceram em
   22/08 sem histórico; num CBO a Meta aloca pra quem ela já prevê que converte. Os de estática
   tinham 1 dia de vantagem e ganharam tudo.
2. **Bid R$ 35 vs CPM real R$ 100–430 na França.** As estáticas entregaram a R$ 35 porque já
   tinham sinal; conjunto novo com bid baixo tende a não achar leilão nenhum.
3. Vídeo precisa de mais sinal inicial que imagem pra Meta começar a servir.

## Próximo passo sugerido

O teste vídeo vs estático **não aconteceu** — vídeo teve zero entrega. Pra ele acontecer, o
vídeo precisa de entrega garantida, e num CBO disputando com 24 conjuntos estabelecidos isso
não vai vir sozinho. Opções:

- Tirar os 10 conjuntos de vídeo do CBO e rodar em campanha ABO própria com budget fixo; ou
- Colocar 1 vídeo **dentro** de um conjunto de estática que já entrega (ex.: o da
  `v22-bedroom-wide-selfie`, o melhor do dia) e ler no nível do anúncio.

E independente do vídeo: **pausar as 5 artes que queimaram R$ 196,60 sem vender** libera 37%
do budget diário pras que estão convertendo.

---

## ✂️ Execução — faxina de 2026-08-23

**5 anúncios pausados via API**, aprovado pelo Gusta. Critério: gasto ≥ R$ 24 no dia com
**zero venda**. IDs conferidos por nome antes de pausar.

| Anúncio | ad_id | Gasto queimado | Conjunto |
|---|---|---|---|
| fr2008-v23-blonde-bodysuit-polaroid-1 | `52549970704134` | R$ 54,35 | `52549931875534` |
| fr2008-v29-bw-lingerie-bed | `52549970718734` | R$ 49,42 | `52549931666934` |
| fr2008-v38-gamer-room-bodysuit | `52549970877934` | R$ 39,30 | `52549931758734` |
| fr2008-v20-beach-freckles | `52549970672334` | R$ 28,81 | `52549931835934` |
| fr2008-v06-20-1 | `52549970625134` | R$ 24,72 | `52549931666934` |

**Sangria estancada: R$ 196,60/dia** — 37% do budget diário liberado pras artes que convertem.

Notas:
- `v23` já estava com `effective_status: ADSET_PAUSED` (o conjunto dele tinha sido pausado no
  gerenciador); pausar o anúncio deixa a intenção explícita.
- `v29` e `v06` dividem o conjunto `52549931666934` — sobra 1 anúncio ativo nele.
- ⚠️ Todos os anúncios da campanha estão com `bid_amount 3500` (R$35), alterado no gerenciador.
