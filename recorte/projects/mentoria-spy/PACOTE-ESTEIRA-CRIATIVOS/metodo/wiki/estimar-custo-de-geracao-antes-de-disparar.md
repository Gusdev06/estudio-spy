---
tipo: tecnica
tags: [custo, producao, ia-generativa, lipsync, processo]
fontes: [[fonte-roteiro-wpp01-l10-2026-09-01]], [[fonte-teardown-lote3-2026-09-01]]
---

# Estimar o custo de geração antes de disparar

Geração paga por IA se estima **por duração × preço unitário**, e o número vai na mesa **antes** do disparo. Ninguém gasta sem mostrar a conta primeiro.

## A armadilha do `base_price`

O `base_price` de US$ 0,08 do `lipsync-2-pro` é **por unidade, não por chamada**. Lido como preço de chamada, uma peça de 57s parece custar centavos; na prática o lote 1 gastou **US$ 2,72** para **31,3s** de lipsync — ~US$ 0,087/s.

Com saldo de US$ 17,47, a diferença entre ler certo e ler errado é a diferença entre um lote e nenhum.

## O procedimento

1. Contar os **segundos que realmente precisam de geração paga** — não a duração da peça. Numa peça em que o rosto sai no meio ([[fechar-o-argumento-antes-do-rosto-sair]]), o lipsync cobre só a parte com rosto: 21s em vez de 45s.
2. Multiplicar por preço unitário **real**, não por regra de três sobre um lote antigo.
3. Multiplicar pelo número de peças que precisam de geração **própria**. Variações que reusam a mesma geração (girar a matte de hook, trocar a legenda) custam **zero** a mais.
4. Reportar o número e só então disparar.

## O que costuma economizar mais que negociar preço

| Alavanca | Efeito |
|---|---|
| Rosto só na parte que persuade | corta 40–55% do lipsync de uma peça longa |
| Eixo de variação que não toca o vídeo (matte, legenda, copy) | N variações pelo custo de 1 |
| ~~Duração curta validada (as peças de 21–23s do swipe ZAP)~~ | ~~~⅓ do lipsync de uma peça de 57s~~ ⚠️ **medido: falso** — ver abaixo |

### ⚠️ Correção (01/09): lipsync escala com segundos de ROSTO, não com duração

A linha riscada acima assumia que uma peça de 21–23s custaria ~⅓ de uma de 57s. **Medido nas quatro
peças, não procede** — porque as duas pontas têm proporções de rosto opostas:

| Peça | Duração | Rosto | Lipsync estimado (US$0,0837/s) |
|---|---|---|---|
| wpp-01 | 56,77s | **26,0s (46%)** | US$2,18 |
| Isabella #06 | 21,34s | **21,3s (100%)** | US$1,79 |
| Lauren #10 | 22,27s | **22,2s (100%)** | US$1,86 |
| Gonçalo #20 | 23,34s | **23,3s (100%)** | US$1,95 |

Uma peça de 22s custa **~85%** de uma de 57s, não ⅓ — o wpp-01 esconde o rosto em 54% da peça e as
curtas o mantêm em 100%. **A duração não prevê o custo; a proporção de rosto prevê.**

Isso reforça o passo 1 do procedimento em vez de contradizê-lo: contar segundos de rosto continua
sendo a conta certa. O que cai é o atalho de estimar por duração.

A economia real das peças de 21–23s não está no preço unitário — está em [[familia-criativos-zap-35-dias]]
**não precisar de edição nova**: o molde já vem validado por 35 dias.


Estimativa derivada de um único ponto de dado **é estimativa** — rotular como tal e nunca reportá-la como preço.

Relacionado: [[roteiro-mestre-com-n-vozes]], [[molde-de-edicao-n-atores]], [[throughput-de-criativo]].

### Preços unitários reais já pagos (atualizar quando mudar)

| Modelo | US$/s de áudio | Saída | Onde foi medido |
|---|---|---|---|
| `sync/lipsync-2-pro` (vídeo + áudio) | ~0,087 | mantém o tamanho da entrada | lote 1 L9 (US$ 2,72 / 31,3 s) |
| `bytedance/avatar-omni-human-1.5` (foto + áudio) | 0,16 | 718×1286, 25 fps | Emilly (4,66 / 29,1 s), Secret (5,18 / 32,4 s) |
| **`pruna-ai/p-video/avatar`** (foto + áudio) — padrão desde 10/09 | **0,025** | 704×1280, 24–25 fps, ~0,7 s mais longo que o áudio | var4 Secret (3,24 / 4 × 32,4 s), wpp-01 3 ganchos (1,60 / 64 s) |

Estimativa do [[lote-gram01-l9-var-avatar-5-rostos]]: 5 × 32,5 s × 0,025 = **US$ 4,06**, na mesa antes do disparo.
