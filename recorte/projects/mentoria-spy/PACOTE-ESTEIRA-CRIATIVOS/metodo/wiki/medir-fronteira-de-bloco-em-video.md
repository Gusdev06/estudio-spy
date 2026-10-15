---
tipo: tecnica
tags: [medicao, edicao, layout, teardown, metodo]
fontes: [[fonte-teardown-vencedor-gram-2026-08-31]], [[fonte-medicao-matte-fade-wpp01-2026-09-11]]
---

# Medir fronteira de bloco em vídeo — e quando cada método mente

Achar onde um bloco termina e outro começa tem **dois métodos, e os dois falham** — em casos opostos. Qual usar depende de você estar medindo algo que **descobriu** ou algo que **construiu**.

| | Referência de terceiro | Peça nossa já montada |
|---|---|---|
| O que você sabe | nada de como foi montada | a faixa é chapada e sintética, você a desenhou |
| Método | **variância temporal** | **cor chapada** |
| Por que o outro falha | cor acha borda decorativa interna | variância confunde bloco quieto com bloco parado |

## Metade 1 — referência de terceiro: variância temporal

Meça **quanto cada linha/coluna muda ao longo do tempo**. Num split os dois lados têm regimes de movimento diferentes — é o que os faz dois blocos.

**A falha da cor aqui: borda decorativa interna.** No [[criativo-gram01-1761247818659822]] a divisão vertical foi medida pelo maior salto de luminância num frame de 10s. Deu `x=129` (35,8%). Errado em 13 px — o certo é `x=142` (39,4%).

| x | variância temporal | luminância (1 frame) |
|---|---|---|
| 127 | 74,2 | 184,9 |
| **128** | 63,5 | **117,3** ← cor despenca |
| 129 | 83,0 | 42,4 |
| 141 | 70,6 | 58,4 |
| **142** | **11,1** ← movimento morre | 59,6 |

A moldura do card do app produz o maior penhasco de cor do quadro sem ser fronteira. O movimento **atravessa** essa borda e só colapsa em 142 — é isso que a desmascara.

**Sintoma de que você caiu nessa:** a fronteira que a cor deu tem conteúdo se mexendo **dos dois lados** dela.

### As duas bordas de um bloco não têm a mesma dificuldade

Esta é a parte que economiza mais tempo, e vale pra qualquer medição por variância:

| borda | o que é | confiabilidade |
|---|---|---|
| **contra o bloco AGITADO** (ex.: faixa → painel) | **subida** de chapado pra agitado | **robusta** |
| **contra o bloco CALMO** (ex.: head → faixa) | **queda** de moderadamente variável pra chapado | **frágil** |

A borda contra o bloco calmo compete com outras quedas **dentro** do bloco de cima — cada região mais parada do head (ombro, peito, fundo) produz uma queda candidata. A borda contra o agitado não tem concorrente: nada mais no quadro sobe tanto.

Medindo a **margem** de cada borda (a transição vencedora dividida pela segunda maior concorrente):

| vídeo | borda de cima | borda de baixo |
|---|---|---|
| referência Sophia Jones | 1,52× | 3,72× |
| peça v1 | **1,05×** | 4,56× |
| peça v2 | **1,04×** | 4,54× |

Uma margem de 1,04× **não é um acerto — é um empate**. A transição ainda ganha, mas por 4%: qualquer mudança de escala de render, recorte de zona ou faixa de frames inverte o resultado.

**É exatamente isso que explica medições divergentes.** Ao testar esta borda em 4 vídeos, o Bisturi obteve topo errado em 2 deles (349 contra 307 esperado na referência; 332 contra 314 na `BASIC EN 5`); no meu pipeline a mesma borda acertou nos 3 que consegui medir. Nenhum dos dois está errado — os dois estão amostrando um quase-empate, e o desempate ficou por conta de detalhes de preparo. **Onde a margem é apertada, o resultado não é reprodutível entre pipelines**, e é isso que torna a borda inutilizável, não o fato de errar num caso específico.

**Regra prática:** meça a margem antes de confiar. Margem < 2× = não use esse número sem uma segunda medição independente.

### ⚠️ Pré-condição: a fronteira precisa existir

A margem diz se uma transição é **detectável com robustez**. Ela **não** diz se aquela é a transição que você procura.

Caso que revelou isso: no [[criativo-wpp01-1762552938111855]] o detector devolveu o topo do card em `y=529` com margem **4,51×** — bem acima do corte — e estava errado. Aquilo era borda interna da UI. O topo do card **não existe como degrau**: o card é alfa-composto e a borda é gradiente ([[card-flutuante-sobre-plano-unico]]). O detector achou a borda real mais forte disponível e a reportou com confiança total.

**Margem alta sobre a fronteira errada é pior que margem baixa, porque não avisa.**

A regra tem **dois passos**, nesta ordem:

1. **A fronteira existe?** O bloco tem borda dura, ou é sobreposição com alpha? Amplie um frame e olhe antes de rodar detector nenhum. Se a borda é gradiente, pare — não há número a extrair, e insistir produz um número confiante e falso.
2. **Só então** meça a margem.

Isso não derruba o corte de 2×; delimita onde ele se aplica. Nas 14 medições anteriores a fronteira sempre existia, e por isso a pré-condição não tinha aparecido.

**Terceiro sinal, quando os dois falham:** no mesmo caso, a borda inferior da matte deu `y=77` numa janela e `y=54` noutra — as duas eram *linhas de texto* do hook. Quem resolveu foi a **fração de pixels quase-pretos por linha**: a matte é 100% preta até `y=96`. Quando variância e luminância discordam entre si, procure uma propriedade do material (cor chapada, opacidade) em vez de um terceiro estatístico.

### ⚠️ Terceiro caso da pré-condição: a fronteira existe, mas é fade (11/09)

O parágrafo acima tratava o `y=96` como *a* fronteira da matte. **Remedido pelo Bisturi em 11/09, não é** ([[fonte-medicao-matte-fade-wpp01-2026-09-11]]): o início bate (100% preta até `y=93`, faixa 91–97 conforme o limiar — o 96 fica), mas **não há penhasco** — std temporal 1,7–2,5 em y 85–95 contra 0,03 na matte pura, margens 1,01–1,19×, e o vídeo só chega a 90% do platô de variância em **y=141**. A matte termina num **fade de ~50 px**.

Isso acrescenta uma terceira resposta à pergunta "a fronteira existe?": **degrau** (meça o penhasco), **alpha sem borda** (não há número — o card desta mesma peça), e **fade** (há **dois** números — fração de preto = início, platô = fim — e nenhum é "a fronteira"). **A matte tem início, não borda.** Detalhe e regra em [[matte-em-fade-nao-tem-penhasco]]. O `y=96` aqui e no teardown fica marcado, não apagado.

### O que o corte de 2× separa (n=14, dois pipelines independentes)

Medido em 4 vídeos × 2 bordas por dois pipelines diferentes (o do Bisturi e o meu, com escalas de render e recortes de zona distintos):

| margem | medições | acertos | leitura |
|---|---|---|---|
| **≥ 2×** | 8 | **8/8** | nenhuma falha nos dois pipelines |
| **< 2×** | 6 | **3/6** | cara ou coroa |

⚠️ **A margem prevê reprodutibilidade, não correção.** É tentador ler a tabela como "abaixo de 2× erra" — foi o que a primeira amostra sugeriu, porque num pipeline as 3 medições de margem baixa erraram. Mas no outro pipeline as 3 medições de margem baixa **acertaram**. O caso mais limpo: a borda de cima da v1 e da v2 dá margem **1,05× e 1,04× nos dois pipelines** — mesma margem até a segunda casa — e **desempate oposto**.

É isso que "não decidível" significa. Abaixo de 2× a borda não decide: você pode receber a resposta certa e não ter como saber que é. Quem medir 1,2× e acertar não está contrariando a regra — está tirando cara.

**O que a tabela autoriza a dizer:** acima de 2×, confie (8/8, dois pipelines). Abaixo, meça de novo por outro método — não conclua que está errado, conclua que não sabe.

Amostra pequena e de um layout só (L9 e a referência dele). O que o próximo teste procura: um contraexemplo **acima** de 2×. Enquanto não aparecer, o corte se sustenta.

## Metade 2 — peça nossa montada: cor chapada

Na peça `gram01-l9-en-01-v2` o detector de variância devolveu `y≈1121` em vez de `y=1212`. A faixa é magenta chapado e dá resposta exata: linha `1211` = 0,000 de magenta, `1212` = 0,96. Uma linha, sem ambiguidade.

Quando a faixa é **sintética e chapada**, cor não é o método pior — é o melhor: você está medindo um objeto que desenhou, com cor que escolheu. É uma checagem determinística, não estatística.

E resolve **as duas bordas** de uma vez, incluindo a frágil: `1211` = 0,000 magenta / `1212` = 1,000 / `1497` = 1,000 / `1498` = 0,000. Sem janela, sem nível, sem margem pra avaliar. É por isso que na peça nossa a cor não é só uma alternativa — é estritamente melhor.

**Sintoma de que você caiu nessa:** a fronteira que a variância deu cai **dentro** de uma região visualmente contínua, e não há transição de cor ali.

### ⚠️ O mecanismo dessa falha não é o lipsync

A leitura inicial foi que o lipsync teria congelado o head (só a boca se mexendo), fundindo a base dele com a faixa. **Medido, não é isso.** Comparando a v1 (sem lipsync) com a v2 (com), por faixa de altura, sobre os mesmos 59 frames:

| região | v1 | v2 | v2−v1 |
|---|---|---|---|
| testa/olhos | 25,01 | 25,00 | −0,01 |
| boca/queixo | 20,19 | 21,01 | **+0,82** |
| pescoço/ombro | 15,63 | 16,58 | **+0,95** |
| base do head | 10,57 | 10,77 | +0,20 |
| faixa | 0,15 | 0,15 | 0,00 |

O lipsync **não reduziu movimento em lugar nenhum** — a v2 se mexe um pouco mais que a v1. A causa real é outra: **a base do head é naturalmente quieta** (ombro e peito, variância ~10,6) comparada ao rosto (~21), em ambas as versões. Um limiar frouxo pega o ombro antes da faixa.

E a falha **não é da v2**: com limiar `var<12`, a v1 (que não tem lipsync nenhum) devolve `y=1081` — pior ainda.

### A correção real: procure a transição, não o nível

Mesmo na peça montada a variância acerta — **se o detector procurar a queda em vez de um valor de corte**. O que quebra é decidir por **nível** (qualquer critério que pergunte "esta linha está abaixo de X?"), não por **transição**.

| detector | v1 | v2 |
|---|---|---|
| **maior queda** (`argmin` do diff) — sem valor de corte | **1212** ✓ | **1212** ✓ |
| nível: 15% do máximo do quadro (=6,07) | 1212 ✓ | 1212 ✓ |
| nível: `var<8` | 1212 ✓ | 1212 ✓ |
| nível: `var<10` | 1177 ✗ | 1180 ✗ |
| nível: 55% da mediana do head (=10,8 / 11,4) | 1149 ✗ | 1143 ✗ |
| nível: `var<12` | 1081 ✗ | 1102 ✗ |

**O eixo não é absoluto vs. relativo.** Os dois critérios relativos da tabela dão respostas opostas: 15% do máximo do quadro acerta, 55% da mediana do head erra. E entre os absolutos, `var<8` acerta e `var<10` erra. O que separa acerto de erro é só **onde o valor calhou de cair** em relação à base quieta do head — ou seja, calibragem. Qualquer nível calibrado num vídeo quebra no seguinte.

A transição é melhor porque não depende de escolher um valor. Mas ela **não é isenta de calibragem** — onde vence por pouco, precisa de janela de busca; ver as duas bordas acima e a regra no fim da página.

### Duas correções que não funcionam (testadas)

**Exigir bloco contíguo não salva.** Trocar "primeira linha abaixo do corte" por "maior bloco contíguo abaixo do corte", mantendo o mesmo nível, devolve o mesmo erro. Motivo: no nível que falha, os candidatos já formam **um único bloco** — `y1149–1497` na v1, `y1143–1497` na v2. A base quieta do head encosta na faixa **sem intervalo**; não existe vale pra separar as duas. Não há bloco melhor a escolher.

**Afrouxar ou apertar o nível também não.** Apertar até funcionar é ajustar ao vídeo que está na sua frente, e é exatamente o que quebra no próximo.

*(Os y exatos de falha variam com a escala de render e com onde você corta as zonas — o Bisturi mediu 1131/1121 onde eu medi 1149/1143 com o mesmo critério. A direção e a conclusão são as mesmas; **não trate os números de falha como universais**, só o padrão.)*

A cor continua sendo o método preferido na peça nossa por ser determinística. Mas o erro de nível é uma armadilha **independente do método**, e vale pros dois casos.

## Procedimento

1. N frames espaçados cobrindo o corpo da peça (59 frames, 1,0–30,0s, funcionou). **Cortar fora o trecho depois de qualquer troca de layout** — se a peça colapsa o split no fim, aquele trecho polui a estatística.
2. Reduzir a luminância a `(t, y, x)`; `std` no tempo, `mean` no eixo transversal → curva de movimento.
3. Procurar **a maior queda**, e exigir que seja penhasco (5–10×), não degrau. Degrau suave = provavelmente não há fronteira ali.
4. **Se a peça é nossa e o bloco é chapado, medir a cor também** e exigir que as duas concordem. Discordância aponta um elemento de arte que você não tinha notado.
5. Conferir com mapa de movimento colorido (azul=parado, vermelho=mexe): a fronteira tem que ser visível a olho.

## Concordância entre PEÇAS vale mais que margem dentro de uma

Quando o mesmo elemento aparece em várias peças de um molde, medir as três e comparar é evidência mais forte que qualquer teste de margem.

Caso: na [[familia-criativos-zap-35-dias]] a borda inferior da tarja verde **reprovou** no corte de 2× nas três (margens 0,90× / 1,18× / 1,12×, porque há verde no conteúdo abaixo dela). Mas as três peças, de três Páginas diferentes, deram **`y=125` independentemente**. Três arquivos concordando ao pixel não é coincidência — e nenhuma margem dentro de um arquivo único chega perto dessa confiança.

**Regra:** margem baixa não obriga a descartar a medida se ela **se repete entre peças independentes**. Repetição entre arquivos é a segunda medida independente que a regra pede — e a melhor delas.

## Regras que sobrevivem aos dois casos

**Duas medidas independentes ou nenhuma.** Onde concordam, fechado. Onde discordam, investigue antes de escolher — foi assim que os dois erros desta página apareceram.

**Transição em vez de nível — mas transição também não é grátis.** Procure a queda, não um valor de corte; isso vale seja o corte absoluto ou relativo, linha a linha ou por bloco contíguo. Só que **a transição não dispensa julgamento**: onde ela vence por pouco (borda contra bloco calmo, margem ~1,05×), ela precisa de janela de busca posicional — que é outro número — e deixa de ser reprodutível entre pipelines. Transição é melhor que nível, não é ausência de calibragem.

Uma afirmação anterior desta página — *"o penhasco não precisa de calibragem"* — **estava errada**, e foi o teste em 4 vídeos que derrubou. Fica registrada aqui em vez de apagada.

**Transporte a fronteira em pixel, não em percentual.** O percentual é uma leitura da resolução em que você mediu; recalculá-lo noutra largura reintroduz arredondamento e pode cair em dimensão ímpar, que H.264 não aceita. Meça em px, converta uma vez, conforme pra par, registre o px de cada resolução.

**Errar pro lado de sobrar.** Cortar 13 px a menos de funil é invisível; 13 px a mais decepa a borda do card e denuncia a montagem.

## Como esta página foi construída (e por que isso é parte do método)

Quatro afirmações desta página foram derrubadas por medição depois de escritas — três minhas, uma do Bisturi:

| afirmação | quem escreveu | o que derrubou |
|---|---|---|
| divisão em 35,8% | Peneira | variância temporal, 59 frames |
| "o lipsync congelou o head" | Bisturi | comparação v1×v2 por zona |
| "nunca por cor" / "penhasco não precisa de calibragem" | Peneira | teste em 4 vídeos |
| "margem <2× é classificador perfeito" | Bisturi | 3 contraexemplos no outro pipeline |

**Nenhuma caiu por argumento. Todas caíram por medição de quem recebeu a correção.** É por isso que a evidência mais forte da página existe: os dois pipelines mediram `1,05×` e `1,04×` na mesma borda, batendo até a segunda casa, e desempataram para lados opostos. Se qualquer um dos dois tivesse aceitado a linha do outro sem medir, esse par não existiria — e a página teria "abaixo de 2× erra", que está errado.

**A regra de trabalho, então:** quando duas medições discordam, não escolha a de quem tem mais contexto — reproduza as duas e procure o que explica a discordância. A discordância costuma ser o dado, não o ruído. E ao corrigir alguém, mande os números junto: o outro lado precisa poder derrubar você.

Corolário prático já usado três vezes aqui: **corrija por marcação, não por apagamento**. Erro apagado sem rastro volta — alguém abre uma cópia antiga, vê o número velho e o "restaura".

Relacionado: [[funil-gravado-como-painel-lateral]], [[spec-de-edicao-layouts-spy]], [[catalogo-de-layouts-spy]], [[criativo-gram01-1761247818659822]].

## Off-by-one: índice da última linha ≠ contagem de linhas (01/09)

A armadilha mais barata de cometer e a mais cara de propagar. Uma tarja que ocupa as linhas
`y 0–125` tem **126 linhas**, não 125. Tomar o índice final como contagem gera dois números que
parecem plausíveis e não são:

| | Cálculo | %  | Em 2532px |
|---|---|---|---|
| **Certo** | 126 ÷ 640 | **19,69%** | **498,5** |
| Errado | 125 ÷ 640 | 19,53% | 494,5 |

**O caso real:** a tarja das três de 35 dias foi reportada num doc de seleção como 19,53% / 494px,
enquanto o kit renderizado e a peça no ar têm **498px** — conferido em 5 colunas (`x` = 20, 300,
585, 900, 1150) na fonte 360×640, no PNG do kit e no frame renderizado, as três batendo entre si.

**Por que 4px importam:** num lote que varia **uma alavanca** ([[variar-uma-alavanca-por-vez]]),
uma arte reconstruída 4px menor que a do controle vira alavanca extra. O erro só se materializa se
alguém **redesenhar** a partir do número em vez de **reusar o asset** — que é a defesa real:
peça-controle e peças novas compartilham o arquivo, não a medida.

**Duas checagens que pegam isso na hora:**
1. **Medir em várias colunas.** Uma coluna pode cair numa letra, num contorno ou numa borda; cinco
   colunas concordando são a fronteira.
2. **Fechar o número por dois caminhos.** Contagem de linhas *e* a porcentagem convertida pra outra
   resolução. Se `126/640` e `498/2532` dão a mesma coisa e `125` não, o índice era índice.

Mesma família do erro que esta página já registra em [[spec-de-edicao-layouts-spy]]: um número
plausível medido do jeito errado sobrevive porque ninguém o refaz. Regra da casa —
**marcar o valor velho, não apagar.**

> ⚠️ **Condição que faltava aqui** (lote 4, 01/09/2026): a regra "concordância entre peças vale
> mais que margem dentro de uma" só se sustenta se as medições forem **independentes**. Duas
> leituras que na verdade são a mesma medição repassada concordam perfeitamente e não provam nada.
> Ver [[nao-somar-medicao-emprestada-como-cruzamento]].
