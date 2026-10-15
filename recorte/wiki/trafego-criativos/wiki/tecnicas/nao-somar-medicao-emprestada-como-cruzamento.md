---
tipo: tecnica
tags: [metodo, medicao, cruzamento, esteira, confiabilidade]
fontes: [[fonte-selecao-atores-lote4-2026-09-01]]
---

# Não somar medição emprestada como cruzamento

Dois agentes chegando ao mesmo número só confirma alguma coisa se as duas medições forem mesmo independentes — e numa tabela de cruzamento **célula vazia nunca conta como voto**.

## A regra

> **"—" na minha coluna quer dizer que eu não medi. Isso não pode entrar como concordância.**

Gatilho prático, pra usar sem pensar: antes de reportar "batemos no número", **conte quantas células da sua própria coluna estão preenchidas**. Se alguma linha do resultado depende de uma célula vazia, o resultado não é cruzado — é herdado.

## O caso que criou a regra (lote 4, 01/09/2026)

Pergunta que decidia o lote: quantos rostos masculinos distintos, com ≥22,0s contínuos limpos, existem no pool do swipe?

O Bisturi mediu e disse **3**. Eu varri por outro caminho e também cheguei a **3**. Reportei ao Maestro como cruzamento independente — e ele, com essa confiança, **repassou o número ao Gusta como decidido**.

Eram **4**.

Na linha do `cr05/` da minha tabela eu havia escrito `—` na minha coluna e **carregado a reprovação dele**, que tinha medido só a variante **V1** (essa falha mesmo, por overlay `EVIDENCE/SUSPICIOUS`). Nenhum dos dois mediu as outras variantes. As **V3 e V6 do mesmo homem** passam limpas: `ffprobe` 51,038s com rosto limpo nos 51 tiles, e 56,913s limpo até ~50s, com o recorte posto **acima da legenda**.

Ou seja: **o "3" dele e o "3" meu eram a mesma medição contada duas vezes.** O acordo não valia nada, mas *parecia* valer o dobro — e foi justamente a aparência de cruzamento que fez o número atravessar a esteira inteira sem ninguém reabrir.

## Por que isso é perigoso e não só chato

Erro herdado **não se cancela na média, se amplifica na confiança**. Uma medição errada sozinha é uma dúvida; duplicada, vira consenso. Quanto mais elos a esteira tem, mais barato fica um erro viajar — porque cada elo lê "os dois bateram" e para de conferir.

O sintoma é fácil de reconhecer depois: **os dois erram exatamente igual**. Medições genuinamente independentes divergem um pouco (16,0 × 16,5s, 12-13 × 13,5s). Concordância perfeita entre dois métodos diferentes é menos provável do que parece — quando aparecer, procure a fonte comum antes de comemorar.

## Contra-exemplo de que isto é o outro lado

[[medir-fronteira-de-bloco-em-video]] ensina que **concordância entre peças vale mais que margem dentro de uma peça**. Continua verdade — **desde que as peças sejam mesmo peças distintas**. Esta página é a condição que falta lá: *concordância só é evidência quando as medições são independentes*. As duas juntas dão a regra inteira:

| | Vale | Não vale |
|---|---|---|
| Fonte das medições | instrumentos/amostras diferentes | mesma amostra, repassada |
| O que a concordância prova | o fenômeno | que a mensagem circulou |

## Como cruzar de verdade

1. **Meça antes de ler o número do outro.** Ler primeiro contamina — você para de procurar quando bate.
2. **Diga a amostra, não só o resultado.** "16,5s" não é auditável; "16,5s medido na V1" é. Foi a ausência disso que escondeu o buraco por três mensagens.
3. **Varra as variantes.** Um "arquivo reprovado" pode ser uma variante reprovada. `V1` não fala pela `V3`.
4. **Ao reportar, marque o que é seu e o que é herdado.** Duas colunas, e a diferença visível.

## Conecta com

- [[medir-fronteira-de-bloco-em-video]] — a página que esta corrige pela borda: concordância entre peças só vale se forem independentes.
- [[janela-limpa-continua-como-criterio-de-casting]] — a medição que estava em jogo aqui; e o registro dos 5 detectores que mentiram no mesmo dia.
- [[variar-uma-alavanca-por-vez]] — mesma família: sem isolar a variável, o resultado não fala do que você acha que fala.
- [[fonte-selecao-atores-lote4-2026-09-01]] — o lote onde isso aconteceu, com os números corrigidos e os valores velhos marcados.
