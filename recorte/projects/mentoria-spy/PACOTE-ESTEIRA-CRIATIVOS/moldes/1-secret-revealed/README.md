# Molde 1 — Secret Revealed (rosto cheio + faixa de headline + karaokê)

Peça: 1080×1920, rosto do avatar ocupando o quadro inteiro, **faixa vermelha de duas linhas** no topo (y 176–384) e **karaokê de uma palavra** (Arial Rounded Bold 86, tracking 7, capitais em y 1248). Sem CTA no fim. Referência: `../../midia/ref-1-secret-revealed.mp4`.

## Produzir uma variação (copy nova + avatar novo)
```bash
# 1. copy e voz  (edite copys.json: h1, h2 = as duas linhas da faixa; txt = a fala)
bash gerar-audio.sh v01

# 2. rosto novo (descrição em elencos/v01.txt) → imagem 9:16
wavespeed run openai/gpt-image-2/text-to-image --input-file base/v01.req.json --json --download base/v01.png

# 3. lipsync
bash gerar-clipes.sh v01

# 4. faixa redesenhada + montagem
python3 fazer-selo.py "SHE'S CHEATING ON YOU" "YOU JUST DON'T WANT TO SEE IT" molde/selo-v01.png
python3 montar.py clipes/v01.mp4 pecas/v01.mp4 --audio audio/v01-ritmo.wav --selo molde/selo-v01.png
```
`montar.py` tira a duração do áudio novo, gera o karaokê do whisper desse áudio e aplica a faixa. Opções úteis: `--zoom`, `--th-y` (enquadramento do rosto), `--tamanho`/`--tracking` (karaokê), `--atraso` (sincronia da legenda).

`remontar-secret.py` é a versão original (usa o áudio do anúncio e recorta a faixa do próprio original) — serve quando você só quer trocar o rosto.
