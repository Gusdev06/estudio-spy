# Amanda Lima 1259333446315112: variação 3 · 2026-09-25 · PRONTA

Mesmo molde da var1 (cards, flashes, painel WhatsApp, mapa, ordem das camadas e emendas redesenhados, nada da mulher original fora dos miolos opacos). Método completo e medidas: `../var1-amanda-lima-1259333446315112-2026-09-25/README.md`.

**Peça:** `pecas/variacao.mp4`. H.264 720×1280, 30 fps, **1822 frames**, áudio AAC **copiado**; md5 do stream (`ffmpeg -i x -map 0:a -f md5 -`) = original `29e25399e94aef0e26a02c23b9d2cca5`. 53 MB (CRF 16).
**Avatar:** mulher de uns 23 anos, pele morena média, cabelo castanho-escuro cacheado preso em coque alto com cachos soltos no rosto, argolas douradas pequenas, suéter mostarda.
**Cenário:** cozinha moderna clara de dia: armários brancos lisos, bancada de mármore claro, prateleiras de madeira com potes e plantas, pendentes pretos e janela grande. (`base/casting.txt`, `base/v3.png`)
**Custo real: US$ 1,6415** (`work/billings.json`, ids em `work/ids.txt`): imagem gpt-image-2/edit medium 1k 0,0665 + Pruna p-video/avatar 720p seed 7: 0,35 + 0,55 + 0,35 + 0,325. Nenhum reroll.

## O que muda em relação à var1
- `base/v3.req.json`: mesmo prompt da var1 sobre o mesmo frame limpo (n 212), só com pessoa/cômodo trocados.
- `montar.py`: antes de cada frame de flash, o quadro novo é levado ao brilho médio do frame limpo do original usado como proxy (k por canal, limitado a 0,6–1,4, com peso que some quando o ganho do flash volta a ~1). `flash-params.json` é o mesmo da var1.
- `gerar-clipes.sh` e `checar.py` com caminhos desta pasta.

## Triagem (`checar.py`)
4/4 clipes decodificam inteiros (14,0 / 22,0 / 14,0 / 13,0 s, 704×1280 24 fps), sem 2º rosto, sem gente entrando, sem troca de pessoa (conferido nas folhas `clipes/c*-sheet.jpg`). Alertas aceitos, como na var1: variação do rosto ×0,76 quando ela olha pra baixo/vira; "borda muda" = mãos no peito na borda de baixo.

## Varredura final (`varredura.py`, fração de pixels |dif|<10 fora dos cards e miolos permitidos)
fora do flash: quadro 0,78% em média (máx 3,75% n1209), caixa do rosto original 1,41% (máx 3,8% n1066). Com flash: rosto até 19,5% (n177), quadro até 96,9% (n1239, pico branco). Nos frames de flash os quadros ficam quase chapados de tinta; `conferencia/varredura-piores.jpg` mostra que não há mulher original.

## Conferência
`conferencia/folha-1.jpg`, `folha-2.jpg` (original em cima × peça, 24 instantes), `emendas.jpg` (n 402–405, 1059–1061, 1462–1464), `varredura-piores.jpg`.

## Concessões
- Flash: cozinha bem mais clara que o quarto original: o ajuste de intensidade (limitado a ×0,6) escurece, mas os vermelhos (n 179–181, 1240–1242) seguem mais claros/rosados que no original e o n1058 puxa pra rosa.
- Demais diferenças do redesenho (HIDDEN DATA nítido, ícones à mão, Arial, % da barra no flash) iguais às da var1.

## Reproduzir (da pasta)
`python3 work/decodificar.py` (G.npy ~5 GB; apagar depois) → `python3 montar.py pecas/variacao.mp4` → `python3 varredura.py` → `python3 conferir.py pecas/variacao.mp4 conferencia/x.jpg n1 n2 …`. Clipes: de `projects/mentoria-spy/`, `SEED=7 bash centerpag-detect/criativos/var3-amanda-lima-1259333446315112-2026-09-25/gerar-clipes.sh c1 c2 c3 c4`.
