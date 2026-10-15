---
tipo: tecnica
tags: [karaoke, legenda, arte, spy-zap, producao, medicao]
fontes: [[fonte-lote4-metodo-vo-2026-09-01]]
---

# Receita do karaokê spy — os parâmetros que não estavam versionados

Os 24 PNG de karaokê do molde spy-zap existiam; **o script que os gerou, não.** Esta é a
receita reconstruída medindo a caixa de tinta dos 24 originais, para que o próximo lote não
precise redescobrir.

## Os parâmetros

| parâmetro | valor |
|---|---|
| Fonte | **Arial Black** |
| Card | **1170×220**, ancorado em **y1676** |
| Altura de tinta | **travada em 81px** |
| Largura máxima | **1005px** (86% de 1170) — só encolhe a fonte ao passar disso |
| Fill | branco `#FFFFFF` |
| Keyword | verde WhatsApp `#25D366` |
| Contorno | `#080808`, ~8px |
| Proporção | **14 verdes em 24 cards** |

## Como a fonte foi identificada

Medindo a razão largura/altura de `NO PASSWORD` no card original: **799px de largura para
81px de altura = 9,86**.

| candidata | razão | veredito |
|---|---|---|
| Impact | 7,29 | condensada demais |
| Helvetica Neue | 10,40 | leve demais |
| Tahoma Bold | 10,60 | R e S divergem |
| **Arial Black** | 11,66 antes do ajuste | **formas de letra batem** |

A razão sozinha aponta Helvetica Neue; **a comparação visual das formas aponta Arial Black.**
Número e imagem discordaram, e a imagem ganhou — a razão inclui o contorno, que distorce.

## O comportamento de tamanho

Não é "preencher a largura". É **tamanho fixo, com teto de largura**: cards curtos
(`IT TOOK`, 38,5% da largura) e longos (`NOTHING INSTALLED`, 85,6%) têm a **mesma altura de
81px**. Só passa a encolher quando a linha chegaria perto de 1005px — aí a altura cai
(`HAD ALREADY DISAPPEARED` fica em 55px).

Quem renderiza preenchendo a largura produz cards de tamanho oscilante e quebra o molde.

## Conecta com
- [[karaoke-verde-marca-o-payoff]] — o critério de qual palavra fica verde
- [[beat-posicionado-na-marca]] — os tempos dos cards saem da grade de beats
- [[molde-de-edicao-n-atores]] — a arte do card é parte fixa do molde
