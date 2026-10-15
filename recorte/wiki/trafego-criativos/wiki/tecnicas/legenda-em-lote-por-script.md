---
tipo: tecnica
tags: [criativo, overlay, esteira, automacao, lote]
fontes: [operacao-2026-08-20]
---

Quando a legenda é **idêntica** em todas as variações, aplicá-la por script (Pillow) é
ordens de magnitude mais rápido e mais fiel que Canva Bulk Create ou modelo de imagem.

## Quando usar esta técnica vs. as outras

| Situação | Técnica |
|---|---|
| Mesma legenda, N imagens-base diferentes | **esta** — script determinístico |
| Mesmo criativo, legenda em outro idioma | [[localizacao-de-value-stack]] (Seedream edit) |
| Variar a oferta/promessa do overlay | [[value-stack-no-overlay]] |
| Variar a imagem mantendo overlay | [[variar-uma-alavanca-por-vez]] |

## Por que não Canva

- O **MCP do Canva** só autentica — não edita design programaticamente.
- **Bulk Create** foi feito pra variar *texto* a partir de CSV, não pra trocar dezenas
  de fundos: exige subir e mapear cada imagem à mão. Mais trabalho manual que o script.
- Modelo de imagem (Seedream/GPT Image) **redesenha** o texto — deriva de fonte, kerning
  e posição a cada geração. Para legenda idêntica isso é bug, não feature.

## O método

1. **Deduplicar por md5** antes de qualquer coisa. Download em lote gera cópias `(1)`
   — em 2026-08-20 foram 37 duplicatas em 130 arquivos (28%).
2. **Calibrar o layout em frações**, não em pixels: medir no criativo campeão a que
   % da altura e da largura cada linha fica, e guardar isso como constante. Assim a
   mesma calibração serve pra qualquer resolução de saída.
3. **Cortar em 4:5 central com `cover`** (escala pelo maior fator, corta o excesso).
   Nunca esticar — distorção em rosto mata a believability.
4. **Sombra gaussiana leve** atrás do texto branco. Sem ela o overlay some em fundo
   claro (praia, banheiro branco), e a base é heterogênea demais pra confiar na sorte.
5. **Piso de resolução** (`--min-width 700`). Imagem-base abaixo disso sai mole no feed
   e não adianta upscalar com LANCZOS — ou upscala com modelo 2K, ou descarta.

## Gotcha

Fonte do Canva precisa ser a **mesma família**, senão o criativo novo não parece irmão
do campeão e você perde o histórico visual que o público já reconhece. O campeão de
300-prompts usa **Montserrat Bold** (variável, em `paid/criativos/_lib/`).

Ver também: [[censura-plataforma-asterisco]] (o `Onl* F` do overlay), [[oferta-300-prompts]].
