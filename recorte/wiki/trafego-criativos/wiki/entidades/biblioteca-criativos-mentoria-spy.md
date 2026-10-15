---
tipo: entidade
tags: [biblioteca, spy-gram, spy-zap, inventario]
fontes: [fonte-varredura-biblioteca-spy-2026-08-31]
---

# Biblioteca de criativos — mentoria-spy

Acervo de vídeo das duas ofertas spy (Instagram e WhatsApp) em `projects/mentoria-spy/`.
**373 arquivos · 296 únicos por md5 · 15,16 GB ocupados pra 10,84 GB de conteúdo — 4,33 GB de duplicata.** ~2h50 de footage único.

Inventário completo (md5 · duração · resolução · bytes · caminho) em
`raw/2026-08-31-inventario-criativos-mentoria-spy.tsv`.

## Como o acervo se organiza

| Grupo | Lotes | Eixo que varia |
|---|---|---|
| **spy-zap** (WhatsApp) | `cr02` · `cr05` | layout — 7 montagens da mesma locução |
| | `base-ingles` | avatar × duração |
| | `ingles-17-08` | casting UGC × hook |
| | `23-02-spy-en-es` | 8 personagens × EN/ES |
| **spy-gram** (Instagram) | `ads-en` (GD-AD01–10) | 10 ângulos de hook |
| | `16-julho` · `26-julho` · `ingles-com-head` | *(não amostrados ainda)* |
| **ambos** | `criativos-personagens` | 3 conceitos × 3-4 atores, duração travada |
| | família `GRAM` | [[familia-criativos-gram-funil-gravado]] — 6 idiomas × 2 gêneros de alvo |
| **swipe** | `gram-detect/anuncios` · `tratados` · `escalados` | concorrentes da Ad Library, documentados à parte |

Subprodutos de geração (não são peças de anúncio): `troca-avatar-studio/jobs`, `lote-5-avatares`, `teste-omni-2026-08-27` — ~95 arquivos.

## O que a biblioteca ensina

- [[eixos-de-variacao-de-criativo]] — os 6 eixos, e em que ordem girar cada um
- [[catalogo-de-layouts-spy]] — os 7 layouts já usados, e o kit de blocos que os compõe
- [[molde-de-edicao-n-atores]] — a unidade de produção é o molde, não o vídeo
- [[rejeitando-no-nome-do-arquivo]] — o único registro de compliance por peça que existe hoje
- [[template-funil-gravado-9-modulos]] — a linha GRAM, sem locução

## Copy transcrita (31/08/2026)

**95 de 114 peças de criativo têm a copy falada transcrita e indexada** em
`projects/mentoria-spy/transcricoes/`:

- `transcricoes.json` — texto completo + segmentos com timestamp, chaveado por md5
- `<lote>.md` — 21 arquivos legíveis, um por lote, com a copy de cada peça
- `folhas/<lote>.jpg` — folha de contato de todo lote (3 frames por vídeo)
- `manifest-criativos.csv` — 1 linha por peça: md5, arquivo, lote, oferta, idioma, alvo, duração, cluster, moderação, **layout**, **ator**, hook falado, caminho

**`layout` e `ator` preenchidos nas 114 linhas** (31/08). Distribuição de layout:
`L8 head cheio+karaokê+insert` 29 · `L1 head+funil` 24 · `L9 funil gravado (sem head)` 12 ·
bruto de editor 13 · swipe de concorrente 10 · L2–L7 um a três cada · assets e fragmentos 6.

**34 atores distintos** identificados. Os dois mais reaproveitados são
`m-negra-trancas-oculos` (9 peças, o lote cr02 inteiro + CR02 do 23-02) e
`h-barbudo-jaqueta` (9 peças, o lote cr05 inteiro + CR05 do 23-02).

⚠️ **Observação a checar:** o talking head do `wpp-01-esther-vicman` — o criativo #1 de 87 do swipe,
supostamente de concorrente — é **o mesmo ator do lote `cr05`** (`h-barbudo-jaqueta`), com a mesma
locução. Ou a página Esther Vicman usa o mesmo creator licenciado, ou é a própria operação sob outro
nome de página. O `gram-detect/README.md` já registra que a página **Gustagoat** aparece no swipe;
vale conferir se Esther Vicman também é da casa antes de tratá-la como concorrente.

As 19 sem copy são mudas **por natureza**: a família GRAM inteira é peça visual sem locução
([[template-funil-gravado-9-modulos]]) e `setas_transparentes.mov` é asset de overlay.

⚠️ **Filtro de alucinação aplicado.** O Whisper devolve `you` / `Thank you.` em faixa silenciosa —
sem filtro, as 12 peças GRAM entrariam no manifest como "tendo copy". Só conta como copy o texto com
6+ palavras distintas.

Distribuição: **spy-zap 74 · spy-gram 29** · idiomas EN 87, ES 12, PT 2, DE/FR/IT 2 cada ·
clusters curto 37, médio 48, longo 29.

## Pendências

1. ⚠️ **4,33 GB de duplicata.** `EDIÇÃO 2/` é cópia byte a byte de `EDIÇÃO/`; `downloads/EDIÇÃO*/` repete de novo; `_APAGAR/` tem 22 já verificadas. Consolidar com o TSV como fonte de verdade.
2. ⚠️ **Zero métrica cruzada.** 296 peças e nenhuma amarrada a gasto/CTR/ROAS. Não se sabe qual layout, ângulo ou personagem converte — só qual ficou mais tempo no ar no swipe.
3. **Manifest sem as colunas caras.** `layout`, `ator`, `gasto`, `ctr`, `roas` existem no CSV mas estão em branco. `layout` e `ator` se preenchem no olho a partir das folhas de contato; as três de performance dependem do Meta Ads.

## Ângulos de hook já testados

Em `spy-gram/ads-en`, verbatim — é o repertório validado da casa:

```
I found something i wasn't even looking for...
You start noticing the little things...
The worst part is realising it was happening right infront of me...
You know when something just feels off...
I kept thinking I would be the first to know...
You think you would be the first to find out...
The second I walk into the room, the phone flips...
Most people believe they would notice right away...
i always thought deleted messages were gone for good...
I noticed she always took the phone with her...
```

**Dois de dez (AD05, AD06) usam o device "primeiro a saber"** — o mesmo binário forçado do sticker do Roteiro D. Não era ideia nova: era repertório da casa que voltou.
