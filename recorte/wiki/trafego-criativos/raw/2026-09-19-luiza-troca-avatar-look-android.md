# Luiza Cristina (Ad Library 2554084605077306) — troca de avatar + look de celular Android · 2026-09-19

Pedido do Gusta: "só a troca de avatar, mas o vídeo original tem uma qualidade não tão boa, o que deixa um ar de realismo — dá pra fazer parecendo que foi gravado de um Android?"

| | |
|---|---|
| **Peça** | `LUIZA-troca-avatar-android-w1.mp4` — 720×720 · 30 fps · 854 frames · 28,58 s · **652 kbps** (original 578). Cópia: `CRIATIVOS-PRONTOS/64` |
| Original | `REFERENCIA-original.mp4`: **quadrado 720×720 dividido ao meio** — rosto à esquerda (x 0–354, medido pela borda vertical), gravação do funil `go.zappdetect.com` à direita. Sem legenda. Áudio: mulher, EN, 28,5 s ("The worst betrayal isn't the one you discover…") |
| Avatar | `elencos/w1.txt` (morena, pele clara-morena, cabelo ondulado solto, argolas, top branco) · `base/w1.png` = gpt-image-2/edit sobre o recorte esquerdo do original (mesmo quarto com flores) · `clipes/w1.mp4` = Pruna 29 s com o áudio original, prompt de pose em positivo sem citar objeto, seed 78 — clipe inteiro limpo (`conferencia/varredura-w1.jpg`) |
| Direita e áudio | os do original, intactos (o quadro inteiro é reencodado uma vez) |

## Look de Android — `montar.py` (calibrado com `medir.py`)
Medi no painel do rosto do original: **nitidez laplaciana 5,0 · ruído p5 0,8 / mediana 4,3 · luma 107 · contraste 47 · saturação 28 · RGB 122/102/96 · 578 kbps**. O clipe do Pruna sai limpo e saturado; a cadeia que iguala os números:

`fps=30 → zoom 1,12 + recorte 1:2,03 (o original é mais fechado no rosto) → scale 355×720 → gblur σ 0,45 → unsharp 0,3 → eq saturação 0,86 · gamma 1,02 · contraste 0,95 → colorbalance −0,02 (tira o quente do gerador) → noise 11 temporal → x264 main 600 kbps (maxrate 690k, buf 1,2 M, GOP 60)`

Resultado medido: nitidez 5,1 · ruído p5 0,71 / med 3,7 · luma 104 · contraste 53 · sat 25 · RGB 116/105/93 · 652 kbps. Tudo por env (`NOISE BLUR SHARP SAT GAMMA CONTRAST WARM BR ZOOM OY`). O que mais faz o "ar de celular" é a soma **bitrate baixo + ruído temporal + leve perda de nitidez + dessaturação** — sem nenhum deles isolado o rosto continua com cara de IA.

## Custo real: ≈ US$ 0,80 (imagem 0,07 + Pruna 0,73)

## Conferência
`conferencia/final-orig-x-novo.jpg` (3 instantes, original × novo), `orig-x-novo.jpg`, `zoom-textura.jpg` (300 % nos olhos: grão/blocos do original × nosso), `varredura-w1.jpg`.

## Variação nova
`elencos/wN.txt` → `base/wN.req.json` (copiar w1 trocando a descrição) → edit → upload → `clipes/wN.req.json` → Pruna → `python3 montar.py clipes/wN.mp4 saida.mp4` (≈ US$ 0,80).
