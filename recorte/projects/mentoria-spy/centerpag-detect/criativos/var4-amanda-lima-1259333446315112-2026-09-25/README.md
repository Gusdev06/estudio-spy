# Amanda Lima 1259333446315112: variação 4 · 2026-09-25 · PRONTA

Mesmo molde da var1 (cards, flashes, painel WhatsApp, mapa, ordem das camadas e emendas redesenhados; nada da mulher original fora dos miolos opacos). Método completo e medidas: `../var1-amanda-lima-1259333446315112-2026-09-25/README.md`. Pipeline copiado da var2 (com o ajuste de intensidade do flash no `montar.py`).

**Peça:** `pecas/variacao.mp4`. H.264 720×1280, 30 fps, **1822 frames**, áudio AAC **copiado**; md5 do stream (`ffmpeg -i x -map 0:a -f md5 -`) = original `29e25399e94aef0e26a02c23b9d2cca5`. 20 MB (CRF 16).
**Avatar:** mulher leste-asiática de uns 25 anos, cabelo preto liso em chanel na altura do queixo com franja reta, brincos pequenos de prata, camisa social azul-marinho.
**Cenário:** canto de home office à tarde, brilho médio: estante de carvalho claro com livros e vasos de cerâmica, mural de cortiça com papéis em branco, jiboia pendente, parede cinza quente e luminária preta de mesa. (`base/casting.txt`, `base/v4.png`)
**Custo real: US$ 1,6415** (`work/billings.json`, ids em `work/ids.txt`): gpt-image-2/edit medium 1k 0,0665 + Pruna p-video/avatar 720p seed 7: 0,35 + 0,55 + 0,35 + 0,325. Nenhum reroll.

## Triagem (`checar.py`)
4/4 clipes decodificam inteiros (14,0 / 22,0 / 14,0 / 13,0 s, 704×1280), sem 2º rosto, sem gente entrando, sem troca de pessoa (folhas `clipes/c*-sheet.jpg`, 1 quadro/s, conferidas a olho). Alertas de "borda muda" = mãos gesticulando na borda de baixo/lateral, como na var1/var2.

## Varredura final (`varredura.py`; fração de pixels |dif|<10 fora dos cards e miolos permitidos)
Fora do flash (`work/varredura-fora-flash.py`): quadro 2,5% em média, máx 5,5% (n1215). Com flash: rosto até 25,4% (n179), quadro até 96,8% (n1238) (pico branco/tinta chapada). `conferencia/varredura-piores.jpg` (flashes) e `varredura-piores-fora-flash.jpg` mostram que não há mulher original.

## Conferência
`conferencia/folha-1.jpg`, `folha-2.jpg` (original em cima × peça, 24 instantes), `emendas.jpg` (n 402–405, 1059–1061, 1462–1464), `varredura-piores*.jpg`.

## Concessões
- As mesmas da var1/var2 (HIDDEN DATA nítido, ícones à mão, Arial, % da barra no flash).

## Reproduzir (da pasta)
`python3 work/decodificar.py` (G.npy ~5 GB; apagar depois) → `python3 montar.py pecas/variacao.mp4` → `python3 varredura.py` → `python3 conferir.py pecas/variacao.mp4 conferencia/x.jpg n1 n2 …`. Clipes: de `projects/mentoria-spy/`, `SEED=7 bash centerpag-detect/criativos/var4-amanda-lima-1259333446315112-2026-09-25/gerar-clipes.sh c1 c2 c3 c4`.
