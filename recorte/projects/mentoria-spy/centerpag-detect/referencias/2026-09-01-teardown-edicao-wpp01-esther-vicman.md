---
tipo: referencia-criativo
atualizado: 2026-09-11
tags: [teardown, edicao, spy-zap, centerpag, vencedor-swipe, whatsapp, card-flutuante]
fonte: https://www.facebook.com/ads/library/?id=1762552938111855
ad_id: "1762552938111855"
arquivo_peca: centerpag-detect/escalados/whatsapp/01-esther-vicman-1762552938111855.mp4
---

# Teardown de EDIÇÃO — wpp-01 Esther Vicman (1762552938111855)

56,77s · 360×640 · 30fps · locução masculina em inglês.

Este teardown cobre **só a edição** — layout, medidas, fases e cortes. A copy, os 7 blocos de
roteiro e as alavancas de persuasão já estão em [[criativo-wpp01-1762552938111855]] e **não são
repetidos aqui**.

## Arquivo da peça (pro portal)

Caminhos **relativos a `projects/`**:

| O que | Caminho |
|---|---|
| **Vídeo (exibir este)** | `centerpag-detect/escalados/whatsapp/01-esther-vicman-1762552938111855.mp4` |
| **Poster** | `centerpag-detect/escalados/whatsapp/01-esther-vicman-1762552938111855-thumb.jpg` |
| **Texto do anúncio** | `centerpag-detect/escalados/whatsapp/01-esther-vicman-1762552938111855.txt` |
| Registro | `centerpag-detect/manifest.json` → `ad_id 1762552938111855` |
| Frames de medição | `centerpag-detect/referencias/medicao-wpp01-2026-09-01/` |

`.mp4` 1.743.046 bytes, md5 `31d9b6a30c53905c1ae2ac57f1a9b830` — conferido contra o `manifest.json`.

⚠️ **Existem 4 cópias no repo.** `escalados/whatsapp/01-…` (canônica), `anuncios/esther-vicman-…`
e `mentoria-spy/gram-detect/escalados/top3-ig-e-whatsapp/wpp-01-…` são **byte a byte a mesma**
(md5 idêntico). As de `tratados/` têm metadados zerados e md5 diferente — **não usar**. Exibir a
de `centerpag-detect/escalados/whatsapp/`.

> ⚠️ Mídia pesada não entra no git: o portal referencia o arquivo no disco.

---

## COPY DO VENCEDOR — reproduzir como está

> Extraída do `.txt` da peça e conferida campo a campo contra o `manifest.json`
> (`ad_id: 1762552938111855`) — os dois batem. Sem reescrever, sem traduzir.

**Texto principal (primary text)**

```
2.4M people already stopped torturing themselves with 'what if.' They chose to know.👇
```

**Título (headline)**

```
Free Test ✅
```

**Descrição**

```
(vazia — o anúncio não usa o campo)
```

**Botão (CTA)**

```
Ver detalhes
```

**Link de destino**

```
GO.CENTERPAG.COM
```

---

## Sinal de escala — melhor que o do lote 1, mesma limitação

| | Lote 1 (GRAM) | **Este (ZAP)** |
|---|---|---|
| Rank de impressões | #1 de 27 | **#1 de 87** |
| Dias no ar | 3,2 | **16,1** |
| Peças no mesmo ângulo | 6 | **29** |
| Corpus de escalados | 13 | **26** |

> ⚠️ **É a mesma limitação de Ad Library, com sinal melhor.** A Meta continua sem publicar gasto,
> CTR, CPA ou ROAS — nada de performance foi verificado. O que melhorou é a **qualidade do proxy**:
> 16,1 dias no ar é sobrevivência de verdade (um anúncio que não paga é pausado antes disso),
> contra os 3,2 dias do lote 1, que ainda eram tração inicial. Continua sendo *sinal de
> sobrevivência*, não campeão medido.

---

## ⚠️ Correção: **não é split screen**

A ficha do wiki e a transcrição do lote 1 descrevem esta peça como *"split screen vertical:
talking head em cima + screen recording embaixo"*. **Medido, não é.**

É **talking head em quadro cheio** com um **card de celular semitransparente composto por cima**
da metade de baixo. O ombro e a jaqueta do ator aparecem **dos dois lados do card** e o corpo dele
é visível **através** do card, que tem cantos arredondados e borda com alpha.

Consequência prática pro Bisturi: **não dá pra montar isto empilhando blocos.** Não existe uma
faixa que separe head de painel. É composição com transparência sobre um plano único.

Ver `medicao-wpp01-2026-09-01/02-card-borda-suave.png` — o card sobre a jaqueta, sem borda dura.

---

## O que é medível, e o que não é

Método: [[medir-fronteira-de-bloco-em-video]] — é referência de terceiro, então variância temporal,
com o teste de margem. **A regra de margem foi aplicada e reprovou a maior parte das fronteiras.**

| Fronteira | Medida | Margem | Vale? |
|---|---|---|---|
| **Fim da matte preta do topo** | **y = 96** (15,0% da altura) | — (por fração de preto: 100% até y96) | **sim** |
| Linha de texto 1 do hook | y ≈ 20–45 | — | é texto, não fronteira |
| Linha de texto 2 do hook | y ≈ 54–75 | 1,42× | **falso positivo** |
| "Fronteira" do card (variância, t2–8s) | y = 529 | 4,51× | **falso positivo** — é borda interna da UI |
| Borda lateral esquerda do card | x ≈ 78 / 127 | 0,54× / 0,82× | **não decidível** |
| Borda lateral direita do card | x ≈ 258 / 215 | 0,80× / 1,31× | **não decidível** |

**Três armadilhas apareceram nesta peça, e valem pro método:**

1. **Margem alta e ainda assim a fronteira errada — e isso refina a regra de 2×.** O detector
   devolveu `y=529` com margem **4,51×**, bem acima do corte, e aquilo é uma borda interna da UI,
   não o topo do card. A linha desenhada sobre o frame mostra na hora
   (`01-matte-e-falsos-positivos.png`).

   **Não é bem um contraexemplo ao corte de 2×** — é a descoberta de uma **pré-condição que faltava**
   nele. A margem mede se uma transição é *detectável com robustez*; ela não sabe dizer se aquela é
   *a transição que você procura*. Aqui o topo do card **não existe** como degrau (o card é
   alfa-composto), então o detector achou a borda real mais forte disponível e a reportou com toda a
   confiança. Margem alta sobre a fronteira errada é pior que margem baixa, porque não avisa.

   **A regra passa a ter dois passos:** primeiro estabelecer que a fronteira existe (o bloco tem
   borda dura?), só depois medir a margem. Sem isso, 4,51× é confiança em cima de nada.
2. **Duas janelas, duas respostas.** A borda inferior da faixa deu `y=77` numa janela e `y=54`
   noutra. As duas eram linhas de texto do hook. Foi a **fração de preto** que resolveu: a matte é
   100% preta até `y=96` e só então a imagem começa.
3. **Não havia fronteira pra achar.** As laterais do card falharam em todos os detectores porque o
   card é alfa-composto: a borda é um gradiente, não um degrau. Detector nenhum acha o que não
   existe.

---

## Layout medido

```
┌──────────────────────────────┐  y 0
│  MATTE PRETA + HOOK FIXO     │  15,0%   ← 2 linhas de texto amarelo, o vídeo inteiro
│  "WHAT THEIR / WHATSAPP…"    │
├──────────────────────────────┤  y 97
│                              │
│   TALKING HEAD — QUADRO      │
│   CHEIO (plano único)        │  85,0%
│                              │
│      ┌──────────────┐        │
│      │ CARD DO APP  │        │  ← composto POR CIMA, semitransparente,
│      │ semitranspa- │        │     cantos arredondados, sem borda dura.
│      │ rente        │        │     Cresce e toma a tela ao longo da peça.
│      └──────────────┘        │
└──────────────────────────────┘  y 640
```

- **Matte do topo:** `y 0–96` (15,0%). Preta chapada, 100% de cobertura. Carrega o hook fixo
  `WHAT THEIR WHATSAPP IS HIDING...` em amarelo, 2 linhas, caixa alta — **nunca muda**.

  > **Nota 2026-09-11 — a fronteira da matte é fade, não degrau** (remedição do Bisturi, lote
  > `zap-wpp01-clone-3-ganchos-2026-09-11`). O `y=96` acima **fica**: é o limiar de fração de preto
  > e continua dentro da faixa medida. Remedido com 58 frames (1–30 s, 2 fps), luminância em numpy,
  > colunas de margem `x 0–30` e `330–360` (fora do texto), em 360×640:
  >
  > | medida | valor |
  > |---|---|
  > | 100 % preta (luma < 20, frame médio) até | **y = 93** (frames isolados, luma < 16: 87 / 89; 5 colunas: 93 / 94 / 103 / 103 / 101; `README-l10` do lote EX já anotava 91–97 — mesma faixa, depende do limiar) |
  > | std temporal na matte pura (y 0–20) | 0,03 |
  > | **std temporal em y 85–95** | **1,7 → 2,5** — 50–80× a da matte pura: o vídeo já atravessa ali |
  > | 10 % / **50 %** / **90 %** do platô de variância (17,0 em y 130–200) | y 67 / **125** / **141** |
  > | penhasco (argmax do diff, y 80–125) | **não existe** — margens 1,01–1,19×; o argmax cai em y 113–125 conforme a coluna |
  >
  > **Leitura:** a matte é um **fade de ~50 px** (100 % preta até y 93, 50 % do platô em y 125,
  > 90 % em y 141), não uma borda. **Não existe penhasco** — a regra *existe-fronteira → só então
  > meça margem* vale aqui: **a matte tem início, não borda.** A fração de preto dá o início; o
  > platô da variância dá o fim; nenhum dos dois é "a fronteira". Em 1080p: início ≈ 279, meio ≈ 375,
  > fim ≈ 423 — o nosso molde L10 corta seco em `y 288` (= 96 × 3).
  >
  > **Evidência:** `centerpag-detect/criativos/zap-wpp01-clone-3-ganchos-2026-09-11/conferencia/original-zoom-matte.jpg`
  > (zoom ×8, luma ×6, t = 2 / 12 / 25 s: a silhueta do microfone/abajur atravessa as linhas de
  > y 90 / 93 / 96 até quase o texto) e a seção "Medição do original" do `README.md` do mesmo lote.
  >
  > **Consequência pro molde: nenhuma neste lote.** O lote de 11/09 varia uma alavanca só (gancho) e
  > o corte duro em 288 já rodou nas EX A/B/C — trocar agora seria alavanca extra. O fade fica como
  > **opção de lote futuro** (proposta do Bisturi: substituir o `pad … :black` do `[actor]` por um
  > gradiente preto de y 240 → 420 em 1080p, uma linha no `remontar-l10.py`, custo zero). Registrado
  > no wiki em [[matte-em-fade-nao-tem-penhasco]].
- **Legenda karaokê:** amarela, 2–4 palavras, centro-baixo, sincronizada com a fala. Vive **sobre**
  o card, não em faixa própria.
- **Watermark:** `zapem/whatstalker.com` discreta, dentro do card.
- **Card:** sem geometria fixa — muda de tamanho e posição por fase. Não medível como bloco.

**Diferença estrutural pro lote 1 (L9):** lá eram 3 blocos empilhados com fronteiras duras e uma
faixa de hook opaca no meio; aqui é 1 plano + overlays. São gramáticas de edição diferentes, e o
molde do L9 **não serve** pra esta peça.

---

## As 5 fases (cortes medidos por detecção de cena)

Transições no quadro inteiro: `0,03 · 8,80 · 30,77 · 40,00 · 41,70 · 49,03 · 49,67 · 50,53 · 50,90 · 52,07`

| Fase | Tempo | O que está na tela |
|---|---|---|
| **1 — Chats** | 0,0–8,8 | Head cheio + card do WhatsApp falso (`Chats`, contatos borrados `Sec*****`/`Ex ⚠️`/`Bab*`, tarja `147 deleted messages recovered!`) |
| **2 — Acesso** | 8,8–30,8 | Card vira `Accessing WhatsApp… +1 3347950651` com loader, depois terminal `root@zapspy:~#` rolando. **O head ainda está lá o tempo todo** |
| **3 — Terminal cheio** | 30,8–40,0 | O card toma a tela. **O head desaparece.** Terminal + `Recovering deleted data… 65→98%` + `SMS INTERCEPTED` + `DELETED DATA FOUND!` |
| **4 — Payoff** | 40,0–49,0 | Lista de conversas em tela cheia, tags `DELETED`/`SUSPICIOUS`/`EVIDENCE`, badges vermelhos, barra verde `Unlock all conversations — Access expires in 09:57` **com timer regressivo** |
| **5 — CTA** | 49,0–56,8 | Tela borra e entra `CLICK THE LINK BELOW AND SEE THE TRUTH NOW` em amarelo + setas ⌄⌄⌄ animadas |

**O corte que importa é o de 30,8s.** É onde o ator sai de cena e não volta — 54% da peça. A partir
dali são 26 segundos de interface pura com a locução por cima. O rosto serve pra abrir e sustentar
o argumento; a prova é entregue sem ele.

**O timer é real:** `09:57` na fase 4 → `09:40` no fim. Conta pra trás dentro do próprio print.

---

## O vencedor é representativo? (corpus de 26)

Esta é a leitura que o lote 1 não teve — lá o corpus era 13, aqui é 26.

**Na copy, sim — é o ângulo dominante:**

| Ângulo dentro do Tier A | Peças |
|---|---|
| **`2.4M people already stopped torturing themselves…`** ← o vencedor | **9 de 26** |
| (agrupados, sem texto exposto) | 6 |
| `Try the app for free now and discover the whole truth.` | 6 |
| `Oh my god, I was in shock when I found all those messages!` | 5 |

No corpus inteiro (87), esse ângulo roda **29 vezes** — é o mais repetido da conta.
A headline `Free Test ✅` é 6 de 26, atrás de `Free trial: enter your partner's phone number` (7).

**No formato, não — é raro.** Testei a assinatura estrutural do vencedor (matte preta no topo com
texto de hook congelado) nas 22 peças mensuráveis:

| Peça | Matte | Hook congelado |
|---|---|---|
| **#01 Esther Vicman (vencedor)** | 26 linhas | **sim** |
| #08 Kendall Godfrey Stephanie | 27 linhas | **sim** |
| #11 Fernanda Mello | 27 linhas | **sim** |
| #03 Emilly Bredoff | 18 linhas | limítrofe (matte curta) |
| as outras 18 | 0 | não |

**Só 3 a 4 de 26 rodam o molde do vencedor.** O resto se divide em: talking head com **celular
físico na mão** apontando pra tela (#02, #06, #10, #20, #23 — "here click on"), talking head puro
(#07, #16, #24), banner sanduíche (#11), mockup gráfico (#12), e grade de 4 (#05).

> **Leitura:** o vencedor combina a **copy mais validada da conta** com uma **edição rara**. A copy
> tem 29 peças de lastro; a edição tem 3. Se for modelar, isso separa o que já está provado
> (o ângulo) do que é aposta do próprio anunciante (o molde).

### ⚠️ Ele não é o mais antigo — e isso importa

| Dias no ar | Peça | Ângulo |
|---|---|---|
| **35,1** | #06 Isabella Walker, #10 Lauren Roberts, #20 Gonçalo Antunes | `See this before it's too late...` |
| 17,1 | #04 Alberto Souza | `See today everything that happens...` |
| **16,1** | **#01 Esther Vicman (este)**, #03 Emilly Bredoff | `Free Test ✅` |

O vencedor é **#1 em impressões mas 5º em sobrevivência**. Três peças rodam há **35 dias** com um
ângulo diferente — e são curtas (21–23s) contra os 57s daqui. O README do swipe já as chama de
"núcleo validado". **Candidato natural pro lote 3**, e por um caminho barato: 22s custa um terço
do lipsync desta.

### Reuploads confirmados por duração

`#02 Alberto Souza` = `#10 Lauren Roberts` (22,27s, md5 diferente) · `#07 Esther Vicman` =
`#24 Victorai Martins` (62,95s, e os dois em **480×360 deitado**) · `#25` = `#26 Sara Oliveira`
(62,18s, mesmo roteiro com **atrizes diferentes** — teste de talento com script travado).
Espalhar o vencedor por várias Páginas é padrão da conta pra diluir risco de bloqueio.

---

## O que o Bisturi precisa saber antes de montar

1. **Não empilhe blocos.** Plano único + card alfa por cima. O molde do L9 não serve.
2. **Matte de 15% no topo** com o hook fixo — é o único bloco com fronteira medida (`y=96`).
3. **O rosto sai aos 30,8s** e não volta. 46% com rosto, 54% sem.
4. **Legenda karaokê** sobre o card, não em faixa própria.
5. **Timer regressivo dentro do print** (`09:57` → `09:40`), não na copy.
6. **57s é quase o dobro do lote 1.** Ver a nota de custo abaixo.

## ⚠️ Custo — estimar antes de disparar

O saldo é **US$17,47**. Esta peça tem **56,77s** contra os 32,5s do lote 1 — **1,75×**. No lote 1 o
lipsync do head (31,3s) custou US$2,72 com `lipsync-2-pro`, cujo `base_price` de US$0,08 é **por
unidade, não por chamada**.

**Regra pro Bisturi:** estimar por **duração × preço unitário** e **reportar o número antes de
disparar qualquer geração paga**. Ninguém gasta sem mostrar a conta primeiro. Atenuante desta peça:
só **26,0s** têm rosto — o lipsync não precisa cobrir os 57s, e essa é a diferença entre caber e
não caber no saldo.

---

## Passagem de bola

O Isca já modelou esta peça duas vezes (call-in show A/B, e breaking news + Roteiro D). Aquilo
tratou **copy e formato de roteiro**. O que este teardown acrescenta é a **gramática de edição** —
e ela contradiz o que os dois roteiros assumiram sobre split screen.
