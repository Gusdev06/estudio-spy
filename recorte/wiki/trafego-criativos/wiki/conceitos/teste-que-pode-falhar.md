---
tipo: conceito
tags: [metodo, medicao, diagnostico, esteira]
fontes: [[fonte-lote4-metodo-vo-2026-09-01]]
---

# Teste que pode falhar — diagnóstico só vale se tinha como dar errado

Ao investigar uma divergência entre duas medições, um teste só é evidência se **existia um
resultado que o derrubaria**. Ajustar um parâmetro livre até reproduzir o número do outro
não é diagnóstico — é curva ajustada, e explica qualquer coisa.

## O caso que originou (lote 4, 2026-09-01)

Bisturi e Isca divergiam numa contagem: **7 de 7** beats precisando de compressão contra
**2 de 7**. Duas hipóteses foram levantadas para explicar:

| hipótese | como foi testada | podia falhar? |
|---|---|---|
| **limiar** de `silencedetect` (Bisturi) | varredura de −60 a −30 dBFS | **sim** — e falhou: a contagem não se moveu em 30 dB, e o efeito tinha sinal contrário ao suposto |
| **denominador** slot cheio × slot menos entrada (Isca) | ajustar a entrada até reproduzir a série do outro | **não** — 0,37s foi escolhido *porque* reproduzia |

A varredura de limiar **eliminou** uma hipótese e por isso valeu. O ajuste de entrada
reproduziu a série e mesmo assim estava errado: `span/(slot−entrada)` e
`span_inflado/slot` dão **a mesma razão**, então nenhuma série de razões conseguiria
distinguir as duas. O parâmetro livre absorveu o erro real e o escondeu.

A causa verdadeira só apareceu abrindo o dado cru: um **bug de extração de span**
(ver [[beat-posicionado-na-marca]]).

## A regra

Antes de aceitar uma explicação para uma divergência, pergunte: **que resultado teria
derrubado essa hipótese?** Se não existe, ela não foi testada — foi ajustada.

Corolário prático: **prefira o teste que varre** (limiar, janela, parâmetro do detector) ao
teste que ajusta. O que varre pode voltar dizendo "não é isso", e é aí que ele serve.

## Parente próximo

Mesma família de [[nao-somar-medicao-emprestada-como-cruzamento]]: nos dois casos a
confiança vem de uma checagem que **parecia** independente e não era.

## Conecta com
- [[beat-posicionado-na-marca]] — a divergência concreta e a causa real
- [[padding-de-silencio-no-tts]] — a régua que a mesma investigação corrigiu
- [[variar-uma-alavanca-por-vez]] — parâmetro livre num diagnóstico é o mesmo problema de duas alavancas numa peça
