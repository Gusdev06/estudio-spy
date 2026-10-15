# Lauren Walker 2091863388082075: var2, homem e cenários novos · 2026-09-25

Molde, pipeline e concessões estruturais são os da **var1** (`../var1-lauren-walker-2091863388082075-2026-09-25/README.md`). Esta pasta é uma cópia autossuficiente.

**Peça:** `pecas/variacao.mp4`: 720×1280, 30 fps, 601 frames, áudio AAC copiado (md5 do stream `090dce621c46e223e4ab6e19a04c276d` = original).
**Avatar:** homem negro americano de ~40 anos, fade curto, barba preta aparada, camisa social azul-marinho.
**Cenários:** blocos A/B (n 0–447): escritório em casa (mesa, estante com fichários, parede azul). Close C (n 448–524): cozinha clara com geladeira inox. CTA (n 525–600): original intocado.

## Como foi feito
1. `base/A.req.json`: gpt-image-2/edit (medium, 1k) sobre a **A2 da var1** (só enquadramento: cabeça na metade de baixo) trocando homem e lugar. Isso economizou o passo de outpaint.
2. `base/C.req.json`: a identidade vem da A nova e o enquadramento do close vem da C da var1. `conferencia/bases-A-C.jpg`.
3. `SEED=7 bash gerar-clipes.sh c1 c2`: Pruna 720p, prompt só em positivo, com o áudio da var1 (mesmos cortes). Avatar e cenários ficam em `base/elenco.json`. Os dois decodificaram inteiros (361 e 73 frames).
4. `python3 checar.py c1 c2` → `conferencia/triagem-c*.jpg`.
5. `<segenv>/bin/python montar.py pecas/variacao.mp4`: igual à var1, mais duas coisas: (a) `limpeza.json` opcional (placa limpa contra letreiro alucinado no fundo); (b) a máscara do homem antigo ganhou um "boné" (elipse do crânio ∩ pixels escuros), porque o MediaPipe deixava buracos no cabelo escuro dele e um fio aparecia na careca da var4.
6. `varredura.py`, depois `python3 folhas.py` → `conferencia/original-x-peca-10-instantes.jpg`, `emendas.jpg`, `varredura-px-iguais-piores.jpg`. Os frames (`frames/full`, `frames/peca`) foram apagados. Pra regerar: `ffmpeg -i REFERENCIA-original.mp4 -start_number 0 frames/full/%03d.png` (idem pra peça).

## Varredura final
- frames com o homem no original: 525 | px iguais na peça: médio 7675.1 máx 24507 no n 405
- frames da peça com != 1 rosto (n<=524): []
- n 0-98: px iguais médio 2575 máx 3005 (máscara média 148730)
- n 99-343: px iguais médio 9148 máx 14262 (máscara média 199620)
- n 344-447: px iguais médio 7526 máx 24507 (máscara média 161735)
- n 448-524: px iguais médio 9747 máx 12271 (máscara média 453997)
- A olho: 10 instantes, as 4 emendas e o topo da cabeça em 8 frames do B. Não sobra rosto, cabelo nem ombro do homem original. Os px "iguais" são coincidência de cor (pele sobre pele, fundo escuro).

## Concessões (além das da var1)
- As mesmas da var1: halo reconstruído por inpainting (levemente borrado no contorno), sem os risquinhos de brilho da seta, sem a mão do n 450–453.
- Letreiro alucinado pelo Pruna no fundo do c1 ("A⅃", clipe k 74–134 = n 92–166). Troquei a caixa pela placa limpa, a mediana dos 12 primeiros frames do mesmo clipe (`limpeza.json`). Só aparece em tela cheia no n 92–98 e, depois disso, o recorte do B descarta o fundo.

## Custo real: US$ 0,594
2 imagens gpt-image-2/edit (0,0665 + 0,0779) e 2 clipes Pruna (15 s = 0,375 e 3 s = 0,075). Ids e preço de cada um estão em `ids.txt`, e a conferência em `custo-billings.json`.
