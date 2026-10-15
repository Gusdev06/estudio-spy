# Flora 959352790554428: variação 11, só com a dupla nova (2026-09-27)

A base é a var5 (`../var5-flora-959352790554428-2026-09-25/`), com o mesmo molde, estúdio (painéis hexagonais cinza), áudio, headline original e scripts. **Só a dupla muda.**
A peça está em `pecas/variacao.mp4`, com cópia em `CRIATIVOS-PRONTOS/variacoes-2026-09-27/flora-959352790554428-2026-09-27/var11-flora-959352790554428.mp4`.

## Elenco
- A (explica): mulher ~45 branca, cabelo castanho ondulado com fios brancos, blusa listrada
- B (pergunta): homem ~30 latino, cabelo cacheado curto, bigode fino, moletom ferrugem

## Pipeline
É o mesmo da var5: `gerar-bases.py` → `gerar-clipes.sh` (SEED=7) → `checar.py` → `montar.py` → `varredura.py`. Os downloads dos clipes deram "fetch failed" ou saíram truncados, então todos foram rebaixados pelo id da predição e validados decodificando o arquivo inteiro, sem regeração. No `checar.py`, os alertas foram giro de cabeça (perfil → 3/4) e deriva leve de câmera no B. Conferi no olho: é a mesma pessoa do começo ao fim, sem 2º rosto e sem moldura.

## Varredura final
```
frames 1026 1026 fps 30/1 audio MD5=317d323d80b5b2ce454825e1aaf93a5a MD5=317d323d80b5b2ce454825e1aaf93a5a
dupla (408 fr): dif janela mediana 56.7 min 12.0 (n 266); corr bordas max 0.12 (n 127) mediana 0.05
fora da janela dif max 3.2; painéis dif max 3.1; YuNet rostos/frame max 1 (frames com >1: []); dupla sem rosto: 1 fr
```

## Custo estimado: ~US$ 0,53
São 2 imagens gpt-image-2/edit (~0,067 cada) e 4 clipes Pruna (~0,10 + 0,09 + 0,05 + 0,125, a US$ 0,025/s).
