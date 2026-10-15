# 30 variações de avatar/roupa/etnia (19–20/09) — peças 71–100

Pedido: "10 variações de cada trocando apenas avatar/roupas/etnias" de três peças prontas: **22** (Secret Revealed, homem em quadro cheio), **64** (Luiza split com look Android, mulher) e **40** (podcast WPP clone, duas mulheres).

| família | peças | molde reaproveitado | por variação |
|---|---|---|---|
| Secret (`secret/`) | 71–80 | `zap-secret-revealed-avatar-2026-09-10/remontar-secret.sh` (faixa vermelha + karaokê do original) | 1 imagem text-to-image + 1 Pruna 33 s |
| Luiza (`luiza/`) | 81–90 | `luiza-troca-avatar-android-2026-09-19/montar.py` (esquerda = avatar, direita = funil, look Android calibrado) | 1 gpt-image-2/edit sobre o frame + 1 Pruna 29 s |
| Podcast (`podcast/` → dados em `../podcast-wpp-clone-avatares-2026-09-13/p01..p10/`) | 91–100 | `gerar-variacao.sh` + `montar-clone.py` (2 closes + two-shot, 5 clipes) | 3 imagens + 5 Pruna curtos |

Elencos em `<família>/casting.tsv` (id · slug · descrição) — 10 etnias/roupas/cabelos distintos por família, gênero = gênero da voz. Casting conferido em folha antes do lipsync (`<família>/conferencia/casting.jpg`); clipes varridos inteiros (`varredura-*.jpg`). Montagem: `montar-tudo.py <família> [ids]` (varre → monta → copia pra CRIATIVOS-PRONTOS → linha no LEIA-ME). Folha das 30: `conferencia-30-pecas.jpg`.

## O que deu errado e como foi resolvido
- **Downloads truncados pela rede:** o `wavespeed run --download` gravou ~10 clipes pela metade (l01–l05 com 270 KB; s07 2,6 MB) sem erro; a montagem saiu com 19 frames. Regra nova: **validar todo clipe decodificando inteiro** (`ffmpeg -v error -i x -f null -`) e rebaixar da URL do `.out.json` (`rebaixar.py`).
- **Mão na lente / segunda pessoa:** Secret s02/s05/s09/s10 (prompt antigo, negativo) e podcast p01 b4, p02 b2/b3, p06 b5 (homem de óculos com microfone entrando na cena) → regerados com **pose em positivo** ("she is the ONLY person in the studio for the entire clip… hands rest on her lap") — todos limparam de primeira. Luiza l02 teve um "batente de porta" alucinado no fim → regerado.
- **Instabilidade da WaveSpeed:** vários "fetch failed" / "Service temporarily unavailable" em uploads e runs — o `gerar-clipes.sh` com `set -e` derrubou um lote inteiro (l06–l10) por 1 upload; refeito. Dois two-shots ficaram com URL vazia no req (upload falhou) → corrigidos à mão.

## Custo real: US$ 27,8 (≈ US$ 0,93 por peça)
50 imagens ≈ 3,4 · 70 clipes Pruna + 9 regerações ≈ 24,4 · 1 estorno. Previsto: US$ 22 + 10 %.
