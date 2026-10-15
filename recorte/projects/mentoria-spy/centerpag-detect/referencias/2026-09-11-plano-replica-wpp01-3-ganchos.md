---
tipo: plano-replica
atualizado: 2026-09-11
tags: [plano-replica, spy-zap, centerpag, wpp-01, l10, gancho, matte, call-out, corpus-26]
fonte: https://www.facebook.com/ads/library/?id=1762552938111855
ad_id: "1762552938111855"
arquivo_peca: centerpag-detect/escalados/whatsapp/01-esther-vicman-1762552938111855.mp4
lote: zap-wpp01-clone-3-ganchos-2026-09-11
alavanca: gancho (matte do topo + bloco 1 falado)
teardown_edicao: 2026-09-01-teardown-edicao-wpp01-esther-vicman.md
roteiro_anterior: ../roteiros/2026-09-01-wpp01-modelado-l10-card-flutuante.md
molde_provado: ../criativos/zap-ex-presente-hook-2026-09-05/
---

# Plano de réplica — wpp-01 Esther Vicman, 3 ganchos (lote 2026-09-11)

56,77 s · 360×640 · 30 fps · locução masculina EN · #1 de 87 em impressões · 16,1 dias no ar ·
29 peças no mesmo ângulo de copy. Layout **L10** (card alfa sobre plano único), matte preta de
15 % no topo (`y 0–96`) com o hook fixo o vídeo inteiro, rosto sai aos 30,8 s (54 %) e não volta.

Este documento **não é outro teardown**. A edição já está medida em
`2026-09-01-teardown-edicao-wpp01-esther-vicman.md`; a copy já está desmontada em
`gram-detect/escalados/top3-ig-e-whatsapp/wpp-01-esther-vicman-1762552938111855-transcricao.md`.
Aqui é o plano: por que vende, o que é o gancho, o que o corpus sustenta, e os 3 ads.

> ⚠️ Tudo que é "escala" aqui é proxy de Ad Library (rank de impressões, dias no ar, repetição).
> A Meta não publica gasto, CTR, CPA nem ROAS. **Nenhum número de performance foi verificado.**
> "Dias no ar" mede sobrevivência, não retorno.

---

## 1. Por que vende

1. **O ângulo é o mais validado da conta.** A copy `2.4M people already stopped torturing
   themselves with 'what if.' They chose to know.👇` roda em **9 de 26** escalados do tier A e
   **29 de 87** no corpus inteiro (`escalados/README.md`, teardown de 01/09 §"O vencedor é
   representativo?"). Headline `Free Test ✅` em 6 de 26. O anunciante não está testando esse
   ângulo — está espalhando.
2. **Os 7 blocos fazem um trabalho cada, na ordem certa** (transcrição, §"Estrutura de copy"):
   call-out + dor (0–8 s) → 3 objeções mortas de uma vez (8–16 s) → empilhamento do que se vê
   (16–28 s) → cumplicidade (28–32 s) → mecanismo/crença (32–43 s) → anti-ceticismo (43–53 s) →
   CTA (53–57 s). Tudo que persuade acontece com rosto; o que vem depois dos 30,8 s é
   demonstração — `[[fechar-o-argumento-antes-do-rosto-sair]]`.
3. **As alavancas, uma por uma:** os **3 "sem"** ("without the other person knowing, without
   having their phone, without installing any software") matam as três objeções antes de elas
   aparecerem; a **cumplicidade** ("and you know what I mean") transforma o espectador em
   cúmplice, não em cliente; o **mecanismo "trail"** ("the truth always leaves a trail and that
   trail is on their phone") dá o *por quê funciona* sem nomear tecnologia; o **timer dentro do
   print** (`09:57 → 09:40`, medido no teardown) coloca a escassez na interface e deixa a copy
   limpa; a **promessa pesada só na imagem** — o áudio nunca diz espionar/hackear, quem diz
   `Encryption bypassed` e `147 deleted messages recovered!` é o card
   (`[[promessa-pesada-so-na-imagem]]`).
4. **O que é provado vs. o que é aposta.** Provado (pelo anunciante, por repetição): o ângulo
   de copy e a estrutura dos 7 blocos. Aposta: o molde L10 — só **3 a 4 de 26** escalados rodam
   matte preta + hook congelado (#01, #08, #11, #03 limítrofe). Se o lote morrer, a leitura é
   sobre o molde; o ângulo tem 29 peças de lastro. Atenuante: o molde já foi montado e provado
   na nossa esteira no lote EX de 05/09 (`remontar-l10.sh`), então o risco é de leilão, não de
   produção.
5. **Ele não é o mais antigo.** Três peças (#06, #10, #20) rodam há **35,1 dias** com o ângulo
   `See this before it's too late...` em 21–23 s. O wpp-01 é #1 em impressões e 5º em
   sobrevivência. Isso importa pro H2 (§4).

---

## 2. O gancho do original, dissecado

Os 3 primeiros segundos, camada por camada (frames em `medicao-wpp01-2026-09-01/frame-0.5s.jpg`,
`frame-1.5s.jpg`, `frame-3s.jpg`):

| Camada | O que está lá em t = 0–3 s | Job | Quem pega |
|---|---|---|---|
| **Texto fixo (matte)** | `WHAT THEIR` / `WHATSAPP IS HIDING...` — amarelo, caixa alta, 2 linhas, contorno preto, sobre matte 100 % preta `y 0–96`. Nunca muda. | **Nomeia o objeto e abre o loop.** "Their" segmenta sem acusar (parceiro, não "he"); "is hiding..." com reticências promete revelação e não entrega. | quem rola no mudo |
| **Falado (bloco 1)** | "If you suspect cheating and you're just sick and tired of the lies and the games, listen up because I'm going to tell you exactly how to find the truth." (0–8 s, 27 palavras ≈ 215 wpm) | Três jobs em uma frase: **segmenta** ("if you suspect cheating"), **valida a dor** ("sick and tired of the lies and the games"), **promete método** ("exactly how to find the truth"). | quem está com som |
| **Visual (card)** | Card "Chats" do WhatsApp falso: contatos `Sec*****` / `Ex ⚠️` / `Bab* ❤️` / `Jes** 💜` com badges vermelhos, tarja `147 deleted messages recovered! / Conversations deleted to hide something from you`. Karaokê `IF YOU SUSPECT` aos 0,5 s. | **Prova antes da promessa.** Nomes borrados mas legíveis o bastante pra projetar o próprio caso; número quebrado (147) lê como dado. | quem só olha a tela |
| *(fora do vídeo)* copy da Meta | `2.4M people already stopped torturing themselves with 'what if.'` + `Free Test ✅` | prova social + nomeia a dor da dúvida + oferta | quem lê antes do play |

**Quem carrega o quê:** a matte carrega **objeto + curiosidade** (o WhatsApp *deles* esconde
algo); a fala carrega **pessoa + dor + promessa de método** (você desconfia, você está cansada,
eu te mostro como); o card carrega **a prova**. Nenhuma camada repete a outra nem a copy da
Meta — é a regra de `[[tres-camadas-de-gancho-sem-repeticao]]`, cumprida.

**Consequência pro lote:** trocar só a matte (como no lote EX) muda a camada sound-off e deixa
a camada falada igual — meio gancho. Por isso a alavanca deste lote é **matte + bloco 1
juntos**, desenhados como par: cada matte pede um call-out que não a repita e que cubra o job
que ela não cobre. Precedente: CRIATIVOS-PRONTOS 10–14 (podcast v1–v5, cena 1 regravada +
caixa).

**Ritmo do bloco 1 pro Isca:** o original gasta 8 s. Alvo da casa é 180–200 wpm sem pausas
(`briefing-spy.md`), call-out de ~5 s → **15 a 17 palavras**. O original tem 27 em 7,5 s; a
versão nossa precisa cortar sem perder os 3 jobs.

---

## 3. Mapa de ganchos do corpus (26 escalados)

Fonte: `escalados/TRANSCRICOES.md` (hook na tela, peça a peça) + `escalados/README.md` (dias e
rank). "Hook na tela" = o que está queimado no vídeo no início; **headline e copy da Meta são
outra camada** e estão marcadas quando entram na leitura. Reuploads contam separado porque a
Meta os entregou separado.

### Família A — "o que ele esconde" (objeto + loop de curiosidade)

| # | Hook na tela | Página | Dias | Copy / headline |
|---|---|---|---|---|
| 01 | `WHAT THEIR WHATSAPP IS HIDING...` (matte fixa) | Esther Vicman | **16,1** | 2.4M / Free Test ✅ |
| 03 | `How to catch someone hiding the truth` (caixa verde) | Emilly Bredoff | **16,1** | 2.4M / Free Test ✅ |
| 09 | `THEY THINK THEY'RE HIDING. YOU CAN SEE EVERYTHING.` (estático) | Sophia Jones | 1,1 | 2.4M / Free trial |
| 15 | `THEY THINK THEY'RE HIDING. YOU HAVE THE POWER TO SEE EVERYTHING.` + `THE TRUTH IS IN THEIR WHATSAPP.` (estático) | Sophia Jones | 1,1 | 2.4M / Free trial |
| 11 | `DISCOVER THE MESSAGES HE'S HIDING FROM YOU` (faixa vermelha topo e base) | Fernanda Mello | 0,1 | 2.4M / — |
| 17 | `🔍 LOOK CLOSER BEFORE YOU TRUST.` (produto Instagram, adjacente) | Verônica Borges | 1,1 | 2.4M / Free Test ✅ |

5 peças (+1 adjacente) · **34,5 peça-dias** · as duas de 16,1 dias são #1 e #3 de 87 em
impressões. É a família do vencedor e é a única com dois sobreviventes de 16 dias **no mesmo
molde de copy** (2.4M + Free Test).

### Família B — imperativo de produto ("CLONE ... RIGHT NOW")

| # | Hook na tela | Página | Dias | Copy / headline |
|---|---|---|---|---|
| 06 | `CLONE YOUR WIFE'S OR HUSBAND'S WHATSAPP RIGHT NOW` (faixa verde fixa) | Isabella Walker | **35,1** | agrupado / See this before it's too late... |
| 20 | idem | Gonçalo Antunes | **35,1** | agrupado / See this before it's too late... |
| 14 | idem (faceless) | Simone Maria Braum | 2,1 | agrupado / See this before it's too late... |
| 23 | idem (= #06 reupload) | Verônica Borges | 1,1 | 2.4M / Free Test ✅ |
| 12 | `CLONE WHATSAPP` (faixa fixa) | Sara Oliveira | 4,1 | Try the app / ⭐ 4.9 |
| 02 / 04 / 10 | sem hook de abertura; a mesma faixa verde entra no meio | Alberto Souza ×2, Lauren Roberts | 4,1 / 17,1 / **35,1** | agrupado / See today… · See this before… |

5 como hook fixo (**77,5 peça-dias**) + 3 com a faixa no meio (56,3). **É a família com mais
lastro por dias × repetição do corpus** — e é intransferível pra este lote por dois motivos:
(1) a palavra `CLONE` é proibida na nossa fala e é o tipo de texto que derrubou a página
Rachel Thompson; (2) o lastro vem colado num script diferente (confissão em 1ª pessoa, "I cloned
my fiancé's WhatsApp", 21–23 s, celular físico na mão — `[[familia-criativos-zap-35-dias]]`),
não num gancho solto. Já é o molde do lote 3/4; não é o deste.

### Família B' — "veja antes que seja tarde" (é HEADLINE, não hook na tela)

`See this before it's too late...` é o título da Meta em **#06, #10, #14, #20** — 35,1 + 35,1 +
2,1 + 35,1 = **107,4 peça-dias**, as três peças mais antigas do corpus. Nunca aparece queimado
no vídeo. Ângulo: medo de descobrir tarde demais / urgência sem número. Transferível: não tem
palavra proibida e não depende do script de confissão. **É o H2.**

### Família C — confissão em 1ª pessoa na tela

| # | Hook na tela | Página | Dias |
|---|---|---|---|
| 21 | `I Never Thought He'D Cheat On Me…` (faixa rosa) | Sara Oliveira | 2,1 |
| 25 | `SICK AND TIRED` / `I Couldn'T Believe What I Found` | Sara Oliveira | 2,1 |
| 26 | `SICK AND TIRED` / `He lied. I found out.` | Sara Oliveira | 2,1 |
| 18 | sem faixa; legenda `Everything was a lie.` | Sara Oliveira | 2,1 |
| 19 / 22 | estático de story: `How did you manage to see his messages?` / `How did you find out he was lying to you?` | Kendall G. S. | 1,1 / 1,1 |

6 peças · **10,6 peça-dias** · tudo com ≤ 2,1 dias e tudo da mesma dupla de Páginas (copy `Try
the app for free` 6/26 e `Oh my god, I was in shock` 5/26). Pouco lastro como família. **Mas
#25/#26 são o anunciante subindo pra tela o call-out falado do wpp-01** ("sick and tired") — a
frase que abre o #1 virou hook fixo num lote posterior. Isso é o dado que sustenta o H3.

### Família D — "como fazer" (método)

| # | Hook na tela | Página | Dias |
|---|---|---|---|
| 03 | `How to catch someone hiding the truth` (também na A) | Emilly Bredoff | **16,1** |
| 08 | `HOW TO SEE YOUR PARTNER'S MESSAGES ON YOUR OWN PHONE` (faixa fixa, podcast) | Kendall G. S. | 1,1 |

Sobrevive quando vem colado ao "esconde" (#03). Sozinho (#08), 1,1 dia. Reserva, não H.

### Família E — sem hook na tela (abre no rosto ou na demo)

#02, #04, #05, #07, #10, #13, #16, #18, #24 — **9 de 26**, 67 peça-dias, puxados por #10 (35,1,
reupload do #02) e #04 (17,1). Nesses o gancho é 100 % falado. Não é opção pro L10, cuja matte
é o bloco que define o molde.

### Teste grátis · prova social · "click here"

**Zero hooks na tela** dizem "free", "trial" ou estrelas. Isso vive só na headline (`Free Test ✅`
6/26, `Free trial: enter your partner's phone number` 7/26, `⭐⭐⭐⭐⭐ (4.9/5.0)` 6/26) e na copy
(`2.4M people…` 9/26). "Click here" / `CLICK THE LINK BELOW AND SEE THE TRUTH NOW` é o card de
**fechamento** em #01, #03, #07, #08, #16, #24 (+ legenda "here click on" em #02/#10) — é CTA,
não abertura. Nenhuma das três vira matte de topo.

### Leitura

- **Mais lastro bruto:** imperativo CLONE (B) — intransferível (palavra + script).
- **Mais lastro transferível:** o par **A + B'**: "o que ele esconde" (2 × 16,1 d, #1 e #3 de 87)
  e "antes que seja tarde" (3 × 35,1 d como headline).
- **Dor validada na tela (C)** é a família mais nova e menos provada, mas é a única em que o
  anunciante reciclou o próprio call-out do vencedor — sinal de que ele acredita na frase.
- O que **não** existe no corpus: hook de anti-objeção na tela ("you don't need their phone"),
  hook de mecanismo ("the phone remembers"), hook de intenção ("nobody deletes to stay
  organized"). As Z-EN-01..10 do roteiro de 01/09 são boas hipóteses, **sem lastro** — ficam
  como reserva, não entram num lote de 3.

---

## 4. Plano dos 3 ads — uma alavanca = gancho (matte + bloco 1)

Blocos 2–7 idênticos em texto e áudio nos três (roteiro do Isca). O que muda: as 2 linhas da
matte e os ~5 s do call-out. Palavras proibidas na fala em §6. Todas as mattes ≤ 22 caracteres
por linha, caixa alta, 2 linhas, amarelo sobre matte preta 15 %.

### H1 — clone fiel · curiosidade sobre o objeto

| | |
|---|---|
| **Matte** | `WHAT THEIR` (10) / `WHATSAPP IS HIDING...` (21) — igual ao original, reticências incluídas |
| **Família / evidência** | A · #01 (16,1 d, #1 de 87) + #03 (16,1 d, #3 de 87), mesmo ângulo de copy |
| **Ataca** | curiosidade + suspeita: nomeia o objeto ("their WhatsApp"), não a pessoa |
| **Direção do call-out** | O mesmo movimento do bloco 1 original com palavras nossas: *condicional de suspeita → cansaço das mentiras → "vou te mostrar exatamente como chegar na verdade"*. Sem "track", sem "software" (isso é bloco 2 e sai de lá também). 15–17 palavras. |
| **Não repete** | a matte não diz "suspect/lies/truth"; a fala não diz "hiding/WhatsApp" |

### H2 — medo de descobrir tarde · urgência sem número

| | |
|---|---|
| **Matte** | `SEE THIS BEFORE` (15) / `IT'S TOO LATE.` (14) |
| **Família / evidência** | B' · headline de #06, #10, #14, #20 — **107,4 peça-dias**, as 3 peças de 35,1 d são as mais antigas do corpus. Vira matte pela primeira vez aqui (no corpus só existe como título). |
| **Ataca** | medo de perda / de ser a última a saber; empurra quem "vai ver depois" |
| **Direção do call-out** | *Se você sente isso há semanas e fica adiando — cada semana que passa, quem esconde fica melhor em esconder. Hoje dá pra saber.* Sem prazo inventado ("10 minutos", "hoje à noite" só se o funil sustentar). |
| **Não repete** | a matte não diz o objeto; a fala não diz "too late" nem "before" |
| **Por que ele e não outro** | é o único ângulo do corpus com mais dias de sobrevivência que o próprio vencedor, e é o único que atinge a **emoção que a família A não cobre** (medo em vez de curiosidade). Testa se o público do wpp-01 responde a urgência sem precisar do script de confissão que carrega esse título lá. |

### H3 — dor validada na tela · "cansei"

| | |
|---|---|
| **Matte** | `SICK AND TIRED` (14) / `OF THE LIES?` (12) |
| **Família / evidência** | C (#25, #26 — 2 × 2,1 d, hook fixo `SICK AND TIRED`) **+** o bloco 1 falado do próprio #01 (16,1 d) **+** a copy `stopped torturing themselves with 'what if'` (29/87), que é a mesma dor por outro nome. É a frase que o anunciante achou boa o bastante pra subir do áudio pra tela. |
| **Ataca** | validação da exaustão — não "ele esconde", e sim "você cansou". Pega quem já está no nível de consciência do problema e não quer mais um loop de curiosidade. |
| **Direção do call-out** | Como a matte já carrega a dor, **a fala NÃO pode dizer "sick and tired"** (repetiria a camada). A fala cobre curiosidade + método: *Você já sabe que tem algo errado. O que falta é a prova — e ela está no celular dele agora. Vou te mostrar como ver.* |
| **Não repete** | matte = dor; fala = certeza + método; card = prova |
| **Por que ele e não outro** | dos ganchos não rodados por nós, é o único que combina (1) lastro no #1 (o call-out), (2) reciclagem pelo próprio anunciante (#25/#26) e (3) uma emoção diferente de H1 e H2 (cansaço, não curiosidade nem medo). Adjacente ao podcast v2 (`IT'S NOT PARANOIA IF HE'S HIDING IT`) em espírito, mas v2 valida a *suspeita*; H3 valida o *cansaço*. Palavras diferentes, job diferente. |

### Por que não os outros

- `HOW TO CATCH SOMEONE / HIDING THE TRUTH` (#03, 16,1 d): lastro forte, mas é família A com
  outras palavras — mediria redação, não ângulo. **Reserva #1** se H1 vencer e o próximo lote
  for girar dentro da família.
- `YOU DON'T NEED / THEIR PHONE.` (Z-EN-03): anti-objeção; no corpus só #08 (1,1 d) chega perto.
  Sem lastro. **Reserva #2.**
- `THEY THINK THEY'RE HIDING. / YOU CAN SEE EVERYTHING.` (#09/#15): 1,1 d cada, estáticos, e
  "you can see everything" é promessa pesada na matte — `[[promessa-pesada-so-na-imagem]]`
  manda deixar isso no card.
- Qualquer coisa com CLONE / SPY / HACK: proibido, e é o que derruba página.
- Z-EN-07 `NO INSTALL. NO PASSWORD. NO CLUE.`: "password" está na lista de proibidas da fala;
  não vale o risco na tela.
- EX A/B/C e podcast v1–v5: já rodados, fora por regra do briefing.

### Ordem de teste sugerida

Os três sobem juntos no mesmo conjunto (é assim que 10–14 rodou). Se o orçamento obrigar a
escolher: **H1 → H2 → H3**. H1 é o controle (clone fiel); H2 é a hipótese com mais lastro de
sobrevivência; H3 é a hipótese mais barata de ler (se ganhar de H1, a dor na tela > curiosidade
na tela, e isso reorienta o banco inteiro). Leitura mínima: `[[piso-de-volume-antes-de-julgar-criativo]]`.

---

## 5. Ficha do ator pro avatar (medido nos frames)

Frames: `medicao-wpp01-2026-09-01/frame-{0.5,1.5,3,8,15,20,25}s.jpg`. O avatar é **novo** — a
ficha é o arquétipo, não a pessoa. Nome da Página (Esther Vicman) não é o nome do ator
(`[[nome-de-pagina-nao-e-nome-do-ator]]`); nenhum nome real entra no lote.

| Atributo | Medido |
|---|---|
| Gênero / idade aparente | homem, ~30–35 |
| Pele / etnia aparente | branco, pele clara com leve vermelhidão nas bochechas |
| Cabelo | curto, castanho-avermelhado (ruivo escuro), testa alta / entradas visíveis |
| Barba | cheia e curta (≈ 1 cm), mesma cor do cabelo, bem preenchida no queixo e bigode |
| Olhos | claros; olha pra baixo (pro celular) em t = 0,5 s, depois direto na câmera |
| Roupa | jaqueta esportiva preta com friso branco na gola e no ombro (track jacket, zíper), camiseta clara por baixo |
| Acessórios | nenhum (sem óculos, boné, brinco) |
| Cenário | interior doméstico; parede cinza-esverdeada escura; teto visível com objeto branco redondo (luminária/detector) no canto superior esquerdo → ele está sentado/reclinado baixo (sofá/cama) |
| Luz | ambiente, fraca, fria, baixo contraste; leve subexposição; grão de fonte 360×640 |
| Câmera | celular na mão, **abaixo da linha dos olhos, apontando pra cima** (contra-plongée leve); ligeiro balanço de mão |
| Enquadramento | busto/cabeça, ombros cortados nas laterais; topo da cabeça encosta na matte (`y≈97`); olhos em `y≈230–250` de 640 (≈ 36–39 % do quadro; no molde EX foi calibrado pra ~35 %) |
| Gesto / expressão | conversa casual, sobrancelha levemente franzida; mão no cabelo em t = 1,5 s; fala olhando pra câmera com meio sorriso em t = 15–20 s |
| Presença no vídeo | 0–30,8 s; sai e não volta |

**Pro Bisturi:** avatar masculino (voz masculina, regra da casa), arquétipo "cara comum
gravando de casa, de baixo pra cima, luz ruim". Pode variar etnia (os lotes Emilly 15–19 e
Secret Revealed 20–24 já fazem isso) — o que **não** varia é: câmera baixa, luz fraca de
interior, jaqueta escura sem marca, sem acessório, olhar na câmera. Nada de estúdio, nada de
ring light.

---

## 6. Travas

1. **PII.** Todo nome, foto, número e prévia de conversa borrado no card — mapa de blur do molde
   EX (`molde/blocos.tsv`). Grave o funil com conta de teste (`[[pii-de-terceiro-em-criativo]]`).
2. **Palavras proibidas na fala:** hack · spy · clone · password · track · location · nome de
   app/marca. **Atenção:** o bloco 2 original diz "track a phone" e o bloco 5 diz "location
   ping" — o Isca troca os dois. O roteiro de 01/09 já resolveu ("nothing gets installed",
   "the trail stays on the phone").
3. **Nenhum número inventado.** `147 / 52 / 44` são teatro da UI do original; o nosso card usa
   o que o funil gravado mostra (no lote EX: 257). Nenhum número da interface vira alegação em
   copy, título ou fala. Sem "10 minutos" na fala.
4. **`2.4M people` na copy da Meta** — pendência do Gusta (roteiro de 01/09 §9, três saídas).
   Não bloqueia o vídeo; bloqueia a subida com a copy literal.
5. **L5 (head recortado) e CR05-V4 rejeitados pela Meta** — não remontar; este lote é L10.
6. **Mapa `TRACKING · Serra, Espírito Santo` do funil fora do quadro** em todos os recortes
   (como no lote EX).
7. **Promessa pesada fica no card**, nunca na matte nem na fala: nada de "see everything",
   "read deleted", "encryption" em texto de topo.
8. **Sem lower third, sem nome, sem "case"** — ator em 1ª pessoa é UGC; com nome vira
   depoimento inventado (`[[ugc-em-primeira-pessoa-sem-virar-depoimento]]`).
9. **Sem imitar veículo ou app real** além do que o próprio funil já é; sem logo de terceiro.
10. **Custo:** lipsync só nos segundos com rosto (~55 % da peça). Estimativa do briefing:
    3 heads × ~38 s × US$ 0,025 ≈ US$ 2,85 + TTS + avatar. Nada dispara sem a conta na mesa e o
    sim do Gusta pro lipsync.

---

## 7. Passagem de bola

**Pro Isca (roteiro):**
1. Um roteiro mestre de 7 blocos, blocos 2–7 travados; **três blocos 1** (H1/H2/H3) de 15–17
   palavras cada, mesma duração ao décimo de segundo (`[[gancho-falado-como-modulo-trocavel]]`).
2. Cada bloco 1 cobre o job que a matte dele não cobre: H1 pessoa + dor + método; H2 adiamento
   + custo de esperar + "hoje dá"; H3 certeza + prova + método (sem "sick and tired").
3. Rosto sai no fim de uma frase resolvida, antes de 55 %; o argumento fecha antes disso.
4. Sem "track" / "location" / "software" — e sem prazo ("ten minutes") que o funil não assina.
5. Marque em cada bloco 1 a palavra-chave do karaokê e escreva as 3 mattes literais no arquivo
   de hooks (`molde/hooks.txt` do lote novo é do Bisturi; o texto é seu).

**Pro Bisturi (montagem):**
1. Molde L10 do lote EX (`remontar-l10.sh`, `karaoke-l10.py`, `cortar-pausas.py`,
   `conferir-lote.py`) — plano único + card alfa, matte `y 0–96` em 360×640 (15 %).
2. Avatar novo pela ficha do §5: homem ~30–35, barba cheia curta, jaqueta esportiva escura,
   câmera baixa, luz fraca de interior, olhos a ~35 % do recorte.
3. Lipsync Pruna (`pruna-ai/p-video/avatar`) só no trecho com rosto; OmniHuman só se o Pruna
   falhar. Conta reportada antes de disparar; lipsync só com o sim do Gusta.
4. Três peças = um talking head + três mattes + três blocos 1 de áudio; o áudio dos blocos 2–7
   é o mesmo arquivo nos três. Silêncio ≥ 0,4 s cortado; respiro ≤ 0,3 s.
5. Blur do card pelo `blocos.tsv`; mapa TRACKING fora; conferir os três contra o wpp-01 na
   folha de 8 instantes como no lote EX.
