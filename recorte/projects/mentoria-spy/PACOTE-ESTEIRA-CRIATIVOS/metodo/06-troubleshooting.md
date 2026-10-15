# Troubleshooting

| sintoma | causa | solução |
|---|---|---|
| Clipe baixado com poucos KB, montagem sai com 19 frames | a CLI da WaveSpeed cortou o download e **não deu erro** | `ffmpeg -v error -i x -f null -`; rebaixar com `scripts/rebaixar.py "pasta/*.out.json"` |
| `KeyError: 'url'` no upload | upload recusado por rede | retry de 5 tentativas (ver `moldes/1-secret-revealed/gerar-clipes.sh`) |
| `Prediction failed: empty output` / `Service temporarily unavailable` | instabilidade do provedor; **é estornado** | repetir o mesmo request; se o áudio tiver > 40 s, partir em dois |
| Rosto cortado na janela | recorte fixo calibrado em outro avatar; ou clipe veio em orientação diferente (imagem 16:9 → clipe 1280×704) | recorte centrado no rosto, lendo a orientação real do clipe |
| "Piscou outro avatar" | (a) frame 0 do Pruna é a imagem parada; (b) o modelo trocou de pessoa no meio | pular frame 0; prompt de identidade travada; refazer o clipe |
| Mão/celular na frente da lente | prompt negativo ("out of frame") | descrever a pose em positivo, sem citar o objeto |
| Legenda estourando a borda | bloco montado só por contagem de palavras | limitar também pela **largura** da linha (ex. 640 px em 720) |
| Voz baixa demais na mistura | MiniMax sai ~6 dB abaixo | `loudnorm=I=-16:TP=-1.5:LRA=11` na voz; música em −28 dB |
| `mlx_whisper` não existe (Windows/Linux) | é Apple Silicon | `pip3 install faster-whisper` e trocar por um shim com a mesma saída JSON (`{"segments":[{"words":[{"word","start","end"}]}]}`) |
| `colorbalance` reclama de opção | nome das opções mudou entre versões do ffmpeg | usar `rs/gs/bs` e `rm/gm/bm`, não `ms` |
| Montagem com karaokê estoura a memória | 900+ PNGs abertos em PIL | montar **uma peça por vez** e conferir o tamanho do arquivo final |
