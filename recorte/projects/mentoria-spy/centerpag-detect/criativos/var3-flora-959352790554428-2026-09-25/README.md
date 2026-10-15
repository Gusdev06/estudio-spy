# Flora 959352790554428: variação 3 com outra dupla e outro estúdio (2026-09-25)

O molde, as emendas por frame e o clarão reconstruído são os mesmos da var1. Detalhe completo em `../var1-flora-959352790554428-2026-09-25/README.md`.

**Peça:** `pecas/variacao.mp4`. Tem 360×640, 30 fps, **1026 frames**, e o áudio é o do original, copiado (md5 do stream `317d323d80b5b2ce454825e1aaf93a5a`). A referência está em `REFERENCIA-original.mp4`.

## Elenco e cenário
| papel | novo |
|---|---|
| A (explica) | mulher ~38, pele clara, loira mel lisa na altura do ombro, suéter tricô creme |
| B (pergunta) | homem ~36, sul-asiático, cabelo preto ondulado, barba curta, camisa oxford azul-clara |
| estúdio | sala escandinava clara: paredes brancas, ripado de carvalho claro, monstera, luz do dia, sem telas, texto ou logo |

## Pipeline (rodar de `projects/mentoria-spy/`)
1. `gerar-bases.py`: gpt-image-2/edit (medium, 1k) sobre os frames limpos do original. As refs e os áudios são os mesmos uploads da var1.
2. `gerar-clipes.sh`: 4 clipes Pruna com SEED=7, 720p e prompt só em positivo. Os downloads foram validados decodificando o arquivo inteiro.
3. `checar.py`: `checar.py` deu dois alertas: "lateral mexe" no b, porque o homem gira a cabeça para a câmera, e "rosto muda" no a3, que é giro de cabeça. Conferi no olho em `conferencia/clipes-s7.jpg`: é a mesma pessoa, sem ninguém entrando.
4. `montar.py pecas/variacao.mp4`: igual ao da var1, exceto que agora lê as dimensões do clipe com ffprobe, porque algumas bases saíram 1402×1122 ou 1280×1024.
5. `varredura.py`: varredura final frame a frame, com as folhas em `conferencia/`.

## Varredura final
```
frames 1026 1026 fps 30/1 audio MD5=317d323d80b5b2ce454825e1aaf93a5a MD5=317d323d80b5b2ce454825e1aaf93a5a
dupla (408 fr): dif janela mediana 82.9 min 12.6 (n 266); corr bordas max 0.13 (n 983) mediana 0.09
fora da janela dif max 3.2; painéis dif max 3.1; YuNet rostos/frame max 1 (frames com >1: []); dupla sem rosto: 1 fr
```
- O "corr bordas" mede a correlação das bordas da janela entre original e peça nos 408 frames da dupla. Valor ≈ 0 quer dizer que não sobra contorno da dupla original.
- O único frame da dupla sem rosto é o n 266, quase branco pelo clarão.
- Folhas conferidas no olho: `orig-vs-peca-10.jpg`, `emendas-1.jpg`, `emendas-2.jpg`, `leak-transicao.jpg`, `casting.jpg` e `clipes-s7.jpg`.

## Custo real: US$ 0,533
Foram 2 imagens (0,067 cada) e 4 clipes Pruna (0,10 + 0,10 + 0,075 + 0,125), cruzados por prediction id em `conferencia/custo.txt`. Não houve regeração.

## Concessões
São as mesmas da var1: o clarão foi reconstruído, não copiado, e a resolução da janela é a do original (360×303).
