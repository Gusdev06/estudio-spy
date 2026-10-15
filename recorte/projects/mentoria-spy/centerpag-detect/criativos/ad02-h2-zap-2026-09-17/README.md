# AD02-H2 versão WhatsApp — copy nova, áudio novo, avatar novo, edição copiada · 2026-09-17

Pedido do Gusta (17/09, depois de aprovar as 53–58): "variação para WhatsApp: o roteiro precisa ser adaptado, as edições também, e gerar um áudio novo com copy nova". É o molde do AD02-H2 reconstruído (`gram-detect/criativos/ad02-h2-reconstrucao-2026-09-17/`) transplantado pra oferta Spy Zap.

| | |
|---|---|
| **Peça** | `AD02-H2-zap-z1.mp4` — 1080×1920 · 30 fps · 1087 frames · **36,23 s**. Cópia: `CRIATIVOS-PRONTOS/59` (md5 `b366a154…`) |
| Hook | frames 0–191 do AD02-H2 original (clipe de reação + manchete "Man catches girlfriend texting 22 different guys…"), vídeo e áudio intactos — não cita Instagram |
| Roteiro | `roteiro.txt` — 90 palavras. Mesma estrutura do original, trocando o mecanismo: "Instagram detail" → "WhatsApp detail"; "suspicious messages, contacts and unusual behavior" → "deleted messages, secret contacts and late-night chats"; "sneak through their phone" → "touch their phone" |
| Áudio | MiniMax `speech-2.6-hd` **Casual_Guy** speed 1,1 (a voz do wpp-01) → `audio/vo-zap.mp3` (30,85 s) → `cortar-pausas-audio.py` (5 pausas ≥ 0,4 s viram 0,25 s) → `audio/vo-zap-ritmo.wav` **29,72 s**, 0 silêncios ≥ 0,4 s |
| Avatar | `elencos/z1.txt` — negro, pele média-escura, ~33, buzz cut, barba boxed, brinco dourado; `base/z1.png` (gpt-image-2/edit sobre o frame do original, medium) → Pruna 30 s `clipes/z1.mp4` (704×1280 24 fps), prompt de pose em positivo, seed 77 |
| Enquadramento | fixo o vídeo inteiro (Z 1,35 / OY 160), como nas 54–58 |

## Timeline — `gerar-timeline.py` → `molde/timeline.json`
As fronteiras dos blocos são **as mesmas palavras do original** (medidas em 17/09), nos tempos do áudio novo (whisper `molde/vo-16k.json`):

| bloco | palavras | frames | camada |
|---|---|---|---|
| card | "There's one WhatsApp detail … away" | 192–287 | **"Accessing cloud backup / Locating backup files…" + barra** (rec 23,6 s), 788×252 cantos r=30 + sombra, mesmo centro vertical do card "Connecting" |
| painel A | "But hardly anyone … confront them, and" | 288–448 | **"Restoring deleted data 72 %" + mapa TRACKING** (rec 116,0 s ao vivo) |
| rosto limpo | "you don't have to touch … small traces" | 449–586 | — |
| painel B | "behind without … know where" | 587–968 | **B1** lista de chats "257 deleted messages recovered" (frame 182,6 s congelado, 4 s) → **B2** rolagem do relatório: deleted cache → suspicious conversations → photos (rec 192,0 s ao vivo, 8,7 s) |
| final | "to look. Get access below…" | 969–1086 | CTA "CLICK THE BELOW" + setas **994–1079** |

Sem legenda nos 24 primeiros frames do painel B e em "to look" (como o original). Karaokê em y 1113 / 1641 / 1695 / 1666 como no original.

## Painéis — `gerar-paineis.sh`
Recortados da **gravação real do funil** `EDIÇÃO 3/EDIÇAO ANIMADA/ScreenRecording_08-13-2026 19-56-53_1.MP4` (go.zappdetect.com, 1170×2532 60 fps — a mesma fonte do painel da peça 06), bbox de painel do original (193,347 · 692×1224). **Telefone e e-mail nunca aparecem:** número do perfil, campo do número e número no botão "Unlock Conversations" desfocados (gblur σ 14); a tela "Your report is ready" (e-mail) e o trecho "Gabriel, the photo on your screen…" ficaram de fora. Conferência: `conferencia/paineis.jpg`.

## Karaokê — `gerar-karaoke-zap.py`
O mesmo desenho do karaokê reconstruído do AD02-H2 (Oswald Bold 76 px, amarelo/vermelho alternando, contorno 7 + sombra), com **blocos automáticos**: até 3 palavras, quebra em `. ? ! ,`, 4 sobrando viram 2+2. Blocos gerados: "There's one WhatsApp | detail that gives | almost everyone away | but hardly anyone | knows where | to look | …".

## Montagem — `montar-zap.py <clipe> <saida>`
O `montar-reconstrucao.py` do AD02-H2 com: card 788×252, painel B em dois inputs (B1/B2), frames de `molde/timeline.json` e **áudio novo** = hook do original (0–6,40 s) + `vo-zap-ritmo.wav` (concat, AAC 192k). Stand-in de layout a custo zero antes do Pruna: `conferencia/standin-n1.mp4` (clipe n1 das 54–58, boca fora de sync).

## Custo real: US$ 0,87
TTS 0,053 + gpt-image-2/edit 0,067 + Pruna 0,75. Painéis, karaokê, montagem: US$ 0.

## Conferência
`conferencia/final-folha.jpg` (10 instantes), `paineis.jpg`, `varredura-z1.jpg` (clipe inteiro), `varredura-z1-mao.jpg` (9,5–13,5 s: o avatar faz um gesto breve com a mão no canto inferior direito em ~11 s — no bloco de rosto limpo, fora do rosto; ficou como gesto natural).

## Pra fazer outra variação
1. Novo avatar: `elencos/zN.txt` → `base/zN.req.json` (copiar z1.req.json trocando a descrição) → gpt-image-2/edit → upload → `clipes/zN.req.json` → Pruna (US$ ~0,82 no total).
2. `python3 montar-zap.py clipes/zN.mp4 AD02-H2-zap-zN.mp4` (áudio, painéis e karaokê já prontos, custo zero).
Copy nova: editar `roteiro.txt` → TTS → `cortar-pausas-audio.py` → whisper → `gerar-timeline.py` → `gerar-karaoke-zap.py` → `gerar-paineis.sh` (as durações dos painéis vêm da timeline) → Pruna → montar.

## Lote 2 — 4 avatares de nacionalidades diferentes (Gusta, 17/09: "mais 4 variações, personagens diferentes, várias nacionalidades") → peças 60–63

| peça | id | avatar |
|---|---|---|
| **60** | z2 | branco escandinavo ~30, loiro-cinza penteado pra trás, barba rala |
| **61** | z3 | mexicano ~36, bigode grosso e cavanhaque |
| **62** | z4 | indiano ~27, cabelo com risca, barba cheia aparada |
| **63** | z5 | coreano ~31, franja texturizada, sem barba |

Mesma copy, locução, painéis, karaokê e edição da 59 — só o clipe do avatar muda (`montar-zap.py clipes/zN.mp4`). Elencos em `elencos/z2..z5.txt`, imagens `base/z2..z5.png` (`conferencia/elencos.jpg`), clipes `clipes/z2..z5.mp4`, varreduras `conferencia/varredura-z*.jpg`, peças `conferencia/final-z2-z5.jpg`.

**Custo real: US$ 4,02** — 4 imagens (0,27) + **5** clipes Pruna (3,75). O 1º z5 veio com o **celular na mão, dentro do quadro, nos 9 primeiros segundos** (`clipes/z5-v1-celular-na-tela.mp4`): o prompt dizia "phone held steady at arm's length in his LEFT hand, out of frame" e o modelo mostrou o celular. Regerado com prompt **sem mencionar celular** ("both of his arms hang relaxed at his sides, completely out of frame … nothing is held in front of him or shown to the camera", seed 78) — saiu limpo. z2/z3/z4 (seed 77) têm o mesmo gesto breve de mão no canto inferior em ~7 s que o z1; ficou.

**Lição:** no `video_prompt` do Pruna, **não citar o objeto que não deve aparecer** (nem "phone … out of frame"): descrever só a pose visível. Ver memória `pruna-inventa-segunda-pessoa`.
