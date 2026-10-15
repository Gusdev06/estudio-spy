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

## Correção 21/09 — podcast 91–100 reprovado ("cortando o rosto" / "piscava avatares anteriores")
Causas encontradas, todas no molde `montar-clone.py` de 13/09 e na geração:
1. **Rosto cortado:** o recorte da janela era fixo (`650:530:42:467`), calibrado nos avatares de 13/09; os novos têm a cabeça em outra altura. → `podcast/montar-clone-v2.py` recorta **centrado no rosto de cada clipe** (detector YuNet/OpenCV, `gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx`), na mesma altura relativa do original (rosto em y≈295/587).
2. **"Avatares anteriores":** (a) o two-shot de 0,5 s mostrava duas mulheres que não eram as dos closes → substituído por um close A cobrindo 0–2,77 s (`bloco-12b`, 10 clipes novos); (b) **o Pruna trocou de pessoa no meio do clipe** em vários blocos (p03 b4/b5, p05 b12/b2/b4/b5, p08 b4, p09 b4/b5 — tirou até o hijab): frame 0 = imagem, do frame 1 em diante outra mulher, mais perto da câmera. Regerados com prompt que **trava a identidade em positivo** ("stays EXACTLY the same person… same hijab… same framing") e, no bloco 5, sem pedir "talks straight to the camera" (isso fazia o modelo reimaginar um plano frontal). Em p05 b2/b4 a imagem usada nem era a do casting (URL trocada por um upload que falhou) — reupload + regeração. (c) frame 0 de todo clipe Pruna é a imagem parada (enquadramento ≠ vídeo) → pulado na montagem.
3. Timing por `tpad` no lugar de `setpts`.
Ferramenta nova: `podcast/checar-identidade.py` (tamanho e cor do rosto no frame 0 × resto — pega o drift de enquadramento; drift de identidade com mesmo tamanho ainda precisa de olho). Custo da correção: ≈ US$ 2,2 (10 clipes 12b + 12 regerações). As 10 peças foram remontadas e substituídas em CRIATIVOS-PRONTOS (91–100). A peça 40 (13/09) tem o mesmo two-shot de 0,5 s e não foi refeita.
