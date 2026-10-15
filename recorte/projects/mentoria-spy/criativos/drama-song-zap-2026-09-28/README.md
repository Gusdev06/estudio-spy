# Lote drama-song Spy Zap — 28/09/2026 (Bisturi)

Formato "drama-style song VSL": mini-drama cantado em 1ª pessoa, animação 3D. Escopo acordado com o Gusta: música completa, fichas da Maya ANTES e do Ryan, 1 cena sonda (B05). Insumos da Isca, que não foram editados: `../../roteiros/2026-09-28-drama-song-zap/` (letra.txt, estilo-musical.txt, personagens.md, plano-de-cenas.md). Portal: `../../esteira.html`.

**Mídia fora do git.** O `.gitignore` local cobre mp3, wav, mp4 e png. O que é texto (README, mapas, scripts, `_runs/*.json`) pode ser versionado.

## Gasto (conta WaveSpeed, chave `macbook`)

Teto do lote: US$ 2,50.

| # | Arquivo | Modelo | Estimativa (`wavespeed price`) | Real (`wavespeed billings`, key macbook) |
|---|---|---|---|---|
| 1 | `musica/cancao-v1.mp3` | `minimax/music-2.6` | US$ 0,15 | **US$ 0,15** (09:47:54Z) |
| 2 | `fichas/maya-antes.png` | `openai/gpt-image-2/text-to-image`, medium, 1k, 16:9 | US$ 0,06 | **US$ 0,057** |
| 3 | `fichas/ryan.png` | idem | US$ 0,06 | **US$ 0,057** |
| 4 | `shot-sheets/B05.png` | `openai/gpt-image-2/edit`, high, 1k, 9:16, 2 refs | US$ 0,242 | **US$ 0,2299** |
| 5 | `sonda/B05-clipe.mp4` | `bytedance/seedance-2.0-fast/image-to-video`, 720p, 7 s, sem áudio | US$ 1,40 (US$ 0,20/s) | **US$ 1,40** |
| | **Total** | | US$ 1,912 | **US$ 1,8939** |

Houve uma chamada ao Seedance recusada antes de rodar ("invalid request body": URL duplicada no campo image). Ela não gerou cobrança; conferi no billings. A transcrição foi local e não custou nada.

Saldo: US$ 5,875 no início. No fim apareceu US$ 23,98, então alguém recarregou a conta no meio do lote. O gasto real acima vem do billings, não da diferença de saldo.

## O que gerou cada arquivo

### 1. Música: `musica/cancao-v1.mp3`
- `minimax/music-2.6` com `lyrics` = letra.txt inteira (2.374 bytes por `wc -c`) e `prompt` = estilo-musical.txt. O input exato está em `_runs/musica-v1.json`.
- **225,2 s (3:45)**, 256 kbps, e decodifica inteiro sem erro (`ffmpeg -f null`). Tem voz do começo ao fim, do intro falado ao CTA "Tap the link…", seguida de ~5,5 s de cauda instrumental. Não precisou de retry.
- Não achei silêncio acima de 1,5 s (silencedetect a −35 dB).

### 2. Mapa de tempo: `mapa-de-tempo.json` + `mapa-de-blocos.md`
- Transcrevi local com `mlx_whisper` (`mlx-community/whisper-large-v3-turbo`, word timestamps, via `uvx --from mlx-whisper`), custo zero. A saída bruta está em `_runs/whisper/cancao-v1.json`.
- `scripts/mapa.py` alinha as palavras da letra (o texto vem da letra) com as do Whisper (os tempos vêm do Whisper) usando difflib. Todas as 58 linhas casaram, com no mínimo 5 de 8 palavras por linha, e nenhuma precisou de interpolação.
- Descartei uma alucinação: "Thank you." em 224,56 s.
- O `mapa-de-blocos.md` traz as durações reais B01–B25 contra a estimativa da Isca. Três refrões passam de 15 s (B06, B10, B19) e precisam de 2 clipes cada.
- **Ouvir antes de fechar a peça:** na linha 33 ("Not a stranger. **Jess.** The friend I knew") o Whisper ouviu "**just** a friend". Se a cantora engoliu o nome, o áudio não entrega a virada da trama. Também vale ouvir a linha 16 ("counselor" saiu como "counseling") e a 27 ("She'd lived this once"). A lista completa está no mapa-de-blocos.md.

### 3. Fichas: `fichas/maya-antes.png`, `fichas/ryan.png`
- Usei o prompt de 4 vistas de personagens.md sem mudar nada, com o bloco DESCRIÇÃO literal. `gpt-image-2` text-to-image, medium, 1672×941. Inputs em `_runs/ficha-*.json`.
- **Maya:** coque bagunçado, olheiras, argolas douradas e cardigã cinza saíram bem. A pinta aparece, mas no close fica **no canto do lábio do lado direito dela** (lado esquerdo de quem olha) e rente à linha do lábio, não acima. Nas vistas de corpo inteiro ela quase não aparece. A descrição pede o lado esquerdo dela. No shot sheet e no clipe a pinta apareceu do lado esquerdo dela, então o modelo não mantém o lado de forma estável. Se o lado importar, reforçar no prompt "on HER left (viewer's right)".
- **Ryan:** meio sorriso, relógio prateado no pulso esquerdo e o conjunto blusão marinho + chino saíram certos. O cabelo saiu castanho-médio, mais escuro que o "dark-blond" pedido. Aceitável.

### 4. Shot sheet: `shot-sheets/B05.png`
- `gpt-image-2/edit`, quality high, 9:16, 768×1360, com as 2 fichas como referência (image 1 = Maya, image 2 = Ryan) e o molde 2x2 do plano, que tem as DESCRIÇÕES literais da Maya, do Ryan, da Jess e da Linda (as duas últimas desfocadas). Input em `_runs/shot-B05.json`.
- Olhei a imagem. Os rostos batem com as fichas nos 4 quadros. Aparecem a pinta e as argolas da Maya no quadro 4 e o relógio do Ryan no quadro 3. A Jess ruiva e a Linda grisalha ficam ao fundo. O celular está com a tela escura, sem interface.
- Desvio: no quadro 2 a mão da Maya está esticada em direção ao celular, não parada acima dele.

### 5. Clipe sonda: `sonda/B05-clipe.mp4` e `sonda/B05-com-musica.mp4`
- `seedance-2.0-fast/image-to-video`, 720p (720×1280, 24 fps), 7 s, `generate_audio=false`. Deixei o prompt explícito: a grade é storyboard e não deve aparecer, nem no primeiro frame. Input em `_runs/sonda-B05.json`. Decodifica inteiro.
- `B05-com-musica.mp4`: corte de 1,00 s até o fim (6,04 s úteis), esticado 1,142× (setpts) para cobrir os **6,90 s** do bloco. O áudio é o trecho exato da canção, **27,92–34,82 s** ("He slid his phone to me… he told the rest"). Medi a coluna central nos primeiros frames da versão final e não há calha branca.
- Os frames para olhar estão em `sonda/contact.png` e `sonda/contact2.png` (0 / 0,3 / 1,2 / 2,5 / 3,8 / 5,2 / 6,9 s e a transição).

## Achados da sonda B05

| Pergunta | Resultado |
|---|---|
| A grade vazou? | **Sim, no início.** Porque o `image-to-video` usa a imagem como 1º frame, do frame 0 ao 0,92 s (23 frames) o vídeo é a própria grade 2x2 com os painéis se mexendo. Em 0,96 s há um corte seco para tela cheia (medido pelo brilho da coluna e da linha centrais: ~155–190 com a calha branca, ~90 sem). A instrução no prompt não impediu. **Solução barata: descartar o 1º segundo** (feito na versão com música). Para isso, gerar cada clipe com +1 s. |
| O rosto bate com a ficha? | **Sim.** A Maya mantém coque, cardigã, argolas e a pinta (visível no close final, lado esquerdo dela). O Ryan mantém cabelo, marinho e meio sorriso. Nenhuma troca de identidade. |
| Mão ou objeto estranho? | O frame de transição (~0,96–1,0 s) tem um borrão/"dedo" na toalha, que ficou dentro do trecho descartado. Depois disso, mãos e celular estão normais e a tela segue escura, sem interface. |
| Inventou segunda pessoa? | Não. Só aparecem a Maya, o Ryan e as convidadas ao fundo, que já estavam no sheet. |
| Seguiu os 4 momentos? | **Parcial.** Na ordem que aparece: 1 (Ryan desliza o celular) só dentro da grade, depois a mão da Maya **pega** o celular (o plano pedia que ela não tocasse), então a Maya chocada com o Ryan gargalhando atrás, e por fim o close lacrimejante com sorriso forçado. O momento 3 (Ryan de braços abertos falando pra mesa) **foi fundido** com o 4: o Ryan ri atrás dela, mas não abre os braços. |
| Veredito | **Aprovado com ajuste.** O visual e a consistência de personagem funcionam. O método "grade como 1º frame" custa ~1 s perdido por clipe e comprime os 4 momentos em ~6 s, então quatro ações num bloco de 7 s é demais. Para os próximos: 2–3 momentos por bloco curto, ou usar o **quadro 1 recortado como `image` e o quadro 4 como `last_image`** (o Seedance aceita). Isso elimina o vazamento e trava o frame final, e dá para testar num bloco de 4–5 s a 480p (~US$ 0,50). |

## Estimativa para fechar a canção inteira

Base: 25 blocos, 225,2 s. Os 3 refrões com mais de 15 s viram 2 clipes cada, o que dá **28 clipes**. Cada clipe é gerado com +1 s para descartar a grade (mínimo de 4 s), totalizando **266 s faturados**, ou **259 s** sem a B05, que já está paga. Preço do Seedance 2.0 Fast i2v conferido no `wavespeed price`: **US$ 0,20/s em 720p** e **US$ 0,10/s em 480p**.

| Item | 720p | 480p |
|---|---|---|
| Clipes (259 s) | US$ 51,80 | US$ 25,90 |
| Shot sheets restantes (27) | US$ 6,21 (high, US$ 0,23) | US$ 2,21 (medium, US$ 0,082) |
| Fichas restantes (Maya DEPOIS via edit, Jess, Nora) | ~US$ 0,20 | ~US$ 0,20 |
| **Subtotal** | **~US$ 58** | **~US$ 28** |
| Com +30% de margem para retry | ~US$ 76 | ~US$ 37 |

Com `image` + `last_image` recortados do sheet, o +1 s some: são ~240 s faturados, ~US$ 48 dos clipes em 720p e ~US$ 24 em 480p. A B05 real pesou US$ 0,20/s × 7 s = US$ 1,40, o que confere com o preço usado aqui.

## Erros nos insumos da Isca

- `plano-de-cenas.md` diz "~2.373 bytes". O `wc -c letra.txt` dá **2.374**. É trivial, dentro do teto de 3000.
- Não achei outro erro. A duração de ~3:20–3:45 bateu (3:45).

## Pastas

- `musica/`: canção
- `fichas/`: fichas de 4 vistas
- `shot-sheets/`: grades 2x2
- `sonda/`: clipe cru, versão com música, frames e contact sheets
- `scripts/mapa.py`: alinhamento da letra com o Whisper
- `_runs/`: inputs e outputs JSON de cada chamada, transcrição bruta e o wav do trecho da B05

---

## Rodada v2 — peça inteira H3 480p (28/09)

Pedido do maestro: peça inteira com **wavespeed-ai/minimax-h3/image-to-video 480p** (escolha do Gusta na `sonda-barata/`), letra **v2** (`letra-v2.txt`, repete o nome "Jess" na revelação). Teto duro US$ 15. A v1 ficou intacta (`musica/cancao-v1.mp3`, `mapa-de-tempo.json`, `shot-sheets/`, `sonda/`).

**Peças:** `pecas/drama-song-zap-v2-legendado.mp4` e `pecas/drama-song-zap-v2-sem-legenda.mp4`. 720×1280, 30 fps, h264 crf 18 + aac 192k, **197,27 s** (= duração da música). Decodificam inteiras sem erro. A música v2 é o único áudio; o áudio nativo do H3 foi descartado. Contact sheet de 24 frames: `pecas/contact-legendado.png`. Legenda ASS: `pecas/drama-song-zap-v2.ass`.

### Gasto (billings, key macbook, casado por prediction id, desde 10:15Z)

| Etapa | Modelo | Estimado | Real |
|---|---|---|---|
| Música v2 | minimax/music-2.6 | 0,15 | **0,15** |
| Fichas Jess, Nora, Linda | gpt-image-2 t2i medium 16:9 | 0,18 | **0,171** |
| Ficha Maya DEPOIS (edit, ref = Maya ANTES) + 23 shot sheets (high, 9:16, 1–4 fichas de ref) | gpt-image-2/edit | 5,36 | **5,6069** |
| 43 clipes (33 do plano + 10 retries, 277 s) | minimax-h3 i2v 480p, US$ 0,02/s | 4,38 + retry | **5,54** |
| **Total** | | **~11** | **US$ 11,47** |

Os sheets com 3–4 fichas de referência saíram um pouco acima dos US$ 0,23 do B05. Transcrição local (mlx-whisper large-v3), custo zero. O resto das cobranças do dia na key `macbook` é de outras sessões (conta compartilhada).

### Etapas
1. **Música v2** (`musica/cancao-v2.mp3`, 197,25 s, 1ª tentativa). Whisper `mlx-community/whisper-large-v3-mlx` com word timestamps (`_runs/whisper-v2/cancao-v2.json`) ouviu **"Not a stranger, it was Jess, my best friend Jess, the one I knew"** (116,5–121,1 s): o nome está audível, sem retry. A cantora repetiu a intro falada (1,34 s e 9,24 s). `scripts/mapa_v2.py` → `mapa-de-tempo-v2.json`; `scripts/plano_clipes_v2.py` → `mapa-de-blocos-v2.md` + `_runs/plano-clipes-v2.json`.
2. **Fichas** `fichas/jess.png`, `nora.png`, `linda.png` (t2i, prompt de 4 vistas de personagens.md com DESCRIÇÃO literal) e `maya-depois.png` (edit com a ficha ANTES como ref). Conferido: pérolas/ruivo/sardas da Jess, mecha grisalha + óculos na gola + pulseiras da Nora, pinta + argolas mantidas na Maya DEPOIS.
3. **Shot sheets** `shot-sheets-v2/B01–B25.png` (`B05.png` reaproveitado da v1). Spec em `scripts/cenas_v2.py`. Todos olhados: rostos batem com as fichas, sem texto legível em tela. Correções locais no quadro recortado (os originais ficam com sufixo `-orig`): **B10 q2** tinha um "beijinho" desenhado perto da boca do Ryan (inpaint) e **B21 q4** pôs a pinta da Maya na Jess (inpaint).
4. **Clipes** (`clipes-v2/`, `scripts/run_clip.py`): quadro inicial e final recortados sem calha (`scripts/recorta_quadros.py`, acha a calha pelo brilho, inset 6 px, 720×1280) em `image` + `last_image`. Blocos > 15 s (B01) ou com troca de lugar entre quadros (B06, B07, B10, B14, B17, B18, B19) viraram 2 clipes com pares de quadros do mesmo lugar. Duração gerada = teto(bloco + 0,15 s). Contact sheet de cada um em `contact-v2/`.
5. **Montagem** `scripts/monta_v2.py`: corta 0,1 s do início de cada clipe, escala 740×1280 → crop 720×1280, 30 fps, apara à duração exata do bloco, concatena, música v2 por cima. Legenda por linha do `mapa-de-tempo-v2.json` (intro nas duas vezes), Arial bold 50, branco com contorno preto, MarginV 250 (terço inferior-médio). Takes escolhidos em `_runs/takes-v2.json`.

### Blocos refeitos (1 retry cada, prompt em `_runs/retry-prompts/`)
| Clipe | Defeito da 1ª tentativa | Retry |
|---|---|---|
| B05 | tela do celular acesa com ícones de app (`B05-t1.mp4`) | prompt "tela preta/brilho em branco" → tela branca sem ícone, mãos no colo ✔ |
| B03 | homem inventado de suéter azul no meio | ✔ |
| B07b | Jess vira outra mulher (morena, cardigã) | ✔ |
| B08 | a conselheira troca de rosto e de roupa | ✔ |
| B14a | Jess aparece na cozinha ao lado da Maya | ✔ |
| B14b | Jess vira Maya e depois Nora | ✔ |
| B17a | Nora aparece no quarto | ✔ |
| B18a | Linda aparece na cozinha | ✔ |
| B18b | Linda ↔ Ryan trocam no meio do clipe | ✔ |
| B01a | mão com celular aceso e tela com UI em 1º plano | **parcial**: o retry ainda mostra o canto de um celular aceso (tela em branco) no pé do quadro |

A partir da B05 (tentativa 2), todo prompt de clipe leva "Any phone screen stays black or shows only a soft blank glow, never icons, apps or text".

### Defeitos conhecidos (não refeitos)
- **B01a**: canto de celular aceso no pé do quadro (tela em branco, sem texto legível). Único bloco com 2 tentativas ruins.
- **B06b**: o sorriso no espelho cresce em vez de sumir, e ela pega um celular (tela não legível).
- **B09**: o relógio digital mostra "01:27" (não é tela de celular; o plano pedia sem dígitos).
- **B10b**: o Ryan volta à cozinha em vez de sair.
- **B25**: a Maya olha o próprio celular (tela virada pra ela) em vez de apontar pro link, com sorriso um pouco exagerado. Serve de fundo pro CTA, mas não aponta.
- H3 480p fica um pouco mole (upscale 480×832 → 720×1280). Várias mesas de jantar têm celulares acesos em branco ao fundo, sem texto.
- A legenda cobre peito/mãos em alguns quadros de corpo inteiro, mas nenhum rosto nos 24 frames conferidos.

Nada foi subido na Meta.
