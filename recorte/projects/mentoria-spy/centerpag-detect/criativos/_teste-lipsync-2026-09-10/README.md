# Prova de lipsync barato — 2026-09-10

Mesma imagem (avatar do Secret Revealed) + mesmos 8 s de áudio em 5 modelos da WaveSpeed (imagem + áudio → avatar falante).
Todos cobram POR SEGUNDO de áudio. `skywork-ai/skyreels-v3-pro/single-avatar` deu "Model not found" (saiu do catálogo).

| Modelo | US$/s | 32 s | Saída | Arquivo |
|---|---|---|---|---|
| bytedance/avatar-omni-human-1.5 (referência) | 0,16 | 5,12 | 718×1286 25 fps | ref-omnihuman15-8s.mp4 |
| bytedance/avatar-omni-human (1.0) | 0,12 | 3,84 | 464×832 | out-omnihuman10.mp4 |
| pruna-ai/p-video/avatar (720p) | 0,025 | 0,80 | 704×1280 | out-pruna.mp4 |
| wavespeed-ai/soulx-flashhead (720p) | 0,075 | 2,40 | 704×1264 | out-soulx.mp4 |
| wavespeed-ai/infinitetalk-fast | 0,075 | 2,40 | 352×624 (baixa demais) | out-infinitetalk-fast.mp4 |

Grid lado a lado (ordem acima, da esquerda pra direita): scratchpad/lipsync-grid-5.mp4 (enviado ao Gusta).
Modelos "lipsync" (sync, veed, kling-lipsync, ltx) exigem VÍDEO de entrada; não partem de foto.
Custo da prova: ~US$1,70.
