---
tipo: tecnica
tags: [criativo, producao, html, mockup-ui, ferramenta]
fontes: [[fonte-teardown-zapspy-2026-08-22]]
---

# Criativo de mockup de UI — renderizar em HTML, não gerar por IA

Quando o criativo é um **print falso de app** (perfil do Instagram, painel, notificação,
conversa), a produção certa é HTML/CSS → Chrome headless → PNG. **Não** use gerador de imagem:
modelo de difusão destrói tipografia, inventa ícone e erra o chrome do app — exatamente as três
coisas que fazem esse criativo funcionar.

## Ganhos
- **Texto exato** — cada palavra, número e badge sai como escrito.
- **1 alavanca por arquivo** — a variação vira um diff, não uma nova geração. É o jeito barato
  de cumprir [[variar-uma-alavanca-por-vez]].
- **Custo zero e ~15s** pra regerar a esteira inteira. Nada de crédito de GERAEW/WaveSpeed.
- Versionável: o `.html` é o fonte, o `.jpg` é o build.

## Receita
1. Template com placeholders (`string.Template` do Python evita conflito com as chaves do CSS).
2. Canvas fixo `1080×1920`, `html,body{overflow:hidden}`, faixas em flex.
3. Ícones em **SVG inline** — não dependa de emoji, que muda de fonte por máquina.
4. Fonte embutida via `@font-face` com `file://` (a operação usa Montserrat Variable em
   `_lib/Montserrat-Variable.ttf`).
5. Renderize com `--force-device-scale-factor=2` (2160×3840) e faça downscale LANCZOS pra
   1080×1920 — texto sai bem mais nítido que renderizar direto em 1x.
6. Headline longa: `white-space:nowrap` + `font-size` por variação, e deixe folga no centro pro
   selo `VS` (senão o texto encosta nele).
7. Sempre monte um **contact sheet** das peças antes de aprovar — pega colisão de texto em
   uma olhada só.

## Os slots de foto precisam de foto de verdade
O erro que cometi na 1ª rodada do ZapSpy: preencher avatar e capas de destaque com **gradiente
CSS**. Some com a ilusão na hora — vira ilustração, não print. Gere as fotos (5 resolveram 11
peças: 1 avatar + 4 capas, reusadas em todas) e trate como parte da DNA travada.

Detalhes que vêm junto e são fáceis de esquecer, porque não são texto:
- **Anel gradiente** de story em volta do avatar E de cada capa de destaque.
- **Botões vazados** (borda, fundo transparente) no lado colorido — não preenchidos.
- **Divisória fina** em gradiente entre os painéis, não um vão escuro.
- O lado dessaturado usa **os mesmos arquivos**, cinza via `filter:grayscale(1)` no painel
  inteiro. Foto cinza de um lado e círculo chapado do outro denuncia a montagem.

Custo real: 5 fotos em GPT Image 2 (WaveSpeed `openai/gpt-image-2/text-to-image`, US$ 0,057
cada) = **US$ 0,29**. Elas aparecem a ~112px numa arte de 1080 — `quality: medium`, `1k`, 1:1
é suficiente. Não pague por resolução que ninguém vai ver.

## Limite
Só vale pra arte de interface/tipografia. Criativo de foto realista continua no fluxo de
[[gerar-criativo-imagem]] (GPT Image 2 → Seedream).

## Onde foi usado
`projects/zapspy/_build/render.py` — 11 peças ([[criativo-swipe-zapspy-split-screen]]).


## Confirmado em produção (31/08/2026)

Insert de dashboard do Roteiro D renderizado em HTML/CSS + `--headless --screenshot` do Chrome, direto em 1080×2400 (mais alto que o frame, pra sobrar curso de scroll). Depois `crop=1080:1920:0:'480*t/2'` no ffmpeg dá o **scroll lento de 2s** sem precisar de editor.

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --screenshot=out.png --window-size=1080,2400 --hide-scrollbars \
  --default-background-color=0B141A "file://$PWD/dashboard.html"
```

Blur em CSS (`filter:blur(5px)`) nos nomes e prévias resolve a censura de contato sem passo extra — e o `filter:none` no badge de contagem mantém o número nítido, que é onde a leitura acontece. Ver [[numero-especifico-quebrado]].

**Entra como cutaway sobre a fala, não como corte:** o overlay cobre só o vídeo (`enable='between(t,2,4)'`) e o áudio do clipe segue correndo por baixo. A tarja persistente é desenhada **depois** do overlay, senão o insert a apaga e a costura quebra ([[costura-de-clipes-por-tarja-persistente]]).
