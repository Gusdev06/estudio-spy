# Roteiro D — produção (2026-08-31)

Criativo de 45s no formato breaking-news âncora + especialista, gerado 100% por IA.
Roteiro em `../../roteiros/2026-08-31-wpp01-copy-formato-breaking-news.md`.

## Entregável

- **`roteiro-d-v1-45s.mp4`** — corte final, 1080×1920, 45,2s, com áudio e tarja.

## Pipeline

| Etapa | Modelo | Custo |
|---|---|---|
| Frames-base (âncora, especialista) | `openai/gpt-image-2/text-to-image` · 9:16 · 2k · high | $0,38 × 2 |
| 5 clipes falados | `kwaivgi/kling-v3.0-pro/image-to-video` · sound=true | ~$0,168/s → $7,56 |
| Tarja + costura | ffmpeg (drawbox + drawtext, Arial Black/Bold) | — |
| **Total** | | **~$8,32** |

**Kling 3.0 Pro fala o roteiro.** Áudio nativo com lip sync — não precisou de TTS nem de
etapa de lipsync. Os 5 clipes foram transcritos com Whisper e batem palavra por palavra
com o roteiro.

## Estrutura

| Clipe | Quem | Dur. | Origem |
|---|---|---|---|
| `c1` | Âncora — abertura + handoff | 11s | `frames/ancora-v1.png` |
| `c2` | Especialista — mecanismo do fracasso + reframe | 15s | `frames/especialista-v1.png` |
| `c3` | Âncora — linha de reação | 5s | `frames/ancora-v1.png` |
| `c4` | Especialista — produto + "nothing gets installed" | 10s | `frames/especialista-v1.png` |
| `c5` | Âncora — fecho + oferta | 4s | `frames/ancora-v1.png` |

Âncora e especialista **nunca aparecem no mesmo quadro** — duas gerações independentes,
costuradas pela tarja idêntica + handoff falado + linha de reação. Ver
[[costura-de-clipes-por-tarja-persistente]] no wiki.

## Tarja

Renderizada por ffmpeg, **parâmetros idênticos em todos os 5 clipes** (é o requisito da
costura). Barra navy `#0E1A2B` com `THE SIGNAL` em Arial Black, barra off-white `#F2F2F2`
com o ticker em Arial Bold navy, filete crimson `#C8102E` na borda esquerda.

Posicionada em **y=1380** de 1920 (72% da altura) — subida da posição original (y=1600) pra
sair da faixa que a UI de Reels/TikTok cobre com legenda, perfil e botões.

`montar.sh` é parametrizado — reconstrói o corte inteiro trocando só a variável:

```bash
TARJA_Y=1300 ./montar.sh                              # sobe a tarja
TICKER="DELETED DOESN'T MEAN GONE" ./montar.sh        # troca o ticker
PROGRAMA="THE BRIEF" ./montar.sh                      # troca o nome do programa
CTA="SEE IT FREE" ./montar.sh                         # troca o card final
STK1="HER FRIENDS" STK2="ALREADY KNOW." STK3="DO YOU?" ./montar.sh   # troca o sticker
STK_BG=0x0E1A2B ./montar.sh                           # sticker navy em vez de crimson
STK_T=2.5 ./montar.sh                                 # sticker sai mais cedo
```

Alternativa gerada no GPT Image 2 em `tarja-gptimage2-alt.png` — **não usada** (o Gusta
aprovou a versão ffmpeg). Fica como referência caso queira uma tarja com mais desenho.

## Decisões de risco aplicadas

- Tarja de **programa inventado** (`THE SIGNAL`), não `BREAKING NEWS`.
- Especialista **sem credencial**: sem jaleco, sem bordado, sem "Dr." na fala. O âncora só
  diz o nome (Elena Ross).
- **Marca nunca falada.** Nenhuma menção ao produto no áudio.
- Ticker anuncia **o problema**, nunca o produto.

## Inserts de footage real (33–35s e 37–40,4s)

Screen recording real do funil `go.zappdetect.com`
(`EDIÇÃO 2/EDIÇAO ANIMADA/ScreenRecording_08-13-2026 19-56-53_1.MP4`, 3min33, 1170×2532).
Substituiu o mockup em HTML — é o produto de verdade e a página **repete a copy do anúncio**
("Built for people who've been burned by spy apps that didn't work", "No app to install",
"No phone access needed"), o que fecha a congruência anúncio → página.

| Insert | Tempo | Fala que cobre | Fonte |
|---|---|---|---|
| A | 33,0–35,0s | "You enter the number" | recording t=2,0 — campo do número + os 3 bullets de objeção + CTA `Reveal The Truth Now`. Recortado **abaixo do seletor `A Man / A Woman`** pra a peça servir os dois segmentos. |
| B | 37,2–40,6s | "you're reading what was already there" | recording t=192,5 — `RECOVERED FROM DELETED CACHE` + conversas suspeitas |

Entram como **cutaway sobre a fala**: cobrem só o vídeo, o áudio da especialista segue
correndo por baixo. A tarja é desenhada **depois** do overlay — se inverter, o insert a apaga
e a costura quebra.

⚠️ **PII borrada.** O recording tem o número real (+55 27 99954-6872), o e-mail
`gabrieljota@gmail.com` e o nome "Gabriel". O insert A tem `boxblur` no campo do número; a tela
do e-mail (t≈168–176) foi evitada por completo. **Qualquer trecho novo desse recording precisa
passar pela mesma checagem antes de entrar.**

O mockup em HTML segue em `insert/dashboard.html` + `dashboard.png` como fallback — útil se
precisar de uma tela que o funil não tem.

## Sticker hook (0–3s)

Três linhas em blocos crimson `#C8102E` — mesma cor da tarja e do card final, a peça toda
fecha em duas cores.

```
EVERYONE FINDS OUT
THE PARTNER IS
ALWAYS LAST
```

Device: **binário forçado virado sentença.** Não pergunta se a pessoa quer descobrir — afirma
que todo mundo descobre e a coloca na pior posição. Sentença dói mais que pergunta porque
ninguém se defende de sentença.

Sai aos 3s, sempre. Passou disso vira caption e compete com a tarja
([[ticker-como-hook-sound-off]]).

**Limite de largura:** ~22 caracteres por linha em Arial Black 60. Passou disso, estoura o
quadro de 1080 — quebre em mais linhas ou baixe o `STK_SZ`.

## Card final (43s–45s)

Barra crimson `#C8102E` encostada no topo da tarja com `FIRST SEARCH IS FREE` em Arial Black,
entrando exatamente quando o âncora fala a linha.

## Legenda

Não usada, de propósito. A tarja já ancora o sound-off — legenda queimada por cima compete
com ela. Ver [[ticker-como-hook-sound-off]].
