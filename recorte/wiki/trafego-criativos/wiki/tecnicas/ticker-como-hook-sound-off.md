---
tipo: tecnica
tags: [hook, formato, breaking-news, legenda, sound-off]
fontes: [fonte-formato-breaking-news-2026-08-31]
---

# Ticker como hook sound-off

No formato de noticiário/programa, a **tarja inferior ocupa o slot de legenda** — não existe caption queimada por cima. Logo, o ticker É o hook pra quem assiste sem som.

Isso impõe duas regras que se somam:

1. **Regra de não-duplicação.** Hook são três componentes simultâneos — ação visual (0–3s), primeira fala, e texto âncora. Os três precisam se complementar, nunca repetir. Se o âncora diz "why tracking apps fail" e o ticker diz a mesma coisa, você gastou dois dos três slots com uma informação só.
2. **O ticker anuncia o problema, nunca o produto.** `MUSCLE LOSS RISK LINKED TO GLP-1 WEIGHT LOSS DRUGS`, não o nome da marca. Nome de produto na tarja derruba o disfarce de programa instantaneamente — e derruba junto a única coisa que o formato tinha a oferecer.

Corolário: como a tarja precisa ser **idêntica pixel a pixel nos dois quadros** pra costurar os clipes ([[costura-de-clipes-por-tarja-persistente]]), testar variação de ticker significa **re-renderizar os dois clipes**. Trate ticker como variável de rodada de hook, não como ajuste de última hora.

Número específico no ticker rende bem no sound-off (`2.4M CHOSE TO STOP GUESSING`, `SHE HAD ELEVEN MINUTES`) — ver [[numero-especifico-quebrado]].

Aplicado em `projects/mentoria-spy/gram-detect/roteiros/2026-08-31-wpp01-copy-formato-breaking-news.md` (8 variações de ticker × 6 hooks).

Relacionado: [[formato-call-in-show]], [[nao-imitar-veiculo-real]], [[marca-depois-do-mecanismo]].
