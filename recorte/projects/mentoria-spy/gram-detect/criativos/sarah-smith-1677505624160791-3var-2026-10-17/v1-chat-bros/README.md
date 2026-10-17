# V1 — "pov: men talk about women" (conversa estilo iMessage)

Peça: `pecas/v1-chat-bros.mp4` — H.264 yuv420p, 720×1280, 30 fps, 1095 frames (36,5 s), áudio AAC do original copiado bit a bit (md5 do stream igual).

## O que mudou
- f0–139 (0–4,63 s): gancho novo, conversa no modo escuro (cabeçalho com avatar "M" e "Mike 🏈", sem logo/marca). "pov: men talk about women" no topo. Mike digitando (f0) → bolha 1 (f8) → "copy her @" (f48) → "put it on Gram Detect" (f64) → digitando (f92) → "wait that works?? 😳" (f114 ≈ 3,8 s).
- f140–154: o push-wipe do original (medido: borda vertical em x = 708 − 48·(f−140)). À esquerda da borda entra o chat empurrado (no lugar do café). À direita ficam os pixels do original, mas nos f141–149 a caixa de legenda do café ("Girl, how do I…") vaza por cima da demo, então a faixa y 860–1145 foi coberta com o f155 deslocado b+4 px (a demo entra empurrada, deslocamento medido), com borda suave.
- f155–1094: original intacto (PSNR Y/médio ≥ 48,8 dB, média 52,3 dB — só a recompressão).

## Refazer
```
python3 render_gancho.py   # frames do chat em work/chat/ (PIL, 2x supersample)
python3 montar.py          # wipe + concat + encode -> pecas/v1-chat-bros.mp4
```
Conferência: `conferencia/folha-contato-1fps.png`, `conferencia/folha-emenda-f138-f157.png`.

## Concessões
- A legenda da demo segue dizendo "Copy his @ and use it on Gram Detect." (é pixel do original); no gancho masculino o certo seria "her". O reveal "her account" agora faz sentido.
- Fonte SF (do sistema) e emojis Apple renderizados pelo PIL; sem logo da Apple.
- Os f141–149 têm a faixa inferior da demo vinda do f155 (congelada só nessa faixa por 0,3 s, durante o movimento do wipe).
