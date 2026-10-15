---
tipo: tecnica
criado: 2026-09-19
fontes: [raw/2026-09-19-luiza-troca-avatar-look-android.md]
tags: [avatar-ia, realismo, ffmpeg, pos-producao]
---

# Look de celular Android calibrado

O clipe de lipsync (Pruna, Kling…) sai limpo, nítido e saturado — e é isso que denuncia IA. O original que escalou (Luiza Cristina, 19/09) tinha "qualidade não tão boa, o que deixa um ar de realismo" (Gusta). A técnica: **medir o original e degradar o clipe até os números baterem**, não "colocar um filtro".

**O que medir no painel do rosto** (`medir.py`): nitidez laplaciana, ruído em blocos lisos (p5 e mediana), luma, contraste, saturação, média RGB e bitrate do arquivo.

**Cadeia que fechou** (original 5,0 / 0,8 / 107 / 47 / 28 / 578 kbps): `gblur σ 0,45 → unsharp 0,3 → eq sat 0,86 gamma 1,02 contraste 0,95 → colorbalance −0,02 → noise 11 temporal → x264 600 kbps GOP 60`. Nenhum item sozinho resolve; é a soma **bitrate baixo + ruído temporal + leve perda de nitidez + dessaturação**. O gerador puxa pro quente e saturado — o corretivo é frio e dessaturado.

**Também conta o enquadramento:** o original era mais fechado no rosto que o clipe 9:16 do Pruna (zoom 1,12 + offset).

Conecta com [[reconstruir-camadas-do-criativo]] (a direita do split e o áudio ficaram intactos) e [[reproduzir-o-defeito-do-original-em-vez-de-corrigir]] — mesma filosofia: o "defeito" é parte do que converteu.
