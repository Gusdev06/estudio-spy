# Beatriz Aguiar 1622854622757052: variação 5 (25/09/2026)

**Peça:** `pecas/variacao.mp4`: 720×1280, 30 fps, 1380 frames. O áudio foi copiado do original (`-c:a copy`), e o md5 do stream decodificado (`ffmpeg -i x -map 0:a -f md5 -`) é `cd0c5c2ba489d921c9dff259e6b7e0c3`, igual ao do original.
**Molde, camadas redesenhadas e pipeline:** iguais aos da var1. Ver `../var1-beatriz-aguiar-1622854622757052-2026-09-25/README.md`. A pasta é autossuficiente, e o elenco fica em `elenco.json`, lido por `gerar-bases.py` e `gerar-clipes.sh`.

## Elenco e cenários
- **Homem (quem fala):** ~26, pele oliva clara, cabelo loiro-escuro ondulado na altura do queixo atrás das orelhas, barba rala loira, camiseta branca e sobrecamisa jeans escura aberta; mesa de jantar numa cozinha à noite, com pendente quente e armários brancos.
- **Esquete (mulher sem fala):** sul-asiática ~27, trança lateral longa preta, moletom lavanda oversized e calça bege; corredor branco com ripado de carvalho claro e porta de carvalho. Plano aberto: quarto com edredom verde-sálvia.

## Pipeline
`gerar-bases.py homem mulherA` → `gerar-bases.py mulherB` → `gerar-clipes.sh s1 s2 s3 eA eB` (o script valida o download decodificando inteiro e rebaixa pelo `.out.json`) → `checar.py` → `rostos.py s1 s2 s3` (trilha do rosto, mesma convenção YuNet de meia resolução do molde) → `montar.py pecas/variacao.mp4` → `varredura.py` + `conferir.py`.

## Conferência
`conferencia/final-emendas.jpg` (14 frames nas emendas) e `final-instantes.jpg` (11 instantes) mostram o original em cima e a peça embaixo. `iguais.jpg` e `varredura-iguais.json` são a varredura frame a frame. Nenhuma pessoa original aparece, nem desfocada atrás dos painéis. Os pixels iguais são glifos de legenda, título e CTA, mais coincidência de cor em parede clara ou fundo escuro. `frames/clipes.jpg` é a folha de contato dos 5 clipes.

## Custo real (cruzado com `wavespeed billings`, ids em `molde/custo-real.txt`)
US$ 1,0794: 4 imagens (0,277; o 1º homem foi descartado por ser do Oriente Médio, de barba cheia preta, parecido demais com o original), 3 Pruna (0,45) e 2 Seedance (0,352).

## Concessões
As mesmas da var1: split com rosto ~15% maior, inclinação 648–672 feita por rotação do quadro, ação da esquete gerada por i2v e brilho do título mais suave. O CTA mantém "CLICK THE BELOW" literal.
- Paredes brancas: a varredura marca muito pixel "igual" na esquete (pico em n45), mas é coincidência de cor com a parede branca do original. Conferi em `iguais.jpg`: nenhum pedaço da mulher original.

## Hook original (25/09)
A pedido do Gusta ("manter o hook original que eu mandei"), `pecas/variacao-hook-original.mp4` usa a esquete do anúncio original nos frames 0–308 (corte seco no 308/309); do 309 em diante é a variação. A versão com a esquete gerada (`pecas/variacao.mp4`) fica guardada.
