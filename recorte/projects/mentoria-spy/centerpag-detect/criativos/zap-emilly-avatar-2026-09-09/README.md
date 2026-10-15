# Lote zap-emilly-avatar — Zap #3 (Emilly Bredoff, 939122432559594) com avatar novo · 2026-09-09

Replicar `centerpag-detect/anuncios/emilly-bredoff-939122432559594.mp4` (360×480, 30 fps, 34,07 s) trocando **só o rosto**. Áudio original em `audio/audio-original.m4a` (locução termina em 28,7 s). Teardown do Peneira: `centerpag-detect/referencias/2026-09-09-teardown-edicao-emilly-bredoff.md` (seção "Reconciliação com o Bisturi"). Casting do avatar: `casting.md` (Maestro).

## Peça (2026-09-09, 23:5x)

`pecas/zap-emilly-avatar.mp4` — 1080×1920 · 30 fps · 1022 frames · **34,07 s** · H.264 crf 16 bt709 · áudio = `audio/audio-original.m4a` inteiro (AAC 192k). Cópia: `CRIATIVOS-PRONTOS/15-ZAP-emilly-avatar-novo.mp4`.

Talking head: `clipes/talking-head-emilly-omnihuman.mp4` (OmniHuman, 718×1286, 25 fps, 28,96 s, `base/avatar-emilly-1.png` + `audio/audio-original-0-29.1.m4a`). Veio **centrado** (rosto em x 330–740 na escala 1080) → `--th-x -330`: rosto em x 0–410, cabeça do microfone visível no queixo, só a orelha direita entra nos 30 px de degradê do card (x 375–405). Não dá pra fechar o rosto inteiro à esquerda de 375 sem cortar a bochecha: o rosto do avatar tem 410 px contra ~300 do original. Depois de 28,96 s o último frame segura até o corte (tpad). Rosto some no corte do CTA, como no original.

**Corte do CTA medido no original: frame 868 = 28,933 s** (luma 26,9 → 55,9). O molde tinha 29,1 s e o card vazava 5 frames do CTA original; corrigido pra 28,933.

Conferência (`conferir-emilly.py` → `conferencia/`): `folha-8-instantes.jpg` (original ×3 | peça em 0,5 · 4 · 9,5 · 13 · 20 · 25 · 29,5 · 33 s), `zoom-caixa-card-t4.jpg` (linha vermelha em x 375), `zoom-card-t20.jpg`, `corte-cta-29.0-29.3-31.jpg`. Silêncios ≥ 0,4 s na peça: 0.

## Custo real

| item | valor |
|---|---|
| imagem-base (GPT Image 2) | US$ 0,06 |
| OmniHuman 0,16 × 29,1 s | US$ 4,66 |
| molde, montagem, conferência | US$ 0,00 |
| **total** | **≈ US$ 4,72** (casting previa 5,57 com 34 s inteiros — o CTA é borrão, não precisa de rosto) |

## Molde — `remontar-emilly.sh`

```
cd projects/mentoria-spy
bash centerpag-detect/criativos/zap-emilly-avatar-2026-09-09/remontar-emilly.sh clipes/<talking-head>.mp4 [--th-x N] [--zoom F] [--th-y N] [--off-head N]
```
→ `pecas/zap-emilly-avatar.mp4` (1080×1920, 30 fps, 34,07 s, áudio original copiado). Custo zero. Geral: `remontar-emilly.sh <th.mp4> <saida.mp4> [opções]`.

Reaproveitado **por recorte do original** (×3): a **caixa verde do hook** (x 43–316 · y 29–83, #00FD11, 2 linhas pretas y 35–51 / 57–78, cantos arredondados r≈5 → máscara r 15) e o **card do app** (x 125 até a borda direita · y 109–407, alfa já composto sobre o quarto escuro; borda esquerda em gradiente → feather 30 px; corre pra fora do quadro no original → fade pra transparente nos últimos 150 px). Os dois seguem o original frame a frame até 29,1 s, então todas as fases do card (landing → digitação → Accessing WhatsApp → perfil → terminal → Chats) vêm de graça. **Não há karaokê** (0 px de branco fora do card em 14 instantes; Peneira confirmou em 6) — `--karaoke` existe só como opção, desligada. **CTA (29,1 s → fim)** refeito em tela cheia: borrão do talking head (boxblur 30, fade 0,35 s) + `CLICK THE LINK BELOW / AND SEE THE TRUTH NOW.` em Poppins Bold 64 #F2F500 (y 560 / 640) + 3 chevrons brancos 318 px (original x 127–233 · y 315–424) com bounce de 18 px a 1,2 s.

## Decisão de enquadramento 9:16 (Bisturi + Peneira, 09/09)

O original é um quadro **1,2:1 (360×299, y 109–407) letterboxado num canvas 4:3**, com a caixa verde na faixa preta de cima e o CTA como asset 9:16 com o topo escondido. **Refazer em 9:16, não cortar o 4:3**: talking head novo em 1080×1920 cheio; a composição medida entra ×3 com a **janela de conteúdo centrada verticalmente** (topo em y 511): card em x 375–1080 · y 511–1408, caixa em x 129–951 · y 271–436 (mesma distância caixa→janela do original, 78 px). Matemática conferida pelo Peneira.

**Ressalva de composição (Peneira):** no original o rosto fica na **metade esquerda** e o card cobre a direita sobre o quarto escuro, nunca sobre a cara. O talking head do OmniHuman deve vir com o sujeito à esquerda (rosto até x≈375) e o lado direito = fundo escuro. Se vier centrado, `--th-x -N` desloca o sujeito pra esquerda e `--zoom 1.2` afasta o rosto do card (o que sobrar à direita fica preto, que é o que o card alfa espera).

## Custo (estimativa antes de disparar)

Talking head só precisa cobrir **0–29,1 s** (a partir daí é borrão): OmniHuman 0,16 × 29,1 s ≈ **US$ 4,66** (34,07 s inteiros = 5,45). Imagem-base GPT Image 2 ×2 = US$ 0,12. Montagem, whisper e conferência: zero. **Real: preencher quando o clipe cair.**

## Teste do molde (o próprio original como entrada)

`bash remontar-emilly.sh centerpag-detect/anuncios/emilly-bredoff-939122432559594.mp4 conferencia/molde/teste-original.mp4 --th-y 185` — o original escalado ×3 entra como "talking head" em y 185, o que põe a janela dele (y 327) exatamente sob o card do molde (y 511); saída ≈ original em 9:16. Folha: `conferencia/molde/folha-molde-emilly.jpg` (original ×3 | molde em 0,5 · 4 · 9,5 · 13 · 20 · 25 · 29,5 · 33 s). 1022 frames, 34,07 s.

Whisper do áudio original (113 palavras, fim 28,7 s): `molde/audio-original-16k.json` — sem pausas ≥ 0,4 s dentro da fala (silencedetect −35 dB); o silêncio final é o CTA, mantido como no original.
