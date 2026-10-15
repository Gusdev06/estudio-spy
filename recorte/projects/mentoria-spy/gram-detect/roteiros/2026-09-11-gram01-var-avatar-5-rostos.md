---
tipo: roteiro-criativo
atualizado: 2026-09-11
oferta: go.zappdetect.com (spy gram / Gram Detect)
lote: gram01 · L9 · variação AVATAR · 5 rostos
controle: ../criativos/gram01-l9-faixa-2026-09-01/pecas/gram01-l9-en-01-v2.mp4
roteiro-mestre: 2026-09-01-gram01-modelado-l9-roteiro-mestre.md
readme-controle: ../criativos/gram01-l9-faixa-2026-09-01/README.md
pasta-do-lote (Bisturi): ../criativos/gram01-l9-var-avatar-2026-09-11/
anexos: 2026-09-11-gram01-var-avatar-5-rostos/video-prompt.txt · video-prompt-reserva.txt
autor: Isca (roteiro e gancho)
tags: [roteiro, spy-gram, L9, variacao-avatar, uma-alavanca, pruna-avatar]
---

# GRAM 01 · L9 · variação AVATAR — 5 rostos, roteiro congelado

**Neste lote o roteiro NÃO muda.** A alavanca é o rosto. Este arquivo congela o que já existe
(locução, beats, faixa, copy) com âncora de bytes, mede a VO pro Bisturi sincronizar, e entrega a
direção de performance (`video_prompt`) que os 5 avatares recebem — a mesma pros 5.

Ordem do Gusta (literal, do briefing): *"talking head novo + edição completa por cima (split,
faixas, caption), versão A com voz original em lipsync. Não entregar só o talking head limpo".*
Não existe versão B (voz gerada) neste lote.

⚠️ Nenhuma métrica do controle foi verificada (proxy de Ad Library, ver seção 5). Nada aqui é
número de performance.

---

## 1. Roteiro congelado — cópia literal do roteiro mestre (seção 4)

### Mapa de beats

| Beat | Tempo | Job |
|---|---|---|
| B1 | 0,0–3,8 | curiosity gap — promete um detalhe, não um produto |
| B2 | 3,8–7,5 | o problema não é você, é onde você olha |
| B3 | 7,5–12,9 | mata as 3 alternativas dela: adivinhar / brigar / pegar o celular |
| B4 | 12,9–18,3 | mecanismo — quem escorrega é a pessoa, não o app |
| B5 | 18,3–26,3 | payoff social — "tanta gente acaba encontrando" |
| B6 | 26,3–29,0 | recolocação — devolve o problema resolvido |
| B7 | 29,0–32,2 | CTA: direção ("aqui embaixo") + escassez ("enquanto está aberto") |

### 🇺🇸 EN — master

> **B1** There's one thing on Instagram that quietly gives people away.
> **B2** Almost nobody knows where to look for it.
> **B3** You don't have to guess, you don't have to start a fight, and you never have to touch anyone's phone.
> **B4** Because when someone is hiding something, they leave small traces behind without noticing.
> **B5** That's how so many people end up finding the conversations, the contacts and the behavior that someone was sure had already disappeared.
> **B6** You just need to know where to look.
> **B7** It's right below, while this is still open.

### Faixa — EN-01 (a única faixa do lote)

| # | Linha 1 | Linha 2 |
|---|---|---|
| EN-01 | 👀 THE PROFILE IS PUBLIC. | THE PATTERN ISN'T. |

### Âncoras de bytes — as 5 peças carregam exatamente isto

Medido em 2026-09-11 sobre `gram-detect/criativos/gram01-l9-faixa-2026-09-01/`:

| Arquivo | md5 | O que é |
|---|---|---|
| `vo/vo-master-en.m4a` | `776f219435732e5ad4e24556e85397ee` | VO mestre EN (aac 44,1 kHz estéreo, 182 kb/s) |
| `faixas/en-01.png` | `85b07aafa7b0374ea5d8947a8420ba58` | faixa EN-01, 1170×286, magenta |
| `pecas/gram01-l9-en-01-v2.mp4` | `2ebaa32269def93ba8fa81cde3c03b1a` | **controle** (rosto original + lipsync-2-pro) |

Regra: VO e faixa entram nas 5 peças como **os mesmos bytes** (a faixa por `overlay` do png; a VO
copiada sem reencode — ver trava 4). Funil (`funil/funil-painel.mp4`) e b-roll
(`broll/broll-painel.mp4`) idem, mas são posse de montagem do Bisturi — eu só ancoro o que é
roteiro: fala e faixa.

---

## 2. Medição da VO — o que o Bisturi precisa antes do lipsync

Fonte: `vo/vo-master-en.m4a`, decodificada mono f32 a 44,1 kHz; limiar −35 dB = 0,01778 linear.

| Medida | Valor |
|---|---|
| Duração (container, `ffprobe format`) | **31,907 s** |
| Duração (stream decodificado) | **31,927 s** (1 408 000 amostras) |
| Duração do vídeo do controle | 32,500 s · 975 fr · 30 fps |
| Primeira amostra > −35 dB (início da 1ª fala) | **0,179 s** |
| Última amostra > −35 dB (fim da última fala) | **31,667 s** |
| Extensão de fala (1ª → última) | 31,487 s |
| Pico / RMS | −2,82 dBFS / −22,57 dBFS |
| `silencedetect n=−35dB d=0.4` | **9 silêncios** (lista abaixo) — somam 5,034 s |
| Palavras (B1–B7, contadas na locução acima) | 89 (10 · 8 · 20 · 13 · 22 · 8 · 8) |
| wpm efetivo sobre a extensão de fala (31,487 s) | **≈ 170 wpm** |
| wpm articulado (extensão − silêncios ≥ 0,4 = 26,45 s) | ≈ 202 wpm |

### Os 9 silêncios ≥ 0,4 s (−35 dB) — e onde caem no roteiro

| # | início | fim | dur | onde |
|---|---|---|---|---|
| 1 | 3,545 | 4,051 | 0,506 | B1 → B2 |
| 2 | 6,547 | 7,639 | **1,092** | B2 → B3 (a maior; é a virada "onde olhar" → objeções) |
| 3 | 9,891 | 10,406 | 0,515 | dentro do B3 ("guess, ‖ you don't have to start a fight") |
| 4 | 12,635 | 13,104 | 0,469 | B3 → B4 |
| 5 | 14,924 | 15,429 | 0,505 | dentro do B4 ("hiding something, ‖ they leave") |
| 6 | 18,169 | 18,632 | 0,464 | B4 → B5 — é o "meio segundo depois de *without noticing*" que o roteiro pede (§4, notas) |
| 7 | 21,959 | 22,373 | 0,413 | dentro do B5 ("the conversations, ‖ the contacts") |
| 8 | 26,320 | 26,778 | 0,458 | B5 → B6 |
| 9 | 28,631 | 29,243 | 0,612 | B6 → B7 (B7 entra em 29,05 conforme o README do controle) |

Todas caem em fronteira de beat ou em vírgula da locução: são a respiração escrita, não sobra de
gravação.

### ⚠️ Correção de premissa do briefing (medição, não opinião)

O briefing (decisão 1) diz: ~~"a VO já tem 0 silêncios ≥0,4 s a −35 dB (medido pelo maestro)"~~.
**Medido aqui: 9.** E não é questão de limiar — a −40 dB dá 8, a −50 dá 7, a −60 dá 6. A premissa
está errada em qualquer escala.

**A decisão continua a mesma e fica registrada com a razão certa:** as pausas **não são cortadas**
neste lote porque a VO tem de ser **bit-idêntica ao controle** — uma alavanca por teste. Cortar
5 s de pausa mudaria duração, ritmo e mapa de beats junto com o rosto, e o teste ficaria cego.
O `cortar-pausas.py` do lote wpp01 **não roda aqui**. Handoff pro Bisturi em
`HANDOFF-isca-para-bisturi.md` (mesma pasta deste arquivo).

### Como a VO está assentada no controle (pro Pruna e pra remontagem)

Comparei a faixa de áudio de `pecas/gram01-l9-en-01-v2.mp4` com `vo/vo-master-en.m4a`:

- offset **0 ms** (correlação normalizada 1,0000 nos primeiros 10 s); resíduo alinhado −78,8 dBFS
  (= ruído de reencode AAC, nada de conteúdo);
- a faixa de áudio do controle dura **31,927 s dentro de um vídeo de 32,500 s** — os últimos
  0,573 s de vídeo não têm amostra de áudio, e a boca do controle fica fechada ali;
- `silencedetect` na peça: os mesmos 9.

Consequência pro Bisturi: o Pruna recebe o áudio e devolve vídeo ≈ duração do áudio + folga
(no var4, 32,37 s de áudio → 33,042 s de vídeo a 24 fps). Enviar a VO como está (31,927 s → cobra
32 s) já deve cobrir os 32,5 s do head+cauda; se precisar de `apad` pra chegar em 32,500 s, o pad
é só na cópia que vai pro modelo — **a faixa de áudio da peça final continua sendo a do controle**.

---

## 3. Direção de performance — `video_prompt` do `pruna-ai/p-video/avatar`

Schema (`~/.cache/wavespeed/models.json`): `video_prompt` = *"Prompt controlling body movement,
framing behavior, and atmosphere"*, padrão `"The person is talking."`. Entradas obrigatórias
`image` + `audio`; `resolution` 720p/1080p; `seed` opcional. A boca é dirigida pelo áudio — por
isso o prompt **não contém nenhuma palavra da fala**.

**Um prompt, o mesmo pras 5.** A alavanca é o rosto; a performance é constante.

### Principal — `2026-09-11-gram01-var-avatar-5-rostos/video-prompt.txt` (md5 `2db97c219265d3d321e47ab1eba97e20`)

```
The person is talking to the camera, looking straight into the lens the whole time, like quietly telling a secret to a close friend. Small natural head movements and slight nods, regular blinks, subtle eyebrow movement, calm and sincere expression, no big smile. Chest-up framing stays fixed, subject centered, shoulders still, hands out of frame. The person never turns to profile, never leans back or moves away from the camera. Static camera, no zoom, no cuts, steady constant lighting.
```

### Reserva — `video-prompt-reserva.txt` (md5 `9a81efbd0bb4c8a01689a6d56ff17f2d`) — o Bisturi usa a principal

```
The person is talking to the camera, looking into the lens, natural small head movements, occasional blinks, calm serious expression, hands out of frame, chest-up framing held constant, static camera, steady lighting.
```

Só entra se a principal fizer o modelo **exagerar** (cabeça balançando demais, sobrancelha teatral)
numa rodada barata de conferência. É a versão mais contida, colada no prompt da casa.

### O que mantive / mudei em relação aos lotes anteriores — e por quê

| Lote | `video_prompt` usado |
|---|---|
| `zap-secret-revealed-avatar-2026-09-10/var4/` (4 avatares Pruna) | **padrão do modelo** — nenhum `video_prompt` nos `vN.out.json`/README; voltou "sujeitos centrados", 704×1280, 24 fps |
| `zap-wpp01-clone-3-ganchos-2026-09-11/` (3 talking heads Pruna) | `The person is talking to the camera, looking into the lens, natural small head movements, hands out of frame.` |

**Mantive** (do wpp01, que já provou voltar sujeito centrado e sem reenquadre):
- a abertura `The person is talking to the camera, looking into the lens` — é a frase que casa com o
  padrão do modelo (`The person is talking.`) e não briga com ele;
- `natural small head movements` e `hands out of frame` — mãos são o maior denunciador de vídeo
  com IA (skill `trocar-avatar`, anti-cara-de-IA), e no L9 o head é cortado em 1170×1212 de um
  704×1280: mão que entra vira dedo derretido dentro do recorte.

**Acrescentei** (e o motivo de cada linha):
- *"like quietly telling a secret to a close friend"* — é o arquétipo do roteiro mestre (§4 notas:
  "tom de amiga que descobriu, não de especialista"; §7: sem prop de autoridade). O var4 e o wpp01
  eram peças de homem/ZAP com outro registro; aqui o registro é este.
- *"regular blinks, subtle eyebrow movement, calm and sincere expression, no big smile"* — rosto
  parado 32 s lê como stock (§7) e sorriso de anúncio contradiz a fala (casting do gd-ad01:
  "sem sorriso de anúncio"). Piscar é o que o var4 não documentou e o olho nota.
- *"Chest-up framing stays fixed, subject centered, shoulders still"* + *"never turns to profile,
  never leans back or moves away"* — o recorte do head é o **mesmo** nas 5 peças e a cauda de
  31,333–32,500 s é o rosto em quadro cheio; se um avatar deriva ou se afasta, o crop de um fica
  diferente do crop dos outros e vira alavanca escondida. No gd-ad01 o rosto voltou menor que o do
  campeão e foi registrado como contaminação — esta linha existe pra evitar repetir.
- *"Static camera, no zoom, no cuts, steady constant lighting"* — luz constante e sem corte pra
  que a única diferença entre as 5 seja a pessoa, não a fotografia. O roteiro (§7) pede "luz frontal
  limpa"; a cor da luz é do casting (imagem-base), o prompt só trava que ela não mude no tempo.

**Não pus** nada de gesto de mão nem de "muda de apoio" do §7 do roteiro mestre — o §7 foi escrito
pra filmagem real; em avatar gerado isso é o que estraga. Registro a perda: o controle (fonte
real) gesticula; os 5 não. Está na tabela de contaminação (seção 5).

---

## 4. Copy da Meta — cópia literal do roteiro mestre (seção 11)

> **Ordem do Gusta: copiar a copy, não reescrever.** Conferida campo a campo entre o `.txt` da
> peça e o `manifest.json` (`ad_id 1761247818659822`). A variação vai no visual e no gancho.

**Texto principal**

```
Ever wondered what someone's Instagram activity really looks like? 👀 Our tool analyzes any public profile and shows you who they follow, what they like, and the accounts they interact with the most. Just type the @username — the first analysis is free.
```

**Título**

```
Analyze any @username in seconds
```

**Descrição**

```
Free first analysis. No login needed.
```

**Botão**

```
Saiba mais
```

**Link**

```
GO.ZAPPDETECT.COM
```

A mesma copy nas 5 peças e no controle. Conjunto separado por peça só se a leitura for por peça;
se for na mesma campanha, mesmo conjunto com as 6 (controle + 5) e mesmo orçamento inicial.

---

## 5. Matriz do teste e nomes

### Peças

| Rótulo | Arquivo (pasta do lote, Bisturi) | Rosto |
|---|---|---|
| **Controle** | `gram01-l9-faixa-2026-09-01/pecas/gram01-l9-en-01-v2.mp4` (não copiar, não renomear) | original — mulher negra, tranças, ~25, filmagem real + lipsync-2-pro |
| V1 | `gram01-l9-var-avatar-2026-09-11/pecas/gram01-l9-en-01-V1.mp4` | avatar 1 (casting do Peneira) |
| V2 | `…/gram01-l9-en-01-V2.mp4` | avatar 2 |
| V3 | `…/gram01-l9-en-01-V3.mp4` | avatar 3 |
| V4 | `…/gram01-l9-en-01-V4.mp4` | avatar 4 |
| V5 | `…/gram01-l9-en-01-V5.mp4` | avatar 5 |

Regra de nome: **mesmo nome do controle + sufixo do avatar.** O Bisturi pode trocar `V1…V5` pelo
slug do casting (`-V1-<slug>`), como o var4 fez (`v2-homem-negro-oculos`).

⚠️ **Colisão de nome a evitar.** O controle já termina em `-v2` (= "versão 2, com lipsync"). Um
arquivo `gram01-l9-en-01-V2.mp4` difere do controle **só pela caixa da letra** — no APFS padrão
(case-insensitive) é o mesmo nome, e no portal/Meta lê como a mesma coisa. Estão em pastas
diferentes, então não sobrescreve; mas confunde. Recomendação (Bisturi decide): manter o `-v2` do
controle no nome e pendurar o avatar depois — `gram01-l9-en-01-v2-av1-<slug>.mp4` … `av5`. Os
rótulos V1–V5 desta matriz continuam valendo pra leitura.

### O que muda / o que fica igual (formato do README do `gd-ad01-var-avatar-2026-09-03`)

| Dimensão | Controle | V1–V5 | Alavanca ou contaminação? |
|---|---|---|---|
| Rosto | mulher negra, tranças, ~25 | **5 mulheres distintas** entre si e do controle (gênero = gênero da voz, f0 ~170 Hz) | **alavanca** |
| Origem do rosto | filmagem real nossa, boca recasada (`sync/lipsync-2-pro`) | rosto **100 % gerado** (GPT Image 2 → Pruna) | **contaminação** — identidade e "real × gerado" andam juntos |
| VO | `vo-master-en.m4a` `776f2194…` | mesmos bytes | igual |
| Roteiro / beats | seção 1 | idêntico | igual |
| Faixa | `en-01.png` `85b07aaf…`, y 1212–1498 | mesmos bytes, mesma posição | igual |
| Funil / b-roll | `funil-painel.mp4` / `broll-painel.mp4` | mesmos arquivos | igual |
| Layout / duração | L9 · 1170×2532 · 975 fr · 32,500 s · colapso no fr 940 | idêntico | igual |
| Copy da Meta | seção 4 | idêntica | igual |
| Cenário do head | ambiente da fonte real | gerado no casting (o roteiro §7 pede doméstico com textura) | contaminação leve — casting decide |
| Nitidez do head | 1170×1212 vindo de 2160×3840 | 704×1280 (720p) escalado ~1,66× | contaminação leve |
| fps do head | 30 nativo | 24 → 30 (conversão do Bisturi) | leve |
| Movimento | gesticula, muda de apoio (fonte real) | `video_prompt` constante; mãos fora, cabeça leve | leve |
| Boca × áudio | lipsync-2-pro sobre boca real | Pruna sobre imagem parada | a checar no olho (zoom na boca em 3 instantes) |

### Leitura esperada — o que cada resultado diria

| Resultado | O que diz | O que NÃO diz |
|---|---|---|
| **Alguma V > controle** | um rosto gerado segura a peça pelo menos tão bem quanto o real; o rosto é alavanca viva nesta família | não diz que "rosto gerado > rosto real" em geral — é 1 filmagem real contra N gerados; nem que a V vencedora vence em CPA se a leitura foi CTR/thumbstop |
| **Todas V < controle** | ou o rosto original é melhor, ou é a penalidade de "cara de IA" — **as duas explicações são indistinguíveis neste lote** (ver contaminação acima) | não diz que "avatar não funciona"; diz que esta geração, neste pipeline, perdeu |
| **Empate (controle ≈ V1–V5)** | rosto não é alavanca nesta peça; o próximo eixo é o gancho falado (roteiro mestre §6) ou a faixa (§5) | não diz que o rosto nunca importa — diz que não importa **com esta VO, esta faixa e este layout** |
| **V_i ≠ V_j entre si** | ranking de rostos dentro de um mesmo pipeline (aqui sim é limpo: mesma origem, mesmo prompt) | nada além disso |

**O que não dá pra concluir de jeito nenhum:** nenhuma métrica do controle foi verificada —
ele nunca rodou com dado de Meta Ads/UTMify cruzado (README do controle, "Registrado como
risco" 2; teardown do vencedor, aviso no topo). O "controle" é controle **de montagem**, não
de performance. A primeira leitura real sai quando as 6 rodarem juntas, no mesmo conjunto, com
o mesmo orçamento inicial e a mesma data de início.

---

## 6. Travas — checklist do Bisturi antes de subir

Conferir em **cada uma das 5** e anotar o valor medido ao lado (não o esperado):

1. **Saída:** `1170×2532` · **975 frames** · **32,500 s** · 30 fps · H.264 · AAC estéreo 44,1 kHz.
2. **Colapso:** faixa presente do frame 0 ao 939, **ausente no frame 940** (31,333 s). Rosto em
   quadro cheio de 940 a 974.
3. **Faixa por cor chapada** (método do controle): linha `y=1211` = 0,000 magenta · `1212` = 1,000 ·
   `1497` = 1,000 · `1498` = 0,000. Divisão vertical `x=462`.
4. **VO bit-idêntica:** faixa de áudio copiada do controle (`-c:a copy`), não reencodada. Prova:
   stream de áudio extraído com offset 0 ms e resíduo ≤ −70 dBFS contra `vo-master-en.m4a`
   (`776f219435732e5ad4e24556e85397ee`); duração do stream 31,927 s; `silencedetect −35 dB d=0.4`
   = **9** (o mesmo do controle — se der 0, alguém cortou pausa; se der outro número, o áudio não é
   este).
5. **Painel idêntico:** funil + b-roll com diff ≤ ruído H.264 contra o controle (o lote 1 mediu
   0,68/255) e head 100 % diferente do controle (é o que muda).
6. **PII zero:** o painel é o mesmo arquivo já borrado — provar por diff (item 5) em vez de reolhar
   as 4 janelas. **Mas o head é novo:** nenhum texto legível gerado no rosto/cenário (camiseta com
   escrita, cartaz, logo, marca de água). GPT Image 2 às vezes inventa letreiro.
7. **Palavras proibidas na tela:** nenhuma faixa nova, logo nada novo — mas conferir que o head
   gerado não trouxe texto com *spy, hack, password, location, private message, DM*, nome do
   produto, preço ou veículo de imprensa. Se trouxe, é a imagem-base que volta, não retoque.
8. **Rosto:** mulher; claramente distinta do controle e das outras 4; mãos fora do quadro nos 975
   frames; olhos na mesma altura relativa nas 5 (o gd-ad01 registrou olhos a ~35–37 % nos blocos de
   rosto cheio — usar como referência de casting, não como lei).
9. **Cauda 31,667–32,500 s:** áudio em silêncio, boca **fechada**; sem card final, seta ou logo.
10. **Custo antes de disparar:** 5 × ceil(31,927 s) = 5 × 32 s × US$ 0,025 = **US$ 4,00**
    (ou US$ 4,125 se o áudio for enviado com pad a 32,5 s → 33 s). `wavespeed price --upload`
    confirma antes; saldo compartilhado, filtrar `key:macbook`. **Só com o "sim" do Gusta.**

---

## Incerto / fora do meu alcance

- Gênero da voz (feminina, f0 ~170 Hz) é decisão do maestro no briefing; não remedi. Se o Gusta
  corrigir, é antes da fase C.
- O Pruna devolve 704×1280 a **24 fps** (var4: 793 fr / 33,042 s; o README de lá diz 25, o
  `ffprobe` diz 24). A conformação pra 940 + 35 frames a 30 fps é montagem do Bisturi.
- `seed`: o schema aceita. Não fixo aqui porque não há evidência de que o mesmo seed com imagens
  diferentes ajude em algo — mas se o Bisturi quiser reprodutibilidade por peça, registrar o seed
  no `out.json` de cada uma.
