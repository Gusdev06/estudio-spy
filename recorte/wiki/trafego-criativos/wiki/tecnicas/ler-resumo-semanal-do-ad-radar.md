---
tipo: tecnica
tags: [ad-radar, resumo-semanal, ingestao, ad-library, metodo, leitura]
fontes: [[fonte-ad-radar-resumo-semanal-2026-09-13]], [[fonte-ad-radar-resumo-semanal-2026-09-11]]
---

# Ler o resumo semanal do ad-radar — o que cada bloco diz e onde ele engana

Todo domingo o `ad-radar` (`projects/mentoria-spy/ad-radar/`, `npm run resumo-wiki -- --ingestar`) grava em `raw/` um markdown com 8 blocos sobre o [[anunciante-centerpag]] e pede ingestão. Esta página é o manual de leitura — o que virar página, o que é limitação do gerador, e as armadilhas já vistas.

## Bloco a bloco

| Bloco | O que é | Vira o quê no wiki | Armadilha |
|---|---|---|---|
| Números | foto do último dia + somas da semana | linha nova na tabela de [[anunciante-centerpag]] | "Ativos hoje" e a curva do dia podem divergir (209 vs 210 em 11/09): são varreduras diferentes do mesmo dia. E **"hoje" é a última varredura, não a data do resumo** — o de 13/09 fecha em 12/09 |
| Curva por dia | ativos/alcance UE/novos/pararam por varredura | comparação semana a semana | só existe do 2º dia de histórico; 1ª semana = 1 linha. Novos/pararam medem a **busca**, não o anunciante ([[churn-inflado-por-varredura-ampliada]]) |
| Páginas | alcance UE por Página + Δ | tabela de concentração em [[anunciante-centerpag]] | "Anterior —" na 1ª semana; ordena por alcance, não por nº de anúncios. **Página parada continua listada** com o valor congelado ([[alcance-ue-congelado-entre-varreduras]]); e Página some do top sem ter caído |
| Mais tempo no ar | top-10 ativos validados | `criativo-<slug>-<ad_id>` pros veteranos que valem modelar | lista **truncada em 10**: famílias com muitos ids aparecem cortadas (3+2 vs 3+4 na [[familia-criativos-zap-stop-doubting]]); ids `<100` entram se a Página tem veterano. Ordena por **dias**, então quem escala rápido não aparece ([[pagina-carol-martin]]) |
| Ângulos novos | headline/copy + contagem | linha na tabela semanal do [[banco-de-headlines-spy-ad-library]] | contagem = anúncios lançados, não performance; a mesma frase com/sem ponto vira 2 linhas. **Não é inédito da semana**: a lista é corrida desde o início do radar e repete frase com contagem igual (`Stop Doubting` 11× em 11 e em 13/09) |
| Escalaram | cruzou 7 d sem `<100` ou alcance UE dobrou | atualizar o `criativo-…` marcado | "nenhum" na 1ª semana é **limitação**, não sinal — precisa de 2 dias de série. Os dois gatilhos dizem coisas diferentes: 7 d = sobreviveu (pode estar flat, +9 % em [[criativo-secret-revealed-934941213003855]]); dobrou = dinheiro entrando agora |
| Pararam | inativos da semana, mais longevos primeiro | `criativo-…` só se for recorde ou Página inteira; senão, linha em [[rotacao-de-paginas-como-padrao]] | Página inteira parando de uma vez ≠ fadiga de criativo. **Repete a semana anterior**: os 7 da Rachel Thompson apareceram em 11 e em 13/09, mesmos ids e mesmo alcance |
| Domínios | destinos, vitrines, candidatos | atualizar [[vitrine-vs-destino-real]] | candidato ≠ concorrente: promover é manual. Com varredura larga, a lista vira catálogo de e-commerce e até texto livre entra como host ([[ruido-e-custo-da-busca-ampliada]]) |

## Regras de ingestão específicas

1. **Novos > ativos** na primeira semana é normal: tudo visto pela 1ª vez conta como novo.
2. **Nunca tratar alcance UE ou dias como ROAS** — [[alcance-ue-como-proxy-de-gasto]], [[carimbo-de-menos-de-100-impressoes]].
3. Antes de criar `criativo-…` pra um veterano, checar se a headline já tem página (ex.: `See this before it's too late...` → [[familia-criativos-zap-35-dias]]) e **linkar em vez de duplicar**.
4. Se uma nota de inventário do mesmo dia disser outro número, registrar os dois na tabela histórica com a hora/varredura — não escolher um e apagar o outro.
5. Peça listada **não é peça baixada**: o resumo não traz vídeo, copy principal nem tela. Marcar "não baixado" na ficha até alguém rodar o swipe.
6. **Leia o custo do run antes dos números** (rodapé do cabeçalho). Custo pulando de patamar = varredura de largura diferente = fluxos, candidatos e "ângulos novos" contaminados na mesma rodada. Em 13/09: US$ 0,58 → 7,59.
7. **Confie em saldo e em Δ positivo; desconfie de fluxo e de Δ zero.** Ativos, alcance UE e crescimento se comparam; "novos", "pararam" e valor repetido, não.
8. **Página que some do relatório não morreu por decreto** — confira o id na Ad Library. Hill Alexis Brown saiu do top de 3.963 pra fora da lista em 1 semana, sem aparecer em "pararam" ([[criativo-hill-alexis-brown-2145000496375191]]).

## Conecta com

- [[fonte-ad-radar-resumo-semanal-2026-09-13]] — a semana em que o alerta "escalou" disparou e o ruído entrou
- [[fonte-ad-radar-resumo-semanal-2026-09-11]] — o primeiro resumo, com todas as armadilhas acima em ato
- [[anunciante-centerpag]] · [[banco-de-headlines-spy-ad-library]] · [[rotacao-de-paginas-como-padrao]]
