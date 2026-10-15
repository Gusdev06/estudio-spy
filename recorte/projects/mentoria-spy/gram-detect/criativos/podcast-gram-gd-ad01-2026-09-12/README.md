# Podcast Gram — o campeão GD-AD01 em formato podcast (2026-09-12)

Pedido do Gusta: "o podcast (peça 06) é da oferta de WhatsApp e deu muita sorte; fazer no mesmo formato pro Instagram, revisando qual é o campeão do Instagram e modelando ele."

**Campeão do Instagram nos registros:** GD-AD01 (`criativos-crus/spy-gram/ads-en/GD-AD01.mp4`) — US$ 4.074 de gasto no print do Gerenciador de 03/09, #1 de 10, 2,5× o segundo. Referência oficial desde a decisão de 03/09 (`decisions/log.md`): o "vencedor do swipe" Sophia Jones eram as nossas peças. Roteiro modelado: `gram-detect/roteiros/2026-09-12-podcast-gram-modelado-gd-ad01.md`. Teardown usado: `gram-detect/referencias/proprios-2026-09-03/01-gd-ad01.md`.

| | Arquivo |
|---|---|
| **Peça** | `PODCAST-GRAM-gd-ad01-funil-musica.mp4` — 1080×1920, 30 fps, 1148 frames, **38,27 s**, H.264 crf 16 bt709, AAC 192k. Cópia: `CRIATIVOS-PRONTOS/33-…` |
| **Versão rápida** | `PODCAST-GRAM-gd-ad01-funil-musica-rapida-1.12x.mp4` — a mesma peça a 1,12× (setpts + atempo, lipsync mantido), **34,17 s**, ~180 wpm. Cópia: `CRIATIVOS-PRONTOS/34-…` |
| Planos | os 3 do podcast Zap (`imagens/p1-two-shot`, `p2-close-host`, `p3-close-guest`; URLs em `imagens/urls.txt`) — custo zero |
| Clipes por cena | `clipes/cena-1..7.mp4` — **Pruna `pruna-ai/p-video/avatar` 720p** (704×1280, 24 fps), imagem do plano + TTS; pedidos em `clipes/cena-N.json` |
| TTS | `audio/host-N.mp3`, `audio/guest-N.mp3` (MiniMax speech-2.6-hd; Wise_Woman host, Calm_Woman convidada; `guest-5-pad` = 3,5 s com silêncio, o modelo recusa áudio curto). URLs em `audio/urls.txt` |
| Whisper | `audio/clip-cena-N.json` (mlx small.en, no áudio embutido do clipe) — fonte da timeline e do karaokê |
| Painéis | `painel/story.mp4` · `card.mp4` · `intercept.mp4` · `fim.mp4` — recortes do próprio GD-AD01 (ver abaixo) |

## Custo real

| item | valor |
|---|---|
| 3 planos | US$ 0 (reaproveitados) |
| TTS 7 falas | ≈ US$ 0,05 |
| Pruna 7 clipes (49 s gerados a US$ 0,025/s) | **US$ 1,125** (billing `key:macbook`, 12/09 07:59 UTC) |
| painéis, montagem, whisper, música, versão rápida | US$ 0 |
| **total** | **≈ US$ 1,20** (o H3 sairia ≈ US$ 5,00; Gusta escolheu Pruna) |

## O que o Pruna fez no two-shot (sonda de 12/09, cenas 5 e 7 antes do lote)

Risco anotado na memória: "anima um rosto só". Com o prompt dizendo **qual** mulher fala ("Only the woman on the LEFT (black blazer) is talking…; the woman on the RIGHT keeps her mouth closed and nods"), o Pruna animou a certa nas duas cenas de two-shot (3: convidada à direita; 7: host à esquerda) e deixou a outra ouvindo. Sonda custou US$ 0,225. Folhas: `conferencia/sonda-cena-5.jpg`, `sonda-cena-7.jpg`.

## Timeline (pausas removidas — regra de 05/09)

Corte no fim da última palavra + 0,3 s; silêncio ≥ 0,4 s dentro da fala fica com 0,25 s (vídeo e áudio juntos). 9 pausas removidas, 2,68 s.

| cena | quem | plano | saída | estado |
|---|---|---|---|---|
| 1 | host | close | 0,00–3,87 | rosto cheio + **caixa** |
| 2 | convidada | close | 3,87–10,33 | rosto cheio + caixa |
| 3 | convidada | two-shot | 10,33–18,53 | **split** · painel story privado |
| 4 | host | close | 18,53–23,77 | rosto cheio |
| 5 | convidada | close | 23,77–26,10 | rosto cheio |
| 6 | host | close | 26,10–34,30 | **split** · card Gram Detect até "the username" (30,57 s), depois LIVE INTERCEPTION |
| 7 | host | two-shot | 34,30–38,27 | **split** · glitch + setas do campeão |

**Cortes em 3,87 · 10,33 · 18,53 · 23,77 · 26,10 · 34,30 s.** 103 palavras em ~35,5 s de fala ≈ 174 wpm (campeão 191; a versão 1,12× fica em ~195).

## Camadas

- **Caixa do gancho** (campeão): frame 0 → 310 (10,33 s), x 106–973 · y 862–1058, #E80052 (#FE0553 no decode), **caixa mista** `I found something I wasn't` / `even looking for...` em Poppins Bold 62 (linha 1 = 844 px), #EFFD11, contorno 2 px + sombra. Caixa mista de propósito: o comparativo de 03/09 mostra slogan em caixa alta como traço dos perdedores; o Zap usou caixa alta.
- **Splits**: rosto = recorte da própria base (1080×1000 em y 240 na cena 3 e y 270 na 6; 1080×1120 em y 200 na 7); painel entra em y 1000 (cenas 3 e 6) e y 1120 (cena 7, o bloco 8 do campeão é mais baixo). Corte seco entre estados.
- **Painéis** (recortes do `GD-AD01.mp4`, sem o karaokê queimado dele): story = 16,5–19,6 s, crop 1080×920 y 500 · card = 8,5–10,5 s, crop y 370 (sem a transição rasgada de 7,8 s) · intercept = 22,3–25,85 s, crop y 1000 (pill "ACCESS IN PROGRESS" + terminal) · fim = 29,25–32,55 s, crop 1080×800 y 1120 (glitch + duas setas brancas já dentro). Cada painel segura o último frame até o fim da cena.
- **Karaokê**: 41 blocos (`molde/karaoke.tsv`), Inter Bold 69, branco com glow, y 1472 nos rostos cheios; y 890 nos splits de painel em 1000; y 1010 na cena 7.
- **Música**: a mesma trilha de suspense do Zap (`podcast-hook-polemico-2026-09-05/audio/musica-7y4kJtkioFk.m4a`) a 9 %, fade in 1 s / out 2,5 s, mixada na montagem (`SEM_MUSICA=1` desliga).
- **Escala**: 704×1280 → 1080×1920 Lanczos (corte lateral de 12 px), 24 → 30 fps.

## Reproduzir

```
bash  gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12/gerar-tts.sh            # 7 TTS (centavos)
bash  gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12/gerar-clipes-pruna.sh   # 7 clipes Pruna (≈ US$ 1,13)  · gerar-clipes.sh = a versão H3 (≈ US$ 5), não rodada
python3 gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12/montar-gram.py [saida] # timeline + karaokê + splits + caixa + música (Y3/Y6/Y7 por env)
```
Tudo de `projects/mentoria-spy/`. Conferência em `conferencia/`: `folha-cenas`, `folha-cortes`, `folha-karaoke` (frame no início de cada bloco), `folha-estados-split`, `folha-paineis`, `dry/` (dry-run com os clipes do Zap, usado pra validar o grafo antes de gastar).

## O que conferir no olho

- Os 9 saltos de pausa dentro da fala (preço da regra de ritmo; `PAUSA_MAX`/`PAUSA_KEEP` por env pra suavizar).
- A cena 5 (convidada pra lente, 2,3 s) é a mais curta: o Pruna começa com ela olhando pro host e vira pra câmera.
- Pruna 720p upscalado 1,53× (o H3 768p era 1,4×): mais macio que o Zap 06. Se incomodar, 1080p custa o dobro.

## Alavancas pra próximos lotes (uma por lote)

Texto da caixa (a mais barata; o Zap fez 5 em US$ 2,30 regerando só a cena 1) · elenco novo (3 planos, US$ 0,20 + 7 clipes) · pronome "his" em vez de "their" · faixa fixa o vídeo inteiro · painel com b-roll de casal (L9) no lugar do split.

## var5 — 5 variações de hook (Gusta, 12/09: "ficou bom, faça 5 versões")

Mesma peça da 33, mudando **só a cena 1** (fala nova da host + texto da caixa) e o karaokê dessa cena. Cenas 2–7, painéis, setas, música e o karaokê delas ficam idênticos — só deslocados pelo tamanho novo da cena 1. Conferido por PSNR nos mesmos offsets das cenas 3, 4, 6 e 7: vários frames batem bit a bit (`inf`), o resto fica em 44–46 dB, que é ruído de quantização do x264 (o GOP muda porque a cena 1 tem outra duração), não diferença de conteúdo.

Regra dos ganchos (do teardown do GD-AD01): caixa é **confissão em caixa mista com reticências**, nunca slogan em caixa alta; a fala da host é a **regra geral / curiosidade** e não repete a caixa; pronome neutro ("their"), sem "hack", "spy", "senha" nem nome do produto.

| var | caixa (Poppins Bold) | fala nova da host (cena 1) | cena 1 | peça | arquivo |
|---|---|---|---|---|---|
| v1 | `I kept thinking I'd be` / `the first to know...` (62) | "If something's going on, would you be the first to find out? Or the last?" | 141 fr · 4,70 s · 1 pausa cortada | 1173 fr · 39,10 s | `var5/PODCAST-GRAM-v1-first-to-know.mp4` |
| v2 | `You know when something` / `just feels off...` (58) | "Some people ask for their partner's phone. People who know where to look never have to ask." | 163 fr · 5,43 s · 1 pausa | 1195 fr · 39,83 s | `var5/PODCAST-GRAM-v2-feels-off.mp4` |
| v3 | `It was right there on` / `their profile the whole time...` (56) | "Almost nobody knows where Instagram keeps the answer." | 101 fr · 3,37 s | 1133 fr · 37,77 s | `var5/PODCAST-GRAM-v3-right-there-on-their-profile.mp4` |
| v4 | `I stopped guessing in` / `about three minutes...` (62) | "There's one thing on Instagram that ends the guessing." | 93 fr · 3,10 s | 1125 fr · 37,50 s | `var5/PODCAST-GRAM-v4-stopped-guessing.mp4` |
| v5 | `Everyone leaves a trail.` / `Even them...` (62) | "People hide a lot worse on Instagram than they think." | 97 fr · 3,23 s | 1129 fr · 37,63 s | `var5/PODCAST-GRAM-v5-everyone-leaves-a-trail.mp4` |

Herança: v1 vem do gancho do GD-AD05 ("I kept thinking I would be the first to know…", US$ 307), v2 do GD-AD04 ("You know when something just feels off…", US$ 611) — os dois validados no mesmo print de 03/09; v5 reaproveita a linha do `gram01-l9-en-02`, aqui em caixa mista. v3 e v4 são novos (lugar do rastro; tempo pra parar de adivinhar).

**Custo real: US$ 0,657** — 5 TTS (US$ 0,032) + 5 clipes Pruna da cena 1 (US$ 0,625), billing `key:macbook` de 12/09. Montagem, whisper e conferência: zero.

Cópias em `CRIATIVOS-PRONTOS/35`–`39`. Conferência em `var5/conferencia/`: `caixas-5-variacoes.jpg`, `folha-cena-1-5-variacoes.jpg`, `resumo.tsv`.

### Reproduzir
```
bash    gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12/var5/gerar-var.sh [v1 …]   # TTS + clipe da cena 1 + whisper (≈ US$ 0,13/variante)
python3 gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12/var5/montar-var.py [v1 …]  # monta (custo zero)
```
Hooks novos: acrescente a linha em `var5/hooks.tsv` (caixa em 2 linhas, fontsize que caiba em 828 px, fala, blocos do karaokê em JSON, slug) e rode os dois. `montar-gram.py` aceita `CAIXA_L1/CAIXA_L2/BOXSZ/CLIPES/AUD/TL/KAR/KDIR/BLOCOS1` por env — foi assim que as variantes reusaram o molde sem duplicar código. Regressão: remontar a 33 com os scripts parametrizados dá md5 idêntico ao entregue.
