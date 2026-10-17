# V2: resultado primeiro (open loop)

Peça: `pecas/v2-resultado-primeiro.mp4`, H.264 yuv420p + AAC, 720×1280, 30 fps, 1014 frames, 33,80 s. Custo de geração: zero (ffmpeg + PIL).

Alavanca única: a ORDEM. A peça abre na prova (perfil aberto) e só depois mostra como chegou lá. O café saiu.

## Mapa de frames (original → peça)

| Peça | Original | O que é |
|---|---|---|
| 0–73 (0–2,47 s) | f733–806 | REVEAL antes do "TRY IT FREE" (aparece em f807). Placa 1 "he said she was / “just a friend” 🙂" em 0–49, placa 2 "so I checked / her account 👇" em 50–73 |
| 74–651 (2,47–21,73 s) | f155–732 | DEMO inteira (Copy his @ → Make sure → Wait…). Placa 2 continua até o frame 93 (0,67 s depois do corte) |
| 652–1013 (21,73–33,80 s) | f733–1094 | REVEAL original com "Done!", TRY IT FREE, setas, crossfade e CTA até o fim |

Medições feitas por frame: o "Done!" começa em f733 (f732 ainda é "Wait…"), o "TRY IT FREE" entra em f807 e a faixa do café some da borda esquerda só em f155 (f150–154 ainda mostram o café na borda, medido pela média da coluna x 0–24).

Áudio: a trilha original de 0 a 33,80 s, com fade-out nos últimos 0,3 s.

## Refazer

```
bash work/montar.sh
```

O script gera `work/placa1.png` e `work/placa2.png` com `work/placas.py` (Montserrat ExtraBold, emoji Apple), monta e roda o ffprobe. Folhas de conferência: veja os comandos no histórico ou gere com `fps=1,scale=180:-1,tile=9x4`.

## Concessões

- O texto "Done! Now you can see…" (x 58–660, y 160–240) fica coberto por uma placa preta sólida arredondada (x 30–690, y 130–300), no estilo da caixa do gancho original. Não reconstruí o fundo porque a câmera está na mão e o fundo se mexe.
- O texto 2 tem duas linhas para caber na mesma placa. Ele fica 0,8 s sobre o reveal e mais 0,67 s sobre a abertura da demo. No total são cerca de 1,5 s, e o corte em si é seco.
- Os primeiros 2,47 s do reveal se repetem quando o reveal original volta em 21,7 s. É proposital: o loop aberto do começo se fecha ali.
- Deixei a demo inteira, sem aparar nada.
