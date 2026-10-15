---
tipo: fonte
tags: [ad-radar, ad-library, spy-zap, spy-gram, centerpag, zappdetect, resumo-semanal, alcance-ue]
data: 2026-09-13
---

# fonte — ad-radar, resumo semanal 06/09 → 13/09/2026 (Spy Zap / Gram Detect)

Segundo resumo semanal do `ad-radar` sobre a operação [[anunciante-centerpag]]: **4 varreduras válidas, custo US$ 7,59, 224 ativos em 33 Páginas, 103 entregando, alcance UE 40.055**. Primeira semana com série de 2 dias — logo, a primeira com Δ por Página e com o alerta **"escalou" disparando**. Cru em `raw/2026-09-13-ad-radar-resumo-semanal.md`; leitura bloco a bloco em [[ler-resumo-semanal-do-ad-radar]].

## O que a fonte mede (e o que não mede)

- Tudo é proxy de Ad Library: dias no ar, carimbo `<100` ([[carimbo-de-menos-de-100-impressoes]]) e [[alcance-ue-como-proxy-de-gasto]]. Zero gasto, CTR ou ROAS.
- **A última varredura é de 12/09**, não de 13/09: "Ativos hoje" é foto do dia 12. A curva tem 2 linhas (11 e 12/09).
- **Custo 13× maior** que a semana passada (US$ 0,58 → 7,59) com varredura mais larga — e o preço aparece nos dados: ruído entrou ([[ruido-e-custo-da-busca-ampliada]]).

## Números da semana

| | 11/09 | 12/09 (esta fonte) |
|---|---|---|
| Ativos hoje | 209 | **224** |
| Entregando (sem `<100`) | 93 (44 %) | **103 (46 %)** |
| Novos na semana | 213 | **350** |
| Pararam na semana | 12 | **138** |
| Alcance UE ativo | 28.814 | **40.055** (+39 %) |
| Páginas ativas | 31 | **33** |

Curva: 11/09 → 210 ativos / UE 29.773 / 36 novos / 0 pararam (idêntica à da semana passada, bate). 12/09 → 224 / 40.055 / **137 novos / 119 pararam** num dia só.

## Achados

1. **Carol Martin virou a operação inteira**: 28.368 de 40.055 = **71 %** do alcance, +11.847 na semana (era 57 %). E nenhum anúncio dela aparece nas listas de veteranos, escalados ou parados — a maior concentração da operação é invisível nos top-10. → [[pagina-carol-martin]]
2. **O alerta "escalou" disparou pela 1ª vez: 4 anúncios.** [[criativo-secret-revealed-934941213003855]] (7 d sem `<100`, UE 1.957), [[criativo-victoria-bennett-1390046942586673]] (UE dobrou 484 → 1.353 em 2 d, headline GRAM), o irmão `1491914503148343` (82 → 236) e [[criativo-patty-marisa-alexis-2682333722195512]] (301 → 934).
3. **Recorde de longevidade quebrado por quem parou: Quinn, 103 dias, em espanhol.** 4 ids de 102–103 d saíram do ar. Bate de frente com o precedente da casa de que a Página Quinn tinha caído em agosto. → [[criativo-quinn-775104445592096]]
4. **Hill Alexis Brown sumiu da tabela de Páginas.** Era a 2ª em alcance (3.963) e tinha o maior anúncio da semana passada (UE 2.106); esta semana não aparece em lugar nenhum do resumo — nem nos ativos, nem nos parados. Alcance da Página caiu pra menos de 681 (o piso do top-8) ou a Página saiu. Isso **enfraquece o lastro do H2** do lote de réplica. → [[criativo-hill-alexis-brown-2145000496375191]]
5. **O teto de validação afundou**: fora [[criativo-dones-1056544273503851]] (36 d), o segundo colocado tem **8 dias**. Não existe nada entre 8 e 36 d no ar.
6. **`tryfidelo.com` foi promovido a destino real** (era candidato com 16 anúncios). Vitrines novas: `dectzap.com`, `detcwpp.com`, `conctwpp.com`. → [[vitrine-vs-destino-real]]
7. **Alemão entrou** (`Kostenloser Test ✅`, 5×), segunda semana com espanhol. → [[banco-de-headlines-spy-ad-library]]
8. **A [[familia-criativos-zap-stop-doubting]] ganhou 1 id e 1 dia** (6 ids, 8 d, UE somado 571 → 640) — segue no padrão "muitos ids, pouco alcance".

## Limitações e contradições registradas

- **"Novos" e "pararam" estão inflados por varredura, não por anunciante.** 137 novos + 119 parados em 12/09, num dia em que os ativos subiram só 14 líquidos, com a varredura mais larga e mais cara da série. → [[churn-inflado-por-varredura-ampliada]]
- **Os 7 anúncios da Rachel Thompson aparecem em "pararam" pela 2ª semana seguida**, com os mesmos ids e o mesmo alcance. O bloco não é incremental. → [[criativo-rachel-thompson-1472763134868396]]
- **"Ângulos novos na semana" não é inédito**: 11 das 15 linhas já estavam no resumo de 11/09, várias com contagem idêntica (`Stop Doubting` 11× nas duas semanas, `Free Test ✅` 8×, `Free Trial…Phone Number` 6×). É lista corrida desde o início do radar, não da semana.
- **Alcance UE repetido ao número** em anúncio e Página: Dones 273 → 273, Rachel Thompson 770 → 770 (+0) **com a Página parada desde a semana passada**. Não prova entrega zerada; pode ser valor congelado da Ad Library ou reuso do último visto. Não verificado. → [[alcance-ue-congelado-entre-varreduras]]
- **`tryfidelo.com` aparece nas duas listas** (destino real e candidato com 1 anúncio) no mesmo arquivo.
- **Lixo na lista de candidatos**: `instagram.com` (256), `api.whatsapp.com` (201), `play.google.com` (136), dezenas de e-commerces indianos/paquistaneses, e uma **legenda inteira em vietnamita ocupando o campo de domínio** — bug de parsing, não anunciante. Junto vieram 3 "ângulos novos" que não são copy de spy (`🔥 AS RELÍQUIAS DO MEGAFUNK`, `wow`, `ITI`).

## Páginas geradas / atualizadas

- Novas: [[pagina-carol-martin]] · [[criativo-secret-revealed-934941213003855]] · [[criativo-victoria-bennett-1390046942586673]] · [[criativo-patty-marisa-alexis-2682333722195512]] · [[criativo-quinn-775104445592096]] · [[churn-inflado-por-varredura-ampliada]] · [[alcance-ue-congelado-entre-varreduras]] · [[ruido-e-custo-da-busca-ampliada]]
- Atualizadas: [[anunciante-centerpag]] · [[ler-resumo-semanal-do-ad-radar]] · [[alcance-ue-como-proxy-de-gasto]] · [[carimbo-de-menos-de-100-impressoes]] · [[rotacao-de-paginas-como-padrao]] · [[vitrine-vs-destino-real]] · [[banco-de-headlines-spy-ad-library]] · [[criativo-dones-1056544273503851]] · [[familia-criativos-zap-stop-doubting]] · [[criativo-rachel-thompson-1472763134868396]] · [[criativo-hill-alexis-brown-2145000496375191]] · [[familia-criativos-zap-35-dias]] · [[glossario]]
- Semana anterior: [[fonte-ad-radar-resumo-semanal-2026-09-11]]
