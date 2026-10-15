---
tipo: tecnica
tags: [clone, edicao, fidelidade, ffmpeg]
fontes: [[fonte-clone-talkinghead-wpp-indianos-2026-09-13]]
---

# Reproduzir o defeito do original em vez de corrigir

O talking head clonado em 13/09 tem um **estouro branco de 4,6 s**: o quadro inteiro lava e o karaokê congela numa palavra enquanto a fala continua. Parece defeito de encoding, e a tentação é entregar o clone "melhorado".

Não melhore. Quando o pedido é manter a edição, o defeito faz parte da peça que está rodando — e não se sabe se ele atrapalha ou se virou parte do que prende a atenção. Corrigir transforma um teste de uma alavanca (o rosto) num teste de duas.

**Como reproduzir, medindo:** o alpha do overlay sai de graça se houver no layout uma região que é **preta no estado normal** (a margem do post, por exemplo). Ali, `alpha = luminância / 255`. Varrendo os frames dessa faixa acha-se o instante exato de entrada, o fade e a saída. No caso: fade nos frames 647-651, alpha constante 0,851 nos frames 652-790, corte seco no 791.

Depois é só aplicar o mesmo no avatar antes de inseri-lo na janela: `lutrgb=r='val*0.149+217'` (o `0.149` é `1-alpha`, o `217` é `255*alpha`). Os poucos frames de fade podem ficar com o original — 5 frames não se vêem.

## Conecta com
- [[clone-talkinghead-wpp-indianos]] — onde foi usado
- [[criativo-como-layout-de-post]] — a faixa preta que serve de régua para medir o alpha
- [[medir-fronteira-de-bloco-em-video]]
