# Secret Revealed com HOOK AGRESSIVO — 10 copys e 10 avatares · 2026-09-23 → peças 112–121

Pedido do Gusta: "10 variações da 77 mudando copy e avatar (pode manter a mesma etnia). Quero um **hook agressivo no começo e na headline**, algo que prenda tocando na dor e deixe a pessoa com raiva/indignada — ex.: *ela tá te traindo, você só não quer saber*".

## O que muda em relação ao molde de 10/09
| camada | antes (peças 20–22, 71–80) | agora |
|---|---|---|
| Faixa vermelha | **recortada** do original ("HOW TO READ YOUR 📱 / PARTNER'S TEXT MESSAGES") | **redesenhada** por variação (`fazer-selo.py`): Anton branco em caixa alta sobre duas caixas #B40000, mesma geometria medida (y 176–384, largura máx. 820 px, mesmo corpo nas duas linhas) |
| Copy/áudio | o áudio original do anúncio | 10 copys novas (83–102 palavras), TTS MiniMax `Casual_Guy` 1,06× com pausas cortadas (24–28 s) |
| Karaokê | palavras do whisper do áudio original | whisper do áudio novo, mesmo desenho (Arial Rounded Bold 86, tracking 7, 1 palavra por vez) |
| Avatar | 1 rosto | 10 filipinos diferentes (roupa, cabelo, idade), `elencos/vNN.txt` |

`montar.py` é o `remontar-secret.py` de 10/09 com `--audio` e `--selo` novos e duração vinda do áudio.

## As 10 headlines (faixa) — a fala abre repetindo a mesma frase
| peça | headline | avatar |
|---|---|---|
| 112 | SHE'S CHEATING ON YOU / YOU JUST DON'T WANT TO SEE IT | moletom preto, 26 |
| 113 | EVERYONE KNOWS BUT YOU / AND THEY'RE LAUGHING | camiseta branca, 30 |
| 114 | SHE CALLS YOU CRAZY / BECAUSE IT'S WORKING | moletom cinza, 24 |
| 115 | SHE SLEEPS WITH HER PHONE / ASK YOURSELF WHY | polo azul, 33 |
| 116 | YOU PAY THE BILLS / HE PAYS FOR HER ATTENTION | camiseta verde, 28 |
| 117 | TWO YEARS OF LIES / AND YOU STILL SAY SORRY | zip hoodie, 35 |
| 118 | SHE CHANGED THE PASSWORD / THAT'S YOUR ANSWER | camisa azul + óculos, 27 |
| 119 | HE'S IN YOUR BEDROOM / THROUGH HER PHONE | camiseta vinho, 29 |
| 120 | YOU APOLOGIZE / SHE KEEPS LYING | moletom creme, 25 |
| 121 | SHE SAYS IT'S A FRIEND / FRIENDS DON'T TEXT AT 2AM | camiseta verde-escura, 31 |

Todas seguem a mesma espinha: **acusação → prova do cotidiano (celular virado, silencioso, banho com o telefone) → "você não está louco" → mecanismo (o que ela apagou continua recuperável) → CTA sem tocar no celular dela**. Nenhuma diz hack/senha/espionar.

## Conferência e custo
`conferencia/final-10.jpg` (frame com a faixa de cada peça), `casting.jpg`, `selo-orig-x-novo.png` (faixa original × redesenhada), `v01-teste.jpg`. Os 10 clipes passaram no `checar-identidade.py` (×0,99–1,07) e nenhum teve mão na lente.

**Custo real: ≈ US$ 8,3** (10 TTS 0,55 · 10 imagens 0,67 · 10 clipes Pruna 7,1). 7 dos 10 clipes falharam na 1ª tentativa por upload recusado pela WaveSpeed → `gerar-clipes.sh` ganhou retry de 5 tentativas no upload.
