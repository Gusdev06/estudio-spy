---
tipo: fonte
tags: [teardown, spy-zap, centerpag, molde, medicao]
data: 2026-09-01
---

# fonte — teardown das três de 35 dias (01/09/2026)

Lote 3. Pergunta que decidia o lote: três Páginas rodando o mesmo ângulo há 35 dias **compartilham o formato de edição, ou só a copy?**

## Entradas

- `centerpag-detect/escalados/whatsapp/` — peças `06`, `10`, `20` (35,1 dias) e `14` (2,1 dias, controle).
- `manifest.json` + os `.txt` de cada peça.
- Cru em `raw/2026-09-01-teardown-lote3-tres-de-35-dias.md`.

## Resposta

**Molde compartilhado, gravação não** — nenhuma das duas opções puras. Ver [[familia-criativos-zap-35-dias]] para os números.

## Achados de método

- **Três peças concordando ao pixel valem mais que qualquer teste de margem.** A borda inferior da tarja reprovou no corte de 2× em todas (0,90–1,18×, porque há verde no conteúdo abaixo), mas as três deram `y=125` independentemente. Concordância entre arquivos distintos é evidência mais forte que margem dentro de um arquivo — ver [[medir-fronteira-de-bloco-em-video]].
- **Calibrar o limiar em vez de escolher:** "mesma imagem" foi definido pela distância entre frames vizinhos da mesma peça (0,28), não por um número arbitrário.
- **Custo de lipsync escala com segundos de rosto, não com duração** — corrigiu a premissa do briefing.

⚠️ Nenhuma métrica de performance verificada. Sobrevivência (35 dias) é proxy melhor que rank, mas continua não sendo ROAS.

## Páginas geradas / atualizadas

- [[familia-criativos-zap-35-dias]]
- [[medir-fronteira-de-bloco-em-video]] — concordância entre peças como evidência
- [[estimar-custo-de-geracao-antes-de-disparar]] — custo por segundo de rosto
