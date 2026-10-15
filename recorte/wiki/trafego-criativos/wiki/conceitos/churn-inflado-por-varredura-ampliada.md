---
tipo: conceito
tags: [ad-radar, medicao, metodo, churn, ad-library, armadilha]
fontes: [[fonte-ad-radar-resumo-semanal-2026-09-13]]
---

# Churn inflado por varredura ampliada — "novos" e "pararam" medem a busca, não o anunciante

No `ad-radar`, **"novo" = visto agora e não antes; "parou" = visto antes e não agora**. Quando a varredura muda de largura (mais termos, mais domínios, mais páginas percorridas), esses dois números disparam **sem que o anunciante tenha feito nada** — anúncio que sempre existiu aparece como novo, anúncio que a busca não alcançou nesta rodada aparece como parado.

## O caso que fechou a regra (12/09/2026)

| | 11/09 | 12/09 |
|---|---|---|
| Ativos | 210 | 224 (**+14 líquido**) |
| Novos no dia | 36 | **137** |
| Pararam no dia | 0 | **119** |

137 nascimentos e 119 mortes num dia pra mover 14 anúncios líquidos. No mesmo período o custo da semana pulou de **US$ 0,58 → US$ 7,59** (13×) e a lista de candidatos encheu de domínio fora do nicho ([[ruido-e-custo-da-busca-ampliada]]). A explicação simples é que a varredura do dia 12 foi mais larga que a do dia 11 — não que a operação tenha rodado 137 criativos novos.

Segundo indício no mesmo arquivo: os **7 anúncios da Rachel Thompson aparecem em "pararam" pela 2ª semana seguida**, mesmos ids, mesmo alcance ([[criativo-rachel-thompson-1472763134868396]]). O bloco não é incremental — repete o que já tinha sido contado.

## Regras

1. **Confie no saldo, não nos fluxos.** Ativos e alcance UE totais são fotos da mesma varredura e se comparam; "novos"/"pararam" dependem de duas varreduras terem a mesma largura.
2. **Antes de ler churn, olhe o custo do run.** Custo pulando = varredura diferente = fluxos não comparáveis.
3. **"Parou" não é morte confirmada.** Confirma-se abrindo o id na Ad Library, ou pelo padrão de Página inteira saindo junto ([[rotacao-de-paginas-como-padrao]]).
4. Mesma família de erro do [[teste-que-pode-falhar]]: um número que sobe por mudança de instrumento não é resultado de nada.

## Conecta com

- [[ler-resumo-semanal-do-ad-radar]] — onde o bloco aparece
- [[alcance-ue-congelado-entre-varreduras]] — o efeito irmão, do lado do alcance
- [[anunciante-centerpag]] · [[carimbo-de-menos-de-100-impressoes]]
