---
tipo: tecnica
tags: [locucao, tts, ritmo, producao, spy-zap, medicao]
fontes: [[fonte-roteiro-lote4-2026-09-01]], [[fonte-roteiro-lote3-2026-09-01]]
---

# Fit de locução por tempo — ⚠️ PÁGINA CORRIGIDA NA RAIZ (01/09)

> **A tese original desta página estava errada e foi substituída.** Ela dizia: *"o TTS lê a 156,9
> wpm, corrija por `atempo` global (1,1995), e o fator fora de 1,15–1,25 diz que a voz está
> errada."* **Os dois números vinham de duração bruta, e a receita descrevia um processo que nunca
> foi usado pra montar a peça.** Marcado, não apagado — a regra da casa é não deixar número errado
> sumir sem rastro.
>
> Substituída por: [[padding-de-silencio-no-tts]] e [[beat-posicionado-na-marca]].

## O erro, e ele tem duas camadas

**1. Duração bruta não é cadência.** O `minimax/speech-2.6-hd` devolve cada beat com silêncio de
cabeça e cauda — **16,8% do arquivo** no controle (4,383s em 26,053s), 25,5% num take posterior.
Os "156,9 wpm" eram palavras ÷ um tempo que é um sexto silêncio e **que não aparece em nenhum
artefato final**. O span de fala real do mesmo material dá **191,0 wpm**.

**2. O molde não monta por `atempo` global.** Ele **posiciona** cada beat na sua marca. Medido no
master do controle, os offsets entre marca e início de fala real: **+0,220 +0,162 +0,205 +0,343
+0,270 +0,174 +0,185** — sete pequenos, todos positivos, e 32,7% de silêncio no master.

## O dado que fecha o caso

| beat | fala | slot | |
|---|---|---|---|
| B1 | 2,490 | 2,578 | cabe |
| B2 | 3,120 | 3,017 | 1,034× |
| B3 | 2,670 | 2,783 | cabe |
| B4 | 2,490 | 2,783 | cabe |
| B5 | 3,360 | 3,456 | cabe |
| B6 | 4,430 | 4,129 | 1,073× |
| B7 | 3,110 | 3,255 | cabe |

**5 dos 7 beats cabiam sem compressão nenhuma.** O `atempo` global de 1,1995 comprimiria os sete em
20% — inclusive os cinco que já cabiam — levando a fala a **229,2 wpm** contra os 191,0 que
shippou. A receita antiga **degradaria a peça**.

## O custo real, porque ele não foi teórico

Triando voz por duração bruta, **6 das 7 vozes do sistema foram reprovadas** por "lerem devagar
demais", e um lote **cuja alavanca era a voz** quase fechou com uma voz só. Remedidas pela fala,
quase todas cabiam. Uma régua errada não erra sozinha — ela estreita o teste que ela deveria servir.

## A receita correta

1. **Aparar** o silêncio de cabeça e cauda de cada beat.
2. **Comprimir só o beat que estoura o seu slot.**
3. **Posicionar** cada beat na marca da grade, com entrada de ~0,20s.

Critério único, no lugar da janela 1,15–1,25 aposentada: **a fala do beat cabe no slot da grade?**

## A lição de método, que é o que sobra

**Uma razão não é um processo.** `26,388 ÷ 22,000 = 1,1995` tinha cara de `atempo` e foi escrita
como se fosse o método de montagem, sem nunca abrir o master — onde os offsets de posicionamento e
os 32,7% de silêncio estavam desde sempre.

Havia sinal contrário à vista e ele foi explicado como ruído: as razões bruto/slot davam
**1,171–1,216** em vez de um fator único, e isso foi anotado como "padding do encoder". Era o
padding do TTS, e era exatamente o fio.

E o pior modo de falhar: **naquele take, "proporcional" e "posicionado" davam quase a mesma
resposta.** A coincidência foi tratada como validação. Num take posterior, que variou de 226,9 a
124,5 wpm entre beats, a mesma suposição jogaria um beat **2 segundos antes da sua marca**,
levando 24 cards de legenda junto.

## ✅ São QUATRO grandezas, não duas — e é aqui que quase todo erro mora

O que parecia divergência de medição era vocabulário faltando. No controle, 69 palavras:

| Grandeza | wpm | Serve pra |
|---|---|---|
| **Bruto** (com padding) | **156,9** | **nada** — inclui silêncio que é descartado na montagem |
| **Span do beat cru** (cabeça/cauda aparadas) | **169,3** | **portão de triagem de voz** |
| **Span do master** montado | **190,2** | **comparar com as fontes** (178–186, medidas em vídeo pronto) |
| **Fonação** (sem pausa interna) | **213,0** | descrever a voz — **nunca dimensionar texto** |

**Pausa interna = 20,5% do span** (20,8% num segundo take, com outra voz — consistente, não ruído).
Descontá-la subdimensiona o texto: ela ocupa o slot igual à fala.

**Antes de comparar dois wpm, diga qual das quatro cada um é.** Foi o que faltou nas duas pontas —
uma publicou bruto como se fosse cadência, a outra publicou fonação sem dizer o que media.

⚠️ **Divergência que fica aberta, e não muda decisão nenhuma:** medindo fala aparada contra o slot,
uma medição conta **5 de 7** beats cabendo sem compressão, a outra **7 de 7** precisando de algum
aperto (máx. 1,158). **Não é limiar** — varrendo −60 a −30 dBFS a primeira contagem não se mexe, é
insensível em 30 dB. **É o denominador:** slot cheio contra slot menos a folga de posicionamento.
**A segunda é a operacionalmente certa** — se o beat entra em +0,20s da marca, o espaço real é
slot menos entrada. As duas matam o `atempo` global; a segunda é mais precisa sobre o dano.

## Conecta com
- [[padding-de-silencio-no-tts]] — a causa da camada 1
- [[beat-posicionado-na-marca]] — a causa da camada 2
- [[receita-do-karaoke-spy]] — a montagem que depende dessas marcas
- [[ritmo-de-locucao-em-wpm]] — mede a peça final, e essa parte segue de pé
- [[medir-fronteira-de-bloco-em-video]] — mesma família: proxy medido do jeito errado sobrevive porque ninguém o refaz
