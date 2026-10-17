# Sarah Smith 1677505624160791: 3 variações (17/10/2026)

**Referência:** `REFERENCIA-original.mp4` (de `~/Downloads/AdLibNote_Sarah Smith_1677505624160791_adstart-2026-10-08_creative-01_video.mp4`), 720×1280, 30 fps, 1095 frames, só música (Whisper: sem fala).
**Molde:** gancho POV no café (f0–139, chicote f140–154) → demo do Gram Detect (f155–732) → reveal "Done! Now you can see everything on her account" + TRY IT FREE (f733–964) → CTA (até f1094).
**Erro do original:** a demo diz "Copy **his** @", mas o perfil pesquisado é de mulher (@samantha…) e o reveal diz "her account". As 3 variações trocam para "Copy **her** @" (legenda reconstruída na V3, reaproveitada em V1/V2).

| Peça | Alavanca | Gancho | Jev |
|---|---|---|---|
| `pecas/v1-chat-bros.mp4` (36,5 s) | formato + gênero do gancho | iMessage "pov: men talk about women": "bro how do I see who my girl is talking to on insta without her knowing??" | 0,561 (risco-fala 0,46) |
| `pecas/v2-resultado-primeiro.mp4` (33,8 s) | ordem (abre na prova) | placa "he said she was “just a friend” 🙂" → "so I checked her account 👇" sobre o reveal; café sai | **0,688** (0,18) |
| `pecas/v3-quem-ele-curte.mp4` (36,5 s) | copy do gancho, mesmo footage | “Girl, who's the girl he keeps liking pics of? 👀” | 0,588 (0,05) |
| original | — | “Girl, how do I get into my boyfriend's Insta without him knowing?” | 0,522 (0,58 ⚠️) |

Jev = `typesafe/pontuar_ganchos.py ganchos.json`, previsão direcional, não prova de conversão.

Detalhes, mapa de frames e comandos em cada pasta (`v1-chat-bros/README.md`, `v2-resultado-primeiro/README.md`, `v3-quem-ele-curte/README.md`). V1 e V2 leem a demo da peça V3 (`montar.py` / `work/montar.sh`): refazer a V3 antes. Versões com "his" guardadas em `v1-chat-bros/work/` e `v2-resultado-primeiro/work/`.

**Custo de geração:** US$ 0 (PIL, ffmpeg). Só o Jev (centavos de TypeSafe) e Whisper Groq pra confirmar que não havia fala.
