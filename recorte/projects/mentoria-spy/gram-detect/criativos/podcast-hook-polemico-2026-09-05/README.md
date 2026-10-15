# Podcast Zap — hook polêmico "A faithful man has no deleted messages." (2026-09-05)

Criativo em formato podcast (host + convidada) pra oferta WhatsApp (Spy Zap). Roteiro: `centerpag-detect/roteiros/2026-09-05-podcast-hook-polemico-zap.md` (Isca). Planos e clipes: Maestro. Montagem: Bisturi, custo zero.

| | Arquivo |
|---|---|
| **Peça** | `PODCAST-ZAP-hook-faithful-man.mp4` — 1080×1920, 30 fps, 845 frames, **28,17 s**, H.264 crf 16 bt709, AAC 192k |
| Planos (imagens) | `imagens/p1-two-shot.png` (768×1360), `p2-close-host.png`, `p3-close-guest.png` (864×1536) |
| Clipes por cena | `clipes/cena-1..7.mp4` — MiniMax H3, 768×1344, 24 fps, áudio embutido (TTS passado pelo modelo, lipsync no vídeo) |
| TTS por fala | `audio/host-1, guest-2, guest-3, host-4, guest-5, host-6, host-7 .mp3` (não usados na trilha: o áudio da peça é o do clipe, que está alinhado com a boca) |
| Whisper por palavra | `audio/clip-cena-N.json` (mlx small.en, local) — fonte da timeline e do karaokê |

## Custo real

| item | valor |
|---|---|
| 3 imagens de plano | US$ 0,20 |
| TTS (7 falas) | ~US$ 0,05 |
| MiniMax H3 768p (39 s pedidos + 8 s de retry) | ≈ US$ 4,90 |
| montagem (ffmpeg) | US$ 0,00 |
| **total** | **≈ US$ 5,15** |

## Timeline final (pausas removidas — regra do Gusta, 05/09)

Cada cena corta no fim da última palavra + 0,3 s de respiro; todo silêncio ≥ 0,4 s dentro da fala (ffmpeg `silencedetect` a −35 dB) fica com 0,25 s, cortando vídeo e áudio juntos pra manter o lipsync. Cortes secos entre cenas.

| cena | quem | clipe | fala até | corte no clipe | pausas removidas | saída |
|---|---|---|---|---|---|---|
| 1 | host, close | 4,46 s | 2,46 s | 2,76 s | — | 0,00–2,77 |
| 2 | convidada, close | 9,42 s | 7,22 s | 7,52 s | 3 (0,76–1,32 · 3,73–4,25 · 5,47–5,83) | 2,77–8,87 |
| 3 | two-shot | 8,00 s | 6,30 s | 6,60 s | 3 | 8,87–14,27 |
| 4 | host, close | 4,46 s | 2,66 s | 2,96 s | 1 | 14,27–16,97 |
| 5 | convidada, close | 4,46 s | 1,48 s | 1,78 s | — | 16,97–18,73 |
| 6 | host, close | 8,00 s | 6,98 s | 7,28 s | 3 | 18,73–24,93 |
| 7 | two-shot | 5,17 s | 3,10 s | 3,40 s | 1 | 24,93–28,17 |

**Cortes em 2,77 · 8,87 · 14,27 · 16,97 · 18,73 · 24,93 s.** 11 pausas removidas, 4,17 s a menos; os clipes somavam 43,96 s e a peça ficou em 28,17 s. 82 palavras em ~26 s de fala ≈ 190 wpm (campeão: 191).

## Camadas

- **Caixa do hook**: frame 0 até o fim da cena 2 (frame 266 = 8,87 s), x 106–973 · y 862–1058, #E80052 (medido #FE0553 no decode), texto `A FAITHFUL MAN HAS` / `NO DELETED MESSAGES.` em Poppins Bold 60 px caixa alta, #EFFD11, contorno 2 px + sombra 5 px, camada RGB → bt709 → overlay (mesma receita do lote GD-AD01).
- **Karaokê**: 34 blocos (`molde/karaoke.tsv`), Inter Bold 69 px, branco com glow, base em y 1521 (78%); na cena 7 sobe pra base y 1250, acima das setas (senão ficava branco sobre branco). Tempos por palavra do whisper no áudio do clipe, remapeados pro tempo de saída descontando as pausas removidas.
- **Setas**: as duas setas brancas do GD-AD01 (bloco 8), 94 frames recortados com alfa por luminância (`setas/`), em loop, x 340–740 · y 1290–1760, do frame 755 (25,17 s) ao fim = últimos 3 s.
- **Escala**: 768×1344 → 1080×1920 Lanczos (corte de 5 px em cima e embaixo), 24 → 30 fps.

## Reproduzir

```
bash gram-detect/criativos/podcast-hook-polemico-2026-09-05/montar.sh          # timeline + karaokê + render
python3 gram-detect/criativos/podcast-hook-polemico-2026-09-05/molde/timeline.py   # só a timeline (RESPIRO, PAUSA_MAX, PAUSA_KEEP por env)
```
Whisper nos clipes: `transcrever-tts.sh` (mp3 de audio/) ou o laço em `molde/` (json por clipe). Conferência em `conferencia/`: `folha-cenas`, `folha-cortes` (último frame de cada cena × primeiro da seguinte), `folha-karaoke` (frame no início de cada bloco com o texto esperado).

## O que conferir no olho

Cortes de pausa dentro da fala: 11 saltos de imagem de 0,2–0,5 s dentro do mesmo plano (a pessoa "pula" um pouco). É o preço da regra de ritmo; se algum incomodar, subir `PAUSA_MAX` ou `PAUSA_KEEP` e remontar.

## Versão com música (Gusta, 05/09)

`PODCAST-ZAP-hook-faithful-man-musica.mp4` — mesma peça, com trilha de suspense por baixo da voz.
Trilha: `audio/musica-7y4kJtkioFk.m4a` ("música de suspense sem direitos autorais", canal canções tube, YouTube
`7y4kJtkioFk`, 103 s). Mix: música a 9% (≈ −21 dB), fade in 1 s, fade out 2,5 s, sem normalizar a voz. Vídeo copiado sem reencode.

## Versão com funil (Gusta, 05/09) — `PODCAST-ZAP-hook-faithful-man-funil.mp4`

Mesma peça e **mesmo áudio da versão com música** (md5 da faixa AAC idêntico, `-c:a copy`). Cenas 3, 6 e 7 viram **split 50/50** (estado D do GD-AD01): rosto em cima (y 0–960), funil gravado embaixo (y 960–1920). Cenas 1, 2, 4, 5 ficam em rosto cheio. Corte seco entre estados. Custo zero. Script: `montar-funil.py` (lê `molde/timeline.json` e `molde/karaoke.tsv` da peça original).

Fonte do funil: `EDIÇÃO 3/EDIÇAO ANIMADA/ScreenRecording_08-13-2026 19-56-53_1.MP4` (go.zappdetect.com, 1170×2532 60 fps, 213 s). Método: [[insert-de-funil-real-como-cutaway]] + [[funil-gravado-como-painel-lateral]] do wiki — recorte da área útil, sem barra do Safari nem URL, `y` ajustado por trecho.

| cena | saída | rosto (recorte 1080×960 da base, y) | painel (trecho da gravação → recorte 1170×1040 → 1080×960) |
|---|---|---|---|
| 3 | 8,87–14,27 s | two-shot, y 440 | **"Restoring deleted data" + mapa TRACKING**, rec 116,0–121,4 s a 1×, recorte y 1110–2150 (linha "Key rejected", card, barra 72→76 %, mapa) |
| 6 | 18,73–24,93 s | close host, y 286 | a) rec 0,00–2,17 s landing → toque → teclado (65 fr) · b) rec 2,0–7,0 s **digitando, 4,4×** (34 fr, começa em "you type" = fr 627) · c1) número completo 4 fr · c2) **"Accessing cloud backup" + mapa**, rec 23,6–26,4 s (83 fr). Recorte do formulário 1150×1022 em (10,110) |
| 7 | 24,93–28,17 s | two-shot, y 400 | **"Scan Complete — Red Flags Found"** + 257 / 19 / 34 + Risk 87 %, frame congelado em 188,05 s (`molde/painel-fim-188.05.png` — a página rola rápido ali), recorte y 960–2000. Setas do campeão por cima do painel a partir de 25,17 s |

- **Karaokê**: y 890 (base ~940) nos três splits — logo acima do painel, ~49 % da altura, como no estado D; y 1472 (78 %) nos rostos cheios. Mesmos blocos e tempos.
- **PII**: campo do número desfocado (`boxblur 22`, x 690–1030 · y 633–811 da gravação) durante a digitação; os recortes das cenas 3, 6c e 7 ficam abaixo do card de perfil e do campo, então o número real não aparece. A linha "Gabriel, … +55 ●●●● 6872" fica fora do recorte da cena 7.
- **Por que o painel 7 é congelado**: entre 3:06 e 3:09 a página rola ~600 px/s; um trecho ao vivo não segura os números no quadro por 3,2 s. As setas pulsando dão o movimento.
- **Trocado no caminho**: o trecho de 0,1 s puxado por `-ss` entrava ~22 frames atrasado no overlay; virou PNG em `-loop 1`.

Conferência em `conferencia/funil-*`: `funil-folha-cenas` (meio de cada cena), `funil-folha-estados` (último frame antes × primeiro depois de cada troca + entrada das setas), `funil-folha-costura` (y 840–1080 ×2, linha vermelha em 960), `funil-folha-paineis` (painel de baixo em tamanho real), `funil-ref-*` (frames da gravação usados). Reproduzir: `python3 gram-detect/criativos/podcast-hook-polemico-2026-09-05/montar-funil.py` e `conferir-funil.py`, de `projects/mentoria-spy/`.

## var5 — 5 variações de hook da versão 06 (Gusta, 05/09: "o podcast foi o que mais performou")

Mesma peça da versão com funil + música (`PODCAST-ZAP-hook-faithful-man-funil.mp4`), mudando **só a cena 1 (host fala o hook novo) e o texto da caixa**. Cenas 2–7, funil nos splits (3 · 6 · 7), setas, karaokê das cenas 2–7 (deslocado pelo tamanho novo da cena 1) e música (9 %, fade 1 s / 2,5 s, remixada sobre a voz nova) idênticos. Script: `var5/montar-var.py vN` (lê `var5/hooks.tsv`, `var5/clipes/cena-1-vN.mp4`, whisper local do clipe → `var5/audio/clip-cena-1-vN.json`, timeline e karaokê por variante em `var5/molde/`). Conferência: `var5/conferir-var.py` → `var5/conferencia/`.

Regra de pausas na cena 1 nova: corte no fim da fala + 0,3 s; silêncio ≥ 0,4 s dentro da fala fica com 0,25 s; silêncio inicial fica com 0,1 s (v5 tinha 1,66 s de espera antes da fala). Caixa: mesma spec (868×197, #FE0553, Poppins Bold 60, #EEFC00, contorno 2 + sombra 5, até o fim da cena 2), texto em 2 linhas balanceadas, fonte cai automaticamente se a linha passar de 828 px (só a v4 caiu, pra 58).

| var | caixa | cena 1 | peça | silêncios ≥ 0,4 s | arquivo |
|---|---|---|---|---|---|
| v1 | IF HE DELETED / IT, HE CHEATED. | 64 fr (2,13 s) · 1 pausa cortada | 826 fr · 27,53 s | 0 | `var5/PODCAST-ZAP-v1-if-he-deleted-it-he-cheated.mp4` |
| v2 | IT'S NOT PARANOIA / IF HE'S HIDING IT. | 82 fr (2,73 s) | 844 fr · 28,13 s | 0 | `var5/PODCAST-ZAP-v2-it-s-not-paranoia-if-he-s-hiding-it.mp4` |
| v3 | 'JUST A FRIEND' / IS HOW IT STARTS. | 55 fr (1,83 s) · 1,77 s de silêncio inicial cortado | 817 fr · 27,23 s | 0 | `var5/PODCAST-ZAP-v3-just-a-friend-is-how-it-starts.mp4` |
| v4 | A HAPPY MARRIAGE / DOESN'T NEED A PASSCODE. (Poppins 58) | 77 fr (2,57 s) · 1,51 s de silêncio inicial cortado | 839 fr · 27,97 s | 0 | `var5/PODCAST-ZAP-v4-a-happy-marriage-doesn-t-need-a-passcode.mp4` |
| v5 | NOTHING TO HIDE, / NOTHING TO DELETE. | 79 fr (2,63 s) · 1,66 s de silêncio inicial cortado | 841 fr · 28,03 s | 0 | `var5/PODCAST-ZAP-v5-nothing-to-hide-nothing-to-delete.mp4` |

(Detalhe por variante em `var5/conferencia/resumo.tsv`; folha da cena 1 das 5 em `var5/conferencia/folha-cena-1-5-variacoes.jpg`; caixas em `caixas-5-variacoes.jpg`.)

Cópias (Maestro) em `CRIATIVOS-PRONTOS/10-ZAP-podcast-v1-if-he-deleted-it-he-cheated` · `11-…-v2-not-paranoia-if-hes-hiding-it` · `12-…-v3-just-a-friend-is-how-it-starts` · `13-…-v4-happy-marriage-no-passcode` · `14-…-v5-nothing-to-hide-nothing-to-delete` (LEIA-ME de lá).

**Custo (Maestro):** TTS 5 falas ~US$ 0,05 + MiniMax H3 768p 5 × ~US$ 0,45 ≈ US$ 2,25 → **≈ US$ 2,30**. Montagem, whisper e conferência: zero.
