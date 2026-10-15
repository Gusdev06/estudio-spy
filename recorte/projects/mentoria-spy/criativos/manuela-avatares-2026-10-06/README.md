# Manuela Freitas 1575322357678875: 5 variações trocando SÓ a avatar (06/10/2026)

**Original:** `~/Downloads/AdLibNote_Manuela Freitas_1575322357678875_adstart-2026-10-02_creative-01_video.mp4` (md5 `c4f88c36…`), 720×1280, 24 fps, 846 frames (35,37 s), EN, voz feminina. Copiado em `REFERENCIA-original.mp4`.
**Pedido do Gusta:** "5 variação desse mudando apenas avatar". O roteiro, o áudio, o b-roll, a menina chorando do split, o explicativo e o CTA ficam iguais. Só a mulher que fala muda; o quarto (cortina bege, arcos) também fica igual.

## Peças (`pecas/`)
| Peça | Avatar |
|---|---|
| `manuela-a1.mp4` | Latina, ~24 anos, cabelo escuro ondulado longo, blusa preta |
| `manuela-a2.mp4` | Negra, ~25 anos, cacheado natural na altura do ombro, camiseta branca |
| `manuela-a3.mp4` | Loira, olho azul claro, cabelo liso, suéter azul claro |
| `manuela-a4.mp4` | Leste-asiática, cabelo preto liso com franja cortina, suéter aveia |
| `manuela-a5.mp4` | Ruiva com sardas, olho verde, cardigã verde-oliva |

Todas têm 720×1280, 24 fps e 846 frames. O áudio é copiado do original (md5 do stream AAC idêntico nas 5: `f1a47203…`). O casting está em `conferencia/casting.jpg`.

## Molde medido (frames)
| frames | o que é | na peça |
|---|---|---|
| 0–101 | avatar em tela cheia, legenda de abertura (Poppins Black com degradê, entrada com blur, sublinhado vermelho com glow) | clipe s1; legenda **redesenhada** (`legenda1.py`) |
| 102–107 | flash (light leak); 104–106 quase brancos | 104–106 são do original; 102, 103 e 107 aplicam a transmissão do flash ao frame novo |
| 108–145 | avatar em tela cheia, legenda branca com sombra | s1; glifo copiado do original, sombra sintética |
| 146–238 | b-roll do casal | original |
| 239–447 | split: menina chorando em cima, avatar embaixo a partir de y≈525 (borda suave 520–536) | parte de baixo do clipe s2, com rampa de 16 px; parte de cima original |
| 448–792 | explicativo animado | original |
| 793–845 | avatar com o CTA (botão rosa "Learn More" → verde "redirecting" + cursor de mão) | s3; botão e cursor copiados pixel a pixel do original |

## Pipeline (pasta autocontida, rodar daqui)
1. `gerar-bases.py a1..a5`: gpt-image-2/edit (medium, 1k) sobre o frame limpo n60. Troca só a pessoa e mantém quarto, enquadramento e tamanho de cabeça.
2. `gerar-clipes.sh a1..a5`: Pruna p-video/avatar (720p, seed 7, prompt só em positivo, braços fora de quadro). Usa o áudio ORIGINAL de 3 trechos: s1 0–6,25 s, s2 9,9167–18,75 s e s3 32,8333–35,37 s.
3. `checar.py`: triagem YuNet. 15/15 passaram. A2-s1 acusou "borda" em 4,5 s, mas eram as mãos dela gesticulando na base; conferi a folha.
4. `rostos.py`: trilha de rosto do original e dos clipes.
5. `montar.py aN`: tudo por número de frame. O enquadramento é GLOBAL: segue o zoom e a posição da câmera original em relação ao n60, sem prender o rosto novo quadro a quadro, que deixava o rosto grande e girado.

## O que aprendi aqui
- **Flash de light leak:** misturar por "brancura" cola branco na pele clara. O que funcionou: transmissão `T=(255-orig)/(255-vizinho sem flash)`, borrada com σ 14 para não carregar traço da pessoa original, e `novo = 255-(255-novo)*T`. Nos frames de flash, a legenda vem do frame vizinho e passa pelo mesmo flash.
- **Legenda com degradê, blur de entrada e sublinhado com glow:** a cópia de glifo corta a parte cinza das letras e puxa pele da mão pro sublinhado. Redesenhar sai melhor (Poppins Black, tracking negativo, degradê nos 38% de baixo).

## Custo real: US$ 2,7075 (estimativa US$ 2,50)
- 5 imagens gpt-image-2/edit: US$ 0,3325 (0,0665 cada).
- 15 clipes Pruna: US$ 2,375 (por avatar 0,175 + 0,225 + 0,075). A Pruna cobra em degraus: 6,25 s saiu por 0,175 e 8,83 s por 0,225.
- Nada foi regerado. Os IDs estão em `molde/prediction-ids.txt`, cruzados com `wavespeed billings` (key:macbook).
- As 5 chamadas Pruna de US$ 0,775 às 01:14 UTC no billing NÃO são deste lote.

## Concessões
- A original gesticula com as mãos no quadro o tempo todo. As novas ficam com os braços quase sempre fora (trava contra mão na lente); a a2 gesticula um pouco por volta de 4,5 s.
- 1 frame (796): o botão aparece já com o texto "Learn More" (no original, o texto entra 1 frame depois).
- A abertura tem espaço entre palavras um pouco mais largo que o original.
