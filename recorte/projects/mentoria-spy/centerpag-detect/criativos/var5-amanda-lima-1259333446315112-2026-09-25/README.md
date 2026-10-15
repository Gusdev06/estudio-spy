# Amanda Lima 1259333446315112: variação 5 · 2026-09-25 · PRONTA

Mesmo molde da var1 (cards, flashes, painel WhatsApp, mapa, ordem das camadas e emendas redesenhados; nada da mulher original fora dos miolos opacos). Método completo e medidas: `../var1-amanda-lima-1259333446315112-2026-09-25/README.md`. Pipeline copiado da var2 (com o ajuste de intensidade do flash no `montar.py`).

**Peça:** `pecas/variacao.mp4`. H.264 720×1280, 30 fps, **1822 frames**, áudio AAC **copiado**; md5 do stream (`ffmpeg -i x -map 0:a -f md5 -`) = original `29e25399e94aef0e26a02c23b9d2cca5`. 39 MB (CRF 16).
**Avatar:** mulher negra de uns 23 anos, box braids pretas longas até a cintura jogadas sobre um ombro, argolas douradas pequenas, blusa canelada vinho.
**Cenário:** sala cheia de plantas, luz natural lateral de brilho médio: parede verde-sálvia, costela-de-adão, plantas pendentes em suportes de macramê, poltrona de couro caramelo e mesinha de madeira. (`base/casting.txt`, `base/v5.png`)
**Custo real: US$ 1,6415** (`work/billings.json`, ids em `work/ids.txt`): gpt-image-2/edit medium 1k 0,0665 + Pruna p-video/avatar 720p seed 7: 0,35 + 0,55 + 0,35 + 0,325. Nenhum reroll.

## Triagem (`checar.py`)
4/4 clipes decodificam inteiros (14,0 / 22,0 / 14,0 / 13,0 s, 704×1280), sem 2º rosto, sem gente entrando, sem troca de pessoa (folhas `clipes/c*-sheet.jpg`, 1 quadro/s, conferidas a olho). Alertas de "borda muda" = mãos gesticulando na borda de baixo/lateral, como na var1/var2.

## Varredura final (`varredura.py`; fração de pixels |dif|<10 fora dos cards e miolos permitidos)
Fora do flash (`work/varredura-fora-flash.py`): quadro 3,3% em média, máx 6,9% (n184). Com flash: rosto até 29,5% (n1062), quadro até 94,4% (n1061) (pico branco/tinta chapada). `conferencia/varredura-piores.jpg` (flashes) e `varredura-piores-fora-flash.jpg` mostram que não há mulher original.

## Conferência
`conferencia/folha-1.jpg`, `folha-2.jpg` (original em cima × peça, 24 instantes), `emendas.jpg` (n 402–405, 1059–1061, 1462–1464), `varredura-piores*.jpg`.

## Concessões
- As mesmas da var1/var2 (HIDDEN DATA nítido, ícones à mão, Arial, % da barra no flash).

## Reproduzir (da pasta)
`python3 work/decodificar.py` (G.npy ~5 GB; apagar depois) → `python3 montar.py pecas/variacao.mp4` → `python3 varredura.py` → `python3 conferir.py pecas/variacao.mp4 conferencia/x.jpg n1 n2 …`. Clipes: de `projects/mentoria-spy/`, `SEED=7 bash centerpag-detect/criativos/var5-amanda-lima-1259333446315112-2026-09-25/gerar-clipes.sh c1 c2 c3 c4`.
