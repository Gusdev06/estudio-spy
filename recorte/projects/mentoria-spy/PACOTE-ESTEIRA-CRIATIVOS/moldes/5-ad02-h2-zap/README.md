# Molde 5 — AD02-H2 adaptado para WhatsApp

Mesmo molde 4 com os painéis do funil do Zap (cloud backup → mapa de rastreamento → lista de chats → relatório) e copy de WhatsApp. É o exemplo de **transplantar um formato entre ofertas**: as fronteiras dos blocos ficam nas mesmas palavras do original, recalculadas no whisper do áudio novo.

```bash
python3 gerar-timeline.py       # fronteiras dos blocos a partir do áudio novo
python3 gerar-karaoke-zap.py    # karaokê
bash gerar-paineis.sh           # recorta os painéis da gravação do funil, com as durações da timeline
python3 montar-zap.py clipes/z1.mp4 saida.mp4
```
Os painéis saem de uma **gravação de tela real do funil** (não de mockup gerado) — telefone e e-mail sempre desfocados.
