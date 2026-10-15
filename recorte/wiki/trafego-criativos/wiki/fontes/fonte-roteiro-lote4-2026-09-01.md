---
tipo: fonte
tags: [roteiro, spy-zap, lote-4, grid-de-atores, molde-validado]
data: 2026-09-01
origem: projects/mentoria-spy/centerpag-detect/roteiros/2026-09-01-lote4-grid-atores-roteiro-mestre.md
raw: raw/2026-09-01-roteiro-lote4-grid-atores.md
---

# Fonte — roteiro mestre do lote 4 (grid de 4 atores, spy zap)

Roteiro que estende o molde das 35 dias para **4 slots variando só rosto e voz**, com toda a geometria e todos os tempos **medidos na peça já renderizada** em vez de estimados.

## O que a fonte trouxe de novo

1. **O fit de locução por tempo.** O TTS leu a 156,9 wpm; o molde pede 188,2. O master fechou em 22,000s por `atempo` de **1,1995**, não por corte de texto. Virou [[fit-de-locucao-por-tempo]] — e confirmou na produção a errata que [[ritmo-de-locucao-em-wpm]] tinha previsto.
2. **A regra do karaokê verde.** 14 cards com keyword verde `#25D366` contra 10 inteiramente brancos, com padrão legível: setup branco, payoff colorido. Virou [[karaoke-verde-marca-o-payoff]].
3. **A tarja sai exatamente no início do B6.** Frame 438 é o mesmo frame em que o beat 6 começa (14,600s), e volta no 589 (19,633s) — 0,888s dentro do B7. Não é aproximação: é o mesmo número. Tarja presente em 77,12% da peça.
4. **Voz não registrada = teste não auditável.** O `jobs.log` da rodada anterior não gravou `voice_id`. Num lote em que a voz É a alavanca, isso impede provar depois que as leituras eram distintas. Registrado em [[fit-de-locucao-por-tempo]].
5. **Escrever contra a grade, não contra o relógio.** A copy do slot 2 (própria) foi escrita com a **mesma distribuição de palavras por beat** da copy do slot 1 — 8·11·9·8·11·12·9 contra 8·12·9·8·11·12·9 — para cair no mesmo timeline sem nenhum ajuste de montagem. Aplicação direta de [[variar-uma-alavanca-por-vez]] dentro do slot que troca a copy.

## Contradição registrada

O briefing do lote listava como FIXO o texto de tarja **do concorrente** (`CLONE YOUR WIFE'S OR HUSBAND'S / WHATSAPP RIGHT NOW`). **A peça que shippou usa outro texto** (`YOU DON'T NEED THEIR PHONE. / YOU NEED THE NUMBER.`), conferido em `kit/tarja.png` e em 4 frames fora da janela sem tarja.

Consequência que torna isso relevante e não cosmético: adotar o texto do briefing faria o slot 1 diferir do controle por **tarja + rosto + voz** — três alavancas, leitura zero. Prevalece o texto que shippou; a linha do concorrente, se for testada, vira lote separado com o rosto travado.

## Medidas que a fonte fixa

| Item | Valor |
|---|---|
| Saída | 1170×2532, 30 fps, 660 frames, **22,000s** |
| Tarja | `y 0–497` (19,67%), verde `#029602` |
| Janela sem tarja | frames **438–588** (14,600–19,633s) |
| Bloco gráfico | 1170×936, `y 1596–2532` |
| Card de karaokê | 1170×220 em `y 1676` · branco `#FFFFFF` · keyword `#25D366` |
| Grade dos 7 beats | 0,000 · 2,578 · 5,595 · 8,377 · 11,160 · 14,616 · 18,745 → 22,000 |
| Custo estimado | US$ 1,84/slot de lipsync · US$ 7,37 nos 4 |

## Em aberto

- **Faltam faces:** o pool `criativos-personagens` tem 3 clipes masculinos para 4 slots, e o rosto do controle não sai desse pool.
- **Pendente do Gusta:** o beat 6 no registro da fonte (o de anti-detecção, que o roteirista não escreve) e o texto da tarja.

## Gerou
- [[fit-de-locucao-por-tempo]] — nova
- [[karaoke-verde-marca-o-payoff]] — nova
- [[ritmo-de-locucao-em-wpm]] — atualizada com a confirmação de produção

## Conecta com
- [[fonte-teardown-lote3-2026-09-01]] — o teardown que definiu o molde
- [[fonte-roteiro-lote3-2026-09-01]] — o roteiro que este estende
- [[molde-de-edicao-n-atores]] · [[variar-uma-alavanca-por-vez]] · [[ugc-em-primeira-pessoa-sem-virar-depoimento]]
