---
tipo: fonte
tags: [medicao, edicao, spy-zap, centerpag, wpp-01, l10, matte, fade, bisturi]
data: 2026-09-11
---

# fonte — remedição da matte do wpp-01: fade, não degrau (Bisturi, 11/09/2026)

Remedição da matte do topo do [[criativo-wpp01-1762552938111855]] feita pelo Bisturi na fase A do lote `zap-wpp01-clone-3-ganchos-2026-09-11`: a fronteira "100 % preta" bate com o teardown de 01/09 (y 93 vs 96, mesma faixa), mas **não há penhasco** — a matte termina num fade de ~50 px. Cru em `raw/2026-09-11-medicao-matte-fade-wpp01-bisturi.md`; origem em `projects/mentoria-spy/centerpag-detect/criativos/zap-wpp01-clone-3-ganchos-2026-09-11/README.md` (seção "Medição do original") + `conferencia/original-zoom-matte.jpg`.

## Método

58 frames (1–30 s, 2 fps), luminância em numpy, colunas de margem `x 0–30` e `330–360` (fora do texto do hook), 360×640. Três estatísticos: fração de pixels quase-pretos por linha, desvio-padrão temporal por linha, argmax do diff (penhasco) em y 80–125.

## Achados

- **Início da matte confirmado:** 100 % preta até **y 93** (luma < 20, frame médio); 87/89 em frames isolados com luma < 16; 93/94/103/103/101 em 5 colunas. O `y 96` do teardown ([[fonte-teardown-edicao-wpp01-2026-09-01]]) e o `91–97` do `README-l10` do lote EX são a mesma faixa — muda o limiar, não a medida.
- **Não é degrau:** std temporal 0,03 na matte pura vs **1,7–2,5 em y 85–95** (50–80×); o vídeo já atravessa ali. 10/50/90 % do platô de variância (17,0 em y 130–200) em **y 67 / 125 / 141**.
- **Não existe penhasco:** margens 1,01–1,19×, argmax em y 113–125 conforme a coluna. No zoom ×8 a silhueta do microfone/abajur cruza as linhas y 90/93/96 até quase o texto.
- **Molde não muda neste lote** — uma alavanca por lote ([[variar-uma-alavanca-por-vez]]); o corte seco em `y 288` (1080p) já rodou nas EX A/B/C. Fade = opção de lote futuro (gradiente preto y 240 → 420, uma linha no `remontar-l10.py`, custo zero).

## Páginas geradas / atualizadas

- [[matte-em-fade-nao-tem-penhasco]] — técnica nova: fração de preto dá o início, platô dá o fim; fade ≠ degrau.
- [[medir-fronteira-de-bloco-em-video]] — a pré-condição "a fronteira existe?" ganha um terceiro caso.
- [[criativo-wpp01-1762552938111855]] — linha da matte anotada.
- Teardown de 01/09 recebeu nota datada (correção fluindo pra trás, sem apagar o valor velho).
