# Lote gram01-l9-var-avatar — 5 avatares sobre o controle L9 en-01 (2026-09-11/12) · ENTREGUE

Oferta Spy Gram (go.zappdetect.com). **Controle:** `../gram01-l9-faixa-2026-09-01/pecas/gram01-l9-en-01-v2.mp4`
(1170×2532 · 975 fr · 32,500 s · 30 fps · x264 crf 19 preset medium · aac 44,1 kHz estéreo 31,927 s · md5 `2ebaa322…`).
**Molde:** L9 reconstruído aqui (`remontar-l9.sh`; o lote-controle não guardou o script — `build/` vazio) e provado
bit a bit. **Alavanca: ROSTO** — VO (`vo-master-en.m4a`, md5 `776f2194…`), funil, b-roll, faixa `en-01.png`, layout e
duração são os mesmos bytes nas 5. Casting do Peneira (`../../referencias/2026-09-11-casting-gram01-var-avatar-5-rostos.md`),
roteiro congelado e `video_prompt` da Isca (`../../roteiros/2026-09-11-gram01-var-avatar-5-rostos/`). Pipeline:
GPT Image 2 → `pruna-ai/p-video/avatar` (704×1280 · 24 fps) sobre a VO inteira, uma chamada por avatar.

## Estado — fases A, B e C concluídas · 5 peças entregues (12/09 00:12–00:25 local)

| | |
|---|---|
| ✓ molde L9 reconstruído e provado (fase A, custo zero) | `remontar-l9.sh` · `conferencia/standin-controle.mp4` = controle **975/975 frames idênticos** (framemd5, PSNR ∞) |
| ✓ enquadramento do controle medido (Haar, 12 frames) | head: olhos **47,4 %** · rosto 61–65 % · queixo ~86 % · cauda: olhos **44 %** · rosto ~60 % |
| ✓ mapeamento Pruna → peça decidido | head `crop CW×CH (CX,OY)` medido por avatar → 1170×1212 · cauda `crop 592×1280 (56,0)` → 1170×2532 · fps 24→30 |
| ✓ preço real (`wavespeed price` com uploads) | 720p **0,80**/avatar (VO 31,927 s → 32 s) · 0,825 com pad · 1080p **1,44** · 1,485 com pad |
| ✓ imagens-base (fase B) | `base/avatar-av1..5.png` · 6 chamadas (av1 regerada 1×) · **US$ 0,342 real** |
| ✓ áudio pro Pruna | `audio/vo-31927ms.wav` (recomendado) e `audio/vo-32500ms.wav` (pad) · URLs em `audio/upload-*.txt` |
| ✓ stand-ins no molde (custo zero) | `conferencia/standin-avN-<slug>.mp4` ×5 + posters + `folha-standins.jpg` · conferidos |
| ✓ scripts da fase C prontos | `gerar-heads.sh` (só com `CONFIRMADO=1`) · `remontar-lote.sh` · `medir-recorte.py` · `conferir-regioes.py` |
| ✓ heads Pruna (fase C, 720p, SIM do Gusta 12/09 ~00:45) | `clipes/talking-head-av1..5.mp4` · 704×1280 · **24 fps** · 769 fr · 32,042 s · 5 chamadas em paralelo (118–201 s cada) · **US$ 4,00 real** (5 × 0,80) · 0 falhas · 0 regerações |
| ✓ peças finais | `pecas/gram01-l9-en-01-avN-<slug>.mp4` ×5 + poster · conferidas (975 fr · VO md5 = master · silêncios 9 · faixa/funil/b-roll no ruído) · copiadas como **28–32** em `CRIATIVOS-PRONTOS/` (md5 iguais) |
| ✓ custo real do lote | **US$ 4,342** (`key:macbook`, billings 16:55–17:12 UTC) · saldo compartilhado 19,79 → **15,79** |

Portal: `projects/mentoria-spy/esteira.html` (http://localhost:8787/esteira.html), reescrito a cada etapa.

## Fase A — molde reconstruído e provado (custo zero)

**`remontar-l9.sh <head 1170×1212> <cauda 1170×2532> <saída> [faixa.png]`** — canvas preto 1170×2532 → head em (0,0)
→ painel `hstack(funil 462×1034, b-roll 708×1034)` em y 1498 → faixa em y 1212 **por último** → `concat` com a cauda
(frames 940–974). Entradas fixas do controle: `funil/funil-painel.mp4`, `broll/broll-painel.mp4`, `faixas/en-01.png`,
`vo/vo-master-en.m4a`. Encode = o do controle, lido do SEI x264 da peça (`strings | grep x264`): `crf=19`, `ref=3 subme=7
me=hex bframes=3 rc_lookahead=40` = **preset medium**, yuv420p, 30 fps. Áudio: o controle **re-encodou** o master
(stream md5 difere, mesmos 1376 frames aac); aqui vai `-c:a copy` — VO bit-idêntica ao master nas 5 (`cc4634ff…`).
Heads/caudas mais curtos que 940/35 frames são clonados (`tpad`), mais longos são cortados.

**Prova** (`conferir-regioes.py`, 26 frames: 0…900 a cada 50, 930, 939, 940, 941, 950, 960, 974; diferença média
absoluta por canal /255 contra `pecas/gram01-l9-en-01-v2.mp4`):

| região | média | máx | n |
|---|---|---|---|
| head (y 0–1212) | **0,000** | 0,000 | 21 |
| faixa (y 1212–1498) | **0,000** | 0,000 | 21 |
| funil (y 1498–2532 · x 0–462) | **0,000** | 0,000 | 21 |
| b-roll (x 462–1170) | **0,000** | 0,000 | 21 |
| cauda (fr 940–974, quadro cheio) | **0,000** | 0,000 | 5 |

Zero exato levantou suspeita, então conferi de outro jeito: **`framemd5` dos 975 frames decodificados: 975/975 iguais**;
`psnr` = ∞; sanidade do medidor: frame 300 × 301 do controle dá 0,84. Mesmas entradas + mesmo x264 (core 164, mesmos
parâmetros) = mesmo bitstream decodificado. Não é "ruído ≤ 1/255" — o molde **é** o controle. Arquivos: `conferencia/
standin-controle.mp4`, `standin-controle-regioes.{txt,json}`, `framemd5-{controle,standin-controle}.txt`.

**Faixa pela cor chapada** (mediana do canto: RGB 214,15,118; tolerância 12): linha **1211 = 0,000 · 1212 = 1,000 ·
1497 = 1,000 · 1498 = 0,000** em todos os frames < 940 (fr 900: 0,998 — o emoji encosta na linha), **0,000 nos frames
≥ 940** (a faixa some no 940 exato). Divisão: penhasco horizontal no painel (argmax |col j+1 − col j|, janela 440–480)
entre **x=461 e 462**, 130,2 contra 2º 21,6 (margem 6,0×). Silêncios ≥ 0,4 s a −35 dB: **9** no controle, no
master e no stand-in (3,545 · 6,547 · 9,891 · 12,635 · 14,924 · 18,169 · 21,959 · 26,320 · 28,631 s; somam 5,03 s) —
o briefing dizia 0; correção da Isca confirmada. Nenhum se corta.

### Enquadramento do head do controle (Haar frontalface + eye, OpenCV 4.14 num venv do scratchpad; `medir-olhos.py`)

| fonte · frame | olhos (y) | caixa do rosto (largura) | queixo (y) |
|---|---|---|---|
| head-panel f100 / f400 / f800 | 47,2 / 48,6 / 58,4 % | 63,7 / 61,5 / 61,0 % | 86,1 / 85,1 / 94,3 % |
| lipsync-raw f50 / f300 / f600 / f900 | 47,4 / 42,8 / 59,6 / 45,5 % | 64,0 / 61,4 / 65,3 / 60,7 % | 86,6 / 80,9 / 96,6 / 82,7 % |
| **head — mediana (7)** | **47,4 %** | **~62 %** (≈ 725 px) | **~86 %** (≈ 170 px de colo/alças abaixo) |
| tail f5 / f20 / f34 · peça f950 / f970 | 42,8 / 44,2 / 44,2 / 43,8 / 45,2 % | 65,7 / 59,7 / 59,5 / 64,4 / 57,9 % | 62,0 / 61,0 / 60,8 / 62,6 / 61,7 % |
| **cauda — mediana (5)** | **44,2 %** | **~60 %** (≈ 700 px) | **~61 %** |

Bate com a medição do Peneira por landmarks (olhos 47,3 % / 44,2 %); a largura dele (47,9 %) é contorno, a caixa Haar
dá ~1,3× isso. Frames anotados em `medicao/` (`olhos-*.jpg`, `folha-enquadramento-controle.jpg`, grades). Ela se
mexe muito (olhos 43–60 % no head) — o alvo é a posição de repouso.

### Mapeamento Pruna 704×1280 → peça (decidido)

- **Head:** `crop=CW:CH:CX:OY` → `scale=1170:1212` (lanczos). CW/CH/CX/OY **medidos por avatar** (`medir-recorte.py`
  no frame 0 do clipe, ou na imagem conformada a 704×1280): CW = 704 × (rosto Haar / 0,62), limitado a 585–704
  (upscale ≤ 2,0×); CH = CW×1212/1170; CX centrado no rosto; OY = olhos − 0,47·CH. Resultado nos stand-ins: olhos
  **47,1–47,3 %**, rosto **59–62,5 %** nas 5 (controle 47,4 / 61–65).
- **Cauda:** `crop=592:1280:56:0` → `scale=1170:2532` (**1,977×**; escala pela altura, corta as laterais, sem
  preenchimento — decisão do maestro). Olhos caem onde a imagem os pôs (36–43 % vs 44 % do controle).
- **fps:** o Pruna devolve **24 fps** (wpp01 e var4, `ffprobe`; o README do var4 diz 25, errado). `fps=30` por
  duplicação (padrão 4→5) num único stream; head = frames 0–939, cauda = 940–974 **do mesmo stream** → o colapso no
  frame 940 é um reenquadre, não um pulo de tempo. `tpad` clone até 975 se o clipe voltar curto.
- **720p vs 1080p:** 704→1170 = 1,66× (com o recorte por avatar 1,73–1,98×); 1080→1170 = 1,08× (1,13–1,29×). O head é o
  único bloco mole da peça (controle vem de fonte 2160 reduzida). **Recomendo 720p** pra este teste (5 peças, alavanca
  rosto, US$ 4,00); 1080p (US$ 7,20) só se o Gusta quiser nitidez de campeão — `remontar-lote.sh` aceita 1080×1920
  (recortes ×1,534; testado: olhos 45,1 % — o arredondamento desloca 2 %; medir no clipe 1080 direto se for o caso).
- **Áudio:** `audio/vo-31927ms.wav` = master decodificado mono 44,1 kHz (numpy: 1.408.000 amostras idênticas);
  `audio/vo-32500ms.wav` = idem + `apad whole_len=1433250` (exatamente 32,500 s; prefixo idêntico, resto zero; gera um
  10º "silêncio" que fica só na cópia do modelo). **Recomendo o sem pad** (US$ 0,125 a menos no lote): o Pruna já
  devolve ~0,6–0,8 s de vídeo além do áudio e esses frames **se mexem** (diff 0,4–1,3/255 entre frames consecutivos nos
  últimos 30 do wpp01-H1 e do var4-v2 — não é frame congelado).

## Fase B — imagens-base + stand-ins (12/09 00:5x local; Bisturi)

### Imagens — `openai/gpt-image-2/text-to-image` · 9:16 · 1k · medium · png · US$ 0,057 cada

Prompts = os do Peneira, literais, **exceto a frase "Framing"** (olhos 27 % → **44 %**, topo 17 → 25 %, queixo meio →
62 %; ver `HANDOFF-bisturi-para-peneira.md`). O modelo devolveu 940–960 × 1672–1696 (9:16 ±0,5 %). Medição na
geometria do Pruna (escala pela altura a 1280 + corte central a 704; `clipes/recorte-medicao.txt`):

| av | slug (Peneira) | rosto Haar | olhos | queixo | recorte do head (CW·CH·CX·OY · escala) | id · tempo |
|---|---|---|---|---|---|---|
| av1 | branca-25-quarto | 54,0 % | 36,1 % | 54 % | 612·634·51·164 · 1,91× | `77e08f14…` · 40 s (**take 2**) |
| av2 | latina-32-cozinha | 59,8 % | 37,0 % | 58 % | 678·702·20·144 · 1,73× | `4c5d8262…` · 76 s |
| av3 | asiatica-27-vaidade | 54,8 % | 41,4 % | 60 % | 622·644·70·227 · 1,88× | `6a617c0c…` · 50 s |
| av4 | branca-40-sala | 52,1 % | 41,9 % | 60 % | 592·612·80·249 · 1,98× | `6e41106f…` · 155 s |
| av5 | negra-30-mesa-luz-quente | 56,0 % | 43,0 % | 62 % | 634·656·49·242 · 1,85× | `245f52ef…` · 93 s |

- **av1 take 1** (`base/avatar-av1-take1.*`): rosto a **75 %** da largura (Haar), olhos não detectados — rosto grande
  demais pra um recorte de largura cheia (o head ficaria 18 % mais fechado que o controle, sem knob pra abrir).
  Regerada com "her face about 40 percent of the frame width (the phone held a little further…)" → 54 %. +US$ 0,057.
- Todas olhadas: boca fechada, olhos abertos, sem mão/celular/texto/óculos, pele com poro e brilho, luz de casa,
  cenário e figurino da ficha. av5 tem o meio-sorriso contido que a ficha pede.
- O GPT Image 2 puxa os olhos pra cima do pedido (36–43 % contra 44): irrelevante no head (OY medido), sobra na cauda.

### Stand-ins — `conferencia/standin-avN-<slug>.mp4` (imagem parada 704×1280 a 24 fps → `remontar-lote.sh` → molde)

| av | head fr 300: olhos · rosto | cauda fr 950: olhos · rosto · queixo | head/cauda vs controle (/255) | faixa · funil · b-roll (/255) | VO md5 · silêncios |
|---|---|---|---|---|---|
| av1 | 47,2 % · 61,8 % | 36,1 % · 64,0 % · 54 % | 67,1 · 64,1 | 0,14 · 0,52 · 0,94 | = master · 9 |
| av2 | 47,1 % · 60,7 % | 37,1 % · 70,2 % · 58 % | 58,4 · 54,2 | 0,14 · 0,53 · 0,94 | = master · 9 |
| av3 | 47,1 % · 62,5 % | 41,4 % · 65,8 % · 60 % | 50,4 · 42,1 | 0,15 · 0,53 · 0,93 | = master · 9 |
| av4 | 47,3 % · 61,1 % | 42,0 % · 62,2 % · 60 % | 51,7 · 62,9 | 0,14 · 0,53 · 0,93 | = master · 9 |
| av5 | 47,1 % · 59,0 % | 43,0 % · 64,7 % · 61 % | 60,1 · 52,7 | 0,13 · 0,53 · 0,93 | = master · 9 |

Todas 1170×2532 · 975 fr · 30 fps · faixa 1211 = 0 / 1212 = 1 / 1497 = 1 / 1498 = 0 e 0 nos frames ≥ 940 · divisão
x=461|462. Fora do head o resíduo 0,13–0,94/255 é ruído do x264 (mudou o head, o encoder redistribui bits; máx 1,26)
— o stand-in do controle deu 0,000 porque ali nada mudou. Folha: `conferencia/folha-standins.jpg` (controle × av1..5,
frames 300 e 950); medidas em `conferencia/standins-enquadramento.txt`; logs em `conferencia/standin-avN.log`,
`regioes-avN.txt`.

### Alavanca ou contaminação — o que difere do controle além do rosto

| item | controle | lote | leitura |
|---|---|---|---|
| cauda (35 fr · 1,17 s) | olhos 44 % · rosto ~60 % · queixo ~61 % | olhos 36–43 % · rosto 62–70 % · queixo 54–61 % | contaminação pequena, aceita pelo maestro (sem preenchimento) |
| nitidez do head | fonte 2160 reduzida (nítido) | Pruna 720p upscalado 1,73–1,98× | contaminação; 1080p (+US$ 3,20) tira |
| movimento do head | pessoa real, passeia (olhos 38–59 %) | movimento gerado, "framing stays fixed" (video_prompt) | inerente ao pipeline; anotar na leitura |
| lipsync | `sync/lipsync-2-pro` sobre gravação real | Pruna gera rosto + boca | inerente |
| fps | 30 nativo | 24 → 30 por duplicação | contaminação mínima |
| áudio | master re-encodado | master copiado (md5 = master) | a favor |
| cabelo/argola/top amarelo do controle | presentes | nenhuma usa amarelo nem argola (casting) | é a alavanca |

### Custo real — `wavespeed billings`, `key:macbook`, 11/09 16:55–16:59 UTC (`audio/billings-fase-b.txt`)

| chamada | prediction | US$ |
|---|---|---|
| av1 take 1 · av2 · av3 · av4 · av5 (paralelo) | `72bb2c58` `4c5d8262` `6a617c0c` `6e41106f` `245f52ef` | 5 × 0,057 = 0,285 |
| av1 take 2 | `77e08f14` | 0,057 |
| uploads (wav ×2, png de sonda) e `price` ×5 | — | 0,00 |
| **fase B** | | **US$ 0,342** |

Saldo compartilhado: 20,21 no início desta rodada (briefing dizia 20,37 — `key:tes` gastou no meio) → **19,79** depois.

## Fase C — estimativa (feita antes do SIM; execução e resultado na seção seguinte)

| opção | conta | total |
|---|---|---|
| **720p · VO sem pad** | 5 × ceil(31,927 s) = 32 s × US$ 0,025 | **US$ 4,00** ← recomendado |
| 720p · pad 32,5 s | 5 × 33 s × 0,025 | US$ 4,125 (briefing: 4,06, sem ceil) |
| 1080p · sem pad | 5 × 32 s × 0,045 | **US$ 7,20** |
| 1080p · pad | 5 × 33 s × 0,045 | US$ 7,425 |

`wavespeed price` sem inputs reais devolve 0; com uploads reais: 0,80 / 0,825 / 1,44 / 1,485 (`conferencia/price-*.json`).
Lote inteiro: 0,342 + 4,00 = **US$ 4,34** (720p) · 0,342 + 7,20 = 7,54 (1080p).

```
cd projects/mentoria-spy/gram-detect/criativos/gram01-l9-var-avatar-2026-09-11
bash gerar-heads.sh 720p                 # sem CONFIRMADO=1: imprime a estimativa e sai com código 1 (testado)
CONFIRMADO=1 bash gerar-heads.sh 720p    # 5 chamadas, uma por vez: image=base/avatar-avN.png (upload), audio=vo-31927ms.wav,
                                         # video_prompt = roteiros/…/video-prompt.txt, resolution=720p → clipes/talking-head-avN.mp4 + avN.out.json
# custo zero depois, por avatar (venv com cv2 pro medir-recorte):
python medir-recorte.py clipes/talking-head-av1.mp4 clipes/recorte-av1.env
bash remontar-lote.sh 1 branca-25-quarto  # → pecas/gram01-l9-en-01-av1-branca-25-quarto.mp4 + poster + conferência
```
`remontar-lote.sh` confere: 975 fr · VO md5 = master · silencedetect = 9 · regiões vs controle (faixa/funil/b-roll ≈
ruído, fronteiras 1211/1212/1497/1498 e x=462, faixa some no 940).

## Fase C — heads Pruna + peças finais (12/09 00:12–00:25 local; Bisturi)

Autorização: Gusta disse "sim" pra 720p em 12/09 ~00:45 local (US$ 4,00 estimados). Rodei `CONFIRMADO=1 bash gerar-heads.sh 720p avN`
**cinco vezes em paralelo** (uma invocação por avatar, cada uma com seu `clipes/avN.out.json` + `avN.log`; `clipes/upload.txt` tem
as 5 URLs das imagens). Início 17:12:13 UTC, fim 17:15:46 UTC (3,5 min pro lote). Áudio `audio/vo-31927ms.wav`, `video_prompt` da
Isca, `resolution=720p`. Nenhuma chamada falhou, nenhuma regeração.

### O que o Pruna devolveu (ffprobe, os 5 iguais)

704×1280 · h264 · **24 fps** · **769 frames · 32,042 s** de vídeo sobre 31,927 s de áudio (aac 1376 frames, mesma duração do master)
→ +0,115 s além do áudio (menos que os 0,6–0,8 s dos lotes anteriores). A 30 fps dá 961 frames: os **14 últimos (961–974, 0,47 s)
são clone do último frame** (`tpad`), dentro da cauda. Prediction ids · tempo: av1 `f2d012dc` 176 s · av2 `545d9c16` 201 s ·
av3 `de9803b6` 118 s · av4 `33279755` 201 s · av5 `5abe9cef` 195 s.

### Deriva do rosto no clipe (Haar, 7 frames: 0·128·256·384·512·640·744 · `clipes/deriva-7frames.txt`, 3 frames em `deriva-olhos.txt`)

| av | olhos no clipe (min–máx · faixa) | cx do rosto (média · crop antigo) | rosto | OY · CX fase B → usados | leitura |
|---|---|---|---|---|---|
| av1 | 35,2–36,4 % · **1,3 %** | 375 · 357 | 50,9–54,7 % | 164·51 → **164·50** (par) | estável; anda 42 px pra direita entre f0 e f744, dentro do recorte |
| av2 | 36,3–37,9 % · **1,6 %** | 386 · 359 | 55,8–61,1 % | 144·20 → **144·20** | estável |
| av3 | 37,1–41,3 % · **4,2 %** | 420 · 381 | 50,3–55,8 % | ~~227·70~~ → **186·82** (média; CX no limite 704−622) | frame 0 = posição da imagem (41,3 %); assenta 2–4 % mais alto a partir do f128 e vai pra direita (+87 px no f384) |
| av4 | 39,3–42,0 % · **2,7 %** | 393 · 376 | 50,7–52,7 % | 249·80 → **248·80** (par) | mantido (< 3 %); f256 é o ponto mais alto |
| av5 | 38,6–43,0 % · **4,4 %** | 416 · 366 | 51,6–56,7 % | ~~242·49~~ → **202·70** (média; CX no limite 704−634) | frame 0 = imagem (43 %); assenta em 39–40 % do f128 em diante e vai pra direita (+78 px) |

Regra aplicada: faixa de deriva > 3 % da altura → OY pela **média dos 7 frames** (olhos − 0,47·CH) e CX recentrado pela média
(limitado a 704−CW). `.env` antigos guardados em `clipes/recorte-av3.env.fase-b` e `recorte-av5.env.fase-b`. O padrão dos dois é o
mesmo: o Pruna começa exatamente na pose da imagem e "assenta" o rosto ~3 % mais alto e ~10 % mais à direita no 1º segundo — nos
próximos lotes, medir o recorte a partir do f128, não do f0.

### Conferência dos clipes antes da montagem (`conferencia/folha-heads-pruna.jpg` = base × f0 × 3,85 s × 7,67 s × 13,12 s × 18,67 s × 31 s)

- **Mãos:** nenhuma nos 5 (7 frames olhados por avatar). Ombros parados, quadro fixo, como o `video_prompt` pede.
- **Identidade:** igual à imagem-base nos 5 (f0 = imagem; f744 = mesma pessoa, mesma roupa, mesmo fundo).
- **Lipsync (medido, não chutado):** correlação de movimento da boca × envelope da VO (a 24 fps, lags −12…+12): pico em **−2…0
  frames (−83…0 ms) nos 5** (r 0,13–0,20 — proxy fraco, mas o lag é consistente). Tiras de boca nos silêncios 1 (3,545–4,051 s) e 2
  (6,547–7,639 s), `conferencia/tira-bocas-silencio{1,2}.jpg`: a boca **reabre 0,1 s depois da fala voltar** (onset no tempo) mas
  **fecha 0,3–0,5 s depois da pausa começar** (no silêncio 1, de 0,5 s, quase não fecha: av1 +29 / av3 +23 de abertura vs ~0 na fala).
  É um viseme segurado, não atraso — igual nas 5. Fraqueza suave do Pruna; não justifica regerar.
- **Nitidez/movimento no head 1170×1212** (`conferencia/` não guarda; números aqui): variância do laplaciano (4 frames) controle **5,5**
  vs av1 14,7 · av2 15,2 · av3 13,2 · av4 14,1 · av5 10,1 — por essa métrica o upscale 1,7–2,0× **não** deixou o head mais mole que o
  do controle (o head do controle é escuro e granulado). Movimento entre frames consecutivos (|Δ|/255): controle **3,10** vs av3 2,08 ·
  av1 1,46 · av4 1,45 · av2 1,28 · **av5 0,83** — os avatares se mexem 1,5–3,7× menos que a pessoa real.

### Peças finais — `remontar-lote.sh` (5 em paralelo, logs em `conferencia/peca-avN.log`, regiões em `conferencia/regioes-avN.txt{,.json}`; os das stand-ins foram renomeados pra `regioes-standin-avN.*`)

Todas: 1170×2532 · **975 fr · 30 fps** · x264 crf 19 medium · aac 44,1 kHz estéreo · **VO stream md5 = master `cc4634ff…`** ·
**silencedetect −35 dB/0,4 s = 9** · faixa por cor chapada 1211 = 0 · **1212 = 0,96–1,00** · 1497 = 1 · 1498 = 0 em todos os
frames < 940 e **0,000 em todos os ≥ 940** · divisão x=461|462 (130,0–130,3 vs 2º 21,6–21,9) · metadata só `Lavf` (PII zero;
funil = `funil-painel.mp4` borrado do controle). A linha 1212 caiu de 1,000 (stand-ins) pra 0,960 (av1 f450) / 0,977 (av1 f650) /
0,988 (av2 f450) em 3 dos 105 frames medidos: sangria do deblocking do x264 na fronteira head|faixa com head em movimento — 1211 e
1498 seguem 0,000 exatos.

| av | head vs controle (/255) | cauda | faixa · funil · b-roll (/255, máx) | olhos no painel f100/300/600/900 | rosto painel | cauda f950/970: olhos · rosto |
|---|---|---|---|---|---|---|
| av1 | 68,5 | 66,4 | 0,135 · 0,555 (1,31) · 0,942 (1,18) | 46,9 · 48,0 · 46,9 · 47,0 % | 55,6–60,7 % | 36,2 % · 58 % |
| av2 | 60,0 | 53,7 | 0,122 · 0,528 (1,17) · 0,929 (1,18) | 45,9 · 49,5 · 45,4 · (f900 Haar falhou) | 60,6–62,7 % | 37,3–37,6 % · **71–72 %** |
| av3 | 51,0 | 44,7 | 0,122 · 0,520 (1,06) · 0,933 (1,18) | 46,9 · 48,4 · 46,5 · 48,3 % | 57,0–64,2 % | 35,2 / 37,0 % · 66 / 57 % (f970: caixa Haar deslocada pra x 31–703; na folha o rosto está inclinado, não cortado) |
| av4 | 52,7 | 63,9 | 0,121 · 0,527 (1,10) · 0,935 (1,18) | 45,0 · 45,2 · 42,2 · 46,0 % | 60,8–62,6 % | 41,3–41,5 % · 62–63 % (a mais perto do controle 44 %) |
| av5 | 62,3 | 53,9 | 0,122 · 0,528 (1,22) · 0,935 (1,19) | **51,5 · 49,8** · 46,0 · 46,1 % | 55,8–62,8 % | 39,0–39,2 % · 61–62 % |

Controle: olhos 47,4 % · rosto 61–65 % no head; 44 % · ~60 % na cauda. Folha lado a lado (controle × 5, frames 300 e 950):
`conferencia/folha-pecas.jpg`; medidas: `conferencia/pecas-enquadramento.txt`.

**O que ficou fraco, por peça (honesto):**
- **av5 (negra-30-mesa-luz-quente) — a mais fraca.** É a que menos se mexe (0,83 vs 3,10 do controle: cara de foto animada) e, como
  o OY foi pela média e ela começa 4 % mais baixa, os **primeiros ~5 s ficam com os olhos a 50–51 %** do painel (alvo 47) antes de
  assentar em 46 %. Rosto e luz são bons; o meio-sorriso da ficha está lá.
- **av2 (latina-32-cozinha)** — head ok, mas a **cauda escala o rosto a 71–72 %** da largura (controle ~60 %): 1,17 s de close
  apertado. Sorriso largo com dentes em 7,67 s e 18,67 s (a VO é "segredo baixinho"); f448 pegou um piscar.
- **av3 (asiatica-27-vaidade)** — maior deriva (4,2 %) e vai pra direita; com o recorte novo ficou centrada, mas na cauda a cabeça
  inclina. Movimento mais natural dos 5 (2,08).
- **av1 (branca-25-quarto)** — boca aberta na pausa 1 (mais visível que nas outras); sorriso em 18,67 s e 31 s. Enquadramento cravado
  (46,9–48,0 %).
- **av4 (branca-40-sala)** — a mais firme (olhos 42–46 %, cauda 41 %); só o f256 desce 2 %. Nada a registrar como fraco além do
  viseme segurado comum às 5.

### Cópias em `CRIATIVOS-PRONTOS/` (md5 conferido, cópia = original)

| # | arquivo | md5 |
|---|---|---|
| 28 | `28-GRAM-gram01-l9-av1-branca-25-quarto.mp4` | `fd65f190…` |
| 29 | `29-GRAM-gram01-l9-av2-latina-32-cozinha.mp4` | `85f44302…` |
| 30 | `30-GRAM-gram01-l9-av3-asiatica-27-vaidade.mp4` | `776b3e29…` |
| 31 | `31-GRAM-gram01-l9-av4-branca-40-sala.mp4` | `ea025a75…` |
| 32 | `32-GRAM-gram01-l9-av5-negra-30-mesa-luz-quente.mp4` | `8fd662bb…` |

### Custo real — `wavespeed billings --since 2026-09-11T17:00:00Z` (`audio/billings-fase-c.txt`) e lote inteiro (`audio/billings-lote-completo.txt`, desde 16:50 UTC)

| fase | chamadas (`key:macbook`) | US$ |
|---|---|---|
| B — imagens | 6 × `openai/gpt-image-2/text-to-image` × 0,057 | 0,342 |
| C — heads | 5 × `pruna-ai/p-video/avatar` × **0,800** (17:12:23–24 UTC: `f2d012dc` `545d9c16` `de9803b6` `33279755` `5abe9cef`) | **4,000** |
| uploads (5 png) · ffmpeg · Haar | — | 0,00 |
| **lote** | 11 chamadas | **US$ 4,342** (estimativa era 4,34 — bateu) |

Saldo compartilhado: 19,79 antes da fase C → **US$ 15,79** depois (`wavespeed balance`, 17:16 UTC). `key:tes` não gastou nada
no intervalo da fase C (o 0,081 do Seedream às 16:55 já estava dentro do 20,21 → 19,79 da fase B).

### Alavanca ou contaminação — atualizada com o que o Pruna devolveu de fato

| item | controle | lote (medido) | leitura |
|---|---|---|---|
| fps | 30 nativo | **24** → 30 por duplicação 4→5 | contaminação mínima, confirmada |
| duração do head gerado | 940 fr reais | 769 fr = 32,042 s (+0,115 s sobre o áudio) → 14 frames clonados no fim da cauda (0,47 s parados) | contaminação pequena, só na cauda |
| nitidez do head | var. laplaciano 5,5 | 10,1–15,2 (720p upscalado 1,7–2,0×) | **não** ficou mais mole que o controle; 1080p não se justifica por nitidez |
| movimento do head | 3,10 /255 entre frames (pessoa real passeia) | 0,83–2,08 (av5 a mais parada, av3 a mais viva) | contaminação real: avatar mais estático que a pessoa; inerente ao Pruna |
| lipsync | sync/lipsync-2-pro sobre gravação | onset no tempo (lag −2…0 fr); boca fecha 0,3–0,5 s tarde nas pausas | inerente; visível só em pausa longa |
| enquadramento do head | olhos 47,4 % · rosto 61–65 % | olhos 45–48 % (av5 50–51 % nos 5 s iniciais) · rosto 56–64 % | ok em 4; av5 leve |
| cauda (1,17 s) | olhos 44 % · rosto ~60 % | olhos 35–41 % · rosto 57–72 % (av2 71 %) | contaminação pequena, aceita pelo maestro |
| mãos | fora | fora nas 5 | ok |
| áudio · funil · b-roll · faixa · layout | — | bit-idênticos (md5 da VO; regiões no ruído x264) | alavanca limpa |

## Riscos (escritos antes da fase C — leitura depois entre parênteses)

1. **Deriva do Pruna em 32 s** — nenhum lote da casa mediu se o rosto passeia/perde identidade ao longo de 30+ s; o
   recorte usa o frame 0. Se passear, o head sai do enquadramento do controle (conferir com `medir-olhos.py` em 3 frames).
   *(Medido: 1,3–4,4 % da altura; identidade preservada; av3/av5 tiveram o OY refeito pela média de 7 frames.)*
2. **Mãos**: o wpp01-H3 mostrou as mãos apesar do prompt. As imagens-base têm mãos fora; o video_prompt pede "hands out
   of frame". Regerar um avatar = +US$ 0,80. *(Nenhuma mão nas 5.)*
3. **Nitidez**: 720p upscalado até 1,98× no head — o bloco mais mole da peça. 1080p resolve por +US$ 3,20. *(Medido: não ficou
   mais mole que o head do controle pela variância do laplaciano.)*
4. **Cauda** com olhos 36–43 % e rosto maior por 1,17 s (tabela acima).
5. Nenhuma métrica do controle foi verificada (proxy de Ad Library) — igual ao lote-controle.

## Pastas

```
remontar-l9.sh        molde L9 (head + cauda + faixa → peça)         conferir-regioes.py   diferença por região vs controle
remontar-lote.sh      clipe do Pruna → head/cauda recortados → molde  medir-olhos.py        olhos/rosto Haar (venv cv2)
gerar-heads.sh        fase C, só com CONFIRMADO=1                     medir-recorte.py      CW/CH/CX/OY por avatar
base/                 avatar-avN.png + -prompt.txt + .json/.log · av1-take1.* · slugs.tsv · medicao-olhos.txt
audio/                vo-31927ms.wav · vo-32500ms.wav · upload-*.txt · billings-*.txt
medicao/              frames do controle com olhos/rosto anotados · grades · folha-enquadramento-controle.jpg
conferencia/          standin-controle.mp4 + regioes/framemd5 · standin-avN-<slug>.mp4 + poster + log · folha-standins.jpg
                      standins-enquadramento.txt · price-*.json · src/ (clipes parados 704×1280 e frames)
clipes/               recorte-avN.env (+ .fase-b pra av3/av5) · talking-head-avN.mp4 + avN.out.json + avN.log · upload.txt ·
                      deriva-olhos.txt · deriva-7frames.txt · billings-antes/depois-*.txt · fase-c-inicio/fim.txt · conformado/ (head/tail 1170)
pecas/                gram01-l9-en-01-avN-<slug>.mp4 + poster (cópias 28–32 em ../../../CRIATIVOS-PRONTOS/)
conferencia/ (fase C) folha-heads-pruna.jpg · tira-bocas-silencio{1,2}.jpg · folha-pecas.jpg · pecas-enquadramento.txt ·
                      peca-avN.log · regioes-avN.txt{,.json} (peças) · regioes-standin-avN.* (stand-ins, renomeados)
HANDOFF-bisturi-para-peneira.md   decisão de enquadramento (olhos 44 %, recorte por avatar) e critérios de aceite ajustados
```
Mídia pesada não entra no git (`.gitignore` da raiz).

## 12/09 — reformatação pra Meta (custo zero)

As 5 peças em 1170×2532 (~1:2,16) dão "não veiculável" no Ads Manager em qualquer posicionamento. `reformatar-meta.sh`
gera, por peça, `pecas/meta/<nome>-9x16.mp4` (1080×1920: head crop 1170×1062 @y40 + faixa + painel crop 732 px, tirando
o teclado; cauda crop 2080 @y150) e `<nome>-4x5.mp4` (1080×1350: head crop 1176 @y36 + faixa, sem painel; cauda crop
1462 @y456). Encode igual ao controle, `-c:a copy` (VO md5 `d6dacce1…` = original). Conferido: 10/10 com 975 frames e
dimensões certas; frames 12 s e 31,8 s de av1/av3/av5 olhados. Copiadas pra `CRIATIVOS-PRONTOS/` como
`28–32-GRAM-…-{9x16,4x5}.mp4`. Lição: o molde L9 nasceu do screenshot de iPhone (1170×2532); o próximo molde deve
nascer em 1080×1920 pra não precisar cortar teclado.
