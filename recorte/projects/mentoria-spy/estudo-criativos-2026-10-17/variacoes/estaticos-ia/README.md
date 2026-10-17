# Estáticos IA — variações dos campeões tryfidelo (17/10/2026)

Modelo `openai/gpt-image-2/edit` (WaveSpeed), image-to-image a partir do campeão, 1k. Uma alavanca por peça.
Custo real (billings, key macbook, por id de predição): **US$ 0,551** de teto US$ 1,50 → `custo-real.txt`.

| Peça | Base | Alavanca | Qualidade | Tentativas |
|---|---|---|---|---|
| `pecas/1a-she-deleted.png` | A (megan-rodriguez-1559475625325895) | gênero invertido: SHE / "Her", mulher no celular | medium | 1 |
| `pecas/1b-he-deleted-dms.png` | A | manchete "HE DELETED THE DMs." | medium | 2 (v1 trocou o selo "Message deleted" pra 2:14 AM) |
| `pecas/1c-clone-novo-rosto.png` | A | outro homem (negro, ~40, barba, moletom, carro à noite) | medium | 1 |
| `pecas/3a-found-hiding-novo-rosto.png` | B (silvia-amorin-2007437113276299) | outra mulher (branca, ~35, ruiva, suéter creme) | high | 2 (v1 desenhou logo do Instagram no 1º ícone e errou 4 linhas do inbox) |

Texto conferido letra por letra nas 4 peças finais (manchetes, timeline, lista, botão, chat, inbox do celular).
Conferência visual referência × peça: `conferencia.jpg`. Prompts: `prompts.md`. Saídas brutas e v1 descartadas: `raw/`.

Observações:
- 1a: o avatar e a foto no chat viraram homem (coerente com a inversão); cabeçalho "Her".
- 1b: o rosto do homem muda levemente em relação ao original (o edit regenera a imagem inteira).
- 3a: ícone "Instagram" e wordmark no celular são os mesmos da referência, nada novo. Saiu em 912×1152 (4:5).
- Peças A saem em 2:3 (1024×1536 / 1040×1552); original era 400×600.
