# HANDOFF · Isca → Bisturi · 2026-09-11 · lote gram01-l9-var-avatar

Medição, não opinião. Roteiro completo em `2026-09-11-gram01-var-avatar-5-rostos.md`.

## 1. A VO tem 9 silêncios ≥ 0,4 s — NÃO corte nenhum

O briefing diz ~~"0 silêncios ≥0,4 s a −35 dB"~~. `ffmpeg -af silencedetect=n=-35dB:d=0.4` em
`gram01-l9-faixa-2026-09-01/vo/vo-master-en.m4a` devolve **9** (3,545 · 6,547 · 9,891 · 12,635 ·
14,924 · 18,169 · 21,959 · 26,320 · 28,631 s; somam 5,034 s). A −60 dB ainda dá 6. Todos caem em
fronteira de beat ou vírgula: são a respiração escrita.

**O `cortar-pausas.py` do lote wpp01 não roda aqui.** A VO tem que ser bit-idêntica ao controle
(md5 `776f219435732e5ad4e24556e85397ee`) — uma alavanca por teste. Trava 4 do roteiro: na peça
pronta, `silencedetect` tem que devolver **9**; se devolver 0, alguém cortou pausa.

## 2. Como a VO está assentada no controle

- Faixa de áudio de `pecas/gram01-l9-en-01-v2.mp4` = VO com **offset 0 ms** (corr 1,0000),
  resíduo −78,8 dBFS.
- Stream de áudio dura **31,927 s** dentro de um vídeo de **32,500 s**: os últimos 0,573 s não têm
  amostra. Primeira fala 0,179 s · última 31,667 s.
- Pra peça final: `-c:a copy` da faixa do controle. Se o Pruna precisar de `apad` pra cobrir 32,5 s,
  o pad é só na cópia enviada ao modelo.

## 3. `video_prompt` (o mesmo nas 5)

Arquivo: `2026-09-11-gram01-var-avatar-5-rostos/video-prompt.txt` (md5 `2db97c219265d3d321e47ab1eba97e20`).
Usar a principal; a `-reserva.txt` só se a principal exagerar o movimento.

## 4. Nome de arquivo

`gram01-l9-en-01-V2.mp4` difere do controle `gram01-l9-en-01-v2.mp4` só pela caixa — APFS padrão
é case-insensitive. Pastas diferentes evitam sobrescrever, mas confunde no portal. Sugestão:
`gram01-l9-en-01-v2-av1-<slug>.mp4` … `av5`. Decisão é sua.

## 5. Custo pra mostrar antes de disparar

5 × ceil(31,927) = 32 s × US$ 0,025 = **US$ 4,00** (4,125 se enviar com pad a 33 s). Pruna volta
704×1280 a **24 fps** (var4: 793 fr / 33,042 s — o README de lá diz 25; `ffprobe` diz 24).
