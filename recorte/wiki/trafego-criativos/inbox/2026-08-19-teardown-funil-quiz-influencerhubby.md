---
tipo: inbox
data: 2026-08-19
origem: clone técnico de funil concorrente (skill web-clone)
status: pendente-ingestao
---

# Teardown do funil de quiz "Modelo de I.A Hubby" (@hubby_academy)

Concorrente direto no nicho PT-BR de "ganhar dinheiro com I.A". Funil de quiz de 32 páginas
rodando em XQuiz (`influencerhubby.xquiz.click`), oferta BlackBox A.I, checkout Lastlink,
12× de R$7,81 ancorado em R$997.

**Clone técnico completo + fonte crua:** `~/Documents/AIS-OS/projects/website-clones/influencerhubby-clone/`
- `TEARDOWN.md` — dissecação técnica + mapa das 32 páginas
- `RECON/funnel.json` — o funil inteiro em JSON (copy, ramificações, temas, assets)
- `REPLACE_GUIDE.md` — o que trocar para virar funil próprio

## Padrões de conversão que valem virar páginas atômicas

1. **Barra de progresso reiniciada por tela** — cada página declara `startValue`/`endValue`
   próprios (10→65, 10→75...). Não mede progresso real; é gatilho de compromisso repetido.
2. **Captura de nome no meio do funil** (página 23 de 32), depois de 2 telas de prova —
   não na porta de entrada. Depois reinjeta `{{nome}}` em toda a copy seguinte.
3. **Diagnóstico com score fixo** — "89% de chance de você estar usando prompts fracos"
   está hardcoded no JSON, não depende das respostas do quiz.
4. **Loading teatral de 5s** ("Examinando suas respostas...") antes da oferta.
5. **Prova antes de pergunta** — abre com imagem de resultado, não com formulário.
6. **Escalada de desejo em blocos separados** — faceswap, consistência de rosto, nicho hot,
   cada um em sua própria tela em vez de uma página longa.
7. **Ancoragem + countdown 10min + garantia 7 dias** na mesma tela de oferta.

## Ângulos de copy dele (mesma audiência da nossa low ticket)
- "o segredo do realismo não está na ferramenta, está na ESTRUTURA DO PROMPT"
- prova com imagem "de celular", não de câmera profissional — realismo por imperfeição
- case da influencer de I.A "Bia": 90 mil em comissões no TikTok Shop, 3 vídeos virais

Relacionado: [[localizacao-de-value-stack]]
