# var4 — 4 avatares da Emilly (Zap #3) · 2026-09-10

Mesma peça de `../pecas/zap-emilly-avatar.mp4` (15) trocando **só o rosto**. Voz original é masculina → 4 homens (correção do Maestro; v2/v4/v5 mulheres descartadas). Talking heads OmniHuman em `clipes/talking-head-vN.mp4` (718×1286, 25 fps, ~29 s, áudio original 0–29,1 s, sujeitos centrados), avatares-base em `base/`, casting em `casting.tsv`.

Montagem: `montar-var4.py vN` (mede o rosto no clipe, calcula o `--th-x`, chama `../remontar-emilly.sh`, confere, copia pra CRIATIVOS-PRONTOS e escreve a linha no LEIA-ME); `vigiar.sh` fez isso sozinho conforme cada clipe caía. `vN=THX` força o deslocamento.

| # | var | avatar | rosto no clipe (x, escala 1080) | --th-x | rosto na peça | arquivo |
|---|---|---|---|---|---|---|
| 16 | v3 | homem branco, barba grisalha | 336–790 (454) | −336 | 0–454 | `pecas/zap-emilly-avatar-v3-homem-branco-barba-grisalha.mp4` |
| 17 | v6 | homem negro, careca, barba | detector: 328–533 (só a área clara da pele) → **forçado −308** (o −158 automático deixou metade do rosto sob o card) | −308 | ≈ 0–410 | `pecas/zap-emilly-avatar-v6-homem-negro-careca-barba.mp4` |
| 18 | v7 | homem asiático | 319–764 (445) | −319 | 0–445 | `pecas/zap-emilly-avatar-v7-homem-asiatico.mp4` |
| 19 | v8 | homem loiro, barba | 298–754 (456) | −298 | 0–456 | `pecas/zap-emilly-avatar-v8-homem-loiro-barba.mp4` |

Todas: 1080×1920 · 30 fps · 34,07 s · áudio original inteiro · 0 silêncios ≥ 0,4 s · corte do CTA em 28,933 s. Regra do reenquadre: borda direita do rosto em x 375 (início do card) sem cortar a bochecha esquerda — como os rostos têm 410–456 px contra ~300 do original, sobram 35–80 px de orelha/bochecha sob os 30 px de degradê do card; olhos e boca sempre livres. Detector de rosto: faixa dos olhos (y 520–820) no frame escalado a 1080, trecho claro contíguo que contém x 540; **falha em pele escura** (v6) — conferir sempre o zoom com a linha x 375.

Conferência em `conferencia/`: `vN-folha-8-instantes.jpg` (original ×3 | peça), `vN-zoom-linha-card.jpg`, `folha-4-avatares-linha-card.jpg`, `folha-5-avatares-t20.jpg` (os 4 + o 15). `resumo.tsv` tem a medição de cada rodada (v6 aparece duas vezes: automática e forçada).

Cópias: `CRIATIVOS-PRONTOS/16..19-ZAP-emilly-avatar-vN-<slug>.mp4` + linhas 16–19 no LEIA-ME.

## Custo real

| item | valor |
|---|---|
| imagens-base (4 + as 3 mulheres descartadas, Maestro) | ≈ US$ 0,20 |
| OmniHuman 0,16 × 29,1 s × 4 | US$ 18,64 |
| montagem, conferência, cópias | US$ 0,00 |
| **total var4** | **≈ US$ 18,84** (≈ 4,66 por avatar + imagens) |
