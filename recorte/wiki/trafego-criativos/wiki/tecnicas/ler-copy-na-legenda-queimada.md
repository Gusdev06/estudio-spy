---
tipo: tecnica
tags: [copy, transcricao, swipe, ad-library, metodo, spy-zap]
fontes: [[fonte-selecao-atores-lote4-2026-09-01]], [[fonte-teardown-sarah-flores-2026-10-14]]
---

# Ler a copy na legenda queimada — quando o anúncio não publica o texto

Em card agrupado a Meta esconde o texto principal, e o `.txt` do swipe só guarda headline/CTA/link. Mas a **legenda karaokê queimada no vídeo** é a transcrição que o próprio anunciante fez da locução: fonte verbatim, sem Whisper e sem chute.

## Quando usar

Quando a copy que interessa é **falada** e não é campo de anúncio. No swipe `go.centerpag.com` as três peças de 35 dias são cards agrupados: `TEXTO PRINCIPAL: (o card agrupado não exibe o texto principal)`. O texto de venda vive na locução — ver [[fonte-teardown-lote3-2026-09-01]].

⚠️ **Cuidado com a hierarquia de fontes.** Se a tarefa disser "confira contra o `.txt`, ele manda", confira **se o `.txt` tem o campo** antes de obedecer. No lote 4 ele não tinha: mandava sobre headline/CTA (onde não havia divergência) e era mudo sobre a locução (onde havia). Hierarquia de fonte só vale campo a campo.

## Método

1. `fps=8`, região baixa do quadro (a legenda desce quando entra insert — não fixe a banda).
2. Máscara de glifo: branco (`>205`) **ou** verde saturado, **com pixel escuro 4px abaixo** (o contorno). Sem a exigência de contorno, tela de celular e parede clara entram como texto.
3. Por frame, ache a **janela de 44px mais densa em glifo** e recorte ali — é o que evita tile de 12.000px de altura quando o fundo é claro.
4. Deduplique por XOR das máscaras (>40% de diferença = legenda nova).
5. **Leia os strips.** O karaokê muda 1 palavra de cor por vez, então a mesma frase repete em vários frames — isso é confirmação de graça.

## O que rendeu no lote 4

Duas locuções de ~22s conferidas palavra por palavra contra o teardown:

- **Lauren** — bate integralmente, zero divergência.
- **Gonçalo** — uma divergência: o teardown trazia `100% discrete`, a legenda mostra **`100% discreet`** em 7 frames seguidos. Uma letra, mas é copy verbatim de anúncio que sobreviveu 35 dias.

Corrigido com o valor velho marcado, não apagado. **Contagem de palavras idêntica** — o que preserva a grade de palavras por beat que o roteiro usa.

## 🆕 Caso 14/10 — legenda e whisper divergem, e cada um erra num lugar

No [[criativo-sarah-flores-2284342465689308]]: a legenda mostra **"ENTÃO DEIXA EU"** onde o whisper começa em "Deixa" (7,22 s) — e em 7,01 s o áudio é silêncio digital de costura, então o "Então" é curtíssimo ou não existe: **ouvir antes de cortar**. A legenda escreve **PRA/PRO** onde o whisper normaliza "para" (a fala é coloquial: a legenda ganha). Mas a legenda também erra: **"PORQUE"** (certo: "por que") e quebra "GRATUITAMENTE PRA VOC / Ê". Regra: legenda é fonte do que foi dito, não de ortografia.

## Conecta com

- [[karaoke-verde-marca-o-payoff]] — a mesma legenda, lida como recurso de edição.
- [[ritmo-de-locucao-em-wpm]] — o outro número que sai da transcrição da locução.
- [[fonte-teardown-lote3-2026-09-01]] — onde as duas locuções foram transcritas primeiro.
- [[nao-imitar-veiculo-real]] — limite do que se copia literal de um anúncio de terceiro.
