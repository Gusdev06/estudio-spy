# Fonte crua — lote 4 spy-zap: o que a montagem dos 4 VOs revelou

Origem: produção do lote 4 (grid de 4 atores no molde dos 35 dias), Bisturi, 2026-09-01.
Peças em `projects/mentoria-spy/centerpag-detect/criativos/lote4-grid-atores-2026-09-01/`.

## 1. O TTS entrega padding de silêncio, e isso corrompe a régua de ritmo

`minimax/speech-2.6-hd` devolve cada beat com silêncio de cabeça e cauda.
Medido nos 7 beats do slot 2: **0,494 · 0,899 · 0,986 · 1,132 · 0,836 · 1,387 · 1,121s**
= 6,855s de padding em 26,880s brutos (25,5% do arquivo).

Consequência: `atempo = soma_bruta / 22,000` mede padding, não cadência.

| medida | slot 2 (Determined_Man) | controle lote 3 |
|---|---|---|
| soma bruta | 26,880s | 26,388s |
| wpm sobre o bruto | 158,5 | 156,9 |
| **fala real** | **20,026s** | **19,437s** |
| **wpm sobre a fala** | **212,7** | **213,0** |

Os 156,9 wpm que circulavam como "a cadência do modelo" são duração bruta.
A fala real do molde roda a **213 wpm**.

Custo do erro: 6 vozes do sistema foram reprovadas por lerem "devagar demais" no bruto.
Remedidas por fala, quase todas serviam. Reprovação errada de
`Casual_Guy`, `Decent_Boy`, `Deep_Voice_Man`, `Imposing_Manner`, `Elegant_Man`, `Patient_Man`.

## 2. O molde não monta por atempo global — posiciona beat na marca

Descoberto medindo os 7 inícios de fala do `vo-master-en.m4a` do controle com
`silencedetect` e comparando com as marcas do `plano.json`:

| marca | fala começa em | offset |
|---|---|---|
| 0,000 | 0,228 | +0,228 |
| 2,578 | 2,742 | +0,164 |
| 5,595 | 5,802 | +0,207 |
| 8,377 | 8,726 | +0,349 |
| 11,160 | 11,438 | +0,278 |
| 14,616 | 14,798 | +0,182 |
| 18,745 | 18,933 | +0,188 |

Sete offsets positivos e pequenos (+0,16 a +0,35s) = cada beat é **colocado na sua marca**,
não concatenado. O silêncio sobra entre beats. O master do controle tem 6,535s de silêncio
em 22,000s.

Por que importa: com atempo global, o slot 2 teria o B6 começando em 12,615s em vez de
14,616s — 2 segundos antes da marca da tarja. A grade inteira desalinha.

Receita que funcionou nos 4 slots: aparar silêncio → aplicar o atempo do controle (1,1995)
→ comprimir só o beat que estoura o slot → posicionar na marca com 0,20s de entrada.
Resultado: 22,000000s exatos nos quatro, fala entrando em +0,200 a +0,221s das marcas.

## 3. Receita do karaokê — reconstruída, não estava versionada

Os 24 PNG do lote 3 existiam; o script que os gerou, não. Reconstruída medindo a caixa
de tinta dos 24 originais:

- Fonte **Arial Black** (testada contra Impact, Tahoma Bold, Helvetica Neue —
  razão largura/altura do original é 9,86; Impact dá 7,29 e Arial Black 11,66 antes
  do ajuste de tamanho, mas as formas de letra batem em Arial Black)
- Card **1170×220**, ancorado em **y1676**
- **Altura de tinta travada em 81px**; só encolhe quando a largura passaria de **1005px** (86%)
- Branco `#FFFFFF`, keyword `#25D366`, contorno `#080808` de ~8px
- Proporção do molde: **14 verdes em 24 cards**

## 4. Nota de operação — a saída do lipsync muda de largura

`sync/lipsync-2-pro` devolveu **1166**, **1170** e **1172** de largura em três chamadas
com a mesma entrada 1170×2532. Reescalonar de volta é passo obrigatório, não opcional.
