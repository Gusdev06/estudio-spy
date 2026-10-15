# Fonte crua — remedição da matte do topo do wpp-01 (Bisturi, 11/09/2026)

Trecho copiado sem edição da seção "Medição do original — fronteiras e matte (11/09)" de
`projects/mentoria-spy/centerpag-detect/criativos/zap-wpp01-clone-3-ganchos-2026-09-11/README.md`.
Evidência visual: `conferencia/original-zoom-matte.jpg` do mesmo lote (zoom ×8, luma ×6, t = 2 / 12 / 25 s,
linhas verde y 90 · ciano y 93 · vermelha y 96). Peça: ad `1762552938111855`, 360×640.

---

**Matte do topo** — 58 frames (1–30 s, 2 fps), luminância em numpy, colunas de margem x 0–30 e 330–360 (fora do texto):

| medida | valor | teardown (01/09) |
|---|---|---|
| fração de pixels com luma < 20, frame médio: 100 % até | **y = 93** | y = 96 ("100 % preta até y96") |
| idem, frames isolados com luma < 16 (t 0,5 / 8,8 s) | y = 87 / 89 | — |
| 5 colunas (x 5 / 15 / 180 / 345 / 355), última linha < 20 | 93 / 94 / 103 / 103 / 101 | — |
| matte pura (y 0–20): luma média · std temporal | 0,0 · 0,03 | — |
| **std temporal em y 85–95** (margens) | **1,7 → 2,5** | — |
| std temporal: 10 % / 50 % / 90 % do platô (17,0 em y 130–200) | y 67 / **125** / **141** | — |
| penhasco (argmax do diff) na variância e na luminância, janela y 80–125 | **não existe** — margens 1,01–1,19×; o argmax cai em y 113–125 conforme a coluna | — |

**Leitura:** a borda "100 % preta" fica em **y 93 (±3, depende do limiar)** — o 96 do teardown está dentro da mesma faixa (`README-l10.md` já anotava 91–97); **não é divergência que mude o molde (288 em 1080p = y 96 ×3).** O achado novo é outro: **a matte não é degrau, é fade.** Abaixo do texto o vídeo já aparece atenuado a partir de ~y 80 (std temporal 50–80× a da matte pura em y 85–95; no zoom ×8 com luma ×6, `original-zoom-matte.jpg`, a silhueta do microfone/abajur atravessa as linhas de y 90–96 até quase o texto) e só chega a 90 % do movimento pleno em **y ≈ 141**. Nosso molde corta seco em 288. Fica registrado pro Maestro/Peneira; **não apliquei** (o molde duro já rodou nas peças EX A/B/C e este lote varia uma alavanca só). Se quiserem aproximar na fase B: trocar o `pad … :black` do `[actor]` por um gradiente preto de y 240 → 420 (1080p) — uma linha no `remontar-l10.py`, custo zero.
