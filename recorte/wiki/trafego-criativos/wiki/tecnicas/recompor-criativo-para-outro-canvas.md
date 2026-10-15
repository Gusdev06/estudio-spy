# Recompor criativo para outro canvas

Mudar a proporção de uma peça pronta sem letterbox e sem mexer no ritmo.

## O princípio

O criativo não é um retângulo, é uma **pilha de camadas com âncoras diferentes**. Reformatar é
redecidir a âncora de cada uma no canvas novo, não redimensionar o conjunto.

| camada | âncora | o que acontece na troca de canvas |
|---|---|---|
| tarja / gancho | topo | escala pela **largura**, fica em y0 |
| bloco gráfico / card de UI | **rodapé** | escala pela largura, encosta na base |
| karaokê | preso ao bloco | mantém o delta medido contra o topo do bloco |
| rosto full-bleed | rodapé | escala pela largura e **perde altura no topo** (cabelo) |

A altura que sobra sai do material que aguenta: cabelo, b-roll, screen recording. Nunca do
grafismo, que carrega a copy.

## Qual offset de corte usar

O offset que **reproduz a relação medida no original** entre a boca e o topo do card. No molde spy
isso deu exatamente o corte máximo (tudo ancorado no rodapé): 10px de folga no original, 10px no
canvas novo. Não foi escolha, foi o que a medição pediu.

⚠️ **Offset por peça vira segunda alavanca.** Num lote que mede ator, enquadramento diferente por
peça quebra a leitura. Use o mesmo corte nas peças do lote e deixe o spread herdado das placas
como está. Ver [[variar-uma-alavanca-por-vez]].

## Split-screen: orçamento de altura por painel

Pilha de 3–5 painéis não aceita "corta o rosto". Decida painel a painel:

- painel de rosto grande → tira dele (é full-bleed, perde cabelo)
- painel de rosto que já é uma **fresta** (só os olhos) → **não tira nada dele**; os painéis
  decorativos (b-roll, screen) absorvem a perda inteira
- faixas de copy → intactas sempre

Cortando b-roll e screen, **mantenha o topo**: é onde ficam header, título e os rostos.

## Reescalar PNG de texto, não re-renderizar

Se o renderizador original não está versionado, **reescale o PNG** em vez de refazer o card.
Re-renderizar arrisca quebra de linha diferente, e o layout precisa ser idêntico. Um PNG de texto
grande reduzido 7,7% não perde nitidez, e a proporção contra a largura do frame fica exata.

Corolário: **versione o script de build junto com a peça.** O do lote 3 morreu no `/tmp` e custou
uma tarde de engenharia reversa.

## Prove o modelo antes de usar

Reconstrua **uma peça no tamanho original** a partir das fontes e diferencie contra a que shippou.
Se não bater no piso de ruído do H.264 (~2/255), o modelo está errado.

Foi assim que apareceu o karaokê 6px fora do lugar: a faixa dava **15,52/255** contra piso 2,10.
Sem esse passo o erro entraria nas 8 peças. É o mesmo raciocínio de [[teste-que-pode-falhar]] —
a reconstrução vale porque **podia não bater**.

Relacionadas: [[ratio-de-entrega-por-placement]] · [[catalogo-de-layouts-spy]] ·
[[teste-que-pode-falhar]] · [[variar-uma-alavanca-por-vez]]
