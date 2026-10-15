# As 6 regras de prompting do Kling 3.0

Cada regra vem com o porquê. Entender o mecanismo é o que permite adaptar quando o caso não encaixa no molde.

## 1. Lidere com ângulo de câmera, depois sujeito, depois ação

Enquadramento de cinematógrafo primeiro dá ao modelo um quadro de referência antes de ele preencher os detalhes. É como um diretor fala com o DP: *"Medium shot, our character, she reaches for the door."* A âncora espacial vem primeiro.

Invertendo a ordem ("ela alcança a porta, em plano médio"), o modelo já comprometeu composição antes de saber o enquadramento — e o resultado costuma ser um plano genérico.

## 2. Trave o personagem nos shots de abertura

Estabeleça claramente nos Shots 1-2. Não introduza no meio da sequência esperando consistência.

O Kling 3.0 constrói um modelo do personagem a partir dos primeiros shots que processa. Interromper isso com uma descrição nova no meio é pedir pra ele reconciliar contradições — e o resultado é drift de rosto/figurino.

Prático: escreva a descrição completa uma vez (rosto, figurino, linha emocional) na Cena 1, e nas cenas seguintes **referencie sem redescrever** ("the same woman", "he").

## 3. Movimento vence estilização

Descrever movimento, timing e progressão rende mais que listas longas de adjetivos estéticos.

`"She spins toward camera"` é mais confiável que `"cinematic, dramatic, emotional, high-production-value"`.

O modelo executa física melhor do que interpreta vibe. Adjetivos de qualidade ("cinematic", "8k", "masterpiece") são quase ruído — o orçamento de tokens do prompt rende muito mais em verbos.

## 4. Use POV para transições de estilo

Atravessar mudanças agressivas de estilo em primeira pessoa reduz muito o drift de consistência. O modelo para de ter que renderizar um rosto e um corpo específicos através de uma estética estrangeira — ele só precisa mover a câmera por um mundo novo.

Isso vale além de style transfer: sempre que a cena exige uma troca visual violenta (mundo real → mundo conceitual, produto → interior do produto), POV é o caminho mais estável.

## 5. Mereça a duração

Se você está usando o tier de 10-15s, escreva um arco: **iniciação → escalada → resolução**.

Uma descrição estática de 15 segundos desperdiça o orçamento de geração. Se o seu prompt não tem começo, meio e fim, seu clipe também não terá.

Formulação útil: "starts… escalates… lands." Clipes longos permanecem coerentes quando você descreve **progressão ao longo do tempo**, não um momento estendido.

## 6. Image-to-video: trave primeiro, depois mova

Trate a imagem de referência como um frame congelado, e então descreva a reação da câmera e o movimento **em volta dela** — não a descrição do sujeito. O sujeito já está definido pela imagem; seu trabalho é dizer à câmera como reagir.

O modelo preserva bem identidade, layout e detalhes de texto da imagem de origem. Redescrever o sujeito compete com esse ancoramento e introduz drift.

---

## Quando as regras quebram

Essas regras valem pra maioria dos tipos de prompt, mas o Kling 3.0 surpreende. Quando uma geração produz algo inesperado e **melhor** do que o planejado, estude o que desviou — esse desvio costuma virar técnica nova.

O modelo tem tendências estéticas que não estão totalmente documentadas. Teste de campo continua sendo o método de pesquisa mais confiável. Registre o que funcionou.

## Terminologia de câmera que o modelo entende bem

O Kling 3.0 entende vocabulário de cinema de verdade. Use os termos reais em vez de descrever o efeito:

- **Enquadramento:** extreme close-up, close-up, medium close-up, medium shot, wide shot, extreme wide, over-the-shoulder, profile shot, macro close-up
- **Movimento:** dolly push-in, dolly out, tracking shot, slow tracking shot from behind, pan left/right, tilt up/down, crane up, handheld, locked-off / static, orbit, whip pan
- **Ótica/profundidade:** shallow depth of field, deep focus, rack focus, anamorphic, wide lens distortion
- **Ponto de vista:** first-person POV, shot-reverse-shot, low angle, high angle, bird's eye, Dutch angle
- **Luz:** golden hour, neon night, hard key light, soft window light, backlit, rim light, practical lights in frame

Descreva também **como a câmera se comporta ao longo do tempo**: seguindo, congelando, panorâmica, movendo em sincronia com o sujeito, retomando o movimento suavemente. A relação câmera-sujeito ao longo do plano é o que dá long takes coerentes.
