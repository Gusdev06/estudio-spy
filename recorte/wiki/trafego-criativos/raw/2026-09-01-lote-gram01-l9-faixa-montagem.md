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

⚠️ **Nota de método:** medir a faixa por variância temporal **deixou de funcionar na v2**. Com
o lipsync só a boca se mexe, então a base do bloco de cima também congela e cola no bloco da
faixa — o detector devolveu 1121 em vez de 1212. Passei a localizar a faixa pela **cor chapada**,
que dá um penhasco de uma linha. O método antigo continua certo pra medir *referência*, não
pra medir *peça nossa já montada*.

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
