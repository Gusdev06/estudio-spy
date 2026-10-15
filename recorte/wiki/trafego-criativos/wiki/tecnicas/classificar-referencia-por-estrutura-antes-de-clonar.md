---
tipo: tecnica
tags: [clonagem, troca-de-avatar, biblioteca-de-referencias, taxonomia, clonador, video-understanding]
fontes: [[fonte-meetshukla-biblioteca-reacoes-ugc-2026-09-22]]
---

# Classificar a referência por estrutura antes de clonar

Rotule cada referência com uma **estrutura** de lista fechada (reaction · lip-sync · hook + demo · talking head · B-roll) e, quando houver rosto, uma **reação** (shocked, confused, angry, choro…) — o rótulo de estrutura escolhe o método de clone, e o de reação deixa buscar a performance em vez do nicho.

## A regra

| Estrutura | Método de clone | O que se preserva da fonte |
|---|---|---|
| reaction, lip-sync | motion-based (driving video: fonte dirige o avatar novo) | expressão, boca, gestos, enquadramento |
| talking head, B-roll | prompt-based (regenera a partir da cena + estrutura) | roteiro, ritmo, composição |
| hook + demo | clona **só a abertura**; demo do produto entra no editor | a promessa do gancho; o demo é seu |

Fonte: Ghostfeed rodou video understanding (Gemini) em 1.066 referências curadas com essas escolhas fixas ([[fonte-meetshukla-biblioteca-reacoes-ugc-2026-09-22]]). Lista fechada é o ponto: rótulo livre não deixa filtrar.

## Por que importa aqui

- Hoje nossa biblioteca spy (`projects/mentoria-spy/`) e o `ad-radar` classificam por oferta, host, ângulo e gasto ([[alcance-ue-como-proxy-de-gasto]]) — **não por estrutura de execução**. Na hora de produzir, o Bisturi mede a estrutura peça a peça ([[medir-fronteira-de-bloco-em-video]]); um rótulo prévio pouparia essa descoberta e já diria qual skill chamar (`trocar-avatar` = motion-based; `clonar-edicao` = prompt/reconstrução).
- Pro [[../../projects/clonador/README|Clonador]] é a triagem de entrada: o job classifica a referência antes de escolher pipeline, em vez de o agente deduzir no meio.
- "Clonar só a abertura" é coerente com o que os nossos dados dizem sobre gancho ([[gancho-de-confissao-em-primeira-pessoa]], [[frame-1-sem-piscar]], [[slogan-fixo-nao-e-gancho]]).

## Cuidados

- Motion-based na nossa stack passa pelos limites já medidos: [[pruna-troca-de-pessoa-no-meio-do-clipe]], [[pruna-inventa-entrevistador-na-borda]], [[avatar-segue-o-genero-da-voz]]. Não é "apertar botão".
- Nada disso foi testado por nós; é hipótese de processo, sem resultado próprio ([[loop-de-performance]]). Não confundir a promessa do produto do autor com evidência.
