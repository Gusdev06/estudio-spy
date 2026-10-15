# Varredura da biblioteca de criativos — mentoria-spy, 31/08/2026

Inventário completo em `2026-08-31-inventario-criativos-mentoria-spy.tsv`
(md5 · duração · resolução · bytes · caminho).

## Números

- **373 arquivos de vídeo · 296 únicos por md5**
- 15,16 GB ocupados · 10,84 GB de conteúdo real · **4,33 GB de duplicata**
- ~2h50 de footage único

## Cobertura desta varredura

**Amostrados com folha de contato (73 peças):** `spy-zap/cr02` (7) · `spy-zap/cr05` (7) ·
`spy-zap/base-ingles` (8) · `spy-zap/ingles-17-08` (10) · `spy-zap/23-02-spy-en-es` en+es (16) ·
`spy-gram/ads-en` (10) · `criativos-personagens` (10) · família `GRAM` (5 de 12 assistidos).

**Inventariados mas ainda não assistidos:** `spy-gram/16-julho/Ingles` (7) · `spy-gram/26-julho` (4) ·
`spy-gram/ingles-com-head` (5) · `exports-0824` (6) · `referencias-zapspy-2026-08-29` (5) ·
`tratados-2026-08-28` (7).

**Fora do escopo de criativo** (subprodutos de geração, não peças de anúncio): `troca-avatar-studio/jobs`
(25) · `criativos/lote-5-avatares` (~35) · `criativos/teste-omni-2026-08-27` (32) · `troca-avatar` (2).

**Já documentado à parte:** `gram-detect/anuncios` + `tratados` + `escalados` (40) — é o swipe da Ad
Library, coberto pelo `gram-detect/README.md` e por [[criativo-wpp01-1762552938111855]].

## Os 6 eixos de variação encontrados

| Eixo | Lote que exemplifica | O que fica constante |
|---|---|---|
| **Layout / montagem** | `cr02`, `cr05` — 7 variações cada | locução, ator, duração |
| **Personagem / avatar** | `criativos-personagens` (AD04: 3 atores em 23,9s exatos) | molde de edição inteiro |
| **Idioma** | `23-02-spy-en-es` (8 atores × EN/ES); família GRAM (6 idiomas) | conceito e layout |
| **Duração** | `base-ingles` (4 avatares × curta ~50s / longa ~70-77s) | ator e layout |
| **Hook / ângulo** | `spy-gram/ads-en` — GD-AD01 a AD10, 10 ângulos distintos | formato e produto |
| **Casting UGC** | `ingles-17-08` — 10 creators reais | roteiro |

## Catálogo de layouts (extraído de cr02 + cr05)

| # | Layout | Onde aparece |
|---|---|---|
| L1 | faixa de hook no topo + talking head + screen recording embaixo | CR05-V1 (= o wpp-01 campeão) |
| L2 | screen + faixa + head + faixa + b-roll — 5 bandas horizontais | CR05-V2, CR02-V5 |
| L3 | head e screen lado a lado, faixa de hook em cima, legenda embaixo | CR05-V3, CR02-V2 |
| L4 | b-roll cinematográfico em cima + faixa + talking head embaixo | CR02-V3, CR02-V4 |
| L5 | head recortado (fundo removido, contorno branco) sobreposto ao screen | CR05-V5 ⚠️ REJEITANDO |
| L6 | head em quadro cheio + insert pequeno de celular + card de CTA | CR02-V6 |
| L7 | conversa falsa de WhatsApp em cima + terminal + head + lista de chats | CR02-V7, CR05-V7 |

## Elementos recorrentes (o kit de peças)

- **Faixa de hook** em caixa colorida — vermelha (spy-zap), magenta (spy-gram), amarela (wpp-01).
- **Legenda karaokê** 2–4 palavras, amarela/verde/branca com contorno.
- **Insert do funil** — `Accessing WhatsApp…` (zap) / `Connecting to Instagram…` (gram).
- **Lista de chats** com tags `DELETED` / `SUSPICIOUS` e badges vermelhos.
- **Terminal hacker** — `root@zapspy:~#`, TOR, encryption bypassed.
- **Card de CTA** — `CLICK THE LINK BELOW AND SEE THE TRUTH NOW` + setas ⌄⌄⌄ amarelas.
- **B-roll de dor** — pessoa olhando o celular na chuva/na cama/andando na rua.

## Clusters de duração

- **Curtos 18–33s** — `ads-en` (17,9–32,6s), `criativos-personagens` (23,9–31,2s), `cr02` (21,4–32,1s)
- **Médios 44–57s** — `base-ingles` curtas, `cr05` (51–57s), família GRAM não-PT
- **Longos 62–82s** — `base-ingles` longas, `23-02` ES, GRAM PT

## Sinal de compliance no nome do arquivo

`CR05-SPY-V4-J-EN REJEITANDO.mp4` e `CR05-SPY-V5-J-EN REJEITANDO.mp4` — dois dos sete do lote cr05
carregam `REJEITANDO` no nome. São justamente os layouts **L5 (head recortado sobre o screen)** e o
multi-painel de WhatsApp. Sinal de reprovação da Meta gravado na convenção de nome.

## Ângulos de hook já testados (spy-gram/ads-en, verbatim)

```
AD01  I found something i wasn't even looking for...
AD02  You start noticing the little things...
AD03  The worst part is realising it was happening right infront of me...
AD04  You know when something just feels off...
AD05  I kept thinking I would be the first to know...
AD06  You think you would be the first to find out...
AD07  The second I walk into the room, the phone flips...
AD08  Most people believe they would notice right away...
AD09  i always thought deleted messages were gone for good...
AD10  I noticed she always took the phone with her...
```

E em `criativos-personagens`: `THERE'S A DETAIL` · `I FOUND SOMETHING BY ACCIDENT.` ·
`Feel like they're hiding something?` · `EVER FEEL SOMETHING'S HIDDEN?` · `I ALWAYS THOUGHT I'D KNOW FIRST.`

**Dois de dez ângulos do `ads-en` (AD05, AD06) usam o device "primeiro a saber"** — o mesmo binário
forçado escolhido pro sticker do Roteiro D. Já é repertório validado da casa.
