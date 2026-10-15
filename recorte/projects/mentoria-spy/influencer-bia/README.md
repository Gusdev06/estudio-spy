# Bia — ficha da influencer (@babado.da.bia)

Criada em 14/10/2026. É a fonte de identidade da Bia: toda geração (imagem ou vídeo) recebe imagens daqui como referência.

## Ficha
`ficha-bia.png`: grade com as 8 bases. Os arquivos ficam em `base/`, cada um com a URL da WaveSpeed ao lado (`.url`).

| # | Arquivo | Uso |
|---|---|---|
| 01 | `01-frente` | **Âncora.** Vai em TODA geração |
| 02 | `02-tres-quartos-esq` | ângulo 3/4 |
| 03 | `03-tres-quartos-dir` | ângulo 3/4 (saiu quase igual à 02, para o mesmo lado; regerar o lado oposto se precisar) |
| 04 | `04-perfil` | perfil |
| 05 | `05-close-rosto` | pele, sardas, pinta: o detalhe que o vídeo perde |
| 06 | `06-corpo-inteiro` | proporção do corpo |
| 07 | `07-expressao-sorriso` | sorrisinho de canto |
| 08 | `08-expressao-cetica` | olhar de lado, cética |

Texto fixo de identidade: `identidade.txt`. Colar igual em todo prompt, sem reescrever. Só cena, roupa e ação mudam.
A pinta fica na bochecha **direita** dela, que aparece no lado esquerdo da imagem.

## Como usar em cada reel (troca pura no molde da gigi)
1. **Bia na cena:** usar o frame do reel e rodar **`google/nano-banana-2.1/edit` 2k** (regra de 15/10: toda imagem da Bia sai do Nano Banana 2.1) com `images=[frame, 01-frente, 05-close-rosto]`, trocando rosto, cabelo, **roupa e acessórios** (decisão de 14/10).
2. **Vídeo:** `seedance-2.0/video-edit` com `reference_images=[bia-na-cena, 01-frente, 05-close-rosto]` (aceita até 9).
3. Conferir frame a frame: rosto, pinta e se a roupa nova segura o vídeo inteiro.

## Regras (pesquisa de 14/10 + o que medimos)
- **Sempre voltar à âncora**, nunca encadear (usar a saída anterior como referência acumula desvio).
- A referência precisa estar **na cena do próprio reel**. Uma Bia de outra cena foi ignorada pelo Seedance e a gigi ficou no vídeo (US$ 2,43 perdidos em 14/10).
- Bases com as mãos vazias e fundo neutro: objeto na mão faz o rosto variar entre ângulos.
- Variar uma coisa por geração (roupa, cena ou ação) e conferir antes de escalar.
- Aspect ratio e qualidade iguais em toda geração.

## Modelo de imagem
Desde 15/10, **toda imagem da Bia sai do Nano Banana 2.1** (`google/nano-banana-2.1/edit`, 2k). O gpt-image-2.5 da ficha original e das primeiras cenas fica só como histórico.

## Custo
8 imagens em `quality=high`, ~US$ 0,20–0,24 cada, ~US$ 1,8 no total (estimado; não conferi na fatura).
Base de origem: `../criativos/Deaen6FBTXu-avatar-novo-2026-10-13/avatar-base.png`.
