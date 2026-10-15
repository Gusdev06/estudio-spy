---
tipo: fonte
tags: [casting, copy, medicao, spy-zap, centerpag, lote-4]
data: 2026-09-01
---

# fonte — seleção dos atores do lote 4 + conferência das duas copies (01/09/2026)

Lote 4 do ZAP. Duas perguntas: **as duas copies de locução batem?** e **quais 2 rostos novos entram nos slots 3 e 4?** Nenhuma geração paga.

## Entradas

- `projects/mentoria-spy/criativos-personagens/` — 10 arquivos candidatos.
- `centerpag-detect/escalados/whatsapp/` — peças `10` (Lauren) e `20` (Gonçalo) + `06` (Isabella, controle).
- Cru em `raw/2026-09-01-selecao-atores-lote4.md`. Frames em `centerpag-detect/referencias/frames-atores-lote4/` e `frames-copy-lote4/`.

## Respostas

**Copies.** O `.txt` **não contém a locução** — só headline/CTA/link (card agrupado). Conferido contra a legenda karaokê queimada: **Lauren bate integralmente**; **Gonçalo tem uma divergência — `discrete` → `discreet`**, corrigida no teardown do lote 3 com o valor velho marcado. Contagem de palavras inalterada, então a grade de palavras por beat do roteiro não se mexe. Método em [[ler-copy-na-legenda-queimada]].

**Atores.** Escolhidos `AD05 - PERSONAGEM 1` (janela limpa 19,50s) e `AD05 - PERSONAGEM 3` (18,40s), ambos 1080×1920 / 60 fps.

## Achados que viraram página

- **Os 10 candidatos são anúncios prontos, não footage de ator** — legenda queimada nos 10, painéis de UI e PII de terceiro (`dodoelady`, `@privatinaovr`). Só se aproveita faixa recortada → [[peca-pronta-nao-e-banco-de-atores]] e [[pii-de-terceiro-em-criativo]].
- **Nenhum dos 10 chega aos ~22s do molde** — o melhor dá 19,50s. Medida e os três detectores que mentiram no caminho → [[janela-limpa-continua-como-criterio-de-casting]].
- **A faixa limpa não preenche a região do ator do molde**: 1080×960 escala pra 1170×1040, contra 1170×2038 necessários — **51%**. Frame cheio cobre, mas traz os overlays. Trava aberta pro Bisturi.
- **"Isabella Walker" é uma Página, e o ator dela é um homem** — a premissa de casting do briefing estava invertida → [[nome-de-pagina-nao-e-nome-do-ator]].

## Contradições registradas

1. **Premissa de casting invertida.** Briefing pedia rostos "distintos da Isabella" supondo atriz; o ator é homem. O dado que desmentia já estava no [[fonte-teardown-lote3-2026-09-01]] ("4 vozes masculinas distintas"), não cruzado. **Resolvida**: primeiro escolhi dois rostos femininos; o adendo abaixo mostrou que a copy verbatim é generificada (homem falando da parceira), e a escolha final virou **dois homens**.
2. **Grid acopla rosto e gênero.** Slots 1, 2 e a peça original são homens; 3 e 4 são mulheres. O teste deixa de isolar "rosto". **Em aberto — decisão do Gusta**, não deste documento.
3. **Texto de tarja: fonte ≠ kit.** O briefing lista como FIXO `CLONE YOUR WIFE'S OR HUSBAND'S / WHATSAPP RIGHT NOW` — esse é o texto da **peça-fonte**, corretamente reportado no teardown do lote 3. A peça que shippou usa outro (`YOU DON'T NEED THEIR PHONE. / YOU NEED THE NUMBER.`, evidência no kit e nos frames do lote 3, achado do Isca). **Não confundir os dois**; nenhum documento de seleção confirma texto de tarja, só a geometria — e ela mesma saiu corrigida para **19,69% / 498px** (ver abaixo).
4. **Hierarquia de fonte precisa ser campo a campo.** "O `.txt` manda" não se aplicava à locução, que o `.txt` não guarda. Registrado em [[ler-copy-na-legenda-queimada]].

## Adendo — varredura por footage masculina (pedido do Isca)

A copy é **generificada e verbatim** (homem falando da parceira: *"my fiance's… her number"*, *"my girlfriend's number"*). Com atriz mulher isso reenquadra a peça sem ninguém ter escolhido. Varri então **os 627 vídeos** de `mentoria-spy/` e `centerpag-detect/` (423 com ≥22s).

**Achou** — e o material limpo é **nosso**, da esteira de avatar, não de concorrente:
- `roteiro-e-2026-08-31/avatares/CRIATIVO-a1-homem-velho.mp4` — **57,10s limpos** em frame cheio, homem negro ~68.
- `lote-5-avatares/final-h2-grisalho-52.mp4` — **26,10s limpos** (8,10→34,20s), homem grisalho ~55.
- Reservas: `sophia-jones-avatar-homem-38/versao-A-mudo.mp4` (34,10s, mas arquétipo colado no ator da Isabella) e `final-h1-jovem-27.mp4` (26,10s).

Isso **derruba as duas travas** do corpo da fonte: os 22s passam a existir com folga e o frame cheio limpo preenche a região do ator. Todo o resto do corpus (`criativos-crus/spy-zap/*`, `troca-avatar-studio/jobs/*`, `anuncios/`, `tratados/`, `escalados/`) é anúncio pronto com legenda queimada → [[peca-pronta-nao-e-banco-de-atores]].

**Dos 10 originais, só 2 homens distintos** (AD04-P1 = AD05-P2), e o melhor dava 16,10s — a pasta não resolvia nem com a premissa corrigida.

⚠️ O detector errou **mais duas vezes** aqui (luminária laranja e camisa escura acusadas como overlay); o contact sheet desmentiu. Reforça [[janela-limpa-continua-como-criterio-de-casting]].

## Correção recebida — altura da tarja: 498px, não 494

Isca mediu e eu reconferi de forma independente: as linhas verdes da fonte são `y 0–125` **inclusive** = **126** linhas de 640 = **19,6875%** → **498,49px** em 2532. Eu tinha escrito 19,53% / 494px — off-by-one ao contar 125. Confirmado em 5 colunas (x 10/90/180/270/350), 126 linhas nas cinco. O [[fonte-teardown-lote3-2026-09-01]] já trazia `126px de 640 = 19,69%` **certo**; o erro era só do doc de seleção, já corrigido lá.

**Por que 4px importam:** se alguém reconstruir a arte a partir de 494 em vez de reusar `kit/tarja.png`, as peças do lote 4 passam a diferir do controle Isabella **também** por altura de tarja — num lote que só pode ter uma alavanca (rosto+voz), 4px viram alavanca. Ver [[variar-uma-alavanca-por-vez]]. Reusar o asset resolve.

## Páginas geradas

- [[peca-pronta-nao-e-banco-de-atores]]
- [[janela-limpa-continua-como-criterio-de-casting]]
- [[nome-de-pagina-nao-e-nome-do-ator]]
- [[ler-copy-na-legenda-queimada]]
