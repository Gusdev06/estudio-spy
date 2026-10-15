# Lições aprendidas (geradas das memórias da operação; "Gusta" é o dono da operação que produziu os lotes)

## Atalhos de preço e modelo (out/2026)
- Rosto novo: `openai/gpt-image-2/edit` medium 1k ≈ US$ 0,067; high ≈ US$ 0,22. Fotos de pessoa realista em cena: `google/nano-banana-2.1/edit` 2k saiu melhor que gpt-image em 14/10.
- Lipsync de foto + áudio: `pruna-ai/p-video/avatar` 720p, US$ 0,025/s (mínimo ~2 s de áudio; devolve 24 fps com cauda, converter com fps=30).
- Troca pura de pessoa num vídeo (mesmo cenário/movimento): `bytedance/seedance-2.0/video-edit` 720p ≈ US$ 2,43 por 8 s, com a imagem da pessoa nova já na cena como referência.
- Ritmo: silêncio > ~0,4 s dentro da fala é cortado (vídeo e áudio juntos); respiro entre cenas ≤ 0,3 s.
- Entregue na resolução do original; se o original for < 1080p, pergunte se o cliente quer upscale.

## "Antes de qualquer chamada paga de geração com mídia longa, estimar por duração e mostrar o número ao Gusta ANTES de disparar"

Antes de qualquer chamada paga de geração de mídia (WaveSpeed etc.) com **mídia longa**,
estimar o custo por **duração × preço unitário** e dizer o número ao Gusta **antes** de disparar.
Nada pago sem perguntar. O que é ffmpeg local pode seguir à vontade.

**Why:** em 2026-09-01, no lote spy, o `base_price` de US$0,08 do `sync/lipsync-2-pro` foi lido
como preço fechado por chamada — mas é **por unidade**. Sincronizar 31,3s de head + 1,2s de cauda
custou **US$2,72**, contra um teto de US$2. O Gusta assumiu metade do erro (o teto dele saiu da
mesma leitura), mas o pedido ficou: estimar por duração antes, sempre.

**How to apply:** o preço base da listagem de modelos não é o custo da chamada. `wavespeed price`
sem inputs reais devolve US$0 e não serve. A estimativa vem de duração × unitário, ou de uma
chamada curta de teste primeiro. Conferir `wavespeed balance` antes e depois pra saber o gasto
real, e reportar esse número — não o base_price.

E não gastar geração à toa: inspecionar schema de modelo pelo cache local
(`~/.cache/wavespeed/models.json`, campo `api_schema.api_schemas[0].request_schema`), nunca
disparando uma chamada "de teste" pra descobrir os parâmetros — isso já queimou US$0,30 numa
geração com prompt "test".

Ver também (gusta-prefere-diagrama-visual).

## "Autorização permanente para gastar centavos em sonda de diagnóstico antes de geração cara, sem perguntar"

Na esteira spy (lote 4, 2026-09-01) ficou autorizado gastar em **sonda barata de
diagnóstico antes de uma geração cara, sem pedir permissão** — enquanto o custo da sonda
for centavos contra o da peça. Só avisar se a sonda passar a custar muito mais que isso.

Caso concreto: US$ 0,29 em 6 sondas de voz (1 beat por voz) contra US$ 1,76 por peça de
lipsync. As sondas evitaram fechar um lote de 4 peças com uma voz só.

**Why:** o risco assimétrico é o argumento — descobrir a escolha errada depois de gastar
US$ 7,04 custa muito mais que testar antes por centavos. A regra de mostrar estimativa
antes de gastar ((estimar-custo-midia-antes-de-gerar)) continua valendo para a geração
cara em si; a sonda é a exceção.

**How to apply:** antes de disparar N gerações caras que dependem de um parâmetro não
medido (voz, modelo, enquadramento), rode 1 unidade barata por candidato, meça, e só
então dispare. Não pergunte se a sonda custa ordens de grandeza menos que o lote.

## "Troca de avatar roda na WaveSpeed com pruna-ai/p-video/avatar (US$0,025/s); avatar segue o gênero da voz; nada de Higgsfield"

Pipeline de troca de avatar da esteira spy (decidido 2026-09-05 a 2026-09-10): imagem-base no GPT Image 2 (WaveSpeed, `openai/gpt-image-2/text-to-image`) → imagem + áudio original direto num modelo de avatar falante → `remontar-*.sh` do Bisturi reconstrói a edição. Modelo padrão desde 10/09: **`pruna-ai/p-video/avatar`** (US$0,025/s, 720p ≈ 704×1280); Gusta escolheu após prova de 8 s contra OmniHuman 1.5 (US$0,16/s), OmniHuman 1.0, SoulX e InfiniteTalk. OmniHuman 1.5 fica como premium.

**Why:** Gusta mandou "não usa a Higgsfield, usa o WaveSpeed", "imagem com o GPT Image 2", "lipsync do áudio via imagem, não gera vídeo". Depois pediu modelos mais baratos. Também: gerar um avatar mulher pra voz masculina custou US$4,66 jogados fora (lote Emilly, 10/09).

Medido em 18/09/2026: para áudio de 28,97 s o Pruna cobrou **US$ 0,75 fixos** (não 0,025×28,97 = 0,72) e devolveu 704×1280 a **24 fps com 30,04 s** — sobra de cauda que a montagem precisa cortar; converter com `fps=30` preserva o sincronismo.

**How to apply:** todo preço na WaveSpeed é por segundo de áudio (o catálogo mostra US$/s). Gerar o talking head só no trecho em que o rosto aparece. Avatar sempre do gênero da voz original. Modelos "lipsync" (sync, veed, kling-lipsync) exigem vídeo de entrada, não servem pra foto. Ver (estimar-custo-midia-antes-de-gerar), (sonda-barata-antes-de-geracao-cara) e (clonador-jobs-duplicam-pedido).

25/09/2026: a Pruna falha ("Service is temporarily unavailable", estornado) com áudio de 0,93 s. Mande ≥ 2 s, pegando a fala anterior, e use só o fim na montagem.

## "Pruna p-video/avatar inventa um entrevistador na borda em cena de podcast; travar com \"SOLO SHOT ... nobody else\" no video_prompt"

Em cena de podcast, o `pruna-ai/p-video/avatar` completa o quadro sozinho: no clone de 13/09/2026 ele inseriu um homem de barba entrando pela borda esquerda em 2 de 3 clipes de close. A trava que funcionou no `video_prompt`:

> SOLO SHOT: exactly one person in the frame at all times. Nobody else is visible, no second person, no one enters or appears at the edges of the frame. … The background stays completely static and unchanged.

Para two-shot, o inverso: "EXACTLY TWO women … and nobody else ever appears", nomeando quem fala e quem escuta.

**Why:** sem isso, 3 clipes foram jogados fora (US$ 0,40 de US$ 1,75 do lote). O defeito só aparece a partir do 2º ou 3º segundo, então o primeiro frame engana.

**How to apply:** pôr a trava em todo `video_prompt` de Pruna, e conferir uma folha de frames ao longo do clipe inteiro, nunca só o primeiro. Ver (pruna-two-shot-prompt-quem-fala) e (lipsync-padrao-pruna-wavespeed).

**Mãos na lente (17/09/2026):** a trava NEGATIVA ("never raises a hand, never brings a palm near the lens") falhou em 3 de 5 clipes de selfie de 30 s. A trava **POSITIVA** resolveu de primeira: "phone held steady in his LEFT hand, out of frame. His RIGHT arm hangs relaxed at his side, completely out of frame, and stays there for the whole clip. Only his head, shoulders and chest are visible." Descrever a pose que se quer, não a que se proíbe.

**Celular em quadro (17/09, lote Zap):** a trava positiva acima cita "phone held … in his LEFT hand, out of frame" — em 1 de 5 clipes o modelo MOSTROU o celular na mão por 9 s. Não citar o objeto que não deve aparecer: "Both of his arms hang relaxed at his sides, completely out of frame, for the whole clip, and nothing is held in front of him or shown to the camera" (seed 78) saiu limpo.

**Troca de pessoa no meio do clipe (21/09/2026):** o frame 0 é a imagem; do frame 1 em diante o Pruna pode gerar OUTRA pessoa (tirou hijab, mudou cabelo, aproximou a câmera) — ~15 % dos clipes do podcast. Folha de 1 frame não pega. Prompt que travou: "The woman in the image — {descrição}, wearing {roupa} — stays EXACTLY the same person from the first frame to the last: same face, same hairstyle and head covering, same clothes, same framing". Não pedir pose diferente da imagem ("talks straight to the camera" com imagem em 3/4 reimagina a cena). Pular o frame 0 na montagem. Recorte de janela sempre centrado no rosto detectado (YuNet em `gram-detect/scripts/modelos/`), nunca fixo.

24/09/2026 (podcast Gram, plano aberto escuro): com "nobody enters from any edge" no prompt, 3/4 clipes estragaram após ~4 s (moldura verde, quadro virando foto sobre papel, gente entrando). O prompt só em positivo ("one continuous full-frame shot… fills the whole frame edge to edge… the room stays still and empty") + seed 7 deu 19/19 limpos. Triagem automática em `gram-detect/criativos/podcast-gram-clone-avatares-2026-09-24/checar.py`.

## "Pruna p-video/avatar funciona em two-shot (duas pessoas) se o prompt disser qual pessoa fala; Gusta preferiu Pruna (US$1,1) ao H3 (US$5) no podcast Gram"

No podcast Gram de 12/09/2026 (`gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12/`), o Pruna `pruna-ai/p-video/avatar` (US$0,025/s, 704×1280 24 fps) animou a pessoa certa nas cenas de two-shot quando o `video_prompt` dizia explicitamente "Only the woman on the LEFT (black blazer) is talking…; the woman on the RIGHT keeps her mouth closed and nods". O medo de "anima um rosto só" não se confirmou. Sonda de 2 cenas custou US$0,225 antes do lote.

**Why:** Gusta escolheu Pruna em vez do MiniMax H3 (≈US$5) quando perguntado; o formato podcast (host + convidada) ficou 4× mais barato sem perder o lipsync.

**How to apply:** pra podcast/duas pessoas, ir de Pruna primeiro, com prompt nomeando quem fala e quem escuta; sondar 1 cena two-shot (centavos) antes do lote. Ver (lipsync-padrao-pruna-wavespeed) e (sonda-barata-antes-de-geracao-cara).

## openai/gpt-image-2/edit cobra US$0,22-0,24 por imagem em quality=high/1k na WaveSpeed, contra base price anunciado de US$0,07

Medido no billing (`wavespeed billings`) em 13/09/2026: três chamadas de `openai/gpt-image-2/edit` com `quality=high` e `resolution=1k` cobraram US$ 0,2185, US$ 0,2185 e US$ 0,2413 — cerca de 3x o base price de US$ 0,07 que o `wavespeed models` mostra.

**Why:** ao estimar um lote de criativo, usar o base price subestima a conta de imagem em 3x. No clone de podcast de 13/09 as imagens foram 39% do custo do lote (US$ 0,68 de US$ 1,75), não os 12% previstos.

**How to apply:** estimar imagem em ~US$ 0,22 por unidade em high/1k, ou baixar para quality=medium quando o cenário vier de edit e não precisar de detalhe. Confirmar sempre no billing depois. Ver (estimar-custo-midia-antes-de-gerar).

## Gusta reprovou o clone feito por recorte de camadas do original ("ficou horrível, gambiarra"); em criativo com camadas queimadas, RECONSTRUIR de verdade

Em 14/09/2026 entreguei o AD02-H2 com 3 avatares novos colando as camadas (karaokê, painéis, CTA) **recortadas do original** por cima do avatar. Gusta: *"FICOU HORRIVEL... PRA DA PROXIMA VEZ VC RECONSTRIR E NAO FAZER CAMBIARRA COMO VOCE FEZ.. FICOU TUDO ERRADO A EDICAO"*. Peças 50-52 reprovadas.

**Why:** recorte retangular arrasta o fundo do original junto, cria emenda, e o zoom/enquadramento nunca casa — o resultado lê como remendo, não como criativo. O barato saiu caro: gastei US$ 3,20 e o material não presta.

**How to apply:** quando o criativo tem karaokê/painéis/CTA queimados sobre o rosto, **reconstruir cada camada de verdade** — medir fonte, tamanho, cor, posição e tempos e redesenhar (karaokê palavra a palavra inclusive), remontar os painéis como elementos próprios, e compor sobre o avatar novo em tela cheia. Custa mais trabalho e é o que ele quer. Nunca entregar composição por recorte de região como se fosse clone. Substitui a lição anterior (camadas-queimadas-recortar-nao-recriar), que estava invertida.

**Feito assim em 17/09/2026 (peça 53, `gram-detect/criativos/ad02-h2-reconstrucao-2026-09-17/`):** karaokê lido frame a frame (34 blocos, 90 cores) e redesenhado em Oswald Bold escolhida por largura medida; painéis com bbox fixa medida por bordas nítidas, recorte justo + sombra sintética; CTA e setas redesenhados; desfoque calibrado pela razão de nitidez. No ffmpeg, inputs secundários com `tpad` transparente, nunca `setpts` (deslocou tudo na 1ª tentativa). Molde reutilizável: `montar-reconstrucao.py <clipe> <saida>`.

25/09/2026 (Kendall 137–141): Gusta reprovou "ainda mostra resquícios do vídeo original, piscando o avatar anterior". Causas: emendas em segundos arredondados deixavam 1–5 frames da original; e o fundo desfocado atrás do card dos painéis era a própria pessoa original. Regra: emendar por número de frame e, antes de entregar, varrer frame a frame onde a pessoa original é visível no ORIGINAL (inclusive borrada atrás de painel/celular) e conferir que a peça não mostra aquilo.

## montar várias peças do Secret Revealed em série estoura a RAM do Mac e o sistema mata o processo; rodar uma por vez

Em 13/09/2026 a montagem de 3 peças do Secret Revealed em série (`montar-indianos.py i1 i2 i3`) foi morta pelo sistema por falta de memória, com duas peças já prontas. Cada montagem desenha 971 PNGs de karaokê em PIL e roda um filtergraph longo no ffmpeg.

**Why:** o job morre sem aviso e a peça parcial fica no disco com tamanho plausível (7 MB de 30 MB), o que engana se só olhar `ls`.

**How to apply:** rodar **uma peça por vez** nesse molde, em background, e conferir o tamanho/`nb_frames` antes de dar por pronta. Vale para qualquer montagem que gere milhares de PNGs. Ver (lipsync-padrao-pruna-wavespeed).

## "wavespeed run --download grava clipe pela metade sem erro quando a rede oscila; validar decodificando inteiro e rebaixar da URL do out.json"

Em 20/09/2026, num lote de 70 clipes Pruna, ~10 vieram truncados (270 KB em vez de 11 MB; ffprobe mostra a duração do header normalmente) e a montagem saiu com 19 frames sem ninguém reclamar. Também houve `fetch failed` em uploads que deixaram `image` vazio no request.

**Why:** a CLI não valida o download; `set -e` num loop derruba o lote inteiro por 1 falha de rede.

**How to apply:** depois de todo lote, `ffmpeg -v error -i clipe -f null -` (stderr vazio = íntegro); se não, rebaixar com curl da `outputs[0]` do `.out.json` (`rebaixar.py` em variacoes-30). Retry por clipe, nunca por lote. Ver (pruna-inventa-segunda-pessoa).

**27/09/2026:** `✖ fetch failed` no `wavespeed run` **não** quer dizer que a predição falhou. Ela completa e é cobrada, e o out.json só guarda o `prediction_id`. Regerar paga em dobro. Então é `wavespeed show <id> --json` → `outputs[0]` → curl → validar. Recuperei 10 de 20 clipes e 1 imagem assim (script em scratchpad `recupera.sh`, lógica: id do out.json → show → curl com retry → decodificar).

## "No recorte centrado no rosto (montar.py do podcast WPP), escolher o rosto do YuNet pelo score e não pela área; a área pega falso rosto nas plantas"

Em 24/09/2026 (var6 do podcast WPP, peças 127–131), `max(d, key=área)` no `montar.py` pegou um falso rosto nas plantas do estúdio (score ~0,65, caixa maior) e colou a convidada na borda em 2 de 5 elencos. Corrigido para `key=score`; os recortes da var5 (106–111) ficaram idênticos.

**Why:** o defeito só aparece na peça montada; o casting e os clipes estavam certos.

**How to apply:** em qualquer recorte por YuNet, escolha pelo score e varra o clipe inteiro com limiar 0,8 contando rostos por frame. Isso também acha a pessoa que a Pruna inventa ((pruna-inventa-segunda-pessoa)). Se ela estiver fora da janela, a peça fica válida. Ver (lipsync-padrao-pruna-wavespeed).

## "Medir silêncios com ffmpeg exige -hide_banner (não -v error)

Em 2026-09-11 (esteira gram01, 5 avatares) eu medi a VO do controle com
`ffmpeg -v error -i vo.m4a -af silencedetect=n=-35dB:d=0.4 -f null -` e contei **0** silêncios.
A Isca mediu **9** (5,03 s). Eu estava errado: `silencedetect` escreve no nível *info*, e `-v error`
engole a saída. O número errado entrou na nota compartilhada e quase virou premissa do lote.

**Why:** um "0" plausível não levanta suspeita, e a decisão do lote (cortar ou não pausas) dependia dele.

**How to apply:** pra `silencedetect`, `blackdetect`, `cropdetect` e afins use `-hide_banner` (sem `-v error`)
e `grep silence_start`. Se um detector devolver zero, rode uma vez sem filtro de verbosidade antes de
registrar. Quando um subagente contesta um número meu, remeço no disco antes de propagar — foi assim que
a correção entrou certa. Ver (esteira-spy-fora-do-maestri).

