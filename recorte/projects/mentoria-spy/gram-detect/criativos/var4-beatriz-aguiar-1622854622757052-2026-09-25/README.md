# Beatriz Aguiar 1622854622757052: variação 4 (25/09/2026)

**Peça:** `pecas/variacao.mp4`: 720×1280, 30 fps, 1380 frames. O áudio foi copiado do original (`-c:a copy`), e o md5 do stream decodificado (`ffmpeg -i x -map 0:a -f md5 -`) é `cd0c5c2ba489d921c9dff259e6b7e0c3`, igual ao do original.
**Molde, camadas redesenhadas e pipeline:** iguais aos da var1. Ver `../var1-beatriz-aguiar-1622854622757052-2026-09-25/README.md`. A pasta é autossuficiente, e o elenco fica em `elenco.json`, lido por `gerar-bases.py` e `gerar-clipes.sh`.

## Elenco e cenários
- **Homem (quem fala):** negro ~23, twists curtos com degradê, bigode fino, moletom com capuz bordô; cama num quarto escuro, parede carvão e LED azul no alto da parede.
- **Esquete (mulher sem fala):** negra ~24, black power curto arredondado, argolas douradas, camiseta mostarda oversized e jogger preta; corredor de parede cinza efeito concreto, porta preta e espada-de-são-jorge. Plano aberto: quarto com edredom terracota.

## Pipeline
`gerar-bases.py homem mulherA` → `gerar-bases.py mulherB` → `gerar-clipes.sh s1 s2 s3 eA eB` (o script valida o download decodificando inteiro e rebaixa pelo `.out.json`) → `checar.py` → `rostos.py s1 s2 s3` (trilha do rosto, mesma convenção YuNet de meia resolução do molde) → `montar.py pecas/variacao.mp4` → `varredura.py` + `conferir.py`.

## Conferência
`conferencia/final-emendas.jpg` (14 frames nas emendas) e `final-instantes.jpg` (11 instantes) mostram o original em cima e a peça embaixo. `iguais.jpg` e `varredura-iguais.json` são a varredura frame a frame. Nenhuma pessoa original aparece, nem desfocada atrás dos painéis. Os pixels iguais são glifos de legenda, título e CTA, mais coincidência de cor em parede clara ou fundo escuro. `frames/clipes.jpg` é a folha de contato dos 5 clipes.

## Custo real (cruzado com `wavespeed billings`, ids em `molde/custo-real.txt`)
US$ 1,1879: 3 imagens (0,211), 4 Pruna (0,625; o s3 seed 7 foi descartado porque aparecia uma MÃO na lente em 2,8 s e 4,3–4,7 s, visível na peça em n≈1269–1272 e 1318; a peça usa o s3 seed 8) e 2 Seedance (0,352).

## Concessões
As mesmas da var1: split com rosto ~15% maior, inclinação 648–672 feita por rotação do quadro, ação da esquete gerada por i2v e brilho do título mais suave. O CTA mantém "CLICK THE BELOW" literal.
- O download do s3 seed 8 veio truncado sem erro. O script detectou e rebaixou pela URL do .out.json, e depois o arquivo decodificou inteiro.

## Hook original (25/09)
A pedido do Gusta ("manter o hook original que eu mandei"), `pecas/variacao-hook-original.mp4` usa a esquete do anúncio original nos frames 0–308 (corte seco no 308/309); do 309 em diante é a variação. A versão com a esquete gerada (`pecas/variacao.mp4`) fica guardada.
