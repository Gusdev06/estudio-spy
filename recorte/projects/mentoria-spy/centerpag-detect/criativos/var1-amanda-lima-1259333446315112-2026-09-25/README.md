# Amanda Lima 1259333446315112: variação com avatar e cenário novos · 2026-09-25 · PRONTA

**Peça:** `pecas/variacao.mp4`. H.264 720×1280, 30 fps, **1822 frames** (60,73 s), mais o áudio AAC **copiado** do original. O md5 do stream de áudio é igual ao do original: `f835a265dc0e1dea51ac1947602a1fc3`.
**Original:** `REFERENCIA-original.mp4` (`~/Downloads/Amanda Lima_1259333446315112_2026-09-25.mp4`).
**Avatar/cenário:** mulher de uns 25 anos, loira mel com ondas até o ombro, sardas, cardigã verde-sálvia sobre blusa branca. Sala clara com sofá cinza, estante de madeira, planta alta e cortina branca (`base/casting.txt`, `base/v1.png`).
**Custo real: US$ 1,64** (teto US$ 1,80), cruzado em `wavespeed billings`: imagem 0,0665 + Pruna 0,35 + 0,55 + 0,35 + 0,325.

## Caminho B: nada da mulher original entra na peça
A primeira tentativa (histórico abaixo) parou porque recortar o original arrastava a mulher junto. Nesta versão, tudo o que ficava por cima dela foi **redesenhado do zero**.

| camada | como foi feita | medida no original |
|---|---|---|
| 17 cards (A pill/navy/vidro HIDDEN DATA, C, D, E, G topo/card escuro/3 botões, I, J) | `cards.py`: PIL com supersampling 2×, Arial/Arial Bold. O tamanho da fonte sai da **largura medida** do texto; a posição sai do topo medido da caixa-alta | bbox por cor em cada frame (`work/track.py` → `work/tracks.json`), cores em hex medidas, cantos e bordas pelos zooms |
| animações | curvas de slide copiadas frame a frame: entrada padrão de 12 frames (−424 → 0), saída padrão de 12, barra do topo com 24 frames, saídas I e J mais lentas, botões G entrando com borrão vertical que some em 23 frames | `work/tracks.json`. Não há flutuação: os cards ficam parados dentro de ±1 px |
| 7 flashes/gradações laranja | `flash.py` funciona como **filtro** sobre o quadro novo: `out = A(x,y)·in + B(x,y)` por canal, em células de 80 px suavizadas. O ajuste compara cada frame tingido com o frame limpo vizinho, só com pixels fora dos cards. Ganho por célula com *ridge* puxando pro ganho global | janelas n 174–182, 228–235, 399–406, 1056–1065, 1234–1243, 1358–1366, 1459–1466 |
| ordem das camadas | medida no original: o flash tinge o vídeo, o painel e o mapa; os cards ficam **por cima** do flash (k≈0 medido nos cards A e G). A exceção é o card E na saída (n 1056–1059), que vai por baixo | |
| painel "Accessing WhatsApp" (n 1060–1239) | fundo liso `#e0e0e2` redesenhado, com degradê suavizado de y 714 a 758, e vídeo novo **subindo 215 px**. Só o conteúdo de tela (spinner, textos, barra) vem do original, a partir de y ≥ 772, com máscara do que difere do fundo liso. Nos frames de flash usa o frame limpo mais próximo | deslocamento −215 medido na luminária; α(y) do degradê medido |
| card do mapa (n 1364–1462) | moldura redesenhada. O miolo opaco do original vem **erodido 8 px** (120,838)–(600,1190) | card opaco (std 0,4–1,2) em (112,830)–(608,1198) |

## Pessoa (pipeline Kendall)
1. `base/v1.req.json`: `gpt-image-2/edit` (medium, 1k) sobre o n 212, trocando pessoa e cômodo com a mesma pose e o mesmo enquadramento.
2. `gerar-clipes.sh c1..c4` (SEED=7, prompt só em positivo): 4 clipes com o áudio original, emendados **dentro de flashes** em n 404, 1060 (pico branco) e 1463. Duração: 13,5 / 21,9 / 13,4 / 12,1 s.
3. `checar.py`: 4/4 decodificam inteiros, sem 2º rosto, sem gente entrando e sem troca de pessoa. A variação do rosto (×0,76) vem do jeito como ela se inclina, e o original varia mais (×0,69). No c2, a "borda muda" era a mão dela na borda de baixo.
4. `montar.py`: escala 720/704 (cobre o quadro, com o rosto no alto). Fica ~34 px mais alto e ~10% maior que no original, porque escalar menos deixaria borda preta. Clipe a 24 fps → 30 fps pelo frame mais próximo. **Sync labial** (abertura da boca × envelope do áudio): atraso de 0 a 1 frame nos 4 trechos.

## Varredura final (`varredura.py`)
- Na caixa do rosto da mulher original, fora do flash, a diferença média entre peça e original é **48 (mín. 35) em 0–255**.
- Fração de pixels "quase iguais" (|dif| < 10) fora de cards e miolos: **1,8% em média, no máximo 4,7%** fora do flash, só coincidência de cor.
- Nos flashes, os piores frames de rosto (n 179, 1062) ficam em 16%, e o quadro inteiro chega a 95% no n 1239. Isso é tinta chapada: os dois quadros estão quase brancos. `conferencia/varredura-piores.jpg` mostra que não há mulher original.

## Conferência
- `conferencia/folha-1.jpg`, `folha-2.jpg`: original (em cima) × peça em 24 instantes, com cada card e cada flash.
- `conferencia/cards-lado-a-lado.jpg`: fidelidade e legibilidade de cada card.
- `conferencia/flash-painel.jpg`: flashes em volta do painel.
- `conferencia/emendas.jpg`: emendas 404 e 1463.

## Onde o redesenho difere do original
- **HIDDEN DATA:** o original é um print borrado com brilho difuso; o nosso é nítido, com vidro fosco. O anel cinza que vaza na borda direita é aproximado.
- **Ícones pequenos** (lixeira, PHOTOS/VIDEOS/MAPS, lupa, ponto do EXPERT GUIDE) foram redesenhados à mão. A fonte é Arial, não a fonte exata do template, mas o tamanho foi casado pela largura.
- **Flashes:** a curva é a mesma, mas o cômodo novo é mais claro, então os frames vermelhos (n 179–181, 1240–1242) saem menos escuros que no original. Nos frames de flash sobre o painel sobram leves manchas pastel (ganho por célula).
- **Conteúdo do painel nos flashes:** vem do frame limpo mais próximo; o % da barra pode estar 1 passo atrás.
- **n 178:** o original mostra os cards A começando a sair sobre o branco; aqui eles saem 210 px à esquerda, como foi medido, sem as posições intermediárias.
- **Arquivo:** 54 MB (CRF 16, igual à Kendall). O original tem 5 MB; se quiser mais leve, reencode com CRF 20.

## Reproduzir (da pasta da peça)
`python3 work/decodificar.py` (gera `work/G.npy`, ~5 GB, apagado depois de usar) → `python3 flash.py` → `python3 montar.py pecas/variacao.mp4` → `python3 varredura.py` → `python3 conferir.py pecas/variacao.mp4 conferencia/x.jpg n1 n2 …`.

## Histórico
- 25/09, primeira passada: parou antes de gastar (US$ 0), porque a máscara por frame não saía limpa. Havia card translúcido, glow, degradê do painel e flash por cima de tudo (`conferencia/evidencia-bloqueio-mascara.jpg`, `std-cards-*.jpg`, `flash-n174-185.jpg`). A decisão do maestro foi o caminho B (redesenhar).
