---
tipo: lote-criativo
atualizado: 2026-09-01
oferta: go.zappdetect.com (spy gram / Gram Detect)
formato: L9 — split de 3 blocos, funil como painel lateral
roteiro: ../../roteiros/2026-09-01-gram01-modelado-l9-roteiro-mestre.md
referencia: ../../referencias/2026-09-01-teardown-vencedor-gram-sophia-jones.md
peca-modelada: ../../escalados/instagram/01-sophia-jones-1761247818659822.mp4
tags: [lote, spy-gram, split-screen, faixa-de-hook, L9, lote-1-faixa]
---

# Lote 1 — GRAM 01 · L9 · eixo faixa de hook

6 peças, `1170×2532`, **975 frames · 32,500s · 30fps**. Uma alavanca só: **a faixa**.
Rosto, b-roll, VO e funil são idênticos nas seis.

**Duas versões, as duas guardadas:**

| | Onde | O que é |
|---|---|---|
| **v2** (atual) | `pecas/gram01-l9-en-0N-v2.mp4` | head e cauda com **lipsync** |
| v1 | `pecas/v1-sem-lipsync/gram01-l9-en-0N.mp4` | sem lipsync — controle legítimo |

A v1 **não foi sobrescrita**: com lipsync × sem lipsync, mesma faixa, é um teste que dá pra ler.

| Peça | Faixa (linha 1 / linha 2) |
|---|---|
| `pecas/gram01-l9-en-01-v2.mp4` | 👀 THE PROFILE IS PUBLIC. / THE PATTERN ISN'T. |
| `pecas/gram01-l9-en-02-v2.mp4` | 🔍 EVERYONE LEAVES A TRAIL. / EVEN THEM. |
| `pecas/gram01-l9-en-03-v2.mp4` | ⚠️ YOU ALREADY KNOW. / YOU JUST CAN'T PROVE IT. |
| `pecas/gram01-l9-en-04-v2.mp4` | 📱 STOP CHECKING THEIR PHONE. / CHECK THIS INSTEAD. |
| `pecas/gram01-l9-en-05-v2.mp4` | 🕐 THREE MINUTES. / ONE @USERNAME. |
| `pecas/gram01-l9-en-06-v2.mp4` | 💬 DELETED ISN'T GONE. / IT'S JUST OUT OF SIGHT. |

Copy da Meta: **a do vencedor, palavra por palavra** (seção 11 do roteiro). Lote A — tudo EN.

---

## Layout — medido, não herdado

| Bloco | y | altura | % |
|---|---|---|---|
| Head | 0–1212 | 1212 | 47,87% |
| Faixa | 1212–1498 | 286 | 11,30% |
| Painel | 1498–2532 | 1034 | 40,84% |

Divisão vertical **x = 462** — funil `x 0–461` (39,49%), b-roll `x 462–1170` (60,51%).

**Medi a referência por variância temporal** (59 frames, 1,0s→30,0s), não por chute: a faixa é
a única coisa congelada no vídeo inteiro, então ela aparece como bloco de variância ~2,7
entre um head que varia 14–21 e um painel que salta pra 37. As bordas são penhascos de uma
linha: `y306→307` e `y378→379`. Ponto de corte varrido a 30fps: **31,333s** (frame 940/975),
onde a diferença do layout pula de 11,7 pra 91,6. Frames anotados em `medicao/`.

⚠️ **Correção que este lote fez no teardown.** O teardown media a divisão em 35,8% (x≈129 em
360px), por cor e num frame só. Por cor o penhasco cai em x≈128 — mas isso é uma **borda
escura dentro do próprio funil**, não o fim do painel: o movimento continua alto até x=141.
A divisão real é **39,4% / 60,6%**. Montar pelo número antigo cortaria 13px de funil fora do
quadro em todas as peças. O roteiro do Isca já foi alinhado por estes números.

Conformação par (1212 / 286 / 1034 / 462) é exigência do H.264 — altura ímpar não codifica.
**Onde houver dúvida, vale o pixel, não o percentual.**

---

## De onde veio cada bloco

**Head** (`head/head-panel.mp4`, 1170×1212, 940 frames) — recorte de
`criativos-crus/spy-gram/ingles-com-head/BASIC EN 5 24.07.26.mp4`, uma peça L9 nossa em
2160×3840. Medi o layout dela pelo mesmo método: faixa em 49,06%, colapso em 26,633s. Head
limpo de 0 a 26,633s → `crop=1804:1870:178:0` → `1170:1212` → `setpts×1,1765` pra chegar aos
31,333s. A cauda (`head/tail-fullframe.mp4`, 35 frames) é o pós-colapso da mesma fonte, que
já é o rosto em quadro cheio que o fecho pede.

Não gastei geração no head: o material já era nosso e no arquétipo certo.

**Funil** (`funil/funil-painel.mp4`, 462×1034, 940 frames) — `downloads/EDIÇÃO/GRAM MASC ING.mp4`
(46,2s) reconformado em **9 janelas**, cada uma com entrada, saída e fator próprios pra bater
nos marcos da seção 3 do roteiro. Wizard 2 e 3 esticam 2,4× e 2,8× (tela estática, não
aparece); o bloco de acesso comprime 0,46×.

**B-roll** (`broll/`, 708×1034, 940 frames) — gerado (WaveSpeed, wan-2.2 t2v-720p), plano
único em ping-pong lento. É o único ativo que a operação não tinha: o painel direito da nossa
L9 é um celular com o app aberto mostrando nome de terceiro — PII e tela legível, os dois
barrados.

**VO** (`vo/vo-master-en.m4a`) — B1–B7 posicionados no mapa de beats do roteiro, desvio máximo
**+0,30s**, sem colisão. B3 acelerado 1,137× (gravado 6,14s, alvo 5,40s) pra o mapa fechar.
B7 entra em 29,05s e cobre o colapso de 31,333s — o CTA falado por cima do rosto sozinho.

**Faixas** (`faixas/*.png`, 1170×286) — magenta chapado, Arial Black caixa alta branca com
contorno preto, emoji colorido, 2 linhas, mesmo corpo nas duas. Desenhada **por último** na
pilha, senão o painel a apaga.

---

## Trava de PII — como foi resolvida

A gravação do funil mostra um perfil real: foto, nome, @, feed com rosto e caixa de DM com
12 nomes civis. A trava do roteiro (seção 8) manda borrar tudo.

**Retângulo fixo não segura conteúdo que rola.** A primeira passada borrou pelas coordenadas de
um frame só, e o feed e a caixa de DM escorregaram por baixo dos rects — vazou nome em vários
pontos. Como a rolagem é **vertical**, a correção foi trocar por **faixas de altura cheia com x
fixo**: aí pega em qualquer posição de scroll.

- `w4` / `w5` — campo do @ digitado e do login: rect fixo (tela estática) basta.
- `w6a` / `w6b` — o card de perfil **muda de layout enquanto carrega**, então virou duas
  janelas com rects próprios. Numa passada anterior o nome escapava no estado de loading.
- `w7` — janela deslocada pra `33,0s`, onde o funil já rolou além do @. Sem borrão nenhum:
  o texto técnico ("Suspicious messages", "12 flagged conversations") fica nítido, e ele é
  parte do que vende.
- `w8` / `w9` — faixas de altura cheia (`y 235→2532`) sobre a coluna de avatares e a de
  texto. O topo (wordmark do Instagram) e o CTA ficam livres.

Conferido frame a frame: nenhum @, nome, rosto ou legenda de terceiro legível nas 6 peças.

---

## O que este lote NÃO herdou do vencedor

- **O contador que desce.** O vencedor vai de 393 → 377 → 304. Regra da casa é subir.
- **A PII escancarada.** Borrada, ver acima.
- **A mistura EN/PT-BR sem decisão.** Este é o lote A: copy, VO e faixa **todos em EN**.

---

## Lipsync — o risco nº1 da v1, resolvido

O risco que a v1 carregava era a boca: a fonte fala inglês, a VO fala outro inglês, e não
casavam palavra a palavra. Decisão do Gusta foi **recasar a boca em vez de gerar rosto novo**.

- Modelo: `sync/lipsync-2-pro` (WaveSpeed), `sync_mode=cut_off`. Resolveu na primeira —
  não precisei dos fallbacks `sync/lipsync-2` nem `veed/lipsync-v2`.
- Entradas: `head/head-panel.mp4` (o **já conformado**, com o `setpts×1,1765` — é o único que
  casa no tempo da VO) e `vo/vo-master-en.m4a` fatiada por bloco.
- **A cauda foi sincronizada também.** Ela é 1,167s de rosto sozinho e o B7 (o CTA) fala por
  cima. Sincronizar só o painel deixaria o último segundo descasado. O trecho de áudio dela
  tinha só **0,595s** de fala + 0,57s de silêncio — preenchi o silêncio com `apad` antes de
  subir, senão o `cut_off` comeria frames. Em silêncio a boca fecha, como tem que ser.
- **O modelo não reenquadrou nada:** voltou `1170×1212` (940 frames) e `1170×2532` (35 frames),
  30fps. Não precisei reconformar.

Saídas cruas em `lipsync/`, tiras de comparação em `lipsync/cmp/`.

### Travas reconferidas depois da remontagem

| Trava | Medido na peça v2 pronta |
|---|---|
| Head idêntico nas 6 | **0,00/255**, máx 0 — bit a bit |
| Painel (ruído H.264) | 0,68/255 (v1 era 0,70) |
| 6 faixas distintas | 6/6 md5 diferentes |
| Faixa | y **1212–1498** — linha 1211 = 0,000 magenta, 1212 = 1,000 |
| Divisão | x = **462** |
| Colapso | faixa some no **frame 940** exato |
| Saída | 1170×2532 · 975 frames · 32,500s · 30fps · aac estéreo |
| PII | reconferida nas 4 janelas sensíveis — nada legível |

### ⚠️ Nota de método — com uma correção de causa

**O que escrevi primeiro (mantido pra registro, a causa está errada):**

> ~~Medir a faixa por variância temporal deixou de funcionar na v2. Com o lipsync só a boca se
> mexe, então a base do bloco de cima também congela e cola no bloco da faixa.~~

**O que os dados mostram (investigado depois, com o wiki):** o lipsync **não congelou nada** —
a v2 se mexe *mais* que a v1 em toda parte. Medido nas duas, 59 frames cada:

| Zona | v1 (sem lipsync) | v2 (com) | Δ |
|---|---|---|---|
| testa/olhos | 22,84 | 22,82 | −0,02 |
| boca/queixo | 23,36 | 23,84 | **+0,48** |
| pescoço/ombro | 18,33 | 19,56 | **+1,22** |
| base do head | 11,86 | 12,14 | **+0,28** |
| faixa | 0,19 | 0,19 | 0,00 |

E o detector erra **na v1 também**, que não tem lipsync nenhum: devolve 1131 contra os 1121 da
v2. Isso encerra a hipótese — se o mesmo erro aparece sem lipsync, a causa não é o lipsync.

**A causa real é o critério de parada.** A base do head é naturalmente quieta nas duas versões
(~12, contra ~23 do rosto): é ombro e peito, não boca. Um critério que procura um **nível**
deixa o ombro passar antes de chegar na faixa. Um que procura a **transição** acerta:

| Critério | v1 | v2 |
|---|---|---|
| o meu (55% da mediana do head, `min()` dos candidatos) | 1131 ✗ | 1121 ✗ |
| **penhasco — maior queda (`argmin` do diff)** | **1212 ✓** | **1212 ✓** |
| limiar relativo a 10% do máx | 1212 ✓ | 1212 ✓ |
| limiar absoluto `var<8` | 1212 ✓ | 1212 ✓ |
| limiar absoluto `var<12` | 1141 ✗ | 1147 ✗ |

Dois detalhes que valem mais que a correção em si:

1. **Exigir bloco contíguo não salva.** Testei: com o meu limiar, os candidatos já formam **um
   único bloco** de 113 linhas (v1) começando em 1131 — a base quieta do head encosta na faixa
   **sem intervalo**. Não há vale pra separar as duas. Por isso o conserto não é "pegue o maior
   bloco contíguo", é trocar nível por transição.
2. **O meu limiar já era relativo** (55% da mediana do head), não absoluto. Ou seja o problema
   não é absoluto-vs-relativo: é **nível-vs-transição**. Qualquer critério calibrado num vídeo
   quebra no seguinte.

3. ⚠️ **Correção de uma afirmação minha.** Escrevi aqui que *"o penhasco não precisa de
   calibragem"*. **Não é verdade** — testei em 4 vídeos depois e a transição pura, sem número
   nenhum, não se sustenta:

   | Vídeo | topo da faixa | base da faixa |
   |---|---|---|
   | referência Sophia Jones (terceiro) | 349 ✗ (esperado 307) | 380 ✓ |
   | BASIC EN 5 (nossa L9, outro layout) | 332 ✗ (esperado 314) | 411 ✓ |
   | peça v1 (sem lipsync) | 373 ✓ | 461 ✓ |
   | peça v2 (com lipsync) | 373 ✓ | 461 ✓ |

   A transição precisa de uma **janela de busca** — que é um número, só que posicional em vez
   de de nível. É uma hipótese mais fraca, mas não é "nenhum número".

   **E o achado que interessa: as duas bordas não têm a mesma dificuldade.** A borda de baixo
   (faixa → painel) é achada pela transição nos **4 vídeos**, porque é uma subida limpa de
   plano chapado pra painel agitado. A borda de cima (head → faixa) é a frágil: é uma queda
   de uma região *moderadamente* variável pra uma chapada, e ela compete com outras quedas
   dentro do próprio head. Foi exatamente essa borda que meu detector original errou
   (topo 1121 errado, base 1498 certa).

4. **A margem explica os dois casos — e prevê o erro antes dele acontecer.** O wiki mediu a
   *margem* de cada borda (transição vencedora ÷ 2ª maior concorrente) e reproduzi:

   | Vídeo | topo | margem | base | margem |
   |---|---|---|---|---|
   | referência Sophia Jones | 306 ✓ | **2,08x** | 380 ✓ | 2,54x |
   | BASIC EN 5 | 331 ✗ | 1,80x | 411 ✓ | 7,70x |
   | peça v1 | 478 ✗ | **1,05x** | 461 ✓ | 3,52x |
   | peça v2 | 478 ✗ | **1,04x** | 461 ✓ | 3,47x |

   Margem de 1,04x não é acerto nem erro: é **empate**. A transição ganha por 4%, e 4% é menos
   que a diferença entre dois preparos do mesmo vídeo — por isso o wiki acertou o topo onde eu
   errei, medindo o mesmo quase-empate com outra escala de render. Nenhum dos dois estava
   errado; a borda é que não é reprodutível.

   ~~Nos meus 8 pontos a margem classificou perfeitamente: toda medida com margem ≥ 2x acertou,
   toda medida abaixo de 2x errou.~~ **Overfit à minha amostra — corrigido pelo wiki.** No
   pipeline dele as três medidas de margem baixa **acertaram** (referência topo 1,52x, v1 topo
   1,05x, v2 topo 1,04x). Juntando os dois conjuntos (n=14, dois pipelines independentes):

   | Margem | Medições | Acertos |
   |---|---|---|
   | **≥ 2x** | 8 | **8/8** — nenhuma falha nos dois pipelines |
   | < 2x | 6 | 3/6 — **cara ou coroa** |

   Ou seja a margem prevê **reprodutibilidade, não correção**. Abaixo de 2x não é "zona de
   erro", é **zona de sorte**. A demonstração mais limpa disso são os nossos dois conjuntos
   juntos: a borda de cima da v1 e da v2 dá 1,05x e 1,04x **nos dois pipelines**, batendo até
   a segunda casa, com desempate **oposto**. Mesma indecidibilidade, moedas diferentes.

   **Regra da casa:** acima de 2x, confie (8/8). Abaixo, meça de novo por outro método — e
   **não conclua que errou, conclua que não sabe**. A formulação importa: quem medir 1,2x e
   tiver acertado, lendo "abaixo de 2x erra", vai concluir que errou e ir mexer numa medida boa.

   Amostra ainda pequena e de um layout só. **O que o próximo teste procura é um contraexemplo
   acima de 2x** — não existe nenhum até agora.

   Consequência prática: isso **reforça** a regra em vez de enfraquecê-la. Pra peça nossa, a
   cor chapada resolve as duas bordas de forma determinística — linha 1211 = 0,000 magenta,
   1212 = 1,000, 1497 = 1,000, 1498 = 0,000. Nenhuma janela, nenhum nível, nenhuma margem a
   avaliar. Ali a cor não é alternativa à variância: é estritamente melhor.

**A conclusão prática continua a mesma** — e é o que a regra manda: peça **nossa** já montada
se mede pela **cor chapada** da faixa, que é determinístico (medimos um objeto que desenhamos,
com uma cor que escolhemos), não estatístico. Referência de terceiro se mede por variância,
porque lá não se sabe a cor. Regra completa em [[medir-fronteira-de-bloco-em-video]].

**Como reconhecer cada erro** (é o que faz a regra ser usável por quem não viveu este lote):

- **a cor errou** → sobrou conteúdo se mexendo dos **dois lados** da fronteira que ela deu;
- **a variância errou** → a fronteira caiu **dentro** de uma região visualmente contínua,
  sem transição de cor.

---

## Registrado como risco

1. **Enquadramento do head mais fechado** do que o plano médio que o roteiro pede. Testei uma
   versão aberta com fundo borrado e ficou pior (a tira de blur encosta na faixa). O
   descasamento de boca, que era o outro lado deste risco, **foi resolvido pelo lipsync**.
2. **Nenhuma métrica de performance do vencedor foi verificada.** O ranking dele é proxy de
   Ad Library — sem gasto, CTR, CPA ou ROAS. Sinal de sobrevivência, não campeão medido.
3. **O ângulo inteiro roda perto da linha da Meta.** A página Quinn, do mesmo grupo, foi banida.

---

## Pastas

```
medicao/   frames anotados da medição da referência (o que prova que medi)
head/      head-panel.mp4 + tail-fullframe.mp4   (entradas do lipsync)
lipsync/   saídas cruas do lipsync + audio fatiado + cmp/ (tiras antes/depois)
funil/     w1..w9 + funil-painel.mp4
broll/     clipes gerados + broll-painel.mp4
faixas/    en-01..en-06.png
vo/        B1..B7 + vo-master-en.m4a
pecas/     as 6 peças v2 + posters
pecas/v1-sem-lipsync/   as 6 v1 + posters (controle, não sobrescrever)
```

## Custo

| Rodada | Gasto | O que comprou |
|---|---|---|
| Montagem | ~US$1,20 | 3 clipes de b-roll úteis + 1 chamada desperdiçada minha |
| Lipsync | **US$2,72** | head 31,3s + cauda 1,2s (`lipsync-2-pro`) |

⚠️ O `base_price` de US$0,08 do `lipsync-2-pro` é **por unidade, não por chamada** — os 31,3s
do head custaram muito mais que isso. Estimar por **duração × preço unitário** antes de
disparar, nunca pelo preço base. `wavespeed price` sem inputs reais devolve US$0 e não serve.

Mídia pesada não entra no git (`.gitignore` da raiz barra mp4/png/jpg em `projects/**`).
