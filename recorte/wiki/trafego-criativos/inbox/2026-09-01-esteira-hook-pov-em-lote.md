---
data: 2026-09-01
projeto: theaimodelab
tipo: tecnica
status: inbox
---

# Esteira de hook em lote sobre criativo único (POV overlay)

Rodada de produção: 1 criativo base (`projects/theaimodelab/raw.mov`) → **100 variações**
só trocando o hook em texto. Ainda sem dado de performance.

## Leitura do criativo base
- 30s, 1080x1920, 30fps. Estrutura: **talking head 0.00→2.95s** → screen recording do
  Prompt Library até o fim.
- O hook original é **falado no áudio**, não existe overlay. O talking head é uma janela
  visualmente limpa — é exatamente onde o hook em texto cabe sem competir com nada.
- O vídeo já tem legendas próprias (branco, itálico, contorno preto) da metade em diante.

## Técnica
- Trocar áudio 100x (clonar voz + re-sync) é inviável. **Overlay de texto queimado nos
  segundos do talking head** é o que escala.
- Render: `ffmpeg` + `drawtext` com `enable='lt(t,2.95)'`, Arial Black branco, contorno
  preto, centralizado no topo (y=220).
- **Auto-fit de fonte** (medição com PIL antes de renderizar) pra frase longa não estourar
  a margem: 60px base, encolhe até caber em 920px. Ficou entre 48 e 60px.
- `h264_videotoolbox` (encoder de hardware) + `-c:a copy`: 3.5s por render, 4 em paralelo
  → 100 arquivos em ~2min. Re-encodar em libx264 levaria ~1h.

## Formato do hook
POV em caixa alta, 2 linhas, 2ª pessoa. Famílias de ângulo usadas: ilegalidade/choque,
gratidão exagerada, descoberta de método, arrependimento por não saber antes, segredo
escondido, urgência.

Ver `projects/theaimodelab/variacoes/` (frases.txt + index.csv + mp4/).
