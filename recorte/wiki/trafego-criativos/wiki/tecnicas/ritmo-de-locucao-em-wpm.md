---
tipo: tecnica
tags: [locucao, roteiro, ritmo, medicao, spy-zap]
fontes: [[fonte-roteiro-lote3-2026-09-01]], [[fonte-roteiro-lote4-2026-09-01]], [[fonte-teardown-sarah-flores-2026-10-14]]
---

# Ritmo de locução em wpm — mire a faixa da fonte, não o seu ouvido

Ritmo de fala é **medível sem ouvir**: palavras ÷ segundos × 60. Antes de decidir que uma locução está rápida demais, meça o wpm **da peça que você está modelando** — a faixa dela é o alvo, e ela costuma contrariar a intuição.

## O caso que originou a página

A [[familia-criativos-zap-35-dias]] pede, pelo texto, um registro de confissão íntima em primeira pessoa. A intuição diz conversa calma. **Medido, as três rodam rápido:**

| Peça | Palavras | Duração | wpm |
|---|---|---|---|
| Isabella #06 | 66 | 21,34s | **186** |
| Lauren #10 | 66 | 22,27s | **178** |
| Gonçalo #20 | 70 | 23,34s | **180** |

Faixas de referência: conversa em inglês **150–170**; leitura de anúncio energética **180–200**; locutor de rádio **200+**.

**O que sobreviveu 35 dias está na faixa de anúncio, não na de conversa.** Um roteiro escrito pra ser lido a 157 wpm sairia mais lento que as três — afastando-se do que está validado enquanto tenta soar mais natural.

## ⚠️ A "confirmação" de 01/09 era espúria — corrigida no mesmo dia

Esta seção dizia que a produção confirmou a página: *"o TTS cru leu a 156,9 wpm — o número exato
que esta página previu"*. **A coincidência era real; a confirmação não.**

Os 156,9 eram palavras ÷ **duração bruta** do TTS, que carrega **16,8% de padding de silêncio** e
não aparece em nenhum artefato final ([[padding-de-silencio-no-tts]]). A previsão de "~157" foi
comparada contra uma grandeza que não é ritmo de fala. **Dois números batendo não é confirmação
quando eles medem coisas diferentes** — e bater com precisão de 0,1 deu a essa comparação uma
autoridade que ela não tinha.

**O que continua de pé, e é a maior parte da página:** o alvo medido nas fontes (**178–186 wpm**) e
o da peça que shippou (**188,2**) são ambos palavras ÷ **duração cheia da peça**, incluindo pausa.
São comparáveis entre si e seguem sendo a régua certa pra julgar uma peça pronta.

**O que caiu:** usar essa régua sobre **TTS bruto**, e a receita de `atempo` global que saiu disso
— ver [[fit-de-locucao-por-tempo]] e [[beat-posicionado-na-marca]].

**A regra de método que fica:** antes de comemorar que a previsão bateu, **confirme que os dois
números medem a mesma grandeza.** Foi o que faltou aqui.

## A consequência prática

**A unidade de escrita não é a contagem de palavras, é o ritmo.** Numa peça de 22s a 180 wpm cabem ~66 palavras; a 157 wpm, ~57. Escrever pro número errado gera um dos dois erros:

- texto longo demais → alguém acelera no render, e a decisão de ritmo passa do roteirista pro editor sem ninguém decidir nada;
- texto curto demais → a peça sai fora da faixa da fonte, e a diferença é atribuída ao ângulo em vez do andamento.

Se a voz escolhida não alcança a faixa alvo, **troque a voz ou estique o tempo — não corte texto.**

## Limite honesto do método

wpm mede **andamento**, não como a fala cai no ouvido. Alguém que fala rápido ainda pode soar natural, e um time-stretch que preserva tom não soa artificial. E as contagens saem de transcrição, que não conta pausa. Dá pra afirmar que uma peça está dentro ou fora da faixa da fonte; não dá pra afirmar que ela soa bem.

É o mesmo tipo de disciplina de [[medir-fronteira-de-bloco-em-video]]: um proxy medido, com o que ele não cobre dito em voz alta.

Relacionado: [[fit-de-locucao-por-tempo]], [[roteiro-mestre-com-n-vozes]], [[molde-de-edicao-n-atores]], [[eixos-de-variacao-de-criativo]].

## 🆕 1º ponto PT-BR — cartomante IA, nicho prosperidade (14/10/2026)

[[criativo-sarah-flores-2284342465689308]]: 223 palavras / 79,22 s = **168,9 wpm** (whisper large-v3-turbo). Por bloco: gancho 167 · história 159 · virada 169 · **oferta 182 · escassez+CTA 185**. A peça acelera onde pede a ação e desacelera na história. Só 2 pausas > 0,4 s em 80 s (silencedetect −35 dB). Arquétipo calmo, 60+ anos — não comparar direto com a faixa EN dos spy (178–186): idioma e persona diferentes, mesma regra de mirar a fonte.
