---
tipo: projeto
atualizado: 2026-08-27
tags: [swipe, ad-library, centerpag, zapspy, zappdetect, concorrente]
---

# centerpag-detect — swipe da Ad Library (go.centerpag.com)

Todos os anúncios que a Meta Ad Library retorna para a busca por palavra-chave
**`go.centerpag.com`** (status ativo, country=ALL, ordenado por total de impressões),
baixados em **27/08/2026**.

Mesmo processo do `../gram-detect/`, outro domínio de destino. **É o mesmo grupo:** a UI que
aparece nos criativos mostra `ZapSpy.ai`, `ZappDetect`, `Configrapp` e `Gram Detect`, e a copy
principal ("2.4M people already stopped torturing themselves with 'what if.'") é a mesma que
roda no swipe do zappdetect. A diferença é o produto vendido: **lá era espionagem de Instagram,
aqui é espionagem de WhatsApp** — clonar/monitorar o WhatsApp do parceiro.

## O que tem aqui

- `anuncios/` — 152 arquivos: 73 vídeos `.mp4` (+ poster `-thumb.jpg` de cada) e 6 estáticos `.jpg`.
  Nome do arquivo = `pagina-adid.ext`, então dá pra rastrear cada peça de volta pra Ad Library.
- `manifest.json` — 1 entrada por anúncio: Página, status, data de início, tempo rodando, copy,
  headline, descrição, CTA, destino, tier e os arquivos correspondentes.
- `escalados/` — as **26 peças sem carimbo de baixo volume**, ranqueadas, cada uma com o texto
  completo do anúncio num `.txt` do lado. Comece por aqui: `escalados/README.md`.
- `tratados/` — as mesmas peças com os metadados zerados (`scripts/tratar-criativos.py`).
- `galeria.html` — visualizador local (abre no navegador, filtra por Página, toca os vídeos).

## Números

- **87 anúncios** no total. **79 com criativo baixado**, **8 indisponíveis**, **2 de ruído da busca**.
- Os 8 indisponíveis são todos da Página **Rachel Thompson** (30/jul a 2/ago): a Meta derrubou a
  conta por violar Padrões de Publicidade e **removeu os criativos** — não existe mídia pra baixar.
- Os 2 de ruído são da Página **Miriam Digital** ("Unshakable Confidence: The Modern Man's Guide
  to Self-Belief"): não têm nada com o centerpag, entraram porque a busca é `keyword_unordered`
  e casou com palavras soltas. Ficam no manifest marcados como `tier: D-ruido-da-busca`.
- **71 criativos únicos** entre os 79 baixados — 8 aparecem em mais de um anúncio da mesma Página.
- **51 dos 85 relevantes estão carimbados `<100 impressões`** pela Meta. Ou seja: a conta sobe
  muito criativo e quase nada entrega. Só 26 passaram do corte.
- **Resolução:** os vídeos vêm no arquivo original do CDN; os estáticos vêm em 338–600px de largura,
  que é o tamanho que a Ad Library renderiza (ela não expõe o original). Pra recriar em alta,
  tratar como referência de layout, não como asset final.

## Páginas anunciando pro mesmo destino

| Página | Anúncios | Escalados | Formato | Máx. dias no ar | Início | Headline dominante |
|---|---|---|---|---|---|---|
| Fernanda Mello | 22 | 1 | video x22 | 0.1 | 27 de ago de 2026 | Fernanda Mello |
| Sara Oliveira | 10 | 6 | video x10 | 4.1 | 23 de ago de 2026 / 25 de ago de 2026 | ⭐️⭐️⭐️⭐️⭐️ (4.9/5.0) |
| Verônica Borges | 10 | 2 | video x10 | 1.1 | 26 de ago de 2026 | Free Test ✅ |
| Rachel Thompson | 8 | 0 | indisponivel x8 | 3.0 | 1 de ago de 2026 a 2 de ago de 2026 / 30 de jul de 2026 a 2 de ago de 2026 | — |
| Karoliny Lucas - Especialista em Diástase | 6 | 0 | video x6 | 0.1 | 27 de ago de 2026 | Free trial: enter your partner's phone number |
| Livia Rain | 6 | 0 | video x6 | 1.1 | 26 de ago de 2026 / 27 de ago de 2026 | Free Trial: Enter Your Partner’s Phone Number |
| Kendall Godfrey Stephanie | 5 | 3 | video x3, imagem x2 | 1.1 | 26 de ago de 2026 | Free trial: enter your partner's phone number |
| Sophia Jones | 4 | 4 | imagem x2, video x2 | 1.1 | 26 de ago de 2026 | Free trial: enter your partner's phone number |
| Victorai Martins | 4 | 1 | video x4 | 1.1 | 26 de ago de 2026 | Free Test ✅ |
| Esther Vicman | 2 | 2 | video x2 | 16.1 | 11 de ago de 2026 / 26 de ago de 2026 | Free Test ✅ |
| Alberto Souza | 2 | 2 | video x2 | 17.1 | 10 de ago de 2026 / 23 de ago de 2026 | See today everything that happens! |
| Emilly Bredoff | 1 | 1 | video x1 | 16.1 | 11 de ago de 2026 | Free Test ✅ |
| Isabella Walker | 1 | 1 | video x1 | 35.1 | 23 de jul de 2026 | See this before it's too late... |
| Lauren Roberts | 1 | 1 | video x1 | 35.1 | 23 de jul de 2026 | See this before it's too late... |
| Simone Maria Braum | 1 | 1 | video x1 | 2.1 | 25 de ago de 2026 | See this before it's too late... |
| Elaine Bezerra | 1 | 0 | video x1 | 35.1 | 23 de jul de 2026 | See this before it's too late... |
| Gonçalo Antunes | 1 | 1 | video x1 | 35.1 | 23 de jul de 2026 | See this before it's too late... |

> **Leitura rápida:** `Fernanda Mello` sozinha responde por 22 dos 85 anúncios — todos subidos em
> 27/ago e **21 deles carimbados `<100`**. É uma Página nova despejando criativo em volume.
> No outro extremo, `Isabella Walker`, `Lauren Roberts`, `Elaine Bezerra` e `Gonçalo Antunes` têm
> 1 anúncio cada, mas rodando **desde 23/jul (35 dias)** — essas são as peças validadas.
> Nenhuma Página do Gusta aparece nesse swipe.

## Ângulos de copy em rotação

- **29x** — 2.4M people already stopped torturing themselves with 'what if.' They chose to know.👇
- **13x** — Oh my god, I was in shock when I found all those messages! 😱 I never imagined I'd discover infidelity and disappointments like this in my life 💔
- **12x** — Ever wondered what someone's Instagram activity really looks like? 👀 Our tool analyzes any public profile and shows you who they follow, what they like, and the accounts they interact with the most. Just type the @username — the first analysis is free.
- **10x** — Try the app for free now and discover the whole truth.
- **6x** — I thought I knew who they really were… until I saw those messages 😳
What I found was packed with secrets, lies, and things I wish I had never discovered 💔

15 anúncios não exibem texto: são cards agrupados ("Esse anúncio tem várias versões"), formato
em que a Meta esconde o rodapé e o texto principal.

## Headlines

- **17x** — Free Test ✅
- **13x** — Free trial: enter your partner's phone number
- **10x** — ⭐️⭐️⭐️⭐️⭐️ (4.9/5.0)
- **5x** — See this before it's too late...
- **4x** — Fernanda Mello
- **2x** — Free Trial: Enter Your Partner’s Phone Number
- **1x** — See today everything that happens!
- **1x** — See today everything that happens... 🔥
- **1x** — Analyze any @username in seconds

**CTA:** Ver detalhes (27x), Saiba mais (24x), Learn More (2x), See Details (1x)
**Descrição** (quase nunca preenchida): "Free test" (2x), "Free first analysis. No login needed." (1x)

## Comparação com a coleta de 22/08 (`../centerpag/`)

Esse mesmo domínio já tinha sido raspado em **22/08**, num formato diferente (split por plataforma,
sem tiers nem escalados) — está em `../centerpag/`. Cruzando os dois manifests:

| | 22/08 (`centerpag/`) | 27/08 (aqui) |
|---|---|---|
| Anúncios coletados | 44 (de ~59 que renderizaram) | 87 (rolagem até esgotar) |
| Carimbados `<100 impressões` | 0 | 51 |
| Máx. dias no ar | 31,2 (Alberto Souza) | 35,1 (4 peças) |
| Páginas | 11 | 17 |

- **Só 3 dos 44 IDs de 22/08 ainda estavam ativos em 27/08.** Em 5 dias a conta trocou
  praticamente todo o inventário de anúncio.
- **6 Páginas sumiram** (Charlotte Miller, Helena Alves, Inêz Cunha, Maria Carmen, Mia Davis,
  Nelma Miranda) e **12 apareceram**. Rotação de conta é parte da operação, não acidente.
- ⚠️ **A coleta de 22/08 era parcial.** As 4 peças que estão no ar desde **23/jul** (35,1 dias)
  não aparecem no manifest dela — ou seja, ela pegou só um pedaço da biblioteca. Trate o "41
  sumiram" como direção, não como número exato de anúncios mortos.
- A headline "See this before it's too late..." era da Alberto Souza em 22/08 (31,2 dias) e hoje
  roda em **4 Páginas diferentes** (Isabella Walker, Lauren Roberts, Elaine Bezerra, Gonçalo
  Antunes), todas com 35,1 dias. É o ângulo mais durável do swipe.

## Como isso foi coletado

A Ad Library bloqueia `curl` (403) e o CSP dela bloqueia iframe e fetch pra fora. O caminho que
funcionou (mesmo do `gram-detect`, com um ajuste):

1. Abrir a busca no Chrome logado e rolar até esgotar — aqui levou ~9 min e três rodadas de
   scroll até parar de carregar em 87 cards (o "~100 resultados" da Meta é estimativa).
2. Extrair no DOM, por card, o texto e os `<video>`/`<img>` com as URLs assinadas do CDN.
3. **Sair da página levando os dados junto:** subir um servidor local, jogar o JSON no
   *fragmento* da URL (`http://127.0.0.1:PORT/#<json>`) e navegar a própria aba pra lá — a página
   local lê `location.hash` e faz POST do JSON pro disco. (O iframe pro localhost é bloqueado
   pelo CSP do Facebook; a navegação da aba não é.) O JSON também vai pro `localStorage` do
   facebook.com como backup, caso a navegação falhe.
4. Baixar as mídias com `curl` usando as URLs assinadas.

Refazer = repetir esse ciclo. **As URLs do fbcdn expiram em algumas horas** — não dá pra guardar
a lista e baixar depois.

⚠️ **Performance não verificada.** A Ad Library não expõe gasto, CTR nem ROAS. Os únicos proxies
de validação aqui são o **carimbo de baixo volume**, o **tempo no ar** (`rodando_ha`) e a
repetição do mesmo criativo/copy. Ver `escalados/README.md`.
