# Prompts de foto realista pra Bia (pesquisa de 14/10/2026)

## Por que a 1ª rodada (perfil/A–D) saiu com cara de IA
- As 4 tinham o mesmo rosto de frente, olhando pra lente, com o mesmo sorrisinho e centralizado: parece documento, não foto de amiga.
- As referências (fundo cinza, pose frontal) puxam essa pose. A referência serve pra identidade, não pra pose.
- Luz limpa e uniforme demais, pele "bonita" demais, nada cortado pela borda do quadro.

## Estrutura que os prompts que funcionam usam (EvoLinkAI case 84; YouMind café iPhone; Hedra)
Prompt em campos, a cena primeiro e o rosto por último:
```
Asset type: candid lifestyle photo for an Instagram post
Primary request: photorealistic phone photo of the woman in the reference images, 100% faithful to her face, beauty mark and hair. Use the references ONLY for identity, never for pose or background.
Scene/backdrop: <lugar real com detalhe de vida: objetos, bagunça leve, outras pessoas desfocadas>
Subject: <roupa com marca de uso, cabelo com fios soltos, AÇÃO acontecendo (mexendo no celular, rindo de lado, olhando a vitrine)>
Style/medium: shot on an iPhone, true-to-life phone processing, subtle grain, slight HDR from the phone
Composition/framing: <quem tirou: amiga do outro lado da mesa / selfie de braço esticado / espelho>; subject off-center, slightly tilted, parts of objects cut by the frame edge; not looking at the lens (or a quick glance)
Lighting/mood: <fonte nomeada: janela à esquerda, sol baixo, flash do celular, luz de geladeira>
Textures: natural pores, uneven skin tone, flyaway hairs, fabric creases, fingerprints on glass
Constraints: no text, no logo, no watermark
Avoid: beauty filter, plastic or waxy skin, symmetrical centered headshot, studio lighting, cinematic grading, perfect makeup, influencer pose
```
- Nunca usar: beautiful, stunning, 8K, masterpiece, cinematic, ultra realistic (Hedra: puxam o look de IA).
- Quanto mais "foto ruim" (flash duro, foco perdido, borda cortada), mais real fica (EvoLinkAI: toy camera; YouMind: Nokia).
- Ancorar a identidade com uma frase só ("100% faithful to the reference") e descrever o resto da cena com muito detalhe (YouMind café).
- Expressão intermediária, não sorriso de foto.

## Fontes
- https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts (cases 84, Curtain Bang, toy camera)
- https://github.com/YouMind-OpenLab/awesome-gpt-image-2 (café iPhone, Nokia selfie)
- https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts (CCD flash candid, RAW iPhone)
- https://mkt.hedra.com/blog/make-ai-images-look-like-real-photos-prompting

## Cor (14/10, depois do "as cores ainda parecem artificiais")
- O que resolveu: mandar uma foto real como 3ª imagem **só de referência de cor e luz** (`ref-estilo/pinterest-golden-hour-carro.jpg`): âmbar quente, contraste baixo, sombras levantadas, leve névoa. Dizer no prompt pra não copiar o rosto, o cabelo, a pose, a roupa e as joias.
- Vazamento: no gpt-image-2.5 a Bia pegou o pingente retangular da referência. Não pedir colar parecido com o da referência.
- gpt-image-2.5-sunburst/edit (~US$0,22): segue melhor a cor da referência (mais dourado). Nano Banana 2.1 edit 2k (~US$0,04–0,08): composição boa, mas cor mais fria e neutra, puxa menos a referência. Pastas `perfil/v3/` × `perfil/v3-nb21/`.
- **14/10 (Gusta): "NANO BANANA 2.1 BEMM MELHOR".** Modelo padrão das fotos da Bia = `google/nano-banana-2.1/edit` 2k, refs [01-frente, 05-close, ref de cor]. 6 selfies no carro em `perfil/carro-nb21/` (~US$0,40).
- Vazamento da referência de cor: na `6-regata-preta-colar` apareceu uma 2ª pessoa no banco de trás (a ref tem outra mulher atrás). Acrescentar "she is alone in the car" ao prompt.
