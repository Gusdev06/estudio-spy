# Conferência (o que olhar antes de dar por pronta)

1. **Folha do clipe inteiro** — 16 a 24 frames do lipsync: mão/celular na frente da lente, segunda pessoa entrando, troca de identidade, fundo deformando.
   `ffmpeg -i clipe.mp4 -vf "select='not(mod(n,30))',scale=90:-1,tile=24x1" -vsync 0 -frames:v 1 varredura.jpg`
2. **Drift de identidade** — `python3 scripts/checar-identidade.py clipes/*.mp4` compara tamanho e cor do rosto no frame 0 com a mediana do resto. `×0,8–1,25` é normal; fora disso, olhe.
3. **Emendas** — um frame antes e um depois de cada troca de bloco, pra ver se não ficou preto nem salto de enquadramento.
4. **Original × novo** — 8 a 14 instantes lado a lado com o original: as camadas têm que cair no mesmo lugar.
5. **Áudio** — `ffmpeg -i peça.mp4 -af silencedetect=n=-35dB:d=0.4 -f null -` (0 silêncios longos) e `volumedetect` (fala ~−16 a −20 dB; cama de música ~−28 dB).
6. **Contagem de frames** — a peça tem que ter a duração e o número de frames esperados (`ffprobe -show_entries stream=nb_frames,duration`).
7. **Integridade dos downloads** — `ffmpeg -v error -i x -f null -` em todo clipe baixado.

Guarde tudo isso numa pasta `conferencia/` por lote: é o que permite responder "por que essa peça está diferente?" três semanas depois.
