---
tipo: fonte
tags: [casting, spy-gram, L9, avatar, gram01, medicao, gpt-image-2, pruna]
data: 2026-09-11
---

# fonte — casting de 5 rostos pro lote gram01 L9 var-avatar (11/09/2026)

Fichas de casting V1..V5 (mulheres, prompts literais pro GPT Image 2 no padrão da casa) com o enquadramento do controle **medido** por landmarks e convertido pro 9:16, mais a tabela de evidência dos rostos que já rodaram. Cru em `raw/2026-09-11-casting-gram01-var-avatar-5-rostos.md`; entregável em `projects/mentoria-spy/gram-detect/referencias/2026-09-11-casting-gram01-var-avatar-5-rostos.md`. Peneira.

## Entradas

- Controle `gram01-l9-faixa-2026-09-01` (README, `head/head-panel.mp4`, `head/tail-fullframe.mp4`, posters).
- `escalados/README.md`, `TRANSCRICOES.md`, thumbs (folha de contato conferida) e `referencias/proprios-2026-09-03/00-ranking-comparativo.md` (gasto real) + frames.
- Padrão de prompt: `centerpag-detect/criativos/zap-wpp01-clone-3-ganchos-2026-09-11/base/avatar-wpp01-prompt.txt`; regras anti-cara-de-IA da skill `trocar-avatar`.

## Método

`VNDetectFaceLandmarksRequest` (Vision/macOS, script Swift) em 63 frames do head a 2 fps e 12 da cauda a 10 fps; mediana/p25/p75; conversão pro recorte 704×730 do 9:16 (fator 0,570). Leitura visual de idade/etnia nos frames. Nada pago.

## Achados

- Head do controle: olhos **47,3 %** (p25–p75 43,9–49,1), rosto **47,9 %** da largura, queixo 87 %, ombros cortados nas laterais; cabeça passeia (nariz 35–76 % da largura). Cauda: olhos 44,2 %, mesma escala, 545 px mais baixo.
- Alvo no 9:16: **olhos a 27 % (25–28), queixo no meio, rosto 48 % da largura** — vai literal no prompt.
- Nossa conta: os 4 que gastaram são 25–30 em cômodo íntimo; os 3 L9 fixos morreram independente do rosto; nenhuma mulher negra jovem, latina ou 30–40 tem dado.
- **A #10 da Ad Library é mulher**, não "homem de óculos" (é a #13) — a prova de "rosto não precisa ser quem fala" caiu.

## Páginas geradas / atualizadas

- [[enquadramento-do-head-l9-para-avatar-gerado]] — nova técnica
- [[mapa-de-rostos-spy-gram]] — nova entidade
- [[avatar-segue-o-genero-da-voz]] — nova técnica (com a fonte irmã)
- [[lote-gram01-l9-var-avatar-5-rostos]] — nova entidade (com a fonte irmã)
- Corrigidas: [[roteiro-mestre-com-n-vozes]], [[molde-de-edicao-n-atores]], [[criativo-gram01-1761247818659822]] (a #10)
- Backlinks: [[criativo-gd-ad01]], [[familia-criativos-spy-gram-16-julho]]
