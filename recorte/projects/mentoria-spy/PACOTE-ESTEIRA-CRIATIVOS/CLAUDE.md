# Instruções para o agente (Claude Code) — esteira de criativos spy

Você opera esta pasta para **clonar criativos de vídeo que já escalam e produzir variações** (avatar novo, copy nova, elenco novo). O dono desta máquina é quem paga a geração: **nada pago roda sem ele ver o custo estimado antes**.

## Leia antes de produzir (nesta ordem)
1. `README.md` — visão geral, instalação, modelos e preços.
2. `metodo/01-regras.md` — **as 8 regras**. Elas não são sugestão: cada uma veio de peça reprovada ou dinheiro perdido.
3. `metodo/02-prompts.md` — prompts de imagem, lipsync e voz (copie a forma, troque só a descrição).
4. `metodo/03-copy.md` — estruturas de copy com dado de gasto atrás.
5. `metodo/04-conferencia.md` + `CHECKLIST.md` — o que conferir antes de entregar.
6. `moldes/<n>/README.md` — o molde específico, quando o criativo for um dos 5 já medidos.

## Como trabalhar
- **Meça antes de montar.** Resolução, duração, faixas, janelas, cortes, onde há rosto e onde há painel. Ferramentas: `ffprobe`, `scripts/analisar-estrutura.py`, PIL/numpy. Nunca estime "no olho".
- **Reconstrua, não recorte.** Legenda, faixa, card e CTA queimados se redesenham. Recorte só o que é sólido sobre fundo liso (ex.: painel que ocupa a janela inteira).
- **Estime o custo** (`wavespeed price …`) e mostre em dólares antes de gerar. Depois do lote, confirme o gasto real com `wavespeed billings --since <ISO> --json`.
- **Confira o clipe inteiro** (folha de 16–24 frames + `scripts/checar-identidade.py`) antes de montar; valide todo download com `ffmpeg -v error -i x -f null -`.
- **Uma peça por vez** na montagem com karaokê (estoura memória em lote).
- Entregue sempre: a peça + a pasta `conferencia/` + o custo real.

## Nunca
- Gerar mídia paga sem autorização explícita do dono.
- Pedir, imprimir ou gravar a chave da WaveSpeed em texto (use `wavespeed login`).
- Escrever "hack", "senha", "invadir" ou "espionar" **na fala** de um criativo (a promessa pesada vive na imagem do painel).
- Deixar telefone, e-mail ou nome real de terceiro visível numa gravação de funil.
- Usar voz de um gênero com avatar de outro.

## Estrutura da pasta
```
metodo/      regras, prompts, copy, conferência, custos, troubleshooting, wiki
moldes/1..5  os 5 moldes prontos (scripts + README de cada um)
scripts/     utilitários genéricos + modelo de detecção de rosto (YuNet)
midia/       criativos de referência dos moldes + trilha
fontes/      as fontes usadas nas legendas e faixas
exemplos/    duas peças finais como exemplo do resultado
```

## Fluxo padrão de um pedido ("faz 5 variações desse")
1. Medir o original e dizer a estrutura encontrada.
2. Propor elenco (descrições) e/ou copy, e estimar o custo total.
3. Gerar imagens → lipsync → conferir cada clipe.
4. Reconstruir camadas (karaokê/faixa) e montar uma peça por vez.
5. Entregar peças + conferência + custo real, e anotar o que deu errado num `README.md` do lote.
