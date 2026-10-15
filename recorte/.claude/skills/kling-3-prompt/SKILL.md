---
name: kling-3-prompt
description: "Transforma uma ideia/briefing de vídeo em um prompt pronto pro Kling 3.0 — com beat map de cenas (2-6 cenas, 5/10/15s cada), linguagem de câmera de cinema, áudio nativo e consistência de personagem. Use SEMPRE que precisar criar ou melhorar um prompt de vídeo com IA: criativo de tráfego em vídeo, hook de TikTok/Reels, UGC, VSL, demo de produto, style transfer, ou quando o usuário mencionar Kling, Kling 3, vídeo com IA, prompt de vídeo, image-to-video, roteiro de vídeo gerado por IA. Também use quando a pessoa trouxer um prompt de vídeo fraco e quiser que renda mais. Baseado no guia da Alici.ai + guia de prompting oficial do fal.ai."
---

# Kling 3.0 — gerador de prompt

Você é um diretor de cena escrevendo instruções pro Kling 3.0. O modelo não responde a listas de adjetivos — ele responde a **direção de cinema**: onde a câmera está, quem se move, em que ordem, em quanto tempo.

A diferença do Kling 3.0 pros modelos anteriores é estrutural: ele gera **de 2 a 6 cenas nativas** num único job, cada uma com duração alvo (5s / 10s / 15s), com **áudio gerado junto com o movimento**. Isso muda o que é um bom prompt: em vez de um parágrafo comprimido torcendo pra sair uma edição, você **desenha a edição antes de gerar**.

## Fluxo

### 1. Entenda o job do vídeo antes de escrever

Pergunte (ou infira do contexto) só o que muda o prompt:
- **Tipo de saída**: criativo de anúncio / hook de TikTok / UGC / demo de produto / vinheta cinematográfica / style transfer.
- **Duração-alvo e formato** (9:16, 1:1, 16:9).
- **Text-to-video ou image-to-video?** Se ele tem uma imagem de referência, o prompt muda de natureza (ver seção específica).
- **Tem fala?** Se sim, use o formato de diálogo.

Se o briefing já responde isso, não pergunte — escreva.

### 2. Monte o beat map (2-6 cenas)

Antes de escrever qualquer frase de prompt, dê um **job** pra cada cena. Isso é o que evita o erro mais caro em vídeo com IA: gerar 15s e descobrir que o hook cai no segundo 8 e só meio segundo é aproveitável.

Beat map padrão pra conteúdo/ads:

| Cena | Job |
|---|---|
| 1 | **Hook** — o pico visual que trava o scroll |
| 2-3 | **Stakes** — a tensão ou o contexto |
| 4-5 | **Turn / payoff** — o momento do produto ou a resolução |
| 6 | **Exit beat** — end frame limpo pra CTA/lettering |

As fronteiras entre cenas viram os pontos de corte naturais. E como cada cena é independente, quando o hook não funciona você **regenera só a Cena 1** — não a sequência inteira.

### 3. Escreva cada cena com esta estrutura

```
Master Intent: [uma frase: o que é o vídeo, tom, gênero, o que o espectador deve sentir.]

Scene 1 (Duration: 5s):
[Ângulo de câmera + sujeito + cenário]. [Ação imediata / momento de hook].

Scene 2 (Duration: 5s):
[Novo ângulo]. [Escalada ou revelação de contexto]. [Descrição específica de movimento].

Scene 3 (Duration: 10s):
[Pico de ação ou virada narrativa]. [Posição clara do sujeito + direção do movimento].

Scene 4 (Duration: 5s):
[Beat de resolução ou clareza do produto]. [Descrição do end frame limpo].
```

A ordem interna de cada cena importa: **ângulo de câmera → sujeito → ação**. É como um diretor fala com o DP ("Medium shot, our character, she reaches for the door"): a âncora espacial vem primeiro, aí o modelo preenche os detalhes dentro de um enquadramento que já existe.

### 4. Rode o checklist antes de entregar

Ver `references/regras.md` pras 6 regras completas com o porquê de cada uma. Resumo operacional:

1. **Câmera → sujeito → ação**, nessa ordem.
2. **Trave o personagem nas Cenas 1-2.** O Kling constrói o modelo do personagem a partir dos primeiros shots que processa. Descrever de novo no meio da sequência é pedir pra ele reconciliar contradições.
3. **Movimento vence estilização.** "She spins toward camera" rende mais que "cinematic, dramatic, emotional, high-production-value". O modelo executa física melhor do que interpreta vibe.
4. **POV pra transição de estilo.** Em primeira pessoa o modelo não precisa renderizar um rosto específico atravessando uma estética estranha — só mover a câmera por um mundo novo.
5. **Mereça a duração.** Se for usar 10-15s, escreva um arco: início → escalada → resolução. Descrição estática em 15s desperdiça o orçamento de geração. Se o prompt não tem começo, meio e fim, o clipe também não terá.
6. **Image-to-video: trave primeiro, depois mova.**

### 5. Entregue

Formato de entrega padrão:

- **O prompt em inglês, em bloco de código, pronto pra colar.** Inglês porque a aderência do modelo a terminologia de cinema é melhor — a menos que o vídeo tenha fala em português, aí o diálogo vai em PT-BR dentro do prompt em inglês.
- **Duração e aspect ratio sugeridos.**
- **2-3 linhas de racional** só sobre as escolhas não-óbvias (por que esse beat map, por que POV aqui). Sem resumo do que você fez.
- **Uma alternativa de Cena 1** quando for criativo de tráfego — o hook é a variável que mais se testa, e ter a segunda versão pronta economiza uma rodada.

## Áudio nativo: descreva física, não som

O Kling 3.0 gera som junto com o movimento. O jeito de controlar isso é contraintuitivo:

**Não escreva:** "add ambient footsteps", "include crowd noise"
**Escreva:** superfície + material + movimento + tempo

`"Continuing wild dance down concrete steps, spinning and kicking, coat flapping dramatically"` — *degraus de concreto* dá a ressonância do passo, *casaco batendo* dá o som do tecido, *fumaça de cigarro rastreando* dá textura ambiente. Nenhuma instrução de som foi dada; a descrição da física gerou o áudio.

Isso também é por que o áudio nativo vale operacionalmente: você consegue ler o ritmo emocional da sequência **no momento da geração**, sem precisar sobrepor música mentalmente.

## Image-to-video: trave primeiro, depois mova

Quando existe imagem de referência, o sujeito **já está definido**. Redescrevê-lo compete com a imagem e produz drift.

- Trate a imagem como um frame congelado.
- O prompt descreve **como a cena evolui a partir dela**: reação da câmera, movimento sutil, mudança de ambiente, profundidade.
- O Kling 3.0 preserva bem identidade, layout e **texto/embalagem** da imagem de origem — o que o torna forte pra peça publicitária com marca.

Errado: `"A woman in a red jacket holding the product, she smiles..."` (redescreve o que a imagem já tem)
Certo: `"Slow dolly push-in toward the subject. She shifts weight, turns her head slightly toward camera, exhales. Steam drifts across the frame from the left. Background lights come into focus behind her."`

## Diálogo e múltiplos personagens

Quando tem fala, quatro princípios evitam que as vozes se misturem — detalhamento e exemplo completo em `references/dialogo.md`:

1. **Nome estruturado** — rótulo único e consistente por personagem. Nunca pronome ou sinônimo. `[Character A: Black-suited Agent]`, não `[Agent]... then he says`.
2. **Âncora visual** — amarre a fala a uma ação física única do personagem *antes* da fala.
3. **Detalhe de áudio** — tom e emoção únicos por personagem: `[Marina, raspy deep voice]`, `[Leo, clear fearful voice]`, mais marcadores de ritmo (fast urgent, whispering, voice cracking).
4. **Controle temporal** — palavras de ligação: "Immediately," "Pause," "Then". Sem elas, as falas colidem.

## Consistência de personagem e style transfer

Pra manter uma pessoa reconhecível atravessando estéticas radicalmente diferentes, existe uma arquitetura de 4 camadas (template de 7 shots pronto em `references/style-transfer.md`):

1. **Establish** (Shots 1-2, terceira pessoa) — trava rosto, âncora de figurino e linha de base emocional.
2. **Enter POV** (Shot 3) — vira primeira pessoa. O espectador vira o personagem.
3. **World-hop em POV** (Shots 4-6) — três trocas de estilo consecutivas. Em POV o modelo não precisa renderizar o protagonista, só o mundo.
4. **Final break** (Shot 7) — troca de mídia inteira (anime, pintura a óleo, etc).

A transição pra POV é o mecanismo-chave. Sem ela, consistência nos shots 4-6 é sorte.

## Onde o Kling 3.0 é forte e onde ele quebra

Desenhe a sequência pra jogar na força dele.

**Forte:** ação cinética rápida, revelações complexas de câmera, texturas fotorrealistas, sequência multi-shot estruturada, áudio nativo.

**Fraco:** close beauty ultra-fechado, detalhe de pele de luxo, renderização precisa de rótulo/label de produto.

Consequência prática pra criativo de tráfego: se o anúncio depende do rótulo do produto legível, **não confie na geração** — coloque o produto como still/overlay na edição, ou use image-to-video com o rótulo já correto na imagem de origem.

## Especificações

- **Cenas:** 2 a 6 por vídeo.
- **Duração por cena:** 5s, 10s ou 15s (até ~90s de saída estruturada por geração).
- **Áudio:** nativo, gerado com o movimento. Múltiplos idiomas, sotaques e code-switching; lip sync e expressão facial coerentes com a voz.
- **Acesso:** Alici.ai e API do fal.ai.

## Loop de produção (quando for peça de tráfego)

Fluxo completo em `references/producao-ads.md`. O essencial:

1. **Trave o personagem antes de escrever a história** — uma âncora de figurino, uma assinatura facial, uma linha de base emocional. Se o personagem muda entre cenas, o anúncio vira colagem.
2. **Trave a referência de estilo** — nível de realismo, paleta, linguagem de lente. É o que faz o anúncio parecer um mundo só.
3. **Gere variantes de composição antes de animar** (grid de enquadramentos, escolha o still mais forte pra leitura do produto e espaço negativo pro texto).
4. **Itere ritmo antes de qualidade de frame** — assista sem som (a história se lê?), depois com som (o ritmo bate?). Só então regenere.
5. **Regenere a cena mais fraca, não a sequência.**

## Exemplo

**Briefing:** "criativo pra low ticket de IA, hook de cara frustrado no notebook, vira ele ganhando dinheiro, 9:16"

**Saída:**

```
Master Intent: A 20-second vertical short-form ad about the shift from
grinding with no results to earning with AI. Tone: raw, real, kinetic —
shot like someone filmed it, not like a commercial.

Scene 1 (Duration: 5s):
Handheld medium close-up, slightly low angle, of a young man slumped
at a cluttered desk in a dim bedroom at 2am, laptop glow on his face.
He drags both hands down his face and exhales hard, then shoves the
laptop away across the desk. Papers scatter.

Scene 2 (Duration: 5s):
Tight over-the-shoulder shot of the laptop screen as he pulls it back.
His hand hesitates, then starts typing fast. The reflection of the
screen brightens across his glasses as the interface fills with
generated results.

Scene 3 (Duration: 5s):
Slow dolly push-in on his face, front-facing, as the expression breaks
from disbelief into a grin. He leans back in the chair, both hands
behind his head. Morning light has replaced the lamp — the room is
warmer, curtains glowing.

Scene 4 (Duration: 5s):
Wide static shot, camera locked off. He stands at the window with a
phone in hand, city waking up behind him. He turns toward camera and
holds still. Clean negative space in the upper third of the frame.
```

**Aspect ratio:** 9:16 · **Duração:** 20s (4 × 5s)

*Racional:* a Cena 4 termina em plano fixo com espaço negativo no terço superior — é ali que entra o lettering do CTA na edição, sem competir com movimento. A troca de luz (lamp → morning) carrega a passagem de tempo sem precisar de corte explicativo, o que economiza uma cena inteira do orçamento de 6.

**Alternativa de Cena 1 (hook B):** `Extreme close-up on his eyes reflecting the laptop screen, dead still. He blinks once, slowly. Cut wider as he suddenly slams the laptop shut — the room goes dark.`

## Arquivos de referência

Leia sob demanda:
- `references/regras.md` — as 6 regras de prompting com o raciocínio por trás, e o que fazer quando elas quebram.
- `references/style-transfer.md` — template de 7 shots (versão preenchida + versão em branco).
- `references/dialogo.md` — formato completo de diálogo multi-personagem.
- `references/producao-ads.md` — workflow de produção pra anúncio, do casting ao export.
