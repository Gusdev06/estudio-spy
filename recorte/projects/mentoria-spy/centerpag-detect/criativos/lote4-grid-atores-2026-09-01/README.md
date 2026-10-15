# Lote 4 — grid de 4 atores no molde dos 35 dias

**Estado: ENTREGUE — 4 peças.** Gasto real US$ 7,2941.

- Roteiro: `../../roteiros/2026-09-01-lote4-grid-atores-roteiro-mestre.md` (Isca)
- Referência: `../../referencias/2026-09-01-teardown-lote3-tres-de-35-dias.md` (Peneira)
- Peça-controle: `../lote3-isabella-2026-09-01/pecas/lote3-isabella-s-en-a.mp4`

Eixo único: **rosto + voz**. Todo o resto é herdado do lote 3.

## Decisão registrada — a tarja

O briefing lista como FIXO `CLONE YOUR WIFE'S OR HUSBAND'S / WHATSAPP RIGHT NOW`. Esse é o
texto da **fonte concorrente**, transcrito no teardown — **não** é o do nosso kit. A peça que
shippou usa a **T1**:

```
YOU DON'T NEED THEIR PHONE.
YOU NEED THE NUMBER.
```

**Vale a T1 nos 4 slots.** Com a tarja do concorrente o slot 1 passaria a diferir do controle por
tarja + rosto + voz (3 alavancas) e o lote perde a leitura de ator. Evidência em
`medicao/01-tarja-briefing-vs-kit.png`. Convergente com o Isca, medido de forma independente.

## Medições feitas aqui

| Arquivo | O que mede |
|---|---|
| `medicao/01-tarja-briefing-vs-kit.png` | os dois textos de tarja lado a lado |
| `medicao/02-tarja-janela-438-589.png` | f437/f438/f588/f589 — a tarja sai e volta em corte seco |
| `medicao/03-pool-zap-ingles-17-08.png` | 10 rostos do pool ZAP, 52,6–67,5s cada |
| `medicao/04-pool-zap-cr02-cr05.png` | cr02 e cr05 = só 2 rostos em 14 clipes |
| `medicao/05-controle-vs-en7-fonte.png` | o rosto do controle sai de `VIDEO EN 7 ZAP 17.08` |

**Janela da tarja** (varredura dos 660 frames, YAVG do recorte 1170×498 em y 0, limiar 0,5/255 =
piso de ruído do H.264): sai no **frame 438** (14,600s), volta no **589** (19,633s). 151 frames
fora, 5,033s, ON em 77,12% da peça. Corte seco nas duas pontas.

## Custo — medido na fatura

| Item | Valor |
|---|---|
| VO 7 beats · `minimax/speech-2.6-hd` | US$ 0,0391 |
| Lipsync 22,000s · `sync/lipsync-2-pro` | US$ 1,7600 |
| Rosto, tarja, bloco, karaokê | US$ 0 |
| **Por peça** | **US$ 1,7991** |
| **4 peças** | **US$ 7,20** (saldo US$ 9,50 → sobra US$ 2,30) |

Tarifa do lipsync = **US$ 0,080000/s**, confirmada em 3 pontos da fatura (2,0s→$0,16 ·
22,0s→$1,76 · 32,0s→$2,56). Como 22,000s é trava do lote, o custo é fixo. Cada segundo extra
custa US$ 0,08/peça.

## Reuso do lote 3

Reuso **byte a byte**: `kit/tarja.png` · `kit/bloco-grafico.png` · grade de `vo/plano.json` ·
janela da tarja · todas as medições.
Reuso nos slots **1, 3 e 4**: os 24 `kit/karaoke/k*.png`.
**Novo por peça:** rosto conformado, VO, lipsync, re-cronometragem do karaokê.
**Novo só no slot 2:** 24 karaokês (copy própria) — render local, custo zero.
Fora de escopo: `blocos/screen.mp4` e `blocos/broll-dor.mp4` (são de L2/L4, não do molde base).

## Pendências antes de montar

1. **Gênero dos slots** — o controle é homem; "Lauren"/"Gonçalo" nomeiam o anúncio-fonte, não o
   nosso ator. Chamada do Gusta/Peneira.
2. **Rostos dos slots 3 e 4** — Peneira escolhendo. Pool utilizável é `criativos-crus/spy-zap/`,
   **não** `criativos-personagens/` (oferta GRAM, já montado, sem janela limpa de 22s).
   Homens novos disponíveis: `EN8`, `EN10`, ator do `cr05`.
3. **voice_id** — o `jobs.log` do lote 3 não gravou. A voz é a alavanca; registrar os 4 aqui.
4. **Fit de ritmo** — TTS lê 156,9 wpm, molde pede 188,2 → atempo 1,1995. Fator fora de
   1,15–1,25 = trocar a voz, não cortar palavra.
5. **Script de build** — não veio versionado no lote 3. Reconstruir e deixar aqui.

## Trava de custo

Uma peça por vez, `wavespeed billings` entre cada uma, estimativa mostrada antes de cada chamada
paga. A chave `key:tes`, que não é nossa, queimou US$ 2,60 hoje em `seedream-v5.0-pro/edit`.
Se o saldo cair sem ser por nós: parar e avisar o Maestro.


---

## Varredura do pool masculino (2026-09-01)

Feita por dois caminhos independentes (eu e o Peneira). Identidade por **imagem**, nunca por
nome de arquivo. Janela limpa por **fração de pele em YCbCr**, limiar calibrado no controle EN7
(que fica entre 0,606 e 0,855 o clipe inteiro).

**9 rostos masculinos distintos** no `criativos-crus/spy-zap`, fora o EN7.

Fusões: `23-02/es` = `23-02/en` dublado (0 rostos novos) · `cr05` = `23-02 CR05` ·
`base-ingles EN-02` = `23-02 CR03` · `base-ingles` são 4 atores × 2 versões espelhadas.
Separações: `base EN-03` ≠ `23-02 CR01` · `base EN-01` ≠ `23-02 CR07` · **EN8 ≠ EN9** (achado do
Peneira, conferido por mim em `medicao/07-en8-nao-e-en9.png`).

Com **≥22,0s contínuos limpos: 4** — `base EN-01` (50,2s), `base EN-02` (54,2s),
`base EN-03` (50,5s) e o barbudo do `cr05` (51,0s, via V3 ou V6 com recorte acima da tarja
queimada; a V1 falha por overlay EVIDENCE/SUSPICIOUS e a V2 pela barra vermelha).

Reprovados por continuidade: EN8 16,5s · EN9 9,0s · EN10 13,5s · CR01 15,0s · CR07 13,0s.

⚠️ **Correção a mim mesmo:** eu tinha afirmado que a cabeça ficava limpa o clipe inteiro no
`ingles-17-08`. Vale **só pro EN7** — EN8, EN9 e EN10 têm takeover de tela cheia. É exatamente
por isso que o EN7 pôde ser o controle.

⚠️ **Correção de número:** eu passei "3,0–4,5x de upscale" pro pool. Aquilo era casamento de
**largura de cabeça** e superestimava. O número certo é o de **altura de placa**: o pool pedia
**2,34x** e o controle **0,86x** — ele foi reduzido, nunca ampliado.

## Os 4 rostos (decisão do Maestro: material de avatar nosso)

| slot | copy | fonte | janela | upscale |
|---|---|---|---|---|
| 1 | controle, verbatim | `lote-5-avatares/final-h1-jovem-27.mp4` | 8,10s | 3,94x |
| 2 | própria (B6 = 15 palavras) | `lote-5-avatares/final-h2-grisalho-52.mp4` | 8,10s | 4,40x |
| 3 | controle | `sophia-jones-avatar-homem-38-2026-08-24/versao-A-mudo.mp4` | 6,00s | 4,68x |
| 4 | controle | `roteiro-e-2026-08-31/avatares/CRIATIVO-a1-homem-velho.mp4` | 10,00s | 3,12x |

Os 4 caminhos foram conferidos e batem exatamente. Todos 1080×1920.

⚠️ **A premissa da liberação era "sem upscale nenhum" — não é o caso.** Os avatares são frame
cheio e limpos, mas são **plano médio**: a cabeça tem 240–360px de 1080, enquanto a do controle
ocupa **96% da largura** da placa. Casar a moldura custa **3,1x a 4,7x** — mais que o pool que
foi descartado por isso.

**Segui assim mesmo, e o motivo é medido:** avatar de IA não tem grão de sensor nem ruído de
compressão no rosto, então amplia limpo. As 4 placas fechadas saíram **mais nítidas que o
próprio controle**, que é vídeo de câmera recomprimido. Ver `medicao/12-close-moldura-do-controle.png`.

Guardei as duas versões. **A escolha é do Gusta, não substituí por conta própria:**
- `rosto/slot*-close.mp4` — moldura do controle (em uso)
- `rosto/slot*-plano.mp4` — 1,32x, mais nítida, moldura larga (vira segunda alavanca)

Saída dos 8 arquivos: **1170×2532 · 660 frames · 22,000000s · 30fps**, exposição conformada ao
alvo 112,4 (saíram 105,6 / 116,2 / 103,2 / 118,2). Custo: **US$ 0**, tudo ffmpeg local.

## Próximos passos (nada pago até a grade chegar)

1. ⏳ Grade nova do Isca. Slots 1/3/4 não mudam (B6 novo tem 12 palavras, igual ao antigo);
   **slot 2 muda** — 71 palavras, atempo previsto 1,2341 contra teto 1,25, e 25 cards em vez de 24.
2. VO do **slot 2 primeiro** — menor folga de atempo; se a voz ler devagar, estoura antes de eu
   gastar nos outros três. `voice_id` registrado no `vo/jobs.log` dos 4.
3. Texto do B6 copiado **do teardown** (`referencias/2026-09-01-teardown-lote3-tres-de-35-dias.md`,
   linhas 63-64 e 70-71) — é a única cópia conferida contra a legenda queimada (`discreet`).
4. Lipsync **uma peça por vez**, `wavespeed billings | head -5` entre cada uma.
   Container: manter 660 frames e cortar o áudio em 22,000 (os 22,013s do lote 3 são padding
   do AAC, não do vídeo — se o container passar de 22s o CEIL cobra 23s = US$ 1,84).


---

# ENTREGUE — 2026-09-01

| slot | copy | ator | voz | peça |
|---|---|---|---|---|
| 1 | controle, verbatim | `final-h1-jovem-27` | `Casual_Guy` | `pecas/lote4-slot1-lauren.mp4` |
| 2 | própria, B6 15 palavras | `final-h2-grisalho-52` | `Determined_Man` | `pecas/lote4-slot2-goncalo.mp4` |
| 3 | controle | `versao-A-mudo` | `Imposing_Manner` | `pecas/lote4-slot3-ator-a.mp4` |
| 4 | controle | `CRIATIVO-a1-homem-velho` | `Deep_Voice_Man` | `pecas/lote4-slot4-ator-b.mp4` |

As quatro: **1170×2532 · 660 frames · container 22,013s** (o mesmo do controle; a sobra é
padding do AAC, não do vídeo — o stream tem 660 frames = 22,000s exatos).

## Controle do teste — uma alavanca, conferido

| trava | medido |
|---|---|
| Tarja | 100% opaca; diferença entre slots **0,012–0,030/255** = ruído de H.264 |
| Janela da tarja | frames **438–588** nas quatro |
| Bloco gráfico | frames **444–583**; difere 12–23/255 entre slots porque é **0,8% opaco** — o que varia ali é o rosto atrás, por projeto |
| Enquadramento | IOD **506/500/496/510** contra 510 do controle (spread 1,4%) |
| Eixo dos olhos | y **1246/1246/1216/1280** contra 1236 |
| Vozes | 4 `voice_id` distintos, gravados nos `vo/slotN/jobs.log` |

## Gasto real, da fatura

| item | valor |
|---|---|
| Lipsync (5 chamadas − 1 estorno) | US$ 7,0400 |
| TTS (4 slots + 1 set descartado + 6 sondas de voz) | US$ 0,2541 |
| **Total** | **US$ 7,2941** |

US$ 0,094 acima dos US$ 7,20 aprovados. A diferença é o set de VO descartado (US$ 0,0384,
voz `Patient_Man` reprovada) e as 6 sondas de voz — as duas coisas que evitaram fechar o
lote com uma voz só.

⚠️ **Uma chamada falhou e foi estornada:** slot 3, `The upstream provider is temporarily
unavailable`. Falha do provedor, não do input. Repetida sem alteração, passou na primeira.
Estorno confirmado por duas linhas na fatura com o mesmo `prediction id`.

⚠️ **O lipsync devolve largura variável:** 1166, 1170 e 1172 em três chamadas com a mesma
entrada 1170×2532. Reescalonar de volta é passo obrigatório.

## Método — três achados ingeridos no wiki

- [[padding-de-silencio-no-tts]] — 25% do mp3 do TTS é silêncio; medir wpm no bruto reprovou
  6 de 7 vozes por engano. A fala real do molde roda a **213 wpm**, não 156,9.
- [[beat-posicionado-na-marca]] — o molde **posiciona** cada beat na sua marca com ~0,2s de
  entrada; não concatena com atempo global. Com global, o B6 do slot 2 cairia 2s antes da marca.
- [[receita-do-karaoke-spy]] — Arial Black, card 1170×220 em y1676, tinta travada em 81px,
  largura máx 1005px, contorno 8px, 14 verdes em 24. Não estava versionado em lugar nenhum.

Corrigiu [[fit-de-locucao-por-tempo]] (valor velho marcado, não apagado).


---

# REENTREGA 9:16 — 2026-09-02

**Motivo: as 8 peças (lote3 L1/L2/L4/s-en-a + lote4 slots 1-4) foram REPROVADAS no Meta Ads.**
Causa medida: `1170×2532` = ratio **0,4621** (9:19,47), mais alto que 9:16 (0,5625). Reprovadas em
6 placements; Instagram Reels e Stories **não** foram listados — a assinatura de proporção, não de
codec (h264 High / yuv420p / 30fps / aac 44,1k estéreo já estavam corretos).

Saída: **1080×1920**, sufixo `-9x16.mp4`, ao lado das originais. **Nada foi sobrescrito.**
Custo: **US$ 0**, tudo ffmpeg local.

## Recomposição, não letterbox

Barra preta encolheria o conteúdo 24% e mataria o gancho. Cada camada foi reancorada no canvas novo:

| camada | 1170×2532 | 1080×1920 |
|---|---|---|
| escala do grafismo | — | 1080/1170 = **0,923077** |
| tarja | y0 h498 · corte seco ON f0–437 e f589–659 | y0 **h460** · mesma janela |
| bloco gráfico | y1596 h936 · **fade** 12f (f438→450 / f576→588) | y**1056** h864 · ancorado no rodapé |
| karaokê | y**1670** h220 | y**1124** h203 |
| rosto | full-bleed 1:1 | escalado pra 1080×2337, **corte de 417px no topo** |

## O modelo foi provado antes de usar

Reconstruí a `lote3-isabella-s-en-a` em 1170×2532 a partir das fontes e diferenciei contra a peça
que shippou. A primeira tentativa deu **15,52/255** na faixa do karaokê — o card estava 6px baixo.
Corrigido, o diff global fecha em **2,83/255** e a faixa do karaokê em **2,18** contra piso de
ruído de **2,10**. Script em `build/molde-1170-verificacao.py`.

⚠️ **Correção ao README acima:** o karaokê está em **y1670**, não `1676`. A tinta do card no
shipped vai de y1762 a 1840; com 1676 a minha ia de 1768 a 1846. O bloco em y1596 está certo
(ancorado no rodapé, 1596+936=2532).

⚠️ **Achado novo:** o bloco gráfico **não é corte seco, tem fade** de 12 frames em cada ponta, e
é um **degradê** (alpha 0 em y1596 subindo até ~230 em y2000) com o card de UI em y1890–2502.
Nada disso estava registrado.

## Corte do rosto: 417px no topo, igual nos 4 slots

Ancorar tudo no rodapé é o único offset que reproduz a relação **boca ↔ topo do card** do original
(10px de folga lá, 10px aqui). Os 417px saem do cabelo.

**Offset por slot viraria segunda alavanca.** O lote mede ator; enquadramento diferente por peça
quebraria a leitura — o mesmo motivo que fixou a tarja T1 nos quatro. O spread de eixo dos olhos
(y1216–1280 no plate) é herdado e preservado, não introduzido.

## Verificação

| checagem | resultado |
|---|---|
| ffprobe das 8 | `1080 × 1920 · 660 frames · 30/1 · 22,000000s` · h264 High · yuv420p · aac 44100 estéreo |
| ratio | 0,5625 = 9:16 exato |
| áudio | PCM extraído dos 4 slots bate **md5 idêntico** ao original (`-c:a copy`) |
| md5 frame 300 | 4 distintos: `d19e6aa5` · `8ca62304` · `faffa570` · `e94d048c` |
| tarja / bloco | frames de prova em `medicao/9x16-*-f100-tarja-no-ar.png` e `-f510-bloco-no-ar.png` |
| antes × depois | `medicao/14-antes-depois-9x16.png` |

## Layout das 3 variantes — orçamento de altura por painel

Os split-screens não aceitam "corte do rosto": são pilhas de 3–5 painéis e todos perderiam altura.

| peça | pilha 1080×1920 | de onde saíram os 417px |
|---|---|---|
| **L1** | rosto 0–1344 · painel screen 1344–1920 (576) | só do topo do rosto; painel screen 1:1 com a fonte |
| **L2** | screen 430 · faixa 187 · rosto 887 · faixa 187 · b-roll 229 | **só dos dois painéis decorativos**; rosto e as duas faixas intactos |
| **L4** | b-roll 702 · faixa 187 · rosto 1031 | só do topo do rosto |

No L2 o rosto já é uma fresta de 887px (mostra só os olhos) — tirar dele mataria a peça.
Os cortes de screen e b-roll mantêm o topo: preservam o header "Accessing WhatsApp", o "Chats" e
os dois rostos do b-roll.

## ⚠️ O 9:16 devolve 2 dos 6 placements, não os 6

| placement | depois do 9:16 |
|---|---|
| Facebook Reels | ✅ volta a veicular |
| Facebook Stories | ✅ volta a veicular |
| Instagram Feed · Explorar · Feed do perfil · Busca | ❌ teto **4:5 (0,8)** — 0,5625 continua fora |

**4:5 não sai por corte, sai por redesenho.** Em 1080 de largura a tarja ocupa 460px e o rodapé
(bloco + card) 864px. Num canvas 1080×1350 isso é **1324 de 1350 = 98,1%** — sobram **26px** de
rosto. Pra caber em 4:5 alguém tem que reduzir a tarja ou o card, e aí muda o criativo.
Leitura: **roda em Reels + Stories, desliga a família de feed.**

## O que NÃO foi refeito, e por quê

- **Karaokê:** reescalei os PNG 1170→1080 (fator 0,923) em vez de re-renderizar. O renderizador que
  gerou os cards não sobreviveu ao `/tmp`; refazer arriscaria **quebra de linha diferente**, e o
  layout tem que ser idêntico. Reduzir 7,7% um PNG de texto grande não custa nitidez, e a proporção
  contra a largura do frame fica exata.
- **B-roll / screen dos split-screens:** levantei a faixa já renderizada do master (opaca, nada
  atrás) e reescalei — mais fiel que reajustar a fonte.
- **Nada em `roteiros/` nem `referencias/`** — donos: Isca e Peneira.

Script de build versionado em `build/build9x16.py`.
