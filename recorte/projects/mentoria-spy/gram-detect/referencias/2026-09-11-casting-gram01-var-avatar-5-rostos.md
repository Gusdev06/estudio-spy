---
tipo: casting
atualizado: 2026-09-11
lote: ../criativos/gram01-l9-var-avatar-2026-09-11/
controle: ../criativos/gram01-l9-faixa-2026-09-01/pecas/gram01-l9-en-01-v2.mp4
alavanca: avatar (só o rosto muda)
pipeline: GPT Image 2 (openai/gpt-image-2/text-to-image) → pruna-ai/p-video/avatar (704×1280)
autor: Peneira
tags: [casting, spy-gram, L9, avatar, lote-var-avatar, gram01]
---

# Casting — GRAM 01 · L9 · variação de avatar · 5 rostos (V1..V5)

Cinco mulheres, cada uma claramente outra pessoa que as demais e que a mulher do controle
(negra, tranças presas, argola grande, top amarelo de alça, sofá cinza, luz fria de noite —
`head/head-poster.jpg`). A voz é a mesma nas 5 (`vo/vo-master-en.m4a`, f0 mediano 170 Hz,
medido pelo maestro) e o avatar **segue o gênero da voz** — regra da casa desde o erro de
10/09 (3 mulheres pra voz masculina, US$ 4,66 perdidos).

Tudo que não é o rosto é **bit-idêntico** ao controle: VO, funil, b-roll, faixa `en-01`, layout,
975 frames / 32,500 s, colapso no frame 940. Este arquivo cobre só o rosto: quem, por quê, e o
prompt literal pra imagem-base.

---

## 1. Enquadramento do controle — medido, não herdado

Método: `VNDetectFaceLandmarksRequest` (Vision, macOS) sobre **63 frames do `head/head-panel.mp4`
a 2 fps (0 → 31,3 s)** e **12 frames do `head/tail-fullframe.mp4` a 10 fps**, mais os dois posters.
Landmarks: centro dos olhos, boca, queixo (ponto mais baixo do contorno), largura do contorno do
rosto. Script em scratchpad (`facedet.swift`); números em % da dimensão do quadro.

### Head (1170×1212 — o bloco de cima da peça)

| Medida | Mediana (63 frames) | p25 – p75 | min – max | `head-poster.jpg` |
|---|---|---|---|---|
| **Olhos (y)** | **47,3 % = 572 px** | 43,9 – 49,1 % | 37,7 – 58,6 % | 48,3 % (585 px) |
| Boca (y) | 72,0 % = 872 px | 67,1 – 74,3 % | 59,3 – 84,3 % | 73,0 % |
| Queixo (y) | 87,0 % = 1054 px | 81,1 – 90,8 % | 74,9 – 99,0 % | 87,8 % |
| Topo da caixa do rosto (y) | 30,1 % = 365 px | — | 24,0 % min | 31,5 % |
| **Largura do rosto (contorno)** | **47,9 % = 560 px** | 45,7 – 49,7 % | 42,9 – 55,2 % | 48,1 % |
| Distância entre olhos | 272 px (23,2 % da largura) | — | 192 – 326 px | 280 px |
| Nariz (x) | 52,2 % | 45,3 – 57,6 % | 35,1 – 76,4 % | 46,2 % |

**Leitura:** plano de cabeça e ombros, mais fechado do que o "plano médio" que o roteiro pede
(risco nº 1 já registrado no README do controle). O queixo fica a 87 % — sobra **~13 % (158 px)**
abaixo dele, que é pescoço, clavícula e a alça do top; **os ombros são cortados nas laterais**
(largura do rosto quase metade do quadro). O topo da cabeça encosta na borda em vários frames
(caixa do rosto começa a 24–30 %; o cabelo preso passa disso).

A cabeça **passeia**: olhos entre 38 % e 59 %, nariz entre 35 % e 76 % da largura ao longo dos
31 s. Isso é o "movimento constante" do arquétipo; o Pruna gera o movimento dele — o que
importa é a **posição de repouso** da imagem-base (mediana), não o extremo.

### Tail (1170×2532 — o rosto em quadro cheio, 31,333 → 32,5 s)

| Medida | Mediana (12 frames) | min – max |
|---|---|---|
| Olhos (y) | **44,2 % = 1117 px** | 41,5 – 45,2 % |
| Queixo (y) | 63,5 % = 1607 px | 59,5 – 64,5 % |
| Largura do rosto | 48,5 % = 567 px | 45,1 – 50,2 % |
| Nariz (x) | 60,1 % | 54,5 – 63,9 % |

O rosto na cauda tem **o mesmo tamanho** do head (567 vs 560 px), mas fica **545 px mais baixo**
no quadro (1117 vs 572). O colapso do controle é isso: mesma escala, rosto desce, aparece o
busto até a cintura.

---

## 2. A conta — onde os olhos ficam na imagem 9:16

O Pruna devolve **704×1280** (9:16). O head é obtido **recortando o topo** do clipe até a
proporção do bloco (1170:1212 = 0,9653): recorte de **704×730** (linhas 0–729; 730 é par) e
escala ×1,662 → 1170×1212. Fator vertical: **730 / 1280 = 0,570**.

| Ponto | No head (controle) | Na imagem 9:16 (alvo do prompt) |
|---|---|---|
| **Olhos** | 47,3 % (572 px de 1212) | **27,0 % = 345 px de 1280** |
| Faixa aceitável (p25–p75 do controle) | 43,9 – 49,1 % | **25,0 – 28,0 %** |
| Topo da caixa do rosto | 30,1 % | 17,2 % = 220 px |
| Boca | 72,0 % | 41,0 % = 525 px |
| Queixo | 87,0 % | **49,6 % = 635 px** (queixo no meio do quadro) |
| Largura do rosto | 47,9 % da largura | **47,9 % = 337 px de 704** (mesmo %: o recorte não mexe em x) |

Ou seja: **no 9:16 a cabeça ocupa de ~17 % a ~50 % da altura**; abaixo do meio é pescoço,
ombro e peito. No recorte do head sobra o busto; na cauda (quadro cheio) o busto aparece, como
no controle. Mãos ficam fora do quadro nos dois casos se o prompt cortar no peito.

**Cauda (PROPOSTA, decisão do Bisturi):** com o clipe escalado pela largura (×1,662 → 1170×2127),
os olhos caem em 573 px; pra bater nos 1117 px do controle o clipe precisa descer **544 px**, o
que deixa 544 px de topo pra preencher (fundo esticado/borrado) e corta 139 px no pé. Alternativa:
escalar pela altura (×1,978 → 1392×2532, corta 111 px de cada lado) — olhos ficam a 681 px
(26,9 %, não 44 %) e o rosto sai **667 px** de largura (57 % vs 48,5 % do controle): rosto mais
perto no colapso, geometria diferente do controle. As duas são escolha de montagem; a primeira
casa tamanho e altura do rosto, a segunda não precisa de preenchimento. Se o prompt deixar
**17 % de parede lisa acima da cabeça** (é o que está pedido), a primeira fica viável.

⚠️ Se o GPT Image 2 devolver proporção diferente de 9:16 (ex.: 2:3), **recorte pra 9:16 antes de
medir** os percentuais — senão a conta acima não vale.

### O que o Bisturi confere na imagem antes de aceitar

Rode o mesmo detector (ou marque à mão numa grade de 5 %) e aceite só se: **olhos entre 25 % e
28 % da altura** do 9:16 (alvo 27 %); **largura do contorno do rosto entre 44 % e 51 %** da
largura (alvo 48 %); queixo entre 46 % e 53 %; nariz entre 42 % e 58 % da largura (centrado, o
Pruna passeia sozinho); **nada de mão, dedo, celular ou objeto na borda de baixo**; olhos abertos
(frame 1 é a miniatura — [[frame-1-sem-piscar]]); boca fechada (o lipsync parte daí); sem
texto, logo, óculos ou marca d'água; pele com poro/brilho visível (se estiver lisa demais,
regera antes de pagar o Pruna); topo da cabeça **dentro** do quadro com ≥ 10 % de folga
(o recorte do head come nada em cima, mas a cauda precisa do fundo). Confira lado a lado com
`head/head-poster.jpg` reduzido à mesma altura: altura da câmera (levemente abaixo do olho,
inclinada pra cima), tamanho do plano, luz frontal disponível, fundo de casa com textura e sem
estúdio. Etnia, idade e cenário **não** se casam — é o que muda.

---

## 3. Evidência pra diversidade dos 5 — quem apareceu e o que fez

### 3a. Nossas 10 peças que gastaram (print do Gerenciador, 03/09 — gasto real, não proxy)

Fonte: `referencias/proprios-2026-09-03/00-ranking-comparativo.md` + frames em
`referencias/frames/proprios-2026-09-03/` (conferidos no olho hoje). Gasto ≠ conversão; dentro do
mesmo conjunto é termômetro do que a Meta quis entregar. Idade e etnia são leitura visual.

| # | Peça | Gasto (US$) | Gênero | Idade (vis.) | Etnia (vis.) | Cenário | Layout |
|---|---|---|---|---|---|---|---|
| 1 | GD-AD01 👑 | 4.074,43 | mulher | ~28 | branca/mediterrânea, morena, sem maquiagem | quarto bagunçado, closet aberto, luz de janela | L8 alternado, karaokê |
| 2 | SPY 5 | 1.663,46 | mulher | ~25 | branca, morena clara | banco de trás de carro à noite, luz do celular | rosto cheio, faixa some aos 8,6 s |
| 3 | GD-AD04 | 610,92 | homem | ~30 | pardo/latino, barba | quarto claro, persiana | rosto cheio + cards |
| 4 | GD-AD05 | 306,91 | mulher | ~25 | branca, morena, olhos marejados | quarto, cômoda branca | rosto cheio + cards |
| 5 | SPY 7 | 50,14 | mulher | ~28 | asiática | sala branca, luz fria | **L9 fixo**, sem legenda |
| 6 | SPY 1 | 46,76 | homem | ~30 | negro, barba | parede bege | **L9 fixo**, sem legenda |
| 7 | GD-AD03 | 33,22 | mulher | 45–55 | branca, grisalha | sala de casa; frame 1 de olhos fechados | kit do campeão, copy acusatória |
| 8 | GD-AD02 | 9,09 | homem | ~35 | branco, barba | quarto, camiseta preta | kit do campeão, 265 wpm |
| 9 | SPY 6 | 1,99 | homem | ~25 | branco | selfie de rua, céu | rosto + card estático |
| 10 | SPY 2 | 0,63 | homem | ~25 | negro, dreads | LED azul | **L9 fixo**, sem legenda |
| — | SPY 3, SPY 4 (o "controle" da Ad Library) | fora do top 10 | mulher | ~25–30 | SPY 4: branca/latina, cabelo escuro solto · SPY 3: negra/parda, cachos | vaidade · sala clara | L9 / split |

O que dá pra ler (com 10 peças, é direção, não prova): **os 4 que gastaram são todos 25–30 e em
cômodo íntimo** (quarto ×3, carro ×1); **3 dos 4 são mulheres brancas/morenas**; os 3 L9 fixos
morreram independente do rosto (asiática, negro, negro com dreads) — ali o molde mata antes do
rosto contar; a única mulher 45+ perdeu, mas com copy acusatória e frame 1 ruim (confundido).
Nenhuma mulher negra jovem rodou fora do L9 fixo — a mulher do controle é, na nossa conta, um
rosto **sem dado**.

### 3b. Os 13 "escalados" da Ad Library (proxy: dias no ar + rank de impressões, sem gasto)

Fonte: `escalados/README.md`, `escalados/TRANSCRICOES.md`, thumbs em `escalados/instagram/`
(folha de contato conferida hoje). ⚠️ Os 5 "Sophia Jones" **são nossos arquivos SPY 1–5**
(`[[swipe-que-mediu-a-propria-operacao]]`) — não são concorrente.

| Rank | Página · peça | Gênero | Idade (vis.) | Etnia (vis.) | Cenário | Obs. |
|---|---|---|---|---|---|---|
| #1 | Sophia Jones 01 (= SPY 4) | mulher | ~25 | branca/latina, cabelo escuro solto, argola | bancada de vaidade, luz clara | o modelo do teardown de 01/09 |
| #2 | Sophia Jones 02 (= SPY 5) | mulher | ~25 | branca | carro à noite | nosso #2 em gasto |
| #3 | Sophia Jones 03 (= SPY 1) | homem | ~30 | negro, barba | parede bege | US$ 47 na nossa conta |
| #4, #5, #7 | Charlotte Miller (estáticos) | — | — | — | UI | sem rosto |
| #6 | Sophia Jones 06 (= SPY 2) | homem | ~25 | negro, dreads | LED azul | US$ 0,63 |
| #8 | VolutPay 08 | — | — | — | mockup | sem rosto |
| #9 | Charlotte Miller 09 | mulher | ~28 | branca, loira/castanha clara | corredor de casa, armário | único vídeo de terceiro com mulher |
| #10 | Sophia Jones 10 (= SPY 3) | **mulher** | ~30 | negra/parda, cachos, moletom cinza | sala clara, quadros | ⚠️ o teardown de 01/09 diz "homem de óculos" — **errado**, conferido aos 15 s e 25 s; ver HANDOFF |
| #11 | VolutPay 11 | homem | ~22 | branco | rua, céu azul | — |
| #12 | VolutPay 12 | mulher | ~30 | morena | poltrona, luz baixa (podcast) | — |
| #13 | VolutPay 13 | homem | ~55 | branco, grisalho, óculos | escritório, malha azul | é este o "homem de óculos" com `IF YOU SUSPECT` |

Rostos de terceiro de verdade (Charlotte Miller, VolutPay): 1 mulher jovem branca, 1 mulher
morena ~30, 1 homem ~22, 1 homem ~55. **Não medido:** nenhuma métrica desses; só sobrevivência
de 2–3 dias.

### Como isso vira 5 rostos

Cobrir o que **tem sinal** (mulher 25–30, branca/morena, quarto — V1), o que **tem sinal
confundido** (asiática em L9 mudo — V3; 45+ com copy ruim — V4 em 40), o que **não tem dado**
(latina ~32 — V2; réplica dentro da demografia do controle — V5). Nenhum homem: a voz é feminina.

---

## 4. As cinco fichas

Gramática comum (é o que **não** muda entre V1 e V5, e é o que casa com o controle): câmera
frontal de celular na mão, um pouco abaixo do olho e inclinada pra cima; cabeça e ombros, ombros
cortados nas laterais, **mãos fora do quadro**; olhos a ~27 % do topo, queixo no meio; olhando
pra lente, **boca fechada**, sobrancelha levemente franzida, cara de quem vai contar uma coisa
pra amiga; luz disponível de casa, um pouco subexposta, baixo contraste, **sem ring light, sem
estúdio**; pele com poro e brilho, grão de celular, sem retoque; ambiente doméstico com textura,
**à noite ou fim de tarde** (como o controle); nada de texto, logo, óculos, chapéu, jaleco.
Nenhuma usa amarelo nem argola grande (marcas do controle).

Padrão do prompt: o de `centerpag-detect/criativos/zap-wpp01-clone-3-ganchos-2026-09-11/base/avatar-wpp01-prompt.txt`
(um parágrafo, inglês, enquadramento em %), com as regras anti-cara-de-IA de
`~/.claude/skills/trocar-avatar/references/casting.md`.

### V1 — `v1-branca-25-quarto`

**Hipótese:** é o rosto-tipo do campeão GD-AD01 (mulher branca/morena ~25–28, sem maquiagem,
quarto bagunçado) transplantado pra casca L9 — se "rosto" for alavanca, esta é a que mais tem
lastro pra ganhar do controle; se perder, o problema é a casca, não o rosto.

```
IDADE/GÊNERO:       mulher, 25
TRAÇO FACIAL:       sobrancelha grossa natural, pinta pequena na bochecha esquerda, olheira leve
ÂNCORA DE FIGURINO: moletom cinza mescla de gola careca, oversized, gola um pouco frouxa
CENÁRIO:            quarto pequeno à noite, cama desfeita, guarda-roupa entreaberto com roupa pendurada
LINHA EMOCIONAL:    confidente, energia baixa, "descobri uma coisa e preciso te contar"
```

**Prompt (GPT Image 2, literal):**

```
Vertical 9:16 video still from a phone's front camera, held in one hand a little below eye level and tilted slightly upward. An ordinary woman around 25 years old, white with light olive skin, long dark-brown hair worn loose and slightly messy with a few strands across her forehead, thick natural eyebrows, a small mole on her left cheek, faint dark circles under her eyes, no makeup. She wears a plain oversized heather-grey crewneck sweatshirt with a slightly stretched collar. No glasses, no hat, no earrings, no logos, no text anywhere. She looks straight into the lens with her mouth closed and her brows slightly drawn together, the quiet serious expression of someone about to tell a friend something she just found out, eyes open. Framing: head and shoulders, shoulders cropped at the sides, top of her head about 17 percent from the top edge, eyes about 27 percent from the top, chin near the middle of the frame, her face about half the frame width, collar and upper chest visible below; hands out of frame. She is sitting on the edge of an unmade bed in a small bedroom at night; behind her a wardrobe with one door half open and clothes hanging, a cream-colored wall, the corner of a pillow. Dim available light from a small bedside lamp to camera-right mixed with cooler light from off-frame, slightly underexposed, low contrast, no ring light, no studio light. Realistic skin texture with visible pores and a little oil on the forehead and nose bridge, mild phone-camera softness and grain, no retouching, not a model, not a stock photo.
```

### V2 — `v2-latina-32-cozinha`

**Hipótese:** sobe a idade e muda a etnia pra latina/morena de ~32 na cozinha — leitura "mulher
casada, rotina de casa"; testa se a audiência BR (servida com copy EN) responde melhor a um rosto
que parece com ela do que ao rosto de vaidade/quarto de 25.

```
IDADE/GÊNERO:       mulher, 32
TRAÇO FACIAL:       linha de expressão leve ao lado da boca, mechas soltas na têmpora, brinco de bolinha dourado pequeno
ÂNCORA DE FIGURINO: regata preta canelada de alça fina
CENÁRIO:            cozinha pequena à noite, azulejo, pano de prato pendurado, chaleira, luz do armário
LINHA EMOCIONAL:    cansada e calma, tom de quem fala baixo pra não acordar ninguém
```

**Prompt (GPT Image 2, literal):**

```
Vertical 9:16 video still from a phone's front camera, held in one hand a little below eye level and tilted slightly upward. An ordinary Latina woman around 32 years old with medium-brown skin, dark hair pulled back into a low messy bun with loose strands at the temples, a faint smile line beside her mouth, small plain gold stud earrings, minimal makeup with slightly tired eyes. She wears a plain black ribbed tank top with thin straps. No glasses, no hat, no necklace, no logos, no text anywhere. She looks straight into the lens with her mouth closed and a calm, slightly worried expression, as if speaking quietly so nobody else in the house hears, eyes open. Framing: head and shoulders, shoulders cropped at the sides, top of her head about 17 percent from the top edge, eyes about 27 percent from the top, chin near the middle of the frame, her face about half the frame width, collarbones and upper chest visible below; hands out of frame. She is standing in a small kitchen at night; behind her a white tiled backsplash, a dish towel hanging from an oven handle, a kettle, cabinets with a warm under-cabinet light. Dim available light, warm from the cabinet light behind her and cooler on her face from the phone screen, slightly underexposed, low contrast, no ring light, no studio light. Realistic skin texture with visible pores and a little oil on the forehead and nose bridge, mild phone-camera softness and grain, no retouching, not a model, not a stock photo.
```

### V3 — `v3-asiatica-27-vaidade`

**Hipótese:** reteste do rosto-tipo da SPY 7 (mulher asiática, US$ 50) **fora** da sala branca e
do L9 mudo — a SPY 7 morreu junto com os outros L9 fixos, então o rosto nunca foi testado sozinho;
aqui ele entra no cenário da peça #1 da Ad Library (bancada de vaidade) com VO, legenda-faixa e
funil iguais aos do controle.

```
IDADE/GÊNERO:       mulher, 27
TRAÇO FACIAL:       pálpebra única, sardas leves no nariz, ponta do nariz e bochechas levemente avermelhadas
ÂNCORA DE FIGURINO: camiseta branca de algodão lisa, gola careca
CENÁRIO:            quarto com bancada de vaidade, prateleira de skincare, espelho com lâmpadas quentes na borda
LINHA EMOCIONAL:    séria, olhar fixo, energia contida — "presta atenção nisso"
```

**Prompt (GPT Image 2, literal):**

```
Vertical 9:16 video still from a phone's front camera, held in one hand a little below eye level and tilted slightly upward. An ordinary East Asian woman around 27 years old with fair skin, straight black hair to the collarbone with a middle part, monolid eyes, light freckles across her nose, the tip of her nose and her cheeks slightly reddish, no makeup except a bit of lip balm. She wears a plain white cotton crewneck t-shirt. No glasses, no hat, no earrings, no logos, no text anywhere. She looks straight into the lens with her mouth closed and a serious, steady expression, brows slightly drawn together, eyes open. Framing: head and shoulders, shoulders cropped at the sides, top of her head about 17 percent from the top edge, eyes about 27 percent from the top, chin near the middle of the frame, her face about half the frame width, collar and upper chest visible below; hands out of frame. She is sitting at a small vanity in her bedroom in the evening; behind her a shelf crowded with skincare bottles and jars, the edge of a mirror with a few warm bulbs along its frame, a pale wall. Available light only — warm spill from the mirror bulbs to camera-left and dimmer cool light from a window off-frame, slightly underexposed, low contrast, no ring light, no studio light. Realistic skin texture with visible pores and a little oil on the forehead and nose bridge, mild phone-camera softness and grain, no retouching, not a model, not a stock photo.
```

### V4 — `v4-branca-40-sala`

**Hipótese:** eixo idade isolado. A única 45+ da casa (GD-AD03) perdeu, mas com copy acusatória,
265 wpm de irmã e frame 1 de olhos fechados — não dá pra culpar a idade. Aqui VO, copy e faixa
são as do controle, então só a idade pesa. 40 e não 50 pra continuar "amiga que descobriu",
não "mãe que avisa".

```
IDADE/GÊNERO:       mulher, 40
TRAÇO FACIAL:       linhas finas ao redor dos olhos e da boca, cabelo castanho-claro na altura do ombro com poucos fios grisalhos
ÂNCORA DE FIGURINO: camiseta verde-escura de algodão lisa
CENÁRIO:            sala de apartamento à noite, sofá, abajur de pé, estante com livros, manta
LINHA EMOCIONAL:    calma, direta, voz baixa de quem já viu isso acontecer com outra pessoa
```

**Prompt (GPT Image 2, literal):**

```
Vertical 9:16 video still from a phone's front camera, held in one hand a little below eye level and tilted slightly upward. An ordinary white woman around 40 years old with fair skin, fine lines around her eyes and at the corners of her mouth, shoulder-length light-brown hair with a few grey strands, worn down and a little flat, natural eyebrows, no makeup. She wears a plain dark-green cotton crewneck t-shirt. No glasses, no hat, no earrings, no logos, no text anywhere. She looks straight into the lens with her mouth closed and a calm, direct expression, the look of someone who has seen this happen to a friend before, eyes open. Framing: head and shoulders, shoulders cropped at the sides, top of her head about 17 percent from the top edge, eyes about 27 percent from the top, chin near the middle of the frame, her face about half the frame width, collar and upper chest visible below; hands out of frame. She is sitting on a couch in a small apartment living room at night; behind her a bookshelf with books and a few objects, a folded throw blanket on the back of the couch, a plain wall. Dim available light from a floor lamp to camera-left, warm, mixed with cooler light from a television off-frame, slightly underexposed, low contrast, no ring light, no studio light. Realistic skin texture with visible pores, faint expression lines and a little oil on the forehead and nose bridge, mild phone-camera softness and grain, no retouching, not a model, not a stock photo.
```

### V5 — `v5-negra-30-mesa-luz-quente`

**Hipótese:** réplica **dentro da demografia do controle** (mulher negra, 25–30) com outra
pessoa, outro cabelo, outra luz e outro cômodo. É o que separa "a alavanca é demografia" de "a
alavanca é a pessoa/execução": se V5 ≈ controle e V1–V4 divergem, é demografia; se V5 também
diverge, é pessoa. Na nossa conta nenhuma mulher negra jovem rodou fora do L9 fixo — é rosto sem
dado. *(É a ficha que o maestro mais provavelmente troca; reserva abaixo.)*

```
IDADE/GÊNERO:       mulher, 30
TRAÇO FACIAL:       cabelo natural curto (sem tranças), pele castanho-escura, maçãs do rosto marcadas, sem brinco
ÂNCORA DE FIGURINO: blusa branca canelada de manga comprida
CENÁRIO:            canto de mesa de jantar de apartamento pequeno, cozinha ao fundo, pendente de luz quente, planta
LINHA EMOCIONAL:    cúmplice, meio-sorriso contido, "vou te falar uma coisa que ninguém te conta"
```

**Prompt (GPT Image 2, literal):**

```
Vertical 9:16 video still from a phone's front camera, held in one hand a little below eye level and tilted slightly upward. An ordinary Black woman around 30 years old with deep brown skin, short natural hair cropped close to the head, no braids, defined cheekbones, natural eyebrows, no makeup, a small healed scar near her right eyebrow. She wears a plain white ribbed long-sleeve top. No glasses, no hat, no earrings, no necklace, no logos, no text anywhere. She looks straight into the lens with her mouth closed and a knowing, slightly conspiratorial expression, the faint beginning of a smile held back, eyes open. Framing: head and shoulders, shoulders cropped at the sides, top of her head about 17 percent from the top edge, eyes about 27 percent from the top, chin near the middle of the frame, her face about half the frame width, collar and upper chest visible below; hands out of frame. She is sitting at the corner of a small dining table in a small apartment at night; behind her the kitchen counter, a warm pendant light hanging over the table, a potted plant, a plain wall. Warm dim available light from the pendant above and slightly behind her, cooler fill on her face from the phone screen, slightly underexposed, low contrast, no ring light, no studio light. Realistic skin texture with visible pores and a little oil on the forehead and cheekbones, mild phone-camera softness and grain, no retouching, not a model, not a stock photo.
```

**Reserva (se o maestro trocar a V5):** `v5r-ruiva-28-escritorio` — mulher branca ruiva ~28,
sardas densas, cabelo preso frouxo, camiseta preta lisa, canto de home office à noite com luz de
monitor + abajur. Mesmo bloco de enquadramento/luz/pele. Hipótese: rosto "distintivo" que
ninguém do acervo testou.

---

## 5. Custo desta etapa (centavos, autorizado)

5 imagens × ≈ US$ 0,06 = **US$ 0,30**; com uma regeração por rosto, US$ 0,60. Fase C (Pruna,
5 × 32,5 s × US$ 0,025 = **US$ 4,06**) **para na estimativa** — só com "sim" do Gusta.

## 6. O que ficou incerto

- Idade/etnia dos rostos do acervo são leitura visual minha, não dado. Gasto é real; conversão não.
- O tamanho da saída do GPT Image 2 na WaveSpeed (se não for 9:16 exato) muda a conta da seção 2 — conferir no arquivo.
- O quanto o Pruna mantém a identidade e a posição de repouso ao longo de 32,5 s não foi medido em lote nenhum da casa (os anteriores tinham 29–33 s e ninguém mediu deriva).
- A cauda: nenhuma das duas montagens propostas é "a certa"; é decisão do Bisturi/maestro.
