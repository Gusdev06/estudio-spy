---
name: edicao-precisa
description: Método pra executar feedback humano preciso sobre um vídeo (corte, legenda, motion graphic) com zero regressão — re-transcrever a janela apontada, nunca cortar no meio de palavra, o ouvido do humano vence a transcrição, verificar olhando o frame renderizado, e mapear cada pedido pra uma causa concreta no código antes de mexer. Use quando o usuário mandar feedback de edição ("corta em 1:07", "tá gaguejando aqui", "remove o card duplicado", "ficou parado"), pedir revisão de um vídeo já montado em Remotion/ffmpeg, ou quando um corte/legenda precisa bater no timestamp exato. Reconstruída em 2026-09-16 a partir do METODO.md do projeto mandarimvideo.
---

# Edição precisa — como executar feedback de vídeo sem regressão

Método extraído do projeto `mandarimvideo` (Remotion + `video-use`). Vale pra
qualquer pipeline onde a edição é código (lista de cortes + overlays ancorados
em tempo) e um humano dá feedback por timestamp.

## 1. Fonte única de verdade + tempo derivado

- Os cortes vivem numa lista única, em **segundos do arquivo original**
  (`remover: [{ de, ate, motivo }]` em `src/cortes.ts`).
- Uma função (`paraCortado(t)`) converte tempo original → tempo no vídeo
  montado. **Todo** overlay/legenda é ancorado no tempo **original**, nunca no
  cortado.
- Mexer em 1 linha de corte reposiciona sozinho duração, montagem e todos os
  elementos. Nunca re-cronometre à mão.

## 2. Edição não-destrutiva

Nada é reencodado no meio do caminho. O corte é uma lista; o artefato é
remontado a cada render. Guarde a **decisão**, materialize depois.

## 3. Evidência acima de suposição

- Todo corte é validado contra timestamp de **palavra**, não de frase.
- **Regra dura: nunca cortar no meio de uma palavra.** Corte dentro de um
  token soa como gaguejo novo.
- **Nunca confie em transcrição herdada** de outra sessão ou de resumo. Quando
  o humano aponta um erro num timestamp:
  1. isole a janela (`ffmpeg -ss X -to Y -i src -c copy janela.mp4`);
  2. re-transcreva **só ela** (`video-use` → `transcribe.py janela.mp4
     --model turbo`);
  3. decida o corte com esses timestamps, somando o offset de volta.
- Heurística de gaguejo escondido: **token com duração 2–3× o normal para o
  seu tamanho = repetição que o ASR fundiu num token só.** Ouça/olhe ali.

## 4. O ouvido humano ganha da transcrição

Caso real: 3 passadas, 2 modelos, nenhum separou o gaguejo em `沒有`; só o
usuário ouvindo pegou. Se a transcrição discordar do humano, **o humano
ganha**. Não trate a discordância como erro dele.

## 5. Restrições duras vencem instruções

Defina as invioláveis antes de receber pedidos (ex.: `rosto = y900→1250,
nunca cobrir`; geometria só em `palco.ts`). Quando um pedido colide com uma
delas (ex.: "centraliza tudo" cobriria o rosto), resolva a favor da restrição
e **declare o desvio** — nunca aplique em silêncio nem obedeça cegamente.

## 6. Feedback → causa concreta antes de agir

Nenhum item de feedback vira tarefa antes de virar **linha de código
identificada**. Monte a tabela:

| Feedback | Causa concreta |
|---|---|
| "remover card duplicado" | `ClipeCena.tsx:54` desenha em y1300, legenda em y1360 → dois blocos |
| "flash preto entre imagens" | dois clipes com fade próprio sobrepostos a 50 % expõem a camada de baixo |
| "talking head parado" | push-in 1.0→1.08 em 111 s — imperceptível |

A tabela também mostra quando dois pedidos têm a mesma causa (uma correção só).

## 7. Varredura sistemática, não pontual

Quando o cliente reporta 1 gaguejo, não pare nele: rode a varredura inteira
(n-grams repetidos, tokens longos demais, toda região de silêncio ≥ 0,4 s),
pra próxima rodada de feedback não ter nada sobrando.

## 8. Auto-verificação antes de entregar

Não declare "está bom" a partir do código. Extraia frames nos pontos de
risco (`npx remotion still Overlays out/f.png --frame=N` ou `ffmpeg -ss`) e
**olhe**. O card duplicado foi confirmado vendo o frame, não lendo o
componente.

## 9. Memória do projeto

O `CLAUDE.md` da pasta de trabalho guarda: pré-requisitos · regras
permanentes do usuário · pipeline numerado · design system · **erros já
cometidos**. Todo erro cometido vira uma linha na última seção — é ela que
impede regressão entre sessões.

## Checklist por rodada de feedback

- [ ] Cada pedido tem causa concreta (arquivo:linha)?
- [ ] Timestamps apontados foram re-transcritos em isolamento?
- [ ] Nenhum corte cai dentro de uma palavra?
- [ ] Varredura completa rodada (não só o ponto reportado)?
- [ ] Restrições duras respeitadas — desvios declarados?
- [ ] Frames reais renderizados e olhados nos pontos de risco?
- [ ] Erro novo registrado no `CLAUDE.md` do projeto?
