---
tipo: inbox
data: 2026-08-26
origem: projects/clinica-que-lucra/paginas/auditoria-lp-2026-08-26.md
---

# Auditoria de LP — Clínica que Lucra (pra ingestar)

Insights que valem além dessa página:

- **Checar se a fonte carrega antes de julgar design.** A LP inteira rodava em Times +
  Helvetica: `family=Jost:wght@0,300;...` devolve HTTP 400 no Google Fonts (o formato
  `0,300` só vale com eixo `ital,wght`) e derruba junto TODA família da mesma requisição.
  Bug estava em 23 arquivos do produto. Teste: `curl` na URL da fonte e conferir 200.
- **Toda regra de fonte precisa de fallback.** `font-family:'Jost'` sem fallback cai no
  serif padrão do navegador — botão de compra em Times New Roman.
- **LP de low ticket vestida de marca premium cria fricção de preço.** Elegância silenciosa
  (didone + neutros + muito respiro) = consideração longa; low ticket precisa de decisão
  rápida, contraste e uma cor de ação saturada exclusiva do botão.
- **Página sem cor de destaque não tem hierarquia.** Se o acento é um cinza-quente, preço,
  botão e rótulo pesam igual — e nada puxa o olho.
- **Depoimento placeholder no ar = risco de conta.** Nomes/cidades de exemplo com 5 estrelas
  em página pública é propaganda enganosa, não rascunho.
- **Estatística sem fonte numa LP é passivo**, não prova.
