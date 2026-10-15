---
tipo: estudo
projeto: mentoria-spy / typesafe
criado: 2026-09-28
tags: [spy-zap, spy-gram, criativos, evidencia, previsao, ad-radar, wiki-trafego]
fontes:
  - projects/mentoria-spy/ad-radar/README.md
  - wiki/trafego-criativos/wiki/entidades/*
  - wiki/trafego-criativos/wiki/conceitos/*
  - wiki/trafego-criativos/wiki/tecnicas/*
---

# 01 — Base de evidência para prever qual criativo converte mais (Spy Zap / Spy Gram)

Compilação da evidência **observada** nos arquivos do repo em 2026-09-28. Nada aqui é
número inventado: onde a fonte não traz o dado, está escrito **"sem dado"**. Regra do
wiki de tráfego (regra 5): métrica só entra se veio de fonte real.

## ⚠️ Aviso sobre os "rótulos" de sucesso — não existe rótulo de conversão

Nenhum arquivo do corpus traz **conversão, CPA, ROAS, CTR ou receita** de criativo. Os
rótulos de sucesso disponíveis são dois, de naturezas diferentes:

1. **Rótulos do concorrente (Ad Library / ad-radar)** — só **proxies públicos**, nunca
   gasto real:
   - **dias-no-ar** = sobrevivência ("ninguém segura peça ruim 30 dias"). É validação de
     sobrevivência, não de ROAS. Fonte: `ad-radar/README.md`.
   - **alcance-UE** (`aaa_info.eu_total_reach`) = proxy de gasto: os anúncios miram
     "Worldwide", então o alcance na Europa é a fatia mensurável. "Melhor número público
     que existe", mas **não é gasto**. Fonte: `alcance-ue-como-proxy-de-gasto.md`.
   - **carimbo `<100 impressões`** = filtro binário "ativo" vs "entregando" (54% dos
     ativos morrem carimbados). Fonte: `carimbo-de-menos-de-100-impressoes.md`.
   - dias-no-ar e alcance-UE são **eixos independentes**: dá pra sobreviver sem escalar
     (Quinn: 103 d com UE 77) e pra escalar sem durar (Hill Alexis Brown: 7 d, UE 2.106).
2. **Rótulo da casa (Gerenciador de Anúncios)** — **gasto real** das nossas próprias
   peças. É o rótulo mais forte que existe no corpus, mas cobre só as peças da casa (Spy
   Gram, lote ads-en/16-julho), não o concorrente. Fonte:
   `gasto-do-gerenciador-como-proxy-de-performance.md`, `familia-criativos-spy-gram-ads-en.md`.

> ⚠️ Duas Páginas "concorrentes" (Sophia Jones / lado GRAM) **são da própria casa** — o
> swipe mediu a própria operação (`swipe-que-mediu-a-propria-operacao`). Página com nome
> de pessoa **não é o ator** (`nome-de-pagina-nao-e-nome-do-ator`).

---

## A) CONJUNTO DE VALIDAÇÃO — concorrente (centerpag / zappdetect), com rótulo real

Uma linha por criativo/família do concorrente [[anunciante-centerpag]] com algum sinal de
performance. **Rótulo de sucesso = dias-no-ar (sobrevivência) + alcance-UE (proxy de
gasto).** Ordenado do que mais escalou (maior alcance-UE / status "escalou") para o que
menos escalou. Todas as métricas são proxy de Ad Library, medidas em 11–12/09/2026 salvo
indicação. Hook na tela = **"sem dado"** na maioria: o radar **não baixa vídeo**, só lista
a camada headline da Meta.

| # | Criativo / Página | dias-no-ar | alcance-UE (proxy gasto) | idioma | família de headline | hook/gancho na tela | ângulo / público | mecanismo | status | fonte (arquivo) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Carol Martin (Página, sem id de peça isolada) | sem dado (nada dela entra no top de dias) | **28.368** (71% da operação; +11.847/sem) | sem dado | sem dado | sem dado (nenhuma peça baixada) | sem dado (ZAP ou GRAM não confirmado) | sem dado | ativa, concentra o gasto | `pagina-carol-martin.md` |
| 2 | Hill Alexis Brown `2145000496375191` | 7 (em 11/09) | **2.106** (maior alcance individual da semana; 53% da Página) | EN | `See this before it's too late...` (B' "antes que seja tarde") | sem dado (era só headline no corpus 27/08; tela não confirmada) | medo de descobrir tarde | `mensagem-apagada-nao-some` (implícito) | **sumiu do relatório em 13/09** | `criativo-hill-alexis-brown-2145000496375191.md` |
| 3 | Secret Revealed `934941213003855` | 7 | **1.957** (99% da Página) | EN | `⭐️⭐️⭐️⭐️⭐️ (4.9/5.0)` (prova social + free) | sem dado | prova social / curiosidade | sem dado | **escalou** (gatilho longevidade, 12/09); ativa | `criativo-secret-revealed-934941213003855.md` |
| 4 | Victoria Bennett `1390046942586673` | 2 | **1.353** (484→1.353, dobrou; +irmão `Free Test` 236) | EN | `Analyze any @username in seconds` (curiosidade sobre o objeto) | sem dado | GRAM — analisar @ de terceiro | `perfil-real-como-prova` (linha GRAM) | **escalou** (gatilho crescimento, 12/09); ativa | `criativo-victoria-bennett-1390046942586673.md` |
| 5 | Patty Marisa Alexis `2682333722195512` | 4 | **934** (301→934; 98% da Página) | EN | `Free trial: enter your partner's phone number` (free + número) | sem dado | desconfiança do parceiro | `mensagem-apagada-nao-some` | **escalou** (gatilho crescimento, 12/09); ativa | `criativo-patty-marisa-alexis-2682333722195512.md` |
| 6 | Família `Stop Doubting. Know The Truth.` (Camila Maria + Andrew Smith, 6 ids) | 8 | **640** somados (571→640; +12%) | EN | `Stop Doubting. Know The Truth.` (dor + comando, família C) | sem dado | desconfiança / dor validada | sem dado | ativa, **nunca escalou** (teste em rotação) | `familia-criativos-zap-stop-doubting.md` |
| 7 | Rachel Thompson `1472763134868396` (+6 irmãos) | **43** | 542 (Página 770) | EN | `Analyze any @username in seconds` (+ irmãos `Free trial…phone number`) | sem dado | GRAM `@` + ZAP `phone` (Página serve as duas ofertas) | `perfil-real-como-prova` | **parou** aos 43 d (Página inteira de uma vez) | `criativo-rachel-thompson-1472763134868396.md` |
| 8 | Dones `1056544273503851` (+3 irmãos carimbados `<100`) | **36** | 273 ⚠️ (congelado a semana toda) | EN | `Free Trial: Enter Your Partner's Phone Number` (headline-base free+número) | sem dado | desconfiança do parceiro | `mensagem-apagada-nao-some` | ativo, **único sobrevivente >8 d** entre ativos | `criativo-dones-1056544273503851.md` |
| 9 | Quinn `775104445592096` (+3 irmãos `<100`) | **103** (recorde da operação) | 77 | **ES** (`Prueba gratuita: introduce el número…`) | free + número (ES) | sem dado | desconfiança do parceiro | `mensagem-apagada-nao-some` | **parou** na semana 06→13/09 (Página inteira) | `criativo-quinn-775104445592096.md` |
| 10 | Família ZAP 35 dias — Isabella / Lauren / Gonçalo (3 Páginas) | **35,1** cada (ranks #13/#17/#51 de 87) | sem dado (alcance-UE não medido no swipe 27/08) | EN | `See this before it's too late...` (B') | **sem hook de tela** (título nunca vai à tela); matte só a partir do nosso lote | medo / confissão (script de traição) | `mensagem-apagada-nao-some` | **fora do ar** desde ~04/09; kit sobreviveu | `familia-criativos-zap-35-dias.md` |
| 11 | wpp-01 — Esther Vicman `1762552938111855` | 16,1 (**rank #1 de 87** em impressões) | sem dado (swipe 27/08 sem alcance-UE) | EN | headline `Free Test ✅`; matte tela `WHAT THEIR / WHATSAPP IS HIDING...` (família A) | `WHAT THEIR WHATSAPP IS HIDING...` (curiosidade sobre o objeto, sound-off) | desconfiança do parceiro | `mensagem-apagada-nao-some` + terminal hacker fake | **fora dos ativos** desde antes de 04/09 (teria ~31 d) | `criativo-wpp01-1762552938111855.md` |

**Corpus agregado "26 escalados" (swipe 27/08, peça-dias = dias-no-ar × repetição)** — rótulo
por família de hook na tela, camada distinta da headline (fonte: `mapa-de-ganchos-zap-26-escalados.md`):

| Família de hook (tela) | peça-dias | leitura |
|---|---|---|
| B' `See this before it's too late...` (só headline, nunca tela) | **107,4** | maior lastro, mas é headline |
| B imperativo `CLONE … RIGHT NOW` | 77,5 (+56,3) | maior lastro de tela, **intransferível** (palavra proibida) |
| E sem hook na tela (9 peças) | 67 | matte define o molde |
| A `o que ele esconde` (`WHAT THEIR WHATSAPP IS HIDING`) | 34,5 | **transferível**, tem #01 (#1 de 87) e #03 (#3) |
| D `como fazer` | 17,2 | reserva |
| C confissão 1ª pessoa (`I Never Thought He'd Cheat…`) | 10,6 | tudo ≤ 2,1 d |

### Referência cruzada — conjunto da CASA com rótulo de GASTO REAL (não é concorrente)

Rótulo mais forte do corpus, mas só cobre peças próprias. Fonte:
`familia-criativos-spy-gram-ads-en.md`, `criativo-gd-ad01.md`, `slogan-fixo-nao-e-gancho.md`,
`criativo-gram01-1761247818659822.md`.

| Peça | gasto real (US$) | gancho escrito na tela | avatar | wpm | fonte |
|---|---|---|---|---|---|
| GD-AD01 (campeão) | **4.074,43** | `I found something I wasn't even looking for...` (confissão 1ª pessoa, reticências) | mulher ~28, quarto | 191 | `criativo-gd-ad01.md` |
| SPY 5 (16-julho) | 1.663 | slogan, mas **sumindo aos 8,6 s** (não fixo) | mulher, carro à noite | sem dado | `slogan-fixo-nao-e-gancho.md` |
| GD-AD04 | 610,92 | `You know when something just feels off...` (confissão) | homem ~30 | 200 | `familia-criativos-spy-gram-ads-en.md` |
| GD-AD05 | 306,91 | `I kept thinking I would be the first to know...` (confissão) | mulher ~25, marejada | 214 | idem |
| L9 slogan fixo (4 peças) | 50 / 47 / 2 / 0,63 | slogan CTA fixo o vídeo todo (`THE WEBSITE IS JUST ONE CLICK AWAY.`) | vários | — | `slogan-fixo-nao-e-gancho.md` |
| GD-AD03 | 33,22 | `The worst part is realizing it was happening right in front of me...` (passado, morno) | mulher 45–55 | 214 | `familia-criativos-spy-gram-ads-en.md` |
| GD-AD02 | 9,09 | `You start noticing the little things...` (1ª pessoa mas morno, sem promessa) | homem ~35 | 265 | idem |
| SPY 1/2/6/7 (16-julho) | **US$ 101 somados**; SPY 4 (a #1 do swipe) nem entrou no top 10 | funil gravado lado a lado (L9) | vários | — | `criativo-gram01-1761247818659822.md` |

⚠️ Contradição-chave registrada: **o formato que mais SOBREVIVEU na Ad Library (L9 funil
gravado / SPY 4) é o que a Meta MENOS quis gastar** na nossa conta. Sobrevivência (proxy do
concorrente) e gasto (rótulo da casa) discordam. Fonte: `criativo-gram01-1761247818659822.md`.

---

## B) TAXONOMIA DE GATILHOS / HOOKS / ÂNGULOS

Todos os drivers de decisão que a operação usa, agrupados. `nome · gatilho na cabeça do
espectador · exemplo real`.

### B.1 Ângulos / públicos (quem é o espectador e qual a dor)

| Ângulo | Gatilho (emoção) | Exemplo real de hook | Fonte |
|---|---|---|---|
| **Desconfiança do parceiro atual** (público original) | suspeita + cansaço dos jogos | fala `If you suspect cheating and you're sick and tired of the lies and the games...` (wpp-01) | `criativo-wpp01-…` |
| **Ex-parceiro (no presente)** | saudade + ciúme + medo de ser esquecida | `I just wanted to know if he still talks about me...` | `angulo-ex-parceiro-presente.md` |
| **Pais de adolescente** | medo protetor (permissão moral total) | `My son deletes every chat before I can see it...` | `angulo-pais-de-adolescente.md` |
| **GRAM — analisar @ de terceiro** | curiosidade sobre atividade pública de alguém | `Analyze any @username in seconds` / fala `there's one detail on Instagram that gives almost everyone away` | `criativo-gram01-…`, `criativo-victoria-bennett-…` |
| **Acusação direta (raiva > curiosidade)** | vergonha + raiva ("você já sabe") | `SHE'S CHEATING ON YOU / YOU JUST DON'T WANT TO SEE IT` | `hook-de-acusacao-direta.md` |

### B.2 Mecanismos (o que sustenta a promessa sem dizê-la)

| Mecanismo | O que ativa | Exemplo real | Fonte |
|---|---|---|---|
| **Mensagem apagada não some** (big idea WhatsApp) | "o aparelho responde o que a pessoa não responde" | funil `Accessing cloud backup / Reading msgstore.db.crypt15 → RED FLAGS DETECTED` | `mensagem-apagada-nao-some.md` |
| **A verdade deixa rastro** (crença central falada) | causa/efeito: quem esconde escorrega | fala `the truth always leaves a trail and that trail is on their phone` | `criativo-wpp01-…`, `promessa-pesada-so-na-imagem.md` |
| **Perfil real como prova** (GRAM) | credibilidade verificável antes do teatro | digita o @ → devolve foto/seguidores/feed reais | `perfil-real-como-prova.md` |
| **Promessa pesada só na imagem** | a fala é vendável, o pixel carrega o proibido | fala diz "find the truth"; tela diz `Encryption bypassed` / `BRUTE-FORCE LOGIN` | `promessa-pesada-so-na-imagem.md` |
| **Autoridade por enquadramento** | cenário/props leem como autoridade sem credencial | bancada + headset de rádio (call-in-show) em vez de "Dr." | `autoridade-por-enquadramento.md` |
| **Dor e mecanismo em paralelo** | causa (dor) + efeito (produto) lidos juntos | split L9: funil trocando de tela × casal na cama, sem corte | `dor-e-mecanismo-em-paralelo.md` |
| **Contraste do mesmo objeto** | ceticismo vira suspeita ("já existe, só escondido") | mesmo perfil cinza (normal) × colorido (revelado), selo `VS` | `contraste-do-mesmo-objeto.md` |
| **Marca depois do mecanismo** | crença fica no mundo, não no produto | marca só na watermark (`whatstalker.com`), nunca falada | `marca-depois-do-mecanismo.md` (via `criativo-wpp01-…`) |

### B.3 Famílias de hook / headline

| Família | Gatilho | Exemplo real | Fonte |
|---|---|---|---|
| **A · "o que ele esconde"** (curiosidade sobre o objeto) | loop de curiosidade sound-off | `WHAT THEIR WHATSAPP IS HIDING...` / headline `See What's Really Going On ✅` (14×→24×) | `mapa-de-ganchos-zap-26-escalados.md`, `banco-de-headlines-spy-ad-library.md` |
| **B · imperativo de produto** (intransferível) | comando direto | `CLONE YOUR WIFE'S OR HUSBAND'S WHATSAPP RIGHT NOW` | `mapa-de-ganchos-…` |
| **B' · "antes que seja tarde"** | medo de descobrir tarde | `See this before it's too late...` (só headline, 107,4 peça-dias) | `mapa-de-ganchos-…`, `familia-criativos-zap-35-dias.md` |
| **C · confissão em 1ª pessoa** | identificação / desabafo de amiga | `I found something I wasn't even looking for...` (US$ 4.074) | `gancho-de-confissao-em-primeira-pessoa.md` |
| **C' · dor + comando** | dor nomeada + ordem | `Stop Doubting. Know The Truth.` (11×) | `familia-criativos-zap-stop-doubting.md` |
| **D · "como fazer"** | promessa de método | `HOW TO SEE YOUR PARTNER'S MESSAGES ON YOUR OWN PHONE` | `mapa-de-ganchos-…` |
| **Anti-padrão: slogan fixo** (NÃO é gancho) | lê como anúncio no segundo zero | `THE WEBSITE IS JUST ONE CLICK AWAY.` (US$ 50/47/2/0,63) | `slogan-fixo-nao-e-gancho.md` |

**Bancos de hipótese (estoque de teste, SEM métrica):** `banco-de-hooks-zap-l10.md` (18
mattes, ângulos: permanência, testemunha muda, anti-objeção, fracasso anterior, troca de
ação, especificidade, intenção) e `banco-de-hooks-gram-l9.md` (26 faixas: público×privado,
rastro inevitável, suspeita já formada, anti-alternativa, custo baixo, especificidade,
permanência). ⚠️ Nenhum tem lastro de performance — são hipóteses, não ranking.

### B.4 Devices (mecânicas de credibilidade / persuasão dentro da peça)

| Device | O que ativa | Exemplo real | Fonte |
|---|---|---|---|
| **Número específico quebrado** | "isso foi medido, não chutado" | `147 apagadas / 52 recuperadas`, senha `28S.X$n3q$b`, `03:17 AM` | `numero-especifico-quebrado.md` |
| **Emoji ✅** na headline | device de headline da casa | `Free Test ✅`, `Try It Free ✅`, `See What's Really Going On ✅` (4 frases) | `banco-de-headlines-spy-ad-library.md` |
| **Prova social numérica** (inventada, varia) | validação por terceiros | `⭐️⭐️⭐️⭐️⭐️ (4.9/5.0)` e `(9.9/10)` convivem | `banco-de-headlines-…`, `criativo-secret-revealed-…` |
| **"Free / free trial"** na headline | fricção baixa (só na headline, zero na tela) | `Free Trial: Enter Your Partner's Phone Number` (EN/ES/DE) | `banco-de-headlines-…`, `mapa-de-ganchos-…` |
| **Contador que sobe como prova de trabalho** | "o trabalho difícil não é seu" | `243.116 senhas testadas → 745.088 → 892.570` (gerúndio) | `contador-que-sobe-como-prova-de-trabalho.md` |
| **Perfil real / PII borrada mas legível** | espectador projeta o próprio caso | contatos `Ex`, `Bab*`, `Sec*****` | `criativo-wpp01-…`, `criativo-mockup-de-ui` |
| **Escassez dentro do print** | urgência sem alegar na copy | barra `Access expires in 09:54` | `criativo-wpp01-…` |
| **Believability + Reveal** (linha 300-prompts, adjacente) | choque "peraí, isso é IA?!" | foto realista → overlay `HYPER-REALISTIC AI` (CTR 7,46%) | `believability-reveal.md` |
| **Gancho sumindo (5–8 s) vs faixa fixa** | confissão retém; slogan fixo repele | caixa `#E80052` some aos 7,8 s (GD-AD01) | `gancho-de-confissao-em-primeira-pessoa.md` |
| **Repetição proposital tela=fala** (só no ângulo raiva) | mesmo soco no mudo e no som | faixa e 1ª fala idênticas (`EVERYONE KNOWS BUT YOU`) | `hook-de-acusacao-direta.md` |

---

## C) PADRÕES OBSERVADOS (só o que os arquivos afirmam)

1. **"Free" domina a camada headline mas é ZERO na tela.** 5 de 11 frases de headline
   (37 anúncios) usam "free"; no corpus de 27/08 e no radar, "free/trial/estrelas" nunca
   aparece como hook de tela. Headline vende o trial, a tela vende a dor — camadas
   diferentes. Fonte: `banco-de-headlines-spy-ad-library.md`, `mapa-de-ganchos-zap-26-escalados.md`.

2. **Curiosidade sobre o objeto foi a headline mais lançada e a que mais cresceu.**
   `See What's Really Going On ✅` foi de 14× → 24× (+10) numa semana; as famílias
   "free trial + número" e "dor + comando" ficaram paradas (+0). Fonte:
   `banco-de-headlines-spy-ad-library.md`.

3. **Sobrevivência ≠ escala — eixos independentes.** Quinn: 103 dias com alcance-UE 77;
   Hill Alexis Brown: 7 dias com UE 2.106. Dones: 36 d / UE 273 vs Hill 7 d / UE 2.106.
   Durar muito não é gastar muito. Fonte: `alcance-ue-como-proxy-de-gasto.md`,
   `criativo-quinn-…`, `criativo-dones-…`.

4. **Concentrar = escalar; espalhar = testar.** As peças que escalaram são
   "1 Página = 1 anúncio" com 98–99% do alcance (Secret Revealed 99%, Patty Marisa Alexis
   98%, Hill 53%). As que testam espalham ids com pouco alcance cada (Stop Doubting: 6 ids,
   640 somados, nunca escalou em 8 d). Fonte: `alcance-ue-como-proxy-de-gasto.md`,
   `familia-criativos-zap-stop-doubting.md`.

5. **O ângulo sobrevive à Página; a operação troca de Página, não de ângulo.**
   `See this before it's too late...` saiu do ar com a família 35 dias e reapareceu em
   Hill Alexis Brown; `Analyze any @username` migrou de Rachel Thompson (parou aos 43 d)
   para Victoria Bennett (escalando). A frase-base não é aposentada, a Página é. Fonte:
   `rotacao-de-paginas-como-padrao.md`, `criativo-hill-alexis-brown-…`, `criativo-victoria-bennett-…`.

6. **Metade do que está "no ar" não entrega.** 54% dos ativos ficam carimbados `<100
   impressões` (11/09: 209→93; 12/09: 224→103). "Ativo" é status do anunciante;
   "entregando" é veredito do leilão. Anúncio novo é ruído até provar o contrário. Fonte:
   `carimbo-de-menos-de-100-impressoes.md`.

7. **Gancho de confissão em 1ª pessoa (inacabado, "...") correlaciona com o maior gasto
   real da casa; slogan fixo em caixa alta correlaciona com o menor.** Os 3 mais gastos do
   Spy Gram são confissão (US$ 4.074 / 610 / 307); os perdedores são slogan ou passado
   morno (US$ 33 / 9); slogan fixo o vídeo todo gastou US$ 50/47/2/0,63, e o MESMO texto
   sumindo aos 8,6 s gastou US$ 1.663. Fonte: `gancho-de-confissao-em-primeira-pessoa.md`,
   `slogan-fixo-nao-e-gancho.md`, `familia-criativos-spy-gram-ads-en.md`.

8. **O formato mais longevo na Ad Library foi o menos gasto no nosso Gerenciador.** A SPY 4
   (L9 funil gravado) é #1 de 27 em impressões no swipe, mas na nossa conta os irmãos L9
   somam só US$ 101 e ela nem entrou no top 10 — sobrevivência (proxy) e gasto (rótulo)
   discordam frontalmente. Fonte: `criativo-gram01-1761247818659822.md`.

9. **A promessa pesada nunca é falada — só aparece na imagem.** Nas duas peças #1 dos
   swipes a locução nunca diz espionar/hackear/senha; o terminal fake e o funil carregam a
   alegação. É blindagem de política deliberada e o motivo de tantas Páginas mesmo assim
   morrerem (ângulo no limite). Fonte: `promessa-pesada-so-na-imagem.md`,
   `risco-de-politica-por-angulo-spy` (citado).

10. **Números quebrados e prova social são encenação, não medição — variam entre anúncios.**
    `4.9/5.0` e `9.9/10` convivem na mesma operação; o contador do líder do swipe até
    DESCE (393→304), contra a regra. Nada disso é copiável como número; o copiável é o
    LUGAR (estrela na headline, dor na tela). Fonte: `banco-de-headlines-spy-ad-library.md`,
    `contador-que-sobe-como-prova-de-trabalho.md`.

11. **Espanhol tem o veterano mais antigo (103 d) e o alemão acabou de entrar** — o
    concorrente localiza a mesma frase-base (`Prueba gratuita…` / `Kostenloser Test ✅`).
    "Inédito" no radar é inédito pro radar, não pro anunciante. Fonte:
    `criativo-quinn-…`, `banco-de-headlines-spy-ad-library.md`.

## Lacunas de dado (o que falta pra fechar a previsão)

- **Hook na tela do concorrente atual: sem dado.** O radar não baixa vídeo; a coluna
  "hook na tela" da tabela A é majoritariamente "sem dado". Só o corpus 27/08 tem tela medida.
- **Zero conversão/CPA/ROAS/CTR** de qualquer criativo (a única exceção de CTR é a linha
  300-prompts, fora do escopo spy: `believability-reveal` CTR 7,46%).
- **Carol Martin** concentra 71% do gasto-proxy e não tem uma única peça baixada, medida
  ou transcrita — é o buraco de evidência mais caro.
- **alcance-UE dos swipes 27/08** (wpp-01, família 35 dias) não foi medido: só rank de
  impressões e dias-no-ar.
