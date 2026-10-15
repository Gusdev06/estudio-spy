# Montagem — receitas de ffmpeg

O script `scripts/montar.sh` faz o caminho principal. Este arquivo é pros casos que fogem dele.

## Extrair o áudio original

```bash
ffmpeg -y -i referencia.mp4 -vn -ac 1 -ar 44100 -c:a aac audio-original.m4a
```

Mono e 44.1kHz basta pro lipsync e mantém o upload pequeno. Se a peça tem trilha além da voz e você quer só a fala, não tem separação limpa via ffmpeg — nesse caso avise o usuário que a Versão A vem com a trilha junto.

## Último frame de um clipe (encadeamento)

```bash
ffmpeg -y -sseof -0.1 -i clipes/a-01.mp4 -vframes 1 -q:v 2 clipes/a-01-last.jpg
```

`-sseof -0.1` busca 0.1s antes do fim. Buscar exatamente o fim às vezes devolve frame vazio, dependendo de como o clipe foi encerrado.

Confira que o JPG saiu com o rosto nítido antes de usar como `start_image` — se o último frame pegou uma piscada ou a boca aberta no meio de uma sílaba, o clipe seguinte nasce daquela cara. Nesse caso pegue meio segundo antes:

```bash
ffmpeg -y -sseof -0.6 -i clipes/a-01.mp4 -vframes 1 -q:v 2 clipes/a-01-last.jpg
```

## Concatenar

O concat demuxer exige **parâmetros idênticos** entre os arquivos. Clipes gerados voltam com fps e resolução variáveis, então normalize antes — é o que `montar.sh` faz. Concatenar sem normalizar dá arquivo que só toca o primeiro clipe, ou áudio andando à frente da imagem.

```bash
# lista.txt com: file '/caminho/absoluto/clipe.mp4'
ffmpeg -y -f concat -safe 0 -i lista.txt -c copy saida.mp4
```

Caminho **absoluto** na lista, ou use `-safe 0` com caminho relativo à lista.

## Normalizar preservando enquadramento

```bash
ffmpeg -y -i entrada.mp4 \
  -vf "scale=1080:1920:force_original_aspect_ratio=decrease,\
pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,fps=30,setsar=1" \
  -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a aac saida.mp4
```

`force_original_aspect_ratio=decrease` + `pad` em vez de `scale` puro: esticar o frame deforma o rosto, e rosto deformado é exatamente o que denuncia o criativo.

## Conferir antes de entregar

```bash
ffprobe -v error -show_entries format=duration \
  -show_entries stream=codec_name,width,height,r_frame_rate \
  -of default=nw=1 saida.mp4
```

Depois **assista**: `/watch <arquivo>` nas duas versões. Procure especificamente por deriva de rosto entre clipes, mão entrando no quadro, e a boca na emenda. Entregar sem olhar é passar o problema adiante.

## Duração: dê folga

Gere o vídeo mudo **1 a 2 segundos mais longo** que o áudio original. Sobra o `sync_mode=cut_off` corta de graça; falta obriga a `loop`, que repete movimento corporal e aparece na hora.

O `montar.sh` compara as durações no fim e avisa se ficou curto.

## Cortes de edição que ficaram de fora

O pedido é talking head limpo, então overlays, split screen, screen recording e legenda queimada **não são recriados**. Liste na entrega o que existia no original pra pessoa saber o que precisa reconstruir na edição:

- barra de caption fixa
- screen recording de UI
- dramatização / b-roll
- selo de contador / prova social
- legenda palavra-a-palavra

Se o original não tinha legenda em parte do vídeo (comum, e um erro), vale sinalizar — é o teste mais barato que existe em cima da peça nova.
