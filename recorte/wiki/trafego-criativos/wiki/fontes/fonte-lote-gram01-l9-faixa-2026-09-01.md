---
tipo: fonte
tags: [lote, montagem, spy-gram, L9, medicao, lipsync]
data: 2026-09-01
---

# fonte — lote GRAM 01 L9, eixo faixa de hook (01/09/2026)

Montagem das 6 peças L9 pelo Bisturi, a partir do teardown do vencedor e do roteiro do Isca. Interessa ao wiki por dois motivos: é a primeira aplicação completa do L9, e a montagem **achou o limite do método de medição** que o próprio wiki tinha acabado de registrar.

## Entradas

- `projects/mentoria-spy/gram-detect/criativos/gram01-l9-faixa-2026-09-01/README.md` — cru em `raw/2026-09-01-lote-gram01-l9-faixa-montagem.md`.
- Peças `pecas/gram01-l9-en-0N-v2.mp4` (com lipsync) e `pecas/v1-sem-lipsync/` (controle).

## Achados

- **6 peças, uma alavanca só** — rosto, b-roll, VO e funil idênticos; só a faixa muda. É [[roteiro-mestre-com-n-vozes]] rodando de verdade, e [[variar-uma-alavanca-por-vez]] com controle preservado (a v1 não foi sobrescrita).
- **O head não custou geração:** saiu de uma peça L9 nossa que já existia, reconformada. O único ativo novo é o b-roll, porque o painel direito da nossa L9 antiga tinha PII e tela legível.
- **PII resolvida com faixa de altura cheia, não retângulo fixo** — conteúdo que rola escorrega por baixo de rect medido num frame só. Reforça [[pii-de-terceiro-em-criativo]].
- **Limite do método de medição** — ver [[medir-fronteira-de-bloco-em-video]]. A variância temporal, que é o método certo pra medir referência de terceiro, devolveu `y≈1121` em vez de `1212` na peça montada; a cor chapada da faixa deu a resposta exata.

## Contradição resolvida na verificação

O README atribui a falha ao **lipsync** ("só a boca se mexe, então a base do bloco de cima congela"). **Medido, não procede:** comparando v1 (sem lipsync) e v2 (com), a variância do head é igual ou levemente maior na v2 (+0,82 na boca/queixo, +0,95 no pescoço/ombro), e a falha reproduz na v1 também (`y=1081` com o mesmo limiar). A causa real é limiar absoluto frouxo pegando a base naturalmente quieta do head. A **conclusão prática do Bisturi continua certa** (usar cor na peça nossa); o mecanismo é que estava trocado, e está corrigido na página.

⚠️ Nenhuma métrica de performance — as 6 peças não subiram. [[arte-nova-nao-herda-validacao]] vale: modelar o vencedor não transfere a performance dele.

## Páginas geradas / atualizadas

- [[medir-fronteira-de-bloco-em-video]] — reescrita com as duas metades da regra
