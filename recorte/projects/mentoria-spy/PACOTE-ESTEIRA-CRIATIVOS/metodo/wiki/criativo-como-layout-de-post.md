---
tipo: tecnica
tags: [layout, clone, karaoke, swipe, troca-de-avatar]
fontes: [[fonte-clone-podcast-wpp-avatares-2026-09-13]]
---

# Criativo como layout de post (e por que isso facilita clonar)

Parte dos criativos do swipe não é vídeo em tela cheia: é uma **montagem sobre fundo preto** com faixa de título em cima, uma janela de vídeo menor no meio e o karaokê embaixo, fora da janela. Medir essas fronteiras antes de qualquer coisa muda o método de clonagem inteiro.

Quando o karaokê está **fora** da janela de vídeo e sobre fundo preto, ele pode ser preservado pixel a pixel ao trocar o rosto — não precisa ser recriado, nem re-sincronizado, nem se aproxima do estilo por tentativa. O mesmo vale para a faixa de título, e a substituição fica restrita a um retângulo.

**Como medir** (custo zero): num frame qualquer, achar as linhas cujo máximo de luminância é > 25 (não-pretas) e listar os blocos contíguos. No podcast WhatsApp de 13/09 (720×1280) deu: faixa de título y 139-271 · **janela de vídeo 720×587 em y 347-933** · karaokê y ~944-1055. Conferir em vários instantes, porque o karaokê muda de altura com o número de linhas — o que importa é que ele nunca invada a janela.

Quando o karaokê está **queimado por cima da imagem** (o caso dos nossos próprios criativos), não há esse atalho: ou se recria a legenda, ou não se troca o rosto.

## Conecta com
- [[clone-podcast-wpp-avatares]] — onde foi usado
- [[medir-fronteira-de-bloco-em-video]] — a família de medições
- [[pruna-inventa-entrevistador-na-borda]] — a armadilha do mesmo lote
