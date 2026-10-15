---
name: trocar-avatar
description: "Recria um criativo de vídeo campeão trocando SÓ o avatar — mantém roteiro, ritmo e enquadramento, descarta split-screen/overlays/b-roll e entrega um talking head limpo. Gera a imagem-base do rosto novo, anima no Kling 3.0 via WaveSpeed e devolve duas versões: uma com a voz ORIGINAL sincronizada (lipsync) e outra com voz gerada pelo Kling. Use SEMPRE que o usuário quiser trocar o avatar/rosto/creator de um criativo, clonar um anúncio que escalou com outra pessoa, recriar um UGC com avatar diferente, testar o mesmo roteiro com outro rosto, ou disser 'troca o avatar', 'refaz esse criativo com outra pessoa', 'mesmo roteiro outro creator', 'variação de avatar'. Roda em cima de um vídeo de referência local ou URL."
---

# Trocar avatar de criativo

Você está clonando um criativo que **já provou converter**. O roteiro, o ritmo e a estrutura são o ativo testado — eles não se tocam. A única variável que muda é o rosto.

Isso importa porque define o padrão de qualidade: não é "fazer um vídeo bom", é **fazer o mesmo vídeo com outra pessoa**. Se o novo avatar fala mais rápido, gesticula diferente ou o enquadramento muda, você perdeu o controle experimental e não vai saber por que o criativo subiu ou caiu.

Duas entregas por rodada, sempre:

- **Versão A — voz original.** O áudio do campeão é extraído e sincronizado no rosto novo. Só o rosto mudou. É o A/B limpo.
- **Versão B — voz do Kling.** O modelo gera a fala junto com o vídeo. Voz, sotaque e ritmo mudam também. É o teste de "a voz importava?".

## Pré-requisitos

```bash
command -v wavespeed && command -v ffmpeg && command -v jq
```

Se faltar `wavespeed`, a skill `wavespeed` tem o setup. Se faltar `ffmpeg`/`ffprobe`, `python3 ~/.claude/skills/watch/scripts/setup.py`.

## Passo 1 — Ler o criativo de referência

Se o usuário deu um vídeo (arquivo local ou URL), rode a skill `watch` nele. Você precisa de quatro coisas:

1. **O roteiro literal, com timestamps.** É o ativo. Transcreva exatamente — não melhore a copy, não corrija gramática, não reescreva. Se a fala original tem uma hesitação ou uma construção estranha que funcionou, ela fica.
2. **A duração total e o aspect ratio.**
3. **O enquadramento do talking head:** plano (medium/close), altura da câmera, cenário, figurino, se as mãos aparecem.
4. **O que descartar.** Split screen, screen recording, overlays, dramatização, selo de contador, legenda queimada — nada disso é recriado. O pedido é talking head limpo. Anote o que existia para poder devolver ao usuário na entrega ("o original tinha X nos primeiros 11s; não foi replicado, entra na edição").

Se o usuário já entregou só o roteiro, pule para o Passo 2 e pergunte a duração-alvo e o ratio.

**Extraia o áudio original agora** — a Versão A depende dele:

```bash
ffmpeg -y -i "<referencia.mp4>" -vn -ac 1 -ar 44100 -c:a aac "<out>/audio-original.m4a"
```

## Passo 2 — Nota de casting

O avatar é definido por descrição a cada rodada. Pergunte o que faltar (idade, gênero, etnia, cenário) e escreva uma **nota de casting** curta — uma âncora de figurino, uma assinatura facial, um cenário, uma linha de base emocional.

A nota é lei: ela reaparece igual na imagem-base e em todo prompt de clipe. Personagem que muda entre clipes vira colagem.

Detalhe completo e o template de prompt anti-cara-de-IA em `references/casting.md`. O resumo do que não pode faltar:

- **Mãos fora do quadro.** É o maior denunciador de vídeo com IA — dedos derretem em movimento. Enquadre em peito/ombros ou apoie as mãos abaixo da borda. Se o original tinha gesto, aceite a perda: um plano sem mãos vence um plano com mãos deformadas.
- **Luz disponível, não luz de estúdio.** Mistura de temperaturas, sombra assimétrica.
- **Textura de pele visível.** Poro, oleosidade na testa, linha de expressão. Pele limpa demais é o segundo denunciador.
- **Grão real** (ISO 500-900) e lente de celular (26mm), não câmera de cinema.

## Passo 3 — Imagem-base

Gere a imagem do avatar no ratio do original (normalmente 9:16, 1080×1920). Essa imagem é o `start_image` do primeiro clipe e a âncora de identidade de tudo.

Ordem de tentativa: **GPT Image 2 via GERAEW** (use a skill `gpt-image-2-prompt` pra montar o prompt), e se falhar, **Seedream via WaveSpeed** — é a regra de fallback já estabelecida na operação.

Mostre a imagem ao usuário e **espere aprovação antes de gerar vídeo**. Um rosto errado aprovado aqui custa a rodada inteira de créditos lá na frente.

## Passo 4 — Fatiar o roteiro

O Kling gera de 3 a 15 segundos por chamada. Fatiar mal é o que produz fala acelerada ou clipe que termina no meio de uma frase.

A regra que segura o ritmo natural é **55-60 sílabas por clipe** (≈10s de fala). Nunca corte no meio de uma frase — prefira um clipe de 8s a uma frase partida.

Use o script:

```bash
python3 ~/.claude/skills/trocar-avatar/scripts/chunk_roteiro.py roteiro.txt --lang pt --json
```

Ele conta sílabas, quebra em fronteira de frase e devolve `{n, texto, silabas, duracao_kling}` por clipe. Confira o resultado contra os timestamps reais da transcrição — se o script diz 10s e o original levou 14s pra falar aquilo, o original falava devagar: use a duração real, não a calculada. **O ritmo do campeão manda.**

## Passo 5 — Gerar os clipes

Chamadas exatas, IDs de modelo e custos em `references/kling-wavespeed.md`. A lógica:

**Encadeamento de identidade.** O clipe 1 sai da imagem-base. Do clipe 2 em diante, o `start_image` é o **último frame do clipe anterior** (extraído com ffmpeg). Isso mantém a continuidade de rosto, luz e pose — sem isso, cada clipe volta à pose inicial e a emenda vira um salto visível.

**Versão A (voz original) — `sound=false`.** O prompt descreve só a performance física: para onde ela olha, como a cabeça se move, quando pisca, o ritmo do corpo. **Não escreva a fala no prompt** — o áudio real entra depois no lipsync, e diálogo no prompt faria o modelo gerar uma boca contando outra história.

**Versão B (voz do Kling) — `sound=true`.** Aí sim o prompt carrega a fala, no formato de diálogo do Kling: ação física âncora primeiro, depois `[Nome, tom]: "fala"`. Use a skill `kling-3-prompt` (`references/dialogo.md`) pra montar. A fala vai literal, na língua do original.

Em ambas: `negative_prompt` cobrindo deformação de mão, dedo extra, drift de rosto e troca de roupa. Está pronto no arquivo de referência.

## Passo 6 — Montar

```bash
bash ~/.claude/skills/trocar-avatar/scripts/montar.sh <dir-da-rodada>
```

O script costura os clipes, normaliza fps e resolução, e produz `versao-B-voz-kling.mp4` e `versao-A-mudo.mp4`.

**O lipsync roda uma vez só, no vídeo inteiro.** Costure primeiro os clipes mudos, depois sincronize o arquivo completo contra o áudio original completo. Sincronizar clipe a clipe acumula deriva nas emendas e custa 3× mais:

```bash
V=$(wavespeed upload <dir>/versao-A-mudo.mp4 --json | jq -r .url)
A=$(wavespeed upload <dir>/audio-original.m4a --json | jq -r .url)
wavespeed run sync/lipsync-2 -i video="$V" -i audio="$A" -i sync_mode="cut_off" \
  --download "<dir>/versao-A-voz-original.mp4" --json
```

## Passo 7 — Entregar

Pasta por rodada, nomeada `<projeto>/criativos/<slug-do-original>-avatar-<slug-do-avatar>-<AAAA-MM-DD>/`:

```
versao-A-voz-original.mp4     ← só o rosto mudou
versao-B-voz-kling.mp4        ← rosto + voz mudaram
avatar-base.png               ← a imagem aprovada
audio-original.m4a
clipes/                       ← os brutos, pra regerar um só
manifest.json                 ← nota de casting, prompts, custos, IDs de job
```

O `manifest.json` é o que permite regerar **um clipe fraco** sem refazer a rodada. Grave nele os prompts literais e os IDs.

Na resposta ao usuário, diga sempre:
- **O que foi descartado do original** (o split screen, os overlays) e que isso entra na edição.
- **Custo real da rodada**, somado dos jobs.
- **Qual clipe está mais fraco**, na sua avaliação — assista antes de entregar.

## Regras que carregam a qualidade

1. **O roteiro é intocável.** Você está testando uma variável. Melhorar a copy no meio do caminho contamina o teste e o usuário perde a leitura do resultado.
2. **Aprovação da imagem-base antes de queimar crédito de vídeo.** Imagem é centavos, vídeo é dólar.
3. **Encadeie o start_image.** Último frame do anterior, sempre.
4. **Mãos fora do quadro** salvo se o usuário insistir — e aí avise que é o ponto de falha mais provável.
5. **Ritmo do original manda** sobre o cálculo de sílabas quando os dois discordam.
6. **Assista antes de entregar.** Você tem a skill `watch` — rode nas duas versões e diga o que está fraco. Entregar sem olhar é passar o problema pro usuário.

## Custo por rodada

Um criativo de ~33s vira 3 clipes de ~11s. Com Kling 3.0 Pro ($0.56/clipe):

| Item | Versão A | Versão B |
|---|---|---|
| 3 clipes Kling | $1.68 | $1.68 |
| lipsync (1×) | $0.05 | — |
| **Subtotal** | **$1.73** | **$1.68** |

Rodada completa das duas ≈ **$3.4** + a imagem-base. Preflight com `-i` … `--json` e some os custos reais; se o usuário pediu várias variações de avatar, apresente o total **antes** de disparar.

Precisando cortar custo num teste exploratório: `kwaivgi/kling-v3-turbo-pro/image-to-video` sai por $0.14 (1080p) — qualidade menor, mas serve pra validar enquadramento e ritmo antes de gastar no Pro.

## Arquivos de referência

- `references/casting.md` — nota de casting e template de prompt da imagem-base com as regras anti-cara-de-IA.
- `references/kling-wavespeed.md` — IDs de modelo, schema completo, chamadas prontas, negative prompt, tabela de custos.
- `references/montagem.md` — receitas de ffmpeg (áudio, último frame, costura, normalização) e o protocolo de lipsync.
- Skills irmãs: `kling-3-prompt` (linguagem de câmera e formato de diálogo), `watch` (ler o original e revisar a entrega), `gpt-image-2-prompt` (prompt da imagem-base).
