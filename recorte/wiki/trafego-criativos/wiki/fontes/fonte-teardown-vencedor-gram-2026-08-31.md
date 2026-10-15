---
tipo: fonte
tags: [teardown, swipe, spy-gram, split-screen, vencedor]
data: 2026-08-31
---

# fonte — teardown do vencedor do swipe GRAM (31/08/2026)

Teardown da peça #1 do swipe de Instagram (`ad_id 1761247818659822`, página Sophia Jones), feito frame a frame e com a locução transcrita localmente.

## Entradas

- `gram-detect/escalados/instagram/01-sophia-jones-1761247818659822.mp4` — 32,5s, 360×640.
  **É o arquivo canônico da peça** (md5 `9e300448c20fd4d138ba074a2e35caa1`); poster em `…-thumb.jpg`.
  A cópia em `top3-ig-e-whatsapp/ig-01-…` é byte a byte a mesma — exibir a de `instagram/`.
- `gram-detect/escalados/instagram/01-…​.txt` + `gram-detect/manifest.json` — copy conferida campo a campo nos dois; batem.
- Peças #3, #6 e #10 da mesma página, usadas como controle.
- Cru em `raw/2026-09-01-teardown-vencedor-gram-sophia-jones.md`.

## Método (pra poder repetir)

- Frames: `ffmpeg fps=1` + folhas de contato, e crops 4× do painel do app pra ler a UI.
- Cortes: detecção de cena (`select='gt(scene,0.10)'` sobre o crop do painel) — medidos, não estimados.
- Medidas de layout: perfil de luminância por linha/coluna sobre o frame de 10s.
- Locução: `mlx-whisper` (`whisper-small.en`) **local**, áudio mono 16 kHz. Nada saiu da máquina.
- Altura de voz: F0 por autocorrelação nos trechos vozeados — estimativa de altura, não identificação de locutor.

## Achados

- O painel esquerdo da peça é o [[template-funil-gravado-9-modulos]] inteiro. O vencedor usa **o mesmo ativo** que a [[familia-criativos-gram-funil-gravado]] já tem gravado — só que como painel de apoio, não como o anúncio.
- Layout novo pro catálogo: 3 blocos com o terço inferior dividido na vertical ([[funil-gravado-como-painel-lateral]]).
- As 4 peças de vídeo da página rodam **o mesmo roteiro palavra por palavra**; a #10 tem voz feminina sobre rosto masculino ([[roteiro-mestre-com-n-vozes]]).
- A faixa de hook é a única variável real entre as 4 — o eixo que o wiki registra como parado na nossa família.
- A locução nunca diz espionar, hackear, DM, senha, nem o nome do produto ([[promessa-pesada-so-na-imagem]]).

⚠️ **Nenhuma métrica de performance verificada.** O ranking é proxy de Ad Library (ausência da flag de baixo volume + ordem de `total_impressions desc` + dias no ar + repetição do ângulo). Não há gasto, CTR, CPA ou ROAS desta peça em lugar nenhum.

## Contradição registrada

O contador da peça **cai** ao longo do vídeo (393 online → 377 analyzing → 304 analyzing), contra a regra de [[contador-que-sobe-como-prova-de-trabalho]]. É defeito do vencedor, não traço a copiar.

## Páginas geradas

- [[criativo-gram01-1761247818659822]]
- [[funil-gravado-como-painel-lateral]]
- [[dor-e-mecanismo-em-paralelo]]
- [[promessa-pesada-so-na-imagem]]
- [[roteiro-mestre-com-n-vozes]]
- [[faixa-de-hook-fixa-sem-legenda]]
