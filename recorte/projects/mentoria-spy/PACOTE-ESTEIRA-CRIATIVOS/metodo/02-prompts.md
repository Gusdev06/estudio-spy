# Prompts que funcionam (copiar e adaptar)

## 1. Rosto novo a partir de um frame do original — `openai/gpt-image-2/edit`
Manda o frame do criativo original como `images[0]` e descreve **só o que muda**:

```
Same room, same phone front camera held at arm's length just above eye level, same framing distance,
same soft daylight, same background of <o que estiver atrás>, same slightly overexposed look of a real
phone recording. Extend the scene vertically into a 9:16 vertical frame, keeping the original composition
in the upper band. REPLACE the man with a DIFFERENT man: <descrição do novo avatar>. Same posture, head
and shoulders filling the upper half of the frame, looking straight into the lens, mouth closed, serious
and confiding expression. Photorealistic phone-camera video still, natural skin texture with visible pores,
mild camera softness, no retouching, ordinary person, not a model, no text, no logos, no watermark.
```
`aspect_ratio` = o do bloco onde o rosto entra (`9:16` para quadro cheio, `16:9` para janela deitada), `quality=medium`, `resolution=1k`.
Sem frame de referência (cenário novo), o mesmo prompt em `text-to-image`.

**Descrição do avatar:** etnia + tom de pele + idade + cabelo + pelo facial + acessório + peça de roupa lisa. Ex.: *"a Black man with deep dark skin, about 28, short fade haircut and a neatly lined full beard, wearing the same style plain cream hoodie"*.

## 2. Lipsync — `pruna-ai/p-video/avatar`
```json
{"image":"<url da imagem>","audio":"<url do mp3>","resolution":"720p","seed":21,
 "video_prompt":"The man in the image — <descrição> — stays EXACTLY the same person from the first frame to the last: same face, same hair, same clothes, same framing and distance from the camera. Selfie-style webcam recording, camera locked off at eye level; the camera never moves and the room behind him stays the same. Both of his arms hang relaxed at his sides, completely out of frame, for the whole clip, and nothing is held in front of him or shown to the camera. SOLO SHOT, exactly one person; nothing ever enters the frame from the edges. He talks straight into the lens, serious and direct, with small natural head movements only."}
```
- **Podcast/entrevista:** troque as duas últimas frases por *"She is the ONLY person in the studio for the entire clip, alone on the cream sofa; locked-off camera, same background and microphone; her hands rest on her lap"*.
- **Two-shot** (duas pessoas): *"EXACTLY TWO women are in the frame, both seated, and nobody else ever appears. Only the woman on the RIGHT is talking; the woman on the LEFT listens with her mouth closed."*
- Áudio acima de ~40 s costuma ser recusado: **parta o áudio na fronteira de uma frase** e gere 2 clipes da mesma imagem; a emenda cai num corte de bloco e não aparece.

## 3. Voz — `minimax/speech-2.6-hd`
```
wavespeed run minimax/speech-2.6-hd -i "text=<copy>" -i voice_id=Casual_Guy -i speed=1.08 \
  -i emotion=neutral -i language_boost=English -i english_normalization=true \
  -i format=mp3 -i sample_rate=44100 -i bitrate=128000 -i channel=1 --json --download vo.mp3
```
Vozes que usamos: `Casual_Guy` (homem UGC), `Determined_Man` (mais firme), `Calm_Woman` (host), `Wise_Woman` (convidada). Depois **corte as pausas**: `python3 scripts/cortar-pausas-audio.py vo.mp3 vo-ritmo.wav` (todo silêncio ≥ 0,4 s vira 0,25 s — regra de ritmo que deixa o wpm em 190–210).

A locução do MiniMax sai ~6 dB abaixo de uma mistura de anúncio: normalize com `loudnorm=I=-16:TP=-1.5:LRA=11` antes de mixar.
