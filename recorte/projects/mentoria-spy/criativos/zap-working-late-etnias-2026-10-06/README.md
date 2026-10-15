# Zap "working late": 5 variações de avatar/etnia (2026-10-06)

- **Referência:** `REFERENCIA-original.mp4` = `~/Downloads/AdLibNote_Canal7_4414694105508752_adstart-2026-10-02_creative-01_video.mp4` (Ad Library, Canal7, ad 4414694105508752, ativo desde 02/10). 720x960, 30,4 s, EN. Layout: faixas vermelhas em cima/embaixo, talking head (rapaz negro) em cima à esquerda, CCTV embaixo à esquerda, tela do app ZAP à direita, karaokê.
- **Alavanca única:** só a pessoa na caixa da cabeça (medida: x 0–336, y 119–443, fixa o vídeo todo). Quarto, camiseta preta, pose, CCTV, tela do app, faixas, karaokê e áudio ficam iguais ao original. O md5 do áudio decodificado das 5 peças é igual ao do original (`6d7e5e5f…`).
- Jev não rodou: a copy é idêntica, e a rubrica não distingue troca de avatar.

| Peça | Avatar |
|---|---|
| `pecas/zap-working-late-v1-branco.mp4` | branco americano, cabelo castanho-claro bagunçado |
| `pecas/zap-working-late-v2-latino.mp4` | latino (mexicano-americano), degradê, bigode ralo |
| `pecas/zap-working-late-v3-asiatico.mp4` | asiático (coreano-americano), franja lisa |
| `pecas/zap-working-late-v4-indiano.mp4` | indiano-americano, cabelo ondulado, barba curta |
| `pecas/zap-working-late-v5-arabe.mp4` | árabe-americano, cacheado curto, barba cheia |

Todas as peças: 720x960, 30 fps, 913 frames, 30,43 s.

## Pipeline
`gerar-bases.py <v…>` (gpt-image-2/edit, medium, 1k, 1:1, sobre o frame de 5 s da caixa; elenco em `elenco.json`) → `gerar-clipes.sh <v…>` (Pruna p-video/avatar, 720p, seed 7, áudio original inteiro; saída 960x960, 24 fps, 31,04 s; valida decodificando inteiro) → `montar.sh <v…>` (fps=30, scale 336x325, trim 30,419, overlay em 0:119, áudio copiado).
Conferência: `conferencia/bases.jpg` (original + 5 rostos), `conferencia/clipes.jpg` (10 instantes por clipe: mesma pessoa o tempo todo, sem segunda pessoa e sem moldura no fim), `conferencia/peca-v3-12s.png`.

## Custo real (`wavespeed billings`, key:macbook; ids em `prediction-ids.txt`)
US$ 4,2075: 5 imagens (5 × 0,0665 = 0,3325) e 5 Pruna (5 × 0,775 = 3,875). Nada regerado. A primeira leva da Pruna foi recusada na validação (URL do áudio vazia) e não foi cobrada.
Às 01:10–01:12 UTC aparecem outras cobranças na mesma chave (1 gpt-image-2/edit e 3 Pruna somando US$ 0,475). Os ids delas não são deste lote; devem ser de outra sessão.
