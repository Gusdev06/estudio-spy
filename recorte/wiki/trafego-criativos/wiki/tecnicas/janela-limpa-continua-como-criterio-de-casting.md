---
tipo: tecnica
tags: [casting, medicao, metodo, edicao, spy-zap]
fontes: [[fonte-selecao-atores-lote4-2026-09-01]]
---

# Janela limpa contínua — a única medida de casting que não mentiu

Escolher rosto por "% de frames com rosto" dá número bonito e errado; o que decide é **o maior trecho CONTÍNUO limpo dentro do recorte que você vai usar de verdade** — e ele só se confirma olhando um contact sheet denso, não um detector.

## A medida

> Maior janela contínua em que, **dentro do recorte proposto**, não há legenda, badge, card de UI nem PII, e o rosto está de frente.

Duas exigências que mudam o resultado:

- **dentro do recorte**, não no frame cheio. Overlay que vive abaixo da linha de corte não conta.
- **contínua**. Somar trechos soltos não serve: a locução do molde é uma tomada só.

No lote 4 (molde de 21,3–23,3s) o ranking ficou:

| Candidato | Janela limpa | Trecho |
|---|---|---|
| AD05-P1 | **19,50s** | 5,60 → 25,10s |
| AD05-P3 | 18,40s | 5,60 → 24,00s |
| AD04-P3 | 17,50s | 0,00 → 17,50s |
| AD04-P1 | 16,10s | 0,00 → 16,10s |

**Nenhum dos 10 chegou aos ~22s.** Esse é o tipo de resultado que só aparece com a medida certa — e é melhor descobrir antes da montagem.

## Três detectores que mentiram (na ordem em que mentiram)

**1. Variância temporal por linha.** Inútil em anúncio dinâmico: não existe banda estática pra isolar. Todo o quadro tem variância alta.

**2. Detecção de pele = "rosto na tela".** Errou nos dois sentidos:
- **falso negativo no color wash** — o frame tingido de laranja/amarelo (0,1s, recurso de edição comum nessas peças) derruba a faixa RGB de pele. O ator *está* lá. Esses frames **contam como aproveitáveis**; só valem nota pro Bisturi corrigir cor.
- **falso negativo E positivo no card *inset*** — o card `dodoelady` cobre o ator mas deixa pele nas bordas: o detector diz "rosto ok" e o rosto sumiu. Foi o que quase promoveu um candidato com **PII de terceiro dentro do recorte**.

**3. Detector de card escuro.** Over-trigger: acusou "95% bloqueado" num arquivo cujo recorte eu tinha acabado de ver limpo.

## O que resolveu

**Contact sheet a 1 fps já no recorte proposto** (`crop=…, fps=1, tile=6x4`). Um quadro por segundo, na moldura real, olhado. Detector serve pra achar a fronteira exata *depois* que a imagem confirmou o regime — nunca pra concluir sozinho.

> Regra da casa que isso reforça: quem mede mostra como mediu. Detector sem frame conferido é opinião com casas decimais.

## Conecta com

- [[peca-pronta-nao-e-banco-de-atores]] — a outra metade do mesmo casting: a faixa tem altura?
- [[medir-fronteira-de-bloco-em-video]] — qual método mente em qual caso; mesma família de erro.
- [[variar-uma-alavanca-por-vez]] — a janela limpa é o que garante que só o rosto mudou.
- [[nome-de-pagina-nao-e-nome-do-ator]] — outro chute por metadado desmentido pela imagem.
