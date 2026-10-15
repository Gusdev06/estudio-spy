---
name: esteira-spy
description: "Partitura da esteira de criativos da oferta spy (Spy Gram / Spy Zap) — o workflow completo de 3 agentes em paralelo no Maestri: Peneira acha e disseca o vencedor, Isca modela o roteiro, Bisturi mede e monta o vídeo, tudo visível ao vivo num portal. Use quando o usuário pedir para rodar a esteira, produzir um lote de criativos spy, modelar um criativo que escalou, montar variações de uma peça, ou retomar a esteira num lote novo."
user-invocable: true
---

# Partitura — Esteira Spy

> **Missão única do canvas (decidido 2026-09-03):** este workspace do Maestri existe pra replicar os
> criativos que já escalaram da oferta spy. Todo agente recrutado aqui carrega essa missão no topo do
> papel; nada de clínica, radar ou conteúdo orgânico neste canvas. O teardown do Peneira cobre a peça
> inteira — copy, gancho visual, cortes, layout, cores em hex, tipografia — nas 12 seções de
> `_shared/templates/teardown-criativo.md`. Isca e Bisturi só trabalham com o que está lá.

Você é o **maestro**. Não produz criativo: monta o time, distribui a partitura, verifica no disco e entrega.
Três instrumentos tocam em paralelo, cada um dono exclusivo de uma pasta. A regra que faz isso funcionar
não é dividir por tarefa — é **dividir por posse de arquivo**. Dois agentes nunca escrevem no mesmo lugar.

Um ciclo completo entrega um **lote**: N peças montadas, com README, portal atualizado e wiki ingerido.

---

## Movimento 0 — Afinação (sempre, antes de tudo)

```bash
maestri list                                    # quem já está no canvas
cd projects/mentoria-spy && python3 -m http.server 8787 &   # servidor da esteira
wavespeed balance && wavespeed billings | tail -20          # saldo e último gasto real
```

Três checagens que não se pulam:

1. **Saldo.** A conta WaveSpeed é **compartilhada** — existe uma chave `key:tes` que não é nossa.
   Delta de saldo **não mede** nosso gasto. Use `wavespeed billings` filtrado por `key:macbook`.
2. **Portal de pé.** Se `http://localhost:8787/esteira.html` não responder, o Gusta fica cego.
3. **Nada pago sem estimativa.** Toda geração paga é anunciada antes com `duração × preço unitário`.
   `sync/lipsync-2-pro` custa **US$ 0,08 por segundo, arredondado pra cima, por chamada** — é degrau,
   não rampa. A resposta padrão pra qualquer gasto novo é **não**, até o Gusta dizer sim.

---

## Movimento 1 — O time

Três papéis, já persistidos em `.maestri/roles/`. Se os agentes não estiverem no canvas:

```bash
maestri role list          # confirma que os 3 papéis existem
maestri recruit "Peneira" --preset "Claude Code" --role "Swipe e Teardown"
maestri recruit "Isca"    --preset "Claude Code" --role "Roteiro e Gancho"
maestri recruit "Bisturi" --preset "Claude Code" --role "Edicao e Montagem"
```

| Agente | Papel | Dono exclusivo de |
|---|---|---|
| **Peneira** | Swipe e Teardown — estrategista sênior: diagnostica POR QUE vende e escreve o plano de réplica (3 ads: clone + 2 melhores, uma alavanca cada) | `referencias/`, `escalados/` |
| **Isca** | Roteiro e Gancho | `roteiros/` |
| **Bisturi** | Edição e Montagem | `criativos/`, `esteira.html`, portal "Esteira Spy" |

> **Regra de edição (Gusta, 2026-09-05): remover pausas longas.** Silêncio acima de ~0,4 s dentro de uma fala ou entre cenas é cortado (`silencedetect` a -35 dB e corte de vídeo junto, pra não perder o lipsync); respiro entre cenas no máximo 0,3 s. Ritmo alvo 180–200 palavras/min sem buraco.

**Ligue Peneira ↔ Bisturi.** A esteira flui pra frente (swipe → roteiro → montagem), mas **correção sempre
flui pra trás**: quem monta é quem descobre que a medição do teardown está errada. Sem esse canal, a
correção passa por você e chega tarde.

⚠️ **`role edit`, `role assign` e `recruit --replace` reiniciam o processo e apagam o histórico do agente.**
Nunca rode isso com um agente no meio de um trabalho. Pra passar contexto novo a quem já está tocando,
use a **nota compartilhada**.

---

## Movimento 2 — A nota compartilhada (`briefing-spy`)

O papel é a parte fixa do instrumento. A nota é a parte que muda a cada lote: qual oferta, qual peça
vencedora, quantas variações, o que já foi decidido. Conecte-a aos três.

```bash
maestri note create --name "briefing-spy" "..."      # primeira vez
maestri note edit "briefing-spy" "<lote antigo>" "<lote novo>"   # nas seguintes
```

A nota carrega o **protocolo de correção**, que vale pros três:

> quem acha erro fala direto com o dono do arquivo, sem triangular · nunca edite arquivo que não é seu ·
> traga medição, não opinião · corrija a causa, não só o número, e marque o valor velho em vez de apagar.

---

## Movimento 3 — Peneira: achar e dissecar

Alvo: uma peça **que já escalou** (30+ dias na Ad Library, ou já marcada no wiki como vencedora).
Entrega um teardown no padrão de `referencias/2026-08-31-ladprofit-*.md` e **ingere no
`wiki/trafego-criativos/`** — fonte crua em `raw/`, páginas atômicas `[[cross-linkadas]]` em `wiki/`,
`index.md` e `log.md` atualizados.

Se o Gusta autorizar copiar a copy do vencedor, **copie literal** — não reescreva, não melhore, não traduza.
Ad Library esconde o texto primário em cards agrupados: nesse caso só a headline é pública, e você diz isso
em vez de preencher o buraco.

---

## Movimento 4 — Isca: modelar o roteiro

Modela o formato que o Peneira mapeou, não inventa do zero. Gancho nos 3 primeiros segundos, corpo, prova,
CTA — cena a cena, com o que aparece na tela e o que a pessoa fala. Sempre em variações de gancho sobre o
**mesmo** formato, pra ter o que testar.

Consulte `wiki/trafego-criativos/wiki/tecnicas/catalogo-de-layouts-spy.md` (L1–L10) e escolha o layout
explicitamente. Nunca invente depoimento, case ou número. Nunca imite veículo de imprensa real.

---

## Movimento 4½ — Jev: pontuar os ganchos antes de gastar

Antes de o Bisturi gastar em lipsync, o **Jev** (TypeSafe) pontua os ganchos que a Isca modelou e diz
**qual tende a converter mais** — pra montar primeiro os fortes e não queimar geração paga em gancho fraco.
É um filtro de priorização calibrado, não um oráculo.

```bash
# monte um JSON {nome: {headline, primeira_fala, angulo, formato}} com as variações da Isca e rode:
python3 typesafe/pontuar_ganchos.py <ganchos.json>      # de projects/mentoria-spy/
```

Devolve o **composto** (0–1) de cada gancho, as dimensões (dor concreta, curiosidade, emoção, confissão) e
uma **flag de risco de política** (`risco-fala ≥ 0,50` = a fala promete hack/senha/espionar → revisar antes).
O Bisturi monta na ordem do ranking; o maestro leva o top ao Gusta.

Verdades que não dá pra esconder (detalhe em `typesafe/estudo/02-estudo-e-resultado.md`):
- A rubrica lê **a copy do gancho**, não a edição. Não distingue variações que só trocam avatar (copy igual),
  nem capta mecânica (gancho sumindo vs fixo).
- Foi validada contra **gasto real** da casa (rho +0,67, n=8) — **direcional**, não prova de conversão.
- Vira previsão de verdade só rodando o top no Meta e re-validando contra CPA/ROAS reais (UTMify/Meta).
- Custa centavos (input US$0,042/MTok, output grátis); mesmo assim, é a regra da casa: **não é geração paga**,
  mas anuncie que rodou. Chave em `typesafe/.env` (gitignored, server-side).

---

## Movimento 5 — Bisturi: medir, gerar, montar

A parte cara e a parte que pode errar em silêncio. Duas skills sustentam ela:
`.claude/skills/trocar-avatar/` (o talking head) e `.claude/skills/clonar-edicao/` (a edição em volta).

**Edição elaborada (além do ffmpeg sobre blocos).** Quando a peça pede motion graphics, overlay animado
sincronizado à fala, data-viz, texto cinético ou um segmento explainer que o remonte de blocos não honra,
o Bisturi **escala pra código-como-vídeo** em vez de inventar gambiarra:

- **Remotion** (já instalado): use `/remotion-reference-overlays` pra talking-head no estilo de uma
  referência (cortes + legenda palavra-a-palavra + motion graphics/B-roll sincronizados, tudo em código);
  `/remotion-create`, `/remotion-markup`, `/remotion-captions`, `/remotion-render` pro resto. É determinístico
  e versionável (cortes.ts / legendas.ts / beats.ts).
- **HyperFrames** (HeyGen, Apache-2.0, HTML/CSS/mídia → MP4 determinístico) pra motion baseado em HTML/CSS.
  ⚠️ Precisa de instalação única, que o **Gusta** roda (o harness bloqueia install de terceiro):
  `claude plugin marketplace add heygen-com/hyperframes` + `claude plugin install hyperframes@hyperframes`,
  ou CLI `npx hyperframes init/preview/render` (Node 22+, ffmpeg). Sem API key pro render local.

Regras não mudam: determinístico (mesmo input → mesmo output), sem PII de terceiro, **medir antes de montar**,
e o resultado é do Bisturi (vai em `criativos/`). Escolha o caminho mais barato que honra a referência —
remonte de bloco (US$0) > Remotion/HyperFrames (código) > geração paga.

**Medir antes de montar.** A fronteira entre os blocos de um vídeo se mede por
`wiki/trafego-criativos/wiki/tecnicas/medir-fronteira-de-bloco-em-video.md`. As regras que já custaram
retrabalho:

- Referência de terceiro → **variância temporal** sobre dezenas de frames. Cor se engana com borda
  decorativa interna (foi assim que um split saiu 35,8% em vez de 39,4%, cortando 13px do funil).
- Peça nossa com faixa chapada → cor funciona; variância funde blocos quase estáticos.
- **Sempre o penhasco (argmin da diferença), nunca um limiar absoluto.** Limiar é calibrado num vídeo e
  quebra no próximo.
- **Existe fronteira? Só então meça a margem.** Margem diz que há transição detectável, não que é a que
  você quer.
- **Concordância entre peças vale mais que margem dentro de uma.**
- Olhe a imagem exportada. Ler perfil de linha sem abrir o frame já errou três vezes num dia só.

**Mostrar o trabalho é obrigatório.** Bisturi reescreve `esteira.html` **a cada etapa**, não só no fim:
referência → frames medidos (com timestamp e o que foi medido) → head gerado → peças montadas. Caminhos
sempre **relativos** a `projects/mentoria-spy/`. Depois de cada reescrita:
`maestri portal screenshot "Esteira Spy"` pra confirmar que renderizou.

Foi esse portal que pegou o defeito de lipsync e o erro de medição **antes** de virarem lote entregue.

---

## Movimento 6 — Verificação (sua, no disco)

Relato de agente não é entrega. Confira você mesmo, sempre:

```bash
ffprobe -v error -show_entries stream=width,height,nb_frames,codec_name -of csv <peca>.mp4
md5 <pecas>            # variação de layout deve manter o head bit-idêntico
grep -rn "<valor-errado>" projects/ wiki/     # correção propagou mesmo?
wavespeed billings | grep macbook             # gasto real da nossa chave
```

Já aconteceu de um número corrigido em 4 páginas do wiki continuar vivo no roteiro. `grep` é barato.

---

## Movimento 7 — Entrega

- Lote em `criativos/<nome-do-lote>-AAAA-MM-DD/` com README dizendo qual roteiro e qual referência
  geraram cada peça.
- Mídia pesada **não** entra no git (o `.gitignore` da raiz já barra `mp4/mov/png/jpg` em `projects/**`).
- Tudo que virou aprendizado vai pro `wiki/trafego-criativos/`. Insight solto vai pro `inbox/` do wiki.
- `open <pasta-do-lote>/pecas` — no Finder, selecionar tudo + **espaço** toca em sequência.
- Reporte o gasto real, não o estimado.

---

## Invariantes (valem em qualquer lote)

1. Nada pago dispara sem estimativa mostrada antes.
2. PII de terceiro nunca entra numa peça. Já tentou entrar duas vezes por caminhos diferentes.
3. Nunca edite arquivo de outro agente — mande o número e a evidência, o dono aplica.
4. Layout L5 e CR05-V4 foram **rejeitados pela Meta**. Não remonte.
5. Uma alavanca por teste: variação de layout mantém head e locução bit-idênticos.
6. Não invente número de performance. Puxe do Meta Ads/UTMify ou marque como suposição.
7. Antes de gastar em geração, passe os ganchos pelo Jev (Movimento 4½) e monte na ordem do ranking. O composto é priorização direcional, nunca prova de conversão.

---

## Variante barata — só variações de layout

Quando o head e a locução já existem, remontar em outros layouts custa **US$ 0,00**: é só ffmpeg sobre
blocos que já estão em `criativos-crus/`. Foi o que produziu L1/L2/L4 do lote 3. Bisturi deve **pular**
molde que não dá pra honrar (falta funil, footage com legenda queimada, layout que corta o rosto) e
**dizer o motivo verificado** de cada pulo, em vez de entregar uma variação inventada.

---

## Metrônomo (opcional)

Pra esteira rodar sozinha num horário:

```bash
maestri routine create "Varredura spy" --daily 09:00 --terminal "Peneira" \
  --command "Varra a Ad Library das ofertas spy e reporte o que passou de 30 dias desde ontem"
```
