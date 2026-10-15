---
tipo: tecnica
tags: [edicao, criativo-video, prova, congruencia, pii]
fontes: [fonte-producao-roteiro-d-2026-08-31]
---

# Insert de funil real como cutaway

Screen recording do **funil de verdade** vale mais que mockup gerado — e mais que print estático. Ele carrega três coisas que nenhuma arte reproduz: o movimento real da interface, os elementos de escassez que a própria página roda (timer, "58 people viewing right now") e a **congruência com a página**.

Congruência é o ponto sub-avaliado: quando o insert mostra a mesma tela que o clique vai encontrar, a promessa do anúncio e a promessa da página são literalmente o mesmo pixel. É o estágio de CVR do funil de diagnóstico ([[piso-de-volume-antes-de-julgar-criativo]] cuida do de cima).

**Caso registrado:** a landing do `go.zappdetect.com` diz *"Built for people who've been burned by spy apps that didn't work"*, *"No app to install"*, *"No phone access needed"* — exatamente a copy do [[criativo-wpp01-1762552938111855]]. O anúncio não estava inventando ângulo; estava lendo a página.

## Como entra

**Cutaway sobre a fala, nunca corte.** O overlay cobre só o vídeo (`enable='between(t,a,b)'`) e o áudio do clipe segue correndo por baixo — a frase não é interrompida. Casar o trecho com a palavra: "you enter the number" → o dedo digitando; "you're reading what was already there" → a mensagem recuperada na tela.

A tarja persistente é desenhada **depois** do overlay. Ordem invertida = o insert apaga a tarja e a costura quebra no meio da peça ([[costura-de-clipes-por-tarja-persistente]]).

Recording de iPhone vem em 1170×2532 (0,462) e o destino é 1080×1920 (0,5625) — `scale=1080:-1,crop=1080:1920:0:<y>`, com o `y` ajustado por trecho pra manter o bloco que importa dentro do quadro.

## ⚠️ PII — checar sempre

Recording de teste é feito com **conta e número reais**. Antes de qualquer trecho entrar:

1. Varra a gravação inteira por número de telefone, e-mail, nome e foto de perfil.
2. `boxblur` na região, ou escolha outro trecho.
3. Telas de captura de e-mail / "welcome back, <nome>" — evite por completo, não dá pra borrar sem matar a tela.

No Roteiro D: `boxblur=24:3` no campo do número e a tela de e-mail cortada fora do recorte.
