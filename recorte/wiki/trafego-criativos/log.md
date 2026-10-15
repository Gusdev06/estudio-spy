---
tipo: log
---

# 📓 Log de Ingestão

Append-only. Uma linha por ingestão: data · fonte · páginas criadas.

## 2026-07-31 — Setup inicial + 2 fontes seed
- **Setup:** estrutura criada (CLAUDE.md, index.md, log.md, raw/, wiki/{conceitos,tecnicas,entidades,fontes}).
- **Ingesta 1:** `raw/teardown-campeao-52515797525534.md` → 5 páginas:
  [[criativo-campeao-52515797525534]], [[believability-reveal]],
  [[value-stack-no-overlay]], [[censura-plataforma-asterisco]],
  [[variar-uma-alavanca-por-vez]].
- **Ingesta 2:** `raw/criativos-bidcap-2026-07-18.md` → 6 páginas:
  [[bid-cap]], [[folga-de-bid]], [[throughput-de-criativo]],
  [[campanha-ca-dzd-hotm-bidcap-en]], [[campanha-bm-latam-bidcap-en]],
  [[oferta-300-prompts]].
- Total: 11 páginas atômicas + 2 páginas de fonte. Contradição registrada: preço $6,99 vs $12,99.

## 2026-07-31 — Melhorias de método (Karpathy/Nate) + glossário
- Adicionado `wiki/glossario.md` (termos canônicos + aliases) e pasta `inbox/`.
- Regras novas no CLAUDE.md: summary line, termo canônico, manutenção/sweep.
- **Contagem real do disco: 14 páginas** (12 atômicas incl. glossário + 2 fontes).

## 2026-07-31 — Audit (index-truth + backlinks + freshness)
- 🔴 Corrigido link quebrado para a skill `aggressive-realism` em believability-reveal (era wikilink pra skill externa, virou referência simples).
- 🟡 Freshness: métricas de 11–18/jul estão drifting (2 semanas). Pendente re-ingestar dado fresco de campanha.

## 2026-07-31 — Re-ingest de freshness (dado UTMify ao vivo 25–31/jul)
- **Fonte nova:** `raw/utmify-campanhas-2026-07-31.md` (dash Principal via `claude_ai_utmfy`).
- 👑 **Troca de campeão:** criado [[criativo-campeao-52537188697334]] (ROAS 1,73); ex-campeão
  [[criativo-campeao-52515797525534]] destronado (ROAS 2,39 → 1,02).
- Atualizadas: [[campanha-ca-dzd-hotm-bidcap-en]] (2,02→1,48), [[campanha-bm-latam-bidcap-en]]
  (1,68→1,29), [[oferta-300-prompts]] (+ máquinas ES e TESTE 20/07), [[folga-de-bid]] (folga sumiu).
- Fonte-page [[fonte-utmify-campanhas-2026-07-31]] linkando tudo.
- Disco agora: 16 páginas .md. Freshness volta a 🟢 (dado de hoje).
- ⚠️ Descoberta acionável: ROAS comprimido na conta toda; alavanca virou criativo, não bid.

## 2026-08-09 — Teardown de concorrentes (Ad Library)
Fonte: `raw/2026-08-09-teardown-concorrentes-ad-library.md`. Páginas criadas: [[concorrente-nexora-teradigital]], [[concorrente-arte-digital]], [[headline-estatica-de-impacto]], [[fonte-teardown-concorrentes-2026-08-09]]. Index atualizado (seção Concorrentes + técnica nova).

## 2026-08-17 — Campeões-imagem (6 campanhas ativas) + localização FR
Fonte: `raw/2026-08-17-campeoes-imagem-e-localizacao-fr.md`. Levantamento ad-level 30d das 3 contas
(230 ads), separação imagem×vídeo, ranking por receita. 4 campeões-imagem localizados pro francês via
Seedream edit. Páginas criadas: [[localizacao-de-value-stack]], [[campanha-cbo-fr-17-08]],
[[fonte-campeoes-imagem-fr-2026-08-17]]. Index atualizado.
- ⚠️ Divergência registrada: `52515797525534` lidera em 30d (112 vd) mas está em ROAS 1,35 em 7d —
  janelas diferentes, não contradição. Regra nova: ler as DUAS janelas ao escolher campeão.
- 🔧 Gotcha novo: Seedream preserva a conjunção curta do idioma original ao "traduzir" — citar a
  palavra atual e a substituta no prompt.


## 2026-08-20 — Esteira de legenda em lote (70 bases × 3 idiomas)
Fonte: operação do dia (pasta `ESTEIRA-BASE-20:08` do 300-prompts). 130 arquivos → 93 únicos
(37 duplicatas md5) → 70 usáveis após piso de resolução. Overlay do campeão aplicado por script
Pillow em ES/EN/FR, 1080x1350. Página criada: [[legenda-em-lote-por-script]]. Index atualizado.
- 🔧 Decisão: Canva descartado (MCP só autentica; Bulk Create não serve pra trocar fundo em lote).
- ⚠️ 23 bases descartadas por resolução (400x500/500x621, thumbnails do site) — decisão do Gusta.
- ⚠️ Copy EN/FR é tradução direta do campeão ES, **não validada em leilão** ainda.

## 2026-08-21 — 1ª leitura de leilão da esteira ES 20/08 (2 dias)
Fonte: `raw/2026-08-21-leitura-esteira-20-08-es-2dias.md` (Meta Ads API via Pipeboard, CA-DZD,
20–21/08, dia 21 parcial). Páginas criadas: [[campanha-bidcap-es-esteira-20-08]],
[[campanha-abo-es-quiz-20-08]], [[estrangulamento-de-entrega-por-bid-cap]],
[[arte-nova-nao-herda-validacao]], [[piso-de-volume-antes-de-julgar-criativo]],
[[fonte-leitura-esteira-20-08-es-2026-08-21]]. Index atualizado.
- 📉 Split central: 4 conjuntos antigos R$241,76 → 18 compras (ROAS 3,37); 10 novos da esteira
  R$239,08 → 3 compras (ROAS 0,77). Mesmo funil, mesma copy, mesma verba.
- 🚫 BIDCAP ESTEIRA 20/08 gastou R$63,96 de R$6.000/dia — bid cap R$50 estrangulou a entrega, 0 vendas.
- ⚠️ Volume por criativo baixíssimo (<150 impr na maioria): ranking individual ainda é ruído.
- 🔧 Infra: Pipeboard estava no login errado do Facebook (sem CA-DZD); reconectado via /mcp.

## 2026-08-22 — Comparativo mensal jul vs ago/2026 (low ticket)
Fonte: `raw/2026-08-22-comparativo-mensal-jul-vs-ago.md` (Meta Ads API via Pipeboard, nível conta,
dias 1–22 dos dois meses). Páginas criadas: [[colapso-de-ic-para-compra]], [[conta-ca-saude-60]],
[[campanha-24dol-bidcap-02-08]], [[fonte-comparativo-mensal-jul-ago-2026-08-22]].
Atualizada: [[campanha-cbo-fr-17-08]]. Index atualizado.
- 📉 CA-DZD + BM-LATAM: gasto −24,5%, compras −43,3%, receita −38,1%, ROAS 1,99 → 1,63, CPA +33%.
- 🚨 CA-DZD: topo intacto (CTR ≈, CPM +7%, freq −9%), IC **+40%**, compras **−46%** →
  IC→compra 41,6% → 16,2%. O furo é no fim do funil, não no criativo.
- 🚀 CA SAUDE 60+ (EUR) saiu de € 27 (jul inteiro) → € 600 (22 dias), CPA € 5,22, ROAS 1,93.
  Puxada pela 24 DOL - BIDCAP - 02/08 (ROAS 2,01, CPA € 5,04) rodando com só ~€ 23/dia.
- ⚖️ BM-LATAM ROAS 2,34 > CA-DZD 1,47 com CPM 25% menor — verba está alocada ao contrário.
- ⚠️ UTMify indisponível (`MCP_INTEGRATION_NOT_FOUND`): números são de pixel, subestimam o real.
- 🔎 Contradição registrada: conta da campanha FR (wiki diz CA-DZD, dado diz CA SAUDE 60+).

## 2026-08-22 (2ª rodada) — Comparativo mensal REVISADO com UTMify
Token da UTMify regenerado pelo Gusta; a leitura da manhã (só pixel) estava **errada** e foi
substituída. Fonte crua atualizada: `raw/2026-08-22-comparativo-mensal-jul-vs-ago.md`.
Páginas criadas: [[pixel-subestima-quando-atribuicao-cai]], [[recusa-de-cartao-como-gargalo]].
Atualizadas: [[colapso-de-ic-para-compra]], [[fonte-comparativo-mensal-jul-ago-2026-08-22]]. Index atualizado.
- ✅ CORREÇÃO: agosto NÃO caiu. Bruto R$ 55.376 → R$ 56.771 (+2,5%), lucro +13,5%,
  ROAS 2,35 → 2,65, margem 54,8% → 60,2%, gastando 9,2% menos. O pixel marcava −38% porque a
  atribuição degradou (MetaAds 881 → 506 pedidos; sem UTM 77 → 200).
- 📉 O que caiu de verdade: front do low ticket (AI INFLUENCER PACK 559 → 379 vendas, −32%),
  com ticket do front estável (R$ 53,34 → R$ 52,64).
- 🔀 Back-end trocado: avulsos −65%, assinatura AI Model Lab +438% (9% → **51% da receita**).
  Ticket médio geral +47%. Concentração de risco.
- 🚨 Recusa de cartão 21,9% → **25,1%** (275 pedidos, ≈ R$ 18,2k barrados em 22 dias).
- 🔬 IC→venda 34,0% → 18,3% confirmado na UTMify (não era artefato de pixel).

## 2026-08-22 (3ª rodada) — Correção: frente FR está não-testada, não reprovada
Gatilho: Gusta perguntou se os criativos FR tinham subido ontem (21/08). Não — subiram em
**17/08**; ontem foi leitura da esteira ES + conteúdo. Ao conferir, achei que a leitura da
manhã julgou o FR abaixo do piso de volume. Atualizada: [[campanha-cbo-fr-17-08]].
- ⚠️ CORREÇÃO: `CBO FR 17/08` (SAUDE 60+) viveu 3 dias — 17/08 ROAS 0,50 · 18/08 0 ·
  19/08 **1,25 (5 compras)** — e foi **desligada no melhor dia**. Nada em 20–22/08.
- 🚫 `BIDCAP FR 17/08` (CA-DZD, bid cap R$50): os 4 criativos FR seguem ativos desde 17/08 e
  fizeram **R$ 6,34 / 51 impressões em 5 dias**. `fr-v2-jatinho` CTR 26,5% com 34 impressões.
  Mesmo [[estrangulamento-de-entrega-por-bid-cap]] da esteira ES.
- 🔧 Ação proposta (aguardando ok do Gusta): religar a CBO em euro + tirar a BIDCAP FR do bid
  cap R$50; julgar a frente só com R$ 300–500 gastos.

## 2026-08-22 (4ª rodada) — Esteira FR 20/08 subida na BIDCAP FR (70 criativos)
Gatilho: Gusta avisou que a esteira 20/08 tinha só os conjuntos em francês, sem criativo.
Confirmado: 23 conjuntos `ESTEIRA FR 20/08 - N` criados vazios em 21/08 22h35. Subidos hoje.
Página criada: [[opt-out-de-enhancements-e-padrao-da-conta]]. Atualizada: [[campanha-cbo-fr-17-08]].
Index atualizado. Entregável: `criativos/esteira-2026-08-20-fr/README-subida-meta-2026-08-22.md`.
- ✅ 70 imagens FR → 70 image_hash → 70 criativos → 70 anúncios, round-robin nos 23 conjuntos.
  Tudo **PAUSADO** esperando o Gusta ligar.
- 🔧 Bid cap R$50 → **R$150** nos 24 conjuntos (a R$50 a campanha fez R$6,34/51 impressões em 5 dias).
- 🧠 Descoberta: a conta já devolve todos os enhancements OPT_OUT por padrão; `standard_enhancements`
  é rejeitado no POST (descontinuado) — só 18 chaves individuais são graváveis.
- ⚠️ Minha varredura anterior errou ao dizer que não existiam conjuntos FR: listei campanhas e
  nunca abri os conjuntos da BIDCAP FR 17/08. Checar nível conjunto antes de afirmar ausência.
- ⚠️ Back FR continua quebrado (upsells em USD) — pré-requisito antes de escalar verba.

## 2026-08-22 (5ª rodada) — Swipe ZapSpy split-screen + esteira de 10 variações
Gatilho: Gusta mandou a URL de CDN de um criativo de app "veja o que sua conta esconde" e pediu
a peça baixada + 10 variações em `projects/zapspy/`.
Páginas criadas: [[criativo-swipe-zapspy-split-screen]], [[contraste-do-mesmo-objeto]],
[[numero-especifico-quebrado]], [[criativo-mockup-de-ui]], [[fonte-teardown-zapspy-2026-08-22]].
Index atualizado (novo grupo "Swipes"). Entregável: `projects/zapspy/` (README + 11 JPGs 1080x1920).
- 🧠 Mecanismo novo pro wiki: contraste do MESMO objeto (cinza x colorido) em vez de antes/depois.
  Vende suspeita ("já está acontecendo") em vez de transformação futura.
- 🧠 Produção: criativo de mockup de UI sai em HTML/CSS + Chrome headless, não em gerador de
  imagem — texto exato, 1 alavanca por diff, ~15s e R$0 pra regerar as 11 peças.
- ⚠️ Sem `ad_id` e sem métrica: o swipe NÃO é campeão validado. Vale como referência estrutural.
- 🔧 Teste desenhado em 4 blocos (hook v01-v04 / stack v05-v06 / CTA v07-v08 / tema v09-v10),
  cada bloco contra o v00. Nada subido ainda.
- 🔧 Correção na mesma sessão: as 11 peças saíram com **gradiente no lugar das fotos** (avatar e
  capas de destaque). Gusta pegou. Refeitas com 5 fotos reais (GPT Image 2 via WaveSpeed, US$0,29)
  + anel de story, botões vazados e divisória em gradiente. Lição na [[criativo-mockup-de-ui]].
- 🧠 Avatar do fonte é homem; as peças daqui usam mulher jovem creator (escolha do Gusta).

## 2026-08-22 (5ª rodada) — Teste de vídeo LTX 2.3 na esteira FR (3 criativos)
Gatilho: Gusta queria versão em vídeo dos criativos mas temia custo e destruição da legenda.
Fonte: `_teste-video-ltx-2026-08-22/`. Página criada: [[animar-estatico-preservando-legenda]],
[[fonte-teste-video-ltx-fr-2026-08-22]]. Index atualizado.
- ✅ **Legenda sobreviveu em 3/3** — texto e selo laranja nítidos até o último frame.
  O medo principal não se materializou.
- 💰 **$0,10/vídeo** (`wavespeed-ai/ltx-2.3/image-to-video`, 720p 5s). Esteira de 70 = ~$7.
  Custo não é barreira — é <1% de um dia de budget da BIDCAP FR.
- ⚠️ O modelo dá push-in mesmo pedindo câmera travada; num teste os pés saíram do quadro.
  Conferir o ÚLTIMO frame, nunca só o primeiro.
- 🔧 Saída 832×1024 → precisa crop+scale pra 1080×1350 (4:5). Áudio vem em silêncio digital.
- 🚫 NÃO responde se vídeo converte mais que estático — animar não herda validação
  ([[arte-nova-nao-herda-validacao]]). Próximo passo proposto: subir os 3 vídeos nos MESMOS
  conjuntos das estáticas correspondentes e comparar com piso de volume.

## 2026-08-22 (6ª rodada) — Esteira 20/08: leitura por idioma (ES/EN/FR)
Fonte: `raw/2026-08-22-esteira-20-08-por-idioma.md` (Meta Ads API, nível anúncio, 20–22/08).
Entregável: `analises/esteira-20-08-melhores-por-idioma-2026-08-22.md`.
- 🇪🇸 ES consolidado (bidcap + ABO): 30 artes, R$ 605,48, 68 IC, **7 compras**, ROAS **0,60**.
  Só 4 artes venderam. velma-carnival (680 impr, ROAS 1,55) e catwoman-latex (565 impr, 1,34)
  são as únicas com massa. flash-couch-tee (ROAS 15,70) e red-dress-sofa (8,22) têm ~70
  impressões — **ruído, não campeão** ([[piso-de-volume-antes-de-julgar-criativo]]).
- ⚖️ Conjuntos antigos validados no mesmo período: R$ 463 → 15 compras → ROAS **1,63**, com
  3 anúncios. Confirma de novo [[arte-nova-nao-herda-validacao]].
- 🇬🇧 EN **está no ar e ATIVO** na `HOTM - BIDCAP — EN` (`6998762845530`), mas entregou
  **R$ 1,90 / 28 impressões / 0 compras** em 3 dias — [[estrangulamento-de-entrega-por-bid-cap]].
- 🇫🇷 FR: 70 criativos subidos hoje, todos PAUSADOS, zero entrega.
- 🚨 ERRO MEU, corrigido pelo Gusta: afirmei que "o EN nunca subiu". Falso. A conclusão veio de
  (a) `get_adsets` com **limit 5** na conta ERRADA (BM-LATAM, sendo que o EN está na CA-DZD) e
  (b) ausência de README tratada como prova. Além disso, `get_insights` só retorna anúncio COM
  entrega — não serve pra provar que algo não existe. **Regra: pra afirmar ausência, listar
  ENTIDADES (get_ads/get_adsets) com limit alto e paginar; nunca inferir de insights ou de
  arquivo local.** Segunda vez no dia que a varredura rasa me derrubou.

## 2026-08-22 (7ª rodada) — 10 vídeos FR subidos em conjuntos SEPARADOS
Decisão do Gusta: conjuntos separados, não os mesmos das estáticas (evita vídeo e estático
competirem pela mesma entrega). Entregável: `_teste-video-ltx-2026-08-22/README.md`.
- ✅ 10 vídeos (1080×1350, 5s, sem áudio) → 10 conjuntos novos `VIDEO FR 20/08 - <arte> (bid150)`
  na **BIDCAP FR 17/08** + 10 anúncios `fr2008-v*-VIDEO`, todos **PAUSADOS**.
- 🔧 Conjuntos clonados da spec dos `ESTEIRA FR 20/08`: geo FR, mobile, pixel 1223791793200733,
  bid cap R$150. Criativo idêntico ao estático (página, link /fr, headline, CTA, copy, UTMs) —
  **só o formato muda**, o que deixa o teste vídeo vs estático limpo.
- ⚠️ API: `image_hash` + `video_id` no mesmo criativo é recusado ("Only one media source
  allowed"). Thumbnail sai do 1º frame do vídeo = a arte original. Anotado em
  [[animar-estatico-preservando-legenda]].
- 📋 Cada uma das 10 artes tem par estático nos `ESTEIRA FR 20/08 - N` → comparar mesma arte,
  vídeo vs estático, respeitando [[piso-de-volume-antes-de-julgar-criativo]].

## 2026-08-23 — FR destravou; vídeo ficou em zero entrega
Fonte: `raw/2026-08-23-fr-primeiro-dia-com-entrega.md`. Página criada:
[[conjunto-novo-em-cbo-nao-recebe-entrega]], [[fonte-fr-primeiro-dia-2026-08-23]]. Index atualizado.
- ✅ **Bid era o gargalo, provado**: R$ 6,34 / 51 impr em 5 dias (bid R$50) → **R$ 529,66 /
  3.134 impr / 9 compras** em ~1 dia. A frente FR nunca tinha sido testada de fato.
- 📊 Dia FR: ROAS 0,89 · CPA R$ 58,85 · ticket R$ 52,48 · 22 IC · 218 LPV.
  Melhores: v22-bedroom-wide-selfie (3 compras, CTR 21,94%, CPA R$ 10,40) e v33-cow-barn-bell
  (2 compras, CPA R$ 8,58). 5 artes queimaram R$ 196,60 (37% do dia) sem vender.
- 🔴 **Os 10 vídeos: ZERO impressão.** Conjuntos ACTIVE, 8 dos 10 anúncios ACTIVE — e nada.
  O CBO deu todo o budget aos conjuntos de estática, 1 dia mais velhos.
- ⚠️ Bid da campanha alterado no gerenciador de R$150 → R$35 (updated 23/08 00:31); 2 anúncios
  de vídeo arquivados. Mudanças feitas fora da API — sempre reler estado antes de concluir.
- 🧠 Lição nova: teste de formato com conjunto novo em CBO maduro não testa formato, testa
  antiguidade. Pra testar vídeo: ABO separada com budget fixo, ou vídeo DENTRO de conjunto
  que já entrega.

### 2026-08-23 — faxina FR: 5 anúncios pausados
Aprovado pelo Gusta. Critério: gasto ≥ R$24 no dia com zero venda. IDs conferidos por nome antes.
v23-blonde-bodysuit-polaroid (R$54,35) · v29-bw-lingerie-bed (R$49,42) · v38-gamer-room-bodysuit
(R$39,30) · v20-beach-freckles (R$28,81) · v06-20 (R$24,72). **Sangria estancada: R$196,60/dia
(37% do budget)**. Bid de toda a campanha segue em R$35 (alterado no gerenciador).

### 2026-08-31 — formato call-in show + remodelagem do wpp-01 (spy zap)
Fonte: `raw/2026-08-31-formato-call-in-show-driftwell.md` (anúncio Driftwell via @ladprofit no X, 41s)
cruzada com o criativo escalado `wpp-01-esther-vicman-1762552938111855` (57s, #1 de 87 em impressões,
16,1 dias no ar, destino go.centerpag.com). Ambos transcritos via Whisper — a legenda nativa do X vinha
trocada (era de outro anúncio, GLP-1/MyoGuard), corrigida.
Achado principal: a referência **não é entrevista de jornal**, é call-in show com **1 pessoa na câmera**
(a cliente é só voz de telefone). 9 beats reproduzíveis, marca revelada só aos 63% do vídeo. O wpp-01 já
tinha 4 desses beats em monólogo — remodelar foi redistribuir, não reescrever. A troca de invólucro
elimina o terminal hacker fake (`Encryption bypassed`/SS7) entregando a mesma crença.
Páginas criadas: [[formato-call-in-show]] · [[autoridade-por-enquadramento]] · [[marca-depois-do-mecanismo]]
· [[cliente-converte-no-ar]] · [[nao-imitar-veiculo-real]] · [[criativo-wpp01-1762552938111855]]
· [[fonte-formato-call-in-show-2026-08-31]].
⚠️ Zero métrica verificada nas duas peças — só tempo no ar.

### 2026-08-31 — formato breaking news âncora+especialista (2ª referência @ladprofit)
Fonte: `raw/2026-08-31-formato-breaking-news-myoguard.md` (45s, 9:16, 100% IA — âncora sintético,
especialista sintética, produto inventado MyoGuard Pro). É o formato "entrevista de jornal" que o
Gusta tinha descrito. Publicado pelo autor como **demonstração de risco**: *"the only thing standing
between this and a multimillion-dollar lawsuit is a disclosure line I burned into the [vídeo]"* — e
o disclosure não aparece na versão do X (ticker cortado à direita = vídeo recortado de quadro mais largo).
Craft reutilizável isolado em [[costura-de-clipes-por-tarja-persistente]]: as duas pessoas NUNCA
aparecem juntas (2 gerações independentes), costuradas por tarja idêntica pixel a pixel + handoff
falado + linha de reação. Ticker anuncia o problema, nunca o produto. Marca aos 69% (Driftwell: 63%).
3 pernas de risco separadas do craft: tarja BREAKING NEWS, credencial médica bordada, alegação de
saúde sobre droga real por médica falsa. Roteiro C (versão sem as 3) adicionado ao arquivo de roteiros.
Páginas: [[costura-de-clipes-por-tarja-persistente]] · [[fonte-formato-breaking-news-2026-08-31]];
atualizadas [[nao-imitar-veiculo-real]] e [[marca-depois-do-mecanismo]].
Nota: a legenda nativa do X no post do Driftwell era **deste** anúncio (tracks trocadas na mesma
conta). Sempre re-transcrever com Whisper antes de confiar em legenda de X.

### 2026-08-31 — Roteiro D: copy do wpp-01 no formato breaking-news
Adaptação da copy do criativo #1 do swipe pra estrutura âncora+especialista do MyoGuard, via skill
`ad-creative`. Mapeamento 1:1 dos 6 beats; a copy do wpp-01 encaixou quase sem forçar porque ela já é
um argumento de mecanismo — só estava sendo entregue por uma pessoa só em vez de duas figuras.
Grounding puxado do `gram-detect/manifest.json` (27 anúncios): a copy mais repetida do swipe é
*"2.4M people already stopped torturing themselves with 'what if.' They chose to know."* (12x) — virou
o fecho do âncora. Entregue: roteiro de 45s, hook matrix de 6 aberturas (3 componentes cada), 8
variações de ticker, 6 textos principais + 5 headlines + 3 descrições com contagem de caracteres,
tabela quente/frio das 3 pernas de risco, e plano de teste em 3 rodadas (thumbstop → hold → CTR).
Página nova: [[ticker-como-hook-sound-off]]. Atualizada: [[criativo-wpp01-1762552938111855]].
⚠️ Lacuna registrada: corpus sem reviews e sem comentários de anúncio. Todo o grounding é ad copy de
concorrente = linguagem de marketing, não de cliente. Raspar comentários da Ad Library é o próximo passo.

### 2026-08-31 — Roteiro D produzido: 1ª peça de anúncio 100% IA da operação
Cadeia: GPT Image 2 (2 frames-base 9:16 2k high, $0,38 cada) → Kling 3.0 Pro image-to-video
(5 clipes falados, sound=true, $0,168/s) → ffmpeg (tarja + concat). Saída: 45,2s, 1080×1920, em
`projects/mentoria-spy/gram-detect/criativos/roteiro-d-2026-08-31/roteiro-d-v1-45s.mp4`.
**Achado principal: o Kling 3.0 Pro fala o roteiro escrito** — áudio nativo com lip sync, sem TTS e
sem etapa de lipsync. Os 5 clipes foram transcritos com Whisper depois e bateram palavra por palavra.
`duration` aceita até 15s, então cada bloco de fala coube num clipe só. Continuidade de cenário entre
os dois personagens resolvida repetindo LITERALMENTE os blocos de cenário e luz nos dois prompts de
imagem. Identidade e cenário aguentaram 15s sem drift.
**Custo total: ~$8,32 por criativo completo de 45s**, sem talento e sem set. Saldo WaveSpeed pós-run: $10,11.
Gotchas: (1) `wavespeed run --download` deu `fetch failed` com o job já `completed` — recuperar com
`wavespeed show <id>` + curl; (2) `drawbox` sobre canvas rgba transparente escreve cor mas não alpha —
desenhar a tarja direto no filtro de cada clipe em vez de gerar PNG.
Decisões de risco aplicadas: tarja de programa inventado (`THE SIGNAL`), especialista sem credencial
nem jaleco, marca nunca falada, ticker anunciando o problema.
Páginas: [[gpt-image-2-para-frames-base]] · [[kling-3-fala-o-roteiro]] · [[fonte-producao-roteiro-d-2026-08-31]].

### 2026-08-31 — Roteiro D fechado: insert de dashboard + card de CTA
Peça finalizada (45,2s). Tarja subida de y=1600 → **y=1380** (72% da altura) pra sair da faixa que a
UI de Reels/TikTok cobre. Adicionados: (1) insert do dashboard em 33–35s — print falso do WhatsApp em
HTML/CSS + headless Chrome a 1080×2400, com scroll de 2s via `crop` com expressão em `t`, entrando
como **cutaway sobre a fala** (overlay só no vídeo, áudio da especialista correndo por baixo);
(2) card `FIRST SEARCH IS FREE` em barra crimson encostada na tarja, 43–45s.
Ordem de filtro importa: a tarja tem que ser desenhada DEPOIS do overlay do insert, senão o insert
a apaga e a costura quebra. Conteúdo do dashboard ancorado no wpp-01 (147 deleted messages, tags
DELETED/SUSPICIOUS, horários quebrados), **sem terminal hacker** — autoridade e visual de invasão
se cancelam. Sem legenda queimada, de propósito: competiria com a tarja.
`montar.sh` parametrizado (`TARJA_Y`, `TICKER`, `PROGRAMA`, `CTA`) — recompõe o corte inteiro em ~40s
sem gastar crédito, que é o caminho pra testar as 8 variações de ticker do roteiro.
Atualizada: [[criativo-mockup-de-ui]].

### 2026-08-31 — Roteiro D: mockup trocado por footage real do funil
Substituídos os inserts de HTML pelo screen recording real do `go.zappdetect.com`
(`EDIÇÃO 2/EDIÇAO ANIMADA/ScreenRecording_08-13-2026 19-56-53_1.MP4`, 3min33, 1170×2532, HEVC 60fps).
Dois cutaways sobre a fala da especialista: A em 33–35s (digitando o número) casando com "you enter
the number", B em 37,2–40,6s (`RECOVERED FROM DELETED CACHE` + conversas suspeitas) casando com
"you're reading what was already there".
**Achado:** a landing repete a copy do anúncio quase literal — "Built for people who've been burned
by spy apps that didn't work", "No app to install", "No phone access needed". Ou seja, o
[[criativo-wpp01-1762552938111855]] não inventou ângulo: leu a página. Congruência anúncio→página
fechada no pixel.
⚠️ **PII:** o recording é de conta real — número +55 27 99954-6872, e-mail gabrieljota@gmail.com,
nome "Gabriel". Aplicado `boxblur=24:3` no campo do número; a tela de captura de e-mail (t≈168–176)
foi evitada inteira. Qualquer trecho novo desse arquivo precisa da mesma varredura.
Nota: destino do recording é `go.zappdetect.com`, mas o wpp-01 aponta pra `go.centerpag.com` —
**não confirmado** se é a mesma oferta em dois domínios. Checar antes de tratar como equivalente.
Página nova: [[insert-de-funil-real-como-cutaway]]. Mockup HTML mantido como fallback.

### 2026-08-31 — teardown completo das edições GRAM (12 criativos)
Varredura de `projects/mentoria-spy/EDIÇÃO/`, `EDIÇÃO 2/` e `downloads/EDIÇÃO*/`: 30 arquivos,
**12 criativos únicos** por md5. Assistidos: MASC ING, FEM PORT, MASC PORT; amostrados: FEM ING,
MASC ESP. Cru em `raw/2026-08-31-edicoes-gram-teardown.md`.
Achados: (1) **nenhum tem locução** — áudio a 2 kb/s, são peças 100% visuais guiadas por interface;
(2) **template fixo de 9 módulos** nos 12; (3) **matriz completa 2 gêneros × 6 idiomas**, sem buraco,
onde MASC/FEM é o gênero do ALVO e não do público; (4) **PT é outlier de duração** (81,8s e 71,7s vs
44–54s) por causa de um 3º card de dados suspeitos e um módulo de fechamento extra que só ele tem;
(5) marca localiza junto (Gram Detect / Gram Espião / Gram Espía); (6) dois alvos só nos 12.
⚠️ **PII de terceiro exposta** nos 12: @kamamortonn e @bennet_chloe_ aparecem legíveis — @, nome,
foto, contagens, posts com legenda e lista de DMs. Só as prévias de mensagem estão borradas.
Precedente de risco: a página Quinn do swipe caiu com os criativos removidos.
⚠️ **1,82 GB de duplicata** — 2,93 GB ocupados pra 1,11 GB de conteúdo. `EDIÇÃO 2/` é cópia byte a
byte de `EDIÇÃO/`.
⚠️ Zero métrica cruzada: não se sabe qual célula da matriz converte.
Páginas: [[familia-criativos-gram-funil-gravado]] · [[template-funil-gravado-9-modulos]] ·
[[matriz-genero-x-idioma]] · [[perfil-real-como-prova]] · [[escalada-de-compromisso-no-wizard]] ·
[[contador-que-sobe-como-prova-de-trabalho]] · [[pii-de-terceiro-em-criativo]] ·
[[fonte-edicoes-gram-2026-08-31]].

### 2026-08-31 — varredura completa da biblioteca de criativos spy (296 peças)
Inventário de todo vídeo em `projects/mentoria-spy/`: **373 arquivos, 296 únicos por md5**, 15,16 GB
ocupados pra 10,84 GB de conteúdo (**4,33 GB de duplicata**), ~2h50 de footage. TSV completo em
`raw/2026-08-31-inventario-criativos-mentoria-spy.tsv`.
Método: folha de contato por lote (3 frames por vídeo a 12/45/80% + nome + duração). Assistir 296 uma
a uma não cabe; a folha por lote revela o **eixo de variação**, que é o que serve pra escalar produção.
Amostrados 73 (cr02, cr05, base-ingles, ingles-17-08, 23-02 en+es, ads-en, criativos-personagens, GRAM);
não assistidos 34 (16-julho, 26-julho, ingles-com-head, exports-0824, referencias-zapspy, tratados-28);
~95 fora de escopo (subprodutos de geração de avatar).
Achados: (1) **6 eixos de variação** em uso — layout, personagem, idioma, duração, hook, casting UGC;
(2) **7 layouts** catalogados de cr02/cr05, que são a MESMA locução montada de 7 formas — o L1 é o
wpp-01 campeão; (3) **o molde é a unidade de produção**: AD04 tem 3 atores em 23,9s exatos, AD05
compartilha o mesmo b-roll entre os 3; (4) **status de moderação no nome do arquivo** em 2 peças
(`REJEITANDO`), justamente os layouts de head recortado sobre screen; (5) clusters de duração
18–33s / 44–57s / 62–82s; (6) 2 dos 10 ângulos do ads-en usam o device "primeiro a saber" — o mesmo
do sticker do Roteiro D, ou seja repertório da casa que voltou.
⚠️ Zero métrica cruzada com qualquer peça. ⚠️ Não existe manifest por criativo.
Páginas: [[biblioteca-criativos-mentoria-spy]] · [[eixos-de-variacao-de-criativo]] ·
[[catalogo-de-layouts-spy]] · [[molde-de-edicao-n-atores]] · [[rejeitando-no-nome-do-arquivo]] ·
[[fonte-varredura-biblioteca-spy-2026-08-31]].

### 2026-08-31 — transcrição em lote: 95 peças com copy indexada
Correção de premissa do Gusta: o acervo **não é aleatório, é curadoria de vencedores**. Isso inverteu
a prioridade que eu tinha proposto — a transcrição deixa de precisar do cruzamento com Meta Ads pra
ter valor, porque a seleção já é o sinal.
Transcritas 114 peças de criativo (excluídos subprodutos de avatar, `_APAGAR` e o swipe da Ad Library):
**95 com copy falada, 19 mudas por natureza** (família GRAM + 1 asset de seta).
Saída em `projects/mentoria-spy/transcricoes/`: `transcricoes.json` (texto + segmentos por md5),
21 `.md` por lote, `folhas/` com folha de contato de todo lote, e `manifest-criativos.csv` (114 linhas).
Cópia do manifest em `raw/2026-08-31-manifest-criativos-spy.csv`.
Dois bugs que custaram rodada e valem registro:
1. **Caminho relativo + cwd errado** — o ffmpeg não achava os arquivos e o script reaproveitava o mp3
   da iteração anterior, o que casaria áudio com o arquivo errado. Sempre resolver pra caminho absoluto.
2. **Whisper alucina em silêncio** — devolve `you` / `Thank you.` em faixa muda. Sem filtro, as 12
   peças GRAM (que são mudas de propósito) entrariam como "tendo copy". Filtro: 6+ palavras distintas.
Também: rate limit do Groq derruba lote grande; resolvido com backoff + fallback pra OpenAI.
Distribuição: spy-zap 74 · spy-gram 29 · EN 87, ES 12, PT 2, DE/FR/IT 2 · curto 37, médio 48, longo 29.
Colunas `layout`, `ator`, `gasto`, `ctr`, `roas` ficaram reservadas em branco no manifest.
Atualizada: [[biblioteca-criativos-mentoria-spy]].

### 2026-08-31 — manifest completo: layout e ator preenchidos nas 114 peças
Colunas `layout` e `ator` do `manifest-criativos.csv` preenchidas a partir das folhas de contato de
todos os 21 lotes. Layout: L8 (head cheio + karaokê + insert) 29 · L1 (head + funil) 24 · L9 (funil
gravado sem head) 12 · bruto de editor 13 · swipe de concorrente 10 · L2–L7 de 1 a 3 cada · assets e
fragmentos 6. **34 atores distintos**; os mais reaproveitados são `m-negra-trancas-oculos` (9 peças) e
`h-barbudo-jaqueta` (9 peças) — cada um cobre um lote inteiro de variação de layout mais uma entrada
no lote bilíngue 23-02.
Dois lotes reclassificados por não serem peça de anúncio: `exports-0824` e `referencias-zapspy` são
**brutos de editor** (86–550s, timeline com várias variações emendadas), e parte de `downloads/` é
asset (setas transparentes, animação de carregando) ou fragmento de 2–5s.
Gotcha: nome de arquivo no macOS vem em **NFD** (o `Ç` de `EDIÇÃO` decomposto) — lookup por string
literal em Python falha silenciosamente. Normalizar com `unicodedata.normalize("NFC", …)` antes de casar.
⚠️ **A checar:** o talking head do `wpp-01-esther-vicman` (o #1 de 87 do swipe, tido como concorrente)
é o MESMO ator e a MESMA locução do lote `cr05` da casa. Ou é creator licenciado em comum, ou a página
Esther Vicman é da própria operação — o README do gram-detect já registra a página Gustagoat no swipe.
Atualizada: [[biblioteca-criativos-mentoria-spy]].

### 2026-08-31 — spec de edição: as medidas dos layouts
Lacuna apontada pelo Gusta: o wiki tinha o catálogo de layouts (o QUE está empilhado) mas nenhuma
medida (ONDE). Das 36 páginas, só uma tinha px ou cor hex. Sem medida ninguém reproduz.
Medido com régua percentual sobre frames amostrados; ferramentas salvas em
`projects/mentoria-spy/transcricoes/medidas/` (`regua.py` sobrepõe a régua, `medir.py` detecta
fronteira de painel e barra chapada). Precisão ±2%.
Registrado em [[spec-de-edicao-layouts-spy]]: posição de banda do L1/L2/L3/L8, spec de legenda por
lote (estilo, cor, posição), cor da faixa de hook por oferta, e a tabela de resolução/aspecto.
⚠️ **Achado que muda placement: 16 peças (`base-ingles` + `23-02-spy-en-es`) são 1440×1080, ou seja
4:3 DEITADO.** Não servem pra Reels/Stories sem recorte — e o recorte come as laterais, que é onde
mora o painel do funil nesse layout. Precisam ser remontadas, não recortadas.
Também: o acervo não é uniforme em resolução — 1080×1920, 1080×1440 (4:5), 1440×2560, 2160×3840 (4K)
e 1170×2532 convivem. Regra que se repete em TODOS os lotes: legenda de 2 a 4 palavras, caixa alta,
contorno preto grosso; nunca frase inteira.


### 2026-08-31 — teardown do vencedor do swipe GRAM (peça #1, Sophia Jones)
Fonte: `raw/2026-09-01-teardown-vencedor-gram-sophia-jones.md` (entregável em
`projects/mentoria-spy/gram-detect/referencias/`). Peça `ad_id 1761247818659822`, 32,5s, 360×640.
Método reproduzível: cortes por detecção de cena sobre o crop do painel do app (medidos, não
estimados), medidas de layout por perfil de luminância, locução transcrita **localmente** com
`mlx-whisper` (nada saiu da máquina), altura de voz por F0 de autocorrelação.
Copy do anúncio conferida campo a campo entre o `.txt` da peça e o `manifest.json` — batem.
Achado principal: **o painel esquerdo do vencedor é o [[template-funil-gravado-9-modulos]] inteiro** —
o mesmo ativo que a [[familia-criativos-gram-funil-gravado]] já tem gravado em 6 idiomas × 2 gêneros.
A diferença é só o invólucro: lá o funil ocupa 35,8% da largura sob um talking head, uma faixa de
hook fixa e um b-roll de dor que nunca corta. **Não falta funil, falta casca.**
> ⚠️ **ERRATA (01/09):** o "35,8%" desta entrada está **errado** — a divisão vertical é **39,4%**
> (`x=142` em 360). O texto acima fica como foi escrito porque o log é append-only; esta marca existe
> pra quem chegar aqui por grep não levar o número velho. Ver a entrada de 01/09 e
> [[medir-fronteira-de-bloco-em-video]].
Segundo achado: as 4 peças de vídeo da página rodam o mesmo roteiro palavra por palavra, com duração
igual ao milissegundo — e a #10 tem **voz feminina sobre rosto masculino**. O talking head é B-roll de
rosto; a faixa de hook é a única variável real entre as quatro (o eixo que o nosso lote tem parado).
Novas: [[criativo-gram01-1761247818659822]], [[funil-gravado-como-painel-lateral]],
[[dor-e-mecanismo-em-paralelo]], [[promessa-pesada-so-na-imagem]], [[roteiro-mestre-com-n-vozes]],
[[faixa-de-hook-fixa-sem-legenda]], [[fonte-teardown-vencedor-gram-2026-08-31]].
Atualizadas: [[catalogo-de-layouts-spy]] (L8 que só existia no spec + **L9** novo),
[[molde-de-edicao-n-atores]], [[familia-criativos-gram-funil-gravado]],
[[contador-que-sobe-como-prova-de-trabalho]].
⚠️ **Nenhuma métrica de performance verificada.** O ranking do swipe é proxy de Ad Library (flag de
baixo volume + ordem de `total_impressions desc` + dias no ar + repetição do ângulo) — não é ROAS.
⚠️ Duas contradições abertas no índice: karaokê vs faixa fixa, e contador que sobe vs contador que
desce no líder.
⚠️ PII de terceiro escancarada na peça (@ real, foto, feed e caixa de DM com nomes civis completos) —
[[pii-de-terceiro-em-criativo]]. Borrar tudo antes de modelar.


### 2026-09-01 — roteiro mestre GRAM no molde L9 (do teardown do vencedor pro filmável)
Fonte: `raw/2026-09-01-roteiro-gram-l9-modelado.md` (entregável em
`projects/mentoria-spy/gram-detect/roteiros/2026-09-01-gram01-modelado-l9-roteiro-mestre.md`).
Deriva de [[fonte-teardown-vencedor-gram-2026-08-31]]. Entrega: tabela cena a cena de 32,5s casando
os 9 módulos do [[template-funil-gravado-9-modulos]] com os 7 beats da locução, VO mestre de 29s em
**EN/PT-BR/ES**, **26 faixas de hook** e **10 ganchos falados** — o eixo que a
[[familia-criativos-gram-funil-gravado]] tem parado (as 12 peças abrem idênticas).
Três coisas novas que o roteiro obrigou a nomear:
**(1)** as camadas de gancho — faixa queimada, fala e UI — entram juntas e **nenhuma repete a outra
nem a copy da Meta**: [[tres-camadas-de-gancho-sem-repeticao]];
**(2)** gravar o **B1 em arquivo separado** faz o gancho falado custar 3,8s de áudio em vez de uma
regravação inteira: [[gancho-falado-como-modulo-trocavel]];
**(3)** o estoque de hook virou página própria: [[banco-de-hooks-gram-l9]].
Decisões registradas: a mistura EN/PT-BR do vencedor **deixa de ser herdada** e vira teste declarado
(lote A todo-EN × lote B com a mistura); traduzir a copy fica travado até o Gusta liberar, porque a
ordem é reproduzir a copy do vencedor como está. Contador **sobe** (291 → 348 → 389 → 412),
corrigindo o defeito do vencedor por [[contador-que-sobe-como-prova-de-trabalho]].
Achado de produção (medido com `ffprobe`, não estimado): os 12 recordings de funil em
`downloads/EDIÇÃO/GRAM {FEM,MASC} {PORT,ING,ESP,FRAN,ITA,ALEM}.mp4` são todos `1170×2532` mas
**não têm a mesma duração** — `FEM PORT` 71,7s, `FEM ESP` 52,8s, `MASC ING` 46,2s. O painel do L9
pede 31,3s: não existe um corte único que sirva pros 12, cada arquivo precisa dos próprios pontos
de entrada e saída pra bater nos 9 marcos.
Novas: [[tres-camadas-de-gancho-sem-repeticao]], [[gancho-falado-como-modulo-trocavel]],
[[banco-de-hooks-gram-l9]], [[fonte-roteiro-gram-l9-2026-09-01]].
Atualizadas: `index.md` (técnicas, entidades, fontes + contradição de idioma).
⚠️ Nenhuma métrica verificada — nem do vencedor modelado, nem dos 26 hooks escritos. É estoque de
teste, não ranking.
⚠️ [[pii-de-terceiro-em-criativo]] repassada ao roteiro como checklist de borrão antes de exportar;
o certo continua sendo regravar o funil com conta de teste.

### 2026-09-01 — teardown do vencedor GRAM: renomeado e completado com o caminho da peça
Consolidação, não re-ingestão. O teardown foi renomeado de `2026-08-31-…` para
`projects/mentoria-spy/gram-detect/referencias/2026-09-01-teardown-vencedor-gram-sophia-jones.md`
(e o cru em `raw/` junto), com as 4 referências ao nome antigo corrigidas — inclusive o roteiro do
Isca em `gram-detect/roteiros/2026-09-01-gram01-modelado-l9-roteiro-mestre.md`. Nenhuma página
atômica foi duplicada; [[fonte-teardown-vencedor-gram-2026-08-31]] mantém o nome porque é a data da
ingestão e já tem 8 backlinks.
Acrescentado o que faltava pro portal do Bisturi: **os caminhos exatos dos arquivos da peça #1**
(vídeo, poster, txt, cópia do top3, registro no manifest), com md5 conferido contra o
`manifest.json` — `9e300448c20fd4d138ba074a2e35caa1` pro `.mp4`. A cópia em `top3-ig-e-whatsapp/`
é byte a byte a mesma; a canônica é a de `escalados/instagram/`.
Atualizadas: [[criativo-gram01-1761247818659822]] (bloco "Arquivo"),
[[fonte-teardown-vencedor-gram-2026-08-31]].
⚠️ Mídia pesada continua fora do git — o portal referencia o arquivo no disco.

### 2026-09-01 — CORREÇÃO: a divisão vertical do L9 estava errada em 13 px
Contestação do Bisturi, conferida aqui de forma independente antes de mexer em qualquer coisa: **ele
está certo**. A divisão do painel do [[criativo-gram01-1761247818659822]] não é 35,8% (`x=129`) e sim
**39,4% funil / 60,6% b-roll** (`x=142` em 360; `x≈426` em 1080; `x≈462` no recording de 1170).
Causa do erro: a primeira medida veio de **cor num frame único** — o maior salto de luminância entre
colunas. Nesse layout há uma **borda escura interna ao painel do funil** (moldura do card do app) em
`x≈128`, onde a luminância cai de 117 → 42. É o maior penhasco de cor do quadro e não é fronteira.
Verificação independente: variância temporal sobre 59 frames (1,0–30,0s) fica em ~78 até `x=141` e
desaba pra ~10 em `x=142` — 7× numa coluna. O movimento atravessa a borda escura, provando que ela é
interna. O mapa de movimento do Bisturi mostra o mesmo a olho nu.
As fronteiras **horizontais** foram reconferidas pelo mesmo método e **estão certas**: `y=306` e
`y=380` batem por cor e por variância. O erro foi só na vertical.
Corrigidas: teardown `2026-09-01-teardown-vencedor-gram-sophia-jones.md` (+ o cru em `raw/`, com a
nota de por que o método antigo engana), [[funil-gravado-como-painel-lateral]],
[[criativo-gram01-1761247818659822]], [[familia-criativos-gram-funil-gravado]],
[[catalogo-de-layouts-spy]].
Nova: [[medir-fronteira-de-bloco-em-video]] — a lição virou método, vale pra todo teardown de split.
⚠️ O número errado propagou pro roteiro do Isca (`gram-detect/roteiros/2026-09-01-gram01-modelado-l9-roteiro-mestre.md`,
`x 0–419` deveria ser `x 0–462`) e pro cru dele em `raw/2026-09-01-roteiro-gram-l9-modelado.md`.
Avisado — a correção é dele, o arquivo é do dono.
⚠️ As entradas de log anteriores a esta linha mantêm o número antigo: log é append-only, esta entrada
as supersede.

### 2026-09-01 — o método de medição tinha um limite; página reescrita e renomeada
Fonte: README do lote `gram01-l9-faixa-2026-09-01` (cru em `raw/2026-09-01-lote-gram01-l9-faixa-montagem.md`),
via [[fonte-lote-gram01-l9-faixa-2026-09-01]].
A página dizia "fronteira se mede por movimento, **nunca** por cor". Estreito demais: isso vale pra medir
**referência de terceiro**. Pra **peça nossa já montada** — onde a faixa é chapada e sintética porque nós
a desenhamos — a cor é o método certo, e determinístico: linha 1211 = 0,000 magenta, 1212 = 0,96.
Renomeada `medir-split-por-variancia-temporal` → [[medir-fronteira-de-bloco-em-video]]; 8 arquivos com
backlink corrigidos (teardown, roteiro do Isca, os dois crus, index, funil-gravado-como-painel-lateral,
criativo-gram01, este log). Nenhuma referência ao nome antigo sobrou.
⚠️ **Divergência com a fonte, resolvida na verificação.** O README atribui a falha ao lipsync ("só a boca
se mexe, a base do head congela e cola na faixa"). Reproduzi nas duas versões e **não procede**: a
variância do head é igual ou maior na v2 (testa 25,01→25,00; boca/queixo 20,19→**21,01**; pescoço/ombro
15,63→**16,58**; faixa 0,15 nas duas). O lipsync não congelou nada. A falha também reproduz na **v1, que
não tem lipsync** (`y=1081`).
Causa real: **limiar absoluto frouxo**. A base do head é naturalmente quieta (~10,6 contra ~21 do rosto)
em ambas as versões; `var<12` pega o ombro antes da faixa. Com o detector de **penhasco** (maior queda) ou
limiar relativo, a variância acerta `y=1212` nas duas. A conclusão prática do Bisturi (usar cor na peça
nossa) **está certa** — o mecanismo é que estava trocado.
Regra nova que saiu disso e vale pros dois casos: **penhasco, nunca limiar absoluto** — limiar é calibrado
num vídeo e quebra no seguinte.
Novas: [[fonte-lote-gram01-l9-faixa-2026-09-01]]. Atualizadas: [[medir-fronteira-de-bloco-em-video]]
(reescrita), index.md (2 correções novas registradas).

### 2026-09-01 — refinamento do Bisturi: o eixo do erro é nível vs. transição, não absoluto vs. relativo
Ele aceitou a correção de mecanismo (reproduziu a comparação v1/v2 por conta própria e chegou na mesma
direção: a v2 se mexe mais, e o detector dele erra na v1 também — 1131 contra 1121 — o que mata a
hipótese do lipsync sozinho). Corrigiu README e portal **por marcação, não apagamento**, e linkou
[[medir-fronteira-de-bloco-em-video]].
E devolveu dois refinamentos que **corrigem a minha generalização**. Verifiquei os dois nos meus dados
antes de aceitar:
1. **"Exigir bloco contíguo" não salva.** No nível que falha, os candidatos já formam um bloco único
   (`y1149–1497` na v1, `y1143–1497` na v2): a base quieta do head encosta na faixa sem intervalo, não
   há vale pra separar. Confirmado.
2. **O limiar dele já era relativo** (55% da mediana do head), então o eixo do erro não é
   absoluto-vs-relativo — eu tinha escrito errado. Prova nos meus próprios números: dois critérios
   relativos dão respostas opostas (15% do máximo do quadro → 1212 ✓; 55% da mediana do head → 1149 ✗),
   e entre absolutos `var<8` acerta e `var<10` erra. O eixo real é **nível vs. transição**: o que separa
   acerto de erro é só onde o valor calhou de cair. Transição não precisa de calibragem.
Página atualizada: a regra passou de "penhasco, nunca limiar absoluto" para **"transição, nunca nível"**,
com a tabela refeita, a seção de correções-que-não-funcionam, e a ressalva de que os y de falha variam
com escala de render (1131/1121 dele × 1149/1143 meus) — o padrão é universal, os números não.
Registro de método: esta é a 3ª vez no lote que uma correção anda **contra** o fluxo da esteira
(Bisturi→Peneira nos 13 px, Peneira→Bisturi no mecanismo, Bisturi→Peneira aqui). O canal a favor
(Peneira→Isca→Bisturi) carrega o trabalho; o erro sempre sobe. Vale como padrão, não como exceção.

### 2026-09-01 — as duas bordas de um bloco não têm a mesma dificuldade (teste em 4 vídeos)
O Bisturi testou a pergunta que ficou em aberto — se a transição acha sozinha, sem número, fora de um
vídeo — e a resposta é **não**. Transição pura sem janela dá resultado sem sentido nas peças montadas
(base acima do topo); com janela posicional melhora, mas o topo ainda erra em 2 dos 4 vídeos.
Isso **derruba uma afirmação minha**: eu tinha escrito que "o penhasco não precisa de calibragem".
Está errado e ficou registrado na página em vez de apagado.
O achado estrutural dele, que é o que vale: **borda contra bloco AGITADO** (faixa→painel, uma subida)
é confiável; **borda contra bloco CALMO** (head→faixa, uma queda) é frágil, porque compete com outras
quedas dentro do próprio bloco de cima. Não por acaso, é a borda que o detector dele errou — ele tinha
reportado "1121–1498" sem notar que só metade estava errada.
Quantifiquei a fragilidade pra fechar a divergência de medição entre nós dois. Margem = transição
vencedora ÷ 2ª maior concorrente:
  referência Sophia Jones — topo **1,52×** · base 3,72×
  peça v1 — topo **1,05×** · base 4,56×
  peça v2 — topo **1,04×** · base 4,54×
Margem de 1,04× não é acerto, é empate. No meu pipeline a borda de cima acertou nos 3 vídeos que medi;
no dele errou em 2 de 4. **Nenhum dos dois está errado** — os dois amostram um quase-empate e o desempate
fica em detalhe de preparo (escala de render, recorte de zona, faixa de frames). O que importa não é quem
acertou: é que **onde a margem é apertada o resultado não é reprodutível entre pipelines**.
Regra nova: medir a margem antes de confiar; margem < 2× exige segunda medição independente.
Reforça a metade da cor: na peça nossa ela resolve as DUAS bordas deterministicamente
(1211=0,000 / 1212=1,000 / 1497=1,000 / 1498=0,000), sem janela, sem nível, sem margem a avaliar.
Atualizada: [[medir-fronteira-de-bloco-em-video]].

### 2026-09-01 — o corte de 2× de margem, medido por dois pipelines (n=14)
O Bisturi reproduziu a margem em 4 vídeos × 2 bordas e reportou **classificador perfeito** nos 8 pontos
dele: toda margem ≥2× acertou, toda <2× errou.
**Nos meus 6 pontos há 3 contraexemplos** — margens 1,52×, 1,05× e 1,04×, todas **acertando**. Conferi
antes de responder.
Juntando os dois pipelines: **margem ≥2× → 8/8 acertos**; **margem <2× → 3/6**. Ou seja, o corte de 2×
separa muito bem, mas o que ele separa é **reprodutibilidade, não correção**. Abaixo de 2× é cara ou
coroa, e a demonstração mais limpa disso é a borda de cima da v1/v2: margem **1,05× e 1,04× nos dois
pipelines**, batendo até a segunda casa, com **desempate oposto**. Mesma indecidibilidade, moedas
diferentes.
Registrar como classificador ("abaixo de 2× erra") seria overfit à amostra dele e induziria ao erro:
quem medisse 1,2× e acertasse concluiria que está errado. A página passou a dizer: acima de 2×, confie;
abaixo, meça de novo por outro método — não conclua que errou, conclua que não sabe.
O que o próximo teste procura: contraexemplo **acima** de 2×. Até aqui não há nenhum, em 8 medições de
dois pipelines. Amostra ainda pequena e de um layout só.
Atualizada: [[medir-fronteira-de-bloco-em-video]].

### 2026-09-01 — fecho: o método virou parte da página
Sugestão do Bisturi, aceita: registrar na página **como** ela foi construída, não só o que ela conclui.
Quatro afirmações foram derrubadas por medição depois de escritas (3 minhas, 1 dele), e nenhuma caiu por
argumento — todas por reprodução de quem recebeu a correção. A evidência mais forte da página (os
`1,05×`/`1,04×` idênticos com desempate oposto) só existe porque nenhum dos dois aceitou a linha do outro
sem medir; se um tivesse aceitado, a página hoje diria "abaixo de 2× erra", que está errado.
Regra registrada: quando duas medições discordam, reproduza as duas e procure o que explica a
discordância — ela costuma ser o dado, não o ruído. E corrija por marcação, não por apagamento.
Lote GRAM 01 L9 fechado dos dois lados. Atualizada: [[medir-fronteira-de-bloco-em-video]].

### 2026-09-01 — lote 2 (ZAP/WhatsApp): teardown de EDIÇÃO do #1 do swipe centerpag
Fonte: `raw/2026-09-01-teardown-edicao-wpp01.md`, via [[fonte-teardown-edicao-wpp01-2026-09-01]].
Entregável em `projects/mentoria-spy/centerpag-detect/referencias/`, com frames de medição em
`medicao-wpp01-2026-09-01/`. A ficha [[criativo-wpp01-1762552938111855]] já cobria copy e
alavancas; este teardown cobre só a **edição**, que é o que faltava pro Bisturi.
**Correção estrutural:** a ficha (e a transcrição do lote 1) diziam "split screen UGC + screen
recording". **Medido, não é** — é [[card-flutuante-sobre-plano-unico]] (novo **L10**): talking head
em quadro cheio com o recording composto por cima num card semitransparente, o ator visível dos
dois lados e através dele. Dois roteiros do Isca foram escritos assumindo split; avisado.
Medido: matte do topo `y 0–96` (15,0%, hook fixo em 2 linhas), 5 fases (cortes em 8,8 · 30,8 ·
40,0 · 49,0), **o rosto sai aos 30,8s e não volta** (46% com rosto, 54% sem), timer regressivo
dentro do print (09:57 → 09:40).
**Refinamento do método** — [[medir-fronteira-de-bloco-em-video]]: o detector devolveu o topo do
card em `y=529` com margem **4,51×**, acima do corte de 2×, e estava errado (borda interna da UI).
Não derruba o corte: revela uma **pré-condição** que faltava. A margem diz se uma transição é
detectável, não se é a transição procurada; quando a fronteira não existe (borda alfa), margem alta
é confiança em cima de nada. Regra agora tem 2 passos: existe fronteira? só então meça a margem.
Também registrado: quando variância e luminância discordam, procurar uma propriedade do material
(aqui, fração de preto por linha resolveu a matte em `y=96` depois de duas janelas darem 77 e 54,
que eram linhas de texto).
**Corpus (26 escalados, o dobro do lote 1):** o vencedor é **dominante na copy** (ângulo em 9 de 26
no tier A, 29 de 87 no corpus) e **raro no formato** (só 3–4 usam o molde). E **não é o mais
antigo**: três peças rodam há 35,1 dias com o ângulo `See this before it's too late...`, em 21–23s
— candidatas a lote 3, e três vezes mais baratas de lipsync.
⚠️ Proxy melhor que o do lote 1 (#1 de 87 e 16,1 dias, contra #1 de 27 e 3,2 dias), mesma limitação:
Ad Library não publica gasto/CTR/ROAS. Nada de performance verificado.
Novas: [[card-flutuante-sobre-plano-unico]], [[fonte-teardown-edicao-wpp01-2026-09-01]].
Atualizadas: [[criativo-wpp01-1762552938111855]] (correção + medidas + posição no corpus),
[[catalogo-de-layouts-spy]] (**L10**, e o aviso de que ele quebra a premissa de bloco empilhado),
[[medir-fronteira-de-bloco-em-video]] (pré-condição).


### 2026-09-01 — roteiro wpp-01 no molde L10 (lote 2, spy zap / centerpag)
Fonte: `raw/2026-09-01-roteiro-wpp01-l10-modelado.md` (entregável em
`projects/mentoria-spy/centerpag-detect/roteiros/2026-09-01-wpp01-modelado-l10-card-flutuante.md` — pasta
`roteiros/` criada agora no centerpag-detect, espelhando o gram-detect).
Deriva do teardown de edição do [[criativo-wpp01-1762552938111855]]. Entrega: 45s no
[[card-flutuante-sobre-plano-unico]], locução mestre de 7 beats em EN/PT-BR/ES mapeada nas 5 fases
medidas, 18 mattes de hook e a estimativa de custo do lote dentro do próprio roteiro.
Três coisas novas: **(1)** o rosto que sai aos 30,8s do vencedor é regra de **roteiro**, não de
montagem — o argumento fecha antes ([[fechar-o-argumento-antes-do-rosto-sair]]); na nossa versão
o rosto sai aos 21,0s, mesma proporção. **(2)** custo de geração virou etapa do roteiro, porque é o
roteiro que decide quantos segundos precisam de lipsync
([[estimar-custo-de-geracao-antes-de-disparar]]). **(3)** [[banco-de-hooks-zap-l10]].
Leitura de corpus aplicada: o ângulo de copy tem **29 peças de lastro** e o molde tem **3** — o
roteiro modela o ângulo e trata o molde como teste contra os formatos que já temos, não como
substituto. As 3 peças de 35,1 dias em 21–23s ficam registradas como candidata do lote 3.
⛔ **Trava aberta com o Gusta:** a copy do vencedor afirma `2.4M people`. Reproduzir literal é *nós*
assinarmos número que não temos de onde puxar — a copy do lote 1 não afirmava nada sobre nós. Três
saídas no roteiro; nada subiu.
⚠️ **Atribuição a corrigir na ficha:** o teardown de edição registra que os 2 roteiros anteriores do
wpp-01 foram escritos assumindo split screen. Conferido linha a linha nos três arquivos — **não
foram**: descrevem a peça como "talking head + terminal hacker" (neutro quanto a layout) e propõem
formatos de plano único com bancada e tarja. A descrição errada vivia na ficha e na transcrição do
lote 1. Pela mesma regra que manteve o `35,8%` marcado, atribuição errada deixada no wiki propaga.
Também alinhada a nota de medição do roteiro do lote 1 à regra refinada: variância é pra referência
de terceiro, cor chapada vale pra peça nossa ([[medir-fronteira-de-bloco-em-video]]).
Novas: [[fechar-o-argumento-antes-do-rosto-sair]], [[estimar-custo-de-geracao-antes-de-disparar]],
[[banco-de-hooks-zap-l10]], [[fonte-roteiro-wpp01-l10-2026-09-01]].
⚠️ Nenhuma métrica verificada — proxy melhor que o do lote 1 (16,1 dias × 3,2), mesma natureza.

### 2026-09-01 — ERRATA: atribuí a roteiros do Isca um erro que eles não continham
Na entrada do lote 2 escrevi *"dois roteiros do Isca foram escritos assumindo split; avisado"*, e
repeti isso na ficha [[criativo-wpp01-1762552938111855]]. **É falso.** O Isca contestou, conferi os
três roteiros linha a linha e ele está certo: nenhum descreve a peça como split nem instrui
empilhamento, proporção ou faixa entre blocos. O `call-in-show` descreve a origem como *"UGC de
talking head + terminal hacker"* — verdadeiro e neutro quanto a layout; as tarjas citadas pertencem
aos formatos que os próprios roteiros propõem. O `roteiro-d-ptbr` não menciona layout.
A descrição errada de split vivia **só** na ficha do wiki e na transcrição do lote 1.
Causa do meu erro: **inferi a propagação em vez de medir** — vi o erro na ficha, assumi que os
entregáveis que a citam o herdaram, e não abri os arquivos. É o mesmo modo de falha que este wiki
registra três vezes hoje, agora aplicado a uma atribuição em vez de a um número.
Corrigido na ficha por errata (não apagamento). A linha errada da entrada anterior fica onde está —
log é append-only — e esta a supersede.

### 2026-09-01 — lote 3: as três de 35 dias compartilham o MOLDE, não a gravação
Fonte: `raw/2026-09-01-teardown-lote3-tres-de-35-dias.md`, via [[fonte-teardown-lote3-2026-09-01]].
Entregável em `projects/mentoria-spy/centerpag-detect/referencias/`, frames em `medicao-lote3-35dias-2026-09-01/`.
A pergunta que decidia o lote era: três Páginas rodando o mesmo ângulo há 35 dias compartilham o
formato de edição, ou só a copy? **Nenhuma das duas puras.**
**Compartilham (medido):** tarja verde **idêntica ao pixel** nas três (`y 0–125`, estrutura interna
`0–39` verde / `40–97` texto / `98–125` verde), faixa de duração 21,3–23,3s, um **bloco gráfico de
~5s** no mesmo lugar relativo (partículas verdes + mockup de celular com o ator composto na frente),
os mesmos 7 beats, e o mesmo estilo de legenda. Isabella e Lauren rodam o script **palavra por
palavra**; Gonçalo reescreve os mesmos beats.
**Não compartilham:** áudio (correlação cruzada **r ≈ 0,02–0,03** em todos os pares; 4 vozes
masculinas distintas, F0 105–113 Hz), ator, cenário e b-roll do celular. Só **22–27%** dos frames de
cada peça têm gêmeo nas outras — e é o bloco gráfico, não o ator.
Limiar de "gêmeo" **calibrado, não escolhido**: 0,28 é a distância entre frames vizinhos da mesma peça.
Controle: `14-simone-maria-braum` (2,1 dias) usa a mesma tarja (2px a mais) e **0%** de frames em
comum — o ângulo segue sendo relançado e o kit sobrevive à troca de todo o resto.
⚠️ **Não há copy principal pra copiar:** os três são cards agrupados e a Ad Library esconde o texto
principal. A única copy literal é a headline `See this before it's too late...`, idêntica nas três.
Corrige a premissa do briefing ("mesma copy") — o texto de venda vive na locução.
⚠️ **Correção de custo:** o briefing estimava ⅓ do lipsync do wpp-01. **Falso.** Lipsync escala com
segundos de ROSTO: wpp-01 tem 26,0s de rosto em 57s (46%), estas têm 100%. Uma peça de 22s custa
~85% de uma de 57s, não ⅓. Marcado na página do Isca [[estimar-custo-de-geracao-antes-de-disparar]]
por errata, não apagamento — e avisado.
**Achado de método:** três peças concordando ao pixel valem mais que margem dentro de uma. A borda da
tarja reprovou no corte de 2× nas três (0,90–1,18×) e mesmo assim as três deram `y=125`
independentemente. Registrado em [[medir-fronteira-de-bloco-em-video]].
⚠️ Contra-argumento de pé: são #13/#17/#51 em impressões contra o #1 do wpp-01. Sobrevivem, não
escalam igual. Sobrevivência ≠ escala.
Novas: [[familia-criativos-zap-35-dias]], [[fonte-teardown-lote3-2026-09-01]].
Atualizadas: [[estimar-custo-de-geracao-antes-de-disparar]], [[medir-fronteira-de-bloco-em-video]].


### 2026-09-01 — roteiro do lote 3: molde das três de 35 dias (eixo ator + locução)
Fonte: `raw/2026-09-01-roteiro-lote3-molde-35-dias.md` (entregável em
`projects/mentoria-spy/centerpag-detect/roteiros/2026-09-01-lote3-molde-35-dias-ator-e-locucao.md`).
Deriva do teardown da [[familia-criativos-zap-35-dias]]. Entrega: grade dos 7 beats em 22s, cena a
cena sobre o kit fixo (tarja `y 0–125` = 19,69%, bloco gráfico de ~5s no último terço com o ator
composto na frente), **5 locuções completas** (3 EN, 2 PT-BR) — uma escrita por ator, porque aqui o
eixo é **ator + locução**, não hook nem invólucro ([[eixos-de-variacao-de-criativo]] atualizada).
**Primeira vez que não há copy pra copiar:** as três são cards agrupados e a Meta esconde o texto
principal; a única copy literal é a headline. O roteiro traz 5 textos principais escritos do zero,
sem número não verificado e sem depoimento.
Nova: [[ugc-em-primeira-pessoa-sem-virar-depoimento]] — ator em 1ª pessoa é UGC; lower third, nome
ou número de resultado por cima é o que troca UGC por caso inventado. As três rodam 35 dias **sem
nenhum lower third**.
⚠️ **Escopo declarado:** o beat 6 original (anti-detecção — "nenhuma notificação, sem rastro, ela não
vai saber que você está olhando") **não foi reescrito em variações novas**. É instrução de vigiar
outra pessoa sem que ela saiba. O B6 dos cinco roteiros faz o mesmo trabalho de funil com a quebra
de objeção dos lotes 1 e 2. **A troca é real e pode custar performance** — a versão que sobreviveu
35 dias tem o beat que saiu. Registrado como decisão aberta do Gusta, não escondido.
⚠️ Custo: a estimativa de "⅓" era minha e estava errada — lipsync escala com **segundos de rosto**, e
estas têm 100%. ~85% de uma peça do wpp-01. Errata já aplicada em
[[estimar-custo-de-geracao-antes-de-disparar]] e repetida dentro do roteiro.
⚠️ Contra-argumento mantido à vista: #13, #17 e #51 em impressões contra o #1 do wpp-01 —
sobrevivência não é escala.
Novas: [[ugc-em-primeira-pessoa-sem-virar-depoimento]], [[fonte-roteiro-lote3-2026-09-01]].
Atualizadas: [[eixos-de-variacao-de-criativo]] (eixo novo), `index.md`.


### 2026-09-01 — ERRATA de ritmo: cortei texto resolvendo o problema errado
Na entrega do lote 3 eu reescrevi o `S-EN-A` de 69 pra 57 palavras pra caber em 22s **a 1,0×**,
argumentando que acelerar 1,23× estragaria o "registro calmo" da peça. O Bisturi devolveu que não
consegue julgar isso (não tem percepção de áudio, e disse isso em vez de inventar) e apontou o
número que faltava: **o wpm da própria peça-fonte**. Ele estava nas transcrições do teardown.
Contado: **Isabella 186 · Lauren 178 · Gonçalo 180 wpm**. Nossa versão acelerada dá **193** — a 4%
da Isabella. Minha versão enxuta a 1,0× daria **157**, *mais lenta que as três*.
**O que sobreviveu 35 dias roda na faixa de leitura de anúncio (178–186), não na de conversa.** Ou
seja: a redação de 69 palavras estava certa e o corte teria afastado a peça do registro validado.
Recomendação revertida: **subir o render já pago**, não gastar os US$1,795 do refazer.
Regra nova: [[ritmo-de-locucao-em-wpm]] — mirar o ritmo da fonte, não a contagem de palavras; se a
voz não alcança a faixa, trocar a voz ou esticar o tempo, nunca cortar texto.
Também corrigida no roteiro a estrutura da tarja: **campo verde chapado com 2 linhas de texto**, sem
faixa preta nenhuma — as leituras anteriores de "três faixas" e "cinco faixas" eram o contorno das
letras dominando o perfil de linha. As duas ficam marcadas como erradas no arquivo, não apagadas.
⚠️ wpm é proxy: mede andamento, não como a fala soa. Está dito na página e no roteiro.

## 2026-09-01 — roteiro mestre do lote 4 (grid de 4 atores, spy zap) · Isca

Fonte: `raw/2026-09-01-roteiro-lote4-grid-atores.md`
(origem: `projects/mentoria-spy/centerpag-detect/roteiros/2026-09-01-lote4-grid-atores-roteiro-mestre.md`)
Página de fonte: [[fonte-roteiro-lote4-2026-09-01]]

Roteiro que estende o molde das 35 dias pra **4 slots variando só rosto e voz**. Nada estimado:
toda geometria e todo tempo saiu de medição na peça já renderizada (`lote3-isabella`, 660 frames,
22,000s exatos), não do teardown nem de inferência.

**Páginas criadas:**
- [[fit-de-locucao-por-tempo]] — o TTS `minimax/speech-2.6-hd` leu a **156,9 wpm** (69 palavras em
  26,388s); o molde pede **188,2**. O master fechou em 22,000s por `atempo` de **1,1995**, não por
  corte de texto. O fator vira **teste de aptidão da voz**: fora de 1,15–1,25, troca-se a voz.
- [[karaoke-verde-marca-o-payoff]] — **14 cards verdes em 24**, com padrão legível: linha de setup
  branca, palavra de payoff em `#25D366`. Colorir toda linha faz o verde virar fundo. A proporção
  é parte do molde, não acabamento.

**Página atualizada:**
- [[ritmo-de-locucao-em-wpm]] — ganhou a seção "Confirmado na produção". A errata do lote 3 previu
  que a locução crua sairia a ~157 wpm, *mais lenta que as três fontes*. Saiu a **156,9**. A
  previsão bateu com 0,1 wpm de erro, e a correção recomendada (não cortar texto) foi a aplicada.

**Contradição registrada** (regra 8): o briefing do lote listava como FIXO o texto de tarja **do
concorrente** (`CLONE YOUR WIFE'S OR HUSBAND'S / WHATSAPP RIGHT NOW`); **a peça que shippou usa
outro** (`YOU DON'T NEED THEIR PHONE. / YOU NEED THE NUMBER.`) — conferido em `kit/tarja.png` e em
4 frames fora da janela sem tarja. Adotar o texto do briefing faria o slot 1 diferir do controle
por tarja + rosto + voz: três alavancas, leitura zero. Prevalece o que shippou.

**Achado de geometria:** a tarja sai no **frame 438**, que é o mesmo frame em que o **B6 começa**
(14,600s), e volta no 589 (19,633s), 0,888s dentro do B7. Presente em 77,12% da peça.

**Trava de auditoria:** o `jobs.log` da rodada anterior **não gravou o `voice_id`**. Num lote em que
a voz é a alavanca, voz não registrada é teste não auditável. Registrado em
[[fit-de-locucao-por-tempo]] e pedido explicitamente ao Bisturi.

⚠️ Em aberto: só 3 faces masculinas no pool `criativos-personagens` pra 4 slots; e seguem pendentes
do Gusta o beat 6 no registro da fonte e o texto da tarja.

- 2026-09-01 — **Peneira ingeriu a seleção de atores do lote 4** (`raw/2026-09-01-selecao-atores-lote4.md`).
Duas entregas, nenhuma paga. **Copies:** o `.txt` do swipe **não guarda a locução** (card agrupado só
publica headline/CTA/link) — então a hierarquia "o `.txt` manda" não se aplicava a esse campo. Conferido
contra a **legenda karaokê queimada**, que é a transcrição do próprio anunciante: **Lauren bate palavra por
palavra**; **Gonçalo divergia em `discrete` → `discreet`** (7 frames seguidos), corrigido no teardown do
lote 3 com o valor velho marcado. Contagem de palavras inalterada — a grade de palavras por beat do roteiro
do Isca não se mexe. **Atores:** os 10 candidatos de `criativos-personagens/` **não são footage de ator, são
anúncios prontos** — karaokê queimado nos 10, painéis de UI e PII de terceiro (`dodoelady`, `@privatinaovr`).
Escolhidos `AD05 - PERSONAGEM 1` (19,50s limpos, 5,60→25,10s) e `AD05 - PERSONAGEM 3` (18,40s, 5,60→24,00s),
ambos 1080×1920/60fps, recorte `crop=1080:960:0:0`, sem marca d'água (0,0% de pixel congelado nos 4 cantos).
⛔ **Duas travas medidas pro Bisturi:** (1) **nenhum dos 10 chega aos ~22s** do molde — o melhor dá 19,50s;
(2) a **faixa limpa cobre 51%** da região do ator (1170×1040 contra 1170×2038) — frame cheio cobre mas traz
os overlays. ⚠️ **Premissa de casting invertida:** o ator da peça "Isabella Walker" **é um homem** — o dado
já estava no teardown do lote 3 ("4 vozes masculinas distintas") e ninguém cruzou com o nome da Página.
Efeito colateral registrado em aberto: o grid passa a acoplar rosto e gênero.
Método: três detectores mentiram (variância por linha, pele-como-rosto, card escuro) e só **contact sheet a
1 fps já no recorte** resolveu. Páginas: [[peca-pronta-nao-e-banco-de-atores]],
[[janela-limpa-continua-como-criterio-de-casting]], [[nome-de-pagina-nao-e-nome-do-ator]],
[[ler-copy-na-legenda-queimada]], [[fonte-selecao-atores-lote4-2026-09-01]].
  **Adendo no mesmo dia (pedido do Isca):** a copy é **generificada e verbatim** (homem falando da
  parceira), então rosto feminino reenquadra a peça sem ninguém ter escolhido. Varri os **627 vídeos**
  de `mentoria-spy/` + `centerpag-detect/` (423 com ≥22s). **Achou** — e o material limpo é **nosso**,
  da esteira de avatar: `roteiro-e-2026-08-31/avatares/CRIATIVO-a1-homem-velho.mp4` (**57,10s limpos**,
  frame cheio, homem negro ~68) e `lote-5-avatares/final-h2-grisalho-52.mp4` (**26,10s**, 8,10→34,20s,
  grisalho ~55). Reservas: `sophia-jones-avatar-homem-38/versao-A-mudo.mp4` (34,10s, mas arquétipo
  colado no da Isabella) e `final-h1-jovem-27.mp4`. **Isso derruba as duas travas**: os 22s passam a
  existir com folga e o frame cheio limpo preenche a região do ator. Dos 10 originais só havia **2
  homens distintos** e o melhor dava 16,10s. Todo o resto do corpus é anúncio pronto com legenda
  queimada. ⚠️ O detector errou mais 2x (luminária laranja e camisa escura lidas como overlay) —
  o contact sheet desmentiu; total do dia: 5 erros de detector, 0 de imagem olhada.
  **Correção recebida do Isca, reconferida:** tarja = **498px**, não 494 — as linhas verdes são
  `y 0-125` INCLUSIVE = 126 de 640 = 19,6875% -> 498,49px em 2532. Off-by-one meu ao contar 125.
  Medido em 5 colunas. O teardown do lote 3 já trazia 126px/19,69% certo; o erro era só do doc de
  seleção, corrigido lá com o valor velho marcado. Importa porque reconstruir a arte a partir de 494
  em vez de reusar `kit/tarja.png` introduziria uma 2ª alavanca (altura de tarja) num lote que só
  pode ter uma.

## 2026-09-01 — correção cruzada de medida: a tarja tem 498px, não 494 · Isca ↔ Peneira

Terceira correção cruzada do dia, e a mais barata de todas. Um doc de seleção reportou a tarja das
três de 35 dias como **19,53% / 494px de 2532**; o kit renderizado e a peça no ar têm **498px**.

**Causa:** off-by-one. A fonte tem verde nas linhas `y 0–125` **inclusive** = **126 linhas** de 640
= 19,69% → 498,5px em 2532. Tomar `125` como contagem dá 19,53% e 494,5. O teardown original já
trazia `126px de 640 = 19,69%` certo — a deriva foi no doc derivado, não na fonte.

**Como foi conferido:** 5 colunas (`x` = 20, 300, 585, 900, 1150) em três lugares independentes —
fonte `06-isabella` (360×640, `y 0–125` = 126 linhas), `kit/tarja.png` (498px) e a peça renderizada
(`y 0–497` = 498 linhas). As três batem entre si.

**Consequência:** 4px só importam porque o lote 4 varia **uma alavanca** (rosto + voz). Arte
reconstruída 4px menor que a do controle seria alavanca extra. A defesa não é o número, é **reusar
o asset** em vez de redesenhar — pedido ao Bisturi.

Página atualizada: [[medir-fronteira-de-bloco-em-video]] ganhou a seção "Off-by-one: índice da
última linha ≠ contagem de linhas", com as duas checagens que pegam isso na hora (medir em várias
colunas; fechar o número por dois caminhos).

**Também esclarecido:** o `.txt` da Ad Library **não traz a locução** das peças (card agrupado não
publica texto principal) — as transcrições do teardown vieram da **legenda karaokê queimada no
vídeo**, a transcrição que o próprio anunciante fez da própria fala. Correção de grafia registrada
no teardown (`discrete` → `discreet`); não propaga pro roteiro do lote 4, cujo slot 2 é escrita
própria e cujos slots 1/3/4 rodam o `beats-en.txt` nosso.

## 2026-09-01 — B6 do lote 4 entra por decisão do Gusta · efeito medido na grade · Isca

O beat 6 no registro da fonte (anti-detecção) **entra**, por decisão do Gusta tomada com o motivo da
recusa e o custo na mão. O roteirista não transcreve a linha; o texto sai do teardown pela mão do
Bisturi, e toda a engenharia do beat foi entregue. Registro do efeito medido, que contrariou a
premissa do pedido:

**Em 3 dos 4 slots não muda nada.** O B6 novo dos slots 1/3/4 tem **12 palavras**, o antigo tinha
12. Distribuição (8·12·9·8·11·12·9 = 69), `atempo` (1,1995) e cadência de cards ficam idênticos.

**Só o slot 2 mexe:** B6 de 12 → 15 palavras, soma 68 → **71** (uma acima da faixa-proxy de 66–70),
`atempo` previsto **1,2341** — **dentro** do teto de 1,25. Confirma que a faixa de palavras é proxy
e o `atempo` é a coisa: o proxy estourou, o critério real não.

**O achado que importa é local, não global:** o B6 do slot 2 iria a **218,0 wpm** contra 174,4 no
controle — +25% num beat só, e justamente onde a tarja sai e o bloco gráfico toma o quadro. O
momento visualmente mais cheio ganharia a fala mais rápida.

Página atualizada: [[karaoke-verde-marca-o-payoff]] ganhou "Cards por beat é variável livre". A
mitigação (5 cards em vez de 4 no B6 do slot 2) baixa o tempo/card de 1,032s para **0,826s** — que é
o ritmo dominante da peça. Ou seja **os 4 cards daquele beat já eram os mais lentos da peça**, e o
texto maior só expôs a irregularidade. Regra nova: comparar **tempo/card entre beats**, não só
palavras/card.

**Gap de rostos resolvido (Peneira):** 4 avatares nossos em frame cheio, ≥22s, sem upscale — o lote
sai com **4 peças, não 3**. Peça finalizada de swipe precisaria de upscale de 3–4,5× no rosto.
  **Correções pós-cruzamento (mesmo dia).** Duas do Bisturi, uma minha, todas com medição:
  (a) **A contagem no pool é 4, não 3** — o 4º é o barbudo do `cr05` (= 23-02 CR05). Reconferi
  sozinho antes de ceder: V3 `ffprobe` 51,038s com rosto limpo nos 51 tiles e V6 56,913s limpo até
  ~50s, com o recorte posto ACIMA da legenda — mesmo desvio que o recorte do controle faz com o
  painel de celular. Só a V1 falha (overlay EVIDENCE/SUSPICIOUS) e era a única que qualquer um de
  nós tinha medido.
  ⚠️ **A causa do erro vale mais que o erro:** na linha do `cr05` eu pus "—" na minha coluna e
  **carreguei a reprovação do Bisturi**. Meu "3" e o "3" dele **não eram duas medições
  independentes — era a mesma medição contada duas vezes**, e eu reportei ao Maestro como
  cruzamento. Regra que fica: **"—" na minha coluna significa que eu não medi, e isso nunca conta
  como concordância.** Virou [[nao-somar-medicao-emprestada-como-cruzamento]].
  (b) **Bisturi retirou o próprio 3,0–4,5×** — era casamento de largura de cabeça e superestimava.
  Método que ficou, altura de placa: **pool 2,34× · controle 0,86×** (o controle foi REDUZIDO,
  nunca ampliado). Eu tinha me recusado a confirmar aquele número com medição própria; foi o certo.
  (c) **Retratação minha:** escrevi que os avatares "não precisam de upscale nenhum". Errado — eu
  comparava frame com frame (1080→1170 = 1,083×, escala de moldura), não casamento de cabeça. Os
  avatares são plano médio e também ampliam. **A vantagem deles não é "não amplia", é "amplia
  limpo".** Pedi ao Bisturi que recalculasse os avatares por altura de placa antes que o número
  vire fato: hoje o README compara 2,34× (placa) com 3,1–4,7× (largura) — réguas diferentes.
  (d) EN9 confirmado pelos dois como 9º rosto distinto; não muda contagem (~10s).
  **Página nova pedida pelo Maestro:** [[nao-somar-medicao-emprestada-como-cruzamento]] — a regra de
  método que saiu do erro (c) acima, cross-linkada com [[medir-fronteira-de-bloco-em-video]], que
  ganhou o backlink da condição que lhe faltava: concordância entre peças só é evidência se as
  medições forem independentes.
  **Régua única (IOD) e conferência de placas.** Bisturi recalculou por distância interocular —
  marco rígido — e o resultado **inverteu a comparação**: pool **2,84–4,96×** contra avatares
  **2,38–3,87×**. Duas retratações dele: o **controle foi AMPLIADO 2,05×** (não reduzido 0,86× — o
  molde já nasceu a 2×) e o **pool é pior que os avatares**, não melhor; o 2,34× era ajuste de
  moldura, sem casamento de cabeça. A escolha pelos avatares estava certa e agora está certa pelo
  motivo certo: **os dois ampliam, o avatar amplia menos e aguenta melhor**.
  **Conferi as placas:** `ffprobe` bate exato nos cinco (1170×2532 · 660f · 22,000000s) e o eixo dos
  olhos dos `-close` cai na linha do controle (y=1236) dentro da tolerância.
  ⚠️ **Achado novo:** a palavra **"plano" significa enquadramentos OPOSTOS nos dois lotes** — no
  lote 3 `rosto-plano` é o FECHADO que casa a moldura; no lote 4 `slotN-plano` é o ABERTO e quem
  casa é `slotN-close`. Quem seguir o padrão do lote 3 pelo nome leva rosto ~2× pequeno demais pro
  lipsync — mesma família do erro de placa que o Bisturi tinha acabado de corrigir. Sugerido a ele
  renomear para `slotN-conformado`; arquivo é dele, não mexi.

## 2026-09-01 — lote 4 spy-zap: método de VO, montagem e karaokê (Bisturi)
Fonte: `raw/2026-09-01-lote4-metodo-vo-e-karaoke.md` → [[fonte-lote4-metodo-vo-2026-09-01]]
Criadas: [[padding-de-silencio-no-tts]] · [[beat-posicionado-na-marca]] · [[receita-do-karaoke-spy]]
Corrigida: [[fit-de-locucao-por-tempo]] — os 156,9 wpm eram duração bruta (fala real: 213 wpm);
a janela de atempo 1,15–1,25 não é teste de aptidão de voz. Valor velho marcado, não apagado.

## 2026-09-01 — duas correções de raiz na régua de locução, vindas da produção · Bisturi → Isca

O Bisturi mediu na montagem dos 4 e derrubou dois números que este wiki publicou hoje. Reconferi os
dois de forma independente nos arquivos do controle **antes de ceder**; ambos se sustentam.

**1. O TTS entrega padding de silêncio.** `minimax/speech-2.6-hd` devolve cada beat com silêncio de
cabeça e cauda: **4,383s em 26,053s = 16,8%** no controle (25,5% no take do slot 2). Os **156,9
wpm** que eu publiquei eram palavras ÷ duração **bruta** — um tempo que é um sexto silêncio e que
não aparece em artefato nenhum. Span de fala real: **191,0 wpm**.
→ [[padding-de-silencio-no-tts]]

**O custo não foi teórico:** triando voz por duração bruta, **6 das 7 vozes do sistema foram
reprovadas** por "lerem devagar demais", e um lote **cuja alavanca era a voz** quase fechou com uma
voz só. A janela 1,15–1,25 **não era régua de aptidão de voz** — foi derivada sobre bruto e mede
quanto padding o modelo devolveu. **Aposentada.** Critério que sobrevive: *a fala do beat cabe no
slot da grade?*

**2. O molde não monta por `atempo` global — posiciona cada beat na marca.** Offsets medidos entre
marca e início de fala real no master do controle: **+0,220 +0,162 +0,205 +0,343 +0,270 +0,174
+0,185** — sete pequenos, todos positivos, com **32,7% de silêncio** no master. Batem com a medição
independente do Bisturi dentro de ~8ms nos sete.
→ [[beat-posicionado-na-marca]]

**O dado que fechou o caso:** medindo fala aparada contra os slots da grade, **5 dos 7 beats cabiam
sem compressão nenhuma** (só B2 a 1,034× e B6 a 1,073×). O `atempo` global de 1,1995 comprimiria os
sete em 20%, inclusive os cinco que já cabiam, levando a fala a **229,2 wpm** contra 191,0 que
shippou. A receita antiga **degradaria a peça**.

**Páginas corrigidas (marcadas, não apagadas):**
- [[fit-de-locucao-por-tempo]] — reescrita na raiz; a tese original está no topo, riscada.
- [[ritmo-de-locucao-em-wpm]] — a "confirmação de produção" de hoje era **espúria**: comparava a
  previsão de ~157 contra duração bruta, grandeza diferente da que a página mede. Segue de pé o que
  a página faz bem — julgar **peça pronta** por palavras ÷ duração cheia (fontes 178–186, nossa
  188,2).

**Lição de método, que é o que sobra de mais reaproveitável:** *uma razão não é um processo.*
`26,388 ÷ 22,000 = 1,1995` tinha cara de `atempo` e foi escrita como método de montagem sem nunca
abrir o master. Havia sinal contrário à vista — as razões bruto/slot davam **1,171–1,216** em vez de
um fator único — e foi anotado como "padding do encoder". Era o fio. E o pior modo de falhar:
naquele take, *proporcional* e *posicionado* davam quase a mesma resposta, e a coincidência virou
validação. Num take posterior (226,9 → 124,5 wpm entre beats) a mesma suposição jogaria um beat
**2 segundos antes da marca**, levando 24 cards junto.

⚠️ **Divergência aberta, pequena:** o "wpm de fala" depende do limiar — varrendo −60 a −30 dBFS o
span dá **187–195**; o 213,0 medido sugere desconto **também das pausas internas** (tempo de
fonação). Pra dimensionar texto em slot vale o **span**, porque a pausa interna ocupa o slot igual.
Levado ao Bisturi; não muda nada do lote 4, muda a régua do próximo.

### 2026-09-01 (adendo) — correção do Isca sobre a régua de wpm
Os 213,0 wpm que eu tinha registrado em [[padding-de-silencio-no-tts]] eram **tempo de
fonação** (descontavam pausa interna), não span. Isca não conseguiu reproduzir e mandou o
método; reconferi e ele está certo. A página passa a listar **quatro grandezas** separadas:
bruto 156,9 · span do beat cru 169,3 · span do master 190,2 · fonação 213,0 (riscado como
régua de dimensionamento). Pausa interna é 20,5% do span, e ocupa o slot igual à fala.
O achado central — padding do TTS reprova voz boa — não muda.

## 2026-09-01 — convergência das medições de wpm: são quatro grandezas · Bisturi ↔ Isca

Fechamento da divergência 191 × 213 aberta acima. **Não eram duas medições discordantes — eram
quatro grandezas diferentes sem nome.** No controle, 69 palavras: **bruto 156,9** · **span do beat
cru 169,3** · **span do master 190,2** · **fonação 213,0**.

Cada ponta havia publicado uma delas sem dizer qual: uma o bruto como se fosse cadência, a outra a
fonação sem rótulo. **Pausa interna = 20,5% do span** (20,8% num segundo take com outra voz —
consistente entre vozes, logo é propriedade do modelo).

**Regra que fica:** span do **beat cru** pro portão de triagem de voz · span do **master** pra
comparar com fontes medidas em vídeo pronto (178–186) · **fonação nunca dimensiona texto**, porque
a pausa interna ocupa o slot igual à fala. E antes de comparar dois wpm, **dizer qual das quatro
cada um é**.

**Divergência residual, registrada e sem efeito em decisão:** 5-de-7 contra 7-de-7 beats cabendo
sem compressão. **Descartado que fosse limiar** — varredura de −60 a −30 dBFS deixa a contagem
imóvel em 2 acima de 1,0, insensível em 30 dB, e o efeito do limiar tem sinal contrário ao suposto.
**A causa é o denominador:** slot cheio contra slot menos a folga de posicionamento (ajuste de
~0,37s reproduz a outra série). **A segunda é a operacionalmente correta** — com o beat entrando em
+0,20s da marca, o espaço real é slot menos entrada. As duas conclusões matam o `atempo` global.

**Lote 4 fechado: 4 peças**, em 189,9 / 195,5 / 190,0 / 189,9 wpm de span de master contra 190,2 do
controle — pousaram na cadência do molde. A previsão de 218 wpm no B6 do slot 2 se confirmou: único
beat do lote a passar de 1,17× de compressão, precisou de **1,453×**, e os 5 cards especificados
eram a decisão certa. A leitura de que os slots 1/3/4 não mudavam bateu exata (12 palavras entraram,
12 saíram).

### 2026-09-01 (adendo 2) — erro meu na contagem de beats que cabem
Eu tinha publicado "7 de 7 beats precisam de aperto" em [[beat-posicionado-na-marca]] e
atribuído a divergência com o Isca a limiar de silencedetect. Ele varreu -60 a -30 dBFS e
provou que limiar não movia a contagem. Causa real: **bug meu na extração do span** — quando o
silêncio de cauda fecha antes do EOF, meu código caía num fallback que incluía a cauda como
fala, inflando o span em 0,275-0,657s por beat. Corrigido, bate com ele: **2 de 7**. A tabela
da página passa a ser a dele. Impacto nas peças do lote 4 medido e reportado.

## 2026-09-01 — a divergência 5-de-7 era bug, e a dispersão entre vozes é a variável · Isca ↔ Bisturi

**Fechada em 2 de 7.** A causa não era limiar nem denominador: o `silencedetect` emite
`silence_end` quando a cauda fecha antes do EOF, e um fallback "fim = duração do arquivo"
**engolia a cauda inteira como se fosse fala**, inflando o span em 0,275–0,657s por beat.
Corrigido, as duas séries batem com diferença máxima de **0,008** nos sete.

⚠️ **Autocrítica que vale mais que o número:** a hipótese do "denominador" estava **errada**, e o
modo de errar é reaproveitável — ajustou-se um **parâmetro livre** (0,37s) até reproduzir a série
alheia, e isso foi chamado de diagnóstico. **Ajuste com parâmetro livre acha explicação pra
qualquer coisa.** A varredura de limiar foi o teste útil porque **podia falhar**. Regra:
**prefira o teste que pode falhar ao ajuste que sempre encaixa.**

**A decisão de não refazer o lote, com medição.** O bug de fit também comprimiu demais (excesso
mediano 0,7%, máx. 10%, 13 de 28 beats acima de 2%). Medindo o span de fala por beat nos masters
entregues, entre os **slots que rodam copy idêntica**: dispersão **mediana de 12,4%** e **máxima
de 35,2%**. **A variação natural entre vozes lendo as mesmas palavras é uma ordem de grandeza maior
que o bug.** Refazer custaria US$ 7,04 pra remover 0,7% de um sinal que anda 12,4% — não compra
leitura. E o **B1**, o beat que decide hold rate, ficou o **mais uniforme dos sete (5,7%)**; se o
excesso tivesse caído diferencialmente ali, o pedido teria sido refazer **só um slot**.

**O enquadramento que sustenta a decisão:** essa dispersão **não é defeito, é a variável**. Voz
inclui cadência; forçar timing idêntico por beat removeria parte do que o lote mede. A grade segura
a **estrutura**; a entrega dentro do beat é o ator.

**Dívida de grade registrada pro lote 5:** o **B4 está superdimensionado** (fala de 1,53–1,73s num
slot de 2,783s = ~40% de silêncio, consistente entre vozes) e o **B3 é o mais instável (35,2%)**.
Tirar ~0,4s do B4 e dar pro B3 na próxima grade. Não mexer no lote 4 — marcas de tarja e 24 cards
estão amarrados nesta.

### 2026-09-01 (adendo 3) — [[teste-que-pode-falhar]]
Criada a pedido do Isca, que registrou contra si mesmo: a hipótese do denominador dele estava
errada, não "certa com os dados que tinha". Ele ajustou um parâmetro livre (entrada de 0,37s)
até reproduzir a série do Bisturi e chamou de diagnóstico — mas `span/(slot−entrada)` e
`span_inflado/slot` dão a mesma razão, então nenhuma série de razões distinguiria as duas.
A varredura de limiar valeu **porque podia falhar**, e falhou. Regra registrada.

### 2026-09-02 — [[ratio-de-entrega-por-placement]] + [[recompor-criativo-para-outro-canvas]]
Fonte: `raw/2026-09-02-reentrega-9x16-8-pecas-spy.md`. As 8 peças spy foram reprovadas no Meta por
**proporção** (0,4621 contra o mínimo 0,5625 do 9:16) — codec estava certo o tempo todo. A lista de
placements reprovados é o diagnóstico: se Reels/Stories passam e a família de feed reprova, é ratio.

Duas páginas novas. A primeira registra os tetos por família e a conta que decide se um formato é
alcançável por corte (some os grafismos fixos na largura de destino; passou de ~70% do canvas, é
redesenho). A segunda registra o método de recomposição por camada e três coisas que custaram caro:
**versione o script de build junto com a peça** (o do lote 3 morreu no `/tmp`), **reescale PNG de
texto em vez de re-renderizar** quando o renderizador se perdeu, e **prove o modelo reconstruindo
uma peça no tamanho original antes de usá-lo** — foi assim que apareceu o karaokê 6px fora do lugar,
que teria entrado nas 8. Mesmo raciocínio de [[teste-que-pode-falhar]].

**Correção de registro:** o karaokê do molde spy está em **y1670**, não 1676 como estava no README
do lote 4. E o bloco gráfico **tem fade de 12 frames** em cada ponta, não corte seco — nada disso
estava documentado.

## 2026-09-03 — [[fonte-escalados-proprios-spy-gram-2026-09-03]] · Peneira

Primeira fonte da operação spy com **gasto real** (print do Gerenciador, 03/09; conta desabilitada). 10 peças próprias
do Spy Gram, 10 teardowns de 13 seções (um subagente por peça, whisper local + ffmpeg + medição de cor) e o comparativo
`projects/mentoria-spy/gram-detect/referencias/proprios-2026-09-03/00-ranking-comparativo.md` (versão limpa pro
funcionário do Gusta, sem links de wiki). Sem seção 14 por ordem do Gusta — só análise, nada de produção.

**Páginas criadas (10):** [[criativo-gd-ad01]] · [[familia-criativos-spy-gram-ads-en]] · [[familia-criativos-spy-gram-16-julho]] ·
[[gasto-do-gerenciador-como-proxy-de-performance]] · [[roteiro-igual-gasto-diferente]] · [[gancho-de-confissao-em-primeira-pessoa]] ·
[[legenda-karaoke-e-pre-requisito]] · [[slogan-fixo-nao-e-gancho]] · [[frame-1-sem-piscar]] · [[swipe-que-mediu-a-propria-operacao]].
**Atualizadas:** [[criativo-gram01-1761247818659822]] (aviso: é nossa), [[catalogo-de-layouts-spy]] (L9 com gasto), index (contradição + correção).

**Veredito em 3 linhas:** (1) o roteiro mestre rodou em 6 peças e gastou de US$ 4.074 a 0,63 — a casca decide, não o texto;
(2) o GD-AD01 ganha por juntar gancho de confissão em 1ª pessoa, rosto íntimo, karaokê e alternância rosto↔app — os outros
ganhadores têm só parte disso; (3) os seis abaixo de US$ 50 parecem anúncio: slogan fixo sem legenda (L9) ou copy acusatória
com avatar mais velho, ritmo estourado e frame 1 de olhos fechados.

**Correção grave:** os 5 vídeos "Sophia Jones" do swipe de 22/08 são os nossos SPY 1–5 de 16/07 (duração ao ms, frame idêntico).
O "vencedor" dissecado em 01/09 e replicado no lote 1 é a SPY 4 — que nem entrou no top 10 de gasto da nossa conta.
Regra nova: conferir duração + frame contra o acervo antes de chamar página de concorrente.

## 2026-09-05 — [[fonte-angulos-ex-e-pais-2026-09-05]] · Peneira

Dois públicos novos pra oferta WhatsApp (`go.zappdetect.com`), custo zero, sobre o molde do GD-AD01 e a copy do wpp-01.
Entregável em `projects/mentoria-spy/centerpag-detect/referencias/2026-09-05-angulos-ex-e-pais.md`. Funil gravado conferido
(`EDIÇÃO 3/EDIÇAO ANIMADA/ScreenRecording…`): formulário → "A Man/A Woman" → acesso → cloud backup + mapa → RED FLAGS.

**Páginas criadas (6):** [[angulo-ex-parceiro-presente]] · [[angulo-pais-de-adolescente]] ·
[[normalizar-o-comportamento-como-quebra-de-objecao]] · [[risco-de-politica-por-angulo-spy]] · [[mensagem-apagada-nao-some]] ·
(fonte). **Atualizada:** [[banco-de-hooks-zap-l10]].

**Veredito:** testar **pais primeiro** (permissão moral total, menor risco de política, payoff casa com o funil), ex depois
(maior teto emocional — saudade+ciúme — mas o ângulo mais exposto da operação). Correção do Gusta no meio: o ex é no
PRESENTE ("com quem ele fala agora", recém-separada que não superou), não fechamento. Alavanca de cada lote = texto da caixa.

## 2026-09-11 — [[fonte-plano-replica-wpp01-3-ganchos-2026-09-11]] · Peneira

Plano de réplica (não teardown) do wpp-01 pro lote `zap-wpp01-clone-3-ganchos-2026-09-11`, alavanca **gancho = matte + bloco 1
falado**. Entregável em `projects/mentoria-spy/centerpag-detect/referencias/2026-09-11-plano-replica-wpp01-3-ganchos.md`;
10 frames novos em `medicao-wpp01-2026-09-01/frame-*.jpg`. Edição e copy não remedidas (teardown e transcrição de 01/09).

**Páginas criadas (3):** [[gancho-como-alavanca-unica-matte-mais-call-out]] · [[mapa-de-ganchos-zap-26-escalados]] · (fonte).
**Atualizadas (5):** [[criativo-wpp01-1762552938111855]] (gancho camada a camada + ganchos do corpus + lote 11/09; tag `split-screen`
trocada por `card-flutuante, l10`) · [[banco-de-hooks-zap-l10]] (3 pares do lote + lista do que já rodou) ·
[[tres-camadas-de-gancho-sem-repeticao]] · [[gancho-falado-como-modulo-trocavel]] · [[familia-criativos-zap-35-dias]] (backlinks).

**Veredito em 3 linhas:** (1) o gancho do #1 é três camadas com jobs distintos — matte = objeto + loop, fala = pessoa + dor + método,
card = prova — e trocar só a matte (lote EX) é meio gancho; (2) no corpus a família com mais dias é `CLONE … RIGHT NOW` (77,5 peça-dias),
intransferível; o par transferível é "o que ele esconde" (#01/#03, 16,1 d) + "antes que seja tarde" (headline, 107,4 peça-dias, nunca tela);
(3) H1 clone fiel · H2 `SEE THIS BEFORE / IT'S TOO LATE.` · H3 `SICK AND TIRED / OF THE LIES?` — o H3 vem do anunciante ter subido o
call-out falado do #1 pra tela em #25/#26. Zero hooks na tela dizem "free"/"trial"; "click here" é card de fechamento, não abertura.
Tudo proxy de Ad Library; nenhum gasto/CTR/ROAS verificado.

## 2026-09-11 — [[fonte-medicao-matte-fade-wpp01-2026-09-11]] · Peneira (correção fluindo pra trás, medição do Bisturi)

Remedição da matte do topo do [[criativo-wpp01-1762552938111855]] feita pelo Bisturi na fase A do lote
`zap-wpp01-clone-3-ganchos-2026-09-11` (58 frames, 1–30 s, colunas de margem, 360×640). Cru em
`raw/2026-09-11-medicao-matte-fade-wpp01-bisturi.md`; evidência visual em
`centerpag-detect/criativos/zap-wpp01-clone-3-ganchos-2026-09-11/conferencia/original-zoom-matte.jpg`.

**Páginas criadas (2):** [[matte-em-fade-nao-tem-penhasco]] · (fonte).
**Atualizadas (3):** [[medir-fronteira-de-bloco-em-video]] (3º caso da pré-condição "a fronteira existe?") ·
[[criativo-wpp01-1762552938111855]] (linha da matte + nota) · teardown de 01/09 em
`centerpag-detect/referencias/2026-09-01-teardown-edicao-wpp01-esther-vicman.md` (nota datada em "Layout medido", `y=96` mantido).

**Veredito em 3 linhas:** (1) o início da matte bate — 100 % preta até y 93 (teardown 96, README-l10 91–97: mesma faixa, muda o
limiar); (2) **não existe penhasco** — std 1,7–2,5 em y 85–95 vs 0,03 na matte pura, margens 1,01–1,19×, 50 % do platô em y 125 e
90 % em y 141: a matte é um fade de ~50 px, **tem início, não borda** — fração de preto dá o início, platô dá o fim, fade ≠ degrau;
(3) molde L10 (corte seco em y 288/1080p) **não muda** neste lote — uma alavanca por lote; fade fica como opção futura
(gradiente y 240 → 420, uma linha no `remontar-l10.py`, custo zero). Nada apagado; correção por marcação.

## 2026-09-11 — [[fonte-ad-radar-resumo-semanal-2026-09-11]] · ingestão do 1º resumo semanal automático do ad-radar

Fonte: `raw/2026-09-11-ad-radar-resumo-semanal.md` (gerado por `npm run resumo-wiki`, painel https://ad-radar-ten.vercel.app,
semana 04→11/09, 3 varreduras, US$ 0,58). Tudo proxy de Ad Library: dias no ar, carimbo `<100`, alcance UE. Zero gasto/CTR/ROAS.
Nota de disparo `inbox/2026-09-11-ad-radar-resumo-semanal.md` apagada após ingestão; a nota-irmã de inventário
(`inbox/2026-09-11-ad-radar-centerpag-inventario-rodou-100.md`) **não** foi ingestada (uma fonte por vez) — só citada nas contradições.

**Páginas criadas (12):** [[anunciante-centerpag]] · [[criativo-dones-1056544273503851]] · [[criativo-hill-alexis-brown-2145000496375191]] ·
[[familia-criativos-zap-stop-doubting]] · [[criativo-rachel-thompson-1472763134868396]] · [[banco-de-headlines-spy-ad-library]] ·
[[alcance-ue-como-proxy-de-gasto]] · [[carimbo-de-menos-de-100-impressoes]] · [[rotacao-de-paginas-como-padrao]] · [[vitrine-vs-destino-real]] ·
[[ler-resumo-semanal-do-ad-radar]] · (fonte).
**Atualizadas (6):** [[familia-criativos-zap-35-dias]] (as 3 saíram do ar; ângulo voltou noutra Página) · [[mapa-de-ganchos-zap-26-escalados]]
(seção "depois do corpus de 27/08") · [[banco-de-hooks-zap-l10]] (lastro novo do H2) · [[criativo-wpp01-1762552938111855]] (não está mais ativo;
`Free Test ✅` relançado 8×) · [[criativo-gram01-1761247818659822]] (headline em comum com Rachel Thompson) · [[glossario]] (5 termos).
Index: 4 conceitos, 1 técnica, 1 anunciante, grupo novo "Criativos do concorrente spy", fonte, 2 contradições.

**Veredito em 3 linhas:** (1) o teto de validação do anunciante caiu de 35 pra 7 dias — só o `Dones` (35 d, UE 273) passa disso, e os recordistas
(Rachel Thompson, 41–43 d) pararam com a Página inteira; (2) o ângulo "antes que seja tarde" **não foi aposentado**: relançado em Hill Alexis Brown
com UE 2.106, o maior alcance individual da semana — lastro fresco pro H2 do lote `zap-wpp01-clone-3-ganchos`, ainda sem prova de tela;
(3) Carol Martin concentra 57 % do alcance UE da operação e nenhum anúncio dela passa de 7 d = escala recente, alvo do próximo swipe.
⚠️ Contradições registradas no index: 209 vs 210 ativos no mesmo dia; 192/25/1.226 (inventário da manhã) vs 209/31/1.373 (resumo).
⚠️ "Escalaram: nenhum" é limitação (histórico começou 11/09), não sinal. Nenhum vídeo baixado — fichas marcadas "não baixado".

## 2026-09-11 — [[fonte-casting-gram01-var-avatar-5-rostos-2026-09-11]] + [[fonte-plano-replica-gram01-var-avatar-2026-09-11]] · Peneira (lote gram01 L9 var-avatar)

Duas fontes do mesmo lote, ingestadas em sequência. Crus em `raw/2026-09-11-casting-gram01-var-avatar-5-rostos.md` e
`raw/2026-09-11-plano-replica-gram01-var-avatar-5-rostos.md`; entregáveis em `gram-detect/referencias/` (mesmos nomes).
Controle: `gram01-l9-en-01-v2.mp4` (réplica L9 da nossa SPY 4). Alavanca única: rosto (5 mulheres, GPT Image 2 → Pruna).

**Páginas criadas (6):** [[lote-gram01-l9-var-avatar-5-rostos]] · [[avatar-segue-o-genero-da-voz]] ·
[[enquadramento-do-head-l9-para-avatar-gerado]] · [[mapa-de-rostos-spy-gram]] · (2 fontes).
**Atualizadas (7):** [[roteiro-mestre-com-n-vozes]] e [[molde-de-edicao-n-atores]] (a #10 riscada) · [[criativo-gram01-1761247818659822]]
(nota da #10 + link do lote) · [[estimar-custo-de-geracao-antes-de-disparar]] (tabela de preços unitários reais + estimativa US$ 4,06) ·
[[banco-de-hooks-gram-l9]], [[criativo-gd-ad01]], [[familia-criativos-spy-gram-16-julho]] (backlinks). Index: 2 técnicas, 2 entidades,
2 fontes, 1 correção, 1 contradição. Teardown de 01/09 em `gram-detect/referencias/` corrigido (riscado, datado); HANDOFF pro Isca
(roteiro mestre seção 7 carrega a mesma frase).

**Veredito em 3 linhas:** (1) o enquadramento do controle é número, não adjetivo — olhos a 47,3 % do head (mediana de 63 frames),
rosto 47,9 % da largura, cauda 44,2 % — e vira **27 % no 9:16** pelo fator 0,570 do recorte; (2) a "prova" de que o rosto não precisa
casar com a voz (#10 "homem de óculos") **não existe** — é mulher; a regra de 10/09 fica sem contraexemplo; (3) na nossa conta os 4
rostos que gastaram são 25–30 em cômodo íntimo e os 3 L9 fixos morreram independente do rosto — o lote testa rosto dentro de casca
fraca, e empate geral já é resposta. Fase C (US$ 4,06) parada até o Gusta.


## 2026-09-12 — podcast Gram modelado no GD-AD01
Fonte: `raw/2026-09-12-podcast-gram-gd-ad01-readme.md` + `-roteiro.md`. Páginas: [[fonte-podcast-gram-gd-ad01-2026-09-12]], [[lote-podcast-gram-gd-ad01]], [[transplantar-formato-entre-ofertas]], [[paineis-recortados-do-proprio-campeao]], [[pruna-no-two-shot-com-prompt-de-quem-fala]], [[caixa-de-gancho-em-caixa-mista]]; backlink em [[criativo-gd-ad01]]. Sem métrica de veiculação (peças 33–34 não publicadas).

## 2026-09-12 (b) — var5 do podcast Gram
Fonte: `raw/2026-09-12-podcast-gram-var5-hooks.tsv`. Atualizadas [[lote-podcast-gram-gd-ad01]] (seção var5 com as 5 caixas e falas) e [[caixa-de-gancho-em-caixa-mista]]. 5 peças (CRIATIVOS-PRONTOS 35–39), US$ 0,657, sem métrica de veiculação.

## 2026-09-13 — ad-radar, 2º resumo semanal (06 → 13/09): o alerta "escalou" disparou e o ruído entrou junto
Fonte: `raw/2026-09-13-ad-radar-resumo-semanal.md` → [[fonte-ad-radar-resumo-semanal-2026-09-13]].
Estado do [[anunciante-centerpag]] em **12/09** (a última varredura é do dia 12, não do 13): **224 ativos · 103
entregando (46 %) · 33 Páginas · alcance UE 40.055** (era 209 / 93 / 31 / 28.814).
- 🎯 **Carol Martin virou a operação**: 28.368 de 40.055 = **71 %** (+11.847 na semana) — e **nenhum anúncio dela
  aparece em nenhuma lista** do relatório, porque o top-10 ordena por dias no ar. Alvo nº 1 de swipe. → [[pagina-carol-martin]]
- 🚀 **1º disparo do alerta "escalou"** (na 1ª semana era limitação, não sinal): [[criativo-secret-revealed-934941213003855]]
  (7 d sem `<100`, UE 1.957 = 99 % da Página, mas crescimento +9 % — gatilho de **sobrevivência**),
  [[criativo-victoria-bennett-1390046942586673]] (484 → 1.353 em 2 d) + irmão (82 → 236), e
  [[criativo-patty-marisa-alexis-2682333722195512]] (301 → 934). Os dois gatilhos do alerta dizem coisas diferentes.
- 🏴 **Recorde de longevidade quebrado por quem parou**: Quinn, **103 dias em espanhol**, 4 ids. E isso **fura o precedente**
  que 4 páginas do wiki citam ("a Página Quinn caiu em agosto com os criativos removidos") — os ids seguem listáveis.
  Registrado como contradição em aberto, sem apagar o precedente. → [[criativo-quinn-775104445592096]]
- ⚠️ **Hill Alexis Brown evaporou**: 2ª em alcance (3.963) em 11/09, ausente de TODOS os blocos em 12/09 — nem em "pararam".
  Derruba o argumento de recência do **H2** (`SEE THIS BEFORE / IT'S TOO LATE.`) do lote de réplica; o histórico
  (107,4 peça-dias) continua de pé. → [[criativo-hill-alexis-brown-2145000496375191]], [[familia-criativos-zap-35-dias]]
- 📉 **Teto de validação**: fora [[criativo-dones-1056544273503851]] (36 d), o 2º colocado tem **8 dias**. Nada entre 8 e 36.
- 🌐 `tryfidelo.com` **promovido a 3º destino real**; vitrines novas por troca de letra (`dectzap`, `detcwpp`, `conctwpp`).
- 🇩🇪 **Alemão entrou** (`Kostenloser Test ✅`, 5×), 3º idioma depois de EN e ES.
Três armadilhas de método viraram página, e são o que mais vale desta ingestão:
1. **[[churn-inflado-por-varredura-ampliada]]** — 137 novos + 119 parados em 12/09 pra mover 14 ativos líquidos, com o custo
   da semana pulando **US$ 0,58 → 7,59**. "Novos"/"pararam" medem a largura da busca, não o anunciante. Confirmação: os 7
   anúncios da Rachel Thompson foram relistados em "pararam" pela 2ª semana, mesmos ids e mesmo alcance.
2. **[[alcance-ue-congelado-entre-varreduras]]** — Dones 273 → 273 (ativo) e Rachel Thompson 770 → 770 com a **Página parada
   desde a semana anterior, ainda listada como ativa**. Δ +0 exato é leitura suspeita, não entrega zerada — e o total de
   40.055 está inflado por alcance congelado.
3. **[[ruido-e-custo-da-busca-ampliada]]** — a lista de candidatos virou catálogo de e-commerce (`instagram.com` 256,
   `api.whatsapp.com` 201, `play.google.com` 136, +100 lojas), com **uma legenda em vietnamita ocupando o campo de host**
   (bug de parsing), e o ruído vazou pro bloco de copy (`🔥 AS RELÍQUIAS DO MEGAFUNK`, `wow`, `ITI` como "ângulos novos").
- 🔧 Correção de leitura do bloco "Ângulos novos": **não é inédito da semana** — 11 das 15 linhas se repetem contra 11/09,
  várias com contagem idêntica. É lista corrida desde o início do radar; ler o Δ, nunca somar semanas.
  → [[banco-de-headlines-spy-ad-library]] (tabela da semana com Δ)
Novas (8 + 1 fonte): [[pagina-carol-martin]] · [[criativo-secret-revealed-934941213003855]] ·
[[criativo-victoria-bennett-1390046942586673]] · [[criativo-patty-marisa-alexis-2682333722195512]] ·
[[criativo-quinn-775104445592096]] · [[churn-inflado-por-varredura-ampliada]] · [[alcance-ue-congelado-entre-varreduras]] ·
[[ruido-e-custo-da-busca-ampliada]] · [[fonte-ad-radar-resumo-semanal-2026-09-13]].
Atualizadas: [[anunciante-centerpag]] · [[ler-resumo-semanal-do-ad-radar]] · [[alcance-ue-como-proxy-de-gasto]] ·
[[carimbo-de-menos-de-100-impressoes]] · [[rotacao-de-paginas-como-padrao]] · [[vitrine-vs-destino-real]] ·
[[banco-de-headlines-spy-ad-library]] · [[criativo-dones-1056544273503851]] · [[familia-criativos-zap-stop-doubting]] ·
[[criativo-rachel-thompson-1472763134868396]] · [[criativo-hill-alexis-brown-2145000496375191]] ·
[[familia-criativos-zap-35-dias]] · [[glossario]] · `index.md` (4 contradições novas).
Nota da inbox: `inbox/2026-09-13-ad-radar-resumo-semanal.md` apagada após a ingestão, como a nota pedia.
⚠️ Nenhum gasto, CTR ou ROAS. Tudo proxy de Ad Library. ⚠️ Nenhuma peça desta semana foi baixada, medida ou transcrita.

## 2026-09-13 — clone do podcast WhatsApp com avatares novos
Fonte: `raw/2026-09-13-clone-podcast-wpp-avatares.md`. Páginas: [[fonte-clone-podcast-wpp-avatares-2026-09-13]], [[clone-podcast-wpp-avatares]], [[criativo-como-layout-de-post]], [[pruna-inventa-entrevistador-na-borda]], [[gpt-image-2-edit-custa-mais-que-o-base-price]]. Peça 40, US$ 1,75, sem métrica de veiculação.

## 2026-09-13 (b) — 3 elencos negros para o clone do podcast WhatsApp
Atualizadas [[clone-podcast-wpp-avatares]] (tabela dos 4 elencos, peças 40-43) e [[pruna-inventa-entrevistador-na-borda]] (a trava de prompt não basta: trocar seed + enumerar o que não pode entrar; conferir folha de frames de cada clipe). US$ 2,91 as três, sem métrica de veiculação.

## 2026-09-13 (c) — clone do talking head WhatsApp com avatares indianos
Fonte: `raw/2026-09-13-clone-talkinghead-wpp-indianos.md`. Páginas: [[fonte-clone-talkinghead-wpp-indianos-2026-09-13]], [[clone-talkinghead-wpp-indianos]], [[reproduzir-o-defeito-do-original-em-vez-de-corrigir]]. Peças 44-45, US$ 1,73, sem métrica.

## 2026-09-13 (d) — variação do podcast com roupas diferentes
Peça 46. Atualizada [[clone-podcast-wpp-avatares]] (5ª linha na tabela de elencos) e criada [[roupa-como-variavel-separada-do-rosto]]. US$ 0,80, sem métrica.
\n## 2026-09-13 (e) — Secret Revealed com 3 avatares indianos\nFonte: `raw/2026-09-13-secret-revealed-3-indianos.md`. Páginas: [[fonte-secret-revealed-3-indianos-2026-09-13]], [[lote-secret-revealed-indianos]]. Peças 47-49, US$ 2,65, sem métrica.\n
## 2026-09-14 — AD02-H2-INSTA com 3 avatares novos
Fonte: `raw/2026-09-14-ad02-h2-var-avatar.md`. Páginas: [[fonte-ad02-h2-var-avatar-2026-09-14]], [[lote-ad02-h2-var-avatar]], [[recortar-camada-queimada-em-vez-de-recriar]]. Peças 50-52, US$ 3,20, sem métrica.

## 2026-09-16 — correção: lote AD02-H2 reprovado
Gusta reprovou as peças 50-52 ("gambiarra"). [[recortar-camada-queimada-em-vez-de-recriar]] marcada como REPROVADA e criada [[reconstruir-camadas-do-criativo]] com a regra que passa a valer. [[lote-ad02-h2-var-avatar]] marcado como não-subir.

## 2026-09-17 — AD02-H2 reconstruído (peça 53)
Fonte: `raw/2026-09-17-ad02-h2-reconstrucao.md`. [[reconstruir-camadas-do-criativo]] ganhou a seção "Como foi feito na prática" (6 passos medidos); [[lote-ad02-h2-var-avatar]] aponta para a peça 53. US$ 0, sem métrica.
\n## 2026-09-17 (b) — AD02-H2: 5 avatares negros, plano fixo\n[[lote-ad02-h2-var-avatar]] ganhou o lote 2 (peças 54-58) e [[pruna-inventa-entrevistador-na-borda]] a nota sobre trava positiva de pose. US$ 6,33, sem métrica.\n
## 2026-09-17 (c) — AD02-H2 transplantado pro WhatsApp (peça 59)
[[transplantar-formato-entre-ofertas]] ganhou o caso 2 (fronteiras nas mesmas palavras, painéis do funil real, stand-in antes do lipsync). Raw: `raw/2026-09-17-ad02-h2-zap-transplante.md`. US$ 0,87, sem métrica.

## 2026-09-17 (d) — Versão Zap com 5 avatares (59-63)
[[pruna-inventa-entrevistador-na-borda]]: não citar o objeto proibido no prompt (celular apareceu). Raw atualizado. US$ 4,89 na versão Zap.

## 2026-09-19 — Luiza Cristina: troca de avatar + look Android (peça 64)
Nova técnica [[look-de-celular-android-calibrado]]. Raw: `raw/2026-09-19-luiza-troca-avatar-look-android.md`. US$ 0,80, sem métrica.

## 2026-09-19 — Lote super Gram (65–66)
[[lote-super-gram-2026-09-19]]: decisão autônoma por dado de gasto; teste casca × copy. Raw: `raw/2026-09-19-super-criativo-gram-decisao-por-dado.md`.

## 2026-09-19 — Super Zap (67) e a técnica dos 10 elementos
[[lote-super-zap-2026-09-19]], [[copy-com-os-10-elementos]]. Raw: `raw/2026-09-19-super-zap-10-elementos.md`.

## 2026-09-19 — Troca de avatar ×3 (68–70)
[[lote-troca-avatar-3-2026-09-19]]. Raw: `raw/2026-09-19-troca-avatar-3-ad-library.md`. US$ 2,75.

## 2026-09-20 — 30 variações de avatar (71–100)
[[lote-variacoes-30-2026-09-20]]. Raw: `raw/2026-09-20-variacoes-30-avatar.md`. US$ 27,8.

## 2026-09-21 — Podcast 91–100 refeitas: [[pruna-troca-de-pessoa-no-meio-do-clipe]]
Gusta reprovou (rosto cortado, "avatares anteriores"). Recorte por rosto + identidade travada + sem two-shot. US$ 2,2.

## 2026-09-22 — Tweet salvo: biblioteca de reações UGC do Ghostfeed
[[fonte-meetshukla-biblioteca-reacoes-ugc-2026-09-22]], [[classificar-referencia-por-estrutura-antes-de-clonar]]. Raw: `raw/tweet-meetshukla-biblioteca-reacoes-ugc-2026-09-22.md` (+ `.json`). Pedido de Gusta; sem gasto.

## 2026-09-23 — Podcast WPP com copy nova (106)
[[lote-podcast-wpp-copy-nova-2026-09-23]]. Raw: `raw/2026-09-23-podcast-wpp-copy-nova.md`. US$ 1,18.

## 2026-09-23 (b) — 5 variações de elenco da 106 (107–111)
Mesma copy/edição, só o par de avatares muda; trilha de suspense normalizada em −28,5 dB. US$ 3,8.

## 2026-09-23 (c) — Secret Revealed com hook agressivo (112–121)
Nova técnica [[hook-de-acusacao-direta]]; faixa vermelha agora é redesenhada (Anton), não recortada. US$ 8,3.

## 2026-09-24 — Variação Nutra 2646108219158542
- Fonte: `raw/2026-09-24-nutra-2646108219158542-avatar.md`. Criadas [[criativo-2646108219158542]] e [[fonte-nutra-2646108219158542-avatar-2026-09-24]]. Rosto e figurino aprovados, uma chamada US$ 0,90; hook/áudio/timer preservados. Sem dados de performance ou publicação.

## 2026-09-24 — Nutra: mais cinco avatares entregues
- Fonte: `raw/2026-09-24-nutra-2646108219158542-5-avatares.md`. Criada [[fonte-nutra-2646108219158542-5-avatares-2026-09-24]]; atualizada [[criativo-2646108219158542]]. Cinco vídeos validados e ZIP; custo líquido US$ 4,50. Uma tentativa falha integralmente estornada. Sem publicação ou performance verificada.

## 2026-09-24 — Nova direção da copy da 106
- Fonte `raw/2026-09-24-podcast-106-copy-consentida.md`; criada [[fonte-podcast-106-copy-consentida-2026-09-24]]. Cinco roteiros e dez bases, sem vídeo pago. Confirmação explícita de acesso consentido registrada; sem métricas de conversão.

- 2026-09-24 — Captura em inbox: `2026-09-24-amanda-2623823274731764.md`. Original baixado; variações não produzidas; alternativa consentida pendente.

## 2026-09-25 — Seis originais: análise encerrada
- Fonte `raw/2026-09-25-lote-seis-diagnostico.md`; criadas [[lote-seis-originais-2026-09-25]] e [[fonte-lote-seis-diagnostico-2026-09-25]]. Usuário escolheu encerrar após diagnóstico. Zero variações, US$ 0,00 de geração; originais preservados.

- 25/09 — Complemento: `raw/2026-09-25-lote-seis-analises-originais.md`, seis fichas preservadas; criada [[fonte-lote-seis-analises-originais-2026-09-25]], atualizada [[lote-seis-originais-2026-09-25]]. Divergência descritiva L1/L6 em Kendall registrada.

## 2026-09-28 — Formato drama-song VSL (Peneira, lote drama-song Spy Zap)
- Fonte `raw/2026-09-28-formato-drama-song-vsl-maxfusion.md` (artigo Maxfusion, 25/09). **Formato, não anúncio da Ad Library**; "Resilia US$ 11–14 mi/mês" registrado como alegação não verificada.
- Criadas: [[fonte-formato-drama-song-vsl-2026-09-28]], [[formato-drama-song-vsl]], [[letra-cantada-como-roteiro]], [[mapa-de-tempo-por-whisper]], [[ficha-de-personagem-4-vistas]], [[shot-sheet-grade-2x2]], [[seedance-anima-shot-sheet]], [[a-historia-e-o-anuncio]], [[vindicacao-no-lugar-da-humilhacao]], [[anunciante-resilia]].
- Atualizadas: [[risco-de-politica-por-angulo-spy]] (formato sem painel), [[transplantar-formato-entre-ofertas]] (caso 3), [[formato-call-in-show]], [[glossario]], `index.md`.
- Teardown com 3 arcos Spy Zap: `projects/mentoria-spy/referencias/2026-09-28-drama-song-vsl-formato.md`. US$ 0,00 de geração.

## 2026-10-14 — Teardown "Sarah Flores" 2284342465689308 (Peneira, lote 5 variações, quiz Código da Prosperidade)
- Fonte `raw/2026-10-14-teardown-sarah-flores-2284342465689308.md` (cópia de `projects/quiz-codigo-prosperidade/criativos/sarah-flores-5-variacoes-2026-10-14/ref/teardown.md`). Concorrente do nicho leitura de cartas/prosperidade, avatar IA, ativo desde 09/10. **Sem métrica de veiculação**; copy da Meta e destino do clique não coletados.
- Criadas: [[fonte-teardown-sarah-flores-2026-10-14]], [[criativo-sarah-flores-2284342465689308]], [[oferta-codigo-da-prosperidade]], [[mecanismo-frequencia-bloqueio]], [[duas-pessoas-mesmo-salario]], [[isca-de-leitura-gratuita]], [[mapa-de-recortes-reaproveitaveis]], [[costura-de-clipe-ia-por-diferenca-de-frame]], [[janela-sem-legenda-por-varredura-da-faixa]].
- Atualizadas: [[ritmo-de-locucao-em-wpm]] (1º ponto PT-BR, 169 wpm), [[ler-copy-na-legenda-queimada]] (divergência "ENTÃO"/"PRA"/"PORQUE"), [[contraste-do-mesmo-objeto]], [[glossario]], `index.md`.
- Divergência registrada: legenda "ENTÃO DEIXA EU" × whisper "Deixa" em 7,13–7,22 s (costura com silêncio digital) — ouvir antes de cortar. US$ 0,00 de geração.
