# Kling 3.0 via WaveSpeed — chamadas exatas

## Modelos

| Uso | Model ID | Preço |
|---|---|---|
| Clipe do avatar (padrão) | `kwaivgi/kling-v3.0-pro/image-to-video` | $0.56 |
| Clipe barato (validar enquadramento/ritmo) | `kwaivgi/kling-v3-turbo-pro/image-to-video` | $0.14 |
| Clipe econômico | `kwaivgi/kling-v3.0-std/image-to-video` | $0.42 |
| Máxima qualidade | `kwaivgi/kling-v3.0-4k/image-to-video` | $2.10 |
| Lipsync (voz original) | `sync/lipsync-2` | $0.05 |
| Lipsync melhor | `sync/lipsync-2-pro` | $0.08 |
| Alternativa de avatar falante | `bytedance/avatar-omni-human-1.5` | $0.16 |

Confirme antes de rodar — o catálogo é vivo:

```bash
wavespeed models --type image-to-video | grep kling-v3.0
wavespeed run kwaivgi/kling-v3.0-pro/image-to-video -h
```

## Schema do Kling 3.0 i2v

| Campo | Tipo | Nota |
|---|---|---|
| `image` | string · **obrigatório** | Frame inicial. jpg/png, ≤10MB, lado ≥300px, ratio entre 1:2.5 e 2.5:1 |
| `prompt` | string | Ou `prompt` ou `multi_prompt` — **nunca os dois** |
| `multi_prompt` | object[] 0..6 | Multi-shot nativo. Incompatível com `end_image` |
| `negative_prompt` | string | |
| `end_image` | string | Frame final. Não funciona junto com multi-shot |
| `duration` | int | 3 a 15. Default 5 |
| `cfg_scale` | number 0..1 | Quanto maior, mais preso ao prompt. Default 0.5 |
| `sound` | boolean | Áudio nativo |
| `shot_type` | string | `customize` (default) ou `intelligent` |
| `element_list` | object[] 0..3 | Elements pra travar personagem |

Para talking head, **um prompt por chamada, não multi_prompt**: cada clipe é um plano contínuo de uma pessoa falando. Multi-shot cortaria dentro do clipe, que é o oposto do que se quer.

`cfg_scale` entre **0.4 e 0.5** para talking head. Acima disso o modelo obedece tanto o texto que começa a se afastar do rosto da imagem-base.

## Versão A — clipe mudo (voz original entra depois)

```bash
IMG=$(wavespeed upload avatar-base.png --json | jq -r .url)

wavespeed run kwaivgi/kling-v3.0-pro/image-to-video \
  -i image="$IMG" \
  -i duration=11 \
  -i sound=false \
  -i cfg_scale=0.45 \
  -i prompt="The woman looks directly into the lens and speaks continuously, calm and low-energy, as if confiding to a friend. Her head tilts slightly to the right as she makes her point, then settles back. She blinks naturally twice. Small shoulder shift midway. Camera is locked off. Hands stay out of frame." \
  -i negative_prompt="hands, fingers, gesturing, changing clothes, changing hairstyle, face morphing, identity drift, subtitles, text overlay, watermark, studio lighting, camera zoom, cut to another shot" \
  --download "clipes/a-01.mp4" --json
```

**Não escreva a fala no prompt da Versão A.** O modelo geraria uma boca articulando um texto qualquer, e o lipsync depois teria que brigar contra esse movimento. Descreva só a *performance*: para onde olha, como a cabeça se move, quando pisca, o ritmo do corpo.

## Versão B — clipe com voz do Kling

```bash
wavespeed run kwaivgi/kling-v3.0-pro/image-to-video \
  -i image="$IMG" \
  -i duration=11 \
  -i sound=true \
  -i cfg_scale=0.45 \
  -i prompt="The woman looks directly into the lens, settles her shoulders, and speaks.
[Sophia, calm low confiding voice]: \"There's one detail on Instagram that gives almost everyone away. The problem is, hardly anyone knows where to look.\"
She tilts her head slightly and holds the look. Camera is locked off. Hands stay out of frame." \
  -i negative_prompt="hands, fingers, gesturing, changing clothes, changing hairstyle, face morphing, identity drift, subtitles, text overlay, watermark, studio lighting, camera zoom, cut to another shot" \
  --download "clipes/b-01.mp4" --json
```

Formato de diálogo: **ação física âncora primeiro, depois `[Nome, tom]: "fala"`.** A ação dá ao modelo o alvo de lip sync. Fala solta sem âncora sai com timing errado. Detalhe completo em `kling-3-prompt/references/dialogo.md`.

Rótulo de tom sempre em inglês; a **fala vai na língua do original**. Se o criativo é PT-BR, `[Sophia, calm low confiding voice]: "Tem um detalhe no Instagram que entrega quase todo mundo."`

## Encadeamento entre clipes

Do clipe 2 em diante, o `start_image` é o último frame do clipe anterior:

```bash
ffmpeg -y -sseof -0.1 -i clipes/a-01.mp4 -vframes 1 -q:v 2 clipes/a-01-last.jpg
NEXT=$(wavespeed upload clipes/a-01-last.jpg --json | jq -r .url)
# usa $NEXT como -i image= na chamada do clipe 2
```

Sem isso, cada clipe volta à pose da imagem-base e a emenda vira um salto visível. Com isso, a costura passa como um corte de UGC normal.

## Lipsync — uma vez, no vídeo inteiro

```bash
V=$(wavespeed upload versao-A-mudo.mp4 --json | jq -r .url)
A=$(wavespeed upload audio-original.m4a --json | jq -r .url)

wavespeed run sync/lipsync-2 \
  -i video="$V" -i audio="$A" -i sync_mode="cut_off" \
  --download "versao-A-voz-original.mp4" --json
```

`sync_mode` resolve descasamento de duração:

| Modo | Comportamento | Quando usar |
|---|---|---|
| `cut_off` | Corta no fim do mais curto | **Default.** Vídeo ligeiramente mais longo que o áudio |
| `silence` | Completa com silêncio | Vídeo mais longo e você quer o frame final segurando |
| `loop` / `bounce` | Repete o vídeo | Vídeo curto demais — evite, denuncia |
| `remap` | Estica/comprime | Último recurso; altera o ritmo |

Gere o vídeo mudo **1 a 2 segundos mais longo** que o áudio e use `cut_off`. Sobra é barata; falta obriga a `loop`, que aparece.

## Preflight de custo

O CLI aceita rodar sem submeter pra ver preço. Some antes de disparar uma rodada de várias variações, e apresente o total ao usuário. Uma rodada de 3 clipes × 2 versões + lipsync ≈ $3.4; cinco variações de avatar ≈ $17.

## Erros comuns

| Sintoma | Causa | Correção |
|---|---|---|
| Rosto muda no meio do clipe | `cfg_scale` alto demais | Baixe pra 0.4 |
| Emenda com salto | Sem encadeamento de start_image | Extraia o último frame |
| Boca fora de sincronia na Versão A | Fala escrita no prompt do clipe mudo | Tire o diálogo, descreva só performance |
| Mão derretendo | Mão no quadro | Regere a imagem-base cortando no peito |
| Vídeo trava no fim | Áudio mais longo que o vídeo | Gere clipes com folga, `sync_mode=cut_off` |
| `prompt` e `multi_prompt` juntos | API rejeita | Só um dos dois |
