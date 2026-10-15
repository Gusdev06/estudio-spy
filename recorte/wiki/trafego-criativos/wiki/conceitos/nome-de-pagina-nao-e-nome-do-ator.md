---
tipo: conceito
tags: [swipe, ad-library, metadado, casting, spy-zap]
fontes: [[fonte-selecao-atores-lote4-2026-09-01]]
---

# Nome de Página não é nome do ator — nem diz o gênero dele

O que o Ad Library mostra é o nome da **Página anunciante**. Não tem relação com quem aparece no vídeo, e tratar um pelo outro produz decisão de casting errada com aparência de fato.

## O caso

A peça `06-isabella-walker-1574339671069220` roda o swipe `go.centerpag.com` há 35,1 dias. O time inteiro — briefing, slots do grid, conversa da esteira — vinha tratando "Isabella" como a atriz, e o critério de casting do lote 4 pedia rostos *"visualmente distintos da Isabella"*.

**O ator da peça #06 é um homem barbudo.** Frames em `frames-atores-lote4/isabella-4frames.jpg`.

O dado pra desmentir já estava medido no [[fonte-teardown-lote3-2026-09-01]]: *"4 vozes masculinas distintas, F0 105,3 · 108,1 · 109,6 Hz"*. Ninguém cruzou com o nome, porque o nome não parecia precisar de conferência.

## Por que isso muda decisão

Casting "distinto da Isabella" significa coisas opostas conforme a premissa:
- **premissa errada** (mulher) → escolher homens pra variar
- **medido** (homem) → escolher mulheres

O lote 4 ia na direção contrária por causa de um nome de Página. E o efeito colateral é maior: os slots 1 e 2 (Lauren, Gonçalo) também são homens, então **rosto e gênero andam acoplados** no grid — o teste deixa de isolar "rosto" e passa a medir "rosto + gênero". Isso é escolha legítima, mas precisa ser escolha, não acidente. Ver [[variar-uma-alavanca-por-vez]].

## Regra

Todo atributo de ator — gênero, idade, aparência — sai do **frame**, nunca do nome do arquivo, da Página ou do slug do swipe. Mesma família de erro que [[rejeitando-no-nome-do-arquivo]]: metadado é pista, imagem é prova.

## Conecta com

- [[janela-limpa-continua-como-criterio-de-casting]] — o resto do casting que também só a imagem resolveu.
- [[rejeitando-no-nome-do-arquivo]] — decidir por nome de arquivo, mesmo vício.
- [[variar-uma-alavanca-por-vez]] — o acoplamento rosto+gênero que isso criou no grid.
- [[familia-criativos-zap-35-dias]] — as três peças de 35 dias e suas Páginas.
