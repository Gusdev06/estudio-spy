---
tipo: referencia-criativo
atualizado: 2026-09-01
tags: [selecao-atores, spy-zap, centerpag, lote-4, whatsapp]
fontes: ["projects/mentoria-spy/criativos-personagens/", "projects/mentoria-spy/centerpag-detect/escalados/whatsapp/"]
---

# Lote 4 — seleção dos 2 atores novos + conferência das duas copies

Duas entregas. Nenhuma geração paga foi disparada.

---

# PARTE 1 — AS DUAS COPIES

## ⚠️ Primeiro: a hierarquia do briefing não se aplica aqui

A tarefa dizia "confira contra os `.txt` originais — se divergir, o `.txt` manda".
**Os `.txt` não contêm a copy falada.** Conferi os dois arquivos inteiros (17 linhas cada):
eles trazem só campo de anúncio — headline, descrição, botão, link e sinais de escala.

```
LINK DE DESTINO : GO.CENTERPAG.COM
TÍTULO          : See this before it's too late...
DESCRIÇÃO       : —
BOTÃO (CTA)     : Saiba mais
TEXTO PRINCIPAL : (o card agrupado não exibe o texto principal)
```

Isso bate **exatamente** com o que o teardown do lote 3 já registrava, inclusive a
observação de que o texto principal não é publicado (card agrupado). **Zero divergência
nesse campo.**

A copy que o lote 4 vai reproduzir é a **locução**, e ela não existe em nenhum `.txt`.
Então usei a única fonte verbatim disponível: **a legenda karaokê queimada no próprio
vídeo** — que é a transcrição que o anunciante fez da própria locução, palavra por palavra.

**Método:** 8 fps, máscara de glifo (branco/verde com contorno escuro), recorte na banda
densa de texto, deduplicação por diferença de máscara. Li os 11 strips resultantes.
Evidência em `referencias/frames-copy-lote4/cc-10-*.jpg` (Lauren) e `cc-20-*.jpg` (Gonçalo).
O `cc-06-*.jpg` é a Isabella, usada como controle do método.

---

## Copy 1 — Lauren Roberts (`10-lauren-roberts-2006430546681746`)

### ✅ CONFERE COM O TEARDOWN — palavra por palavra, zero divergência

```
I cloned my fiance's WhatsApp using only her number. Man, it's ridiculously easy.
Type her number here, click on monitor number, and that's it. The app searches for
WhatsApp and connects instantly. You'll see photos she deleted, audios she secretly
recorded, suspicious calls, and her exact location now. Rest assured, no notifications
will go to her phone. It's totally safe. Try it now and see everything.
```

Blocos de karaokê na ordem em que aparecem (é assim que a legenda quebra, útil pro Bisturi):

`I cloned my` · `fiance's WhatsApp using` · `only her number` · `man it's ridiculously` ·
`easy` · `type her number` · `here click on` · `monitor number` · `and that's it` ·
`the app searches` · `for WhatsApp and` · `connects instantly` · `you'll see photos` ·
`she deleted audios` · `she secretly recorded` · `suspicious calls` · `and her exact` ·
`location now rest` · `assured` · `no notifications will` · `go to her` · `phone` ·
`it's totally safe` · `try it now` · `and see everything`

> `fiance's` aparece sem acento na legenda queimada. Mantido como está.

---

## Copy 2 — Gonçalo Antunes (`20-goncalo-antunes-1378183431123084`)

### ⚠️ UMA DIVERGÊNCIA — `discrete` → `discreet`

```
Using my girlfriend's number, I cloned her WhatsApp and found out where she went after
work. It's that simple. Type in the number, press monitor and wait for the connection.
You can access deleted messages, late night calls, audio recordings, and live location.
Stop believing lame excuses. The tool is 100% discreet with no notifications, no trace.
She won't know you're watching. See the truth with your own eyes now.
```

| Onde | Valor velho (teardown) | Valor correto (legenda queimada) |
|---|---|---|
| 6º beat, anti-detecção | `The tool is 100% ~~discrete~~ with…` | `The tool is 100% **discreet** with…` |

A legenda mostra `100% discreet` em 7 frames consecutivos, com o karaokê passando por
`100%` → `discreet` → `with`. Não é ambíguo. Ver `frames-copy-lote4/cc-20-04.jpg`.

**Teardown já corrigido** em `2026-09-01-teardown-lote3-tres-de-35-dias.md`, com o valor
velho marcado (é meu arquivo). Resto da locução do Gonçalo: bate palavra por palavra.

Blocos de karaokê: `using my girlfriend's` · `number` · `I cloned her` · `WhatsApp` ·
`and found out` · `where she went` · `after work` · `it's that simple` · `type in the` ·
`number` · `press monitor and` · `wait for the` · `connection` · `you can access` ·
`deleted messages` · `late night calls` · `audio recordings` · `and live location` ·
`stop believing lame` · `excuses` · `the tool is` · `100% discreet with` ·
`no notifications` · `no trace she` · `won't know you're` · `watching` · `see the truth` ·
`with your own` · `eyes` · `now`

---

# PARTE 2 — OS 2 ROSTOS NOVOS

## ffprobe — os 10 candidatos

Todos idênticos em formato: **1080×1920, 60/1 fps**. Nenhum é 1170×2532.

| Arquivo | W×H | fps | nb_frames | dur. vídeo | dur. container |
|---|---|---|---|---|---|
| AD01 - PERSONAGEM 1.mp4 | 1080×1920 | 60/1 | 1685 | 28,083s | 28,097s |
| AD01 - PERSONAGEM 2.mp4 | 1080×1920 | 60/1 | 1873 | 31,217s | 31,231s |
| AD01 - PERSONAGEM 3.mp4 | 1080×1920 | 60/1 | 1773 | 29,550s | 29,560s |
| AD01 - PERSONAGEM 4.mp4 | 1080×1920 | 60/1 | 1782 | 29,700s | 29,722s |
| **AD04 - PERSONAGEM 1.mp4** | 1080×1920 | 60/1 | 1433 | 23,883s | 23,894s |
| AD04 - PERSONAGEM 2.mp4 | 1080×1920 | 60/1 | 1433 | 23,883s | 23,894s |
| AD04 - PERSONAGEM 3.mp4 | 1080×1920 | 60/1 | 1433 | 23,883s | 23,894s |
| **AD05 - PERSONAGEM 1.mp4** ✅ | 1080×1920 | 60/1 | 1576 | 26,267s | 26,286s |
| AD05 - PERSONAGEM 2.mp4 | 1080×1920 | 60/1 | 1576 | 26,267s | 26,286s |
| **AD05 - PERSONAGEM 3.mp4** ✅ | 1080×1920 | 60/1 | 1576 | 26,267s | 26,286s |

## ⚠️ O achado que muda a premissa: não são atores crus, são anúncios prontos

Os 10 arquivos **não são footage de ator**. São peças finalizadas do Gram Detect, com:

- **legenda karaokê queimada** nos 10, do primeiro ao último segundo
- **badge de gancho vermelho** nos primeiros ~4s
- **painéis de UI sobrepostos** (Gram Detect, BRUTE-FORCE LOGIN, LIVE INTERCEPTION)
- **PII de terceiro**: o handle `dodoelady` (card de story do Instagram) e o alvo
  `@privatinaovr` (linha de terminal nos painéis)
- **b-roll de terceiros** (casal em quarto, pessoas na rua)

Ou seja: o critério "SEM legenda queimada, SEM PII" **reprova os 10 no arquivo inteiro**.
O que dá pra aproveitar é uma **faixa superior recortada**, onde o rosto vive e nenhum
overlay entra. Foi isso que medi.

## Método (e onde ele me enganou antes de eu olhar)

Registro isto porque o erro é reproduzível e vale pro próximo:

1. **Variância temporal por linha** → inútil aqui. Estes anúncios são dinâmicos em toda a
   altura; não há banda estática pra isolar.
2. **Detector de pele pra "rosto na tela"** → deu números que eu quase reportei
   (AD05-P3 com "24,00s contínuos"). **Errado nos dois sentidos:**
   - falso negativo nos **frames de color wash** (laranja/amarelo) — o ator *está* lá,
     só tingido. Ver `frames-atores-lote4/gaps-finalistas.jpg`.
   - falso negativo **e** falso positivo no card `dodoelady`, que é *inset*: a pele
     aparece nas bordas, o detector diz "rosto ok", e o rosto na verdade sumiu.
3. **Detector de card escuro** → over-trigger (disse "AD04-P1 95% bloqueado" quando eu
   tinha acabado de ver o recorte limpo).
4. **O que resolveu: olhar.** Contact sheet denso a 1 fps **já no recorte proposto**.
   É a única medida que não me enganou. Os números abaixo saem de detector *confirmado
   contra a imagem*, nunca de detector sozinho.

## Medida que decide: maior janela contínua limpa

"Limpa" = dentro do recorte proposto, sem legenda, sem badge, sem card de UI, sem PII,
rosto de frente. Frames de color wash (0,1s) **contam como aproveitáveis** — o rosto está
visível, só tingido — e estão listados à parte pro Bisturi corrigir cor ou cortar.

| Candidato | Recorte | Janela limpa | Trecho | Washes dentro |
|---|---|---|---|---|
| **AD05 - PERSONAGEM 1** ✅ | 1080×960 @ y0 | **19,50s** | 5,60 → 25,10s | 21,50–21,60s |
| **AD05 - PERSONAGEM 3** ✅ | 1080×960 @ y0 | **18,40s** | 5,60 → 24,00s | 9,90–10,00s |
| AD04 - PERSONAGEM 3 | 1080×810 @ y0 | 17,50s | 0,00 → 17,50s | 7,4 · 9,1 · 12,5 · 14,4s |
| AD04 - PERSONAGEM 1 | 1080×810 @ y0 | 16,10s | 0,00 → 16,10s | 4,00–4,10s |

---

## ✅ SLOT 3 — `AD05 - PERSONAGEM 1`

**Caminho:** `projects/mentoria-spy/criativos-personagens/AD05 - PERSONAGEM 1.mp4`

- **Trecho aproveitável: 5,60s → 25,10s (19,50s contínuos)**
- ffprobe: **1080×1920 · 60/1 fps · 1576 frames · 26,267s**
- Recorte limpo: **`crop=1080:960:0:0`** — overlays só entram a partir de y≈997
- Rosto de frente e enquadrado nos 20 segundos amostrados a 1 fps
- Marca d'água: **nenhuma** — 0,0% de pixels congelados nos 4 cantos na janela útil
- Mulher, ~25-30, cabelo castanho ondulado solto, quarto claro

Evidência: `frames-atores-lote4/cropdense-ad05-p1.jpg` (30 tiles, 1 fps, já no recorte)

## ✅ SLOT 4 — `AD05 - PERSONAGEM 3`

**Caminho:** `projects/mentoria-spy/criativos-personagens/AD05 - PERSONAGEM 3.mp4`

- **Trecho aproveitável: 5,60s → 24,00s (18,40s contínuos)**
- ffprobe: **1080×1920 · 60/1 fps · 1576 frames · 26,267s**
- Recorte limpo: **`crop=1080:960:0:0`** — overlays só entram a partir de y≈1002
- Rosto de frente e enquadrado nos 19 segundos amostrados a 1 fps
- Marca d'água: **nenhuma** — 0,0% de pixels congelados nos 4 cantos na janela útil
- Mulher, ~35-40, cabelo escuro preso, argolas, cozinha/estúdio

Evidência: `frames-atores-lote4/cropdense-ad05-p3.jpg`

### Distinção entre si e da Isabella — verificada na imagem

`frames-atores-lote4/picks-vs-isabella.jpg`

- **Entre si:** idades, cabelo (solto ondulado × preso), cenário e estrutura facial
  claramente diferentes. São duas pessoas distintas.
- **Da Isabella:** ⚠️ **corrigindo uma premissa do time — o ator da peça #06
  "Isabella Walker" é um HOMEM barbudo**, não uma mulher. "Isabella Walker" é o nome da
  Página no Ad Library, não do ator. Confere com o teardown do lote 3, que já media
  "4 vozes masculinas distintas". Ver `frames-atores-lote4/isabella-4frames.jpg`.
  Logo os dois escolhidos são **máximo de distinção** contra ele.
- **Consequência pro grid:** os slots 1 e 2 (Lauren, Gonçalo) também são homens. Com
  slots 3 e 4 mulheres, o grid fica 3 homens × 2 mulheres. Se a intenção era ler só o
  efeito do rosto, isso **acopla rosto e gênero** — decisão do Gusta, não minha, mas
  fica registrada porque muda a leitura do teste.

---

## ❌ Descartados — motivo medido de cada um

| # | Arquivo | Motivo MEDIDO |
|---|---|---|
| 1 | AD01 - PERSONAGEM 1 | Legenda amarela a partir de **y=405**, dentro da banda de pele (y290–1010). Recorte que exclui a legenda corta o rosto. |
| 2 | AD01 - PERSONAGEM 2 | **Mesma atriz do AD05-P3** — duplicata confirmada na imagem (`cmp-mulher-ad01p2-vs-ad05p3.jpg`). Além disso legenda a partir de **y=405**. |
| 3 | AD01 - PERSONAGEM 3 | Legenda a partir de **y=405**, sobre o rosto. |
| 4 | AD01 - PERSONAGEM 4 | Legenda a partir de **y=400**, sobre o rosto. |
| 5 | AD04 - PERSONAGEM 1 | Janela limpa de só **16,10s** (0,00–16,10s). O card branco Gram Detect sobe até **y=448** entre 16,80 e 17,50s — alto demais pra recortar por cima sem cortar o queixo. |
| 6 | AD04 - PERSONAGEM 2 | Legenda amarela a partir de **y=510**, sobre o rosto (ator enquadrado mais perto). |
| 7 | AD04 - PERSONAGEM 3 | Janela limpa de **17,50s** — melhor dos AD04, ainda 4,5s abaixo dos ~22s. Card entra em 17,50–18,30s. |
| 8 | AD05 - PERSONAGEM 2 | **Mesmo ator do AD04-P1** — duplicata confirmada na imagem (`cmp-homem-ad04p1-vs-ad05p2.jpg`); mesma pinta, mesma barba, mesma linha de cabelo. Janela limpa menor que a dos escolhidos. |

---

## ⛔ Duas travas medidas que o Bisturi precisa resolver ANTES de montar

### 1. Nenhum candidato chega aos ~22s

O molde dura **21,3–23,3s**. O melhor candidato dá **19,50s**. Faltam ~2 a ~4s.
Não existe recorte que resolva isso: o que limita é o card `dodoelady` no começo
(3,9–5,6s) e o fade escuro no fim. **Nenhum dos 10 chega a 22s contínuos limpos.**

### 2. A faixa limpa não preenche a região do ator no molde

Conta, com os números do molde do lote 3:

- Saída do kit: **1170×2532**. Tarja verde = **19,69%** da altura → **498px**.
  ⚠️ **Corrigido 2026-09-01 (achado do Isca, reconferido por mim).** Eu tinha escrito ~~19,53% / 494px~~ — off-by-one: as linhas verdes são `y 0–125` **inclusive** = **126** linhas de 640, não 125. Reconferi em 5 colunas da fonte (x 10/90/180/270/350): verde `y 0–125` nas cinco, 126 linhas = 19,6875% → **498,49px** em 2532. Bate com as três medições do Isca (fonte, `kit/tarja.png`, peça renderizada). O teardown do lote 3 já trazia `126px de 640 = 19,69%` certo — quem escorregou foi este doc.
- Região do ator = **1170 × 2034**.
- Usando o **frame inteiro** (1080×1920): escala 1,083× → 1170×2080. **Cobre os 2034** ✅
  — mas traz junto toda a legenda queimada e os painéis.
- Usando só a **faixa limpa** (1080×960): escala 1,083× → 1170×1040.
  **Cobre 51% dos 2034** (1040 de 2034) ❌.

Ou seja: **dá pra ter frame cheio com overlay, ou faixa limpa sem altura — não os dois.**
Pra usar a faixa limpa em altura cheia seria preciso upscale de ~2,1×.

Os caminhos que vejo (a escolha é do Bisturi, não minha):
- cobrir tudo abaixo de **y≈960 do fonte** (= y≈1515 dos 2532 finais) com elemento do kit —
  é área bem maior que a faixa de karaokê do molde, que fica em y≈1939;
- ou recompor o layout do molde pra caber num talking head de meia altura.

Mando o número, não a decisão.

---

## Arquivos de evidência (pro portal)

Caminhos relativos a `projects/mentoria-spy/centerpag-detect/referencias/`:

**`frames-atores-lote4/`**
- `cropdense-ad05-p1.jpg`, `cropdense-ad05-p3.jpg` — os dois escolhidos, 1 fps, no recorte
- `cropdense-ad04-p1.jpg`, `cropdense-ad04-p3.jpg` — os dois vice, mesmo método
- `sheet-ad0*-personagem-*.jpg` — os 10 candidatos, varredura inicial 1 frame/2s
- `dense-ad04-p1.jpg`, `dense-ad05-p3.jpg` — frame cheio a 1 fps
- `picks-vs-isabella.jpg` — os 2 escolhidos + o ator da Isabella
- `isabella-4frames.jpg` — prova de que a peça #06 é um homem
- `cmp-mulher-ad01p2-vs-ad05p3.jpg` · `cmp-homem-ad04p1-vs-ad05p2.jpg` — as 2 duplicatas
- `gaps-finalistas.jpg` — os frames de color wash (o rosto está lá)
- `ad05p3-t4-pii-dodoelady.jpg` — a PII de terceiro em t=4s
- `crop-ad04p1-sheet.jpg`, `crop-ad05p3-sheet.jpg`, `tail-ad05p3.jpg`

**`frames-copy-lote4/`**
- `cc-10-00..05.jpg` — legenda da Lauren, ponta a ponta
- `cc-20-00..05.jpg` — legenda do Gonçalo (o `discreet` está no `cc-20-04.jpg`)
- `cc-06-00..04.jpg` — Isabella, controle do método
- `lauren-5frames.jpg`, `goncalo-4frames.jpg` — frames cheios de referência

> Mídia pesada não entra no git: os `.mp4` ficam no disco, aqui só os frames (7,3 MB).

---

## Nada pago

Nenhuma chamada de geração foi disparada nesta tarefa. Só `ffmpeg`/`ffprobe` local.

---

# ADENDO — varredura por footage MASCULINA (pedido do Isca)

**Motivo:** a copy é generificada e verbatim. Lauren diz *"my fiance's… only **her** number… photos **she** deleted"*; Gonçalo diz *"using my **girlfriend's** number, I cloned **her** WhatsApp"*. É homem falando da parceira. Com atriz mulher e copy verbatim, a peça vira mulher falando da namorada — enquadramento que ninguém escolheu. O Isca pediu pra varrer fora de `criativos-personagens/` antes de levar isso ao Gusta como decisão.

## ✅ ACHOU. E é melhor que tudo que havia em `criativos-personagens/`.

### Antes: o gênero dos 10 originais (que eu não tinha reportado)

| Gênero | Arquivos | Pessoas distintas |
|---|---|---|
| Mulher | AD01-P1, AD01-P2, AD01-P3, AD01-P4, AD04-P3, AD05-P1, AD05-P3 | 6 (AD01-P2 = AD05-P3) |
| **Homem** | **AD04-P1, AD04-P2, AD05-P2** | **2** (AD04-P1 = AD05-P2) |

Só **2 homens distintos** na pasta, e o melhor deles (AD04-P1) dava **16,10s** — 6s abaixo dos 22s. Por isso a pasta não resolvia mesmo com a premissa corrigida.

### O que varri (627 vídeos → 423 com ≥22s)

`ffprobe` em **todos** os vídeos sob `projects/mentoria-spy/` e `projects/mentoria-spy/centerpag-detect/`.
182 descartados por durar <22s; 22 ignorados em `_APAGAR/` (duplicatas marcadas pra exclusão).

| Pasta | Veredito |
|---|---|
| `criativos-crus/spy-zap/cr02`, `cr05`, `23-02-spy-en-es/{en,es}`, `ingles-17-08` | ❌ **anúncios prontos** — faixa de gancho queimada no topo (`WHAT THEIR WHATSAPP IS HIDING…`, `I Never Thought He'D Cheat On Me…`), karaokê e painéis. Atrizes mulheres na maioria. |
| `criativos-crus/spy-zap/base-ingles` | ⚠️ **split** app-à-esquerda / ator-à-direita, 1440×1080 landscape, **sem legenda**. Homem. Mas o ator ocupa coluna estreita (~790×1080) — vira talking head apertado e de baixa resolução no molde retrato. Fallback marginal, não recomendo. |
| `gram-detect/troca-avatar-studio/jobs/*` | ❌ anúncios prontos com karaokê queimado; atrizes mulheres. |
| `centerpag-detect/{anuncios,tratados,escalados}`, `gram-detect/{anuncios,tratados,escalados}` | ❌ corpus de swipe — anúncios de concorrente, legenda queimada por definição. |
| `centerpag-detect/criativos/lote3-isabella-*/` | ❌ é a peça já montada + seus blocos, não ator novo. |
| **`gram-detect/criativos/roteiro-e-2026-08-31/avatares/`** | ✅ **limpo** |
| **`gram-detect/criativos/sophia-jones-avatar-homem-38-2026-08-24/`** | ✅ **limpo** |
| **`gram-detect/criativos/lote-5-avatares/`** | ✅ **limpo após a abertura** |

O material limpo é **nosso**, gerado na esteira de avatar — sem legenda, sem watermark, sem PII de terceiro. Melhor ponto de partida que footage de concorrente.

---

## ✅ SLOT 3 (revisado) — `CRIATIVO-a1-homem-velho`

`projects/mentoria-spy/gram-detect/criativos/roteiro-e-2026-08-31/avatares/CRIATIVO-a1-homem-velho.mp4`

- **Trecho aproveitável: 0,00s → 57,10s — 57,10s contínuos** (2,6× o necessário)
- ffprobe: **1080×1920 · 61,30s** (container) / 59,30s de vídeo decodificado
- **Frame cheio, sem recorte** — nenhum overlay, nenhum painel, nenhuma legenda
- Único overlay do arquivo: CTA amarelo `CLICK THE LINK BELOW AND SEE THE TRUTH NOW` em **57,10–59,30s** — fora do trecho
- Homem negro, ~65-70, barba grisalha, polo azul-marinho, sala com luz quente
- **Máxima distinção** contra os três do grid (todos homens brancos, 28-40, cabelo escuro)

Evidência: `frames-varredura-lote4/dense-a1-homem-velho.jpg` (0–31s) e `-b.jpg` (31–59s), 1 fps.

## ✅ SLOT 4 (revisado) — `final-h2-grisalho-52`

`projects/mentoria-spy/gram-detect/criativos/lote-5-avatares/final-h2-grisalho-52.mp4`

- **Trecho aproveitável: 8,10s → 34,20s — 26,10s contínuos**
- ffprobe: **1080×1920 · 34,17s**
- **Frame cheio a partir de 8,10s.** Antes disso é split screen com faixa vermelha `Stay one step ahead. Pay attention.` + prints de Instagram de terceiros (**PII — fica fora do trecho**)
- Homem branco, ~55, cabelo e barba grisalhos, camisa azul, sala clara
- Distinto dos três do grid pela idade e pelo grisalho

Evidência: `frames-varredura-lote4/dense-h2-grisalho.jpg`, 1 fps.

### Reservas (servem, mas com ressalva)

| Candidato | Janela limpa | Ressalva |
|---|---|---|
| `sophia-jones-avatar-homem-38-2026-08-24/versao-A-mudo.mp4` | **34,10s** (arquivo inteiro) | ⚠️ **arquétipo mais próximo do ator da Isabella** — homem branco ~38 de barba escura cheia. Tecnicamente o 2º melhor; reprovado só na distinção. |
| `lote-5-avatares/final-h1-jovem-27.mp4` | 26,10s (8,10→34,20s) | homem branco ~27, cacheado; mais próximo do ator do Gonçalo em idade e coloração. |

Comparativo lado a lado: `frames-varredura-lote4/cmp-candidatos-homens.jpg` (os 4) e `cmp-ja-no-grid.jpg` (Isabella, Lauren, Gonçalo).

---

## O que isso destrava

Com os dois de cima, **as duas travas do corpo deste documento caem**:

| Trava | Com `criativos-personagens/` | Com o material de avatar |
|---|---|---|
| ~22s contínuos limpos | ❌ máximo 19,50s | ✅ **57,10s** e **26,10s** |
| Faixa limpa preenche 1170×2034 | ❌ 51% (só o topo servia) | ✅ **frame cheio limpo** → escala 1,083× cobre |
| Gênero coerente com a copy verbatim | ❌ mulher sobre copy de homem | ✅ **homem** |
| PII de terceiro | ❌ dentro do recorte | ✅ fora do trecho (a1 não tem nenhuma) |

**Recomendação:** trocar os slots 3 e 4 para `a1-homem-velho` e `h2-grisalho-52`. As duas escolhas femininas do corpo deste documento (`AD05-P1`, `AD05-P3`) ficam registradas como o melhor possível *dentro de `criativos-personagens/`* — que era a pasta errada.

## Ressalva de método

O detector me enganou **mais duas vezes** nesta varredura, sempre no mesmo sentido: acusou `a1-homem-velho` e `versao-A-mudo` como 100% sujos. Causas medidas — a luminária laranja da sala do a1 dispara o detector de faixa vermelha; a camisa/tee escura dispara o de "metade de baixo escura". O contact sheet a 1 fps desmentiu os dois. **Todos os números deste adendo saem de detector conferido contra a imagem.**

Também descartei o teste de watermark por "pixel congelado" aqui: em vídeo de avatar com câmera travada o fundo estático é esperado, então o teste não separa marca d'água de parede parada. A ausência de watermark nos dois escolhidos vem da varredura visual dos contact sheets, não desse número.

## Nada pago

Nenhuma geração disparada no adendo. Só `ffprobe`/`ffmpeg` local.

---

# ADENDO 2 — contagem de rostos masculinos no pool spy-zap

**Pergunta do Isca:** quantos rostos masculinos **distintos**, com **≥22,0s contínuos limpos**, existem no pool `ingles-17-08 + cr02 + cr05 + base-ingles + 23-02-spy-en-es`, **excluindo o EN7** (o controle)? Ele precisa de 4; o Bisturi diz 3.

## RESPOSTA (corrigida): **4** passam nos 22s. ~~3~~

> ⚠️ **Correção 2026-09-01 — cedi ao Bisturi, depois de medir por conta própria.**
> Eu havia reportado **3**. São **4**. O 4º é o barbudo do `cr05/` (= 23-02 CR05, mesmo homem).
> **Meu erro tem causa nomeável:** na linha do `cr05/` da minha tabela eu escrevi "—" na minha
> coluna e **carreguei a reprovação dele**, que tinha medido só a **V1**. Nenhum de nós dois mediu
> as variantes. Ou seja: meu "3" e o "3" dele não eram duas medições independentes — era **a mesma
> medição contada duas vezes**, e o acordo entre nós não valia o que eu disse que valia.
> Reconferi agora com sheet a 1 fps: **V3 = 51,0s** (`ffprobe` 51,038s) e **V6 ≈ 50s** de
> `ffprobe` 56,913s, ambas com o rosto limpo do começo ao fim, recorte posto **acima da legenda** —
> mesmo desvio que o recorte do controle faz com o painel de celular. A V2 cai mesmo (barra
> vermelha queimada dentro do recorte). Frames: `frames-pool-lote4/band-cr05-v3.jpg` e `-v6.jpg`.
> **Lição:** "—" na minha coluna significa que eu não medi. Não posso somar isso como concordância.

Contado por caminho independente do Bisturi, e **batemos no número**.

### Como medi

Banda do rosto (`crop=1440:1000:0:0`), contact sheet a **1 fps**, olhado tile a tile. Gênero e identidade **sempre na imagem**, nunca no nome do arquivo.

### O mecanismo que explica tudo (e no qual eu e o Bisturi convergimos)

**O EN7 é o único do `ingles-17-08` sem takeover de tela cheia.** Medi os 57 tiles: rosto limpo e frontal em **todos**, painel nenhum invade a banda. Os outros **alternam** talking head com painel de app em tela cheia — por isso o EN7 virou controle, e por isso os irmãos dele não servem.

### Gênero no `ingles-17-08` (10 arquivos)

| Mulheres | Homens |
|---|---|
| EN1, EN2, EN3, EN4, EN5, EN6 | EN7 (controle, excluído), **EN8, EN9, EN10** |

### Janela contínua limpa — onde cruzo com o Bisturi

| Arquivo | Meu número | Bisturi | Veredito |
|---|---|---|---|
| EN7 (controle) | **57s** (sem takeover) | idem | excluído por definição |
| EN8 | ~16s | 16,5s | ❌ |
| **EN9** | **~10s** | *não listado* | ❌ |
| EN10 | ~12-13s | 13,5s | ❌ |
| 23-02 CR01 / CR05 / CR07 | — | 15,0 / 17,2 / 13,0s | ❌ |
| `cr05/` V1 | — | overlay EVIDENCE/SUSPICIOUS na janela | ❌ |
| **`cr05/` V3 e V6** (mesmo homem) | **51,0s e ~50s** | ≥22,0s | ✅ **o 4º** |
| **base EN-01 / EN-02 / EN-03** | — | **≥22,0s** | ✅ **os 3** |
| `cr02/` (7 arquivos) | **nenhum homem** — é a mesma atriz nos 7 | — | ❌ |

### ⚠️ Divergência de identidade: são **9** rostos, não 8

O Bisturi conta 8 masculinos fora o EN7. Falta o **`ingles-17-08/VIDEO EN 9 ZAP 17.08 PL.mp4.mp4`**.

**Não é o EN8** — conferido lado a lado em `frames-pool-lote4/cmp-en8-vs-en9.jpg`:

| | EN8 | EN9 |
|---|---|---|
| Pele | mais clara | mais escura |
| Cabelo | ondulado, volumoso | raspado |
| Roupa | camisa azul de colarinho | jaqueta escura |
| Cena | carro de dia, árvores | carro à noite, flare de luz forte |

**Não muda a resposta** (EN9 dá ~10s), mas a contagem de identidade do pool é **9**.

### O gate que decide de verdade: enquadramento

O Bisturi achou o que derruba os aprovados do `base-ingles`. ⚠️ **O número dele mudou** — ele mesmo corrigiu depois: casar por **largura de cabeça** superestima (~~3,0×–4,5×~~). Por **altura de placa**, que é o método que ficou: **pool 2,34× · controle 0,86×** — o controle foi **reduzido**, nunca ampliado.

**Fiz bem em não confirmar o número com medição minha** — ele estava inflado, e o próprio Bisturi o retirou. Confirmo o fenômeno, não o pixel. Na imagem (`frames-pool-lote4/base-enquadramento.jpg`) é inequívoco: o controle é selfie fechada, os 3 do `base-ingles` são plano médio de mesa com o ator pequeno num split com painel de app. Meu bounding box de pele **não serve pra confirmar o número** — contaminou (o fundo bege quente do EN7 deu 1440px, e as mãos gesticulando dos três entram na conta). Onde não tenho medição limpa, o número do Bisturi vale mais que o meu.

## Consequência pra decisão do Gusta

**Dentro do pool: 0 rostos aproveitáveis** na moldura do controle. Os 3 que passam nos 22s pedem upscale de 3–4,5×.

**Mas o lote não precisa cair.** O material do ADENDO 1 está fora do pool e é **nosso**:

> ⚠️ **Retratação minha (2026-09-01, número do Bisturi).** Eu escrevi que os avatares
> **"não precisam de upscale nenhum"**. ~~Errado.~~ Eu estava comparando **frame com frame**
> (1080 → 1170 de largura = 1,083×), que é escala de moldura. A pergunta que importa é outra:
> **quanto ampliar pra a CABEÇA casar com a do controle** — e aí os avatares são plano médio,
> cabeça de **240–360px** contra ~96% da largura no controle, o que dá **3,1×–4,7×**.
> Os avatares **não são isentos do mesmo custo que reprovou o pool**. O que os mantém escolhidos
> é outra coisa, e é preciso dizer qual: **avatar de IA amplia limpo** e na imagem ficou melhor
> que o controle — não é que não amplie.

| Arquivo | Janela limpa | Enquadramento |
|---|---|---|
| `roteiro-e-2026-08-31/avatares/CRIATIVO-a1-homem-velho.mp4` | **57,10s** | **frame cheio**, sem legenda/painel/PII — mas plano médio: casar a moldura custa 3,1–4,7× |
| `lote-5-avatares/final-h2-grisalho-52.mp4` | **26,10s** (8,10→34,20s) | frame cheio a partir de 8,10s |
| `sophia-jones-avatar-homem-38/versao-A-mudo.mp4` | 34,10s | frame cheio (arquétipo colado no da Isabella) |
| `lote-5-avatares/final-h1-jovem-27.mp4` | 26,10s | frame cheio a partir de 8,10s |

São **4 homens distintos, todos ≥22s, todos frame cheio limpo**. Com eles o lote 4 sai inteiro.

⚠️ **A vantagem deles não é "não amplia" — é "amplia limpo".** Corrigido acima. O número (3,1–4,7×)
está registrado no README e no portal pelo Bisturi.

**A decisão que sobra pro Gusta não é "4 ou 3 peças"** — o pool também fecha 4, agora que o `cr05`
V3/V6 entrou. É **"pool do swipe, ou material de avatar nosso"** — e como os dois lados pedem
ampliação, o critério vira **qual amplia melhor**, não qual amplia menos. Foi por isso que os
avatares ganharam: filmagem de celular esticada borra, avatar de IA não.

## Nada pago

---

# ADENDO 3 — régua única (IOD) e conferência das placas

## A régua que ficou: distância interocular

O Bisturi recalculou por **IOD (pupila a pupila)** — marco rígido, imune ao volume de cabelo e à cabeça virada, que era o mecanismo que inflava a largura de cabeça. Alvo: IOD da placa do controle, **511px em 1170 de largura**.

| | IOD na fonte | Fator até a placa |
|---|---|---|
| controle EN7 | 249px | **2,05×** |
| slot4 `a1-homem-velho` | 215px | 2,38× |
| pool `base EN-03` | 180px | 2,84× |
| slot3 `sophia-homem-38` | 156px | 3,27× |
| slot2 `h2-grisalho-52` | 145px | 3,58× |
| slot1 `h1-jovem-27` | 132px | 3,87× |
| pool `base EN-02` | 111px | 4,60× |
| pool `base EN-01` | 103px | 4,96× |

**Duas retratações do Bisturi que mudam o argumento:**

1. **O controle foi AMPLIADO 2,05×** — não ~~reduzido 0,86×~~. Aquele 0,86× saiu do mesmo bbox de pele contaminado que me fez recusar confirmar o número dele. **O molde nunca foi "sem upscale": ele já nasceu a 2×.**
2. **O pool é PIOR que os avatares** — não ~~melhor~~. Na régua certa: pool **2,84–4,96×**, avatares **2,38–3,87×**. O ~~2,34×~~ do pool era ajuste de moldura (2532 ÷ altura da fonte), sem casamento de cabeça nenhum — não media a mesma coisa.

> A decisão pelos avatares estava certa e agora está certa **pelo motivo certo**. Não é "o pool amplia e o avatar não" (minha frase errada), nem "o pool amplia menos" (a dele) — é que **os dois ampliam, o avatar amplia menos e aguenta melhor**.

Aritmética conferida por mim (511/249 = 2,05). **Os valores de IOD em si eu não confirmo** — não tenho medição limpa de marco facial, e disse isso antes de aceitar.

## Conferência das placas — passam

- **`ffprobe`:** os 4 slots batem com o controle **exatamente** — `1170×2532 · 660 frames · 22,000000s` nos cinco.
- **Eixo dos olhos:** montei tira dos 5 com linha desenhada em **y=1236** (olhos do controle). Nos arquivos **`-close`** os olhos caem na linha nos quatro, dentro da tolerância declarada (spread IOD 1,4%, eixo Y 2,5%). Slot3 praticamente em cima; slot2 e slot4 um pouco abaixo — consistente com os 1216 e 1280 dele.
  Evidência: `frames-pool-lote4/verif-eixo-olhos-close.jpg`

## ⚠️ Achado: "plano" significa enquadramentos OPOSTOS nos dois lotes

Os `slotN-plano.mp4` do lote 4 **não** alinham — olhos ~100–140px **acima** da linha do controle em t=5s. Isso **não é defeito**: `-plano` é o plano aberto e `-close` é o que casa a moldura.

O problema é o **nome**:

| Lote | Arquivo que casa a moldura | O outro |
|---|---|---|
| Lote 3 | `rosto-**plano**.mp4` (fechado — conferido) | `rosto-conformado.mp4` (também fechado) |
| Lote 4 | `slotN-**close**.mp4` | `slotN-**plano**.mp4` (**aberto**) |

**Risco concreto:** quem seguir o padrão do lote 3 e pegar `slotN-plano` leva um rosto ~2× pequeno demais pro lipsync — exatamente a família de erro que o Bisturi acabou de corrigir (slot3 25% apertado, slot4 rosto 740px alto). E a esteira já mostrou hoje que erro viaja rápido quando o nome parece óbvio.

Sugestão passada ao dono do arquivo (não mexo em arquivo que não é meu): renomear `slotN-close` → `slotN-conformado`, casando com o vocabulário do lote 3, ou deixar explícito no README qual dos dois vai pro lipsync.
Comparativo: `frames-pool-lote4/verif-nomes.jpg`

## Nada pago
