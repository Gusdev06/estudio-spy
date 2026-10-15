---
name: clonar-edicao
description: "Reconstrói a EDIÇÃO de um criativo de vídeo que já escalou — split screen, faixas, ponto de corte — usando um talking head novo por cima, e reaproveitando os painéis do original (screen recording, b-roll, barra de caption). Mede as faixas e os cortes do original por análise de imagem em vez de chute, e monta com ffmpeg. Use SEMPRE que o usuário quiser: copiar a estrutura/edição/montagem de um criativo, refazer um anúncio com a mesma divisão de tela, 'deixar do mesmo jeito só trocando a pessoa', reaproveitar a animação de baixo de um vídeo, descobrir onde um criativo corta ou como ele está dividido, ou montar um split screen igual ao de uma referência. Vem depois da skill trocar-avatar, que produz o talking head."
---

# Clonar a edição de um criativo

A `trocar-avatar` entrega um talking head limpo. Esta aqui devolve a **edição** em volta dele: a divisão de tela, as faixas, o instante do corte — reaproveitando os painéis do criativo original.

A premissa é a mesma: o criativo campeão já provou converter, e a estrutura de edição faz parte do que foi testado. Você não está desenhando uma montagem; está **remontando a mesma**, com outro rosto.

## Por que medir em vez de olhar

Estimar no olho onde termina o talking head e começa o painel de baixo erra por dezenas de pixels, e a emenda aparece. Achar o corte arrastando a barrinha do player erra por meio segundo, e o corte cai no meio de uma palavra.

Os dois números estão no arquivo. Faixas diferentes têm estatística de linha diferente (uma barra de caption é lisa e colorida, um rosto tem textura, uma captura de tela tem bordas retas), e o instante em que essa assinatura muda é o corte.

## Passo 1 — Ler a estrutura do original

```bash
python3 ~/.claude/skills/clonar-edicao/scripts/analisar_estrutura.py referencia.mp4
```

Devolve, por segmento: os limites `y` de cada faixa e os instantes de corte de layout. Exemplo real:

```
360x640 · 30fps · 32.51s
cortes de LAYOUT: 8.66s
(descartados como troca de conteudo, nao de layout: 0.25s, 1.94s, 4.47s)

SEGMENTO 1: 0.25s -> 8.66s · dividido
    y     0-279   (43.6%)  painel
    y   279-358   (12.3%)  barra de caption / lettering
    y   358-640   (44.1%)  painel

SEGMENTO 2: 8.66s -> 32.51s · tela cheia
    y     0-640   (100%)   painel principal
```

O script separa **corte de layout** de **troca de conteúdo**. Um b-roll trocando ou um feed rolando muda a imagem sem mudar a estrutura — se você tratar isso como corte, pica o vídeo em pedaços que não existem. Ele só considera corte real quando a estrutura de faixas difere dos dois lados.

**Confirme com o olho.** Os papéis das faixas ("barra de caption", "painel") são palpite estatístico. Extraia um frame de cada segmento e olhe antes de cortar em cima:

```bash
ffmpeg -y -ss 4 -i referencia.mp4 -vframes 1 seg1.jpg
```

## Passo 2 — Escolher o corte no vídeo novo

O corte do original quase nunca cai no mesmo segundo do vídeo novo — o avatar novo fala em ritmo próprio.

A regra: **corte na fronteira de frase, não no relógio.** Veja o que está sendo dito no instante do corte do original e ache a mesma frase no vídeo novo. Se a `trocar-avatar` gerou por clipes, a emenda entre clipes provavelmente já está no lugar certo — use ela, porque ali já existe um corte natural.

Exemplo do caso real: o original cortava em 8,66s, bem no início de "You don't need to guess". No vídeo novo, o clipe 1 terminava em 8,04s exatamente nessa frase. Corte em 8,04s, não em 8,66s.

## Passo 3 — Acertar o enquadramento antes de renderizar

Este é o passo que mais se erra, e ele é barato de acertar e caro de descobrir depois.

O talking head novo foi gerado em quadro cheio 9:16. A faixa de cima é bem mais baixa que isso. Colar o vídeo direto deixa a cabeça enorme — no caso real ela ocupou 85% da faixa contra ~70% no original, e virou rosto colado onde a referência tinha plano com ombros.

A correção é reduzir o avatar e preencher as laterais com uma cópia desfocada dele mesmo. Funciona bem quando o fundo é liso; a emenda some.

Renderize **um frame** e compare:

```bash
python3 ~/.claude/skills/clonar-edicao/scripts/montar_composto.py \
  --ref referencia.mp4 --avatar novo.mp4 \
  --topo 279 --corte-ref 8.66 --corte 8.04 \
  --escala 0.70 --preview pv.jpg
```

Sai um JPG com a referência à esquerda e o composto à direita. Compare o **tamanho da cabeça**. Maior no seu? baixe `--escala`. Menor? suba. Ajuste `--headroom` se sobrar ou faltar ar acima da cabeça.

Não existe fórmula confiável para essa escala sem medir a cabeça de verdade, então `0.70` é ponto de partida, não resposta. Duas ou três iterações de preview custam segundos.

## Passo 4 — Renderizar

```bash
python3 ~/.claude/skills/clonar-edicao/scripts/montar_composto.py \
  --ref referencia.mp4 --avatar novo.mp4 \
  --topo 279 --corte-ref 8.66 --corte 8.04 \
  --escala 0.70 -o criativo-final.mp4
```

O áudio vem do vídeo novo, inteiro e contínuo — só a composição da imagem muda no corte. Saída padrão 1080 de largura, no mesmo aspect ratio da referência.

## Passo 5 — Conferir antes de entregar

Extraia frames em volta do corte (um antes, um depois) e confirme que a transição acontece onde devia. Depois rode `/watch` no arquivo final: com o vídeo montado, dá pra ver se o corte cai bem em relação à fala.

Na entrega, diga sempre:

- **A resolução real da faixa reaproveitada.** Se o original veio do swipe file em 360px de largura e a saída é 1080, aquele painel foi ampliado 3× e vai sair mole. Não tem conserto sem uma cópia melhor do original — e vale pedir.
- **O que veio junto do recorte.** Barra de caption, selo de contador, lettering queimado: tudo isso vem no painel e continua no criativo novo. Pode ser o que se quer, ou não.
- **O que o original fazia mal e foi herdado.** Se ele não tinha legenda em dois terços do vídeo, o clone também não tem.

## Casos que fogem do padrão

**Painéis lado a lado (colunas), não faixas.** O analisador lê faixas horizontais. Para divisão vertical, o mesmo método funciona transpondo — rode a análise no vídeo girado 90° (`-vf transpose=1`) e converta os `y` encontrados em `x`.

**Mais de dois segmentos.** O script monta dois trechos (dividido → cheio). Para uma sequência com três ou mais layouts, monte cada trecho separado e concatene com o `montar.sh` da `trocar-avatar`, que já normaliza fps e resolução.

**Faixa de cima não é o sujeito.** Alguns criativos põem o b-roll em cima e o rosto embaixo. `--topo` continua sendo a fronteira; troque qual fonte vai em cada faixa editando o filtergraph, ou gire a ordem no `vstack`.

## Arquivos

- `scripts/analisar_estrutura.py` — mede faixas e cortes. `--json` para consumir programaticamente.
- `scripts/montar_composto.py` — monta. `--dry-run` mostra as contas, `--preview` gera o frame de comparação.
- `references/metodo.md` — como a detecção funciona por dentro, e o que fazer quando ela erra.
- Skills irmãs: `trocar-avatar` (gera o talking head), `watch` (ler o original e revisar a entrega).
