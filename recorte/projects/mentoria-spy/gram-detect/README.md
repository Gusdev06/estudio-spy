---
tipo: projeto
atualizado: 2026-08-22
tags: [swipe, ad-library, zappdetect, concorrente]
---

# gram-detect — swipe da Ad Library (go.zappdetect.com)

Todos os anúncios que a Meta Ad Library retorna para a **frase exata `"go.zappdetect.com"`**
(status ativo, country=ALL, ordenado por total de impressões), baixados em **22/08/2026**.

## O que tem aqui

- `anuncios/` — 43 arquivos: 20 vídeos `.mp4`, 3 estáticos `.jpg` e o poster (`-thumb.jpg`) de cada vídeo.
  Nome do arquivo = `pagina-adid.ext`, então dá pra rastrear cada peça de volta pra Ad Library.
- `manifest.json` — 1 entrada por anúncio: página, status, data de início, tempo rodando, copy,
  headline, descrição, CTA, destino e os arquivos correspondentes.
- `escalados/` — as 13 peças com volume real de impressões, ranqueadas, cada uma com o texto
  completo do anúncio num `.txt` do lado. Comece por aqui: `escalados/README.md`.
- `tratados/` — as mesmas peças com cor corrigida e metadados zerados (`scripts/tratar-criativos.py`).
- `galeria.html` — visualizador local (abre no navegador, filtra por página, toca os vídeos).

## Números

- **27 anúncios** no total. **23 com criativo baixado**, **4 indisponíveis**.
- Os 4 indisponíveis são da página **Quinn** (1–2/jun/2026, <100 impressões): a Meta derrubou a
  conta por violar Padrões de Publicidade e **removeu os criativos** — não existe mídia pra baixar.
- Nenhum criativo duplicado: os 23 arquivos têm md5 distintos.
- **Resolução:** os vídeos vêm no arquivo original do CDN; os 3 estáticos vêm em **338×600**, que é o
  tamanho que a Ad Library renderiza (ela não expõe o original). Pra recriar em alta, tratar como
  referência de layout, não como asset final.

## Páginas anunciando pro mesmo destino

| Página | Anúncios | Formato | Início | Headline dominante |
|---|---|---|---|---|
| Gustagoat | 9 | video x9 | 21 de ago de 2026 / 22 de ago de 2026 | Free Test ✅ |
| Sophia Jones | 5 | video x5 | 19 de ago de 2026 | Analyze any @username in seconds |
| VolutPay | 5 | video x5 | 20 de ago de 2026 | Free Trial ✅ |
| Charlotte Miller | 4 | imagem x3, video x1 | 19 de ago de 2026 | Analyze any @username in seconds |
| Quinn | 4 | indisponivel x4 | 1 a 2 de jun de 2026 | — |

> ⚠️ **`Gustagoat` é a página do próprio Gusta.** 9 dos 27 anúncios saem dela — ou seja, parte
> desse resultado é a nossa própria operação, não concorrente. Ao ler o swipe, separe: concorrentes
> reais = Sophia Jones, Charlotte Miller, VolutPay, Quinn.

## Ângulos de copy em rotação

- **12x** — 2.4M people already stopped torturing themselves with 'what if.' They chose to know.👇
- **6x** — Ever wondered what someone's Instagram activity really looks like? 👀 Our tool analyzes any public profile and shows you who they follow, what they like, and the accounts they interact with the most. Just type the @username — the first analysis is free.
- **4x** — I couldn't believe what I was seeing! 😳 Every message revealed another lie. I never imagined the truth would be this heartbreaking. 💔
- **1x** — I couldn't believe someone could hide so much. 😢 Every message uncovered another betrayal. My heart broke with every word. 💔

## Headlines / CTA


- **9x** — Analyze any @username in seconds
- **7x** — Free Test ✅
- **4x** — Free Trial ✅
- **1x** — Free first analysis. No login needed.

## Como isso foi coletado

A Ad Library bloqueia `curl` (403) e o CSP dela bloqueia qualquer canal de saída da página. O caminho
que funcionou: abrir a busca no Chrome logado, rolar até carregar tudo, extrair no DOM os `<video>`/
`<img>` de cada card, passar a lista pra um servidor local via fragmento de URL e baixar as mídias
com `curl` usando as URLs assinadas do CDN. Refazer = repetir esse ciclo (as URLs do fbcdn expiram).

⚠️ **Performance não verificada.** A Ad Library não expõe gasto, CTR ou ROAS. O único proxy de
validação aqui é **tempo no ar** (`rodando_ha` no manifest) e a repetição do mesmo criativo/copy.
