# LLM Wiki — Tráfego & Criativos

Este é um **segundo cérebro** de tráfego pago e criativos do Gusta, no método
Karpathy/Nate Herk: fontes cruas entram em `raw/`, e você (o agente de ingestão) as
quebra em **páginas atômicas de markdown cross-linkadas** dentro de `wiki/`. O valor
não está em armazenar — está nas **conexões** entre criativos, campanhas, conceitos e
técnicas, que deixam qualquer agente (analista-trafego, copywriter, creative-producer)
achar padrão rápido.

Escopo: a operação de ads do Gusta (low ticket 300-prompts, AI Model Lab, GERAEW).
Foco maior hoje: escalar a low ticket de 1 → 4 ofertas de R$1k/dia.

## Estrutura

- `raw/` — jogue aqui a fonte crua (teardown, análise, transcrição de ad, print de
  gerenciador, artigo). Nada é editado aqui; é só entrada. Um arquivo = uma fonte.
- `inbox/` — captura rápida sem fricção. Uma ideia solta, um insight de campanha, um
  "testar X". Não precisa estar formatado. Periodicamente peça pra limpar o inbox: o
  agente vira cada nota em página atômica no lugar certo e esvazia. *Não deixe o perfeito
  ser inimigo do útil* — capture bruto aqui, organize depois.
- `wiki/` — as páginas atômicas geradas. Subpastas:
  - `conceitos/` — ideias e mecanismos (bid cap, believability, folga de bid…).
  - `tecnicas/` — como-fazer acionável (value stack no overlay, variar 1 alavanca…).
  - `entidades/` — coisas concretas: criativos (`criativo-<ad_id>`), campanhas
    (`campanha-<slug>`), ofertas (`oferta-<slug>`), plataformas.
  - `fontes/` — 1 página por fonte ingestada de `raw/`, com resumo + links pras
    páginas que ela gerou. É o "de onde veio esse dado".
- `index.md` — mapa/índice navegável de tudo (table of contents).
- `log.md` — log append-only de cada ingestão (data, fonte, páginas criadas).

## Regras de ingestão (siga à risca)

1. **Uma fonte por vez.** Leia o arquivo em `raw/`, entenda, e ANTES de escrever
   confira o `index.md` pra não duplicar página que já existe — se já existe, ATUALIZE
   e adicione backlink, não crie outra.
2. **Páginas atômicas.** Uma página = um conceito/técnica/entidade. Uma fonte densa
   vira 5–15 páginas. Prefira granular a monolítico.
3. **Cross-link agressivo.** Toda página referencia outras com `[[nome-do-arquivo]]`
   (sem extensão, sem caminho — o Obsidian resolve pelo nome). Link mesmo que a página
   alvo ainda não exista (marca o que falta criar).
4. **Nomes kebab-case** e estáveis. Criativo = `criativo-<ad_id>`. Campanha =
   `campanha-<slug>`. Nunca renomeie um arquivo já linkado sem consertar os backlinks.
5. **Não invente número.** Métrica só entra se veio de fonte real (Meta Ads/UTMify/
   arquivo). Se faltar, escreva "não verificado" — nunca chute ROAS/CPA/CTR.
6. **Frontmatter** em toda página (`tipo`, `tags`, `fontes`). Veja o template abaixo.
7. **Sempre** atualize `index.md` (novas páginas nos grupos certos) e acrescente uma
   linha em `log.md` ao fim de cada ingestão.
8. **Cace contradições.** Se duas fontes divergem (ex.: criativo diz $6,99 e página
   vende $12,99), registre a divergência explicitamente na página — é o maior valor do
   wiki.
9. **Summary line que filtra.** A 1ª linha de toda página é um resumo de 1 frase. É o
   sinal que deixa o agente decidir relevância SEM ler o arquivo inteiro (economiza
   token). Frontmatter `tags` reforça isso.
10. **Termo canônico único.** Escolha UM nome por ideia e use sempre o mesmo (ex.: "bid
   cap", não alternar com "lance máximo"/"bid máximo"). Sinônimos viram alias na página
   [[glossario]], não páginas novas. Terminologia consistente = o agente acha na 1ª.

## Manutenção (evita degradar com o tempo)

Rode uma **varredura** de tempos em tempos (peça: *"faz um sweep de manutenção do wiki
de tráfego"*). O agente:
- Acha **páginas órfãs** (sem nenhum backlink apontando pra elas) e as conecta.
- Acha **backlinks quebrados** (`[[nome]]` sem arquivo) e cria a página faltante ou corrige.
- Marca **dados desatualizados** (métricas velhas — o mercado muda semanal) com a data e
  sinaliza pra re-ingestar.
- Reabre **contradições** não resolvidas listadas no `index.md`.

## Template de página

```markdown
---
tipo: conceito | tecnica | entidade | fonte
tags: [bid-cap, criativo, ...]
fontes: [[fonte-...]]
---

# Título

Resumo de 1-2 linhas.

## Corpo
...conteúdo com backlinks [[...]] pra conceitos/técnicas/entidades relacionados...

## Conecta com
- [[pagina-a]] — por quê
- [[pagina-b]] — por quê
```

## Como usar (ingestão)

Coloque a fonte em `raw/` e peça: *"ingesta a nova fonte em raw/ no wiki de tráfego"*.
O agente segue as regras acima. Batch: *"ingesta tudo que tem em raw/ ainda não logado"*.
