# Molde 4 — AD02-H2 (Instagram): rosto cheio + caixa de gancho + painéis do app

Peça 1080×1920, 5 blocos: card "Connecting" → painel de perfil → rosto limpo → painel de DMs → CTA com setas. O gancho escrito é uma **caixa rosa (#FE0553, letra #EEFC00)** de confissão em caixa mista que some aos 7,8 s. Karaokê em Oswald Bold amarelo/vermelho alternando. Referência: `../../midia/ref-4-ad02-h2.mp4`; o campeão que originou a copy é `ref-5-gd-ad01-campeao.mp4`.

```bash
python3 gerar-karaoke.py                      # 1 PNG por frame, a partir do whisper do áudio
python3 montar-reconstrucao.py clipe.mp4 saida.mp4     # troca só o avatar (áudio e hook do original)
python3 montar-super.py clipe.mp4 saida.mp4            # versão com copy própria + caixa de gancho nova
```
Env úteis: `Z` e `OY` (zoom e offset do rosto — Gusta pediu **plano fixo**, sem zoom por bloco), `BLUR` (desfoque do rosto nos blocos de painel), `CAIXA_L1`/`CAIXA_L2` (texto da caixa). Os painéis e as setas/CTA prontos estão em `assets/`.
