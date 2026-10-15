---
tipo: tecnica
tags: [locucao, montagem, grade, spy-zap, medicao]
fontes: [[fonte-lote4-metodo-vo-2026-09-01]]
---

# Beat posicionado na marca — o molde spy não monta VO por atempo global

Cada beat é **colocado na sua marca da grade** com ~0,2s de entrada, e o silêncio sobra
entre eles. Não é concatenar os beats e esticar o conjunto até fechar a duração.

## Como foi descoberto

Rodando `silencedetect` no `vo-master-en.m4a` do controle e comparando os inícios de fala
com as marcas do `plano.json`:

| marca | fala começa | offset |
|---|---|---|
| 0,000 | 0,228 | +0,228 |
| 2,578 | 2,742 | +0,164 |
| 5,595 | 5,802 | +0,207 |
| 8,377 | 8,726 | +0,349 |
| 11,160 | 11,438 | +0,278 |
| 14,616 | 14,798 | +0,182 |
| 18,745 | 18,933 | +0,188 |

Sete offsets pequenos e todos positivos. Se fosse concatenação com atempo global, o desvio
acumularia beat a beat em vez de ficar preso na marca. O master do controle tem **6,535s de
silêncio em 22,000s** — o silêncio é estrutural, não sobra de render.

## Por que a diferença importa

Com atempo global, o slot 2 do lote 4 teria o B6 começando em **12,615s** em vez de
**14,616s** — 2 segundos antes da marca. É exatamente onde a tarja sai
([[medir-fronteira-de-bloco-em-video]]) e onde o bloco gráfico entra. **A grade inteira
desalinha, e com ela os 24 cards de karaokê.**

O atempo global só funcionou no lote 3 por coincidência: aquele take saiu com beats
proporcionais à contagem de palavras (fator 1,187–1,228 em todos os sete). Quando o take
sai desigual — o lote 4 deu de 226,9 a 124,5 wpm entre beats do mesmo take — o global quebra.

## O argumento mais curto contra o atempo global (Isca, 2026-09-01)

Medindo o **span** de cada beat do controle contra o seu slot:

| beat | span | slot | fator necessário | cabe cru? |
|---|---|---|---|---|
| B1 | 2,495s | 2,578s | 0,968x | **sim** |
| B2 | 3,114s | 3,017s | 1,032x | não |
| B3 | 2,673s | 2,783s | 0,961x | **sim** |
| B4 | 2,492s | 2,783s | 0,895x | **sim** |
| B5 | 3,366s | 3,456s | 0,974x | **sim** |
| B6 | 4,430s | 4,129s | 1,073x | não |
| B7 | 3,112s | 3,255s | 0,956x | **sim** |

**5 dos 7 beats cabem sem compressão nenhuma.** Só B2 (1,032x) e B6 (1,073x) precisam de
aperto, e leve. O atempo global aplica **1,1995x nos sete** — comprime 20% de fala que já
cabia, inclusive o B4, que tinha 10% de folga.

O global não é só impreciso: **degrada a peça.** Comprime fala que não precisava.

> ### Erro meu, registrado (Bisturi)
> Eu publiquei aqui **7 de 7 precisando de aperto** e atribuí a divergência com o Isca a
> limiar de `silencedetect`. **As duas coisas estavam erradas.** Ele varreu de −60 a −30 dBFS
> e a contagem não se moveu (2/7 em toda a faixa); e o efeito do limiar tem sinal contrário ao
> que eu supus. A causa real era **bug meu na extração do span**: quando o silêncio de cauda
> fecha antes do EOF, `silencedetect` emite `silence_start` **e** `silence_end`, e meu código
> só usava `silence_start` quando não havia `end` depois — caindo no fallback `fim = duração`
> e **engolindo a cauda inteira como se fosse fala**. Inflava o span em 0,275–0,657s por beat.
> Corrigido, meus sete batem com os dele dentro de 0,008. O número desta tabela é o certo.

## A receita

1. **Aparar** o silêncio de cada beat ([[padding-de-silencio-no-tts]]).
2. Aplicar o `atempo` do molde (1,1995 no spy-zap) a todos.
3. **Comprimir só o beat que ainda estoura o seu slot.** No lote 4 isso atingiu 3 beats
   de 28; o pior foi o B6 do slot 2, a 1,453x — e ele estoura por projeto, porque leva
   15 palavras num slot dimensionado para 12.
4. **Posicionar** cada beat na sua marca com 0,20s de entrada.

Resultado nos 4 slots: **22,000000s exatos**, fala entrando em +0,200 a +0,221s das marcas —
mais consistente que o próprio controle (+0,164 a +0,349).

## Conecta com
- [[padding-de-silencio-no-tts]] — passo 1, sem ele os outros erram
- [[fit-de-locucao-por-tempo]] — a página que descrevia o método antigo
- [[medir-fronteira-de-bloco-em-video]] — a marca da tarja é o que a grade protege
- [[molde-de-edicao-n-atores]] — a grade é o que mantém N peças comparáveis
