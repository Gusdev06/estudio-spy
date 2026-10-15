# GD-AD01 — variação D: avatar novo gerado do zero, mesma edição (2026-09-03/04)

Ordem do Gusta: "gerar do 0 com outro avatar e construir o criativo do 0 com a mesma edição". O rosto é novo (OmniHuman 1.5 sobre `base/avatar-base-1.png`, casting em `casting.md`), a voz é a original e toda a edição é reconstruída pelo molde `remontar.sh` a partir do próprio campeão.

| | Arquivo |
|---|---|
| **Ad A** (controle) | `criativos-crus/spy-gram/ads-en/GD-AD01.mp4`, intocado |
| Talking head cru | `clipes/talking-head-omnihuman.mp4` — 718×1286, 25 fps, 32,601 s, com áudio (o original passado pelo modelo) |
| Talking head preparado | `clipes/talking-head-1080x2400-30fps.mp4` — zoom 1,25× (Lanczos), tela alta 1080×2400, 30 fps, mudo |
| **Ad D** | `GD-AD01-D-avatar-omnihuman.mp4` — 1080×1920, 30 fps, 978 frames, 32,6 s, H.264 crf 16 bt709, **áudio original** (md5 `af796be7…`, igual ao campeão) |

## Custo real

| item | valor |
|---|---|
| imagem-base do avatar | US$ 0,06 |
| OmniHuman 1.5 (WaveSpeed): US$ 0,16/s × 32,6 s | US$ 5,22 |
| remontagem (Bisturi, ffmpeg) | US$ 0,00 |
| **total** | **US$ 5,28** |

## Preparação do talking head (etapa 1)

- Áudio embutido conferido contra `audio-original.m4a`: correlação 0,976, defasagem −23 ms = 1024 amostras a 44,1 kHz, o atraso de priming do AAC, não desalinhamento do modelo. A saída usa o áudio do campeão direto.
- Olhos no clip cru a ~28% da altura, rosto menor que o do campeão (que tem olhos a ~37% nos blocos de rosto cheio). Zoom 1,25× com corte pelo topo põe os olhos a ~35% e aproxima o tamanho do rosto. Tela alta de 2400 px pra cada bloco recortar sua janela sem faixa preta.
- 25 → 30 fps por duplicação de frames (`fps=30`): 1 em cada 5 frames repete.
- Enquadramento por bloco, porque o campeão sobe o rosto quando há painel embaixo: `OFF_A=305` (olhos a ~19%), `OFF_D1=215` (~24%), `OFF_8=245` (~22%), `OFF_C=0` (~35%).

Comando exato:
```
OFF_C=0 OFF_A=305 OFF_D1=215 OFF_8=245 bash gram-detect/criativos/gd-ad01-var-avatar-2026-09-03/remontar.sh \
  gram-detect/criativos/gd-ad01-var-avatar-2026-09-03/clipes/talking-head-1080x2400-30fps.mp4 \
  gram-detect/criativos/gd-ad01-var-avatar-2026-09-03/GD-AD01-D-avatar-omnihuman.mp4
```

## Correções no molde feitas nesta conferência

1. Estado A: o karaokê que vinha dentro do recorte com degradê ficava translúcido (acinzentado). Agora é re-queimado por cima, opaco, na mesma posição (base y 1209).
2. Bloco 8: o recorte do card trazia o moletom cinza do campeão nas laterais e a sombra cinza abaixo do card, visíveis sobre o moletom preto da avatar. Recorte justo x 96–983 · y 1098–1773 com máscara de cantos arredondados (r 40).

Conferência: `conferir-d.py` → `conferencia/folha-D.png` (8 blocos, campeão × D), `conferencia/lado-a-lado-D-t*.png`, `conferencia/zoom-costuras-D.png`.

## O que difere do campeão

| Dimensão | Campeão | Variação D | Alavanca ou contaminação? |
|---|---|---|---|
| Rosto | morena, cabelo escuro solto | **outra pessoa** (loira-escura, rabo baixo, sardas, moletom preto) | **alavanca** |
| Cenário | quarto com closet aberto | quarto com closet aberto (gerado, parecido) | quase igual |
| Voz e roteiro | original | **idêntico** (áudio do campeão) | igual |
| Painéis, card, story, setas, caixa do gancho | original | recortados do original nos mesmos frames | igual |
| Karaokê | Inter Bold branco com sombra suave | re-queimado em Inter Bold 69 com glow em 2 passadas, mesmas palavras e tempos | aproximação |
| Tamanho do rosto | grande, ocupa a largura | menor mesmo com zoom 1,25× | contaminação leve |
| Nitidez | 1080 nativo de celular | 718 px de fonte × 1,88 de escala total: mais macio | contaminação leve |
| Transições do bloco B | glitch RGB na entrada, arrasto com blur na saída | corte seco | contaminação leve |
| Fundo do bloco B | rosto original desfocado | rosto novo desfocado (só nas margens do card) | igual em função |
| Jump cut 27,3 s | tem | não tem | leve |
| fps | 30 nativo | 25 → 30 por duplicação | leve |
| Movimento | gesticula com a mão nos blocos 3 e 7 | mãos fora do quadro, só cabeça e boca | leve |
| Boca × áudio | gravação real | OmniHuman: sincronizado; expressões mais contidas | a checar no olho |

Leitura: D × A mede **rosto** (e, junto, "pessoa real" × "pessoa gerada"). Roteiro, voz, edição, painéis e caixa são os mesmos.
