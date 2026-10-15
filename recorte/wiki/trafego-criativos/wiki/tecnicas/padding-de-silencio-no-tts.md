---
tipo: tecnica
tags: [locucao, tts, ritmo, medicao, spy-zap, correcao]
fontes: [[fonte-lote4-metodo-vo-2026-09-01]]
---

# Padding de silêncio no TTS — medir ritmo na duração bruta mede o silêncio, não a fala

O `minimax/speech-2.6-hd` devolve cada beat com silêncio de cabeça e cauda. Medir wpm ou
`atempo` sobre a duração do arquivo mede esse padding junto — e reprova voz boa por engano.

## O número

Sete beats do slot 2 do lote 4, padding por arquivo:
**0,494 · 0,899 · 0,986 · 1,132 · 0,836 · 1,387 · 1,121s** = **6,855s** de silêncio em
26,880s brutos. **25,5% do arquivo é silêncio.**

**⚠️ Corrigida em 2026-09-01 pelo Isca:** a primeira versão desta página dizia
"a fala do molde roda a **~~213 wpm~~**". Aquilo era **tempo de fonação** — descontava
também as pausas internas. São **quatro grandezas diferentes**, e usar a errada
subdimensiona o texto:

| grandeza | controle | o que responde | usar para |
|---|---|---|---|
| bruto (com padding) | 156,9 wpm | nada — artefato do TTS | ❌ nunca |
| **span do beat cru** | **169,3 wpm** | o beat cabe no slot? | **portão de voz** |
| **span do master montado** | **190,2 wpm** | cadência da peça pronta | **comparar com concorrente** |
| fonação (sem pausa interna) | ~~213,0 wpm~~ | quanto tempo há voz | diagnóstico, não dimensionamento |

**Pausa interna é 20,5% do span** no controle e 20,8% no slot 2 — coerente entre takes.
Ela ocupa o slot igual à fala, então descontá-la faz a conta dizer que cabe mais palavra
do que cabe. Foi esse o erro.

**O par que importa:** dimensionar texto em slot usa **span do beat cru**; comparar ritmo
com as fontes de 35 dias (178–186 wpm, medidas em vídeo pronto) usa **span do master**.
As 4 peças do lote 4 saíram em 189,9 / 195,5 / 190,0 / 189,9 contra 190,2 do controle.

O que **não** muda: o padding é real e medir no bruto continua sendo o erro que reprovou
6 vozes boas.

## O custo do erro, medido

Triando vozes pela duração bruta, **6 das 7 vozes do sistema foram reprovadas** por
"lerem devagar demais": `Casual_Guy`, `Decent_Boy`, `Deep_Voice_Man`, `Imposing_Manner`,
`Elegant_Man`, `Patient_Man`. Remedidas por fala, quase todas cabiam na grade.

Um lote cuja alavanca é a voz ([[molde-de-edicao-n-atores]]) quase saiu com uma voz só
porque a régua media padding.

## A regra

**Aparar o silêncio antes de medir qualquer coisa.** `silencedetect=noise=-40dB:d=0.08`
resolve. Só depois calcular wpm, `atempo` ou fit contra a grade.

Corolário: a janela de `atempo` de [[fit-de-locucao-por-tempo]] (1,15–1,25) foi derivada
sobre duração bruta e **não é régua de aptidão de voz**. O critério que sobrevive é
**a fala do beat cabe no slot da grade?** — ver [[beat-posicionado-na-marca]].

## Conecta com
- [[fit-de-locucao-por-tempo]] — a página que esta corrige
- [[beat-posicionado-na-marca]] — o que fazer com a fala depois de medida
- [[ritmo-de-locucao-em-wpm]] — o alvo de wpm precisa dizer se é bruto ou de fala
- [[variar-uma-alavanca-por-vez]] — a régua errada quase matou a alavanca do lote
