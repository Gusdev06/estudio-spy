# Amanda Silva 1680455873461877: variação 4 (25/09/2026)

Esteira spy (Zap), papel Bisturi. Mesmo pedido, molde e montagem da var1: pessoa e cenário novos, com áudio, card "You Deserve The Truth", clarão laranja, tela do app, ritmo e cortes do original. Molde, pipeline e concessões herdadas estão em **`../var1-amanda-silva-1680455873461877-2026-09-25/README.md`**. Esta pasta é autossuficiente: tem a referência, `molde/medidas.json`, os scripts com caminhos próprios, a base, o áudio, os clipes e a conferência.

- **Avatar:** mulher leste-asiática de ~26 anos, pele clara, chanel preto liso com franja reta, argolinha prata, moletom cinza mescla com capuz (`base/pessoa.txt`). É do mesmo gênero e da mesma faixa de idade da voz.
- **Cenário:** quarto com parede verde-sálvia, quadro botânico de folha, poltrona de rattan, planta alta, luz do dia (`base/cena.txt`). Não tem TV, tela, texto nem logo.
- **Base:** `base/base.png`, gerada por gpt-image-2/edit (medium, 1k) sobre o frame limpo n360.
- **Clipes:** Pruna 720p, seed 7, de primeira. O `checar.py` passou nos 3 clipes e nenhum precisou ser refeito. Os downloads foram decodificados inteiros, sem erro (601/409/481 frames).

## O que mudou em relação à var1: a emenda c2|c3
Na var1 a emenda era seca em 43,0 s (numa pausa de 0,4 s) e dava um salto de pose. Aqui:
- **Áudio:** c1 = 0–24,467 s; c2 = 24,467–41,45 s; c3 = 40,9 s–fim. c2 e c3 se sobrepõem 0,55 s dentro da pausa maior, de 40,75 a 41,65 s. As durações ficam abaixo do segundo inteiro (25 + 17 + 20 s), então o custo é o mesmo da var1.
- **Escolha da emenda:** o `montar.py` escolhe, entre n1230 e n1240, o frame em que as poses de c2 e c3 mais se parecem (5 landmarks do YuNet, medidos no quadro já recortado). Nesta peça a emenda ficou em **n1230**.
- **Enquadramento:** o c3 entra casado com o c2 (deslocamento de 49/2 px e escala 1.003) e volta ao próprio enquadramento em 24 frames. Quando o recorte passa da borda, a imagem é espelhada em até 64 px na lateral.
- **Transição:** crossfade de 3 frames.
- **Resultado** (`salto-emenda.py` → `conferencia/salto-emenda.txt`): o maior salto de landmarks na emenda é de **5,2 px/frame**, contra 2,2 px/frame de movimento típico. Na var1, pela mesma medida, o salto é de 33,7 px/frame. A folha está em `conferencia/emenda-c2c3.jpg`.

## Entrega
`pecas/variacao.mp4`: 960×720, 1817 frames, 60,74 s. Decodifica inteira. O md5 do stream de áudio é `03fab35903247102d62ed86cc7f309e3`, idêntico ao original.

## Conferência
- **Varredura** dos 1817 frames (`varredura.py`; saída em `conferencia/varredura.txt` e `.json`): há 1 rosto fora da tela do app em todos os frames. Fora das áreas herdadas, a fração de pixels iguais ao original é de 0.0231 em média e 0.0319 no máximo. É coincidência de cor sem forma (`conferencia/iguais-ao-original.jpg`): a pessoa original não aparece em nenhum frame.
- **Folhas:** `conferencia/momentos.jpg` (original | peça), `clipes-todos.jpg` e `emenda-c2c3.jpg`.

## Concessões
- As concessões da var1 continuam: a luz do leak é aproximada e os gestos de mão são os da própria avatar.
- No crossfade (3 frames) aparece um leve fantasma de roupa e cenário, porque só o rosto é alinhado.
- Durante a volta do enquadramento, a borda esquerda pode mostrar alguns px espelhados por até 0,8 s.

## Custo real: US$ 1,6165 (conferido em `wavespeed billings`)
| prediction | o quê | US$ |
|---|---|---|
| ecb5b7ec… | gpt-image-2/edit (base) | 0,0665 |
| 2a29dc4e… | Pruna c1 (25 s) | 0,625 |
| c1528b9e… | Pruna c2 (17 s) | 0,425 |
| 6bad2417… | Pruna c3 (20 s) | 0,50 |
