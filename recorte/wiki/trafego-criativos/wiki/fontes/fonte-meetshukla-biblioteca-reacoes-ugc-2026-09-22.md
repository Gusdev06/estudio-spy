---
tipo: fonte
data: 2026-09-22
tags: [ugc, clonagem, troca-de-avatar, biblioteca-de-referencias, video-understanding, clonador, referencia-externa]
fontes: ["https://x.com/meetshukla_/status/2102271476950819238"]
---

# Ghostfeed: biblioteca de 1.066 referências UGC classificada por estrutura e reação → workflow de clonagem

Fundador do Ghostfeed (@meetshukla_) descreve como rodou video understanding (Gemini) numa biblioteca de referências UGC pra rotular estrutura + reação, e como cada rótulo decide o método de clonagem: motion-based (reação, lip-sync) ou prompt-based (b-roll, talking head). Salvo por pedido de Gusta em 22/09/2026.

## Conteúdo recuperado

- **Biblioteca:** 10.000+ vídeos importados por usuários em 6 meses → 1.066 referências curadas à mão. O gargalo declarado não era gerar, era **achar a referência certa**.
- **Classificação automática:** Gemini analisou cada vídeo com escolhas fixas de **estrutura** — `reaction`, `lip-sync`, `hook + demo`, `talking head`, `B-roll` — e um rótulo separado de **reação** (`shocked`, `confused`, `angry`, choro…). Motivo: buscar uma *performance* específica, não uma categoria de nicho tipo "beauty".
- **Estrutura → workflow de clonagem:**
  - `reaction` e `lip-sync` → **motion-based cloning** (troca o creator, mantém a performance da fonte como driving video; cita "Wan 3 Smart Motion").
  - `B-roll` e `talking head` → **prompt-based cloning** (versão nova a partir da cena e da estrutura).
  - `hook + demo` → clona **só a abertura** e encaixa o demo do produto no editor; não recria o vídeo inteiro.
- **Exemplos mostrados (não assistidos aqui):** reação de choro preservando olhos/boca/microexpressões em creators diferentes; lip-sync no espelho preservando boca + gestos de mão + enquadramento. O autor diz que confere com áudio antes de escolher a versão.
- **Saída:** abertura clonada + texto de gancho + footage do produto, transição aparada pra o demo cumprir o que a abertura prometeu; depois varia creator / primeira linha / ângulo de produto e exporta o lote pra IG + TikTok.
- Link do autor: https://ghostfeed.ai/tools/reaction-inspiration-library (não visitado).

## O que isso diz pra nós

- É a **mesma tese do [[../../projects/clonador/README|Clonador]]** e das skills `trocar-avatar`/`clonar-edicao`, embalada como produto: referência → método de clone → lote. Vale como confirmação de mercado, não como novidade de técnica.
- A peça reaproveitável é a **taxonomia de entrada** (estrutura + reação como rótulos fixos), não a ferramenta — ver [[classificar-referencia-por-estrutura-antes-de-clonar]]. Nossa biblioteca spy e o `ad-radar` classificam por oferta/host/ângulo; não classificam por *estrutura de execução* nem por *reação*.
- "Clonar só a abertura" bate com o que já medimos: o gancho decide ([[gancho-de-confissao-em-primeira-pessoa]], [[frame-1-sem-piscar]]); recriar o vídeo inteiro é custo sem retorno.
- Motion-based = driving video; nosso equivalente hoje é Pruna/Kling via WaveSpeed com os cuidados de [[pruna-troca-de-pessoa-no-meio-do-clipe]] e [[avatar-segue-o-genero-da-voz]]. "Wan 3 Smart Motion" não foi verificado nem conectado.

## Fonte e limites

[Post original](https://x.com/meetshukla_/status/2102271476950819238) · [[tweet-meetshukla-biblioteca-reacoes-ugc-2026-09-22]] · [JSON bruto](../../raw/tweet-meetshukla-biblioteca-reacoes-ugc-2026-09-22.json).
Recuperado via FxTwitter em 22/09/2026 (1.568 views, 16 likes, 38 bookmarks na captura). É artigo promocional do próprio produto do autor; os vídeos não foram assistidos, nenhum resultado de performance foi apresentado nem auditado. Não altera prioridade (foco segue Launchwing) nem autoriza gasto de geração.

## Conecta com

- [[tweets-referencias-2026-09-22]] — coleção pedida por Gusta.
- [[classificar-referencia-por-estrutura-antes-de-clonar]] — a técnica extraída.
- [[throughput-de-criativo]] — a biblioteca rotulada existe pra alimentar volume de variação.
- [[reconstruir-camadas-do-criativo]] — nossa regra de qualidade que o "clone só a abertura + demo no editor" precisa respeitar.
