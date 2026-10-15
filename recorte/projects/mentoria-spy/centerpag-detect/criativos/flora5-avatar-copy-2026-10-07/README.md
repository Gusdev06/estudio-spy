# Flora var5 com avatar E copy novos · 2026-10-07 → peças 172–173

Pedido do Gusta: "2 variações dos melhores criativos, dessa vez de avatar e de copy". A Flora var5 foi a 4ª em vendas (02/08–30/09): 22 vendas, ROAS 4,16, CTR 5,5% e o menor custo por venda do top 5 (R$ 61).
Até então as variações da Flora (var1–var11) só trocavam a dupla e o estúdio, e o áudio e o karaokê eram os do original. Aqui também mudam a fala, o título e o karaokê.

## O que mudou
| camada | var5 (mãe) | 172 / 173 |
|---|---|---|
| Título | recortado do original | redesenhado (`p17x/elenco.json → titulo`), 3 linhas na mesma caixa branca |
| Fala | áudio original | diálogo novo (`p17x/roteiro.tsv`), TTS em 2 vozes (A explica, B pergunta) |
| Karaokê | queimado do original | redesenhado sobre preto limpo pro áudio novo, com caixa roxa na palavra falada |
| Dupla + estúdio | latina de headphone, estúdio cinza | novos (abaixo) |
| Painéis do funil | original | original, reencaixados na nova timeline |

| peça | título | dupla | estúdio | duração |
|---|---|---|---|---|
| 172 `chats-apagados` | HOW TO SEE THE CHATS / YOUR PARTNER DELETES / BEFORE BED | etíope ~40, cabelo raspado curto, blusa cobalto × filipino ~38 de óculos, suéter cinza | parede terracota, nicho em arco, capim-dos-pampas | 31,5 s |
| 173 `intuicao` | HOW TO SEE WHO / YOUR PARTNER TEXTS / WHILE YOU SLEEP | branca ~42, rabo de cavalo loiro-morango, gola alta caramelo × samoano ~35 de barba, camisa sálvia | parede azul-petróleo, discos de vinil, pendente âmbar | 30,9 s |

Ganchos: 172 "Your partner deletes their chats every night. You can still read them." · 173 "If your gut says something is off, their phone already knows why."

## Conferência (`conferir.py`, `conferencia/conferencia.txt`)
As duas peças decodificam inteiras, em 360×640 a 30 fps, com 0 silêncios ≥ 0,5 s (medido com `-hide_banner`). O YuNet acha no máximo 1 rosto por frame. As bordas da janela não correlacionam com a dupla original (máx. 0,21 / 0,16), e os painéis batem com o original (dif. ≤ 2,2).
Folhas: `final-2.jpg` (12 instantes por peça), `emendas-p17x.jpg`, `karaoke-sync-p17x.jpg`, `bases.jpg`, `clipes-s7.jpg`.
O agente que produziu foi interrompido depois de renderizar a 173. Por isso a conferência da 173, a `final-2.jpg` e este README foram feitos pelo maestro em seguida, sem gasto novo.

## Custo
≈ **US$ 1,48** pelas 2 peças. O valor é por diferença: o total da chave macbook na WaveSpeed desde 07/10 14:00 UTC deu US$ 8,57, menos US$ 5,23 da Secret e US$ 1,86 do CP108.
