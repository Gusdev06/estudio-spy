---
tipo: tecnica
tags: [edicao, spec, layout, producao, biblioteca-spy]
fontes: [fonte-varredura-biblioteca-spy-2026-08-31]
---

# Spec de edição — as medidas dos layouts spy

[[catalogo-de-layouts-spy]] diz **o que** está empilhado. Esta página diz **onde**. Sem medida ninguém reproduz — nem um editor, nem eu.

Medições lidas com régua percentual sobre frames amostrados (`projects/mentoria-spy/transcricoes/medidas/`). Precisão ±2%. As ferramentas ficam lá: `regua.py` (sobrepõe a régua) e `medir.py` (detecta fronteira de painel e barra chapada).

## Resolução e aspecto — não é uniforme

| Lote | Resolução | Aspecto | Placement |
|---|---|---|---|
| `ads-en`, `criativos-personagens` | 1080×1920 | 9:16 | Reels/Stories |
| `cr02`, `cr05` | 1080×1920 (5–6 peças) | 9:16 | Reels/Stories |
| `cr02`, `cr05` | 1080×1440 (1–2 peças) | 4:5 | Feed |
| `ingles-17-08` | 1440×2560 | 9:16 | Reels/Stories |
| `26-julho`, `ingles-com-head` | 2160×3840 | 9:16 (4K) | Reels/Stories |
| **`base-ingles`, `23-02-spy-en-es`** | **1440×1080** | **4:3 deitado** | Feed / desktop |
| família `GRAM` | 1170×2532 | 9:16 | Reels/Stories |

⚠️ **16 peças (`base-ingles` + `23-02`) são 4:3 DEITADO.** Não servem pra Reels nem Stories sem recorte — e recortar 4:3 pra 9:16 come as laterais, onde nesse layout mora o painel do funil. Se o objetivo é placement vertical, essas 16 precisam ser remontadas, não recortadas.

## L1 — faixa + head + screen · `CR05-V1`, o campeão

```
  0% ┌───────────────────────────┐
     │  HOOK amarelo, 2 linhas   │  ← 2% a 13%, Impact/condensada, contorno preto
 13% │                           │
     │      TALKING HEAD         │  ocupa o quadro inteiro por trás
     │                           │
 66% │  watermark discreta       │  ← zapem.whatstalker.com, ~66%, cinza translúcido
 72% ├───────────────────────────┤  ← fronteira dura
     │   SCREEN RECORDING        │  Accessing WhatsApp / terminal
 82% │   legenda karaokê         │  ← verde/amarela sobre o painel de baixo
100% └───────────────────────────┘
```

O hook fica **fixo os 57s inteiros**. A legenda karaokê troca a cada 2–4 palavras.

## L2 — 5 bandas · `CR05-V2`

```
  0% ┌───────────────────────────┐
     │   SCREEN / terminal       │
 30% ├───────────────────────────┤
     │ FAIXA VERMELHA, 2 linhas  │  ← 30% a 38%
 38% ├───────────────────────────┤
     │      TALKING HEAD         │
 76% ├───────────────────────────┤
     │ FAIXA VERMELHA, 1 linha   │  ← 76% a 84%
 84% ├───────────────────────────┤
     │   B-ROLL (dor)            │
100% └───────────────────────────┘
```

Duas faixas com **copy diferente**: a de cima é o mecanismo (*"track a phone without ever touching it"*), a de baixo é a promessa (*"no more lies: see the truth"*). Cinco bandas é o limite — acima disso nenhuma lê no feed.

## L3 — head | screen lado a lado · `CR05-V3` (4:5)

```
  0% ┌───────────────────────────┐
     │ FAIXA VERMELHA, 2 linhas  │  ← 0% a 15%, hook com aspas
 15% ├─────────────┬─────────────┤
     │    HEAD     │   SCREEN    │  ← 50/50 na largura
 75% ├─────────────┴─────────────┤
     │   legenda centralizada    │  ← ~85%, branca com contorno
100% └───────────────────────────┘
```

## L8 — head cheio + karaokê + insert · o mais usado (29 peças)

```
  0% ┌───────────────────────────┐
     │                           │
     │      TALKING HEAD         │  quadro inteiro, sem faixa
     │                           │
 45% │   LEGENDA KARAOKÊ         │  ← 40% a 52%, 1–2 linhas
 55% ├───────────────────────────┤
     │   INSERT DO FUNIL         │  card flutuante, 55% a 100%
100% └───────────────────────────┘
```

Duas larguras de insert em uso: **estreito** (~40% da largura, centralizado — `ingles-17-08`) e **largo** (~90% — `criativos-personagens`). O estreito deixa o rosto respirar; o largo prioriza legibilidade da UI.

## Legenda — a especificação varia por lote e é o que dá a assinatura

| Lote | Estilo | Posição |
|---|---|---|
| `cr05` | karaokê verde/amarela, contorno preto | sobre o painel de baixo, ~82% |
| `cr02` | branca caixa alta, contorno preto | ~85% |
| `ingles-17-08` | branca com **realce colorido** na palavra-chave (amarelo/rosa/ciano) | 40–50% |
| `criativos-personagens` | amarela caixa alta, contorno preto | ~52% |
| `ads-en` | branca embaixo + **hook em caixa magenta** no terço superior | hook 20–30%, legenda 75% |
| `26-julho`, `ingles-com-head` | branca com realce ciano/magenta, fonte arredondada | 40–55% |

**Regra que se repete em todos:** 2 a 4 palavras por vez, caixa alta, contorno preto grosso. Nunca frase inteira.

## Cor da faixa de hook por oferta

- **spy-zap** → vermelho `#C8102E`-ish, texto branco
- **spy-gram** → magenta/rosa, texto branco
- **wpp-01 (L1)** → amarelo puro, sem caixa, só contorno preto

## Como medir um layout novo

```bash
cd projects/mentoria-spy
python3 transcricoes/medidas/regua.py saida.jpg "caminho/video.mp4@20"   # régua percentual no frame
python3 transcricoes/medidas/medir.py "caminho/video.mp4"                # fronteiras + barras chapadas
```

Medir em vez de chutar é a mesma disciplina da skill `clonar-edicao`.

Relacionado: [[catalogo-de-layouts-spy]], [[molde-de-edicao-n-atores]], [[eixos-de-variacao-de-criativo]], [[legenda-em-lote-por-script]].
