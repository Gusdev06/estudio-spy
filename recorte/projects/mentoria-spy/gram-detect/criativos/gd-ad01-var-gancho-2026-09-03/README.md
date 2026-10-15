# GD-AD01 — variação B: só o texto da caixa do gancho (2026-09-03)

Teste da esteira com **uma alavanca**: o texto da caixa rosa dos primeiros 7,8 s. Tudo o mais é o GD-AD01 original.

| | Arquivo | Texto da caixa | Custo |
|---|---|---|---|
| **Ad A** (controle) | `criativos-crus/spy-gram/ads-en/GD-AD01.mp4` (md5 `4a6906ae22e2a3c483e9fa7ccf2435fa`), intocado | `I found something I wasn't even looking for...` | zero |
| **Ad B** (variação) | `GD-AD01-B-caixa-supposed.mp4` (nesta pasta) | `I wasn’t even supposed` / `to see this...` | **zero** (só ffmpeg, nada pago) |

- Roteiro (Isca): `gram-detect/roteiros/2026-09-03-gd-ad01-var-gancho.md`
- Referência/teardown (Peneira): `gram-detect/referencias/proprios-2026-09-03/01-gd-ad01.md`, seção 14
- Montagem: `montar.sh` (comando ffmpeg completo, reproduzível). Conferência: `conferir.py`.
- Fonte: Poppins Bold (OFL) em `gram-detect/scripts/fonts/Poppins-Bold.ttf`.

## Como foi montado

Caixa opaca 868×197 desenhada em RGB com `drawbox`/`drawtext` (Poppins Bold 60 px, amarelo #EEFC00, contorno 2 px + sombra +5/+5 px em #2C040A), convertida pra YUV com matriz **bt709** e sobreposta em (106, 862) do frame 0 ao 233 (`enable='lt(n,234)'`). Fora da caixa o vídeo passa sem filtro. Áudio copiado sem reencode (`-c:a copy`). Saída 1080×1920, 30 fps, 978 frames, 32,6 s, H.264 crf 16, bt709.

Por que overlay e não `drawbox`+`drawtext` direto no vídeo: no ffmpeg 6.0 esses filtros convertem a cor pro YUV com matriz bt601, e o vídeo é bt709. Desenhando direto, o rosa decodifica como #F91A51 em vez do #FE0553 do original. Com a camada convertida em bt709 explicitamente, saiu #FC0351 (2 níveis de diferença, invisível).

## Medição que guiou a peça (frame t=1 s do original, decodificado com a tag bt709)

| item | original | variação B |
|---|---|---|
| caixa (bbox rosa) | x 106–973 · y 862–1058 | x 106–973 · y 862–1058 |
| cor da caixa (mediana) | #FE0553 | #FC0351 |
| linha 1: topo · centro x · largura | y 900 · x 541 · 810 px | y 900 · x 539,5 · 719 px (frase mais curta) |
| linha 2: topo · centro x · largura | y 974 · x 539,5 · 547 px | y 974 · x 538,5 · 357 px |
| amarelo (mediana) | #EEFC00 | #ECFA00 |
| contorno + sombra (extensão do escuro) | esq 2 · dir 7 · cima 3 · baixo 7 px | esq 2 · dir 8 · cima 3 · baixo 7 px |
| caixa entra / último frame / some | frame 0 / 233 / 234 (7,800 s) | frame 0 / 233 / 234 |

Fonte calibrada por largura: Poppins Bold 60 px reproduz a frase original em 813 px (medido 810) e a linha 2 em 547 px (medido 547).

## Conferência de saída (`conferir.py`)

- Frames 0, 30, 90, 233: caixa nova cobre a antiga; nenhum rosa da caixa antiga fora do retângulo (os ~500 px "rosa" na faixa y 840–1080 são a borda de croma da própria caixa, presentes também no original).
- Frame 234 em diante: zero rosa da caixa (frame 234, 977). O frame 500 tem 775 px rosa na região porque é a tela do story com gradiente, igual no original.
- Áudio: md5 da trilha `af796be74e3a089b804db1cafe8dd1c2` nos dois arquivos (bit a bit igual).
- Fora da caixa (frames 0–233) e no frame inteiro (234–977): diferença média 1,5–2,4 níveis, p99,9 ≤ 17, só ruído de reencode.
- Frames exportados em `conferencia/`: `lado-a-lado-t1s.png`, `recorte-caixa-2x.png`, `saida-caixa-f233-f234.png`, `mapa-diferenca-t1s.png` e os pares `fNNN-orig/var.png`.

## Custo

**US$ 0,00.** Nenhuma geração de vídeo, voz, rosto ou imagem.
