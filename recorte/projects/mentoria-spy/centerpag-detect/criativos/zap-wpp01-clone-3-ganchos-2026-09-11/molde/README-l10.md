# Molde L10 — wpp-01 Esther Vicman (card alfa sobre plano único) · medido em 2026-09-05

Tudo medido no `centerpag-detect/escalados/whatsapp/01-esther-vicman-1762552938111855.mp4` (360×640, 30 fps, 56,77 s) por análise de pixel (numpy sobre frames rawvideo), depois ×3 pra 1080×1920. Teardown de edição: `centerpag-detect/referencias/2026-09-01-teardown-edicao-wpp01-esther-vicman.md`. Wiki: [[card-flutuante-sobre-plano-unico]].

| elemento | medido (nativo 360×640) | no molde (1080×1920) |
|---|---|---|
| **Matte do topo** | 100 % preta até y 91–97 (t = 2 · 12 · 25 s); teardown: y 96 | y 0–288 — é o talking head colado abaixo de y 288 (recorte 1080×1632 em `--off-head`) |
| **Hook fixo** | 2 linhas, y 25–44 e 54–74 (cap 20 px, passo 29), centro x 178, amarelo **#EEFF00** (238,255,0 — cor mais frequente), contorno preto | Poppins Bold 86 (cap ≈ 60 px), topos y 75 / 162, contorno 5 + sombra 4 — **é o único lugar onde A/B/C diferem** |
| **Card do app** | x 65–290 (largura 227 = 63 %), topo y 410, corre pra fora do quadro por baixo; cantos arredondados; borda em gradiente (sem degrau — o detector de fronteira reprova); **alfa ≈ 0,85** (preto da UI sobre jaqueta luma 45 dá 6–7; URL bar cinza dá 38–50 ≈ 0,85·60 + 0,15·45) | x 200, largura 680, topo y 1230, altura 1261 (gravação 1170×2170 na proporção), raio 45, máscara com feather 6 px, `colorchannelmixer aa=0.85` |
| **Fase 3 — card toma a tela** | x 10–350, y 15–625, fundo preto, o ator some | card 1020×1830 em (30,45), raio 45, sobre preto |
| **Fase 4 — payoff** | tela cheia, sem card | gravação 1080 de largura, recorte 1080×1920 |
| **Karaokê** | amarelo #EEFF00, caixa alta, 2–4 palavras; 1 linha até 16 caracteres ("THE OTHER PERSON"), 2 linhas acima disso ("AND INSTANT / MESSAGES"); cap 16 px; **topo y 513 (81 %)** sobre o card, **y 309 (50 %)** nas fases de tela cheia; 2 linhas: 501 / 524 (passo 23) | Poppins Bold 69 (cap 48), topo y 1539 (card) / 927 (cheio·bleed·cta), passo 69, contorno 4 + sombra 3 |
| **CTA final** | tela borra; 4 linhas `CLICK THE LINK / BELOW AND / SEE THE TRUTH / NOW`, y 134–163 · 176–206 · 219–248 · 261–291 (cap 30, passo 42,5), x 13–341; chevrons amarelos em **contorno** (sem preenchimento), 1→2→3 empilhados, y ≈ 370–520, centro x 180, laço ≈ 1,2 s | boxblur 30 com fade de 0,35 s; Poppins Bold 129, topos 402 + k·128; `molde/setas/000–035.png` (360×450, 36 frames em laço) em (360, 1110) |
| **Cortes** | 0,03 · 8,80 · 30,77 · 40,00 · 41,70 · 49,03 · 49,67 · 50,53 · 50,90 · 52,07 | corte seco por bloco; só o CTA entra com fade do borrão |
| **Gravação do funil** | — | área útil = `crop 1170:2170:0:110` (sem barra de status nem Safari); `vel < 1` = câmera lenta pra segurar tela parada; `blur x:y:w:h;…` em coordenadas da gravação |

Fonte: não há Poppins ExtraBold no repo; Poppins Bold + contorno 5 px chega perto do peso do campeão.

## Arquivos

- `remontar-l10.sh` / `remontar-l10.py` — o molde. `bash remontar-l10.sh <talking-head.mp4> <blocos.tsv> <hooks.txt> <karaoke.tsv> <prefixo> [--off-head N] [--rec …] [--cta "L1|L2|L3|L4"]` → `<prefixo>-base.mp4` (crf 10, sem hook) + `<prefixo>-A/-B/-C.mp4` (só o texto do matte muda; áudio do talking head copiado).
- `karaoke-l10.py <whisper.json> <karaoke.tsv>` — blocos de 2–4 palavras, caixa alta, `|` quebra em 2 linhas acima de 16 caracteres. Whisper local: `uvx --from mlx-whisper mlx_whisper audio-16k.wav --model mlx-community/whisper-small.en-mlx --word-timestamps True --output-format json`.
- `blocos.tsv`: `ini_s fim_s fase(card|cheio|bleed|cta) rec_ini_s vel blur nota`. O Isca entrega o trecho do funil por bloco; a linha vira uma linha aqui.
- `hooks.txt`: `variante<TAB>linha1|linha2`.

## Teste do molde (campeão como entrada)

`bash remontar-l10.sh centerpag-detect/escalados/whatsapp/01-esther-vicman-1762552938111855.mp4 molde/blocos-teste-wpp01.tsv molde/hooks-teste.txt molde/karaoke-teste-wpp01.tsv conferencia/molde/teste-wpp01 --off-head 288` → `conferencia/molde/teste-wpp01-{base,A,B,C}.mp4` (56,77 s, 1703 frames). `--off-head 288` descarta o matte do próprio campeão, então o ator entra limpo abaixo do nosso matte; o card queimado do campeão aparece por baixo do nosso (só no teste). Folha: `conferencia/molde/folha-molde-l10.jpg` (campeão | molde em t = 2 · 5 · 12 · 25 · 33 · 45 · 50 · 53 s), `mattes-abc.jpg`, `zoom-card-t25.jpg`.

Blocos do teste (trechos SEM mapa da gravação): Chats + "257 deleted messages recovered!" (rec 179,4 s, vel 0,17, botão Unlock desfocado) → formulário digitando (rec 1,5, campo desfocado) → "Accessing WhatsApp" checklist (rec 7,3, número vermelho desfocado) → BACKUP RECOVERED / HIDDEN DATA DETECTED (rec 152) → **cheio** BIOMETRIC SIGNATURE ANALYSIS → MATCH FOUND 94,7 % (rec 158,5) → **bleed** conversas recuperadas (rec 190,5) → **cta** (rec 199,5 borrado).

PII na gravação (checar por bloco): número real inteiro no campo do formulário (x 690–1030 · y 633–811), em vermelho em "Accessing WhatsApp" (x 276–895 · y 779–832), no card de perfil (y 340–635, t ≥ 20 s), no botão "Unlock Conversations" (x 300–900 · y 1565–1635 em t 179–181), no terminal (t 146–152, texto miúdo) e "Gabriel, … 6872" nos resultados (t 183–190). E-mail em "Your report is ready" (t 168–178) — não usar.

## Custo

Zero (ffmpeg + whisper local). Lipsync/TTS/OmniHuman do talking head são do Maestro e ficam fora daqui.
