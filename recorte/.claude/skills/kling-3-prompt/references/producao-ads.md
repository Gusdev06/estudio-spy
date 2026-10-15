# Workflow de produção pra anúncio

Prompting é metade. A outra metade — a que gera qualidade repetível em vez de sorte — é o workflow em volta.

## Passo 1: trave o personagem antes de escrever a história

Defina o personagem como uma **nota de casting**: uma âncora de figurino, uma assinatura facial, uma linha de base emocional. Você vai usar isso em todos os shots.

Se o personagem muda entre cenas, o anúncio parece uma colagem — e o espectador sente isso antes de conseguir nomear.

Exemplo de nota de casting:
> Homem, 28, cabelo escuro bagunçado, barba de 3 dias, moletom cinza com capuz (âncora de figurino em todos os shots), olhar cansado que só quebra no payoff.

## Passo 2: trave uma referência de estilo visual

Antes do storyboard, comprometa-se com:
- **nível de realismo** (documental cru / comercial polido / híbrido)
- **paleta de cor**
- **linguagem de lente** (wide, handheld, slow dolly, golden hour, neon night)

É isso que faz um anúncio parecer **um mundo só** em vez de três cenas sem relação.

## Passo 3: gere variantes de composição

Antes de animar, faça o scouting do melhor ângulo. Gere um grid 3×3 de opções de enquadramento e escolha o still mais forte considerando duas coisas: **legibilidade do produto** e **espaço negativo pro texto**.

Isso importa porque o Kling 3.0 é fraco em renderizar rótulo/label — se a leitura do produto depende do texto da embalagem, resolva no still e entre por image-to-video.

## Passo 4: monte o beat map (2-6 cenas)

Para uma narrativa "Escape Reality" estilo Netflix:

1. Setup no mundo real (candid, crível)
2. Momento de gatilho (produto ativa / portal abre)
3. Mundo de alto conceito (a zona de força do Kling 3.0)
4. Retorno + brand lockup (end frame limpo)

Rotule o job de cada cena: **Hook / Build / Turn / Payoff / CTA**.

## Passo 5: itere ritmo antes de qualidade de frame

Assista o primeiro pass **sem som** — a história se lê?
Depois **com som** — o ritmo bate?

Só então regenere a cena que está falhando — não a sequência inteira.

> Julgue a cena mais fraca, não o vídeo inteiro. Regenerar uma cena em vez do vídeo completo economiza tempo e custo de geração de forma significativa.

## Sequência do zero ao output usável

1. **Decida o tipo de saída.** Beat sequence de anúncio, hook de TikTok ou vinheta cinematográfica — cada um tem contagem de cena e estrutura de beat diferente.
2. **Escreva um beat map (2-6 cenas).** Rotule o job de cada cena.
3. **Rascunhe os prompts por cena.** Ângulo de câmera + ação + ambiente primeiro, em cada uma.
4. **Se clareza composicional importa, gere variantes antes.** Escolha o still mais forte antes de animar.
5. **Gere a sequência.** Assista uma vez sem som, uma vez com som.
6. **Regenere só a cena mais fraca.** Não reinicie a sequência inteira, a menos que a âncora de estilo esteja fundamentalmente errada.
7. **Exporte.** Adicione overlays de texto, brand lockup e trims de aspect ratio.

## Fit por caso de uso

| Caso de uso | Fit | Por quê |
|---|---|---|
| Criador de anúncio de performance | Forte | Estrutura beat-mapped + iteração rápida |
| Criador de conteúdo TikTok | Forte | Hooks multi-shot, áudio nativo pro ritmo |
| Filmmaker de conceito / storyboard | Forte | Ritmo e exploração de câmera baratos |
| Workflow de produção UGC | Bom | Multi-shot com personagem consistente |
| Close de beleza / luxo | Parcial | Menos confiável em detalhe de pele ultra-fechado |
| Clipe único estático→movimento | Alternativas existem | Ferramentas mais simples podem ser mais rápidas |

## Onde o Kling 3.0 se posiciona (fev/2026)

|  | Kling 3.0 | Sora 2 | Runway Gen-4.5 | LTX-2 |
|---|---|---|---|---|
| Estrutura multi-cena | 2-6 cenas nativas | Prompt único | Requer concatenação | Prompt único |
| Duração máx. | ~90s (6 × 15s) | ~20s | ~10s | ~5s |
| Áudio nativo | Gerado com o movimento | Silencioso | Silencioso | Silencioso |
| Consistência de sujeito | Boa entre estilos | Forte (estilo único) | Forte (estilo único) | Moderada |
| Melhor pra | Sequências de anúncio estruturadas, multi-shot TikTok | Planos-sequência cinematográficos | Cenas fotorrealistas | Iteração rápida de conceito |

Leitura honesta: Sora 2 ainda produz o plano-sequência mais cinematográfico; Runway Gen-4.5 é o mais forte em close fotorrealista; LTX-2 é o jeito mais rápido de testar um conceito antes de comprometer.

A vantagem estrutural do Kling 3.0 — sequenciamento multi-shot nativo com áudio — é única no grupo. Se o workflow exige contar uma história **através de cenas** em vez de torcer pra um clipe conter uma edição, o Kling 3.0 é hoje a única ferramenta em que isso é operação de primeira classe.
