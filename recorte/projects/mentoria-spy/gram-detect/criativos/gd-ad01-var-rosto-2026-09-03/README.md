# GD-AD01 — variação C: rosto/cenário (PERSONAGEM 3, cozinha) + correções por edição (2026-09-03)

**Não é uma alavanca só.** O arquivo-base foi regravado: voz nova e legenda em outro estilo estão queimadas no vídeo e não têm conserto por edição. A tabela "O que difere do campeão" abaixo é o que contamina o teste. O Gusta precisa ler isso antes de decidir subir.

| | Arquivo | Custo |
|---|---|---|
| **Ad A** (controle) | `criativos-crus/spy-gram/ads-en/GD-AD01.mp4` (md5 `4a6906ae…`), intocado | zero |
| Base da C | `criativos-personagens/AD01 - PERSONAGEM 3.mp4` (md5 `cf4d71f70c2b892456851e649f6bd8f7`), 1080×1920, 60 fps, 29,55 s | já existia |
| **Ad C** | `GD-AD01-C-rosto-p3.mp4` (nesta pasta) | **zero** (só ffmpeg) |

- Escolha e spec (Peneira): `gram-detect/referencias/proprios-2026-09-03/01-gd-ad01.md`, seções 14 (caixa) e 14b (P3 e correções).
- Montagem: `montar.sh`. Conferência: `conferir.py`. Frames em `conferencia/`.

## Correções aplicadas (só as listadas, nada regravado, nada pago)

| # | Correção | Como ficou | Medido |
|---|---|---|---|
| 1 | Caixa do campeão com o texto original | Caixa #FE0553 em **x 40–1039, y 862–1326 (1000×465)**, Poppins Bold 60 px, #EEFC00, contorno 2 px + sombra 5 px #2C040A, passo 75 px, centro x 540, **par de linhas centrado verticalmente na caixa** (topos em y 1025 e 1100; bloco y 1026–1162, centro 1094 = centro da caixa). No campeão as linhas ficam em y 899/974 dentro de uma caixa de 197 px; aqui, com a caixa de 465 px, o texto colado no topo deixava um bloco rosa vazio embaixo (ajuste do Maestro). Mesma receita da variação B (camada RGB → bt709 → overlay) | Na C: caixa x 40–1039 · y 862–1326 · #FC0351 · linha 1 x 134–947, y 1026–1088 (centro x 540,5) · linha 2 x 268–810, y 1100–1162 (centro x 539). Campeão: x 136–946 / 266–813, y 900–956 / 974–1030 |
| 1b | Caixa **maior que a do campeão** (868×197 → 1000×465), texto centrado nela | Correção do Maestro (03/09): a legenda cursiva do P3 ("THERE'S A detail on… always GIVES away people") desce até **y 1317** (frame 208, 3,47 s) e o logo do Instagram vaza pra esquerda até **x 47** (y 1246–1320, 0,6–3,85 s). Uma versão anterior com a caixa até y 1091 deixava o "always" cortado pela borda, que parece defeito. Fechei 10 px abaixo do branco e 7 px além do logo, simétrico em torno de x 540; o painel do app começa em ~1330 e fica intacto. Um segundo retângulo só de 0 a 3,8 s daria salto visível, então é caixa única de 0 a 6,65 s | Varredura dos 399 frames da C: 0 linhas de branco em y 1327–1400 dentro da largura; 0 px de logo fora da caixa |
| 2 | Caixa some junto com a transição do P3 | Frames 0–398; some no **frame 399 = 6,650 s**, início do flash amarelo→branco que traz o card Gram Detect (no campeão é 7,800 s) | rosa na região: 146.201 px no frame 398, 0 no 399 |
| 3 | Voz −9 dB | `volume=-9dB`, AAC 192 kbps | P3 cru −16,5 dB / −13,5 LUFS → C **−25,5 dB / −22,5 LUFS**; campeão −25,6 dB / −22,7 LUFS |
| 4 | Fade escuro final cortado | `-t 29.2`: o fade começa no frame de 29,200 s (luma 85,7 → 81,8 → … → 2,3). C fecha em corte seco no frame 1751 (29,183 s), sobre as setas | último frame da C luma 85,7 = frame limpo do P3 |
| 5 | Frame 0 de olhos abertos | Conferido no frame 0 do P3, in point mantido | `conferencia/f000-varC.png` |

Saída: 1080×1920, **60 fps** (mantido do P3), 1752 frames, 29,200 s, H.264 crf 16 bt709.

## O que difere do campeão (contaminação do teste)

| Dimensão | Campeão GD-AD01 (A) | Variação C | Corrigível por edição? |
|---|---|---|---|
| Rosto | mulher ~28, cabelo solto | **mesma mulher** (hipótese Peneira: gerada por IA a partir dela), coque | não é a alavanca "outra pessoa"; é "mesma cara, outro visual" |
| Cenário | quarto bagunçado, closet aberto | **cozinha** com pia e geladeira | não |
| Roupa | moletom cinza | camiseta bege | não |
| Voz | original, F0 281 Hz | **regravada**, F0 200 Hz, correlação de envelope 0,11 com a original | não; só o volume foi igualado |
| Legenda | branca, caixa mista, 2–3 palavras, contorno preto | **amarela itálica, CAIXA ALTA, 1 palavra**. A abertura em cursiva branca com logo do Instagram (0–3,85 s) fica **inteiramente coberta** pela caixa; da transição em diante a legenda amarela do P3 aparece normalmente | parcial: a abertura está coberta; o resto exigiria inpainting |
| Caixa do gancho | 0–7,8 s, 868×197 px (80% da largura, 10% da altura) | 0–6,65 s, **1000×465 px** (93% da largura, 24% da altura); texto centrado verticalmente (linhas em y 1025/1100, no campeão 899/974) | corrigido, com as duas diferenças declaradas |
| Roteiro falado | roteiro mestre, 95 palavras | idêntico palavra por palavra (cai o "it" de "without realizing it") | igual |
| Painéis do app | card Connecting → Gram Detect → story → interceptação → setas | mesmo kit, **retemporizado**; transição em flash amarelo/branco em 6,55–6,75 s que o campeão não tem | não |
| Cortes | 8 | ~11 | não |
| Duração / fps | 32,6 s · 30 fps | **29,2 s · 60 fps** | não (só o fade foi cortado) |
| Volume da voz | −25,6 dB | −25,5 dB | corrigido |
| Fade final | não tem | tinha, cortado | corrigido |

Leitura honesta do teste: **C × A mede "mesmo roteiro, mesmo kit, mesma caixa de gancho; muda cenário (cozinha), visual do cabelo/roupa, voz e estilo da legenda"**. Se C ganhar de A, não dá pra dizer qual dessas quatro coisas ganhou. Se perder, idem.

## Custo

**US$ 0,00.**
