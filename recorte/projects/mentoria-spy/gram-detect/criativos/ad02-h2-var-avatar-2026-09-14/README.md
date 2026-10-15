# ⛔ AD02-H2-INSTA com avatar novo — 3 variações · 2026-09-14 · REPROVADO

> **Veredito do Gusta (16/09):** *"ficou horrível… reconstruir e não fazer gambiarra… ficou tudo errado a edição"*. As peças 50-52 **não sobem**. O método descrito abaixo — devolver as camadas por recorte do original — está **revogado**. Para refazer: reconstruir cada camada (medir fonte/cor/tempos do karaokê e redesenhar, remontar os painéis como elementos próprios) e compor sobre o avatar em tela cheia. Registro em `decisions/log.md` (16/09).

Pedido do Gusta: "quero fazer 3 variações desse mas mantendo o hook atual, muda só o avatar", sobre `~/Downloads/AD02 - H2 - INSTA.mov`.

**Original:** 1080×1920, 30 fps, **36,33 s**, master de alta qualidade (11,6 Mbps) — não é swipe comprimido. md5 `ca528edb89e71cf77d739f64560f1df7`. Cópia em `REFERENCIA-original.mov`. Perguntei se havia projeto de edição com as camadas separadas; **só existe o .mov exportado**, então as camadas foram preservadas por recorte.

## Estrutura medida

| frames | tempo | conteúdo | ação |
|---|---|---|---|
| 0–191 | 0,00–6,40 | **HOOK**: clipe de reação de terceiro + faixa "HEADING: 💔 Man catches girlfriend texting 22 different guys daily after 5 years together." | **intacto** |
| 192–1089 | 6,40–36,33 | homem de moletom creme falando o roteiro, com painéis do app, karaokê e setas queimados por cima | **avatar novo** |

O trecho do avatar tem 9 blocos, e o editor foi **fechando o plano** ao longo deles (o bloco 1 é plano médio, o 4 e o 9 são close). Em 6 dos 9 blocos o rosto fica **desfocado atrás de um painel** do app.

| bloco | frames | o que aparece |
|---|---|---|
| 1 | 192–311 | rosto nítido + card "Connecting to Instagram" embaixo |
| 2–3 | 312–457 | rosto desfocado + card do perfil `bennet_chloe_` |
| 4 | 458–607 | **rosto nítido em tela cheia** (close) |
| 5–6 | 608–814 | rosto desfocado + painel "Real-time access / Suspicious data detected" |
| 7 | 815–848 | rosto desfocado + print do feed do Instagram |
| 8 | 849–966 | rosto desfocado + print das DMs |
| 9 | 967–1089 | rosto nítido + setas brancas + "CLICK THE BELOW" |

## Por que as camadas foram recortadas, não recriadas

O karaokê deste criativo é **palavra a palavra**: o bloco de 3 palavras fica fixo e o destaque anda de uma para a outra, alternando **amarelo e vermelho**, em fonte condensada pesada com contorno preto grosso. São ~120 estados em 30 s, em **duas alturas diferentes** (mais alto no bloco 1, onde o card ocupa a base). Recriar isso seria aproximação; recortar a faixa do original devolve **pixel a pixel**.

O mesmo vale para os painéis do app, as setas e o CTA. O avatar novo entra **por baixo** e cada camada volta por cima, recortada do próprio original:

| região | retângulo (x0,y0,x1,y1) | onde entra |
|---|---|---|
| karaokê alto + card | 0,1090 – 1080,1920 | bloco 1 |
| faixa do karaokê | 0,1500 – 1080,1900 | blocos 2–8 |
| painel do app | 90,250 – 990,1580 | blocos 2,3,5,6,7,8 |
| "CLICK THE BELOW" + faixa do karaokê | 0,130 – 1080,390 · 0,1500 – 1080,1900 | bloco 9 |

Nos blocos desfocados o avatar leva `boxblur` antes de receber o painel, para casar com o original.

### As setas foram a exceção
As 3 setas do original são **branco semitransparente**: a luminância máxima dentro delas é 204, não 255. Não saem por máscara, e o recorte retangular traria o rosto do rapaz antigo colado por cima do avatar novo (foi o que aconteceu na 1ª montagem). Foram **redesenhadas** em `setas/*.png` com PIL, nas medidas do original (x 295–755, três chevrons a partir de y 545, espessura 46, opacidade crescente de cima para baixo) e entram como overlay com alfa em 6 fases de pulso.

## Elenco

Todos no mesmo banheiro, mesmo moletom creme e mesma luz, por **edit do frame do próprio original**:

| peça | avatar |
|---|---|
| **a1** | homem branco, ~30, cabelo castanho curto e barba aparada |
| **a2** | homem latino, ~27, cabelo preto penteado para cima, barba por fazer |
| **a3** | homem indiano, ~35, cabelo preto e barba cheia aparada |

Peças: `CRIATIVOS-PRONTOS/50`, `51` e `52` — 1080×1920, 1090 frames, **36,33 s**, a mesma duração do original.

## Custo real — US$ 3,20

| item | valor |
|---|---|
| 3 imagens `gpt-image-2/edit` (medium) | US$ 0,20 |
| 4 clipes Pruna de 30 s (3 + 1 regerado) | US$ 3,00 |
| montagem, setas, conferência | US$ 0,00 |

O clipe do a1 saiu com **a mão cobrindo a lente** nos últimos 5 s. Regerado com seed 31 e a trava "He keeps BOTH HANDS OUT OF FRAME for the entire clip: he never raises a hand, never gestures toward the camera, never brings a palm or fingers anywhere near the lens" — resolveu de primeira.

## Reproduzir

```
python3 gram-detect/criativos/ad02-h2-var-avatar-2026-09-14/montar-ad02.py clipes/<id>.mp4 AD02-H2-<id>.mp4
```
De `projects/mentoria-spy/`. `Z1`, `Z4`, `Z9` por env ajustam o zoom do avatar em cada bloco de rosto nítido, e `BLUR` o desfoque dos blocos de painel.

## O que conferir no olho

- **Zoom por bloco:** o avatar é gerado num plano só e acompanha o fechamento do original por crop central. Os fatores estão calibrados por comparação, não por medição automática — a segmentação da cabeça falhou porque o fundo do banheiro é escuro como o cabelo.
- **Emenda das regiões recortadas:** junto com cada camada vem uma moldura do fundo original. Como o avatar foi gerado no mesmo cenário e com o mesmo moletom, a emenda tende a sumir; onde não sumir, é ali que se vê.
