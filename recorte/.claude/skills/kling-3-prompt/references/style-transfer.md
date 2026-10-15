# Style transfer e consistência de personagem

O problema que isso resolve: manter **um personagem identificável** enquanto pula entre estéticas visuais radicalmente diferentes.

## Arquitetura de 4 camadas

1. **Establish** (Shots 1-2, terceira pessoa) — trava rosto, figurino e linha de base emocional do personagem em dois planos claros.
2. **Enter POV** (Shot 3) — troca pra primeira pessoa. O espectador vira o personagem.
3. **World-hop em POV** (Shots 4-6) — três trocas de estilo consecutivas. Porque você está em POV, o modelo não precisa renderizar o protagonista — só o mundo.
4. **Final break** (Shot 7) — troca de mídia inteira (ilustração anime, pintura a óleo, etc).

A transição pra POV é o mecanismo-chave. Sem ela, manter consistência de personagem nos Shots 4-6 não é confiável. Com ela, dá pra atravessar quase qualquer mudança de estilo.

## Template de 7 shots — versão validada (montanha-russa)

Este é o template confirmado, testado e validado no guia original. Serve como calibração de nível de detalhe.

**Shot 1:** A medium shot from behind the head of a blonde woman as she sits in a rollercoaster car. The sky is a vibrant, deep pink and orange sunset. She suddenly turns her head to the side with an expression of intense shock and terror.

**Shot 2:** A close-up, front-facing shot of the woman in the rollercoaster car. Her hair is blowing wildly in the wind, and her eyes are wide with fear as she screams. The background shows the high-speed motion of the ride against the sunset sky.

**Shot 3:** A first-person perspective (POV) shot from the front of the rollercoaster as it rapidly ascends a steep, metal track. Below, an amusement park is visible under the glowing evening sky.

**Shot 4:** A POV shot as the rollercoaster track transforms into a soft, pink fuzzy material. The coaster climbs a bright green, rounded hill populated by a flock of white, fluffy sheep. The sky is bright blue with stylized pink clouds.

**Shot 5:** A POV shot of the rollercoaster speeding through a futuristic, dark tunnel illuminated by concentric rings of glowing white and pink neon lights. The motion is extremely fast and dizzying.

**Shot 6:** A POV shot as the rollercoaster emerges into a hyper-realistic New York City street during golden hour. The track runs perfectly straight down the center of the avenue, flanked by towering skyscrapers, with the sun setting directly at the end of the street.

**Shot 7:** A transition into an anime-style illustration. The woman, drawn in a classic 90s anime aesthetic, is standing up in the moving coaster car with her arms raised in the air. She is screaming in excitement/terror as the sun rays burst behind her and the city skyline.

## Template em branco

Substitua os colchetes pelo seu personagem e seus mundos.

```
Shot 1: A [medium/wide] shot of [character] in [scene]. [Color palette]. [Emotional action].
Shot 2: A [close-up] shot of [character]. [Emotion detail]. Background shows [speed/motion].
Shot 3: A first-person POV shot from [position]. [Main visual]. [Environment] visible [relation].
Shot 4: A POV shot as [element] transforms into [World A - style + materials + atmosphere].
Shot 5: A POV shot through [World B - signature visuals]. Motion is [tempo].
Shot 6: A POV shot as [movement] emerges into [World C - hyper-real place, lighting, detail].
Shot 7: A transition into [medium/style]. [Character in new style]. [Peak emotion + background]
```

## Como escolher os três mundos

Os shots 4-6 rendem mais quando os mundos **contrastam entre si em material e tempo**, não só em tema:

- Mundo A: material macio, tempo lento, paleta saturada
- Mundo B: geometria dura, tempo rápido, alto contraste
- Mundo C: hiper-realista, tempo médio, luz natural (funciona como "aterrissagem" antes do break de mídia)

O padrão de transição que segura melhor é sempre o mesmo elemento se transformando — o trilho, a estrada, o corredor. Amarrar a troca de mundo a um **objeto contínuo** dá ao modelo um eixo pra manter enquanto tudo mais muda.

## Adaptação pra tráfego pago

O mesmo esqueleto funciona pra criativo de "escape reality" / transformação:

1-2: realidade do lead (terceira pessoa, cru, crível)
3: POV — o espectador entra no lugar dele
4-6: os mundos que o produto abre
7: break de estilo + brand lockup / end frame limpo

Quando o objetivo é performance, o Shot 7 vira o end frame com espaço negativo pro CTA — não um clímax visual.
