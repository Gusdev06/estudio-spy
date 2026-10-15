# Molde 3 — podcast WhatsApp (layout de post)

Peça 720×1280: **título fixo** (caixa branca, y 140–270), **janela de vídeo 720×587** em y 346 e **karaokê** (caixa alta branca + caixa roxa #6912D1 na palavra falada, y 967–1031). A janela alterna closes dos avatares e painéis do funil; os últimos 15 s são o b-roll de CTA em quadro cheio. Referência: `../../midia/ref-3-podcast-wpp-57s.mp4`.

## Copy nova + avatares novos (o caminho completo)
```bash
# 1. roteiro em diálogo (roteiro.tsv: id, papel A/B, fala) → uma voz por papel, pausas de 0,12/0,24 s
# 2. gera a timeline das linhas e corta o áudio por bloco
# 3. 2 imagens (edit sobre frames do original) + 6 clipes de lipsync (um por bloco de fala)
bash gerar-clipes-variacao.sh w1
# 4. karaokê do áudio novo + montagem
python3 gerar-karaoke.py
CLIPES=w1/clipes python3 montar.py pecas/w1.mp4
# 5. trilha por baixo (normalizada no nível da cama do original, −28,5 dB)
bash por-musica.sh pecas/w1.mp4 ../../midia/trilha-suspense.mp3 pecas/w1-musica.mp4
```
`montar-clone-v2.py` é a variante que só troca o avatar mantendo a copy do original (recorte centrado no rosto, sem two-shot).
