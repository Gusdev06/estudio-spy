# Kendall 1987478995288058 — 5 variações com avatar e cenário novos · 2026-09-25 → peças 137–141

Pedido do Gusta: "faça 5 variações desse mudando avatar e cenário".
**Original:** `~/Downloads/Kendall Godfrey Stephanie_1987478995288058_2026-09-25.mp4` (md5 `eab217de…`), 720×1254, 30 fps, 20,2 s → `REFERENCIA-original.mp4`. Mulher sentada na cama falando pra câmera, faixa amarela "FIND OUT IF YOUR PARTNER IS BEING UNFAITHFUL", funil do Zap. A TV do fundo mostrava o logo do "Good Morning America" (imitação de imprensa): o cenário novo tira isso.

## Molde medido
| trecho | o que é | origem na peça |
|---|---|---|
| 0–2,67 | ela em tela cheia + faixa (y 549–704) | clipe c1, rosto em (357,292) com h 214 |
| 2,67–7,83 | ela só em y 0–549 (outro zoom) + faixa + funil digitando embaixo | clipe c1, rosto em (360,180) h 172 · funil e faixa do original |
| 7,83–15,07 | painéis em tela cheia | original |
| 15,07–16,0 | ela em tela cheia, plano aberto, sem faixa | clipe c2, rosto em (356,353) h 180 |
| 16,0–20,2 | CTA "CLICK THE LINK BELOW" | original |

## Pipeline (de `projects/mentoria-spy/`)
1. `gerar-bases.py`: gpt-image-2/edit sobre o plano aberto (t=15,5 s), trocando pessoa **e** cômodo, com a mesma pose e o mesmo enquadramento (`casting.tsv`).
2. `gerar-clipes.sh kN` (SEED=7, prompt só em positivo): c1 = áudio 0–7,83; c2 = áudio **14,07–16,0**. Com 0,93 s a Pruna falhou nas 5 ("service unavailable", estornado), então a montagem usa o c2 a partir de 1,0 s.
3. `checar.py kN`: borda, laterais, 2º rosto, rosto sumindo, variação de tamanho. 10/10 OK.
4. `montar.py kN pecas/kN.mp4`: escala = h do rosto alvo / h no clipe (mín. o que cobre o quadro) e posiciona o rosto no ponto medido. No trecho B a escala mínima deixa o rosto ~5% maior que no original.

| peça | variação |
|---|---|
| 137 | k1: negra de cachos, sala clara com sofá cinza |
| 138 | k2: loira, quarto quente com abajur |
| 139 | k3: latina de rabo de cavalo, cozinha branca |
| 140 | k4: asiática de bob, escritório em casa com estante |
| 141 | k5: ruiva, varanda com luzinhas e a cidade ao fundo |

Áudio md5-idêntico ao original nas 5. Conferência: `casting.jpg`, `conferencia/final-5.jpg`, `conferencia/momentos.jpg`.

## Custo real: US$ 1,58
5 imagens 0,33 + 10 clipes Pruna 1,25 (5 c1 × 0,20 + 5 c2 × 0,05; as 5 chamadas curtas que falharam foram estornadas).

## Correção 25/09: "ainda mostra resquícios do vídeo original, piscando o avatar anterior" (Gusta)
Varri frame a frame onde a mulher original continuava visível. Eram dois problemas:
1. **Emendas por segundo arredondado:** sobravam 7 frames da original (n 80 no buraco entre A e B; n 235–239, porque ela fica até 8,00 s e não até o corte de 7,83; n 452 antes do C). Agora as emendas são por **número de frame**: A 0–79, B 80–239, C 452–479.
2. **Fundo dos painéis (n 240–451):** em volta do celular (x 51–668, y 78–1175) o original mostra a própria mulher desfocada (plano aberto, gaussiano σ≈12, ganho 1,0, ajustado contra o n 452). Agora esse fundo é a avatar nova no plano aberto com o mesmo desfoque, e o celular do original vai por cima via `molde/mascara-celular.png`.
Conferência: `conferencia/emendas-corrigidas.jpg`, `conferencia/k4-iguais.jpg` (o que sobra igual à original é só faixa/funil/celular + coincidência de cor). 602 frames, áudio md5 = original. Custo da correção: US$ 0.
