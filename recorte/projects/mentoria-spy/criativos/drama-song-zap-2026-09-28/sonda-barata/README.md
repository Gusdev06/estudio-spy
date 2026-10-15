# Sonda de modelo barato — B05 (2026-09-28)

Mesma cena B05, quadro 1 e quadro 4 do shot sheet recortados (sem grade) como `image` + `last_image`.

| Modelo | Saída | Custo real (billings key:macbook) | US$/s | Veredito |
|---|---|---|---|---|
| bytedance/seedance-2.0-fast i2v 720p (Bisturi) | 7,0 s | 1,40 | 0,20 | grade vazou 0,9 s; 3 de 4 momentos |
| **pruna-ai/p-video-2-pro i2v 768p** | 7,3 s | **0,245** | **0,035** | **os 4 momentos, sem grade, rostos consistentes** |
| wavespeed-ai/minimax-h3 i2v 480p | 7,3 s (48 s de fila) | 0,14 | 0,02 | 4 momentos, atuação mais expressiva (mesa ri de verdade); um pouco mole em 480p |
| wavespeed-ai/minimax-h3 i2v 768p | 7,3 s (136 s de fila) | 0,28 | 0,04 | igual ao 480p, mais nítido; melhor custo-qualidade do teste |
| wavespeed-ai/wan-2.2 i2v-720p-ultra-fast | 8,0 s | 0,16 | 0,02 | perde o beat do celular; Ryan some; fraco |

Recorte dos quadros de primeiro/último frame resolve o vazamento da grade.
Estimativa pra fechar a peça com Pruna: ~259 s × 0,035 ≈ US$ 9 de vídeo + ~28 shot sheets (gpt-image-2/edit ~0,23) ≈ US$ 6,5 → **~US$ 16** (+30% retry).

Peça inteira com H3 (vídeo ~259 s + shot sheets ~US$ 6,5): 480p ≈ US$ 12 · 768p ≈ US$ 17. Todos os modelos fizeram a Maya encostar no celular (o plano pedia sem tocar) — corrigir no prompt em positivo.
