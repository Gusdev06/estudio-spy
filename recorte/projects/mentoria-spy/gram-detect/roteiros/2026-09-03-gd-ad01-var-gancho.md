---
tipo: roteiro
atualizado: 2026-09-03
tags: [roteiro, spy-gram, gd-ad01, variacao-gancho, custo-zero]
peca_base: criativos-crus/spy-gram/ads-en/GD-AD01.mp4
md5_base: 4a6906ae22e2a3c483e9fa7ccf2435fa
plano: gram-detect/referencias/proprios-2026-09-03/01-gd-ad01.md (secao 14)
alavanca: texto da caixa rosa do gancho
custo: zero
---

# GD-AD01 — variação B: só o texto da caixa do gancho

Teste da esteira. Duas entradas: **Ad A** = GD-AD01 original, intocado, controle. **Ad B** = o mesmo arquivo com **uma** mudança: o texto dentro da caixa rosa dos primeiros 7,8 s.

## A frase

| | Texto |
|---|---|
| Original (Ad A) | `I found something I wasn't even looking for...` |
| **Nova (Ad B)** | **`I wasn't even supposed to see this...`** |
| Linha 1 | `I wasn't even supposed` |
| Linha 2 | `to see this...` |

Apóstrofo curvo (’), caixa mista (só o "I" maiúsculo), reticências no fim da linha 2. Copiar exatamente como está, sem ponto final a mais, sem caixa alta.

Por que essa (do Peneira, seção 14): o original diz "achei algo que não procurava"; a nova diz "vi algo que não era pra eu ver". Mesma primeira pessoa, mesmo loop aberto, mas já planta que **alguém escondia**, que é o mecanismo da fala ("when someone is trying to hide something, they leave small traces"). Hipótese, não promessa.

## Quando a caixa entra e sai

Medido no mp4 (30 fps, 978 frames) por mim e pelo Peneira, independentes, mesmo resultado:

| evento | frame | tempo |
|---|---|---|
| caixa entra | 0 | 0,000 s, já inteira no primeiro frame, sem animação |
| último frame com caixa | 233 | 7,767 s |
| caixa some | 234 | 7,800 s, corte seco, sem fade |
| reaparece? | não | nada de rosa no resto da peça |

Ou seja: a caixa nova cobre a original **do frame 0 ao 233** e desaparece **no frame 234**, junto com a transição glitch pro card do app.

## Spec da caixa (a mesma da original, pro Bisturi cobrir)

Referência completa na seção 14 do teardown. Resumo:

| item | valor |
|---|---|
| retângulo | x 107, y 862, **867 × 197 px** (1080×1920) |
| fundo | #EC0054 opaco (seção 7 mediu #E80052; qualquer um cobre) |
| texto | #F0FF0E, contorno preto 3–4 px |
| fonte | sans geométrica bold (Poppins Bold ou Montserrat ExtraBold), ~60 px |
| linha 1 | y 899, centralizada em x 540 |
| linha 2 | y 974, centralizada em x 540 |
| alinhamento | centralizado nas duas linhas |

A frase nova tem 37 caracteres (22 + 14) contra 46 (26 + 19) da original, então cabe na mesma caixa com a mesma fonte e o mesmo tamanho. Não encolher nem esticar a caixa.

## TUDO O RESTO É IDÊNTICO AO ORIGINAL

Não reescrever, não regerar, não retocar:

- **A fala**: mesmo áudio, mesma voz, mesmos 32,6 s. Copiar a trilha de áudio sem reencode (`-c:a copy`).
- **A legenda karaokê**: branca, 2–3 palavras, mesma posição e mesmo tempo. Não tocar.
- **Os 8 cortes** (7,8 · 10,7 · 16,4 · 19,7 · 22,2 · 25,9 · 27,3 · 29,2): iguais.
- **Os painéis do app**, o story bloqueado, o painel "LIVE INTERCEPTION", o glitch e as setas finais: iguais.
- **O rosto**: o mesmo. Nada de troca de personagem neste lote.
- **Duração e resolução**: 32,6 s, 1080×1920, 30 fps, 978 frames.

Se qualquer coisa além do texto da caixa mudar, o teste deixa de ter uma alavanca só e não diz mais nada.

## Conferência de saída (pro Bisturi)

1. Frame 0 e frame 90 (3,0 s): zero pixel rosa da caixa antiga fora do retângulo novo (mesma máscara de cor da seção 14).
2. Frame 234 em diante: nada de rosa.
3. Áudio bit a bit igual ao original (md5 da trilha extraída).
4. Fora da região da caixa nos frames 0–233, e em todo frame de 234 a 977, diferença contra o original só de ruído de reencode.

## Nome sugerido

`GD-AD01-B-caixa-supposed.mp4`, na pasta do Bisturi em `criativos/`.

## Custo

**Zero.** Só edição sobre arquivo existente. Nenhuma geração de vídeo, voz, rosto ou imagem.
