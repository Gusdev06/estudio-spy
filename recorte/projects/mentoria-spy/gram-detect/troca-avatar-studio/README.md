# Troca de Avatar — studio local

Interface pra recriar um criativo campeão com **vários rostos de uma vez**, mantendo
cenário, roupa, enquadramento e o áudio original. Um criativo entra, N anúncios saem —
um por avatar. Roda em quatro modelos da Kie.ai, escolhidos na tela.

## Os modelos

| | `gemini-omni-video` | `google/gemini-omni-flash-1-1` | `wan/3-0-video` | `minimax-h3/reference-to-video` |
|---|---|---|---|---|
| janela | 1–10s | 1–10s | 1–15s | **4–15s** |
| recorta no servidor deles | **sim** (`start`/`ends`) | **sim** | não | não |
| a instrução vai como | **imagem** + "read the images" | **imagem** | texto no `prompt` | texto no `prompt` |
| seed | sim | sim | sim | **não** |
| teto por arquivo | 100 MB | 100 MB | — | **50 MB** |
| saída | 1080p | 1080p (o padrão dele é 720p) | 1080P | 2K (a montagem reduz pra 1080×1920) |
| custo | US$0,84/janela (medido) | não publicado | não publicado | não publicado |

A diferença que muda o código é **quem recorta**. O Gemini aceita uma fonte de até 30s e
corta por `start`/`ends` do lado dele, então três janelas vizinhas dividem um upload. Os
outros dois não recortam: o arquivo que sobe **já é** a janela, o que significa um upload
por janela. `ensureSource` tem os dois caminhos e a chave do cache muda junto.

A instrução também não é a mesma. No Gemini, escrita no campo `prompt` ela é ignorada e ele
devolve a pessoa original — só funciona renderizada como imagem. No Wan e no MiniMax o
`prompt` é campo de texto de verdade (20k e 7k chars), então vai escrita.

**Preço não publicado não vira chute.** A estimativa aparece como `?` até o modelo rodar
pela primeira vez aqui; o servidor guarda o que a Kie cobrou de verdade em
`jobs/.custos.json` e usa esse número nas estimativas seguintes.

O método e as regras que sustentam isso estão em
`../criativos/teste-omni-2026-08-27/README.md`.

## Rodar

```bash
cd projects/gram-detect/troca-avatar-studio
node server.js          # abre em http://localhost:4321
```

Precisa de `node` (18+), `ffmpeg`, `ffprobe` e `curl` no PATH. Sem dependências npm.

A chave da Kie fica no `.env` (`KIE_API_KEY=...`), que está no `.gitignore`.
Rodando local o `.env` costuma ter só isso. Exposto na rede, precisa também de
`STUDIO_PASSWORD=...` — veja abaixo.

## Rodar na VPS (Docker)

Serverless não dá conta e não é questão de configuração: o upload é um criativo
de 150MB em streaming (function tem teto de 4,5MB de body), o estado do job vive
entre ~6 requisições que compartilham o mesmo disco (lá só existe `/tmp`
efêmero, e cada request pode cair numa instância diferente), e a montagem é
ffmpeg reencodando 1080×1920 por minutos. Precisa de container com volume.

**Antes de expor:** a API não tem autenticação própria e **cada disparo gasta
crédito de verdade**. `STUDIO_PASSWORD` liga um Basic Auth em tudo menos
`/saude`. Sem ela o processo sobe assim mesmo e avisa no log — o que é o certo
pra rodar local, e errado pra rodar num domínio.

### EasyPanel (a mesma VPS do `social-hub-worker`)

| campo | valor |
|---|---|
| Source | GitHub → `Gusdev06/AIS-OS`, a branch onde está |
| Build path | `projects/gram-detect/troca-avatar-studio` |
| Build | Dockerfile |
| Environment | `KIE_API_KEY=...` e `STUDIO_PASSWORD=...` |
| Volume | mount `/app/jobs` — **sem isso um deploy apaga o job em andamento** |
| Domain / porta | `4321` |
| Health check | caminho `/saude`, porta `4321` |
| Resources | 2 vCPU / 3 GB — uma montagem é ffmpeg em todos os núcleos |

### Docker puro

```bash
scp .env root@SEU_IP:/opt/troca-avatar-studio/.env   # KIE_API_KEY + STUDIO_PASSWORD
ssh root@SEU_IP
cd /opt/troca-avatar-studio && docker compose up -d --build
docker compose logs -f
```

O `docker-compose.yml` publica só em `127.0.0.1:4321` — quem coloca na internet
é o proxy da VPS, com TLS. O volume nomeado `jobs` sobrevive a rebuild.

## O fluxo

1. **Arquivos** — solta o criativo, **uma ou várias fotos de avatar** e (opcional) uma
   imagem de instrução. Os avatares acumulam: dá pra soltar dois, depois mais um, e tirar
   qualquer um pelo × antes de analisar. Cada rosto vira um vídeo final independente.
   Aqui também se escolhe **o modo**, e é a decisão que mais muda o resultado e a conta:

   | | **Só onde tem gente** | **Blocos de 10s** |
   |---|---|---|
   | onde corta | em cima da pessoa: a janela começa e termina onde ela aparece | grade fixa de 10s |
   | quem decide | você, clicando na linha do tempo | a detecção, bloco a bloco |
   | o que vai pro modelo | só os segundos marcados | o bloco inteiro, com a edição dentro |
   | o que não vai | cópia byte a byte do original | idem — bloco sem ninguém nem vira chamada |
   | conferência | 40 quadros na linha do tempo | 6 blocos na grade |

   Os dois deixam de fora o que não tem rosto; a diferença é **onde cortam**. O primeiro
   aperta a janela em volta da pessoa, o que gasta menos quando ela aparece em trechos
   curtos e espalhados. O segundo manda o bloco inteiro, preservando a edição que estiver
   dentro dele — split screen, overlay, o que for — e é o modo pra quando você quer que o
   Omni receba o criativo como ele é.

   **Nem sempre o mais apertado é o mais barato.** Medido num criativo real de 57s com 22s
   de pessoa: o modo 1 partiu os segmentos em quatro janelas de 5,5s (US$3,36), o modo 2
   encheu três blocos de 10s (US$2,52). Janela pela metade custa o mesmo que janela cheia
   — é por chamada, não por segundo.

   Sem imagem de instrução, usa `assets/prompt-face-hair.png`:
   > REPLACE THE FACE AND HAIR OF THE WOMAN IN THE VIDEO WITH THE FACE AND HAIR OF THE
   > WOMAN IN THE IMAGE. DO NOT CHANGE ANYTHING ELSE.

2. **Onde tem gente em quadro** *(só no modo "só onde tem gente")* — o servidor amostra 1
   quadro por segundo, mede proporção
   de pele no miolo superior e marca o que é talking head. A linha do tempo mostra as
   miniaturas; verde vai pro modelo, escuro passa intacto. **Clique pra corrigir.**
   O slider de sensibilidade refaz o passe automático.

   Cada segundo que você não marcar é dinheiro que não gasta: num criativo de 57s onde só
   22s têm pessoa em quadro, gerar tudo custaria 2,5× mais e ainda destruiria os prints de app.

3. **Plano** — divide cada segmento marcado em janelas de no máximo 10s (limite do
   `video_list` da API), por igual, e mostra o custo antes de disparar — já multiplicado
   pelos rostos (`3 rostos × 2 trechos = 6 chamadas`). O botão de gerar carrega o número
   no rótulo, porque com quatro avatares o mesmo clique custa quatro vezes mais.

   Aqui fica a opção **"tentar com áudio primeiro"** (ligada por padrão). Manda a trilha
   junto; se o safety review do Google barrar, a ferramenta **remove o áudio e refaz sozinha**,
   sem intervenção. O card mostra qual modo cada clipe usou e, se caiu, a mensagem do bloqueio.
   Job barrado não cobra crédito, então tentar sai de graça.

4. **Clipes** — **um bloco por rosto**, com barra de progresso, e dentro dele um card por
   janela. A troca é estocástica: às vezes um clipe volta sem trocar, ou trocando só no
   meio. Assista e regere o que estiver errado — a regeração usa seed nova e é por clipe,
   então um rosto ruim não obriga a refazer os outros.

5. **Montagem** — costura trechos originais + clipes gerados na ordem, devolve a trilha
   original inteira e escreve `final-<avatar>.mp4` e `final-web-<avatar>.mp4` na pasta do
   job. Um avatar por requisição, em sequência, e cada final aparece assim que sai.

## Decisões que não são óbvias no código

- **O job sobrevive ao F5.** As gerações correm no servidor e continuam cobrando mesmo com
  a aba fechada; o id ficar só numa variável de JS significava que um reload abandonava
  trabalho já pago. Agora o id vai pro hash da URL (dá pra guardar o link ou abrir noutra
  aba) e pro `localStorage`, e a tela remonta sozinha de onde parou — inclusive a correção
  manual dos blocos, que é refeita a partir do que estava salvo em vez da detecção
  automática. Job apagado do disco devolve 404, e aí a tela esquece o id em vez de travar
  nele.

- **O modo blocos não é uma pipeline separada.** Muda só o planejador: `planWindows`
  recorta em cima dos segmentos de pessoa, `planChunks` varre uma grade fixa e decide bloco
  a bloco. Daí pra frente é o mesmo caminho — mesma fonte compartilhada, mesma geração,
  mesma montagem, mesma trilha vinda do original. Dois modos pro usuário, um pipeline só
  pra manter.
- **A grade desenha antes de qualquer aviso.** Ela é o único controle do modo blocos: se
  a detecção não achar ninguém e a tela esconder a grade junto com o erro, o usuário fica
  sem ter como dizer que ela errou. Detecção vazia mostra a grade toda apagada, o botão de
  gerar desabilitado e um aviso que diz o que fazer — não um beco sem saída.
- **A conferência do modo blocos é na grade, não na linha do tempo.** A detecção erra pra
  mais em split screen (meio rosto dá 0,46–0,55 de pele, perto do limiar), então clicar
  pra corrigir continua existindo — só que são 6 blocos em vez de 40 quadros. Bloco
  corrigido na mão manda a lista junto do plano e o servidor obedece ela em vez da detecção.
- **Blocos vizinhos que vão pro modelo dividem uma fonte só.** A API aceita 30s por arquivo
  e recorta por `start`/`ends`, então três blocos seguidos viram um upload, não três. No
  criativo de 57s medido, os blocos 20–30, 30–40 e 40–50 subiram como um arquivo de 20–50s.
- **Quanto o modelo preserva do que não pediram pra mudar é uma pergunta aberta.** O que
  foi medido: legenda queimada é redesenhada e embaralha no miolo, **inclusive nos clipes
  em que ele não trocou a pessoa** — ou seja, ele regenera o quadro inteiro sempre, não
  existe máscara. Se uma gravação de tela (blocos de UI maiores que texto de legenda)
  sobrevive melhor, ninguém mediu ainda. É uma janela de US$0,84 pra descobrir; o modo
  "vídeo inteiro" existe justamente pra poder testar isso sem gambiarra.
- **Avatar é uma dimensão do job, não um job por rosto.** A análise, os rótulos da linha
  do tempo, o plano de janelas e — o que importa — **os trechos cortados e subidos pra
  Kie** são os mesmos pros N rostos. Rodar quatro jobs separados repetiria quatro vezes um
  upload de dezenas de MB por segmento. Aqui só a chamada de geração multiplica: é o único
  custo que é mesmo por rosto. Na montagem vale o mesmo — os trechos que passam intactos
  são recortes idênticos do original, cortados uma vez e reusados por todos os finais.
- **Montagem é uma requisição por avatar.** Montar reencoda o criativo inteiro; quatro
  numa chamada só ficariam minutos de pé até um proxy desistir. A tela chama em sequência
  e mostra cada final assim que fica pronto, em vez de tudo no fim.

- **O bloqueio por áudio não é determinístico.** Medido no mesmo criativo: o trecho 20–30s
  foi barrado duas vezes ("The uploaded audio was flagged by Google safety review"), e o
  trecho 20–25,5s passou sem problema. Depende do que está sendo dito naquela janela, não
  do criativo inteiro — por isso o fallback é por janela, e cada disparo manual volta a
  tentar com áudio em vez de assumir que o criativo é "proibido".
- **A trilha final vem sempre do original, nunca dos clipes.** Os trechos que passam intactos
  já carregam o áudio original; se os gerados trouxessem áudio próprio, a trilha ficaria
  inconsistente nas emendas. Mandar áudio na entrada serve pra melhorar o sincronismo de
  boca, não pra reaproveitar o som da saída.
- **A instrução vai como imagem, não no campo `prompt`.** Escrita no `prompt`, o modelo
  ignora e devolve a pessoa original. Renderizada como imagem + `prompt: "read the images"`,
  ele executa.
- **Corte com o filtro `trim`, nunca `-ss` antes do `-i`.** Input seeking busca keyframe e
  desloca o corte em até um GOP.
- **Uma fonte muda por segmento, reaproveitada pelas janelas dele.** A API aceita fonte de
  até 30s/100MB e recorta por `start`/`ends`, então não precisa subir um arquivo por janela.
- **Limiar padrão 0.70.** A curva de pele sai bimodal: talking head cheio 0.84–0.97,
  split screen 0.46–0.55, pessoa desfocada atrás de overlay 0.16–0.33, print puro 0.04–0.11.
  Split screen fica de fora de propósito — gerar por cima destruiria a UI na metade de baixo.

## Comparar antes e depois

`/comparar.html` (link no topo da tela) abre dois players lado a lado travados no mesmo
tempo: arrasta o original de um lado, o gerado do outro. <kbd>espaço</kbd> pausa os dois
juntos, <kbd>←</kbd>/<kbd>→</kbd> anda um quadro nos dois. É o jeito de ver se a troca
segurou o quadro inteiro — dois QuickTimes abertos não param no mesmo frame.

Só o vídeo da esquerda manda no tempo; o da direita persegue. Sincronizar em mão dupla faz
os dois brigarem pelo `currentTime` e tremerem. Som só no da esquerda: a trilha é a mesma
nos dois, e juntas viram eco.

Pra guardar ou mandar pra alguém, o mais robusto é virar um arquivo só:

```bash
ffmpeg -i original.mp4 -i gerado.mp4 -filter_complex hstack -c:a copy lado-a-lado.mp4
```

## Custo

No Gemini, 168 créditos = **US$0,84** por janela de até 10s, **por rosto**. Um criativo com 2 janelas
e 3 avatares são 6 chamadas, US$5,04. O contador na tela soma o que a API cobrou de
verdade, não a estimativa. Job bloqueado pelo safety não cobra.

## Limites conhecidos

- **Legenda queimada é redesenhada pelo modelo, não copiada** — as pontas batem, o miolo
  embaralha. Pra criativo com legenda queimada, o certo é rodar num master sem legenda e
  recompor o overlay depois. A ferramenta ainda não faz esse recorte.
- Saída fixa em 1080×1920 (9:16).
- **O último rótulo é um segundo inteiro que passa do fim do vídeo** (32,416s vira rótulo
  até 33). O plano corta a última janela na duração real — pedir `ends=33` numa fonte que
  acaba em 32,4 é pedir o que não existe.
- **Upload grande depende do proxy.** O servidor recebe em streaming sem limite,
  mas um proxy na frente pode cortar o body e devolver 413. Se um criativo
  grande falhar no envio, é ali que se mexe, não aqui.
- A detecção é por proporção de pele, não face detection: acerta bem talking head contra
  screen recording, mas num criativo com muita pele que não seja rosto vai precisar de
  correção manual na linha do tempo.

## Estrutura

```
server.js        rotas HTTP, estado do job em jobs/<id>/job.json
lib/media.js     ffmpeg: corte, normalização, concat, remux, detecção
lib/kie.js       API da Kie: upload, createTask, status, download
public/index.html  a tela inteira (sem build)
public/comparar.html  antes/depois lado a lado, travados no mesmo tempo
assets/          imagem de instrução padrão
jobs/            um diretório por job (gitignored; volume no container)
Dockerfile       node 22 + ffmpeg + curl, processo sem privilégio
docker-compose.yml  volume do jobs/, health check, teto de CPU
```
