---
tipo: tecnica
tags: [layout, edicao, criativo-video, spy-zap, composicao]
fontes: [[fonte-teardown-edicao-wpp01-2026-09-01]]
---

# Card flutuante sobre plano único

Gramática de edição alternativa ao split de blocos: **um plano só** (talking head em quadro cheio) com a gravação de tela composta **por cima**, num card de celular semitransparente com cantos arredondados. O ator continua visível dos dois lados do card e **através** dele.

É o molde do [[criativo-wpp01-1762552938111855]] — #1 de 87 no swipe do centerpag, 16,1 dias no ar.

## Como difere do split de blocos

| | [[funil-gravado-como-painel-lateral]] (L9) | Card flutuante |
|---|---|---|
| Estrutura | 3 blocos empilhados, fronteiras duras | 1 plano + overlays |
| O ator | confinado ao bloco de cima | ocupa o quadro inteiro |
| A tela | bloco próprio, opaco | card alfa por cima |
| Fronteiras | medíveis (`y=306`, `y=380`, `x=142`) | **não existem** — borda é gradiente |
| Faixa de hook | bloco opaco no meio | matte no topo, ou overlay de texto |
| Custo de montagem | recorte e empilhamento | composição com alpha e máscara |

**Consequência prática:** quem tenta reproduzir isto empilhando blocos produz outra peça. Não há faixa separando ator de tela — há sobreposição.

## O que se ganha

- **O ator não encolhe.** Em split, o rosto perde metade da altura; aqui ele mantém o quadro inteiro e a tela entra sem tirar presença dele.
- **A tela pode crescer.** Como é overlay, o card muda de tamanho ao longo da peça sem quebrar layout — no wpp-01 ele começa pequeno na base e aos 30,8s toma a tela inteira, e o ator sai de cena de vez. 46% da peça com rosto, 54% sem.
- **Menos recorte, mais máscara.** Não precisa reconformar o recording pra caber numa coluna; ele entra na proporção nativa dentro de uma moldura de celular.

## O que se perde

- **Legibilidade da tela** enquanto o card é pequeno e translúcido — o que passa é a *impressão* de interface, não o conteúdo. Por isso a peça só entrega dado legível depois que o card cresce.
- **Medição.** Ver [[medir-fronteira-de-bloco-em-video]]: sem borda dura, nenhum detector acha fronteira, e um detector confiante devolve borda interna com margem alta.

## Sinais de que a peça usa este molde

Matte preta no topo com texto de hook **congelado o vídeo inteiro**, legenda karaokê **sobre** o card (não em faixa própria), e watermark dentro do card. Medido nas 26 escaladas do swipe: **3 a 4 usam este molde**; o resto usa celular físico na mão, talking head puro ou mockup gráfico.

Relacionado: [[catalogo-de-layouts-spy]], [[criativo-wpp01-1762552938111855]], [[dor-e-mecanismo-em-paralelo]].
