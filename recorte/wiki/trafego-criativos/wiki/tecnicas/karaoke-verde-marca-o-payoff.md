---
tipo: tecnica
tags: [legenda, karaoke, spy-zap, molde-validado, sound-off]
fontes: [[fonte-roteiro-lote4-2026-09-01]], [[fonte-teardown-lote3-2026-09-01]]
---

# Karaokê com keyword em verde — o verde marca o payoff, não a linha

Legenda karaokê de 2–4 palavras em que **só a palavra que carrega o beat vai em cor**; a linha de setup fica branca inteira. Colorir toda linha destrói o próprio mecanismo.

## A medida

Peça `lote3-isabella` (molde das 35 dias), 24 cards em 22,000s: **14 com keyword verde, 10 inteiramente brancos.**

O padrão card a card (B=branco, V=verde):

```
k01 B  k02 V  k03 V  k04 B  k05 V  k06 B
k07 V  k08 B  k09 V  k10 V  k11 B  k12 V
k13 B  k14 V  k15 B  k16 V  k17 V  k18 V
k19 B  k20 V  k21 B  k22 B  k23 V  k24 V(inteiro)
```

Especificação: card 1170×220 em `y 1676`, texto centralizado, branco `#FFFFFF`, keyword **`#25D366`** (o verde do WhatsApp — não é o verde da tarja, que é `#029602`), contorno `#080808`.

## A regra que o padrão revela

Os cards brancos são todos **linha de entrada**: `LAST MONTH I`, `IT TOOK`, `I NEVER TOUCHED`, `YOU TYPE`, `IT CONNECTS`, `THEN YOU SEE`, `SOMEONE WAS SURE`, `YOU NEVER NEED`, `SEE IT YOURSELF`, `BEFORE YOU SPEND`.

Os verdes são todos **o substantivo ou verbo que fecha o beat**: `GUESSING`, `MINUTE`, `PHONE`, `NUMBER`, `CHECK`, `OWN`, `CONVERSATIONS`, `DISAPPEARED`, `PASSWORD`, `INSTALLED`, `WEEK`.

Ou seja: a legenda respira em dois tempos — **setup branco, payoff colorido** — e o olho aprende a cadência nos primeiros 3 segundos. Com 100% das linhas coloridas o verde vira fundo e para de sinalizar qualquer coisa. **A proporção é parte do molde**, não acabamento.

Duas exceções que também são regra:
- **`k17`/`k18` verdes seguidos** (`NO PASSWORD` / `NOTHING INSTALLED`) — quebra de objeção em rajada; o verde consecutivo faz o efeito de martelo.
- **`k24` inteiro verde** (`WONDERING`) — único card totalmente colorido, é o fecho.

## Por que importa para sound-off

O anúncio é consumido sem som. O verde é o que faz a **promessa** ser lida mesmo quando ninguém escuta a locução — mesmo trabalho que [[ticker-como-hook-sound-off]] faz na tarja, mas dentro da fala. As três camadas continuam não se repetindo: tarja, karaokê e UI dizem coisas diferentes ([[tres-camadas-de-gancho-sem-repeticao]]).

## Ao replicar em copy nova

Manter **a mesma cadência de cards e o mesmo padrão B/V** quando a peça nova é variante de copy dentro do mesmo teste. Se o slot novo mudar a copy **e** o ritmo de legenda, viram duas alavancas e a leitura some ([[variar-uma-alavanca-por-vez]]).

## Conecta com
- [[legenda-em-lote-por-script]] — como renderizar os N cards
- [[ticker-como-hook-sound-off]] — a camada de cima do mesmo problema
- [[tres-camadas-de-gancho-sem-repeticao]] — o verde é a 3ª camada, e não repete as outras duas
- [[spec-de-edicao-layouts-spy]] — as medidas do molde onde este karaokê vive

## Cards por beat é variável livre — e card lento denuncia beat subdividido de menos (01/09)

Quando um beat ganha palavras, o reflexo é espremer mais texto nos mesmos cards. **O certo é somar
um card** — e às vezes isso *melhora* o ritmo em vez de degradar.

Caso medido: o B6 de uma peça de 22,000s passou de 12 para 15 palavras.

| | 4 cards | 5 cards |
|---|---|---|
| Palavras por card | 3,75 *(todo card no teto da regra 2–4)* | **3,0** |
| Tempo por card | 1,032s | **0,826s** |

**0,826s é o ritmo dominante da peça** — os cards de B1, B5 e B7 rodam a 0,829 / 0,841 / 0,812s. Ou
seja, **os 4 cards do B6 já eram os mais lentos da peça inteira**, e ninguém tinha notado porque o
beat cabia. O texto maior só expôs uma irregularidade que já estava lá.

**A regra que sai disso:** ao montar a grade de karaokê, **compare o tempo/card entre beats**, não
só as palavras/card. Um beat cujo card fica visivelmente mais lento que os vizinhos está
subdividido de menos — e a hora de corrigir é antes de renderizar, não quando o texto muda.

⚠️ Contrapartida honesta: em teste de **uma alavanca** ([[variar-uma-alavanca-por-vez]]), mudar a
cadência de cards de um slot o afasta do controle por mais uma coisa. Só vale quando a copy daquele
slot **já é** a alavanca declarada — e mesmo assim, mexer **num beat só**, mantendo os outros seis
idênticos.

Relacionado: [[fit-de-locucao-por-tempo]] — o `atempo` conserta o andamento global; a contagem de
cards conserta a densidade local. São dois botões diferentes e os dois erram sozinhos.
