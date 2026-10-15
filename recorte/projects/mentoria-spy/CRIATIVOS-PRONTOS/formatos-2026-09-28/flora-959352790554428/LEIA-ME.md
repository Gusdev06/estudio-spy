# Flora: 5 formatos novos (2026-09-28)

Pedido do Gusta: "mais 5 variações, uma de cada, mudando formato, headline, edição, ângulo, hooks agressivos" (exemplo dele: "quem ama também trai"). Tudo em inglês, 720×1280.

Diferente das rodadas anteriores (que só trocavam avatar sobre o molde da Flora), aqui **cada peça é um formato diferente**: roteiro, voz, edição e enquadramento próprios. A voz é gerada por IA (ElevenLabs v3, timing por palavra) e o lipsync é Pruna. Os painéis do funil (celular na mão, formulário, chats) vêm da Flora original.

| # | arquivo | dur | headline (tela) | ângulo / hook | formato & edição |
|---|---|---|---|---|---|
| f1 | `f1-love.mp4` | 20,8 s | LOVING YOU DOESN'T STOP THEM FROM **CHEATING.** | "ele me ama, não faria isso" — a versão do teu "quem ama também trai" | talking head 9:16 no quarto, punch-in por frase, karaokê grande, card do funil |
| f2 | `f2-clean-phone.mp4` | 20,4 s | THE **SWEETEST** PARTNERS HAVE THE **CLEANEST** PHONES. | celular limpo demais é suspeito | **sem rosto**: painéis do funil em tela cheia escurecida, voz sussurrada |
| f3 | `f3-red-flags.mp4` | 21,5 s | IF THEY FLIP THEIR PHONE **FACE DOWN** WATCH THIS. | call-out de 3 sinais | listicle com números gigantes vermelhos, cortes por item, no carro |
| f4 | `f4-podcast-mistake.mp4` | 18,1 s | EVERY **CHEATER** MAKES THE SAME MISTAKE. | mecanismo: apagar não some | podcast reeditado (dupla da var8), cold open, barra de progresso, zoom |
| f5 | `f5-not-crazy.mp4` | 18,0 s | I'M NOT **CRAZY.** I JUST SAW THE MESSAGES. | "não é paranoia" (validação) | split: rosto em cima, prova do funil embaixo, desabafo em 1ª pessoa |

## Blindagem de política (aplicada nas 5)
A fala **não** diz hack, spy, clone, senha nem localização — a promessa técnica fica só no painel. Sem nome, idade, lower third ou número de resultado sobre rosto (seria depoimento fabricado). Fonte: `wiki/trafego-criativos/wiki/tecnicas/` (risco-de-politica-por-angulo-spy, ugc-em-primeira-pessoa-sem-virar-depoimento).

## Produção
- Lote-fonte com roteiros, vozes, timings e scripts: `centerpag-detect/criativos/formatos-flora-2026-09-28/` (`ROTEIROS.md`, `_kit/render.py`).
- Rostos f1/f3/f5: 3 imagens novas gpt-image-2 (selfie 9:16). f4: recorte 9:16 da dupla da var8.
- As 3 mulheres se mantêm a mesma pessoa do começo ao fim (1 rosto por frame, sem 2ª pessoa, conferido no olho).
- **Custo estimado ~US$ 3,3**: 6 vozes eleven-v3 + 3 imagens + 5 clipes Pruna. Montagem é ffmpeg/PIL, custo zero.

Nada subiu no Meta.
