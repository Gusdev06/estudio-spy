# V3 — "quem é a garota que ele curte"

Peça: `pecas/v3-quem-ele-curte.mp4`. H.264 yuv420p bt709, 720×1280, 30 fps, 1095 frames (36,5 s). O áudio é copiado do original com `-c:a copy` (MD5 do stream igual: c9dd1a85…). Custo de geração: zero (só ffmpeg, PIL, numpy e OpenCV).

## O que mudou
1. **Legenda do gancho (f0–149)**: troquei “Girl, how do I get into my boyfriend’s Insta without him knowing?” por **“Girl, who’s the girl / he keeps liking pics of? / 👀”**. O topo "pov: women talk about men" ficou igual.
2. **1ª legenda da demo (f144–378)**: troquei "Copy **his** @ and use" por "Copy **her** @ and use". A linha 2 ("it on Gram Detect.") ficou como está.
3. O resto ficou idêntico: reveal "her account", TRY IT FREE, CTA e áudio.

## Medidas (no frame, não no chute)
- **Caixa do gancho**: preto puro (0,0,0), uma caixa por linha unida numa silhueta só.
  - L1 x79–640, L2 x42–677, L3 x238–481, y948–1133.
  - Retângulo de 72 px por linha, passo de 56 px, raio de ~12 px, folga lateral de ~18 px.
  - A silhueta está salva em `scripts/sil_f0.npy`.
- **Fonte do gancho**: Open Sans, peso 750, 40 px, entrelinha de 56 px, centro em x=360, branca. Ajustei por diferença de pixel por linha. Aspas curvas. O 👀 é Apple Color Emoji.
- **Legenda da demo**: Montserrat, peso 800, 36,5 px, tracking −1,5 px e contorno preto de 3 px. A tinta da linha 1 ocupa y899–934. "his" ocupava x284–333; "her" tem 8 px a mais.
- **Chicote (f140–155)**: é uma transição em painéis. A camada de legenda do gancho anda rígida com dx = −12−48·(i−140), e aparece também a cópia em dx+720. Bate 100% nos frames 140–149 e some no f150. A legenda da demo entra com dx = 708−48·(i−140) até o f154, e fica parada do f155 ao f378.

## Como foi feito
- **Gancho**: a silhueta original foi mantida pixel a pixel. O interior (4 px para dentro da borda) virou preto, e o texto novo foi desenhado ali. No chicote, a caixa nova é aplicada em cada cópia deslocada, só nas colunas onde a camada original está visível (85% ou mais do interior batendo). Por isso o recorte de painel do original se repete igual.
- **Demo**: apaguei a linha 1 inteira com inpaint (Telea, r=6), mascarando também a linha 2 para não puxar o contorno preto dela. Depois redesenhei "Copy her @ and use" centrada. Nenhum pixel do "his" antigo ficou: olhei os frames 146–378 nas folhas.

## Conferência
- Folhas com original em cima e peça embaixo em `conferencia/`:
  - `folha-gancho-e-chicote.png`: f0, 70, 139, e 140 a 150.
  - `folha-legenda-demo.png`: f146–379.
  - Zooms do chicote e da legenda.
- Fora das áreas editadas, a diferença média por frame contra o original é de no máximo 1,24/255 (média de 0,68). É o nível de recompressão: crf 12 com conversão bt709 casada, e o round-trip sem edição dá 0,01.

## Concessões
- **Texto em 3 linhas dentro da silhueta antiga**: a copy nova é mais curta, e uma caixa justa ao texto não cobriria a caixa antiga (o fundo por baixo nunca aparece no vídeo). Por isso o texto ficou centrado dentro da mesma silhueta, com folga lateral maior (~70 px contra 18 px no original). Com isso, a L3 ficou só com "👀”".
- **"Copy" andou 2–5 px**: a linha 1 da demo foi recentrada, porque "her" é 8 px mais largo.

## Refazer
```
cd v3-quem-ele-curte
ffmpeg -i ../REFERENCIA-original.mp4 -vf "scale=in_color_matrix=bt709:in_range=tv:out_range=full:flags=accurate_rnd+full_chroma_int,format=rgb24" -vsync 0 -start_number 0 tmp/f%04d.png
python3 scripts/caixa.py      # camada de texto do gancho (scripts/texto_novo.npy)
python3 scripts/montar.py     # gera pecas/v3-quem-ele-curte.mp4
mkdir -p tmp/out && ffmpeg -i pecas/v3-quem-ele-curte.mp4 -vf "scale=in_color_matrix=bt709:in_range=tv:out_range=full:flags=accurate_rnd+full_chroma_int,format=rgb24" -vsync 0 -start_number 0 tmp/out/f%04d.png
python3 scripts/conferir.py && python3 scripts/folha.py
```
- **Fontes** em `fontes/`: Open Sans variável, baixada do google/fonts (OFL); Montserrat e TikTok Sans vêm do lote var1.
- **Scripts de medição**: `fit*.py` e `rastreio.py`.
