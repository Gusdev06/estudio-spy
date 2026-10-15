# Molde 2 — split quadrado com look de celular Android

Peça 720×720: **rosto à esquerda** (x 0–354) e **gravação do funil à direita**, sem legenda. O truque desse molde é o **look de celular**: o clipe do lipsync sai limpo demais e denuncia IA, então ele é degradado até bater com os números medidos no original (nitidez, ruído, cor, bitrate).

```bash
# rosto novo (edit sobre o recorte esquerdo do original) → lipsync com o áudio do original → montagem
python3 montar.py clipes/w1.mp4 pecas/w1.mp4
python3 medir.py ../../midia/ref-2-luiza-split.mp4 pecas/w1.mp4   # confere nitidez/ruído/cor
```
Cadeia de degradação (tudo por env em `montar.py`): `gblur σ 0,45 · unsharp 0,3 · eq sat 0,86 gamma 1,02 contraste 0,95 · colorbalance −0,02 · noise 11 temporal · x264 600 kbps GOP 60`. Alvo medido no original: nitidez laplaciana 5,0 · ruído p5 0,8 · luma 107 · saturação 28 · 578 kbps.
