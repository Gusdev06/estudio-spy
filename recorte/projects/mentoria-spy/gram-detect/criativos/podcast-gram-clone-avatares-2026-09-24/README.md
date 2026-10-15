# Podcast Instagram (Gram) — clone com 5 pares de avatares · 2026-09-24 → peças 132–136

Pedido do Gusta: "agora faça desse" (depois das 127–131) → mais elencos, agora sobre um criativo da Ad Library pro Gram.
**Original:** `~/Downloads/AQPsn8yj…mp4` (md5 `3bdc9d41…`), 720×1280, 30 fps, 52,1 s → `REFERENCIA-original.mp4`. É o mesmo formato do podcast WPP (lote 40), só que pro Instagram e com o Gram Detect nos painéis.

## Molde medido
| camada | medida |
|---|---|
| Título | caixa branca y 101–245: "HOW TO ACCESS YOUR PARTNER'S INSTAGRAM FROM YOUR PHONE" (some no CTA) |
| Janela de vídeo | 720×812 em y 250 (a borda de baixo vai até ~1062; na B o vídeo encosta em 1078, mas fica escuro) |
| Legenda | frases em minúsculo, branco, sobre preto, y 1063–1135: **fora da janela, preservada do original** |
| Estrutura | host A 0–5,53 · convidada B 5,53–13,40 · A 13,40–18,27 · painéis Gram Detect 18,27–37,47 · A 37,47–44,10 · CTA b-roll em quadro cheio 44,10–52,1 |
| Detalhe | 7,07–8,45: a host fala ("you don't need to touch their phone") com a câmera na convidada. No áudio do clipe B esse trecho vai **mudo**, pra a convidada ouvir de boca fechada |

## Pipeline (de `projects/mentoria-spy/`)
1. `gerar-bases.py`: gpt-image-2/edit sobre o frame da janela (A t=0,034 · B t=8,0), mesma roupa, fone, poltrona e cenário. Só a pessoa muda.
2. `gerar-clipes.sh gN` (`SEED=7`, prompt só em positivo): 4 clipes Pruna com o áudio original de cada bloco. Saem em 896×1024, 24 fps.
3. `checar.py gN`: borda clara (moldura), faixa lateral mexendo (gente entrando) e 2º rosto com score ≥ 0,86.
4. `montar.py gN pecas/gN.mp4`: clipe → 720×823 → corta 812 → overlay na janela; o resto é o original. Áudio copiado: md5 idêntico ao original.

## O que deu errado e como ficou
- **1ª leva do g1 (seed 21, prompt citando "nobody enters from any edge"):** a Pruna (a) encolheu o quadro numa "foto sobre papel" no fim do a1, (b) pôs moldura verde no fim do a2 e (c) fez gente entrar pela direita no b. Regerados com prompt só em positivo ("one continuous full-frame shot… the room stays still and empty") e seed 7. Os 3 limpos, e os 16 de g2–g5 passaram de primeira. Descartes em `g1/descartados/`.
- **Falso positivo do checador:** o vaso da estante dá rosto com score 0,80. O limiar da contagem ficou em 0,86.
- 2 imagens vieram truncadas no download: rebaixadas da URL do `.json`, sem pagar de novo.

Conferência: `casting.jpg` (1ª coluna = original), `conferencia/final-5.jpg` (original + 5 peças em 10 instantes), `conferencia/emenda-inferior.jpg`, `conferencia/g1-clipes*.jpg`.

## Custo real: US$ 4,46
11 imagens 0,73 (uma cobrada apesar do "fetch failed") + 23 clipes Pruna 3,73 (20 finais + 3 descartados, ≈ 0,50). Outro elenco agora ≈ US$ 0,80.
