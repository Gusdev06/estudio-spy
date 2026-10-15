# Insight solto — 2026-10-06 — troca de avatar com flash de light leak e legenda animada (Manuela Freitas)

- Referência: Manuela Freitas, ad 1575322357678875 (adstart 02/10/2026), Spy Zap EN, 720x1280, 35,4 s. A estrutura: talking head → b-roll do casal → split com a menina chorando em cima e a avatar embaixo → explicativo animado → avatar com o CTA "Learn More/redirecting" e o cursor. As transições são flashes de light leak de ~6 frames.
- Lote: `projects/mentoria-spy/criativos/manuela-avatares-2026-10-06/`. São 5 avatares e uma alavanca só; o áudio é bit-idêntico. Custo US$ 0,54 por peça (imagem edit no frame limpo + Pruna só nos ~17 s em que a avatar aparece).
- Técnica do flash: para reproduzir o light leak sobre o frame novo, use a transmissão `T=(255-orig)/(255-vizinho sem flash)` borrada com σ 14 e aplique `255-(255-novo)*T`. Misturar por brancura falha em pele clara, e T sem borrar carrega o fantasma da pessoa original.
- Técnica da legenda: legenda com degradê, blur de entrada e sublinhado com glow não se copia bem do original (perde a parte cinza da letra e puxa pele). Redesenhe com a fonte (aqui Poppins Black) nos tempos medidos.
- Enquadramento: transformação global que segue o zoom da câmera original relativo ao frame da base. Prender o rosto quadro a quadro amplia e gira demais.
- Pendente: performance das 5 vs o original. Não há número ainda; puxar da UTMify depois de rodar.
