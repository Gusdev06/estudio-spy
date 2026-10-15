---
tipo: template
atualizado: 2026-09-03
tags: [template, teardown, criativo, swipe]
---

# Template — teardown completo de criativo

> Uso: o Peneira preenche TODAS as 14 seções pra cada peça que vai ser replicada. Seção sem dado
> recebe `n/a — motivo`, nunca some. O Isca e o Bisturi trabalham só com o que está aqui:
> se não está no teardown, não existe. Modelo preenchido:
> `projects/mentoria-spy/gram-detect/referencias/2026-09-01-teardown-vencedor-gram-sophia-jones.md`.

Frontmatter obrigatório: `tipo: referencia-criativo`, `ad_id`, `fonte` (URL da Ad Library),
`arquivo_peca` (caminho relativo a `projects/mentoria-spy/`), `layout` (L1–L10 ou `novo`).

## 1. Identificação e sinais de escala
Página · ad_id · duração · resolução/aspecto · idioma da locução · dias no ar · rank de impressões ·
flag de volume · quantas peças a página roda no mesmo ângulo. **Ranking é proxy de Ad Library,
não performance** — repetir o aviso. Nenhum número inventado.

## 2. Copy da Meta (reproduzir como está)
Primary text · headline · descrição · botão · link de destino. Em bloco de código, campo a campo,
conferido contra o `manifest.json`. Anotar divergência de idioma se houver.

## 3. Locução — transcrição com tempo
Texto corrido + tabela `tempo | fala`. Método (whisper local, ffmpeg). Marcar a keyword de cada
frase (a que vira verde no karaokê).

## 4. Gancho — as três camadas dos primeiros 3 s
| Camada | Conteúdo | Job |
|---|---|---|
| Visual (frame 1) | o que está na tela em t=0: rosto? print? b-roll? UI? | parar o dedo |
| Texto na tela | faixa/headline queimada, palavra por palavra | prometer |
| Falado | primeira frase da locução | abrir o loop |
Exportar o **frame 1** (`ffmpeg -ss 0 -frames:v 1`) pra `referencias/frames/<ad_id>-t0.jpg`.

## 5. Estrutura e cortes (medido, não chutado)
Tabela `bloco | início | fim | o que aparece | o que se fala | função (gancho/dor/mecanismo/prova/CTA)`.
Fronteiras de bloco medidas com a skill `clonar-edicao` (`medir-fronteira-de-bloco-em-video`).
Exportar 1 frame por bloco pra `referencias/frames/`.

## 6. Formato e layout de tela
Layout do catálogo (`[[catalogo-de-layouts-spy]]`, L1–L10) ou `novo` com descrição.
Bandas em % e px: faixa de hook (y início–fim), talking head, painel/screen, legenda.
Blocos do kit usados: faixa colorida · karaokê · insert do funil · lista de chats · terminal ·
card de CTA · b-roll de dor · faixa fixa sem legenda.

## 7. Visual — cores, tipografia, elementos
- **Paleta**: 3–5 cores dominantes em hex, medidas do frame (não "vermelho": `#E0192B`). Qual é
  a cor da faixa, do karaokê, da keyword, do fundo do card.
- **Tipografia**: família (ou a mais próxima), peso, caixa (ALTA/mista), contorno/sombra,
  tamanho relativo à largura (%), alinhamento.
- **Legenda**: n de palavras por bloco, cor base, cor da keyword, posição y.
- **Elementos de UI**: qual app/tela aparece, é real ou mockup, idioma da UI.
- **Pessoa**: gênero, idade aparente, enquadramento (busto/rosto), fundo, luz, olha pra câmera?
- **B-roll**: o quê, quantos clipes, duração de cada.
- **Movimento**: zoom, corte seco, transição, ritmo (cortes por 10 s).

## 8. Áudio
Voz (gênero, sotaque, TTS ou humana, lipsync?) · música (sim/não, gênero, volume) · SFX.

## 9. Oferta, prova e CTA
Promessa · mecanismo · prova mostrada (print, número, depoimento) · CTA falado · CTA na tela ·
o que acontece no clique (destino).

## 10. Público e POR QUE vende (o diagnóstico do estrategista)
- **Avatar**: quem está do outro lado (idade, situação, o que sente às 2 da manhã), em 3 linhas.
- **Nível de consciência** (Schwartz): inconsciente / problema / solução / produto / mais consciente.
  Onde o ad pega a pessoa e pra onde leva.
- **Dor e desejo**: a dor nomeada, o desejo prometido, a emoção que move (medo, ciúme, alívio, controle).
- **Big idea e mecanismo**: a ideia em uma frase; o "por quê funciona" que o ad vende (ex.: rastros
  que a pessoa deixa sem perceber).
- **Crença instalada e objeção neutralizada**: o que a pessoa precisa acreditar pra clicar; qual
  objeção o ad mata e como (sem login, grátis, em segundos).
- **Motor de retenção**: o que segura até o CTA (loop aberto, revelação adiada, prova progressiva).
- **Veredito**: por que ESTE ad vende e o similar não — 3 a 5 causas, ordenadas por peso.

## 11. O que roubar / o que variar
Duas listas curtas. "Roubar" = o molde fixo que não se mexe. "Variar" = os eixos de teste
(`[[eixos-de-variacao-de-criativo]]`): uma alavanca por lote.

## 12. Arquivos pro portal
Tabela `o que | caminho relativo a projects/mentoria-spy/`: vídeo canônico, thumb, txt, frames
exportados, md5 conferido contra o manifest.

## 13. Ingestão no wiki
Lista das páginas criadas/atualizadas em `wiki/trafego-criativos/` (fonte em `raw/`, página do
criativo, técnicas novas, `index.md`, `log.md`).

## 14. PLANO DE RÉPLICA — os ads novos (obrigatório)
Três ads novos, cada um numa tabela: `hook falado | hook na tela | hook visual (frame 1) | body
(bloco a bloco, com a fala) | prova | CTA falado + na tela | avatar (quem fala, enquadramento) |
formato/layout | edição (cortes, legenda, paleta, tipografia) | duração`.
- **Ad A — clone fiel**: o molde inteiro, copy palavra por palavra quando a ordem for copiar. É o controle.
- **Ad B e C — melhores que o original**: cada um muda **uma alavanca** e diz qual e por quê, em uma
  linha, apontando pra causa do veredito (seção 10) que ela ataca. "Melhor" = hipótese com
  justificativa, nunca promessa de resultado. Sem número inventado.
- Custo estimado por ad (duração × preço unitário) e o que reaproveita do original.
