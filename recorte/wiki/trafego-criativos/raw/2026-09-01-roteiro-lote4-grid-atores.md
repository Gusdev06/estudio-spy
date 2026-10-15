---
tipo: roteiro-criativo
atualizado: 2026-09-01
oferta: go.centerpag.com (spy zap / CenterPag)
lote: 4
estende: 2026-09-01-lote3-molde-35-dias-ator-e-locucao.md
peca-base: ../criativos/lote3-isabella-2026-09-01/pecas/lote3-isabella-s-en-a.mp4
teardown: ../referencias/2026-09-01-teardown-lote3-tres-de-35-dias.md
formato: molde dos 35 dias · eixo unico = rosto + voz
duracao: 22,000s exatos (660 frames a 30 fps) nos 4 slots
idioma: EN
tags: [roteiro, spy-zap, molde-validado, lote-4, grid-de-atores, uma-alavanca]
---

# Lote 4 — grid de 4 atores no molde dos 35 dias

**Eixo único: rosto e voz.** Tudo o mais é herdado da peça que já rodou.
Nada aqui é estimado — cada número abaixo foi medido em
`criativos/lote3-isabella-2026-09-01/`, na peça renderizada e nos arquivos de VO.

---

## 0. ⚠️ Correção ao briefing — o texto da tarja

O briefing do lote 4 lista como FIXO o texto **`CLONE YOUR WIFE'S OR HUSBAND'S / WHATSAPP RIGHT NOW`**.
**A peça que shippou não usa esse texto.** Ela usa o T1 do roteiro do lote 3:

```
YOU DON'T NEED THEIR PHONE.
YOU NEED THE NUMBER.
```

**Evidência:** `kit/tarja.png` (1170×498) e qualquer frame da peça fora da janela 14,6–19,6s —
conferi em `t=1s`, `t=6s`, `t=12s` e `t=21s` de `pecas/lote3-isabella-s-en-a.mp4`. O texto do
briefing é o da **fonte concorrente**, transcrito no teardown; não é o que está no nosso kit.

**Por que isso não é detalhe:** o lote inteiro existe pra ler efeito de **ator**. Se o slot 1
sair com a tarja do concorrente e o controle Isabella com a T1, o slot 1 passa a diferir do
controle por **tarja + rosto + voz** — três alavancas, leitura zero. Vale pros quatro slots.

**Fica valendo a T1.** Se o Gusta quiser a linha do concorrente, ela vira **um lote separado**
com o rosto travado, não uma troca dentro deste. Mandei isso direto pro Peneira e pro Bisturi.

---

## 1. FIXO — não inferir, não re-derivar

Medido na peça renderizada. Bisturi: reusar os assets, não reconstruir.

| Item | Valor medido | Onde está |
|---|---|---|
| Saída | **1170×2532, 30 fps, 660 frames, 22,000s** | `pecas/lote3-isabella-s-en-a.mp4` |
| Tarja — arte | 1170×498, verde chapado **RGB(2,150,2)** `#029602` | `kit/tarja.png` |
| Tarja — posição | **y 0–497** (498px = 19,67% de 2532) | medido na coluna x=585 |
| Tarja — texto | `YOU DON'T NEED THEIR PHONE.` / `YOU NEED THE NUMBER.` | branco `#FFFFFF`, contorno `#080808` |
| **Tarja — janela de saída** | **sai no frame 438 (14,600s), volta no 589 (19,633s)** | 5,033s fora · ON em 77,12% da peça |
| Bloco gráfico | 1170×936, ancorado embaixo → **y 1596–2532** | `kit/bloco-grafico.png` |
| Karaokê — card | 1170×220, **y 1676**, x 0, texto centralizado | `kit/karaoke/k*.png` |
| Karaokê — cor | branco `#FFFFFF` · keyword **`#25D366`** (verde do WhatsApp) · contorno `#080808` | amostrado dos PNGs |
| Rosto | quadro cheio, **100% da peça**, do 1º ao último frame | define o custo do lipsync |
| Ordem dos beats | B1→B7, imutável | seção 2 |

**A tarja sai exatamente no início do B6.** Frame 438 é o mesmo frame em que o B6 começa —
não é aproximação, é o mesmo número. E volta 0,888s depois do B7 ter começado. Regra pro Bisturi:
**tarja fora = janela do B6 + os primeiros 0,9s do B7.** Vale igual nos 4 slots, porque a grade
de tempo é a mesma (seção 2).

**Travas herdadas do lote 3, seguem de pé:** nenhum lower third, nome, idade ou número de
resultado sobre o rosto (é o que separa UGC de depoimento fabricado) · toda conversa, nome, foto
e prévia entram borradas · nenhum número de interface vira alegação na copy.

---

## 2. A grade de tempo — medida, não estimada

De `vo/plano.json` do master de 22,000s. **Os 4 slots rodam esta grade sem alteração.**

| Beat | Início | Fim | Duração | Frames | Job |
|---|---|---|---|---|---|
| B1 | 0,000 | 2,578 | 2,578s | 0–77 | confissão em 1ª pessoa |
| B2 | 2,578 | 5,595 | 3,017s | 77–168 | desarme de dificuldade |
| B3 | 5,595 | 8,377 | 2,783s | 168–251 | os dois passos |
| B4 | 8,377 | 11,160 | 2,783s | 251–335 | a máquina conecta sozinha |
| B5 | 11,160 | 14,616 | 3,456s | 335–438 | o payoff |
| B6 | **14,616** | 18,745 | 4,129s | **438**–562 | quebra de objeção · **tarja sai aqui** |
| B7 | 18,745 | 22,000 | 3,255s | 562–660 | CTA · tarja volta no frame 589 |

**Por que a grade não muda entre os slots:** o slot 2 tem copy própria, mas foi escrita com a
**mesma contagem de palavras por beat** do slot 1 (seção 4). Então cai no mesmo timeline,
com a mesma marca de tarja e o mesmo ponto de entrada do bloco gráfico. Uma alavanca só,
inclusive no slot que troca a copy.

---

## 3. ⚠️ O ritmo — a descoberta que decide a produção dos 4 VOs

Isto é novo e vale mais que o resto do documento. O lote 3 previu por errata que a voz leria
devagar demais; a produção confirmou, e a correção **não foi cortar texto, foi acelerar**.

| | Palavras | Duração | wpm |
|---|---|---|---|
| TTS cru (soma dos 7 mp3) | 69 | **26,388s** | **156,9** |
| Master fitado (o que shippou) | 69 | **22,000s** | **188,2** |
| Fonte — Isabella #06 | 66 | 21,34s | 186 |
| Fonte — Lauren #10 | 66 | 22,27s | 178 |
| Fonte — Gonçalo #20 | 70 | 23,34s | 180 |

Durações cruas por beat: 3,060 · 3,600 · 3,312 · 3,312 · 4,140 · 4,968 · 3,996 = **26,388s**.
Fator aplicado: **26,388 ÷ 22,000 = 1,1995** (atempo ≈ **1,20**, +20%).

**O modelo `minimax/speech-2.6-hd` lê a ~157 wpm. O molde precisa de ~188 wpm.** Cru, a peça
sairia mais lenta que as três fontes; fitada, cai dentro da faixa validada. **Toda voz nova
precisa deste passo de fit**, e o fator muda com a voz.

**Receita pro Bisturi, por slot:**
1. Escrever/usar **66–70 palavras** (as duas copies deste doc têm 68 e 69).
2. Gerar os 7 beats separados, medir a soma crua.
3. `atempo = soma ÷ 22,000`. **Tem que cair entre 1,15 e 1,25.**
4. **Fora dessa faixa a voz está errada, não o texto.** Trocar a voz — não cortar palavra,
   não esticar a peça. A duração é trava do lote.
5. Recortar os beat starts da seção 2 sobre o master fitado.

⚠️ **Lacuna registrada:** o `vo/jobs.log` do lote 3 **não gravou o `voice_id`** — só a resposta
do job. Sem isso não dá pra provar que as 4 vozes são distintas da do controle. **Anotar o
`voice_id` de cada slot no log desta vez.** É a alavanca do teste; se ela não for auditável,
o lote não é lido.

⚠️ **wpm é proxy.** Mede andamento, não como a fala cai no ouvido, e as contagens vêm de
transcrição (não contam pausa). Dá pra afirmar que o andamento entra na faixa da fonte; não dá
pra afirmar que soa bem.

---

## 4. Os 4 slots

| Slot | Papel no teste | Copy | VO a produzir | Voz |
|---|---|---|---|---|
| **1** | rosto+voz novos, copy do controle | **idêntica ao controle** (seção 5) | `vo/vo-slot1-en.m4a` | V1 — masculina, ≠ controle |
| **2** | variante de copy | **própria** (seção 6) | `vo/vo-slot2-en.m4a` | V2 — masculina, ≠ V1 |
| **3** | rosto+voz novos, copy do controle | **idêntica ao controle** (seção 5) | `vo/vo-slot3-en.m4a` | V3 — masculina, ≠ V1/V2 |
| **4** | rosto+voz novos, copy do controle | **idêntica ao controle** (seção 5) | `vo/vo-slot4-en.m4a` | V4 — masculina, ≠ V1/V2/V3 |
| *(controle)* | *já existe* | *— * | `lote3-isabella-2026-09-01/vo/vo-master-en.m4a` | *V0* |

**São 4 vozes novas + a do controle = 5 leituras distintas da mesma copy em 3 slots.**
Slots 1, 3 e 4 rodam o mesmo texto que o controle: **3 rostos novos sobre copy idêntica** é a
leitura limpa de ator. O slot 2 é o único que move a copy, e move só ela.

**Todas as vozes masculinas.** As três fontes de 35 dias têm F0 de 105,3 / 108,1 / 109,6 Hz —
homem falando de uma parceira. Trocar o gênero da fala junto com o rosto seria a segunda alavanca.

> **Os nomes do briefing são das Páginas do concorrente, não dos nossos atores.** "Slot 1 =
> Lauren Roberts" quer dizer *o slot que modela a peça #10*, não que exista uma atriz Lauren.
> Mesma correção que o lote 3 já tinha registrado. E como a duração é travada em 22,000s nos
> quatro, a diferença de grade entre as fontes (21,3 / 22,3 / 23,3s) **não se propaga** — ela
> viraria uma alavanca a mais.

### Rostos — o que existe e o que falta

Pool em `projects/mentoria-spy/criativos-personagens/` (10 clipes 1080×1920, 23–31s).
**Só 3 são masculinos:**

| Arquivo | Cena |
|---|---|
| `AD04 - PERSONAGEM 1.mp4` | homem barbudo, camiseta verde escura, escrivaninha |
| `AD04 - PERSONAGEM 2.mp4` | homem jovem, cabelo cacheado, camiseta navy, sala de jantar |
| `AD05 - PERSONAGEM 2.mp4` | homem cabelo escuro, barba por fazer, sala de estar |

⚠️ **Faltam faces.** São 3 masculinas pra 4 slots, e o rosto do controle **não sai desse pool**
(é outro ator, cabelo claro). A quarta precisa vir de `criativos-crus/spy-zap/` — decisão do
Bisturi, é território dele. Registro aqui só pra ninguém descobrir isso no meio da montagem.

⚠️ Os 10 clipes têm **overlay queimado da oferta gram** (painel "Connecting to Instagram…",
tarja vermelha de hook). O crop fechado no rosto que o Bisturi já usou no controle resolve —
mas é passo obrigatório, não opcional.

---

## 5. COPY DOS SLOTS 1, 3 e 4 — verbatim, palavra por palavra

**É o texto de `criativos/lote3-isabella-2026-09-01/vo/beats-en.txt`, sem uma vírgula de
diferença.** Não reescrever, não melhorar, não traduzir, não adaptar o tom. Copiar.

```
B1  Last month I stopped guessing about my relationship.
B2  It took me about a minute, and I never touched her phone.
B3  You type the number in, and you press check.
B4  It connects on its own — you just wait.
B5  Then you see the conversations someone was sure had already disappeared.
B6  No password. Nothing installed. You never need the phone in your hand.
B7  See it yourself, before you spend another week wondering.
```

**69 palavras.** A 22,000s = 188,2 wpm, dentro da faixa das três fontes.

**Gênero:** só o **B2** é gendered (`her phone`). O par masculino é uma palavra: `his phone`.
Se rodar os dois, vão em **conjuntos de anúncio separados** — nunca no mesmo. A peça é o eixo;
o público é a copy.

### As 24 linhas de karaokê — copiadas dos cards que shippou

`kit/karaoke/plano.json` + os PNGs renderizados. **Keyword em verde `#25D366` em negrito;
o resto branco.** Card sem negrito = **card inteiro branco** — não é esquecimento, é o padrão:
linha de setup fica branca, o verde marca o payoff. São **14 verdes em 24**, e essa proporção
é parte do molde.

| # | Início | Fim | Linha (keyword em **verde**) | Beat |
|---|---|---|---|---|
| k01 | 0,000 | 0,829 | LAST MONTH I | B1 |
| k02 | 0,829 | 1,659 | STOPPED **GUESSING** | B1 |
| k03 | 1,659 | 2,488 | ABOUT MY **RELATIONSHIP** | B1 |
| k04 | 2,578 | 3,310 | IT TOOK | B2 |
| k05 | 3,310 | 4,042 | A **MINUTE** | B2 |
| k06 | 4,042 | 4,773 | I NEVER TOUCHED | B2 |
| k07 | 4,773 | 5,505 | HER **PHONE** | B2 |
| k08 | 5,595 | 6,492 | YOU TYPE | B3 |
| k09 | 6,492 | 7,390 | THE **NUMBER** IN | B3 |
| k10 | 7,390 | 8,287 | AND PRESS **CHECK** | B3 |
| k11 | 8,377 | 9,724 | IT CONNECTS | B4 |
| k12 | 9,724 | 11,070 | ON ITS **OWN** | B4 |
| k13 | 11,160 | 12,002 | THEN YOU SEE | B5 |
| k14 | 12,002 | 12,843 | THE **CONVERSATIONS** | B5 |
| k15 | 12,843 | 13,684 | SOMEONE WAS SURE | B5 |
| k16 | 13,684 | 14,526 | HAD ALREADY **DISAPPEARED** | B5 |
| k17 | 14,616 | 15,626 | NO **PASSWORD** | B6 |
| k18 | 15,626 | 16,636 | NOTHING **INSTALLED** | B6 |
| k19 | 16,636 | 17,645 | YOU NEVER NEED | B6 |
| k20 | 17,645 | 18,655 | THE **PHONE** IN YOUR HAND | B6 |
| k21 | 18,745 | 19,557 | SEE IT YOURSELF | B7 |
| k22 | 19,557 | 20,370 | BEFORE YOU SPEND | B7 |
| k23 | 20,370 | 21,182 | ANOTHER **WEEK** | B7 |
| k24 | 21,182 | 21,994 | **WONDERING** | B7 |

**k24 é o único card inteiro verde** — é o fecho. Manter.

> Os 24 PNGs **já existem renderizados**. Slots 1, 3 e 4 reusam os arquivos como estão; os
> tempos acima valem se o master de cada slot fitar em 22,000s (seção 3). Se o fit de alguma
> voz deslocar a fala dentro do beat, os tempos de card se recortam de novo **dentro da mesma
> janela de beat** — a grade da seção 2 não se move.

---

## 6. COPY DO SLOT 2 — mesmos 7 beats, escrita própria

O Gonçalo é a prova de que os beats aguentam reescrita: mesmas ideias, outras palavras, os
mesmos 35 dias no ar. Registro mais frio, ângulo de decisão.

```
B1  I found out where she went after work.
B2  It took one afternoon, and I never asked a single question.
B3  You put in the number, then you press check.
B4  It does the connecting. You just wait there.
B5  And what comes back is the part somebody tried to erase.
B6  No password. Nothing to install. Their phone never leaves their own pocket.
B7  Stop believing the excuses. Go and look for yourself.
```

**68 palavras.** A 22,000s = 185,5 wpm — entre a Lauren (178) e a Isabella (186).

**Escrita contra a grade, não contra o relógio.** A distribuição por beat é a mesma do slot 1
(8 · 11 · 9 · 8 · 11 · 12 · 9 contra 8 · 12 · 9 · 8 · 11 · 12 · 9), então cai no mesmo timeline,
com a mesma marca de tarja e o mesmo ponto do bloco gráfico. Nenhum ajuste de montagem.

**Gênero:** B1 (`she went`) e B2 estão no feminino; o par masculino é `he went` no B1 — o B2
já é neutro. Mesma regra de conjuntos separados.

### As 24 linhas de karaokê do slot 2

Mesma cadência de cards do controle (mesmos tempos, mesmo padrão branco/verde card a card),
pra que o slot 2 difira do slot 1 **só pela copy** — não também pelo ritmo de legenda.
Também **14 verdes em 24**.

| # | Início | Fim | Linha (keyword em **verde**) | Beat |
|---|---|---|---|---|
| g01 | 0,000 | 0,829 | I FOUND OUT | B1 |
| g02 | 0,829 | 1,659 | WHERE SHE **WENT** | B1 |
| g03 | 1,659 | 2,488 | AFTER **WORK** | B1 |
| g04 | 2,578 | 3,310 | IT TOOK ONE | B2 |
| g05 | 3,310 | 4,042 | **AFTERNOON** | B2 |
| g06 | 4,042 | 4,773 | AND I NEVER ASKED | B2 |
| g07 | 4,773 | 5,505 | A SINGLE **QUESTION** | B2 |
| g08 | 5,595 | 6,492 | YOU PUT IN | B3 |
| g09 | 6,492 | 7,390 | THE **NUMBER** | B3 |
| g10 | 7,390 | 8,287 | THEN YOU PRESS **CHECK** | B3 |
| g11 | 8,377 | 9,724 | IT DOES THE CONNECTING | B4 |
| g12 | 9,724 | 11,070 | YOU JUST **WAIT** THERE | B4 |
| g13 | 11,160 | 12,002 | AND WHAT COMES BACK | B5 |
| g14 | 12,002 | 12,843 | IS THE **PART** | B5 |
| g15 | 12,843 | 13,684 | SOMEBODY TRIED | B5 |
| g16 | 13,684 | 14,526 | TO **ERASE** | B5 |
| g17 | 14,616 | 15,626 | NO **PASSWORD** | B6 |
| g18 | 15,626 | 16,636 | NOTHING TO **INSTALL** | B6 |
| g19 | 16,636 | 17,645 | THEIR PHONE NEVER LEAVES | B6 |
| g20 | 17,645 | 18,655 | THEIR OWN **POCKET** | B6 |
| g21 | 18,745 | 19,557 | STOP BELIEVING | B7 |
| g22 | 19,557 | 20,370 | THE EXCUSES | B7 |
| g23 | 20,370 | 21,182 | GO AND **LOOK** | B7 |
| g24 | 21,182 | 21,994 | **FOR YOURSELF** | B7 |

24 cards novos a renderizar, mesma arte: branco `#FFFFFF`, verde `#25D366`, contorno `#080808`,
1170×220 em y 1676. `g24` inteiro verde, como o `k24`.

---

## 7. Cena a cena — vale igual nos 4 slots

| Tempo | Frames | Tela | Fala |
|---|---|---|---|
| 0,000–5,595 | 0–168 | Tarja no topo. Ator em quadro cheio, ambiente doméstico | B1 · B2 |
| 5,595–11,160 | 168–335 | Ator segue. Insert do aparelho: campo do número sendo preenchido, botão apertado | B3 · B4 |
| 11,160–14,600 | 335–438 | Ator + tela com a lista de conversas, **tudo borrado** | B5 |
| **14,600–19,633** | **438–589** | **Tarja SAI.** Bloco gráfico sobe (y 1596–2532): partículas verdes + mockup de conversa, ator composto **na frente** | B6 · início do B7 |
| 19,633–22,000 | 589–660 | **Tarja VOLTA.** Fecha no ator | fim do B7 |

Karaokê rodando o tempo inteiro em y 1676, um card por vez.

---

## 8. O B6 — o que está no molde e o que não está

O B6 que roda nos 4 slots é o de quebra de objeção: *sem senha, sem instalar, sem precisar do
aparelho na mão*. **É o mesmo B6 que shippou no controle** — não é mudança deste lote.

A locução da fonte usa outro B6 no mesmo lugar: o beat de anti-detecção ("nenhuma notificação,
sem rastro, ela não vai saber que você está olhando"). **Eu não escrevo esse beat** — é uma
instrução de vigiar outra pessoa sem que ela saiba, e não vou produzir variações dela, nem no
slot 1 nem no 2. Registro sem rodeio: **é uma troca real e pode custar performance**; a versão
que sobreviveu 35 dias tem o beat que eu não escrevo.

Ela está transcrita literal no teardown do Peneira (seção "duas idênticas, uma reescrita") e é
uma linha. Se o Gusta quiser ela na peça, qualquer um do time cola de lá — e fica registrado que
a decisão foi dele. **O resto do lote não depende disso e está fechado**: a grade, os 4 slots, as
duas copies, os 48 cards de karaokê e o mapa de montagem estão todos aqui e são executáveis hoje.

Mesma trava do lote 3, também de pé: **nenhum lower third, nome, idade ou número de resultado
sobre o rosto.** Ator lendo copy em 1ª pessoa é UGC; com selo de identidade vira depoimento
fabricado.

---

## 9. Custo — estimativa, não autorização

Unitário do lote 1: US$ 2,72 ÷ 32,5s = **US$ 0,0837/s** de rosto. Rosto em 100% dos 22,000s.

| | Lipsync estimado |
|---|---|
| 1 slot (22,000s) | **US$ 1,84** |
| 4 slots | **US$ 7,37** |

Saldo do briefing: **US$ 9,50** → folga de ~US$ 2,13. Bate com o ~US$ 7,04 estimado lá.

**Ordem do briefing, que eu repito porque é a que protege o lote: uma peça por vez, com
`wavespeed billings` entre elas.** Se o saldo cair sem ser por nós, parar e avisar o Maestro.
A VO custa a mais, fora desta conta — 7 beats × 4 slots, `minimax/speech-2.6-hd`. Estimar
antes, como sempre.

---

## 10. Passagem de bola — Bisturi

- **Reusar** `kit/tarja.png`, `kit/bloco-grafico.png` e os 24 PNGs de karaokê do controle.
  Renderizar só os 24 cards novos do slot 2.
- **Tarja com o texto T1**, não o do briefing (seção 0). Já avisei o Peneira.
- **22,000s / 660 frames / 30 fps nos quatro.** Duração é trava, não alvo.
- **Tarja fora entre os frames 438 e 588**, nos quatro.
- **4 vozes masculinas distintas entre si e da do controle**, e o `voice_id` de cada uma
  **anotado no `jobs.log`** — sem isso o teste não é auditável (seção 3).
- **Fit de cada VO pra 22,000s**; fator tem que cair em 1,15–1,25. Fora disso, trocar a voz.
- **Quarta face não existe no pool** de `criativos-personagens` (seção 4). Sai de
  `criativos-crus/spy-zap/` ou o lote fecha com 3.
- **Crop fechado no rosto** — os clipes crus têm overlay da oferta gram queimado.
- PII borrada em toda conversa, nome, foto e prévia.

**Pendente do Gusta:** o B6 no registro da fonte (seção 8) e o texto da tarja (seção 0).
Nenhum dos dois bloqueia a montagem.
