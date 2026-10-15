---
tipo: tecnica
tags: [teste, alavanca, elenco, figurino, clone]
fontes: [[fonte-clone-podcast-wpp-avatares-2026-09-13]]
---

# Roupa como variável separada do rosto

Num lote de troca de avatar, a roupa é o que se deve **segurar fixo** para o teste responder "qual rosto vende mais". Nas peças 40-43 as duas mulheres usam sempre verde-sálvia (quem explica) e preto (quem pergunta): muda o rosto, mais nada, e a peça lê como "outra dupla no mesmo programa".

Quando a roupa também muda (peça 46), a leitura contra o controle vira "outro conjunto" e não separa o que pesou. Isso não invalida a peça — só muda a pergunta que ela responde. Para isolar figurino de verdade: **repetir um elenco já testado trocando apenas a roupa**.

Na prática, a roupa precisa ser parâmetro em três lugares do pipeline, não só na geração da imagem: nas closes, no two-shot e no `video_prompt` de cada clipe — é pela roupa que o modelo de lipsync identifica quem fala num two-shot ([[pruna-no-two-shot-com-prompt-de-quem-fala]]).

## Conecta com
- [[variar-uma-alavanca-por-vez]] — o princípio
- [[clone-podcast-wpp-avatares]] — as peças 40-43 (roupa fixa) e 46 (roupa nova)
