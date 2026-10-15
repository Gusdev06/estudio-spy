# YuNet: escolher o rosto pelo score, não pela área (24/09)

No recorte centrado no rosto (`montar.py` do podcast WPP), `max(d, key=área)` pegou um falso rosto nas plantas do fundo do estúdio: score ~0,65, caixa maior que o rosto real (0,95). A convidada saiu colada na borda direita da janela em 2 de 5 elencos (x3, x5 da var6). Trocar pra `max(d, key=score)` resolveu sem mudar os recortes já validados. Regra: com fundo texturizado, escolha o rosto por confiança e varra o clipe inteiro com limiar de 0,8 pra contar pessoas. Isso também pegou o homem que a Pruna inventou na x2, fora da janela.
Fonte: `projects/mentoria-spy/centerpag-detect/criativos/podcast-wpp-57s-copy-nova-2026-09-23/README.md` (var6).
