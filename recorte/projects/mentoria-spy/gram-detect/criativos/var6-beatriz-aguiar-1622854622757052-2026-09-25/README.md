# Beatriz Aguiar 1622854622757052: variação 6 (25/09/2026)

**Peça:** `pecas/variacao.mp4`: 720×1280, 30 fps, 1380 frames. O áudio foi copiado do original (`-c:a copy`), e o md5 do stream decodificado (`ffmpeg -i x -map 0:a -f md5 -`) é `cd0c5c2ba489d921c9dff259e6b7e0c3`, igual ao do original.
**Molde, camadas redesenhadas e pipeline:** iguais aos da var1. Ver `../var1-beatriz-aguiar-1622854622757052-2026-09-25/README.md`. A pasta é autossuficiente, e o elenco fica em `elenco.json`, lido por `gerar-bases.py` e `gerar-clipes.sh`.

## Elenco e cenários
- **Homem (quem fala):** latino ~22, cabelo cacheado preto no topo com degradê, sem barba, bigode ralo, moletom com capuz caramelo; quarto escuro com parede azul-marinho e varal de luzinhas quentes desfocado.
- **Esquete (mulher sem fala):** latina ~22, cabelo ondulado ruivo-acaju no ombro, moletom preto de zíper e jeans claro wide-leg; corredor amarelo-manteiga com porta branca, maçaneta de latão e jaqueta jeans no gancho. Plano aberto: quarto com edredom azul-marinho.

## Pipeline
`gerar-bases.py homem mulherA` → `gerar-bases.py mulherB` → `gerar-clipes.sh s1 s2 s3 eA eB` (o script valida o download decodificando inteiro e rebaixa pelo `.out.json`) → `checar.py` → `rostos.py s1 s2 s3` (trilha do rosto, mesma convenção YuNet de meia resolução do molde) → `montar.py pecas/variacao.mp4` → `varredura.py` + `conferir.py`.

## Conferência
`conferencia/final-emendas.jpg` (14 frames nas emendas) e `final-instantes.jpg` (11 instantes) mostram o original em cima e a peça embaixo. `iguais.jpg` e `varredura-iguais.json` são a varredura frame a frame. Nenhuma pessoa original aparece, nem desfocada atrás dos painéis. Os pixels iguais são glifos de legenda, título e CTA, mais coincidência de cor em parede clara ou fundo escuro. `frames/clipes.jpg` é a folha de contato dos 5 clipes.

## Custo real (cruzado com `wavespeed billings`, ids em `molde/custo-real.txt`)
US$ 1,0129: 3 imagens (0,211), 3 Pruna (0,45), 2 Seedance (0,352). Nada regerado.

## Concessões
As mesmas da var1: split com rosto ~15% maior, inclinação 648–672 feita por rotação do quadro, ação da esquete gerada por i2v e brilho do título mais suave. O CTA mantém "CLICK THE BELOW" literal.

## Hook original (25/09)
A pedido do Gusta ("manter o hook original que eu mandei"), `pecas/variacao-hook-original.mp4` usa a esquete do anúncio original nos frames 0–308 (corte seco no 308/309); do 309 em diante é a variação. A versão com a esquete gerada (`pecas/variacao.mp4`) fica guardada.
