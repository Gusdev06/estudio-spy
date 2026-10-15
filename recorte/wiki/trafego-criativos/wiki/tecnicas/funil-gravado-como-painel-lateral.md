---
tipo: tecnica
tags: [layout, edicao, funil-gravado, spy-gram, producao-em-escala]
fontes: [[fonte-teardown-vencedor-gram-2026-08-31]]
---

# Funil gravado como painel lateral

O mesmo screen recording do funil rende muito mais como **painel de apoio dentro de um invólucro UGC** do que como a peça inteira. O vencedor do swipe GRAM prova as duas versões lado a lado: ele roda o [[template-funil-gravado-9-modulos]] completo em 39,4% da largura da tela, e o resto do quadro é rosto, hook e dor.

## A montagem (L9)

Três blocos, com o terço de baixo dividido na vertical:

```
talking head UGC          47,7%
faixa de hook fixa        11,6%
funil 39,4% | b-roll 60,6%  40,6%
  x 0–141   |   x 142–359
```

Em 360×640: divisão vertical em **`x=142`**. Em 1080×1920: head `0–916`, faixa `916–1139`, painel `1139–1920`, divisão vertical em **`x≈426`**; no recording de origem (1170 de largura), **`x≈462`**.

⚠️ Essa divisão **tem que ser medida por variância temporal**, nunca por cor num frame só: há uma borda escura interna ao painel do funil que produz um falso positivo 13 px antes do fim real. Ver [[medir-fronteira-de-bloco-em-video]] — é o erro que este próprio teardown cometeu e que foi corrigido em 01/09.

## Por que ganha da versão em tela cheia

| | Funil em tela cheia | Funil como painel |
|---|---|---|
| Quem segura o scroll | a UI, sozinha | rosto + faixa + UI, três entradas |
| Locução | impossível (não há a quem atribuir) | 29s de VO por cima |
| Dor | ausente | roda em paralelo ([[dor-e-mecanismo-em-paralelo]]) |
| Legibilidade da UI | máxima | reduzida — só sobrevive UI de contraste alto e fonte grossa |

O preço é a legibilidade: a 39,4% da largura, só passa tela com título grande, botão chapado e no máximo 4 linhas. Módulo denso (terminal, log de 8 linhas) vira textura — o que, para o job dele, basta.

## Como montar sem regravar nada

O ativo caro já existe. É recorte e reposicionamento:

1. Recortar do recording a coluna central do celular (`scale` + `crop`, com o `y` ajustado por módulo pra manter o bloco que importa no quadro — mesma manobra de [[insert-de-funil-real-como-cutaway]]).
2. Comprimir os 9 módulos no tempo da locução. No vencedor: wizard 0–7,5s, input 7,5–14,7s, confirmação 15,9–22,7s, teatro técnico 22,7–24,6s, payoff 24,6–31,3s. **Os módulos 1–3 levam 70% do tempo** — coerente com a regra de que a peça está no começo.
3. Faixa de hook desenhada **por último**, senão o painel a apaga ([[costura-de-clipes-por-tarja-persistente]]).
4. Fechar colapsando: no último ~1,2s, split some e o rosto vai a quadro cheio, em cima do CTA falado.

Relacionado: [[catalogo-de-layouts-spy]], [[spec-de-edicao-layouts-spy]], [[eixos-de-variacao-de-criativo]], [[criativo-gram01-1761247818659822]].
