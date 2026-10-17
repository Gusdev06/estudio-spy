# Variações de gancho (copy) sobre a V2 "resultado primeiro" (17/10)

Uma alavanca só: o texto da placa 1. Montagem, cortes, áudio e placa 2 são os da V2 (`gram-detect/criativos/sarah-smith-1677505624160791-3var-2026-10-17/v2-resultado-primeiro/`). Custo zero (ffmpeg + PIL).

| Peça | Placa 1 (f0–49) | Placa 2 (f50–93) |
|---|---|---|
| `pecas/4a-without-touching.mp4` | This is how I caught him / cheating without / touching his phone | so I checked / her account 👇 |
| `pecas/4b-stopped-guessing.mp4` | I finally / stopped guessing. | igual |

As duas saem em H.264 yuv420p + AAC, 720×1280, 30 fps, 1014 frames e 33,80 s.

- 4a: com 3 linhas a fonte cai de 54 para 46 px, porque "This is how I caught him" mede 705 px em 54 e a placa tem 660. A placa fica mais alta (y 112–318) e continua cobrindo o "Done!..." (y 160–240).
- Correção em relação à V2: as imagens das placas entram com `-framerate 30`. Sem isso o loop roda a 25 fps e a placa 1 aparece nos frames 50–53 e 55–58, no lugar da placa 2. A V2 publicada tem esse defeito.

Refazer: `bash work/montar.sh`. Conferir frame a frame se o texto antigo vaza: `python3 work/checar.py pecas/<peça>.mp4 work/<4a|4b>-placa1.png work/placa2.png`. As folhas ficam em `conferencia/`.
