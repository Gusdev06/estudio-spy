# Lauren Walker 2091863388082075 — var1: homem e cenário novos · 2026-09-25

**Original:** `~/Downloads/Lauren Walker_2091863388082075_2026-09-25.mp4` (md5 `3dfa6b3a…`), 720×1280, 30 fps, 601 frames, 20,03 s → `REFERENCIA-original.mp4`.
**Peça:** `pecas/variacao.mp4`: 720×1280, 30 fps, 601 frames, h264, áudio AAC copiado (md5 do stream `19450316…` = original).
**Avatar/cenário:** homem branco de ~45 anos, barba curta grisalha, camiseta cinza. Nos blocos A/B ele está numa sala de estar com estante e abajur; no C, numa varanda ensolarada. O original era um homem latino numa sala borrada e depois dentro de um carro.

## Molde medido (n = número do frame; rosto YuNet por score em `molde/rostos-original.json`)
| n | o que é | como ficou na peça |
|---|---|---|
| 0–98 | homem em tela cheia + coração quicando (y 170–550) + caixa "Discover Infidelity IN Minutes." (y 555–725), sem cobrir o rosto | clipe c1 em tela cheia; coração e caixa do original por máscara de cor, frame a frame |
| 99–447 | gravações de celular em tela cheia com o homem **recortado POR CIMA** (B1 99–343 no canto inferior esquerdo, B2 344–447 no inferior direito). Berinjela e flor passam por trás dele | recorte da avatar nova (MediaPipe selfie_multiclass) por cima. Onde a silhueta antiga (dilatada 12 px) passa da nova, o celular é reconstruído por inpainting usando só o entorno, sem pixel do homem antigo |
| 448–524 | close no carro + seta vermelha com contorno branco quicando | clipe c2 em tela cheia + seta **redesenhada** (sprite sintético, posição tirada da seta do original em cada frame) |
| 525–600 | CTA "ACCESS NOW" sobre celular borrado, sem o homem (inclui os frames pretos 564/595) | original intocado |

## Pipeline (desta pasta)
1. Bases: `base/A.req.json` (gpt-image-2/edit sobre o n 50) veio centralizada, com o rosto grande demais. Então `base/A2` recebeu A padded no enquadramento do original e fez outpaint, e `base/C` gerou o close com a identidade da A2 e o enquadramento do n 470.
2. `SEED=7 bash gerar-clipes.sh c1 c2`: c1 usa o áudio de 0 a 14,933 s (n 0–447) e c2 o de 14,933 a 17,5 s (n 448–524). Prompt só em positivo. Os dois decodificaram inteiros.
3. `python3 checar.py c1 c2`: nenhum dos dois teve moldura, gente entrando, 2º rosto ou rosto sumindo.
4. `<venv mediapipe>/bin/python montar.py pecas/variacao.mp4` (o venv usa `seg.py`; o modelo `selfie_multiclass_256x256.tflite` fica no scratchpad da sessão). As emendas são por número de frame e o clipe é lido em t = (n−n0)/30 + 1/24.
5. `varredura.py` confere frame a frame (n 0–524).

## Varredura final
- Os 525 frames em que o homem aparece no original têm 1 rosto na peça, e esse rosto é o novo.
- A máscara do homem antigo tem de 150 mil a 450 mil px por frame. Desses, só 3 a 11 mil px (média) ficam iguais ao original. `conferencia/varredura-px-iguais-exemplos.jpg` mostra que são coincidência de cor: camiseta cinza sobre camiseta cinza, pele sobre pele. O pico de 20 mil px no n 405 é o polegar e a borda do celular de quem segura o aparelho, que não fazem parte do homem.
- `conferencia/original-x-peca-10-instantes.jpg`, `conferencia/emendas.jpg` (98/99, 343/344, 447/448, 524/525) e `conferencia/zoom-coracao-caixa-seta.jpg` foram conferidas a olho: não sobra rosto, cabelo nem ombro do homem original.

## Concessões
- No B, o homem novo tem ombros naturais. No original, o recorte cortava o ombro numa vertical. Por isso o novo cobre um pouco mais do celular, por exemplo o teclado no n 99–199.
- O halo onde a silhueta antiga passava da nova (4,8 mil px em média, 12 mil no máximo) é celular reconstruído por inpainting, e fica levemente borrado junto ao contorno.
- Os risquinhos brancos de "brilho" em volta da seta (n 448–470) não foram redesenhados. A seta vermelha com contorno branco ficou.
- A mão do homem original que entra no quadro no n 450–453 não existe na peça.
- 1ª tentativa de halo: preenchi com o clipe novo desfocado e virou um brilho marrom, e a máscara antiga pegava a mão do celular. Corrigi com um envelope da cabeça, pele só no pescoço e inpainting.

## Custo real: US$ 0,66 (teto 0,90)
3 imagens gpt-image-2/edit, US$ 0,211 (0,0665 + 0,0665 + 0,0779), e 2 clipes Pruna, US$ 0,450 (15 s = 0,375 e 3 s = 0,075). Os ids estão em `ids.txt` e a conferência em `custo-billings.json`.
