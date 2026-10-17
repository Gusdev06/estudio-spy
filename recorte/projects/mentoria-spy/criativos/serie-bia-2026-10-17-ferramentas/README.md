# Série "day N" da Bia — lote 1 (day 1–3), 17/10/2026
Estratégia: `../../influencer-bia/estrategia-30k-2026-10-17.md`. Cena dos virais FollowSpy ainda não replicados, texto próprio da série.

| Pasta | Original (darkugc top 40) | Look da Bia | Final |
|---|---|---|---|
| serie-day1-bia-2026-10-17 | #13 avagirltalk, batata-doce | moletom cinza, trança | final/bia-serie-day1.mp4 (5,67 s) |
| serie-day2-bia-2026-10-17 | #20, abóbora | blusa preta manga longa, cabelo solto | final/bia-serie-day2.mp4 (6,27 s) |
| serie-day3-bia-2026-10-17 | #09 cat.girltea, lasanha | tricô creme, piranha | final/bia-serie-day3.mp4 (5,60 s) |

Pipeline por vídeo: `apagar-texto.py` (máscara estática por mínimo/máximo temporal + inpaint Telea) → frame 0,5 s sem texto → `google/nano-banana-2.1/edit` 2k [frame, ficha 01, ficha 05] → `bytedance/seedance-2.5/video-edit` 720p sem áudio sobre o vídeo sem texto → `texto.py` (texto da série) → `montar.sh` (áudio original, duração do original).
Conferência: decodificação integral ok, folhas `final/conferencia.jpg` sem texto residual, sem 2ª pessoa, mesma Bia nos 3.
Custo estimado (tabela, sem fatura): ~US$ 7,5 (3 × Nano Banana ~0,08 + 3 × Seedance ~2,4).
