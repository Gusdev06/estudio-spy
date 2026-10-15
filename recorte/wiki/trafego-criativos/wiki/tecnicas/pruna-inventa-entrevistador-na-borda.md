---
tipo: tecnica
tags: [pruna, lipsync, podcast, defeito, custo]
fontes: [[fonte-clone-podcast-wpp-avatares-2026-09-13]]
---

# Pruna inventa um entrevistador na borda

Em cena de podcast, o `pruna-ai/p-video/avatar` completa o enquadramento por conta própria: no clone de 13/09 ele inseriu **um homem de barba entrando pela borda esquerda** em 2 de 3 clipes de close. O defeito não aparece no primeiro frame — surge a partir do segundo ou terceiro segundo, então conferir só a abertura engana.

Trava que funcionou, no `video_prompt`:

> SOLO SHOT: exactly one person in the frame at all times. Nobody else is visible, no second person, no one enters or appears at the edges of the frame. Podcast studio, locked-off camera on a tripod. The background stays completely static and unchanged.

Para two-shot, o inverso, nomeando os papéis: "EXACTLY TWO women … and nobody else ever appears; only the woman on the RIGHT is talking; the woman on the LEFT listens with her mouth closed."

Custo de descobrir: US$ 0,40 de clipes jogados fora num lote de US$ 1,75.

**A trava não é suficiente sozinha (13/09, lote de 3 elencos).** Mesmo com o "SOLO SHOT", o defeito voltou em 2 de 15 clipes — homem de camisa jeans ocupando o primeiro plano. O que resolveu foi **trocar a seed** (21 e depois 99) somado a uma trava que *enumera* o que não pode entrar: "no man, no interviewer, no guest, no shoulder, no back of a head, no arm, no hand entering from any edge". Um dos clipes só cedeu na terceira tentativa.

Daí a regra de método: **conferir uma folha de frames do clipe inteiro, de cada clipe, antes de montar**. O defeito nunca aparece no primeiro segundo, então revisar a abertura não detecta nada.

**Mãos na lente (17/09):** mesma classe de defeito, e a lição é a mesma que a do two-shot: o modelo obedece melhor a uma **pose descrita em positivo** ("RIGHT arm hangs relaxed at his side, out of frame, for the whole clip") do que a uma lista de proibições. A trava negativa falhou em 3 de 5 clipes; a positiva acertou os 3.

**Celular em quadro (17/09, lote Zap):** citar o objeto proibido também falha — "phone held in his LEFT hand, out of frame" fez o modelo mostrar o celular por 9 s em 1 de 5 clipes. Regra: descrever só a pose visível ("both arms relaxed at his sides, out of frame, nothing held in front of him"), sem nomear o que não deve aparecer.

## Conecta com
- [[pruna-no-two-shot-com-prompt-de-quem-fala]] — a regra irmã, sobre quem fala
- [[clone-podcast-wpp-avatares]]
- [[criativo-como-layout-de-post]]
