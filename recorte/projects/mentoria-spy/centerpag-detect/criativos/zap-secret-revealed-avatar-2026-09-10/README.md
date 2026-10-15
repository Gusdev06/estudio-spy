# Lote zap-secret-revealed-avatar — Zap "secret revealed" (934941213003855) com avatar novo · 2026-09-10

Replicar `centerpag-detect/anuncios/secret-revealed-934941213003855.mp4` (720×1280, 30 fps, 32,23 s de vídeo / 32,37 s de áudio) trocando **só o rosto**. Molde UGC puro (teardown do Peneira `centerpag-detect/referencias/2026-09-10-teardown-edicao-secret-revealed.md`): rosto cheio o vídeo inteiro, faixa vermelha de hook fixa no topo, karaokê de 1 palavra, sem card, sem funil, sem CTA. Áudio original em `audio/audio-original.m4a`. Casting em `casting.md`.

## Peça

`pecas/zap-secret-revealed-avatar.mp4` — 1080×1920 · 30 fps · 971 frames · **32,37 s** · H.264 crf 16 bt709 · áudio original (AAC 192k) · 0 silêncios ≥ 0,4 s. Cópia: `CRIATIVOS-PRONTOS/20-ZAP-secret-revealed-avatar-novo.mp4` (linha 20 no LEIA-ME).

Talking head: `clipes/talking-head-secret-omnihuman.mp4` (OmniHuman, 718×1286, 25 fps, 32,12 s, áudio original inteiro, sujeito centrado). Entra escalado a 1080×1934, centrado (y −7), sem deslocamento: a peça é rosto cheio como o original. Os últimos 0,25 s seguram o último frame. **Jump cut do original em 19,33 s: ignorado** — era o ator antigo; o clipe novo é contínuo (registro conforme pedido).

## Molde — `remontar-secret.sh`

```
cd projects/mentoria-spy
bash centerpag-detect/criativos/zap-secret-revealed-avatar-2026-09-10/remontar-secret.sh clipes/<talking-head>.mp4 [--th-x N --zoom F --th-y N --fonte F --tamanho N --tracking N --y N --atraso S]
```

| elemento | medido no original (720×1280) | na peça (×1,5) |
|---|---|---|
| **Faixa vermelha** | duas caixas #B40000 empilhadas, bbox x 90–627 · y 116–257, texto branco condensado caixa alta "HOW TO READ YOUR 📱 / PARTNER'S TEXT MESSAGES", emoji em x 536–602 · y 102–190 | **recortada do original** (x 85–632 · y 110–262) com alfa só nas caixas + emoji → x 127–948 · y 165–393. Idêntica (o Peneira sugeriu redesenhar; o recorte saiu igual, com emoji, então ficou o recorte) |
| **Karaokê** | 1 palavra branca caixa alta, centrada, capitais y 832–874 (cap 42, 65 % da altura); largura "BOYFRIENDS" 423 px (avanço ≈ cap: fonte arredondada, larga); sombra escura suave pra baixo/direita, contorno fino; **troca a cada palavra** (30 fps: 40 trocas em 10 s vs 38 palavras do whisper — o teardown leu a 1 fps e viu ~1/s); legenda − whisper = +0,03 s (mediana de 40 trocas) | faixa de PNGs a 30 fps desenhada em PIL: **Arial Rounded MT Bold 86** (cap 64) + **tracking 7 px** ("BOYFRIENDS" 634 px como o original), traço engrossado (stroke branco 2), borda escura 4 px @43 %, sombra (4,5) blur 3 @59 %; capitais em y 1248; 113 palavras do whisper (`molde/legenda.tsv`), cada uma do seu onset até o onset da próxima; atraso 0 |
| Rosto | quadro cheio, olhos ~35 % | talking head 1080 de largura, centrado |
| CTA / fim | não há; termina no rosto | idem |

Sem Poppins ExtraBold nem a fonte exata do original; Arial Rounded MT Bold (sistema) é a mais próxima em forma e largura entre as disponíveis. Se o Peneira identificar a fonte, é só trocar `--fonte`.

## Conferência

`conferencia/folha-8-instantes.jpg` (original | peça em 0,5 · 2 · 4 · 8 · 12,2 · 20 · 25 · 30 s), `zoom-karaoke-original-x-peca.jpg` (3 palavras, y 1210–1360), `zoom-selo-t2.jpg`. Teste do molde com o próprio original: `conferencia/molde/` (`teste-original.mp4`, `folha-molde-secret.jpg`, `zoom-legenda-original-x-molde.jpg` — a legenda dupla ali é o original queimado + a reproduzida, esperado).

## Custo real

| item | valor |
|---|---|
| imagem-base | US$ 0,06 |
| OmniHuman 0,16 × 32,37 s | US$ 5,18 |
| molde, karaokê, montagem, conferência | US$ 0,00 |
| **total** | **≈ US$ 5,24** |
