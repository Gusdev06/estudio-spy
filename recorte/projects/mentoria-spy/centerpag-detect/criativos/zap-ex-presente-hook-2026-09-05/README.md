# Lote zap-ex-presente — wpp-01 reescrito pra ex no presente, molde L10 (2026-09-05)

Oferta WhatsApp (go.zappdetect.com). Roteiro: `centerpag-detect/roteiros/2026-09-05-zap-ex-presente.md` (Isca, 7 blocos, 5 fases). Molde de edição: wpp-01 Esther Vicman, layout L10 — card alfa sobre plano único, medido em `molde/README-l10.md` (Bisturi). Locução final: `audio/locucao-ex-v2.mp3` (MiniMax speech-2.6-hd, 37,04 s; fala termina em 36,62 s). Avatar: `base/avatar-ex-1.png` (casting.md).

## Peças (2026-09-05, 12:10 — versão SEM PAUSAS)

| | Arquivo |
|---|---|
| **A** | `pecas/zap-ex-presente-A.mp4` — hook `IF HE MISSED YOU, / HIS PHONE WOULD SHOW IT.` |
| **B** | `pecas/zap-ex-presente-B.mp4` — hook `WHAT HE DELETES / SAYS WHAT HE FEELS.` |
| **C** | `pecas/zap-ex-presente-C.mp4` — hook `HE MOVED ON IN PUBLIC. / CHECK WHAT HE DELETED.` |
| base | `pecas/zap-ex-presente-base.mp4` — sem hook, crf 10 (só pra regerar variantes) |

1080×1920 · 30 fps · 939 frames · **31,30 s** · H.264 crf 16 bt709 · AAC do clipe cortado. Diferem só no texto do matte.

**Regra de ritmo (Gusta, 05/09) aplicada no talking head antes da remontagem** (`cortar-pausas.py`): o clipe do OmniHuman tinha **18 silêncios ≥ 0,4 s** (silencedetect −35 dB); cada um ficou com 0,25 s, cortando vídeo e áudio juntos → `clipes/talking-head-ex-omnihuman-sem-pausas.mp4`, **36,92 → 31,17 s (−5,75 s)**. Fronteiras do `blocos.tsv` remapeadas pro tempo novo (original em `molde/blocos-com-pausas.tsv`), karaokê refeito do whisper do clipe cortado (`molde/clipe-sem-pausas-16k.json`; o anterior em `karaoke-com-pausas.tsv`). Conferido: **0 silêncios ≥ 0,4 s** nas 3 peças. Trechos removidos em `molde/pausas.json`.

Talking head bruto: `clipes/talking-head-ex-omnihuman.mp4` (OmniHuman, 718×1286, 25 fps, 36,92 s, avatar `base/avatar-ex-1.png` + locução v2) — não apagado; a montagem usa o `-sem-pausas`. Escalado a 1080 de largura (1934 de altura), recorte 1080×1632 em **`--off-head 240`**: olhos do clipe em y ≈ 650 → y ≈ 700 na peça (campeão: y ≈ 670, 35 % do quadro). Áudio conferido contra a v2 (`conferir-audio.sh`): correlação de envelope 0,98, deslocamento +0,02 s, 103 palavras iguais no whisper → karaokê da v2 mantido.

## Custo real

| item | valor |
|---|---|
| imagem do avatar | US$ 0,06 |
| TTS locução v2 (MiniMax speech-2.6-hd) | ~US$ 0,05 |
| OmniHuman 0,16 × 37,04 s | US$ 5,93 |
| molde, karaokê, montagem, conferência (ffmpeg + whisper local) | US$ 0,00 |
| corte de pausas + remontagem | US$ 0,00 |
| **total** | **≈ US$ 6,05** (3 peças, uma geração só — o matte é queimado por cima) |

## Conferência

`conferencia/lote-folha-8-instantes.jpg` (campeão × peça A em fases equivalentes: F1 2 s × 2,5 s · F2 12 × 7 · 20 × 11 · 28 × 16,5 · F3 33 × 19 · F4 45 × 23,5 · 47 × 26,7 · F5 53 × 29,5) · `lote-folha-blocos.jpg` (meio dos 11 blocos) · `lote-zoom-card-t11.jpg` · `lote-zoom-karaoke-cheio.jpg` · `lote-zoom-cta.jpg` · `lote-mattes-abc.jpg`. Script: `conferir-lote.py`.

## Pra remontar (ex.: outro clipe ou outro hook)

```
cd projects/mentoria-spy
bash centerpag-detect/criativos/zap-ex-presente-hook-2026-09-05/remontar-l10.sh clipes/<talking-head>.mp4 --off-head N
```
Sai em `pecas/zap-ex-presente-{base,A,B,C}.mp4` — A/B/C diferem **só no texto do matte** (`molde/hooks.txt`). Áudio = o do talking head, copiado (o clipe do OmniHuman já deve trazer a locução v2). `--off-head` = y do recorte 1080×1632 no talking head (o ator entra abaixo do matte, y 288); medir no clipe: olhos a ~30–35 % da altura do recorte. Se o clipe tiver menos de 37,04 s, a última imagem congela (tpad); se tiver mais, corta em 37,04 s.

Se a locução do clipe divergir da v2, refazer o karaokê: whisper local no áudio do clipe e `python3 karaoke-l10.py <json> molde/karaoke.tsv --blocos molde/karaoke-blocos.txt`, e conferir as fronteiras em `molde/blocos.tsv`.

## Fronteiras (clipe sem pausas; whisper por palavra em `molde/clipe-sem-pausas-16k.json`)

| fase | s (sem pausas) | s (antes) | bloco | tela |
|---|---|---|---|---|
| F1 Teaser · card | 0,00–4,90 | 0,00–5,75 | B1 | Chats + "257 deleted messages recovered!" + contadores |
| F2 Acesso · card | 4,90–9,21 | 5,75–11,20 | B2 | formulário, número digitado (desfocado) |
| | 9,21–13,30 | 11,20–15,60 | B3a | Accessing WhatsApp |
| | 13,30–15,29 | 15,60–18,25 | B3b | PROFILE HIDDEN · Start Analysis |
| | 15,29–17,97 | 18,25–21,50 | B4 | Accessing cloud backup |
| **F3 Card cheio** — rosto sai | **17,97**–20,34 | 21,50–23,90 | B5a | Restoring deleted data → Backup decrypted! |
| | 20,34–22,88 | 23,90–27,00 | B5b | terminal → BACKUP RECOVERED → HIDDEN DATA 257/150 |
| F4 Payoff · bleed | 22,88–24,77 | 27,00–28,90 | B6a | RECOVERED FROM DELETED CACHE |
| | 24,77–26,22 | 28,90–30,70 | B6b | Scan Complete · 257/19/34 · 87 % |
| | 26,22–27,25 | 30,70–32,40 | B6c | Dating Profiles |
| F5 CTA | 27,25–31,30 | 32,40–37,04 | B7 | borrão + CLICK THE LINK… + setas |

Rosto sai em 17,97 s = **57 %** (roteiro 55,7 %, campeão 54 %) — é onde "Because what he deletes…" começa (whisper do clipe cortado: 18,14 s). Corte seco em cada fronteira; só o CTA entra com fade de 0,35 s.

Hooks (roteiro §3): A `IF HE MISSED YOU, / HIS PHONE WOULD SHOW IT.` (Poppins Bold 70 — a linha 2 tem 24 caracteres e não cabe a 86) · B `WHAT HE DELETES / SAYS WHAT HE FEELS.` (86) · C `HE MOVED ON IN PUBLIC. / CHECK WHAT HE DELETED.` (76). O tamanho cai automaticamente até a linha mais larga caber em 1000 px; o bloco fica centrado no matte.

PII: campo do formulário, número vermelho, card de perfil (2×), botão Unlock, linha "Gabriel, … 6872" — tudo desfocado por bloco (`blur` no `blocos.tsv`). O terminal com o número (151,5–152,5 s) ficou de fora. Mapa TRACKING fora de todos os recortes.

## Validação (custo zero)

`conferencia/standin-avatar-locucao.mp4` = avatar parado + locução v2, só pra provar a esteira. Saídas em `conferencia/standin-zap-ex-presente-{A,B,C}.mp4`; folha por bloco em `conferencia/folha-blocos-standin.jpg`; mattes em `conferencia/mattes-lote-abc.jpg`. Molde testado antes com o próprio wpp-01: `conferencia/molde/`.

## Custo

Roteiro, molde, karaokê e montagem: zero. Locução v2: MiniMax (Maestro). Talking head OmniHuman: estimativa duração × preço unitário antes de disparar (Maestro).
