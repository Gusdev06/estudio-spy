---
tipo: roteiro-criativo
atualizado: 2026-08-31
oferta: spy zap / detecção de traição
versao-de: 2026-08-31-wpp01-copy-formato-breaking-news.md (Roteiro D, EN)
idioma: PT-BR
tags: [roteiro, breaking-news, dublagem, ptbr]
---

# Roteiro D — versão PT-BR

Não é tradução literal. O registro de telejornal brasileiro é diferente do americano: mais
"a gente acompanha", menos "we're following". Mantidos os tempos de cada clipe pra o corte
existente servir.

## Fala (os 5 clipes)

**C1 — ÂNCORA · 11s**
> "A gente acompanha hoje uma preocupação que não para de crescer — de quem já desconfiou que
> o parceiro esconde alguma coisa no celular."
>
> "Quase todo aplicativo feito pra isso falha. E a gente soube hoje que a culpa não é do
> aplicativo. Quem explica é Elena Ross."

**C2 — ESPECIALISTA · 15s**
> "Todos eles precisam do celular na sua mão. Fisicamente. E é justamente isso que você nunca
> vai conseguir."
>
> "Só que o celular nunca foi onde o registro fica guardado. Toda mensagem, todo texto apagado,
> toda localização — fica tudo fora do aparelho."

**C3 — ÂNCORA · 5s** *(linha de reação)*
> "É por isso que tanta gente diz que já tentou três, quatro aplicativos diferentes — e continua
> sem saber de nada."

**C4 — ESPECIALISTA · 10s**
> "É isso que muda o jogo."
>
> "Você põe o número. Não instala nada. Nem no celular da pessoa, nem no seu. Dez minutos depois
> você está lendo o que já estava lá."

**C5 — ÂNCORA · 4s**
> "Você não precisa continuar se torturando com o 'e se'. A primeira busca é grátis."

**Notas de tradução**
- `the record lived` → **"onde o registro fica guardado"**. É o beat de reframe, o pico do vídeo.
  Meio segundo de silêncio depois. Não traduza como "armazenado" — burocratiza e mata a frase.
- `not on their phone` → **"nem no celular da pessoa"**, não "dele/dela". Mantém a peça neutra
  e servindo os dois públicos.
- `torturing yourself with what if` → **"se torturando com o 'e se'"**. É a copy 12x do swipe;
  preserve a palavra *torturar*, que é o que carrega.

## Texto em tela

| Elemento | PT-BR | Chars |
|---|---|---|
| Programa (tarja) | `O SINAL` | 7 |
| Ticker | `POR QUE OS APPS DE RASTREIO QUASE SEMPRE FALHAM` | 47 |
| Sticker linha 1 | `TODO MUNDO DESCOBRE` | 19 |
| Sticker linha 2 | `O PARCEIRO É` | 12 |
| Sticker linha 3 | `SEMPRE O ÚLTIMO` | 15 |
| Card final | `A PRIMEIRA BUSCA É GRÁTIS` | 25 |

⚠️ **Não use nome de programa brasileiro real.** Nada de Linha Direta, Fantástico, Profissão
Repórter. `O SINAL` é inventado, que é a regra ([[nao-imitar-veiculo-real]]). Alternativas:
`ALERTA DIGITAL`, `PONTO DE VIRADA`.

Acentos renderizam normal no `drawtext` com Arial Black — testado.

**Comando pra trocar só o texto em tela (grátis, não regera vídeo):**

```bash
PROGRAMA="O SINAL" \
TICKER="POR QUE OS APPS DE RASTREIO QUASE SEMPRE FALHAM" \
STK1="TODO MUNDO DESCOBRE" STK2="O PARCEIRO É" STK3="SEMPRE O ÚLTIMO" \
CTA="A PRIMEIRA BUSCA É GRÁTIS" \
./montar.sh
```

## Copy do anúncio (Meta)

**Texto principal** — 125 caracteres visíveis, gancho na frente.

| # | Copy | Chars |
|---|---|---|
| P0 | 2,4 milhões de pessoas já pararam de se torturar com o "e se". Escolheram saber. 👇 | 83 |
| P1 | Você não tem um problema de prova. Você tem um problema de acesso. 👇 | 67 |
| P2 | Todo mundo descobre. O parceiro é sempre o último. 👇 | 50 |
| P3 | O celular nunca foi onde ficava o registro. É por isso que os apps falham. 👇 | 75 |
| P4 | Apagado não é sumido. Só quer dizer que você não está olhando no lugar certo. 👇 | 78 |
| P5 | Três apps. Todos pediam o celular na mão dela. Ela nunca conseguiu. 👇 | 68 |
| P6 | Ela pôs o número dele. Dez minutos depois estava lendo mensagens que ele apagou em março. 👇 | 90 |

P0 é o controle — é a copy mais repetida do swipe (12 de 27 anúncios) traduzida.
P2 é o sticker virado copy: testar se o que funciona queimado na tela funciona no texto.

**Títulos** — 40 caracteres recomendados.

| # | Título | Chars |
|---|---|---|
| T0 | Teste Grátis ✅ | 14 |
| T1 | Por que os apps de rastreio falham | 34 |
| T2 | Sem instalar. Sem pegar o celular. | 34 |
| T3 | Primeira busca grátis | 21 |
| T4 | Apagado não é sumido | 20 |

**Descrições** — 30 caracteres recomendados.

```
Primeira busca grátis    (21)
Sem login                (9)
Não instala nada         (16)
```

### Variação por público

O vídeo é neutro; o que separa as campanhas é a copy. **Conjuntos separados**, nunca a mesma
variação dentro do mesmo conjunto.

**Público feminino** (checando um homem) — P5, P6 como estão acima.
**Público masculino** (checando uma mulher):

| # | Copy | Chars |
|---|---|---|
| M5 | Três apps. Todos pediam o celular na mão dele. Ele nunca conseguiu. 👇 | 68 |
| M6 | Ele pôs o número dela. Dez minutos depois estava lendo mensagens que ela apagou em março. 👇 | 90 |
| M7 | As amigas dela já sabem. E você? 👇 | 33 |

## Pra ter a peça falada em português

O corte atual tem o áudio em inglês. Regerar os 5 clipes com a fala em PT-BR custa **~$7,56**
no Kling 3.0 Pro (saldo atual: $9,73). Os frames-base não mudam — mesmos âncora e especialista,
mesmo estúdio.

No prompt do Kling: corpo em inglês (a aderência a termo de câmera é melhor), **a fala entre
aspas em português**, e o rótulo de tom em inglês com o sotaque explícito:
`[Character A: Anchor, calm measured broadcast voice, unhurried, Brazilian Portuguese]`.
