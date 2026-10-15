---
tipo: tecnica
tags: [casting, reaproveitamento, edicao, medicao, spy-zap]
fontes: [[fonte-selecao-atores-lote4-2026-09-01]]
---

# Peça pronta não é banco de atores — meça a faixa limpa antes de prometer o rosto

Anúncio finalizado tem legenda queimada, painel de UI e PII do primeiro ao último segundo: o que sobra pra reaproveitar é **uma faixa horizontal recortada**, e ela quase nunca tem altura pra preencher o molde de destino.

## O erro que isso evita

Uma pasta chamada `criativos-personagens` parece um banco de atores. No lote 4 os 10 arquivos eram **peças prontas do Gram Detect**, não footage cru: karaokê queimado nos 10 do começo ao fim, badge de gancho vermelho nos primeiros ~4s, painéis sobrepostos, e PII de terceiro (`dodoelady` num card de story, `@privatinaovr` numa linha de terminal) — ver [[pii-de-terceiro-em-criativo]].

Critério "sem legenda, sem PII" reprova o arquivo inteiro. A pergunta útil não é *"serve?"*, é **"qual faixa serve, e ela tem altura?"**.

## As duas medidas que decidem

**1. Onde o primeiro overlay entra (y).** Detector de glifo — branco/amarelo saturado **com pixel escuro logo abaixo** (o contorno da legenda). Sem a exigência de contorno, janela e parede clara viram falso positivo e o número não presta.

No lote 4 isso separou os candidatos em dois grupos:

| Grupo | 1º overlay | Consequência |
|---|---|---|
| AD01 (4 peças) | y ≈ 400–405 | overlay **sobre o rosto** — recorte que limpa, decapita |
| AD04 / AD05 | y ≈ 890–1040 | metade de cima livre |

**2. Se a faixa limpa preenche o destino.** Aritmética, não opinião. Fonte 1080×1920; molde 1170×2532 com tarja de 19,53% (494 px) → região do ator **1170×2038**.

| O que se usa | Escala | Cobre 2038? |
|---|---|---|
| frame inteiro (1080×1920) | 1,083× → 1170×2080 | **sim** — mas traz legenda e painéis |
| faixa limpa (1080×960) | 1,083× → 1170×1040 | **51%** ❌ |

**Dá pra ter frame cheio com overlay, ou faixa limpa sem altura — não os dois.** Encher a faixa limpa em altura cheia pediria upscale ~2,1×.

Faça essa conta **antes** de anunciar o ator como escolhido: ela é o que separa "achei o rosto" de "o rosto entra no molde".

## Conecta com

- [[janela-limpa-continua-como-criterio-de-casting]] — a outra medida do mesmo casting: quantos segundos seguidos.
- [[pii-de-terceiro-em-criativo]] — o handle de terceiro que vem junto na peça pronta.
- [[spec-de-edicao-layouts-spy]] — as medidas do molde de destino que entram na conta.
- [[medir-fronteira-de-bloco-em-video]] — a mesma família: qual detector mente em qual caso.
- [[arte-nova-nao-herda-validacao]] — reaproveitar peça validada não transfere validação ao recorte.
