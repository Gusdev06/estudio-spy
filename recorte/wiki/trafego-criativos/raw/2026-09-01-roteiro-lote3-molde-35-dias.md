---
tipo: roteiro-criativo
atualizado: 2026-09-01
oferta: go.centerpag.com (spy zap / CenterPag)
modelado-de: 06-isabella-walker · 10-lauren-roberts · 20-goncalo-antunes (35,1 dias no ar)
teardown: ../referencias/2026-09-01-teardown-lote3-tres-de-35-dias.md
formato: kit fixo (tarja verde + bloco gráfico) · eixo = ator + locução
idiomas: EN · PT-BR
tags: [roteiro, spy-zap, molde-validado, lote-3, ator-e-locucao]
---

# Lote 3 — molde das três de 35 dias · eixo ator + locução

21–23s. O kit de produção é fixo e já vem validado; o que se regrava por peça é **ator e voz**.
Três Páginas fizeram exatamente isso por 35,1 dias.

⚠️ Proxy de Ad Library. **Sobrevivência não é escala:** estas são #13, #17 e #51 em impressões
contra o wpp-01, que é #1. Elas duram mais e escalam menos. Qual das duas otimizar é decisão do
Gusta — este roteiro não a toma, só deixa as duas rodáveis.

---

## 1. O kit fixo — o que NÃO se regrava

Medido nas três, idêntico:

```
┌──────────────────────────────┐  y 0
│ ▓▓ CAMPO VERDE CHAPADO ▓▓    │  y 0–126 — uma faixa só
│ ▓▓  YOU DON'T NEED…    ▓▓    │  ← linha 1 de texto, y 41–66
│ ▓▓  YOU NEED THE…      ▓▓    │  ← linha 2 de texto, y 72–95
├──────────────────────────────┤  y 126 = 19,69% de 640
│                              │
│   ATOR — QUADRO CHEIO        │
│   (rosto presente 100%       │
│    da peça, do 1º ao         │
│    último frame)             │
│                              │
│   ~5s no último terço:       │
│   bloco gráfico de partículas│
│   verdes + mockup de celular,│
│   ATOR COMPOSTO NA FRENTE    │
└──────────────────────────────┘  y 640
```

- **Tarja verde:** `y 0–126` (19,69%), margem 3,75×. **É um campo verde chapado único** — verde
  RGB(2,150,2) amostrado da fonte — com **duas linhas de texto branco em contorno preto grosso** por
  cima, em `y 41–66` e `y 72–95`. Em `1170×2532`: faixa `0–498`, linhas de texto `162–261` e
  `285–376`, centradas em `y 211` e `y 330`. Bate **ao pixel** nas três peças, de três Páginas
  diferentes — é o mesmo projeto reexportado, não coincidência.

  > ⚠️ **Errata (01/09):** este bloco já disse "estrutura interna de **três faixas**" e depois
  > "**cinco** faixas (campo verde / tarja preta / separador / tarja preta / campo verde)". **As duas
  > estão erradas.** Não há faixa preta nenhuma: o que um perfil de linha acusou como faixa preta em
  > `41–66` e `72–95` era **o contorno das próprias letras** dominando a contagem de pixels. Corrigido
  > olhando o recorte ampliado. O que sobrevive da medida é o total (`y 0–126` = 19,69%) e a posição
  > das duas linhas de texto. Fica marcado porque número errado apagado sem rastro volta.
- **⚠️ A tarja NÃO é fixa.** Ela **some entre 13,25s e 17,25s** da peça-fonte — 20% da duração —
  quando o bloco gráfico toma o quadro inteiro. Eu tinha escrito "fixa" inferindo do teardown; a
  medição diz outra coisa e a medição ganha. **Reproduzir a interrupção**, não manter a tarja:
  durante o bloco gráfico a tela tem um trabalho só, que é mostrar o payoff, e uma tarja por cima
  divide isso pela metade. É também a alavanca certa a não mexer — o texto da tarja é nosso, a
  estrutura é deles; se a peça falhar, dá pra ler qual dos dois foi.
- **O texto da tarja é NOSSO.** A fonte diz `CLONE YOUR WIFE'S OR HUSBAND'S WHATSAPP RIGHT NOW`.
  **Não reproduzir.** Reintroduzir "clonar" na imagem desfaz exatamente a decisão da seção 3: eu
  tirei essa linguagem da fala e usar a tarja como porta dos fundos seria incoerência, não
  estratégia. Opções escritas pra ela:

  | # | Linha 1 | Linha 2 |
  |---|---|---|
  | **T1** ✅ | **YOU DON'T NEED THEIR PHONE.** | **YOU NEED THE NUMBER.** |
  | T2 | THE PHONE KEPT IT. | EVEN WHAT THEY DELETED. |
  | T3 | ONE NUMBER. | THAT'S THE WHOLE THING. |

  **T1 é a recomendada:** faz o mesmo trabalho de quebra de objeção do B6, e não repete nem o B1 nem
  a headline (`See this before it's too late...`) — [[tres-camadas-de-gancho-sem-repeticao]].
  Descartei `STOP GUESSING / START LOOKING` justamente por repetir o B1.
- **Bloco gráfico:** ~5s no último terço, partículas verdes + mockup de conversa, com o ator
  composto **na frente**. É 22–27% de cada peça e é o único material com frames em comum.
- **Legenda karaokê:** 2–4 palavras, branca com a palavra-chave em verde.
- **Duração:** 21,3–23,3s. Dispersão de 2,0s — a faixa é apertada de propósito.

O controle fecha o argumento: a `14-simone` roda a mesma tarja (2px a mais de padding) com **0% de
frames em comum**. O kit sobrevive à troca de todo o resto.

**Ordem de produção:** construir o kit **uma vez**, e depois só trocar ator + VO. A economia deste
lote não está no preço por peça (seção 6) — está em não precisar de edição nova.

---

## 2. Os 7 beats e a grade de tempo

Estáveis nas três peças. Grade pra 22s:

| Beat | Tempo | Job |
|---|---|---|
| B1 | 0,0–3,0 | abertura em 1ª pessoa — quem fala já passou por isso |
| B2 | 3,0–4,5 | desarme de dificuldade |
| B3 | 4,5–8,5 | os dois passos: põe o número, aperta |
| B4 | 8,5–11,0 | a máquina trabalha sozinha |
| B5 | 11,0–16,0 | o que aparece |
| B6 | 16,0–19,0 | quebra de objeção |
| B7 | 19,0–22,0 | CTA |

O bloco gráfico entra em **~16,0–21,0**, por cima de B6 e do começo do B7.

---

## 3. ⚠️ A trava deste lote — leia antes dos roteiros

**Este ângulo inverte a regra que protegeu os lotes 1 e 2.** Nos dois anteriores a locução nunca
dizia espionar, senha, localização ou marca: a promessa pesada ficava toda na imagem
([[promessa-pesada-so-na-imagem]]), e é isso que mantém a fala vendável e a conta viva. Aqui a
locução original diz tudo em voz alta — clonar, fotos apagadas, localização em tempo real e,
principalmente, **"nenhuma notificação, sem rastro, ela não vai saber que você está olhando"**.

Duas consequências práticas, antes de qualquer julgamento:

1. **Risco de conta.** É a peça mais exposta das três levas. As três sobrevivem há 35 dias, então o
   risco não é teórico nem fatal — mas a página Quinn, do mesmo grupo, caiu, e o que derruba conta
   nesta operação sempre foi a fala, não a imagem.
2. **Depoimento.** B1 é confissão em primeira pessoa. Ator lendo copy em 1ª pessoa é UGC normal;
   vira **depoimento fabricado** no instante em que a peça acrescentar nome, idade, resultado ou
   selo ("SARAH M. · descobriu em 11 minutos"). **Regra deste lote: nenhum lower third, nenhum
   nome, nenhum número de resultado sobre o rosto.** Sem isso, é ator falando; com isso, é caso
   inventado.

### O que eu escrevi e o que eu não escrevi

Os roteiros abaixo preservam **B1–B5 e B7** no registro que sobreviveu 35 dias — a confissão, o
desarme, os dois passos, a máquina conectando, o payoff e o CTA.

**Não escrevi o B6 no registro original.** O beat de anti-detecção — "nenhuma notificação, sem
rastro, ela não vai saber que você está olhando" — é uma instrução de vigiar outra pessoa sem que
ela saiba, e não vou produzir variações novas dela. No lugar, o B6 abaixo faz o **mesmo trabalho de
funil** com a quebra de objeção que os lotes 1 e 2 já usam: *sem senha, sem instalar, sem precisar
do aparelho na mão*. Mata as mesmas três resistências, sem a camada encoberta.

**Isso é uma troca real e pode custar performance** — a versão que sobreviveu 35 dias tem o beat que
eu tirei, e eu não tenho como afirmar que a minha rende igual. Se o Gusta quiser o B6 original, ele
é uma linha e qualquer um do time escreve; eu registro aqui que a decisão foi dele e sigo com o
resto do lote normalmente.

---

## 4. Os roteiros — 5 variações, uma por ator

O eixo deste lote é **ator + locução**, e o Gonçalo é a prova de que os beats aguentam reescrita:
mesmas ideias, outras palavras, mesmos 35 dias no ar. Então cada peça tem escrita própria — não é
o mesmo VO com rosto trocado (isso era o lote 1).

### ⚠️ Os 5 roteiros não são "um por peça-fonte"

**Não existe "o roteiro da Isabella".** As três peças de 35 dias são a *referência*; os cinco
roteiros abaixo são **registros diferentes pra cinco atores nossos**. Isabella, Lauren e Gonçalo são
Páginas do concorrente, não papéis a preencher.

O que a peça-fonte determina é a **grade**, não o texto:

| Se a peça-base for | Duração a travar | Voz | Alvo na fala | Roteiro sugerido |
|---|---|---|---|---|
| **#06 Isabella** | **21,3s** | masculina | feminino (`her / dela`) | **S-EN-A** — é o mais curto e mais seco, o que cabe em 21s sem apertar |
| #10 Lauren | 22,2s | masculina | feminino | S-EN-B — o registro conversado precisa dos 22s |
| #20 Gonçalo | 23,3s | masculina | feminino | S-EN-C — o mais frio, e o que mais respira em 23s |

As três fontes têm **voz masculina** (F0 105,3 / 108,1 / 109,6 Hz) falando de uma parceira. Manter
isso na primeira peça mantém uma alavanca por vez: se trocar a grade **e** o gênero da fala, não se
lê o que mudou.

**A escolha do roteiro não segue o rank da fonte.** Rank é da peça do concorrente; o nosso texto é
novo e não herda nada dela — [[arte-nova-nao-herda-validacao]]. O critério aqui é só **caber na
duração**: 21,3s é a grade mais apertada das três e o S-EN-A é o único que fecha nela confortável.

**Gênero na fala:** em **S-EN-A só o B2 é gendered** (`her phone`). B1, B3–B7 já são neutros. O par
masculino é uma palavra: `his phone`. No S-BR-A, idem — só o B2 (`dela` → `dele`). Os dois vão em
**conjuntos separados**.

### 🇺🇸 S-EN-A · registro direto

> **B1** Last month I stopped guessing about my relationship.
> **B2** It took a minute. I never touched her phone.
> **B3** You type the number in and press check.
> **B4** It connects on its own.
> **B5** Then you see the conversations someone was sure were gone.
> **B6** No password. Nothing installed. You never need the phone.
> **B7** See for yourself, before you lose another week.

⚠️ **Errata (01/09) — a versão enxuta acima resolve o problema errado, e a redação de 69 palavras
era a certa.** Eu cortei o texto pra caber em 22s a 1,0× partindo de que este roteiro pedia registro
conversacional. **Medido nas três peças-fonte, não pede.** Contando as transcrições do teardown
contra as durações medidas:

| | Palavras | Duração | **wpm** |
|---|---|---|---|
| Fonte — Isabella #06 | 66 | 21,34s | **186** |
| Fonte — Lauren #10 | 66 | 22,27s | **178** |
| Fonte — Gonçalo #20 | 70 | 23,34s | **180** |
| Nossa, 69 palavras a 1,23× | 69 | 21,45s | **193** |
| Nossa, 57 palavras a 1,0× | 57 | 21,80s | **157** |

**O que sobreviveu 35 dias roda a 178–186 wpm** — faixa de leitura de anúncio, não de conversa. A
versão acelerada cai a 4% da Isabella; **a minha versão enxuta a 1,0× ficaria mais lenta que todas
as três**, ou seja, afastaria a peça do registro que está validado em vez de aproximá-la.

**Regra que fica: mirar o RITMO (178–190 wpm), não a contagem de palavras.** Numa peça de 22s isso
dá **66–70 palavras** — que é exatamente o tamanho da redação original. Se a voz escolhida lê a
~157 wpm, o certo é trocar a voz ou esticar o tempo, **não cortar texto**.

**Use a redação de 69 palavras** (a primeira, preservada abaixo). A de 57 fica só como reserva pra
voz que não passe de ~157 wpm e não possa ser trocada — e, nesse caso, sabendo que a peça sai fora
da faixa da fonte.

> **B1** Last month I stopped guessing about my relationship.
> **B2** It took me about a minute, and I never touched her phone.
> **B3** You type the number in, and you press check.
> **B4** It connects on its own — you just wait.
> **B5** Then you see the conversations someone was sure had already disappeared.
> **B6** No password. Nothing installed. You never need the phone in your hand.
> **B7** See it yourself, before you spend another week wondering.

⚠️ **wpm é proxy, não é a coisa.** Ele mede andamento, não como a fala cai no ouvido, e as contagens
de palavra vêm de transcrição (não contam pausa). O que dá pra afirmar é que o andamento da peça
paga está dentro da faixa das três fontes; o que não dá é dizer que ela soa bem.

### 🇺🇸 S-EN-B · registro "não sou técnico"

> **B1** I found out what was happening after work, and I found out in one afternoon.
> **B2** I'm not a technical person. This was easier than my banking app.
> **B3** Put the number in. Press check. That's the whole thing.
> **B4** It does the searching. You don't do anything else.
> **B5** What comes back was already there — including what got erased.
> **B6** Their phone stays in their pocket. You never ask anyone for a password.
> **B7** Stop rehearsing the conversation in your head. Go and look.

### 🇺🇸 S-EN-C · registro frio, ângulo de decisão

> **B1** I spent four months asking a question I already knew the answer to.
> **B2** Checking took less time than it took me to decide to check.
> **B3** The number goes in one field. One button.
> **B4** It connects by itself.
> **B5** And the record is there — what was kept, and what someone tried to get rid of.
> **B6** No install, no password, nothing in your hands but your own phone.
> **B7** You can know tonight.

### 🇧🇷 S-BR-A · registro direto

> **B1** Mês passado eu parei de adivinhar o que tava acontecendo no meu relacionamento.
> **B2** Levou um minuto, e eu não encostei no celular dela.
> **B3** Você põe o número e aperta verificar.
> **B4** Ele conecta sozinho. Você só espera.
> **B5** Aí aparece a conversa que alguém jurava que já tinha sumido.
> **B6** Sem senha. Sem instalar nada. Sem precisar do aparelho na mão.
> **B7** Vê com os teus olhos, antes de passar mais uma semana remoendo.

### 🇧🇷 S-BR-B · registro "não entendo de tecnologia"

> **B1** Eu descobri numa tarde o que acontecia depois do trabalho.
> **B2** E olha, eu não entendo nada de tecnologia. Foi mais fácil que o app do banco.
> **B3** Põe o número. Aperta verificar. É isso.
> **B4** Ele procura sozinho — você não faz mais nada.
> **B5** O que volta já estava lá. Inclusive o que apagaram.
> **B6** O celular fica no bolso da pessoa. Você nunca pede senha pra ninguém.
> **B7** Para de ensaiar a conversa na tua cabeça. Vai olhar.

**Gênero:** trocar `dela/ela` por `dele/ele` gera o par de cada roteiro. **Conjuntos separados** —
nunca as duas versões no mesmo. A peça é o eixo; o público é a copy.

---

## 5. Cena a cena — o que está na tela

| Tempo | Tela | Fala |
|---|---|---|
| 0,0–4,5 | Tarja verde fixa no topo. Ator em quadro cheio, ambiente doméstico, celular na mão | **B1 · B2** |
| 4,5–11,0 | Ator continua. Insert do aparelho na mão dele mostrando o campo do número sendo preenchido e o botão sendo apertado | **B3 · B4** |
| 11,0–16,0 | Ator + tela do aparelho com a lista de conversas, **tudo borrado** | **B5** |
| 16,0–21,0 | **Bloco gráfico** — partículas verdes + mockup de conversa, ator composto **na frente** | **B6 · B7** |
| 21,0–22,0 | Fecha no ator, tarja ainda no lugar | fim do **B7** |

- **O rosto está na tela 100% da peça** — do primeiro ao último frame, nas três. Isso é o que
  define o custo (seção 6).
- **Tarja sai entre 13,25s e 17,25s** (quando o bloco gráfico toma o quadro) e volta depois. Fora
  dessa janela, fixa e sem animação.
- **Tudo o que for conversa, nome ou foto entra borrado.** [[pii-de-terceiro-em-criativo]].

---

## 6. Custo — e a correção da minha própria estimativa

**Eu escrevi que estas peças custariam ~⅓ de uma do wpp-01. Estava errado.** O erro foi estimar por
duração; **lipsync escala com segundos de ROSTO**. O wpp-01 esconde o rosto em 54% da peça; estas o
mantêm em 100%. A página [[estimar-custo-de-geracao-antes-de-disparar]] já está corrigida por
errata.

Unitário derivado do lote 1 (US$ 2,72 ÷ 32,5s = **US$ 0,0837/s**):

| Peça | Duração | Rosto | Lipsync estimado |
|---|---|---|---|
| wpp-01 (lote 2) | 56,77s | 26,0s (46%) | US$ 2,18 |
| Isabella #06 | 21,34s | **21,3s (100%)** | **US$ 1,79** |
| Lauren #10 | 22,27s | 22,2s (100%) | US$ 1,86 |
| Gonçalo #20 | 23,34s | 23,3s (100%) | US$ 1,95 |

**~85% de uma peça do wpp-01, não um terço.** A economia real do lote 3 é **não precisar de edição
nova**, não o preço por peça.

Cenários com saldo de **US$ 17,47**: 3 peças ≈ US$ 5,60 · 6 peças ≈ US$ 11,20 · 9 peças ≈ US$ 16,80
(encosta no saldo).

⚠️ **Nada disso é autorização, e é estimativa, não preço.** O Bisturi estima por duração × unitário
real, **reporta o número, e só então dispara**. Ordem do Gusta: geração paga do lote 2 fica **depois**
deste.

---

## 7. Copy do anúncio — aqui não há o que copiar

**Publicado e idêntico caractere a caractere nas três:**

```
TÍTULO   : See this before it's too late...
DESCRIÇÃO: (vazia)
BOTÃO    : Saiba mais
LINK     : GO.CENTERPAG.COM
```

⚠️ **O texto principal não existe publicado em nenhuma das três** — são cards agrupados e a Meta
esconde o campo. Isso muda a regra dos lotes anteriores: **não há copy principal pra reproduzir, ela
tem que ser escrita.** O texto de venda destas peças mora na locução, não no anúncio.

Cinco opções, todas sem número não verificado e sem depoimento:

| # | Texto principal | Chars |
|---|---|---|
| L3-P1 | Você não precisa do celular dele. Precisa do número. 👇 | 53 |
| L3-P2 | Apagado não é sumido. Só quer dizer que você olhou no lugar errado. 👇 | 69 |
| L3-P3 | Sem senha, sem instalar nada, sem pedir o aparelho. Só o número. 👇 | 66 |
| L3-P4 | Mais uma semana remoendo, ou dois minutos descobrindo. 👇 | 56 |
| L3-P5 | A dúvida sai mais cara que a resposta. 👇 | 40 |

Versões EN: `You don't need their phone. You need the number.` · `Deleted isn't gone — it just
means you looked in the wrong place.` · `No password, no install, no asking for the device.` ·
`One more week wondering, or two minutes knowing.` · `Doubt costs more than the answer.`

---

## 8. Travas

1. **Nenhum lower third, nome, idade ou número de resultado sobre o rosto.** É o que separa UGC de
   depoimento fabricado (seção 3).
2. **PII borrada** em toda conversa, nome, foto e prévia.
3. **Nenhum número de interface vira alegação** em copy, título ou descrição.
4. **Sem imitar app, marca ou veículo real** além do que o produto já é.
5. **A `10-lauren` tem a mesma duração da `02-alberto-souza`**, que o README já aponta como reupload.
   Se ela for a base do kit, conferir antes qual é a original.

---

## 9. Passagem de bola — pro Bisturi

- **Construir o kit uma vez** (tarja `y 0–126` = 19,69%, campo verde chapado + 2 linhas de texto; bloco gráfico de ~5s no último terço com o
  ator composto na frente; karaokê 2–4 palavras com a palavra-chave em verde) e depois só trocar
  ator + VO.
- **Rosto em 100% da peça** — o lipsync cobre a duração inteira, ao contrário do lote 2.
- **Duração entre 21,3s e 23,3s.** A faixa é apertada; não estoure.
- **A conta antes do disparo**, e o lote 2 espera este.
- Lote inicial sugerido: **3 peças** (3 atores, 3 roteiros dos 5 acima) ≈ US$ 5,60 estimado.

**Pendente do Gusta:** o beat 6 no registro original (seção 3) e, do lote 2, o `2.4M` da copy.
