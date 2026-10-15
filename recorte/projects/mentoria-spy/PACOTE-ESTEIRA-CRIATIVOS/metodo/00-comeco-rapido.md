# Começo rápido — sua primeira peça em ~25 minutos

Objetivo: pegar um criativo que já escala e devolver a mesma peça com **outro rosto**. Custo: ~US$ 0,85.

```bash
# 0. instalar (uma vez)
brew install ffmpeg uv && pip3 install pillow numpy opencv-python-headless && npm i -g @wavespeed/cli && wavespeed login

# 1. medir o criativo que você baixou da Ad Library
ffprobe -v error -show_entries stream=width,height,r_frame_rate,nb_frames:format=duration -of default=nw=1 original.mp4
python3 scripts/analisar-estrutura.py original.mp4          # onde estão as faixas e os cortes
ffmpeg -i original.mp4 -vf "fps=1,scale=140:-1,tile=15x3" -frames:v 1 folha.jpg   # olhe esta folha

# 2. tirar o áudio (vai ser reaproveitado)
ffmpeg -i original.mp4 -vn -c:a libmp3lame -b:a 160k audio.mp3

# 3. rosto novo a partir de um frame do original
ffmpeg -ss 2 -i original.mp4 -frames:v 1 frame.png
wavespeed upload frame.png --json        # guarde a url
#   monte o .req.json com o prompt de metodo/02-prompts.md e rode:
wavespeed run openai/gpt-image-2/edit --input-file base.req.json --json --download avatar.png

# 4. lipsync (imagem + áudio)
wavespeed upload avatar.png --json ; wavespeed upload audio.mp3 --json
wavespeed run pruna-ai/p-video/avatar --input-file clipe.req.json --json --download clipe.mp4

# 5. CONFERIR antes de montar
ffmpeg -v error -i clipe.mp4 -f null -                       # download íntegro?
ffmpeg -i clipe.mp4 -vf "select='not(mod(n,30))',scale=90:-1,tile=24x1" -vsync 0 -frames:v 1 varredura.jpg
python3 scripts/checar-identidade.py clipe.mp4               # trocou de pessoa?

# 6. montar com o molde certo (moldes/<n>/README.md)
```

Se o criativo que você baixou for um dos 5 moldes que já estão aqui, pule para o README do molde — o trabalho de medição já está feito.
