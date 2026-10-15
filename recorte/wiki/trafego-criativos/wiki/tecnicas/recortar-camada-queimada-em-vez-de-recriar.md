---
tipo: tecnica
tags: [clone, troca-de-avatar, karaoke, camadas, reprovado]
fontes: [[fonte-ad02-h2-var-avatar-2026-09-14]]
---

# ⛔ Recortar camada queimada — REPROVADO (16/09/2026)

**Esta técnica foi testada e reprovada pelo Gusta.** Fica registrada como o que NÃO fazer.

A ideia era: em criativo de rosto em tela cheia, compor o avatar novo por baixo e devolver karaokê, painéis e CTA por **recorte retangular do original**, porque voltariam pixel a pixel e porque recriar um karaokê palavra-a-palavra (~120 estados em duas alturas) daria aproximação.

Na prática, o veredito sobre as peças 50-52 foi *"ficou horrível… gambiarra… ficou tudo errado a edição"*. Os três motivos:
1. **O recorte arrasta o fundo do original junto.** Cada retângulo traz uma moldura da cena antiga, e a emenda aparece.
2. **Camada semitransparente não sai de jeito nenhum.** As setas do AD02-H2 tinham luminância máxima 204; o retângulo colou o rosto do ator antigo por cima do avatar novo.
3. **O enquadramento não casa.** Quando o editor aplica zoom progressivo, cada bloco precisaria de crop e offset próprios, e o casamento por tentativa nunca fecha.

## O que fazer no lugar
[[reconstruir-camadas-do-criativo]] — medir e redesenhar cada camada de verdade.

## Conecta com
- [[lote-ad02-h2-var-avatar]] — o lote reprovado
- [[criativo-como-layout-de-post]] — o caso em que o problema não existe, porque as camadas já vivem fora da janela do rosto
