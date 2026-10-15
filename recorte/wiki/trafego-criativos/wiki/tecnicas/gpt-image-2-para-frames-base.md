---
tipo: tecnica
tags: [imagem-ia, gpt-image-2, producao, continuidade]
fontes: [fonte-producao-roteiro-d-2026-08-31]
---

# GPT Image 2 para frames-base de vídeo

Quando dois personagens precisam parecer que estão no **mesmo lugar** mas são gerados separados, a continuidade se resolve no prompt da imagem, não na edição.

**O truque:** escreva o bloco de cenário e o bloco de luz **com as mesmas palavras** nos dois prompts, mudando só o sujeito e o mobiliário. Não parafraseie — repita literalmente.

Verificado em 31/08/2026: âncora atrás da bancada e convidada na poltrona saíram com a mesma skyline noturna, a mesma luz âmbar de cove, o mesmo grade frio. Leem como o mesmo estúdio.

## Parâmetros

`openai/gpt-image-2/text-to-image` · `aspect_ratio="9:16"` · `resolution="2k"` · `quality="high"` → **$0,38/imagem**. No `1k`/`medium` cai pra $0,057, mas aí não segura como frame-base de vídeo.

## Regras pra frame que vai virar vídeo

1. **Zero texto na imagem.** Tarja, ticker, logo e legenda entram na edição — só assim ficam idênticos entre clipes ([[costura-de-clipes-por-tarja-persistente]]). Liste todos no `Avoid`.
2. **Reserve o espaço negativo**: "leave the lower fifth of the frame visually simple and uncluttered". É onde a tarja vai pousar.
3. **Câmera na altura do olho, plano médio, sujeito centrado** — o Kling parte desse enquadramento; se a imagem já vem torta, o vídeo herda.
4. **Negue o que não pode aparecer no figurino** (jaleco, crachá, credencial bordada) — decisão de risco, ver [[nao-imitar-veiculo-real]].

Segue pra [[kling-3-fala-o-roteiro]].
