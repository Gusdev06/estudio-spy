---
tipo: roteiro-criativo
atualizado: 2026-09-11
oferta: go.zappdetect.com (spy gram / Gram Detect)
modelado-de: gram-01 Sophia Jones · ad_id 1761247818659822 (#1 do swipe de Instagram)
teardown: ../referencias/2026-09-01-teardown-vencedor-gram-sophia-jones.md
peca-original: ../escalados/instagram/01-sophia-jones-1761247818659822.mp4
ad-library: https://www.facebook.com/ads/library/?id=1761247818659822
formato: L9 — split de 3 blocos, funil como painel lateral
idiomas: EN · PT-BR · ES
tags: [roteiro, spy-gram, split-screen, funil-gravado, faixa-de-hook, roteiro-mestre]
---

# Roteiro mestre GRAM · L9 — split de 3 blocos

1 locução mestre de 29s. N rostos. N faixas de hook. O funil que já está gravado vira
painel lateral em vez de ser o anúncio inteiro.

**O que este arquivo entrega:** o roteiro cena a cena (o que aparece na tela e o que a
pessoa fala, marcado no tempo), a locução mestre nos 3 idiomas, **26 faixas de hook** e
**10 ganchos falados** alternativos — que são os dois eixos a multiplicar.

**O que ele NÃO mexe:** a copy da Meta. Ordem do Gusta é reproduzir a do vencedor como
está. Ela está no fim do arquivo, no bloco marcado.

⚠️ Nenhuma métrica de performance do vencedor foi verificada. O ranking dele é proxy de
Ad Library (sem flag de baixo volume + ordem de `total_impressions desc` + 3,2 dias no ar
+ 6 peças no mesmo ângulo). Não é ROAS, não é CTR, não é gasto. Ler como **sinal de
sobrevivência**, não como campeão medido.

---

## 1. Decisão de idioma — fazer de propósito, não herdar

O vencedor roda copy da Meta em **inglês**, botão em **português** e conteúdo do funil em
**PT-BR**, servindo público BR. O teardown registra isso como divergência a decidir. Decidido:

| Lote | Copy da Meta | Locução | Faixa de hook | Funil (arquivo) | Status |
|---|---|---|---|---|---|
| **A — controle EN** | EN, do vencedor, palavra por palavra | EN | EN | `GRAM MASC ING.mp4` | ✅ obedece a ordem, peça 100% coerente |
| **B — mistura do vencedor** | EN, do vencedor, palavra por palavra | PT-BR | PT-BR | `GRAM FEM/MASC PORT.mp4` | ✅ obedece a ordem; replica de propósito a mistura que está no topo |
| **C — PT-BR inteiro** | traduzida | PT-BR | PT-BR | `GRAM ... PORT.mp4` | ⛔ **precisa de OK do Gusta** — mexe na copy |
| **D — ES** | traduzida | ES | ES | `GRAM FEM/MASC ESP.mp4` | ⛔ mesma trava do C; leads chegam em ES, vale pedir |

**A × B é o teste que importa** e é uma alavanca só ("idioma da peça"). Rodar em conjuntos
separados, nunca a mesma variação dentro do mesmo conjunto. C e D ficam engatilhados neste
arquivo pra subirem no minuto em que o Gusta liberar tocar na copy.

---

## 2. O layout (L9) — onde cada coisa mora

Nosso lote é `1170×2532`. Percentuais do teardown convertidos:

```
┌────────────────────────────────────────┐  y 0
│                                        │
│           TALKING HEAD UGC             │  47,87%  → y 0–1212
│                                        │
├────────────────────────────────────────┤  y 1212
│  FAIXA DE HOOK — fixa, 2 linhas        │  11,30%  → y 1212–1498 (h 286)
├───────────────┬────────────────────────┤  y 1498
│     FUNIL     │     B-ROLL DE DOR      │
│  (recording)  │   (plano único, sem    │  40,84%  → y 1498–2532 (h 1034)
│     39,49%    │     corte nenhum)      │
│    x 0–461    │  60,51% · x 462–1170   │
└───────────────┴────────────────────────┘  y 2532
```

Detalhe de montagem em [[funil-gravado-como-painel-lateral]] e [[spec-de-edicao-layouts-spy]].
Faixa desenhada **por último**, senão o painel a apaga.

⚠️ **A divisão vertical é 39,4% / 60,6% — corrigida em 01/09.** A primeira medida (35,8%) foi lida
por cor num frame único e caiu numa borda escura que é **interna** ao card do funil. Montar pelo
número antigo cortaria 13 px de funil pra fora do quadro. A fronteira certa veio de variância
temporal sobre 59 frames — o desvio desaba 7× numa coluna só (`x=142` em 360 de largura), e o
movimento atravessa a borda escura, o que prova que ela não é o fim do painel. Em **referência de
terceiro** a fronteira se mede por movimento; cor chapada só vale pra peça nossa, cuja faixa a gente
mesmo desenhou — os dois métodos e onde cada um mente estão em [[medir-fronteira-de-bloco-em-video]].
As faixas horizontais não mudaram — reconferidas pelos dois métodos e batem.

**Os pixels acima são os do corte que vai ser montado**, conformados pelo Bisturi pra números
pares (H.264 pede dimensão par): `head 1212 · faixa 286 · painel 1034 · divisão 462`. Os percentuais
do teardown (47,7 / 11,6 / 40,6 e 39,4 / 60,6, medidos em 360 de largura) batem com eles dentro do
arredondamento. **Onde houver dúvida, vale o pixel, não o percentual.**

**Sem legenda karaokê.** A peça inteira tem uma faixa de texto e ela nunca muda — é o oposto
do `wpp-01`. Está registrado como contradição em aberto no wiki
([[faixa-de-hook-fixa-sem-legenda]]); este lote roda o lado "faixa fixa".

---

## 3. Roteiro cena a cena — 32,5s

Coluna "funil" = qual módulo do [[template-funil-gravado-9-modulos]] está no painel esquerdo.
Coluna "fala" = locução mestre (o texto está em 3 idiomas na seção 4).

| Tempo | Painel esquerdo — FUNIL | Painel direito — B-ROLL | Rosto | Fala (beat) |
|---|---|---|---|---|
| **0,0–1,8** | Wizard **passo 1** · `O que você quer descobrir?` · 4 checkboxes já marcados · `STEP 1 OF 3` | plano único começa e **não corta mais** | fala pra câmera, plano médio | **B1** — gancho de curiosidade |
| **1,8–4,4** | Wizard **passo 2** · `Quem você vai monitorar?` · `Um homem` / `Uma mulher` · `STEP 2 OF 3` | idem, rodando | idem | **B1** fim + **B2** início |
| **4,4–7,5** | Wizard **passo 3** · `Ativar modo invisível?` · `⚡ Sim, 100% invisível` / `🚫 Não precisa` · `STEP 3 OF 3` | idem | idem | **B2** — "quase ninguém sabe onde olhar" |
| **7,5–14,7** | **Input do @** · o arroba sendo digitado letra a letra, teclado nativo · badge `⚡ 1 análise grátis por dispositivo` · contador `● 291 online` | idem | idem | **B3** — as 3 objeções mortas |
| **14,7–15,9** | `Conectando ao Instagram… localizando o perfil` + loader | idem | idem | **B4** início |
| **15,9–22,7** | **Card de confirmação de perfil** · foto **borrada**, @ **borrado**, contagens visíveis · `⚠️ Confira com atenção — esta é sua única análise grátis` · `✓ SIM, CONFIRMAR` | idem | idem | **B4** — o mecanismo (a pessoa escorrega) |
| **22,7–24,6** | `⚡ ACESSO EM ANDAMENTO` · barra de progresso · contador `● 348 analisando agora` | idem | idem | **B5** início |
| **24,6–27,2** | **Payoff 1** — feed do perfil abrindo, **legendas borradas** · contador `● 389 analisando agora` | idem | idem | **B5** — payoff social |
| **27,2–31,3** | **Payoff 2** — caixa de mensagens, **todos os nomes e prévias borrados**, só o formato lê · contador `● 412 analisando agora` | idem, até aqui sem uma emenda | idem | **B5** fim + **B6** |
| **31,3–32,5** | — **a tela colapsa** — split some, faixa some | — | **rosto em quadro cheio, sozinho** | **B7** — CTA falado |

### Os três cortes que carregam a peça

1. **0,0** — as três camadas de gancho entram juntas e nenhuma repete a outra: a faixa
   queimada (lê no mudo), a fala (curiosity gap) e o wizard já preenchido (a mecânica antes
   da promessa). Ver [[tres-camadas-de-gancho-sem-repeticao]].
2. **7,5** — o @ sendo digitado. É o módulo mais longo (7,2s) de propósito: é onde a
   espectadora se vê fazendo. Os módulos 1–4 comem 45% do vídeo — a peça está no começo.
3. **31,3** — **o corte que importa.** Tira tudo da tela e devolve o rosto por 1,2s, exatamente
   em cima do CTA falado. É o único momento em que ela não tem pra onde olhar além da pessoa.
   Não substituir por card final, seta ou logo — o CTA visual fica por conta do chrome do anúncio.

### O painel direito nunca corta

O b-roll roda ininterrupto os 31,3s enquanto o funil troca 9 vezes ao lado. Um lado é o
relógio, o outro é o metrônomo ([[dor-e-mecanismo-em-paralelo]]). Se o b-roll cortar, os dois
lados viram ruído.

### Contador: **sobe**

`291 → 348 → 389 → 412`. O vencedor deixa o dele cair (393 → 377 → 304) e isso lê como fila
esvaziando. Regra da casa é subir ([[contador-que-sobe-como-prova-de-trabalho]]). Número
quebrado, nunca redondo ([[numero-especifico-quebrado]]).

---

## 4. Locução mestre — 29s de fala em 32,5s de vídeo

**Estrutura:** curiosidade → 3 objeções mortas de uma vez → mecanismo → payoff social →
recolocação → CTA de direção + escassez.

**Regra que não se quebra:** a locução **nunca** diz espionar, hackear, invadir, mensagem
privada, senha, localização, o nome do produto, o preço ou a marca. A promessa pesada fica
toda na imagem ([[promessa-pesada-so-na-imagem]]). O que a fala promete é *um detalhe que
entrega quase todo mundo* e que *quase ninguém sabe onde procurar*.

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

### 🇧🇷 PT-BR — master

> **B1** Tem um detalhe no Instagram que entrega quase todo mundo.
> **B2** O problema é que quase ninguém sabe onde olhar.
> **B3** Você não precisa adivinhar, não precisa brigar, e não precisa pegar o celular de ninguém.
> **B4** Porque quem esconde alguma coisa acaba deixando rastro pra trás sem perceber.
> **B5** É por isso que tanta gente acaba encontrando conversa, contato e comportamento que a outra pessoa jurava que já tinha sumido.
> **B6** Você só precisa saber onde olhar.
> **B7** Está aqui embaixo, enquanto ainda está aberto.

### 🇪🇸 ES — master

> **B1** Hay un detalle en Instagram que delata a casi todo el mundo.
> **B2** El problema es que casi nadie sabe dónde mirar.
> **B3** No tienes que adivinar, ni discutir, ni tocar el teléfono de nadie.
> **B4** Porque cuando alguien esconde algo, siempre deja rastros pequeños sin darse cuenta.
> **B5** Por eso tanta gente termina encontrando conversaciones, contactos y comportamientos que la otra persona juraba que ya había borrado.
> **B6** Solo tienes que saber dónde mirar.
> **B7** Está justo aquí abajo, mientras siga abierto.

**Notas de locução**
- Tom de *amiga que descobriu*, não de especialista. Sem urgência de vendedor, sem grito.
- **Gravar o B1 em arquivo separado** dos beats B2–B7. É o que torna o gancho falado um módulo
  trocável (seção 6) sem regravar os outros 25s.
- B4 pede meio segundo de silêncio depois de "sem perceber" / "without noticing". É o beat de
  reframe.
- B7 sem exclamação. Direção + escassez em 3,2s, voz baixando no fim.
- Neutro de gênero de propósito: "o celular de ninguém", não "dele/dela". A mesma peça serve os
  dois públicos; quem separa é a copy no conjunto.

---

## 5. Eixo 1 — as faixas de hook (a variável a multiplicar)

**A faixa é a única variável entre as 4 peças do vencedor.** VO igual, funil igual, copy igual,
duração igual ao milissegundo — só o hook queimado muda ([[roteiro-mestre-com-n-vozes]]). E é
exatamente o eixo que está parado nas nossas 12 peças, que abrem idênticas.

**Spec:** caixa alta, 2 linhas, ~6 palavras, branco com contorno grosso sobre barra chapada,
emoji no início. Fica o vídeo inteiro, nunca anima, nunca sai. Cor da faixa pra spy-gram é
magenta/rosa ([[spec-de-edicao-layouts-spy]]).

**Regra:** a faixa **não pode repetir** nem a fala (B1) nem a copy da Meta. São três entradas
diferentes pro mesmo espectador — quem lê no mudo, quem ouve, e quem só vê a UI.

### 🇺🇸 EN — 10 faixas

| # | Linha 1 | Linha 2 |
|---|---|---|
| EN-01 | 👀 THE PROFILE IS PUBLIC. | THE PATTERN ISN'T. |
| EN-02 | 🔍 EVERYONE LEAVES A TRAIL. | EVEN THEM. |
| EN-03 | ⚠️ YOU ALREADY KNOW. | YOU JUST CAN'T PROVE IT. |
| EN-04 | 📱 STOP CHECKING THEIR PHONE. | CHECK THIS INSTEAD. |
| EN-05 | 🕐 THREE MINUTES. | ONE @USERNAME. |
| EN-06 | 💬 DELETED ISN'T GONE. | IT'S JUST OUT OF SIGHT. |
| EN-07 | 👁️ WHAT THEY LIKE AT 2AM | SAYS MORE THAN WORDS. |
| EN-08 | 🚩 YOUR GUT ISN'T LYING. | CHECK IT ANYWAY. |
| EN-09 | 🔓 NO LOGIN. NO PASSWORD. | JUST THE @. |
| EN-10 | 😶 THEY HID IT | FOR A REASON. |

### 🇧🇷 PT-BR — 10 faixas

| # | Linha 1 | Linha 2 |
|---|---|---|
| BR-01 | 👀 O PERFIL É PÚBLICO. | O PADRÃO NÃO É. |
| BR-02 | 🔍 TODO MUNDO DEIXA RASTRO. | INCLUSIVE ELE. |
| BR-03 | ⚠️ VOCÊ JÁ SABE. | SÓ NÃO CONSEGUE PROVAR. |
| BR-04 | 📱 PARA DE OLHAR O CELULAR. | OLHA AQUI. |
| BR-05 | 🕐 TRÊS MINUTOS. | UM @ DE INSTAGRAM. |
| BR-06 | 💬 APAGADO NÃO É SUMIDO. | SÓ SAIU DA SUA VISTA. |
| BR-07 | 👁️ O QUE ELE CURTE ÀS 2 DA MANHÃ | FALA MAIS QUE ELE. |
| BR-08 | 🚩 SEU INSTINTO NÃO MENTE. | CONFIRA MESMO ASSIM. |
| BR-09 | 🔓 SEM LOGIN. SEM SENHA. | SÓ O @. |
| BR-10 | 😶 ELE ESCONDEU | POR ALGUM MOTIVO. |

**Versão pra público masculino** (checando uma mulher) — trocar só o pronome, mesmo layout:
BR-02 `INCLUSIVE ELA.` · BR-07 `O QUE ELA CURTE ÀS 2 DA MANHÃ / FALA MAIS QUE ELA.` ·
BR-10 `ELA ESCONDEU / POR ALGUM MOTIVO.` Conjuntos separados, nunca no mesmo.

### 🇪🇸 ES — 6 faixas

| # | Linha 1 | Linha 2 |
|---|---|---|
| ES-01 | 👀 EL PERFIL ES PÚBLICO. | EL PATRÓN NO. |
| ES-02 | 🔍 TODOS DEJAN RASTRO. | ÉL TAMBIÉN. |
| ES-03 | ⚠️ YA LO SABES. | SOLO NO PUEDES PROBARLO. |
| ES-04 | 📱 DEJA SU TELÉFONO. | MIRA AQUÍ. |
| ES-05 | 💬 BORRADO NO ES DESAPARECIDO. | SOLO NO LO VES. |
| ES-06 | 🔓 SIN LOGIN. SIN CONTRASEÑA. | SOLO EL @. |

---

## 6. Eixo 2 — os ganchos falados (troca só o B1, 3,8s)

Segundo eixo, mais caro que a faixa (pede VO novo) mas ainda barato se o **B1 for gravado em
arquivo separado**: troca 3,8s de áudio, os outros 25s ficam.

⚠️ **Girar um eixo por vez** ([[variar-uma-alavanca-por-vez]]). Faixa primeiro — é a mais barata
e a de maior teto. O gancho falado entra no segundo lote, com a faixa vencedora travada.

### 🇺🇸 EN

| # | B1 (0,0–3,8) |
|---|---|
| EN-G0 | *(controle)* There's one thing on Instagram that quietly gives people away. |
| EN-G1 | Nobody hides everything. There's always one thing they forget. |
| EN-G2 | You can tell more from what someone likes than from what they post. |
| EN-G3 | Everything they do on that profile leaves a mark somewhere. |
| EN-G4 | The person being lied to is always the last one looking in the right place. |

### 🇧🇷 PT-BR

| # | B1 (0,0–3,8) |
|---|---|
| BR-G0 | *(controle)* Tem um detalhe no Instagram que entrega quase todo mundo. |
| BR-G1 | Ninguém esconde tudo. Sempre esquece uma coisa. |
| BR-G2 | Dá pra saber mais pelo que a pessoa curte do que pelo que ela posta. |
| BR-G3 | Tudo o que a pessoa faz naquele perfil deixa marca em algum lugar. |
| BR-G4 | O parceiro é sempre o último a saber. E não é por falta de sinal. |

*(BR-G4 é a linha de maior tração do acervo — é o sticker do `wpp-01` virado gancho falado.
Vale testar contra o controle logo no primeiro lote de gancho.)*

---

## 7. Direção de arte

### Talking head (47,7% de cima)

- **Arquétipo: "amiga que descobriu", não especialista.** Sem jaleco, sem credencial, sem prop de
  autoridade. A credibilidade vem do enquadramento, não do título ([[autoridade-por-enquadramento]]).
- Pessoa de 22–32 anos, ambiente doméstico com textura — bancada de vaidade, cozinha, quarto com
  prateleira. Luz frontal limpa, nada de estúdio.
- **Plano médio, nunca fechado na boca.** A locução é dublada por cima, sem lip sync — enquadramento
  fechado convida leitura labial e derruba a peça ([[roteiro-mestre-com-n-vozes]]).
- Movimento constante: gesticula, olha pra câmera, muda de apoio. Rosto parado 32s lê como stock.
- **Duração exata de 32,5s**, cortado ao frame. Duração é eixo próprio; se mudar junto com o rosto,
  cega a leitura do teste.
- ~~3 rostos no primeiro lote (1 mulher, 1 homem, 1 mulher +35). O rosto **não precisa ser quem fala**
  — a #10 do vencedor tem voz feminina sobre rosto masculino e está no topo do ranking.~~
  **Corrigido em 2026-09-11:** a #10 é **mulher** (cachos, moletom cinza), conferida nos frames 0 / 15 s / 25 s
  pelo Peneira (`../referencias/HANDOFF-peneira-para-isca.md`); o "homem de óculos" era a **#13** (VolutPay,
  outra página, outro roteiro). Nas 4 peças do vencedor, rosto e voz **casam de gênero**: #1 e #10 mulher /
  voz feminina (258 Hz); #3 e #6 homem / voz masculina. A premissa "rosto não precisa ser quem fala" ficou
  sem prova. **Regra vigente (decisão do Gusta, 10/09): avatar segue o gênero da voz**
  ([[avatar-segue-o-genero-da-voz]] em `wiki/trafego-criativos/wiki/tecnicas/`). Consequência pro casting:
  com **uma VO só**, os rostos do lote são todos do gênero dela (VO feminina → só mulheres, variando idade
  e etnia); se o lote quiser homem e mulher, são **duas VOs**, uma por gênero, como a página do vencedor faz.

### B-roll de dor (60,51% do painel, direita — 708 px de largura)

- **Plano único, 31,3s, sem um corte.** Se não houver 31s contínuos, dar loop lento no mesmo plano —
  nunca emendar dois planos diferentes.
- Cena de dor doméstica, não de tragédia: alguém no celular virado de costas na cama, tela iluminando
  o rosto no escuro, celular virado pra baixo na mesa quando o outro entra.
- Sem rosto reconhecível, sem tela legível. É textura emocional, não informação.
- Fica **constante no lote 1**. Vira eixo de variação só depois que faixa e gancho estiverem lidos.

### Faixa (11,6%)

Barra chapada magenta/rosa, texto branco caixa alta com contorno preto grosso, 2 linhas centradas.
Desenhada por último na pilha.

---

## 8. Travas — checar antes de subir

1. **PII de terceiro.** O vencedor mostra @ real, foto de perfil, feed com legenda e caixa de
   mensagens com **nomes civis completos**. A nossa família tem a mesma trava aberta
   ([[pii-de-terceiro-em-criativo]]). **Regravar o funil com conta de teste** é o certo; enquanto
   isso não acontece, **borrar**: @, foto de perfil, todos os nomes, todas as prévias de mensagem,
   todas as legendas do feed. O formato da tela é o que vende — o conteúdo dela não precisa ser legível.
2. **Nada de veículo de imprensa real** na faixa nem no b-roll ([[nao-imitar-veiculo-real]]).
   Precedente: a página Quinn, do mesmo grupo, foi banida.
3. **Nenhum número inventado.** Os contadores são teatro de interface e ficam sinalizados como tal
   internamente — não viram alegação de performance em lugar nenhum. Zero depoimento, zero case,
   zero "X mil clientes".
4. **A fala não promete o que a imagem promete.** Se alguma variação de gancho começar a dizer
   "ver mensagem", "senha", "localização" — cortar. Esse é o eixo que derruba conta.
5. **O ângulo inteiro roda perto da linha da Meta.** Sobreviver 3,2 dias no ar não é o mesmo que
   estar seguro.

---

## 9. Nota de produção — conformar o funil

Os recordings existem e são o ativo caro. Já estão em 6 idiomas × 2 gêneros, em `1170×2532`:

```
projects/mentoria-spy/downloads/EDIÇÃO/GRAM {FEM,MASC} {PORT,ING,ESP,FRAN,ITA,ALEM}.mp4
```

⚠️ **Eles não têm a mesma duração** — amostrados: `FEM PORT` 71,7s · `FEM ESP` 52,8s ·
`MASC ING` 46,2s. O painel precisa de **31,3s**. Então cada arquivo pede seus próprios pontos de
entrada e saída pra bater nos 9 marcos da tabela da seção 3 — não existe um corte único que sirva
pros 12. Onde faltar tempo, o módulo do @ sendo digitado (7,5–14,7) é o que aguenta esticar; onde
sobrar, o wizard é o que aguenta acelerar.

Recorte: coluna central do celular (`scale` + `crop`), com o `y` ajustado por módulo pra manter o
bloco que importa no quadro. A 39,49% da largura (462 px) só sobrevive tela de título grande, botão chapado e
até 4 linhas — módulo denso vira textura, e pro job dele isso basta.

---

## 10. Matriz do lote

Uma gravação de VO gera o lote inteiro:

| Lote | O que gira | O que trava | Peças |
|---|---|---|---|
| **1 — faixa** | 6 faixas de hook | 1 rosto, 1 b-roll, 1 VO | **6** |
| **2 — gancho falado** | 4 ganchos alternativos | a faixa vencedora do lote 1 | **4** |
| **3 — rosto** | 3 rostos | faixa + gancho vencedores | **3** |

Teto sem gravar áudio novo: 10 faixas × 3 rostos = **30 peças** por idioma, de 1 VO mestre.
Começar por 6 é o suficiente pra ler o eixo sem estourar a esteira.

---

## 11. COPY DA META — reproduzir como está

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

---

## 12. Passagem de bola — pro Bisturi

Tem tudo pra montar o **lote 1 (6 peças)** sem esperar mais nada:

- Layout e medidas: seção 2 (`1170×2532`, head `y 0–1212`, faixa `y 1212–1498`, painel `y 1498–2532`,
  divisão vertical em `x=462` — funil `x 0–461`, b-roll `x 462–1170`). Todos pares, pro H.264.
- Marcos do funil no tempo: tabela da seção 3. Contador **sobe**: `291 → 348 → 389 → 412`.
- Faixas: 6 primeiras de EN-01…EN-10 (lote A) ou BR-01…BR-10 (lote B).
- Fecho: colapsa pro rosto em quadro cheio nos últimos 1,2s. Sem card final, sem logo, sem seta.
- Antes de exportar: passar o checklist de borrão da seção 8.

Pendente de decisão do Gusta: liberar tradução da copy (lotes C e D).
