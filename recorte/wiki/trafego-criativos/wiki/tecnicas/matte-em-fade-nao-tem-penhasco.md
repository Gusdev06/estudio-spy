---
tipo: tecnica
tags: [medicao, edicao, layout, matte, fade, teardown, metodo, l10]
fontes: [[fonte-medicao-matte-fade-wpp01-2026-09-11]], [[fonte-teardown-edicao-wpp01-2026-09-01]]
---

# Matte em fade não tem penhasco — fração de preto dá o início, o platô dá o fim

Quando uma matte termina em gradiente, "onde ela acaba" são **dois números** (onde deixa de ser 100 % preta e onde o vídeo volta a ser pleno) e **nenhum deles é uma fronteira**: fade ≠ degrau, e o detector de penhasco devolve ruído com cara de resposta.

## O caso

Matte do topo do [[criativo-wpp01-1762552938111855]] (360×640). O teardown de 01/09 achou `y=96` por fração de preto e o registrou como a única fronteira medível da peça. Em 11/09 o Bisturi remediu com 58 frames, colunas de margem fora do texto:

| medida | valor (y) |
|---|---|
| 100 % preta (luma < 20, frame médio) | **93** (87/89 em frames isolados; 93–103 em 5 colunas; 91–97 no `README-l10`) |
| std temporal: matte pura → y 85–95 | 0,03 → **1,7–2,5** (50–80×) |
| 10 / **50** / **90** % do platô de variância (17,0 em y 130–200) | 67 / **125** / **141** |
| penhasco (argmax do diff, y 80–125) | **não existe** — margens 1,01–1,19× |

Os três limiares de "100 % preta" (93, 96, 91–97) **não divergem** — são o mesmo início lido com limiares diferentes. O que o teardown não tinha visto é que **a partir dali não vem imagem plena: vem ~50 px de fade** (93 → 141). No zoom ×8 a silhueta do microfone atravessa y 90/93/96 até encostar no texto do hook.

## A regra

[[medir-fronteira-de-bloco-em-video]] já dizia: *primeiro estabeleça que a fronteira existe, só depois meça a margem*. Este caso mostra que "existe" tem **três respostas**, não duas:

| a borda é… | o que medir | o que reportar |
|---|---|---|
| **degrau** (chapado → conteúdo numa linha) | penhasco + margem ≥ 2× | uma linha |
| **alpha sem borda** (card composto, gradiente lateral) | nada — não há número | "não medível" |
| **fade** (chapado → gradiente → conteúdo) | **fração de preto** = início · **platô de variância** (90 %) = fim | **dois números + a largura** |

**A matte tem início, não borda.** Fração de preto responde "até onde é só matte"; platô responde "a partir de onde é só vídeo"; a diferença é a largura do fade. Rodar detector de penhasco no meio disso devolve o argmax do ruído (aqui y 113–125, mudando por coluna) com margem ~1× — o sintoma clássico de "não há fronteira" da página-mãe, só que agora a matte existe de fato.

**Sintoma de que você está num fade e não num degrau:** a fração de preto e o platô discordam por dezenas de px, e a variância nas linhas logo abaixo do "100 % preta" já é 50× a da matte pura.

## Consequência pro molde (e por que não mudou)

Nosso molde L10 corta seco em `y 288` (1080p, = 96 × 3) — reproduz o **início** e ignora o fade (fim ≈ 423 em 1080p). No lote de 11/09 **não se mexeu**: a alavanca é o gancho ([[gancho-como-alavanca-unica-matte-mais-call-out]]) e o corte duro já rodou nas EX A/B/C — trocar agora seria alavanca extra ([[variar-uma-alavanca-por-vez]]). Fica como **opção de lote futuro**: substituir o `pad … :black` do `[actor]` por gradiente preto de y 240 → 420 (1080p), uma linha no `remontar-l10.py`, custo zero (proposta do Bisturi, no README do lote).

Corrigido **por marcação, não apagamento**: o `y=96` continua no teardown, com nota datada ao lado.

## Conecta com

- [[medir-fronteira-de-bloco-em-video]] — página-mãe; este é o terceiro caso da pré-condição "a fronteira existe?".
- [[criativo-wpp01-1762552938111855]] — a peça medida.
- [[card-flutuante-sobre-plano-unico]] — o mesmo criativo já tinha o caso "alpha sem borda" (laterais do card).
- [[variar-uma-alavanca-por-vez]] — por que o achado não virou mudança de molde no mesmo lote.
- [[nao-somar-medicao-emprestada-como-cruzamento]] — o 93 e o 96 são medições independentes (pipelines diferentes) que concordam; o 91–97 do `README-l10` é uma terceira.
