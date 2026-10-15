# Flora 959352790554428: variação 1 com outra dupla e outro estúdio (2026-09-25)

**Original:** `~/Downloads/Flora Zamorano Castejón_959352790554428_2026-09-25.mp4` (md5 `56d84641…`). É 360×640, 30 fps, 1026 frames, 34,2 s. A cópia está em `REFERENCIA-original.mp4`. É o mesmo formato do podcast WPP (lote 40): um layout de post sobre fundo preto.
**Peça:** `pecas/variacao.mp4`. Tem 360×640, 30 fps, **1026 frames**, 34,20 s. O stream de áudio é o do original, copiado: o md5 é `56739afc…` nos dois.

## Molde medido
| camada | medida |
|---|---|
| Título | caixa branca em y 44–150, "HOW TO READ YOUR PARTNER'S MESSAGES ON YOUR PHONE". Fica **fora** da janela e sai intocado |
| Janela de vídeo | 360×303 em y 168–470. É a única área trocada |
| Karaokê | y ~520–575, sobre preto. Fica **fora** da janela e sai intocado |
| Estrutura (nº de frame) | mulher n 0–116 · homem n 117–225 · mulher n 226–266 · painéis do funil n 267–884 · mulher n 885–1025 |
| Transição | n 263–266: um *light leak* laranja cobre o quadro inteiro por cima da mulher, e o painel entra no n 267 |
| Fala | não há sobreposição: silêncio em 3,65–4,05 s e em 7,40–7,60 s. Nenhum clipe precisou de trecho mudo |

## Pipeline (de `projects/mentoria-spy/`)
1. `gerar-bases.py`: gpt-image-2/edit (medium, 1k) sobre o frame da janela ampliado 3×. A mulher sai do n 30 e o homem do n 150. A pose e o enquadramento são os mesmos, e a pessoa e o estúdio mudam.
2. `gerar-clipes.sh` (SEED=7, prompt só em positivo): 4 clipes Pruna (a1 0–3,9 · b 3,9–7,53 · a2 7,53–9,53 · a3 29,5–34,2). Cada um leva o áudio original do bloco. Saem em 1024×896 e 24 fps. Os downloads foram validados decodificando o arquivo inteiro.
3. `checar.py`: moldura, lateral, 2º rosto, rosto sumindo, tamanho e identidade. Não houve moldura, gente entrando nem 2º rosto. O alerta "rosto muda" disparou por causa do giro de cabeça (perfil → 3/4). Conferi no olho em `conferencia/clipes-s7.jpg`: é a mesma pessoa do começo ao fim.
4. `montar.py pecas/variacao.mp4`: montagem em numpy, com emendas por número de frame. O rosto de cada clipe é escalado e posicionado no centro e na altura medidos no original (YuNet, maior score). Só a janela é substituída. No leak (n 263–266), a luz é lida nas faixas pretas logo acima e abaixo da janela, onde a base é preta e portanto só aparece a luz. Depois ela é interpolada por coluna, e o escurecimento de cada canal é ajustado. Por fim, a luz é reaplicada sobre a mulher nova, então nada da original entra.

## Elenco e cenário
| papel | original | novo |
|---|---|---|
| A (explica) | mulher ~40, cabelo escuro liso, blazer azul-marinho | mulher ~38, pele morena clara, cachos ruivo-escuros presos num coque baixo, argolas douradas, suéter mostarda |
| B (pergunta) | homem ~35, cabelo escuro, barba, camisa escura, de perfil | homem ~36, cabelo loiro-escuro curto, barba castanha aparada, suéter grafite, de perfil |
| estúdio | parede verde-oliva, abajur verde, monitor com WhatsApp Web | tijolo aparente, lâmpada Edison âmbar, estante de madeira, espuma acústica, sem telas |

## Varredura final
- A janela foi trocada em todos os 408 frames em que a dupla original aparece (n 0–266 e 885–1025). A diferença média ficou em 64 de mediana. O mínimo foi 14,4, no n 266, que é o frame quase branco do leak.
- A correlação de bordas entre original e peça nesses frames tem máximo de 0,07 e mediana de 0,00. Num painel mantido ela é 1,00. Não sobra contorno da dupla original.
- Painéis e tudo fora da janela: a diferença máxima é 3,3, que é só a recompressão.
- O YuNet encontrou no máximo 1 rosto (≥ 0,86) por frame. Os "rostos" nos painéis (n 320 e 749) são as flores de censura do próprio original.
- Folhas conferidas no olho: `conferencia/orig-vs-peca-10.jpg`, `emendas-1.jpg`, `emendas-2.jpg`, `leak-transicao.jpg` e `casting.jpg`.

## Custo real: US$ 0,533
Foram 2 imagens gpt-image-2/edit (0,133) e 4 clipes Pruna (0,10 + 0,10 + 0,075 + 0,125). Não houve regeração nem estorno.

## Concessões
- O leak foi reconstruído, não copiado. No n 266 a mulher nova aparece um pouco mais que a original sob o clarão, mas com o mesmo tom.
- A resolução da fonte é baixa, 360×303 de janela. A peça sai na mesma dimensão do original.
