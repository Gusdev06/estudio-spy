# Como a detecção funciona, e o que fazer quando ela erra

## A assinatura de linha

Para cada linha horizontal do frame o analisador calcula três números:

- **média** dos canais — quão clara é a linha
- **desvio horizontal** — quanta variação existe ao longo dela. Área lisa (barra sólida, parede) dá desvio baixo; rosto e captura de tela dão desvio alto.
- **vermelhidão** — `R − (G+B)/2`. Barra de caption quase sempre é colorida, e essa é a forma mais barata de achá-la.

Média sozinha não serve: uma barra de UI clara e um rosto claro têm a mesma média. É a combinação dos três que separa.

## Achar o corte

Compara a assinatura de frames consecutivos amostrados a cada 0,5s. Onde a distância dá um salto, houve mudança. Depois refina por busca binária até a precisão pedida (`--precisao`, default 0,05s).

**Isso pega mudança de conteúdo junto com mudança de layout.** Um b-roll trocando muda a assinatura sem mudar a estrutura. O filtro vem no passo seguinte.

## Separar layout de conteúdo

Depois de achar os candidatos, o script mede as faixas dos dois lados de cada corte e **funde** os segmentos cuja estrutura de faixas é a mesma. Só sobrevive como corte de layout o que realmente reorganizou a tela.

A comparação usa só as **faixas grandes** (≥15% da altura). Comparar a lista inteira é frágil: uma barra de caption às vezes sai como um bloco e às vezes como dois, e a comparação falharia por isso, não porque o layout mudou.

## Achar as faixas

Duas exigências, e as duas importam:

**Estabilidade.** O perfil de gradiente é calculado em 5 frames do segmento e tomado o **mínimo** entre eles. Só sobrevive a fronteira que existe em todos os frames. Sem isso, o feed do Instagram rolando no painel de baixo vira "faixa" e a análise devolve lixo.

**Nitidez.** A fronteira precisa ser um pico local pronunciado (2,5× a mediana da vizinhança). Divisão de layout troca de fonte em uma ou duas linhas; a linha do teto de um cômodo ou o encosto de um sofá sobem devagar. Sem essa exigência, o segmento de tela cheia vem picado em faixas que não existem.

Por fim, faixas vizinhas de **mesmo caráter** são fundidas — se as duas têm média, vermelhidão e textura parecidas, são a mesma fonte visual e a fronteira entre elas era ruído.

## Quando erra

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| Corte a mais, no meio de um segmento | Troca de conteúdo forte demais (corte de b-roll) | Suba `--limiar`. Ou ignore: a lista de descartados já mostra o que ele considerou |
| Corte de layout não detectado | Layouts parecidos demais entre si | Baixe `--limiar`, ou passe `--passo 0.25` para amostrar mais fino |
| Faixa a mais em tela cheia | Borda de cena muito nítida (moldura, batente) | Suba `--min-altura` |
| Faixa de menos | Painéis com estatística parecida | Confirme no frame e passe `--topo` na mão pro montar_composto |
| Corte impreciso | Amostragem grossa | `--precisao 0.02` |

**A saída é ponto de partida, não veredito.** Extrair um frame de cada segmento e olhar custa segundos e é o que separa uma montagem certa de uma emenda visível.

## Por que a escala do avatar não é calculável

O caminho óbvio seria medir onde começa a cabeça nos dois vídeos e derivar a proporção. Não funciona: "topo da cabeça até o fim do quadro" mede coisas diferentes em cada vídeo, porque o quadro do talking head novo desce até o colo e o da faixa da referência é cortado no peito. Casar esses dois números produz uma escala errada com aparência de precisa.

Medir o tamanho da cabeça de verdade exigiria detecção facial, que é peso demais para o ganho. Então: `0.70` é um começo empírico, e `--preview` resolve em duas iterações. Preferimos um default honesto com um jeito rápido de conferir a uma fórmula que erra em silêncio.

## Reaproveitar painel de baixa resolução

O criativo do swipe file costuma vir em 360×640 (o que o download entrega), enquanto a saída é 1080×1920. O painel reaproveitado sobe 3× e fica mole — nítido o bastante para ler a UI, longe do padrão do resto.

Não tem correção por filtro; é informação que não existe no arquivo. Duas saídas de verdade:

1. **Conseguir o original em resolução maior** (Ad Library em tela cheia, ou o arquivo com quem rodou). Aí é só remontar; o resto do pipeline não muda.
2. **Recriar o painel** em vez de reaproveitar — regravar a captura de tela, gerar o b-roll de novo. Custa tempo, e muda uma variável a mais no teste.

Diga qual dos dois está valendo na entrega. Uma faixa mole que o usuário não esperava vira retrabalho.
