---
tipo: referencia-criativo
atualizado: 2026-09-01
tags: [teardown, spy-gram, split-screen, funil-gravado, ugc, vencedor-swipe, instagram]
fonte: https://www.facebook.com/ads/library/?id=1761247818659822
ad_id: "1761247818659822"
arquivo_peca: gram-detect/escalados/instagram/01-sophia-jones-1761247818659822.mp4
---

# Teardown — vencedor do swipe GRAM (Sophia Jones · 1761247818659822)

32,5s · 360×640 (9:16) · locução feminina em inglês · **split screen de 3 blocos**.

## Arquivo da peça (pro portal)

Caminhos **relativos a `projects/mentoria-spy/`**:

| O que | Caminho |
|---|---|
| **Vídeo (exibir este)** | `gram-detect/escalados/instagram/01-sophia-jones-1761247818659822.mp4` |
| **Poster / thumb** | `gram-detect/escalados/instagram/01-sophia-jones-1761247818659822-thumb.jpg` |
| **Texto do anúncio** | `gram-detect/escalados/instagram/01-sophia-jones-1761247818659822.txt` |
| Cópia idêntica (top 3) | `gram-detect/escalados/top3-ig-e-whatsapp/ig-01-sophia-jones-1761247818659822.mp4` |
| Registro na Ad Library | `gram-detect/manifest.json` → `ad_id: 1761247818659822` |

`.mp4` 1.061.460 bytes, md5 `9e300448c20fd4d138ba074a2e35caa1` · `-thumb.jpg` 276.927 bytes,
md5 `7e8326af0285a0387a13dd88fd2ce3dd` (conferidos contra o `manifest.json`). A cópia em
`top3-ig-e-whatsapp/` é byte a byte a mesma — **exibir a de `instagram/`**, que é a canônica.
Ad Library: <https://www.facebook.com/ads/library/?id=1761247818659822>

⚠️ Mídia pesada não entra no git: o portal referencia o arquivo no disco, não o versiona.

---

É a peça **#1 do swipe de Instagram**: 3,2 dias no ar, rank de impressões #1 de 27, sem flag
de baixo volume, e a página roda **6 peças no mesmo ângulo de copy**.

> ⚠️ **O ranking é proxy de Ad Library, não performance.** A Meta não publica gasto, CTR, CPA
> nem ROAS. O que existe aqui é: (a) ausência da flag "baixo volume de impressões", (b) a ordem
> em que a busca `sort=total_impressions desc` devolveu os cards, (c) dias no ar, (d) repetição
> do ângulo. **Nenhum número de performance desta peça foi verificado** — não há dado de Meta
> Ads nem de UTMify cruzado com ela. Ler como *sinal de sobrevivência*, não como campeão medido.

---

## COPY DO VENCEDOR — reproduzir como está

> **Ordem do Gusta: copiar a copy, não reescrever.** Extraída do `.txt` da peça e conferida
> campo a campo contra o `manifest.json` (`ad_id: 1761247818659822`) — os dois batem.
> A variação vai no visual e no gancho.

**Texto principal (primary text)**

```
Ever wondered what someone's Instagram activity really looks like? 👀 Our tool analyzes any public profile and shows you who they follow, what they like, and the accounts they interact with the most. Just type the @username — the first analysis is free.
```

**Título (headline)**

```
Analyze any @username in seconds
```

**Descrição**

```
Free first analysis. No login needed.
```

**Botão (CTA)**

```
Saiba mais
```

**Link de destino**

```
GO.ZAPPDETECT.COM
```

⚠️ **Divergência de idioma registrada:** primary text, headline e descrição em **inglês**, botão
em **português** ("Saiba mais"), e o conteúdo dentro do funil (legenda do feed, nomes dos DMs)
em **português do Brasil**. O anúncio está sendo servido pra público BR com copy em EN. Não é
descuido de transcrição — é o que a Ad Library devolve. Se for modelar, decidir o idioma de
propósito em vez de herdar a mistura.

---

## Locução — texto corrido

> There's one detail on Instagram that gives almost everyone away. The problem is, hardly anyone
> knows where to look. You don't need to guess, or argue, or secretly check someone's phone —
> because when people try to hide something, they usually leave small traces behind without
> realizing it. That's why so many people uncover messages, contacts and suspicious behavior,
> even when the other person thinks they deleted everything. You just need to know where to look.
> Access is right below, while this tool is still available.

| Tempo | Fala |
|---|---|
| 0,0–3,8 | There's one detail on Instagram that gives almost everyone away. |
| 3,8–7,5 | The problem is, hardly anyone knows where to look. |
| 7,5–12,9 | You don't need to guess, or argue, or secretly check someone's phone. |
| 12,9–18,3 | Because when people try to hide something, they usually leave small traces behind without realizing it. |
| 18,3–26,3 | That's why so many people uncover messages, contacts, and suspicious behavior, even when the other person thinks they deleted everything. |
| 26,3–29,0 | You just need to know where to look. |
| 29,0–32,2 | Access is right below, while this tool is still available. |

**Método:** áudio extraído com ffmpeg (mono 16 kHz) e transcrito localmente com `mlx-whisper`
(`whisper-small.en`) — nada saiu da máquina. A última frase sai como *"This is right below"* nas
peças de voz feminina e como *"Access is right below"* na peça #3 (voz masculina, mesmo roteiro);
**"Access"** é a leitura correta e é a que o transcript da peça #10 já registrava.

---

## O gancho

Três camadas empilhadas nos primeiros 2 segundos, e **nenhuma delas é a copy da Meta**:

| Camada | Conteúdo | Job |
|---|---|---|
| **Faixa queimada** | 🔍 `LOOK CLOSER BEFORE YOU TRUST.` — caixa alta, branco com contorno, sobre grafite verde-limão em barra preta | thumbstop sound-off. Fica **o vídeo inteiro**, nunca troca |
| **Falada** | "There's one detail on Instagram that gives almost everyone away." | curiosity gap. Promete *um detalhe*, não um produto |
| **Visual** | wizard `What do you want to discover?` com 4 checkboxes já marcados | mostra a mecânica antes de qualquer promessa verbal |

O gancho falado **não repete** o gancho escrito, e nenhum dos dois repete a copy da Meta. São
três entradas diferentes pro mesmo espectador — quem lê no mudo, quem ouve, e quem só vê a UI.

---

## O formato — split de 3 blocos (layout novo)

Não é o L1 do catálogo (faixa · head · screen). Aqui o terço inferior é **dividido na vertical**:
o funil e a dor rodam **ao mesmo tempo**, não alternados.

```
┌──────────────────────────────┐  y 0
│                              │
│      TALKING HEAD UGC        │  47,7% da altura
│  (mulher, bancada de beleza) │
│                              │
├──────────────────────────────┤  y 306
│ 🔍 LOOK CLOSER BEFORE        │  11,6%  ← faixa fixa, preta + grafite verde
│    YOU TRUST.                │
├────────────┬─────────────────┤  y 380
│  FUNIL     │                 │
│  (screen   │  B-ROLL DE DOR  │  40,6%
│  recording │ (casal na cama, │
│  do app)   │  ele no celular)│
│   39,4%    │      60,6%      │
└────────────┴─────────────────┘  y 640
    x 0–141      x 142–359
```

**Medidas e método.** As fronteiras **horizontais** (head/faixa/painel) foram medidas por perfil de
luminância e **reconferidas por variância temporal** sobre 59 frames (1,0–30,0s): batem em `y=306`
e `y=380`. A divisão **vertical** do painel foi medida por **variância temporal**, não por cor —
ver abaixo.

Em 360×640: head `y 0–305`, faixa `y 306–379`, painel `y 380–639`, divisão vertical em **`x=142`**
(39,4% funil / 60,6% b-roll). Em 1080×1920: head `0–916`, faixa `916–1139` (h≈223), painel
`1139–1920`, divisão vertical em **`x≈426`**. No recording de origem (1170 de largura): **`x≈462`**.

**Onde houver dúvida, vale o pixel, não o percentual.** Os percentuais foram medidos em 360 de
largura e só sobrevivem ao arredondamento: recalcular `39,4% × 1170` dá 461, e H.264 pede dimensão
par. A conformação correta é `x=462` — funil `0–461`, b-roll `462–1170`.

> ⚠️ **Correção de 01/09 — a divisão vertical estava errada neste teardown.** A primeira medida
> disse 35,8% (`x=129`) e veio de **cor num frame único**: eu peguei o maior salto de luminância
> entre colunas. Nesse layout isso engana, porque **existe uma borda escura DENTRO do painel do
> funil** — a moldura do card do app — em `x≈128`, onde a luminância despenca de 117 para 42. É um
> penhasco de cor real, mas não é o fim do painel.
>
> A medida certa é por **variância temporal**: o funil troca de tela 10 vezes e o b-roll é um plano
> único quase parado, então a coluna que separa os dois é onde o movimento morre. Sobre 59 frames, o
> desvio-padrão temporal fica em ~78 até `x=141` e cai para ~10 em `x=142` — queda de 7× numa coluna
> só. O movimento continua alto **através** da borda escura, provando que ela é interna ao funil.
>
> Montar em 35,8% cortaria **13 px de funil** fora do quadro. Medida do Bisturi, conferida aqui de
> forma independente (frames anotados em `../criativos/gram01-l9-faixa-2026-09-01/medicao/`).
> Método virou regra: [[medir-fronteira-de-bloco-em-video]].

**Nenhuma legenda karaokê.** A peça inteira tem *uma* faixa de texto e ela nunca muda. Isso é o
oposto do `wpp-01` (karaokê amarelo, 3–4 palavras por vez) — duas peças da mesma operação
resolvendo o texto de formas opostas.

**Direção de arte do talking head:** mulher ~25 anos, cabelo escuro solto, argola, blusa verde-sálvia,
gravando em ambiente de vaidade/prateleira de cosméticos com luz frontal limpa. Arquétipo "amiga
que descobriu", não especialista. Sem credencial declarada, sem prop de autoridade —
[[autoridade-por-enquadramento]] pela via oposta à do MyoGuard.

---

## Estrutura cena a cena — e onde corta

Cortes medidos por detecção de cena no painel do app (`scene>0.10`), não estimados.

| Corte | Trecho | Painel esquerdo (funil) | Fala por cima |
|---|---|---|---|
| **0,0** | 0,0–1,8 | Wizard **passo 1** — `What do you want to discover?` · 4 checkboxes já marcados (Deleted messages & Instagram DMs / Hidden photos & videos in the gallery / Exact real-time location / Feed, Stories & what they liked) · `→ Confirm & continue` · `STEP 1 OF 3` | "There's one detail on Instagram…" |
| **1,8** | 1,8–4,4 | Wizard **passo 2** — `Who are you going to monitor?` · `A man` / `A woman` · `STEP 2 OF 3` | "…that gives almost everyone away. The problem is…" |
| **4,4** | 4,4–7,5 | Wizard **passo 3** — `Enable invisible mode?` + explicação ("hides every notification… so you stay completely unnoticed") · `⚡ Yes, keep me 100% invisible` / `🚫 No need` · `STEP 3 OF 3` | "…hardly anyone knows where to look." |
| **7,5** | 7,5–14,7 | `Enter the Instagram username` · badge `⚡ 1 free analysis per device` · header `● Live monitoring · 393 online` · **o @ sendo digitado letra a letra** com teclado nativo do iPhone (`Senhas` na barra) · rodapé `go.zappdetect.com` | "You don't need to guess, or argue, or secretly check someone's phone…" |
| **14,7** | 14,7–15,9 | `Connecting to Instagram… Locating the profile` + loader circular | "…because when people try to hide something…" |
| **15,9** | 15,9–22,7 | **Card de confirmação de perfil** — foto real, `rafamendss_`, `18 POSTS · 1.851 FOLLOWERS · 605 FOLLOWING` · ⚠️ `Confirm carefully — this is your single free analysis` · `Is this the right profile?` · `✓ YES, CONFIRM` / `No, search again` (sub-cortes em 18,4 e 21,5: a foto carregando) | "…they usually leave small traces behind without realizing it." |
| **22,7** | 22,7–24,6 | `⚡ ACCESS IN PROGRESS` · `● LIVE INTERCEPTION @rafamendss_` · `Do not close this page until access is granted` · `● BRUTE-FORCE LOGIN` com `LOGIN: rafamendss_01` / `PASSWORD: 28S.X$n3q$b` e barra `…combinations tested / testing…` | "That's why so many people uncover messages…" |
| **24,6** | 24,6–27,2 | **Payoff 1** — feed real do perfil, posts abrindo, legenda em PT-BR, contador `377 people analyzing right now` | "…contacts, and suspicious behavior…" |
| **27,2** | 27,2–31,3 | **Payoff 2** — caixa de DM (`Primary · General · Requests 2`), notas no topo (`Your note`, `what's up?`, `miss this`, `our secret`), lista de nomes masculinos com preview e timestamp · contador `304 people analyzing right now` (sub-cortes 28,5 / 28,7 = scroll) | "…even when the other person thinks they deleted everything. You just need to know where to look." |
| **31,3** | 31,3–32,5 | **A tela colapsa.** Split acaba, faixa some, talking head vai a quadro cheio. Sem card final, sem CTA visual, sem logo | "Access is right below, while this tool is still available." |

**O corte que importa é o de 31,3.** A peça fecha *tirando* tudo da tela e devolvendo o rosto —
1,2s sozinha com a pessoa, exatamente em cima do CTA falado. É o único momento em que o
espectador não tem pra onde olhar além dela.

**O painel de dor nunca corta.** O b-roll do casal na cama roda ininterrupto os 31,3s, enquanto o
funil troca 10 vezes ao lado. Um lado é o relógio, o outro é o metrônomo.

---

## A promessa

**A locução nunca promete espionagem.** Nem uma vez diz "espionar", "hackear", "ler DM", "senha",
"localização" — nem o nome do produto, nem preço, nem marca. O que ela promete é **um detalhe que
quase todo mundo entrega** e que "quase ninguém sabe onde procurar".

A promessa pesada — DM apagada, foto oculta, localização em tempo real, senha quebrada — está
**inteira na imagem**: nos 4 checkboxes do passo 1 e no bloco de brute-force. É a mesma divisão de
trabalho do `wpp-01`: a fala fica vendável, a imagem carrega o que não se pode dizer.

Quebra de objeção embutida na fala, sem anunciar que é quebra de objeção:
*"You don't need to guess, or argue, or secretly check someone's phone"* — mata as três
alternativas do espectador (adivinhar / brigar / mexer no celular) em 5 segundos.

E a justificativa de mecanismo: *"when people try to hide something, they usually leave small
traces behind"*. Não é o app que é mágico — é a pessoa que escorrega. A crença fica no mundo,
não no produto.

---

## A prova

Quatro camadas, nenhuma delas depoimento:

1. **Perfil real na tela** (15,9–22,7) — foto, @, 18 posts, 1.851 seguidores, 605 seguindo. É o
   único dado verificável da peça, e é o que compra crédito pro teatro técnico que vem depois.
   Ver [[perfil-real-como-prova]].
2. **Número específico quebrado** — `1.851`, `605`, `18`, e a senha `28S.X$n3q$b`. Especificidade
   no lugar de alegação. Ver [[numero-especifico-quebrado]].
3. **Contador ao vivo** — `393 online` → `377 people analyzing right now` → `304 people analyzing
   right now`.
4. **Payoff em duas etapas** — feed primeiro (inofensivo, prova que entrou), DM depois (o que a
   pessoa veio buscar). Nunca ao contrário.

⚠️ **Defeito de craft registrado:** o contador **cai** (393 → 377 → 304) ao longo da peça. A regra
da operação é [[contador-que-sobe-como-prova-de-trabalho]] — número que desce lê como fila
esvaziando, não como demanda. É um erro do vencedor, não um traço a copiar. **Na nossa versão,
subir.**

---

## O CTA

- **Falado:** *"Access is right below, while this tool is still available."* — direção
  ("right below") + escassez ("still available"), 3,2s, sem grito.
- **Visual:** nenhum. Sem card final, sem seta, sem "clique no link", sem logo.
- **Na Meta:** botão `Saiba mais` → `GO.ZAPPDETECT.COM`.

A peça delega o CTA visual pro chrome do próprio anúncio. Zero segundos gastos com branding.

---

## Cruzamento com o wiki — o achado que importa

**O painel esquerdo desta peça é o [[template-funil-gravado-9-modulos]] rodando inteiro.** Wizard de
3 passos → input do @ → confirmação de perfil real → login falso → contador → acesso → feed → DMs.
Os mesmos 9 módulos, o mesmo app `Gram Detect`, o mesmo `go.zappdetect.com`.

A diferença com a [[familia-criativos-gram-funil-gravado]] (nossos 12 arquivos) é só o **invólucro**:

| | Nossos 12 (família GRAM) | Vencedor do swipe (#1) |
|---|---|---|
| Funil gravado | **tela cheia**, é a peça inteira | **39,4% da largura**, painel lateral |
| Talking head | nenhum | 47,7% da altura, o vídeo todo |
| Locução | nenhuma (peças mudas) | 29s de VO cobrindo os 32,5s |
| B-roll de dor | nenhum | 60,6% do painel, ininterrupto |
| Faixa de hook | nenhuma | fixa, o vídeo inteiro |
| Duração | — | 32,5s |

Ou seja: **não falta funil pra gente, falta casca.** O ativo mais caro (a gravação do funil, 6
idiomas × 2 gêneros) já existe e já é o que o vencedor usa — só que ele o trata como *prova de
apoio* e não como o anúncio.

### Roteiro mestre, N rostos, N vozes

Conferi as 4 peças de vídeo da Sophia Jones. **Todas rodam o mesmo roteiro, palavra por palavra**
(#1, #3, #6, #10 — transcritas uma a uma). O que muda:

| Peça | Duração | F0 mediana da voz | Rosto na tela | Faixa de hook |
|---|---|---|---|---|
| #1 | 32,508s | 258 Hz (feminina) | mulher | 🔍 LOOK CLOSER BEFORE YOU TRUST. |
| #3 | 32,508s | 112 Hz (masculina) | homem | 💻 THE WEBSITE IS JUST ONE CLICK AWAY. |
| #6 | 32,137s | 138 Hz (masculina) | homem | ⚠️ TRUST YOUR INSTINCTS, BUT CHECK THE FACTS. |
| #10 | 32,508s | 258 Hz (feminina) | homem de óculos | IF YOU SUSPECT… |

(F0 estimado por autocorrelação sobre os trechos vozeados — método local, é estimativa de altura
de voz, não identificação de locutor.)

Duas leituras que valem dinheiro:

1. **A #10 tem voz feminina num rosto masculino** — mesma F0 da #1, mesmo roteiro, mesma duração
   ao milissegundo. O talking head dessa família **não é quem fala**. É B-roll de rosto. Isso
   derruba o custo de escalar o vencedor a quase zero: [[molde-de-edicao-n-atores]] levado ao limite.
2. **A faixa de hook é a única variável real entre as 4.** Copy da Meta idêntica, VO idêntico,
   funil idêntico, duração idêntica — só o hook queimado muda. É exatamente o eixo que o wiki
   registra como **parado** na nossa família ("nenhuma variação de hook"). O concorrente que está
   no topo do ranking está rodando justamente esse eixo.

---

## O que dá pra roubar (e o que não)

**Roubar:**
- A copy da Meta inteira — ordem do Gusta, e ela é o ângulo mais repetido do Tier A (6 peças).
- O split de 3 blocos, com o funil como painel **lateral** e não como peça.
- O roteiro de 29s: curiosidade → 3 objeções mortas → mecanismo ("as pessoas escorregam") →
  payoff social ("so many people uncover…") → CTA de direção + escassez.
- Fechar colapsando pro rosto em quadro cheio nos últimos ~1,2s.
- Rodar 1 VO mestre com N rostos e N faixas de hook.

**Não roubar:**
- O contador que desce.
- A PII de terceiro (abaixo).
- A mistura EN/PT-BR sem decisão.

---

## ⚠️ Travas antes de qualquer modelagem

1. **PII de terceiro, escancarada.** A peça mostra `@rafamendss_` com **foto de perfil real**,
   contagem de seguidores, feed com legenda em PT-BR, e uma caixa de DM com **nomes civis completos**
   (Gabriel Gomes, Eduardo Miranda, Yago Moraes, José Elias Massaria, Fernando Cesar Santos, Jhon
   D4S, João Ribeiro JR) e prévias de mensagem. É a mesma trava já aberta na nossa família —
   [[pii-de-terceiro-em-criativo]]. **Borrar tudo** na nossa versão: @, foto, nomes, legendas.
2. **Prova social fabricada** — contadores "X people analyzing right now" e o bloco de
   brute-force com senha na tela. É teatro; não passa a ideia de que exista métrica real por trás.
3. **A página Quinn, do mesmo grupo, foi banida.** O ângulo inteiro roda perto da linha da Meta.
   Sobreviver 3,2 dias não é o mesmo que estar seguro.

---

## Passagem de bola

Pro **Isca**: a copy está no bloco marcado acima, para reproduzir sem tocar. O que é do roteiro
é a estrutura de 29s (curiosidade → 3 "you don't need to" → mecanismo do escorregão → payoff →
"access is right below, while this tool is still available") e a faixa de hook como **a** variável
a multiplicar. O funil pra ocupar o painel esquerdo já está gravado em `projects/mentoria-spy/`.
