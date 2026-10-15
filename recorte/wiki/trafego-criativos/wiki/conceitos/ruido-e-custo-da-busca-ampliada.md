---
tipo: conceito
tags: [ad-radar, ad-library, busca, custo, ruido, apify, metodo]
fontes: [[fonte-ad-radar-resumo-semanal-2026-09-13]]
---

# Ruído e custo da busca ampliada — alargar a varredura não é de graça nem é neutro

Alargar os termos de busca do `ad-radar` na Ad Library cobra duas vezes: **em dólar** (cada URL varrida é um run pago) e **em qualidade** — o que entra a mais é majoritariamente anúncio de outro nicho, que contamina justamente os blocos usados pra decidir (candidatos a concorrente, ângulos novos, churn).

## A semana em que isso ficou visível (06 → 13/09/2026)

- **Custo: US$ 0,58 → US$ 7,59** na mesma vigilância, para 4 varreduras em vez de 3.
- **Lista de candidatos a concorrente** virou catálogo de e-commerce: `instagram.com` (256), `api.whatsapp.com` (201), `play.google.com` (136), `pehnawastore.pk` (31), `thesocialcat.com` (22) e mais de cem lojas sem nenhuma relação com spy. Na semana anterior eram **6 candidatos**.
- **Bug de parsing**: uma legenda inteira em vietnamita (decoração de festa, com hashtags) ocupa o campo de domínio na lista de candidatos. O extrator aceitou texto livre como host.
- **O ruído vazou pro bloco de copy**: `🔥 AS RELÍQUIAS DO MEGAFUNK ESTÃO DE VOLTA!` (2×), `wow` (1×) e `ITI` (1×) entraram como "ângulos novos" da operação spy.
- Provável mesma causa do churn absurdo do dia 12 ([[churn-inflado-por-varredura-ampliada]]).

## Regras

1. **Busca por frase exata**, nunca por palavras soltas — já custou US$ 3,47 num run abortado em 11/09 ([[vitrine-vs-destino-real]]).
2. **Relevância é filtro de saída, não só de entrada**: candidato só conta se o host real está na lista de destinos **ou** a Página já rodou a operação. Domínio de loja com 1 anúncio é lixo por construção.
3. **Promover candidato a destino real é decisão manual.** Nesta semana `tryfidelo.com` foi promovido — e ainda assim aparece nas duas listas do mesmo arquivo.
4. **Custo por semana é métrica de saúde do radar**, não rodapé: pulou 13× sem mudar o alvo, alguma coisa mudou na busca e os números do relatório mudaram junto.

## Conecta com

- [[ler-resumo-semanal-do-ad-radar]] · [[anunciante-centerpag]] · [[banco-de-headlines-spy-ad-library]] (onde o lixo de copy aparece) · [[alcance-ue-congelado-entre-varreduras]]
