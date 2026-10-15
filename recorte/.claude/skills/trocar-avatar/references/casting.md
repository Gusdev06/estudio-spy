# Casting e imagem-base

## A nota de casting

Escreva antes de gerar qualquer pixel. Cinco linhas, sem enfeite:

```
IDADE/GÊNERO:      mulher, 34
TRAÇO FACIAL:      sobrancelha marcada, pinta abaixo do olho esquerdo
ÂNCORA DE FIGURINO: moletom cinza gola careca + corrente fina dourada
CENÁRIO:           sala de apartamento, parede clara com moldura ao fundo
LINHA EMOCIONAL:   confidente, baixa energia, tom de quem conta um segredo
```

A âncora de figurino é o item que reaparece **literalmente igual** em todo prompt. É o que o modelo usa pra reconhecer que é a mesma pessoa entre clipes. Troque a descrição do moletom no clipe 3 e você ganha uma pessoa nova.

A linha emocional evita o erro mais comum em avatar gerado: energia de apresentador. O criativo original quase nunca é um apresentador — é alguém sentado em casa falando baixo. Essa diferença de registro sozinha já denuncia o anúncio.

## Por que vídeo com IA parece IA

| Problema | Correção |
|---|---|
| Pele limpa/perfeita demais | Poro visível, oleosidade natural, linha fina de expressão |
| Iluminação de estúdio | Luz disponível, mistura de temperaturas, sombra assimétrica |
| Personagem parado demais | Micro-movimento: piscada, inclinação de cabeça, balanço leve |
| Voz robótica | Voz original via lipsync, ou tom marcado explicitamente no prompt |
| **Mão estranha** | **Mão fora do quadro ou completamente estática** |

### A questão das mãos

Todo modelo de vídeo — Kling, Veo, Seedance — erra mão em movimento. Dedo funde, gesto fica sem física, e é o primeiro detalhe que o olho pega.

Quatro saídas, em ordem de segurança:

1. **Enquadrar em cabeça/ombros** — corta a mão fora do frame de vez.
2. **Braços cruzados** — pose estática, sem dedo pra animar.
3. **Mãos abaixo da borda** — a linha da mesa corta no pulso.
4. **Cobrir com corte** na edição, se aparecer algo estranho.

Se o criativo original tem gesto e o usuário quer manter, avise: é o ponto de falha mais provável da rodada, e vale gerar 2 variações do mesmo clipe pra ter escolha.

## Template do prompt da imagem-base

Preencha os colchetes com a nota de casting. Mantenha o ratio do original.

```
A vertical 9:16 UGC-style video frame shot on an iPhone resting on a tripod.
Medium shot at true eye level, subject seated, slightly forward-leaning posture.

SUBJECT: A [idade] [gênero] with [etnia/tom de pele], [cor] eyes, [sobrancelha],
[traço facial distintivo]. [Cabelo: cor, textura, comprimento]. Expression is
[linha emocional] — [detalhe específico da expressão, não um adjetivo genérico].

WARDROBE: [âncora de figurino, literal].

SKIN: Visible pores across the T-zone, faint expression lines, natural oil catching
light on the forehead and nose bridge. No filter, no foundation, no retouching.

FRAMING: Cropped at mid-chest — hands are out of frame.

CAMERA: Native phone lens (26mm equivalent), mild barrel softness at the edges,
slight neural blur only around hair edges.

LIGHTING: Available light — cool daylight from a window camera-left, warm lamp
spill camera-right. Soft asymmetric shadow, natural falloff. ISO grain 500-900.

BACKGROUND: [cenário], softly out of focus, everyday and lived-in — not styled.
```

**Negative prompt da imagem:**

```
studio lighting, beauty retouching, poreless skin, plastic skin, oversharpened,
symmetrical lighting, stock photo look, visible hands, extra fingers, watermark,
text overlay, oversaturated
```

## Casar com o original

Antes de aprovar a imagem, ponha lado a lado com um frame do criativo de referência e confira quatro coisas:

- **Altura da câmera** — original no nível dos olhos? A base tem que estar igual.
- **Tamanho do plano** — se o original é medium e a base é close, a energia do vídeo muda.
- **Direção da luz** — se a janela do original vem da esquerda, mantenha.
- **Densidade do fundo** — fundo cheio demais compete com o rosto; vazio demais parece estúdio.

O que você **não** deve casar: a etnia, o gênero e a idade do avatar original. Trocar isso é o ponto do exercício. O que se mantém é a **gramática visual**, não a pessoa.
