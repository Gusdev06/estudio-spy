---
tipo: tecnica
criado: 2026-09-21
fontes: [raw/2026-09-20-variacoes-30-avatar.md]
tags: [pruna, lipsync, identidade, defeito, conferencia]
---

# Pruna troca de pessoa no meio do clipe (frame 0 engana)

No lote de 30 variações (21/09), em ~9 de 60 clipes do podcast o `pruna-ai/p-video/avatar` começou com a imagem-base e, **do frame 1 em diante, gerou outra mulher** — mais perto da câmera, outro cabelo, sem o hijab. O frame 0 é sempre a imagem, então a folha de 1 frame não pega; o Gusta viu como "piscava imagens dos avatares anteriores".

**Quando acontece:** pedido de pose diferente da imagem ("talks straight toward the camera" com imagem em 3/4) e closes com muito ar em cima; parece aleatório entre seeds.

**O que resolveu (de primeira, 7/7):** prompt travando a identidade **em positivo** — "The woman in the image — {descrição}, wearing {roupa} — stays EXACTLY the same person from the first frame to the last: same face, same hairstyle and head covering, same clothes, same framing and distance from the camera" — e não pedir mudança de pose. Pular o frame 0 na montagem (é a imagem parada, enquadramento diferente).

**Como conferir:** `checar-identidade.py` (tamanho/cor do rosto no frame 0 × mediana do resto, YuNet) pega o drift de enquadramento; o de identidade com mesmo tamanho ainda pede folha de rosto por bloco. Recorte da janela sempre **centrado no rosto detectado**, nunca fixo ([[reconstruir-camadas-do-criativo]]).

Conecta com [[pruna-inventa-entrevistador-na-borda]] (mesma família: o modelo reimagina a cena) e [[lote-variacoes-30-2026-09-20]].
