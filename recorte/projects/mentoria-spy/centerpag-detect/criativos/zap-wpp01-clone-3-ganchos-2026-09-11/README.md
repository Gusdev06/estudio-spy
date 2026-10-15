# Lote zap-wpp01-clone-3-ganchos — clone do wpp-01 Esther Vicman em 3 ganchos, molde L10 (2026-09-11)

Oferta Spy Zap (go.centerpag.com / go.zappdetect.com). Peça modelada: **wpp-01 Esther Vicman**, ad `1762552938111855`, #1 de 87, 16,1 dias — `centerpag-detect/escalados/whatsapp/01-esther-vicman-1762552938111855.mp4` (56,77 s · 360×640 · 30 fps · md5 `31d9b6a30c53905c1ae2ac57f1a9b830`). Teardown de edição: `centerpag-detect/referencias/2026-09-01-teardown-edicao-wpp01-esther-vicman.md`. Molde L10 (card alfa sobre plano único) copiado do lote EX `zap-ex-presente-hook-2026-09-05/` — medidas em `molde/README-l10.md`.

**Alavanca: GANCHO.** Muda o matte do topo (2 linhas amarelas) **e** o bloco 1 falado (~5 s). Blocos 2–7 idênticos em texto e áudio. H1 = clone fiel (`WHAT THEIR / WHATSAPP IS HIDING...`); H2/H3 = do Peneira/Isca (roteiro em `centerpag-detect/roteiros/2026-09-11-wpp01-clone-3-ganchos/`, ainda não entregue em 11/09 00:5x). Voz masculina EN, avatar masculino. Alvo 35–40 s sem pausas; rosto sai em ~55 %.

## Estado — fase C: PEÇAS FINAIS PRONTAS (custo real do lote: US$ 1,7445 = fase B 0,1445 + Pruna 1,60)

| | |
|---|---|
| ✓ estrutura + scripts adaptados do EX (fase A) | `remontar-l10.sh/.py`, `karaoke-l10.py` (matcher corrigido 11/09), `cortar-pausas.py`, `conferir-lote.py`, `conferir-audio.sh` |
| ✓ prova do molde a custo zero (fase A) | `conferencia/standin-ex-{base,H1}.mp4` — md5 da base bate com a do EX (`276d4c7c…`) |
| ✓ medição do original (fase A) | `conferencia/original/`, `original-folha-fases.jpg`, `original-zoom-matte.jpg` |
| ✓ roteiro (Isca) | `roteiros/2026-09-11-wpp01-clone-3-ganchos/{corpo,h1,h2,h3}.txt` (104 + 18/18/18 palavras; corpo md5 `c7340fbd…`) |
| ✓ áudio (TTS MiniMax, 4 chamadas, US$ 0,0875) | `audio/{corpo,h1,h2,h3}.mp3` → `audio/locucao-H{1,2,3}.wav` (corpo bit-idêntico nas 3) |
| ✓ avatar (GPT Image 2, 1 chamada, US$ 0,057) | `base/avatar-wpp01.png` 941×1672 |
| ✓ stand-ins completos no molde (custo zero) | `conferencia/standin-wpp01-H{1,2,3}.mp4` + folhas, mattes, zooms |
| ✓ estimativa do lipsync | (a) só rosto **US$ 1,60** · (b) head inteiro US$ 2,875 — Gusta liberou a (a), teto US$ 2,00 |
| ✓ lipsync Pruna (3 chamadas, **US$ 1,60 real**) | `clipes/talking-head-H{1,2,3}.mp4` (704×1280 · 24 fps · ~21 s) — seção "Peças finais" |
| ✓ peças finais (custo zero) | `pecas/zap-wpp01-H{1,2,3}.mp4` · 0 silêncios · rosto sai 51,6 / 53,9 / 52,1 % |

## Fase B — o que foi feito (11/09, 01:09–01:35 local; Bisturi)

### (a) TTS — `minimax/speech-2.6-hd`, voz `Casual_Guy`, speed 1.15 (US$ 0,0875)

`emotion=neutral language_boost=English english_normalization=true format=mp3 sample_rate=44100 bitrate=128000 channel=1`. Preço conferido antes com `wavespeed price` (corpo 0,0586 · hook 0,0097). `Casual_Guy` foi a primeira opção do Maestro (controle do wpp-01 no lote 4, a mais UGC); ficou porque o wpm efetivo depois do corte de pausas passou de 175 (regra: abaixo disso trocaria pra `Determined_Man`).

| arquivo | id | duração | fala (1ª–última amostra > −35 dB) | palavras | wpm cru / sobre a fala |
|---|---|---|---|---|---|
| `audio/corpo.mp3` | `34bd9e22…` | 32,84 s | 32,41 s | 104 | **190** / 193 |
| `audio/h1.mp3` | `44f5c1fb…` | 4,10 s | 3,61 s | 18 | 265 / 299 |
| `audio/h2.mp3` | `686ce883…` | 5,75 s | 5,39 s | 18 | 189 / 200 |
| `audio/h3.mp3` | `756f8496…` | 4,44 s | 3,99 s | 18 | 245 / 270 |

`audio/locucao-HN.wav` = hN + 0,25 s de silêncio + corpo (ffmpeg concat, pcm 44,1 kHz mono). **Cauda dos 3 wavs == `corpo.mp3` decodificado, amostra por amostra (numpy `array_equal` True nas 3)**; cabeça == hN.mp3; miolo = 11025 amostras = 0,250 s.

| locução | wav | silêncios ≥ 0,4 s (−35 dB) | sem pausas (0,25 s cada) | wpm efetivo (122 palavras) | whisper |
|---|---|---|---|---|---|
| H1 | 37,149 s | 11 (−3,02 s) | 34,13 s | **214** | 121 tokens, todas as palavras (whisper junta "every one" → "everyone") |
| H2 | 38,786 s | 11 (−2,87 s) | 35,92 s | **204** | idem |
| H3 | 37,486 s | 11 (−2,94 s) | 34,55 s | **212** | idem |

Whisper local dos wavs crus: `molde/locucao-HN-16k.{wav,json}`.

**Divergências medidas (pro Maestro decidir; não regerei nada por conta):**
1. **Duração das 3 não é igual ±0,3 s**: a voz leu as 18 palavras do bloco 1 em 3,61 / 5,39 / 3,99 s (h1 e h3 a 265–299 wpm, h2 a 189–200). Diferença máxima entre as peças: 1,85 s (H2 − H1). O corpo é idêntico; só o bloco 1 varia. Opção barata: regerar h1 e h3 a `speed=1.0` (≈ US$ 0,02) — aproxima, não iguala.
2. **wpm efetivo 204–214, acima do alvo 180–200** (o corpo cru está em 190; o `cortar-pausas.py` comprime pra ~200+). É o mesmo comportamento do EX (197 efetivo).
3. **Rosto sai em 51,5 % no H1** (alvo 52–57 %) — consequência do h1 curto; H2 53,9 % e H3 52,1 % dentro.

### (b) Avatar — `openai/gpt-image-2/text-to-image` 9:16 · 1k · medium · png (US$ 0,057 cobrado)

`base/avatar-wpp01.png` (941×1672, id `28d3c58c…`, prompt em `base/avatar-wpp01-prompt.txt`, 79 s). Da ficha do Peneira (§5 do plano): homem ~32, branco, cabelo curto castanho-avermelhado com entradas, barba cheia curta da mesma cor, olhos claros, track jacket preta com friso branco na gola/ombros sobre camiseta cinza, sofá, parede cinza-esverdeada, teto visível com luminária branca redonda no canto superior esquerdo, celular abaixo dos olhos apontando pra cima, luz fraca fria e subexposta, boca fechada, sobrancelha levemente franzida, olhando pra lente, mãos fora. Sem texto, logo ou defeito → **não precisou regerar**. Olhos em y ≈ 555 (33 % da altura). Luz fria (ficha), não o abajur quente do rascunho do plano.

### (c) Stand-ins completos — custo zero

```
ffmpeg -loop 1 -i base/avatar-wpp01.png -i audio/locucao-HN.wav -vf "scale=704:1280:force_original_aspect_ratio=increase,crop=704:1280" -r 25 … conferencia/standin-HN.mp4
python3 cortar-pausas.py conferencia/standin-HN.mp4 conferencia/standin-HN-sem-pausas.mp4      # molde/pausas-standin-HN-sem-pausas.json
ffmpeg -i conferencia/standin-HN-sem-pausas.mp4 -ac 1 -ar 16000 molde/clipe-HN-16k.wav && mlx_whisper … → molde/clipe-HN-16k.json
python3 karaoke-l10.py molde/clipe-HN-16k.json molde/karaoke-HN.tsv --blocos molde/karaoke-blocos-HN.txt   # 45 blocos, 0 avisos
bash remontar-l10.sh conferencia/standin-HN-sem-pausas.mp4 molde/blocos-HN.tsv molde/hooks-HN.txt molde/karaoke-HN.tsv conferencia/standin-wpp01-HN --off-head 240
```

`karaoke-l10.py` ganhou um casamento mais estrito (exato, ou prefixo só com token ≥ 3 letras / palavra do whisper ≥ 4; sobra de palavra colada casa com o token seguinte): o antigo casava "one" (de "every one") com o "on" de "going on" e perdia 25 linhas. `molde/karaoke-blocos-HN.txt` = quebras sugeridas pelo Isca (§5).

**Fronteiras (`molde/blocos-HN.tsv`)**: o corpo é o mesmo áudio nas 3, então as fronteiras dos blocos 2–7 foram calculadas UMA vez, relativas ao início do corpo (mediana das 3 whispers − min(0,1 s; gap/2); spread entre whispers 0,03–0,5 s), e deslocadas pelo início do corpo em cada clipe sem pausas (`molde/fronteiras-corpo.json`: H1 3,917 · H2 5,702 · H3 4,333 s). Blocos 2–7 têm a **mesma duração nas 3 peças**: B2 5,74 · B3a 3,20 · B3b 1,52 · B4 3,18 · B5a 3,72 · B5b 3,22 · B6a 2,10 · B6b 1,00 · B6c 1,58 · B7 4,92 s. B6c ("it's impossible. It's not.") começa uma frase antes do roteiro pra Dating Profiles durar ≥ 1 s.

| | H1 | H2 | H3 |
|---|---|---|---|
| clipe sem pausas | 34,14 s | 35,93 s | 34,55 s |
| bloco 1 (gancho) | 0–3,96 | 0–5,74 | 0–4,37 |
| **rosto sai** (início de B5a "Because the truth…") | **17,60 s = 51,5 %** | **19,38 s = 53,9 %** | **18,01 s = 52,1 %** |
| whisper "because" no clipe sem pausas / no wav cru | 17,60 / 19,86 | 19,40 / 21,44 | 18,18 / 19,98 |
| peça `conferencia/standin-wpp01-HN.mp4` | 1080×1920 · 30 fps · 1024 fr · 34,15 s | 1078 fr · 35,99 s | 1036 fr · 34,64 s |
| silêncios ≥ 0,4 s (−35 dB) | 0 | 0 | 0 |
| md5 | `faddb2be…` | `a04269ee…` | `06f67357…` |

`--off-head 240`: olhos do avatar em y ≈ 652 no clipe escalado a 1080 → y ≈ 700 na peça (calibração do EX; campeão 690–750). Comparação em `conferencia/…` (o campeão tem a cabeça um pouco maior e encostada na matte; o nosso tem ~70 px de ar — o molde não escala o clipe; fica registrado).

**Trechos da gravação corrigidos em relação ao EX (medido frame a frame, `EDIÇÃO/EDIÇAO ANIMADA/…MP4`):**
- **B5a começa em rec 144,1** (EX: 145,0). Com 3,72 s o bloco chegaria a 148,7: em 148,4 a tela já vira "Accessing… Initializing" e em **148,8 o terminal escreve "whatspy v4.7.2"** (palavra proibida). De 144,1 a 148,0 é Restoring 95 % → Backup decrypted!, número e campo dentro dos blurs.
- **B5b começa em rec 153,6** (EX: 153,3). Em 153,0–153,3 o terminal ainda mostra "[OK] Account matched: 5527999546872" (o README-l10 dizia 151,5–152,5). Em 153,5 a linha já rolou. 153,6–156,8: terminal limpo → BACKUP RECOVERED → HIDDEN DATA DETECTED, sem PII.
- **Blur do formulário (B2) ampliado pra `450:633:580:178`** (EX: `690:633:340:178`). O campo do número começa em x ≈ 450 da gravação; com o blur do EX os 4 primeiros dígitos ("2799") ficam legíveis por ~1 s. → **Pro Maestro: as peças EX A/B/C provavelmente carregam esses dois vazamentos (dígitos em B2 por ~1 s; número no terminal por ~0,2 s em B5b). Medido na gravação, não conferido nas peças EX (não são minhas).**

Conferência visual (todas olhadas): `conferencia/folha-standin-HN.jpg` (8 instantes: gancho, form, accessing, último com rosto, rosto sai, terminal, scan, CTA), `matte-HN.jpg` + `mattes-h123.jpg` (Poppins Bold 86, topos 70/157, #EEFF00 com contorno), `card-t0.5-HN.jpg` (primeiro card = tela Chats, sem número/nome no quadro), `zoom-blur-B2-B3a-B4-HN.jpg` (campo do número, número vermelho e card de perfil desfocados). Mapa TRACKING fora de todos os recortes (começa em rec y ≈ 1631; crop 110:1600 e card visível até y ≈ 1297).

### (d) Estimativa do lipsync — Pruna `pruna-ai/p-video/avatar`, US$ 0,025/s de áudio, ceil por chamada

| forma | H1 | H2 | H3 | total |
|---|---|---|---|---|
| **(a) só o trecho com rosto** = ceil(s até "because" no wav cru + 0,5) | ceil(19,86+0,5) = 21 s → 0,525 | ceil(21,44+0,5) = 22 s → 0,550 | ceil(19,98+0,5) = 21 s → 0,525 | **US$ 1,60** |
| **(b) head inteiro** = ceil(duração do wav) | 38 s → 0,950 | 39 s → 0,975 | 38 s → 0,950 | **US$ 2,875** |

`wavespeed price pruna-ai/p-video/avatar --upload` (sem cobrança; upload em cache 24 h) confirmou a forma (b): **0,95 / 0,975 / 0,95**. Na forma (a) o clipe volta só até B4; o resto do áudio (blocos 5–7, sem rosto) precisa ser reanexado ao clipe antes do `cortar-pausas.py` (o molde copia o áudio do talking head): cortar o wav em `ceil(because+0,5)`, gerar, depois `concat` do áudio restante com tpad do último frame — mais um passo, US$ 1,28 a menos. OmniHuman só se o Pruna falhar no rosto (0,16/s → US$ 18,4 na forma b).

Custo real da fase B (`wavespeed billings | grep macbook`, 11/09 18:09–18:11 UTC): 0,0586 + 0,0097 + 0,0095 + 0,0097 + 0,0570 = **US$ 0,1445**. Saldo da conta compartilhada: 23,06 antes → 22,07 depois (o resto é `key:tes`, não é nosso). Uploads do `price` não cobraram (`audio/billings-antes.txt`, `audio/billings-depois.txt`).

### (e) Pronto pra disparar — SÓ COM O SIM DO GUSTA (forma b, 3 chamadas, US$ 2,875)

```
cd projects/mentoria-spy; L=centerpag-detect/criativos/zap-wpp01-clone-3-ganchos-2026-09-11
IMG=$(wavespeed upload $L/base/avatar-wpp01.png --json | jq -r '.[0].url // .url')       # mesmos bytes → mesma URL do price (cache 24 h)
for N in H1 H2 H3; do                                                                        # UMA por vez; wavespeed billings | head -5 entre cada
  wavespeed run pruna-ai/p-video/avatar -i image="$IMG" -i audio=@$L/audio/locucao-$N.wav -i resolution=720p \
    -i video_prompt="The person is talking to the camera, looking into the lens, natural small head movements, hands out of frame." \
    --download "$L/clipes/talking-head-$N.mp4" --json > "$L/clipes/$N.out.json" 2> "$L/clipes/$N.log"
done
# depois, por variante (custo zero) — mesmas fronteiras dos stand-ins se o Pruna devolver o áudio de entrada intacto (conferir):
cd $L
python3 cortar-pausas.py clipes/talking-head-H1.mp4 clipes/talking-head-H1-sem-pausas.mp4
bash conferir-audio.sh clipes/talking-head-H1-sem-pausas.mp4 conferencia/standin-H1-sem-pausas.mp4        # envelope ≥ 0,9, |desloc| ≤ 0,05 s → blocos-H1.tsv e karaoke-H1.tsv valem
bash remontar-l10.sh clipes/talking-head-H1-sem-pausas.mp4 molde/blocos-H1.tsv molde/hooks-H1.txt molde/karaoke-H1.tsv pecas/zap-wpp01-H1 --off-head 240   # medir olhos no clipe; 704×1280 = mesma geometria do stand-in
# H2, H3 idem · conferência: silencedetect 0 · BLOCOS=molde/blocos-H1.tsv python3 conferir-lote.py pecas/zap-wpp01-H1.mp4 (ajustar tp pros tempos deste lote)
```
URLs já hospedadas (válidas até ~12/09 01:30 local): imagem `…/images/1789064851121230299_gF5eoxHO.png`, áudios H1 `…/audios/1789064877473433271_qQE7uThh.wav`, H2 `…1789064884317004161_9LUaS1bk.wav`, H3 `…1789064891873310845_hTAJT3bk.wav` (prefixo `https://d2h7xmz5gqybh9.cloudfront.net/media/cc96ac48027e40ab8f92189bbfcd32c9/`).

## Peças finais — fase C (11/09, 01:54–02:20 local; Bisturi)

| peça | matte | duração · frames | rosto sai (B5a) | silêncios ≥ 0,4 s | md5 |
|---|---|---|---|---|---|
| `pecas/zap-wpp01-H1.mp4` | `WHAT THEIR / WHATSAPP IS HIDING...` | 34,13 s · 1024 fr | **17,61 s = 51,6 %** | 0 | `68ce1517…` |
| `pecas/zap-wpp01-H2.mp4` | `SEE THIS BEFORE / IT'S TOO LATE.` | 36,00 s · 1080 fr | **19,40 s = 53,9 %** | 0 | `ab075c45…` |
| `pecas/zap-wpp01-H3.mp4` | `SICK AND TIRED / OF THE LIES?` | 34,57 s · 1037 fr | **18,02 s = 52,1 %** | 0 | `1cd7d12e…` |

1080×1920 · 30 fps · H.264 crf 16 bt709 · AAC (áudio = o do head estendido, copiado). `-base.mp4` (crf 10, sem hook) ao lado de cada uma, só pra regerar o matte. Posters `pecas/zap-wpp01-HN-poster.jpg`.

### Custo real do Pruna (`wavespeed billings | grep macbook`, 11/09 18:56–19:00 UTC)

| chamada | áudio enviado | prediction | cobrado | tempo |
|---|---|---|---|---|
| H1 | `audio/locucao-H1-rosto.wav` 20,43 s (wav cru até 19,86 + 0,5) | `9f823355927f49d29d61edbe4b60c8b6` | **US$ 0,525** | 120 s |
| H2 | `audio/locucao-H2-rosto.wav` 21,98 s (21,44 + 0,5; o primeiro corte a 22,01 s cotava 23 s = 0,575 — recortado pra ficar em 22 s) | `6b47ebea15294a48ad1c50319effde98` | **US$ 0,55** | 68 s |
| H3 | `audio/locucao-H3-rosto.wav` 20,53 s (19,98 + 0,5) | `9d438581847146e5a3c79dd483ae383f` | **US$ 0,525** | 53 s |
| **fase C** | | | **US$ 1,60** (= estimativa; teto 2,00; nenhuma repetição) | |
| **lote** | fase B 0,1445 + fase C 1,60 | | **US$ 1,7445** | |

Saldo da conta compartilhada: 21,47 antes → 19,05 depois (a diferença além dos nossos 1,60 é `key:tes`). `wavespeed price --upload` cotou 0,525 / 0,55 / 0,525 antes de disparar (`audio/billings-fase-c-{antes,depois}.txt`). Imagem: `clipes/upload.json` (mesma URL do cache da fase B). Comando: o do README (seção e), com `-i audio=@audio/locucao-HN-rosto.wav`, 720p, video_prompt "The person is talking to the camera, looking into the lens, natural small head movements, hands out of frame." Saídas: `clipes/talking-head-HN.mp4` + `HN.out.json` + `HN.log`.

### Talking heads (olhados frame a frame: início, meio, fim + zoom na boca)

| | H1 | H2 | H3 |
|---|---|---|---|
| ffprobe | 704×1280 · **24 fps** (não 25) · vídeo 21,04 s / áudio 20,43 s | 704×1280 · 24 fps · 22,04 / 21,98 s | 704×1280 · 24 fps · 21,04 / 20,53 s |
| rosto | íntegro, boca sincronizada, fecha a boca no fim | íntegro, dentes visíveis, ainda falando no fim | íntegro; **mãos entram no quadro em ~9–11 s** (gesto natural, 5 dedos, sem deformação) apesar do prompt |
| Pruna × wav cru (envelope) | 1,000 · 0,00 s | 1,000 · 0,00 s | 1,000 · 0,00 s |

O vídeo do Pruna sai ~0,6 s mais longo que o áudio (último frame parado). Frames em `clipes/talking-head-HN-frames.jpg`. H3 não foi regerado: custaria mais 0,525 e passaria do teto; na peça as mãos aparecem por ~2 s no B2 dos lados do card (parcialmente atrás dele) — **decisão do Maestro** se vale US$ 0,525 pra tentar de novo.

### Montagem (custo zero) e o que mudou em relação ao fluxo dos stand-ins

1. **Head estendido** `clipes/talking-head-HN-ext.mp4` = vídeo do Pruna + `audio/locucao-HN.wav` inteiro (`-map 0:v -map 1:a`, `tpad=stop_mode=clone` até o fim do wav, `-t` na duração do wav; crf 12, AAC 256k). Envelope ext × wav cru: deslocamento 0,00 s em todas as janelas de 4 s → sem `-itsoffset`. O trecho depois do rosto é frame parado, coberto pelo card cheio/bleed/CTA.
2. **Corte de pausas**: 11 silêncios ≥ 0,4 s nas 3, cortes idênticos aos dos stand-ins (desvio 0,0 s). **Achado:** com vídeo a 24 fps o `concat` usa a duração do vídeo por segmento (múltiplo de 1/24 s) e o áudio ganhava um buraco de até 1 frame por corte — no H1 a peça derivava **+0,11 s** em relação ao stand-in (medido por janela). `cortar-pausas.py` ganhou `SNAP_FPS=24`: cada corte é encaixado na grade de frames antes de cortar vídeo e áudio juntos → vídeo e áudio com a mesma duração (34,11 · 36,00 · 34,58 s). A pausa mantida fica em 0,25 ± 0,02 s. `molde/pausas-talking-head-HN-sem-pausas.json`.
3. **Whisper** dos clipes cortados → `molde/head-HN-16k.{wav,json}` (121 palavras nas 3, iguais ao roteiro).
4. **Fronteiras** recalculadas pelo mesmo método da fase B (mediana das 3 whispers relativa ao início do corpo − min(0,1; gap/2), `molde/fronteiras-corpo-head.json`) → `molde/blocos-HN.tsv` (versão dos stand-ins guardada em `blocos-HN-standin.tsv`). Delta vs stand-ins ≤ 0,08 s. Blocos 2–7 com a mesma duração nas 3 (±0,01 s): B2 5,72 · B3a 3,23 · B3b 1,50 · B4 3,20 · B5a 3,71 · B5b 3,14 · B6a 2,14 · B6b 1,02 · B6c 1,56.
5. **Karaokê** `karaoke-l10.py molde/head-HN-16k.json molde/karaoke-HN.tsv --blocos molde/karaoke-blocos-HN.txt` (45 linhas, 0 avisos; anterior em `karaoke-HN-standin.tsv`). A linha "BECAUSE THE TRUTH" do H1 começava 0,03 s antes da fronteira B5a e o molde a desenhava no y do card (1539) em vez do y do card cheio (927) — início preso à fronteira (17,58 → 17,61). H2/H3 já batiam.
6. **`--off-head 240`** (medido: olhos do Pruna em y ≈ 635–660 no clipe escalado a 1080, iguais aos do avatar parado → y ≈ 690–720 na peça, conferido com grade; campeão 690–750).
7. `remontar-l10.sh clipes/talking-head-HN-sem-pausas.mp4 molde/blocos-HN.tsv molde/hooks-HN.txt molde/karaoke-HN.tsv pecas/zap-wpp01-HN --off-head 240` — ~38 s por variante.

### Conferência (todas as imagens olhadas)

- `conferencia/folha-final-HN.jpg` — 8 instantes (gancho, form, accessing, último com rosto, rosto sai, terminal, scan, CTA). H1: matte + head do Pruna falando, card alfa sobre a jaqueta, karaokê no card, card cheio em 17,9 s com "BECAUSE THE TRUTH" no meio, terminal, scan com blur, CTA borrado com chevrons. H2: idem, deslocado 1,8 s. H3: idem; no "form B2" (7,2 s) as mãos do avatar aparecem dos dois lados do card.
- `conferencia/mattes-final-h123.jpg` — 3 mattes, Poppins Bold 86, topos 70/157, texto centrado, contorno preto.
- `conferencia/card-final-t0.5-HN.jpg` — primeiro card = tela Chats ("257 deleted messages recovered!" + contadores), sem nome/número; karaokê "IF YOU THINK" sobre o card.
- `conferencia/zoom-blur-final-B2-B3a-B4-HN.jpg` — campo do número desfocado (só "+55" e a bandeira legíveis), número vermelho do Accessing desfocado, foto/número do card de perfil desfocados; "Serra, Espírito Santo" é do funil.
- `conferencia/zoom-cheio-B5a-B5b-HN.jpg` — card cheio: "BECAUSE THE TRUTH" no meio (y 927) nas 3; no B5b o funil mostra "9█-███" (mascaramento do próprio funil, já presente nos stand-ins e no EX) sob "EVERY MESSAGE".
- **Silêncios ≥ 0,4 s (−35 dB): 0 · 0 · 0.**
- **Mesmo áudio nos blocos 2–7** (envelope a partir do início do corpo, `conferir-audio.sh --ini-clipe/--ini-ref`): H3 × H1 correlação 0,973, deslocamento −0,05 s constante; H2 × H1 0,92 → 0,75 por janela com deriva −0,01 → −0,10 s a partir do B5a — é o encaixe das pausas na grade de 24 fps, que difere por variante (até 1/24 s por corte); o áudio é o mesmo, com offsets ≤ 0,10 s. A correlação inteira H2 × H1 (0,594) cai por causa dessa deriva, não por diferença de locução.

### Pendências pro Maestro (fase C)

- H1 rosto sai em 51,6 % (alvo 52–57) — herdado do h1 curto (fase B).
- H3: mãos por ~2 s no B2. Regerar = US$ 0,525 (acima do teto atual).
- Deriva de até 0,10 s entre os corpos de H2 e H1 (grade de 24 fps) — não afeta o lipsync de cada peça (vídeo e áudio cortados juntos), só a comparação entre peças.
- `9█-███` no B5b é do funil, não é vazamento nosso.

## Prova do molde (stand-in do EX, 11/09 00:58)

```
bash remontar-l10.sh ../zap-ex-presente-hook-2026-09-05/clipes/talking-head-ex-omnihuman-sem-pausas.mp4 \
  molde/blocos-standin-ex.tsv molde/hooks-standin-ex.txt molde/karaoke-standin-ex.tsv conferencia/standin-ex --off-head 240
```
Mesmas entradas do EX (clipe sem pausas, `blocos.tsv` e `karaoke.tsv` copiados como `*-standin-ex.*`, gravação do funil, setas, crf 10) → `conferencia/standin-ex-base.mp4` **md5 `276d4c7c1250eb79237cac5a138a768e` = `zap-ex-presente-base.mp4`** (bit a bit). `standin-ex-H1.mp4`: 1080×1920 · 30 fps · 939 frames · 31,30 s · 0 silêncios ≥ 0,4 s. Folha em `conferencia/folha-standin.jpg` (8 instantes: matte H1, card alfa sobre a avatar do EX, karaokê, card cheio, payoff, CTA). 45 s de render. O pipeline copiado está intacto; só mudam prefixo de saída e gravação padrão (`EDIÇÃO/EDIÇAO ANIMADA/…`, md5 `08183dfe494a3120462b9f398819a165`, idêntica à cópia em `EDIÇÃO 3/`).

Hook H1 em Poppins Bold 86, topos 70 / 157 (bloco centrado no matte — mesmo cálculo do EX; o campeão tem 75 / 162).

## Medição do original — fronteiras e matte (11/09)

Frames em `conferencia/original/frame-{0.5,8.8,30.8,40.0,49.0,54}s.png` (fronteiras do teardown: 0,03 · 8,80 · 30,77 · 40,00 · 49,03 s). Folha `conferencia/original-folha-fases.jpg` confirma as 5 fases: F1 chats com rosto · F2 acesso com rosto · F3 terminal em tela cheia, **rosto fora em 30,8 s** · F4 payoff (Unlock 09:59) · F5 CTA (09:40) · fim.

**Matte do topo** — 58 frames (1–30 s, 2 fps), luminância em numpy, colunas de margem x 0–30 e 330–360 (fora do texto):

| medida | valor | teardown (01/09) |
|---|---|---|
| fração de pixels com luma < 20, frame médio: 100 % até | **y = 93** | y = 96 ("100 % preta até y96") |
| idem, frames isolados com luma < 16 (t 0,5 / 8,8 s) | y = 87 / 89 | — |
| 5 colunas (x 5 / 15 / 180 / 345 / 355), última linha < 20 | 93 / 94 / 103 / 103 / 101 | — |
| matte pura (y 0–20): luma média · std temporal | 0,0 · 0,03 | — |
| **std temporal em y 85–95** (margens) | **1,7 → 2,5** | — |
| std temporal: 10 % / 50 % / 90 % do platô (17,0 em y 130–200) | y 67 / **125** / **141** | — |
| penhasco (argmax do diff) na variância e na luminância, janela y 80–125 | **não existe** — margens 1,01–1,19×; o argmax cai em y 113–125 conforme a coluna | — |

**Leitura:** a borda "100 % preta" fica em **y 93 (±3, depende do limiar)** — o 96 do teardown está dentro da mesma faixa (`README-l10.md` já anotava 91–97); **não é divergência que mude o molde (288 em 1080p = y 96 ×3).** O achado novo é outro: **a matte não é degrau, é fade.** Abaixo do texto o vídeo já aparece atenuado a partir de ~y 80 (std temporal 50–80× a da matte pura em y 85–95; no zoom ×8 com luma ×6, `original-zoom-matte.jpg`, a silhueta do microfone/abajur atravessa as linhas de y 90–96 até quase o texto) e só chega a 90 % do movimento pleno em **y ≈ 141**. Nosso molde corta seco em 288. Fica registrado pro Maestro/Peneira; **não apliquei** (o molde duro já rodou nas peças EX A/B/C e este lote varia uma alavanca só). Se quiserem aproximar na fase B: trocar o `pad … :black` do `[actor]` por um gradiente preto de y 240 → 420 (1080p) — uma linha no `remontar-l10.py`, custo zero.

## Arquivos

- `molde/hooks.txt` — **definitivo**: H1 `WHAT THEIR|WHATSAPP IS HIDING...` · H2 `SEE THIS BEFORE|IT'S TOO LATE.` · H3 `SICK AND TIRED|OF THE LIES?`; `hooks-HN.txt` = uma linha cada (entrada do `remontar-l10.sh`). `hooks-standin-ex.txt` = só H1, da prova da fase A.
- `molde/blocos-HN.tsv` (fronteiras + trechos + blur por variante), `karaoke-HN.tsv` (45 blocos), `karaoke-blocos-HN.txt` (quebras do Isca), `clipe-HN-16k.{wav,json}` (whisper do clipe sem pausas), `locucao-HN-16k.{wav,json}` (whisper do wav cru), `pausas-standin-HN-sem-pausas.json`, `fronteiras-corpo.json`. `blocos-standin-ex.tsv`/`karaoke-standin-ex.tsv` = cópias do EX da prova. `setas/`, `README-l10.md`, máscaras e `k/` do script.
- `audio/` — `corpo|h1|h2|h3.{mp3,json,log}`, `locucao-H{1,2,3}.wav`, `billings-antes.txt`, `billings-depois.txt`.
- `base/` — `avatar-wpp01.{png,json,log}`, `avatar-wpp01-prompt.txt`.
- `conferencia/` — `standin-HN.mp4` (avatar parado + wav, 704×1280), `standin-HN-sem-pausas.mp4`, `standin-wpp01-HN{-base,}.mp4` (peças stand-in no molde) + `-poster.jpg`, `folha-standin-HN.jpg`, `matte-HN.jpg`, `mattes-h123.jpg`, `card-t0.5-HN.jpg`, `zoom-blur-B2-B3a-B4-HN.jpg`; da fase A: `standin-ex-*`, `folha-standin.jpg`, `original/`, `original-folha-fases.jpg`, `original-zoom-matte.jpg`.
- `clipes/` — `upload.json`, `talking-head-HN.mp4` (Pruna) + `HN.out.json` + `HN.log`, `talking-head-HN-ext.mp4` (head + wav cru), `talking-head-HN-sem-pausas.mp4`, `talking-head-HN-frames.jpg`. `audio/locucao-HN-rosto.wav` = wav cru cortado no rosto (entrada do Pruna); `audio/billings-fase-c-{antes,depois}.txt`.
- `pecas/` — `zap-wpp01-HN.mp4`, `zap-wpp01-HN-base.mp4`, `zap-wpp01-HN-poster.jpg`. `molde/head-HN-16k.{wav,json}`, `fronteiras-corpo-head.json`, `blocos-HN-standin.tsv`, `karaoke-HN-standin.tsv`, `pausas-talking-head-HN-sem-pausas.json`.

## Pendências

- ~~Lipsync Pruna: aguardando o sim do Gusta~~ → feito 11/09 (forma a, US$ 1,60 real). Ver "Pendências pro Maestro (fase C)".
- Decisão do Maestro sobre as durações desiguais do bloco 1 (1,85 s entre H2 e H1) e o wpm efetivo 204–214.
- Copy da Meta do vencedor traz `2.4M people already stopped torturing themselves…` — número que não é nosso; decisão do Gusta na hora de subir.
- Matte do campeão é fade (fase A) e o molde corta seco — não aplicado (uma alavanca por lote).
- Pro Maestro/dono do lote EX: blur do B2 curto (x 690 → dígitos "2799" legíveis ~1 s) e B5b em 153,3 (número no terminal até 153,3) — medido na gravação em 11/09.

## Verificação do Maestro e promoção (11/09, 02:30)

Conferido no disco: 1080×1920 · 30 fps · 0 silêncios ≥ 0,4 s nas 3; folha das 3 peças e campo do número do H1 (4,3 / 6,5 / 8,0 / 9,4 s) olhados — borrado. Cópias `CRIATIVOS-PRONTOS/25-ZAP-wpp01-clone-H1-what-their-whatsapp-is-hiding.mp4`, `26-…-H2-see-this-before-its-too-late.mp4`, `27-…-H3-sick-and-tired-of-the-lies.mp4` (md5 igual às peças) + linhas no LEIA-ME; galeria do 3D Brain reconstruída (`GET /api/graph?rebuild=1`). Custo total do lote ≈ US$ 1,75. Aceito como está: H3 mostra as mãos do avatar por ~2 s aos 7 s (regerar custaria US$ 0,53); peças diferem em até 1,9 s pelo ritmo do bloco 1.
