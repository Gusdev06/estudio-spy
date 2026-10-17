# Guia: máquina de conteúdo orgânico com influencer de IA (modelo @itsteawithbia)

Versão de 17/10/2026. Escrito a partir do que foi construído e medido de verdade entre 13 e 17/10/2026 para o perfil @itsteawithbia (nicho: relacionamento/traição, vendendo um app). Serve para qualquer nicho.

---

## PARTE 0 — Para você, que vai usar (leia só isto)

Você não precisa saber programar. Quem vai construir é o seu Claude.

1. Instale o **Claude Code** (claude.com/claude-code) e abra num computador (Mac ou Windows).
2. Crie uma pasta vazia, por exemplo `minha-maquina`, e coloque este arquivo dentro com o nome `GUIA.md`.
3. Abra o Claude Code nessa pasta e mande:

> Leia o GUIA.md inteiro. Quero montar essa máquina para o nicho **[seu nicho]**, vendendo **[seu produto/link]**. Me guie uma etapa por vez, faça você tudo que der e me diga exatamente o que eu preciso clicar quando for comigo.

4. Ele vai te pedir para criar algumas contas (lista na Parte 3). Tudo que custa dinheiro, ele deve te perguntar antes.

O que a máquina faz, em uma frase: **acha os vídeos que mais viralizam no seu nicho, recria cada cena com uma influencer de IA sua (sempre o mesmo rosto), coloca uma frase nova na tela, e posta no Instagram sozinha numa fila, medindo o que funciona.**

---

## PARTE 1 — Instruções para o Claude que vai construir

Você (Claude) está ajudando uma pessoa leiga a reproduzir este sistema num nicho novo. Regras de trabalho:

- **Uma etapa por vez.** Termine, mostre o resultado, peça o ok, siga. Não despeje o guia inteiro.
- **Pergunte o nicho, o produto, o link de venda, a língua do público e o país** antes de qualquer coisa. Tudo abaixo usa o caso da Bia como exemplo; troque pelo nicho dele.
- **Nada que custe dinheiro sem estimar o custo e perguntar.** Geração de imagem e vídeo é cobrada por unidade. Mostre "isso vai custar ~US$ X, posso?".
- **Teste com 1 antes de fazer 10.** Gere uma cena, confira, só depois o lote.
- **Nada vai pro ar sem o ok da pessoa.** O script de publicação tem modo "só conferir" por padrão.
- **Nunca guarde senha/token dentro do código.** Use um arquivo `.env` e coloque `.env` no `.gitignore`.
- **Confira cada vídeo final antes de dizer que está pronto** (Parte 9). Vídeo gerado por IA erra de jeitos que só aparecem olhando os frames.
- Faça você o que for terminal/código. Para a pessoa, só o que exige clique dela (criar conta, aprovar app, logar).
- Fale simples. Ela é leiga.

---

## PARTE 2 — O sistema inteiro, num desenho

```
 [1] PESQUISA            [2] PERSONA              [3] RÉPLICA DA CENA
 contas do nicho  ──►   ficha da influencer  ──► frame do viral → imagem com a
 que viralizam          (8 fotos, 1 texto)       persona → vídeo com a persona
 top 40 vídeos                                   (mesmo movimento, outra pessoa)
        │                                                 │
        ▼                                                 ▼
 padrão do viral ───────────────────────────► [4] TEXTO NA TELA + LEGENDA
 (duração, texto,                                 frase nova + áudio original
  cena, legenda)                                          │
                                                          ▼
                       [5] VARIAÇÕES GRÁTIS ◄──── vídeo base pronto
                       mesma cena, frase nova            │
                                                          ▼
                                                 [6] CONFERÊNCIA (QA)
                                                          │
                                                          ▼
                       [8] MÉTRICAS ◄──────────── [7] FILA + PUBLICAÇÃO
                       o que passou vira               (API do Instagram)
                       mais variação
```

O segredo do custo: o vídeo caro (persona na cena) é feito **uma vez**. Depois cada vídeo base vira 5, 10, 20 posts só trocando a frase na tela, de graça.

---

## PARTE 3 — Contas e ferramentas (a pessoa cria, o Claude instala)

| O quê | Para quê | Custo |
|---|---|---|
| Claude Code | constrói e opera tudo | assinatura Claude |
| **WaveSpeed** (wavespeed.ai) + CLI `wavespeed` | gera imagem e vídeo por API (Nano Banana 2.1, Seedance) | pré-pago, por geração |
| **Apify** (apify.com) | baixa a lista de reels/TikToks de um perfil com views | tem plano grátis com crédito mensal |
| Instagram **profissional** (Criador) | onde a persona posta | grátis |
| App na **Meta for Developers** com "Instagram Login" | gera o token que deixa o script postar | grátis |
| TikTok (opcional) | segunda rede; postar à mão | grátis |
| No computador: `python3`, `ffmpeg`, `pip install pillow opencv-python numpy`, `yt-dlp` | montar os vídeos | grátis |

Token do Instagram: o Claude guia a pessoa no painel da Meta (criar app → produto "Instagram" → "API setup with Instagram login" → adicionar a conta como testadora → gerar token com `instagram_business_basic` + `instagram_business_content_publish`). Vai no `.env`:

```
IG_ACCESS_TOKEN=...
IG_USERNAME=nomedaconta
WAVESPEED_API_KEY=...
APIFY_TOKEN=...
```

---

## PARTE 4 — Etapa 1: Pesquisa (achar o que já viraliza)

Objetivo: não inventar formato. Copiar a **estrutura** do que já provou que funciona no nicho.

1. A pessoa aponta 2 a 5 perfis do nicho que crescem com vídeo curto **sem rosto famoso** (persona, "faceless", rotina banal + frase). Se não souber, o Claude procura com ela.
2. Coletar via Apify os últimos ~100 vídeos de cada perfil com views, likes, shares, duração e legenda. Atores que usamos: `apify/instagram-profile-scraper`, `apify/instagram-reel-scraper` (para TikTok, um scraper de perfil do TikTok equivalente).
3. Ordenar por views. Baixar os **40 mais vistos** (`yt-dlp <url>`).
4. Montar uma **folha de contato**: 1 frame de cada vídeo numa grade (ffmpeg + Pillow). Olhar a folha e preencher a tabela:

| Campo | O que anotar |
|---|---|
| Duração | quantos segundos (na Bia: 5–6 s nos virais) |
| Texto na tela | tamanho (palavras), tom, posição, cor, fonte |
| Cena | o que a pessoa está fazendo, onde, olha ou não pra câmera |
| Expressão | séria, rindo, neutra |
| Áudio | original, música, fala |
| Legenda do post | como cita o produto, CTA, hashtags |
| Repetição | a mesma cena aparece em vários virais? |

5. Escrever `padrao-virais.md` com "o que TODOS fazem". Esse arquivo manda em tudo que vem depois.

**O que achamos no nosso nicho (exemplo, 16/10/2026, 40 vídeos de 2,9M a 15,9M views):** 5 segundos; texto fixo, branco, no meio da tela, 20 a 60 palavras (longo demais pra ler em 5 s, então a pessoa revê = replay); desabafo triste em 1ª pessoa; mulher comum cortando legume na cozinha, sem olhar pra câmera; **a marca nunca aparece no vídeo, só na legenda**, contada como história ("i found out on [app]"). No seu nicho o padrão vai ser outro: o Claude tem que medir, não supor.

---

## PARTE 5 — Etapa 2: A persona (a influencer de IA)

Uma persona só, sempre o mesmo rosto. Consistência é o que faz parecer uma pessoa real.

1. **Texto fixo de identidade** (`identidade.txt`), colado igual em todo prompt, nunca reescrito. Exemplo real:

```
Bia, 27 years old woman. Light olive skin, brown eyes, thick natural dark eyebrows,
small beauty mark on her right cheek (appears on the left side of the image when she
faces the camera), a few faint freckles across the nose, full lips, oval face with soft
jawline, dark brown hair (mid-back length, slight natural wave). Slim natural body.
Real skin texture: visible pores, slight shine on forehead and nose, faint redness
around the nostrils, tiny under-eye shadows. Not retouched.
```

Um detalhe marcante (pinta, sarda, cicatriz) ajuda a conferir se o rosto se manteve.

2. **Ficha com 8 imagens** (pasta `persona/base/`), fundo neutro, mãos vazias: `01-frente` (âncora, vai em TODA geração), `02/03` três quartos, `04` perfil, `05` close do rosto (pele e pinta), `06` corpo inteiro, `07` sorriso, `08` expressão séria. Custo nosso: ~US$ 1,8 as 8.
3. **Fotos do perfil** (foto de perfil + 3 posts fixos) com cara de foto de celular de amiga, não de estúdio. Estrutura de prompt que funcionou:

```
Asset type: candid lifestyle photo for an Instagram post
Primary request: photorealistic phone photo of the woman in the reference images, 100% faithful
  to her face, beauty mark and hair. Use the references ONLY for identity, never for pose or background.
Scene/backdrop: <lugar real com bagunça leve, objetos, gente desfocada>
Subject: <roupa com marca de uso, fios soltos, AÇÃO acontecendo>
Style/medium: shot on an iPhone, true-to-life phone processing, subtle grain
Composition/framing: <quem tirou: amiga do outro lado da mesa / selfie / espelho>; off-center,
  slightly tilted, objects cut by the frame edge; not looking at the lens
Lighting/mood: <fonte nomeada: janela à esquerda, flash do celular, sol baixo>
Textures: natural pores, uneven skin tone, flyaway hairs, fabric creases
Constraints: no text, no logo, no watermark. She is alone.
Avoid: beauty filter, plastic skin, symmetrical centered headshot, studio lighting, cinematic grading
```

- Nunca usar: beautiful, stunning, 8K, masterpiece, cinematic, ultra realistic (puxam cara de IA).
- Para a cor parecer real: mandar uma foto real de referência **só de cor e luz** e dizer no prompt para não copiar rosto, roupa nem joias.
- Modelo: `google/nano-banana-2.1/edit` em 2k, imagens `[01-frente, 05-close, ref-de-cor]`. ~US$ 0,04–0,08 por imagem.

**Regras da persona (aprendidas errando):**
- Sempre voltar à âncora (`01-frente` + `05-close`). Nunca usar uma saída anterior como referência: o rosto vai derivando.
- Variar uma coisa por geração (roupa OU cena OU ação).
- Escrever "she is alone": a IA às vezes inventa uma segunda pessoa no fundo.

---

## PARTE 6 — Etapa 3: Réplica da cena (o vídeo caro)

Pega um viral do padrão e recria a mesma cena, mesmo movimento, com a persona. Pasta por vídeo:

```
criativos/<nome-do-original>/
  original/   original.mp4, url.txt
  base/       frame.png, persona-na-cena.png
  clipes/     persona.mp4
  legendas/   texto.txt, texto.png
  final/      final.mp4, legenda.txt, conferencia.jpg
  logs/       pedidos e respostas da API (ids, custo)
```

Passo a passo:

1. **Baixar o original** e converter para H.264 (`ffmpeg -i original.mp4 -c:v libx264 -c:a aac original-h264.mp4`).
2. **Apagar o texto queimado do original** antes de tudo (senão a IA às vezes mantém o texto). Técnica: o texto fica parado o vídeo todo, então os pixels que ficam claros (ou escuros) em todos os frames dentro da caixa do texto viram uma máscara; aplica inpaint em cada frame (OpenCV `cv2.inpaint` TELEA). Script `apagar-texto.py <pasta> x0 y0 x1 y1 claro|escuro limiar`.
3. **Tirar um frame** limpo (~0,5 s) → `frame.png`.
4. **Persona na cena** (imagem): `google/nano-banana-2.1/edit` 2k com `images=[frame, 01-frente, 05-close]`. Prompt modelo:

```
Edit image 1. Replace the woman with the woman from images 2 and 3 (same identity, face and
beauty mark). She is alone. <TEXTO DE IDENTIDADE INTEIRO>
<roupa e cabelo novos, descritos>
Keep everything else in image 1 exactly the same: her pose, head angle, gaze, hand and arm
positions, <objetos da cena>, the lighting, the colors, the framing and the camera angle.
Remove ALL on-screen text: no letters, words or captions anywhere. Photorealistic front
phone camera, not retouched.
```

5. **Vídeo com a persona**: `bytedance/seedance-2.5/video-edit` (ou 2.0), 720p, `generate_audio=false`, `video=<original sem texto>`, `reference_images=[persona-na-cena, 01-frente, 05-close]`. Prompt modelo:

```
Replace the woman in the video with the woman from the reference images for the entire video:
<rosto, pele, cabelo, roupa exatamente como na primeira referência>. She must keep this outfit
in every frame. She is alone. Keep every movement, gesture, hand position, timing and camera
framing exactly as in the original video: <descreve a ação>. Keep <cenário> exactly as in the
original. No text anywhere in any frame.
```

Custo: ~US$ 2,4 por clipe de 5 s (estimado pela tabela). É o item caro do sistema.

6. **A referência tem que estar na cena do próprio vídeo.** Mandar uma foto da persona de outra cena não funciona: a IA ignora e a pessoa original continua no vídeo (perdemos US$ 2,43 assim).

---

## PARTE 7 — Etapa 4: Texto na tela + legenda do post

**Texto na tela** (`texto.txt` → `texto.png` transparente 1080×1920):
- Fonte limpa (Helvetica Neue Medium ou parecida), branca ou creme, centralizada, quebra automática em ~820 px, sombra leve para ler em fundo claro.
- Fala do **assunto do nicho**, não do produto. Medimos: frase que citava o produto teve mediana de 11 mil views; frase sobre o tema (homem, traição) teve 37 mil.
- Siga o padrão medido na Parte 4 (tamanho, tom). No nosso caso: desabafo longo em 1ª pessoa.

**Montagem final** (vídeo da persona + texto + áudio original, mesma duração do original):

```bash
ffmpeg -y -i clipes/persona.mp4 -i original/original-h264.mp4 -i legendas/texto.png \
 -filter_complex "[0:v]trim=0:<DURACAO>,setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1,format=yuv420p[v0];[v0][2]overlay[v]" \
 -map "[v]" -map 1:a -c:v libx264 -crf 17 -profile:v high -c:a aac -b:a 128k -ar 44100 \
 -shortest -movflags +faststart final/final.mp4
```

**Legenda do post** (`legenda.txt`): história curta em 1ª pessoa que cita o produto pelo nome + CTA + 5 hashtags fixas do nicho. Exemplo:

```
Bald men and red flags have one thing in common: you can see both from a mile away 😭
Wanna know what he's really up to? Link in bio 👀
#microcheating #redflags #cheatingex #breakup #breakuptok
```

---

## PARTE 8 — Etapa 5: Variações grátis (onde o volume sai barato)

Cada vídeo base pronto (`bases.json`: caminho do clipe, do áudio e altura do texto) vira vários posts trocando só a frase. Custo zero.

```json
{ "cebola": { "clip": "criativos/.../clipes/persona.mp4",
              "audio": "criativos/.../original/audio.m4a", "cy": 970 } }
```

Lote = lista de `[base, frase na tela, legenda]`:

```json
[["cebola", "they made sugar-free candy, decaf coffee and fat-free cheese but never a man without a \"she's just a friend\"",
  "If she's \"just a friend\" you can check that too. Link in bio 👀"]]
```

Script `variar.sh <base> "<frase>" <saida.mp4>`: desenha a frase num PNG (Pillow) e sobrepõe ao clipe com o áudio da base (ffmpeg, igual à montagem acima). O Claude escreve as frases em lote seguindo o padrão; **a pessoa aprova as frases antes de renderizar.**

Regra medida: base ruim trava qualquer frase. Duas das nossas bases (maquiagem, brócolis) ficaram sempre em ~150 views, não importa o texto. Base que passa num teste ganha mais variações; base que não passa sai.

---

## PARTE 9 — Etapa 6: Conferência antes de postar (obrigatória)

O Claude roda isto em todo vídeo final, sem exceção:

1. **Decodificar o arquivo inteiro** (`ffmpeg -v error -i final.mp4 -f null -`). Download de API às vezes vem cortado sem dar erro.
2. **Folha de conferência**: 12 frames espalhados numa grade (`conferencia.jpg`) e olhar:
   - é o mesmo rosto da âncora o vídeo todo (a IA às vezes troca de pessoa no meio)?
   - tem segunda pessoa, mão estranha, moldura, texto antigo sobrando?
   - a roupa se manteve?
   - o texto novo está legível e não piscando?
3. **Spec do Instagram**: H.264, 23–60 fps, largura ≤ 1920, AAC, 3 s a 15 min, ≤ 300 MB, `+faststart`. O script de publicação já recusa vídeo fora disso.

---

## PARTE 10 — Etapa 7: Fila e publicação automática

**Fila** (`fila-posts.json`): um item por post.

```json
[{ "video": "variacoes/videos/l1-01.mp4",
   "legenda": "variacoes/legendas/l1-01.txt",
   "quando_utc": "2026-10-18T11:00:00Z",
   "slot": "07h NY 18/10",
   "trial": "SS_PERFORMANCE",
   "status": "pendente" }]
```

**`publicar-reel.py`** (Python puro, sem biblioteca extra) faz, pela API oficial `https://graph.instagram.com/v25.0`:
1. Confere o vídeo com `ffprobe` (spec acima) e confere que o token é da conta certa (`IG_USERNAME`). **Sem a flag `--publicar`, para aqui** e nada vai pro ar.
2. Sobe o vídeo para uma URL pública (usamos `wavespeed upload <arquivo>`; a Meta precisa baixar de um link).
3. `POST /{ig_id}/media` com `media_type=REELS`, `video_url`, `caption`, `share_to_feed=true`, `thumb_offset` e, se quiser, `trial_params={"graduation_strategy": "..."}`.
4. Repete `GET /{container}?fields=status_code` até `FINISHED`.
5. `POST /{ig_id}/media_publish` com `creation_id` e devolve o link do post.
- Repetir GET em erro de rede é seguro; **nunca repetir o POST de publicar** (duplica o post).
- Limite da API: ~100 posts por 24 h. Bem acima do que se deve postar.

**`rodada.py`**: pega todos os pendentes com o horário mais antigo, publica um por um, grava `status`, `permalink` ou `erro` na fila e **para no primeiro erro**. A pessoa manda "posta a rodada" e o Claude roda `python3 rodada.py --publicar`.

**Trial Reels** (vai só para quem não segue):
- `MANUAL`: você tem que "graduar" no app depois. **Não use como padrão**: nossos 44 primeiros reels ficaram presos em 1,5–3,3 mil views e o perfil parecia vazio (3 posts), porque nunca foram graduados.
- `SS_PERFORMANCE`: o Instagram gradua sozinho se for bem. Use este.
- Ou post normal (sem trial) para os que você quer no grid.

TikTok: postar à mão pelo app com o mesmo vídeo e legenda, marcando o rótulo "AI-generated".

---

## PARTE 11 — Etapa 8: Métricas e decisão

Puxar pela mesma API, todo dia, para um `metricas-AAAA-MM-DD.json`:
- por post: `GET /{media_id}/insights?metric=views,reach,shares,saved,likes,comments`
- da conta: `profile_views`, `follows_and_unfollows`, `website_clicks`.

Como decidir:
- Medir por **mediana e por quantos passam de um teto** (ex.: > 100 mil), não post a post. É um jogo de loteria: o volume compra os vídeos que estouram.
- O que passou: mais variações grátis da mesma base, "part 2", série.
- O que não passou em 2–3 frases diferentes: a base sai.
- Olhar o funil inteiro, não só view: views → visitas ao perfil → seguidores → cliques no link → vendas.

---

## PARTE 12 — Custos reais (nosso caso, preços de tabela, out/2026)

| Item | Custo |
|---|---|
| Ficha da persona (8 imagens) | ~US$ 1,8, uma vez |
| Fotos do perfil | ~US$ 0,40 |
| Persona na cena (imagem) | ~US$ 0,04–0,08 |
| Vídeo com a persona (Seedance, 5 s) | ~US$ 2,4 |
| **Vídeo base completo** | **~US$ 2,5** |
| Cada variação de frase | US$ 0 |
| Publicação e métricas | US$ 0 |

Nosso teto planejado: US$ 300/mês ≈ 3 vídeos base novos por dia + 2–3 variações grátis por dia.

---

## PARTE 13 — O que deu errado com a gente (para não repetir)

Primeiros 4 dias: **44 reels, 56 mil views, 29 visitas ao perfil, 4 seguidores, 0 clique no link.** View não era o problema. As causas, por peso:

1. **Todos em Trial MANUAL e nunca graduados** → teto baixo e perfil com 3 posts. Quem visitava não via motivo para seguir. → Use `SS_PERFORMANCE` e tenha pelo menos 9–12 posts no grid antes de escalar.
2. **Vídeo avulso não dá motivo para seguir.** → Faça **série numerada** ("day 4 of …", "part 2 on my page"). Quem quer o final, segue.
3. **Volume demais numa conta só** (15/dia, mesma base repetida). → 3–5 por dia, só bases que passaram.
4. **Link com degrau** (Linktree antes do produto). → Link direto, domínio próprio, nome do produto na legenda para quem buscar no Google.
5. **Frase engraçada e curta quando o padrão do nicho era desabafo longo.** → Seguir o que a Parte 4 mediu, não o gosto da gente.
6. Antes de mandar tráfego: **fazer uma compra real de ponta a ponta** no produto.

---

## PARTE 14 — Regras e riscos (não pule)

- **Rótulo de IA:** TikTok e Instagram exigem marcar conteúdo realista gerado por IA. Sem o rótulo, o vídeo pode cair ou a conta tomar strike.
- **Divulgação:** se a persona recomenda um produto que é seu, deixe isso visível ("my app", "#ad"). Esconder é publicidade enganosa na maioria dos países.
- **Conteúdo não original:** as redes cortam alcance de vídeo copiado. Recriar a cena com sua persona e **texto próprio** é bem mais seguro que repostar ou copiar o texto do viral palavra por palavra. Com o tempo, troque réplicas por cenas próprias.
- **Nunca repostar o vídeo de outra pessoa.** É risco de direito autoral e de derrubada da conta.
- **Sem depoimento, número ou prova social inventados** na legenda ou na página de venda.
- **Uma conta só = um ponto de falha.** Se tomar shadowban, tudo para. Considere uma conta reserva depois que o formato provar resultado.

---

## PARTE 15 — Estrutura de pastas sugerida

```
minha-maquina/
  GUIA.md                  este arquivo
  .env                     tokens (nunca no git)
  pesquisa/                coleta Apify, top 40, folha de contato, padrao-virais.md
  persona/                 identidade.txt, base/ (8 imagens), perfil/
  criativos/<video>/       uma pasta por réplica (Parte 6)
  variacoes/               bases.json, lote-N.json, variar.sh, videos/, legendas/
  scripts/                 apagar-texto.py, texto.py, publicar-reel.py, rodada.py, metricas.py
  fila-posts.json
  metricas/                um JSON por dia
```

---

## PARTE 16 — Primeira semana

| Dia | Entrega |
|---|---|
| 1 | Contas criadas, ferramentas instaladas, token do Instagram funcionando (publicar-reel.py em modo conferir passa) |
| 2 | Pesquisa: top 40 do nicho baixado e `padrao-virais.md` escrito |
| 3 | Persona: identidade + ficha de 8 + foto de perfil + bio |
| 4 | 3 réplicas (vídeos base), conferidas. Custo ~US$ 7,5 |
| 5 | 15 variações grátis aprovadas, fila montada, 9 primeiros posts no ar |
| 6–7 | 3–5 posts/dia em `SS_PERFORMANCE`, métricas diárias |
| 7 | Decisão com dado: alguma base passou? Taxa de seguidor por view? Algum clique? Dobra no que passou, corta o resto |
