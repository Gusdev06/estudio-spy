---
tipo: conceito
tags: [risco-de-conta, compliance, pii, producao]
fontes: [fonte-edicoes-gram-2026-08-31]
---

# PII de terceiro em criativo

Gravação de funil feita com **conta real** carrega a identidade de quem foi usado como alvo. Nos 12 criativos GRAM, dois perfis do Instagram aparecem **legíveis e sem borrão**:

- `@kamamortonn` — "Kama Morton", 11 publicações, 1.344 seguidores
- `@bennet_chloe_` — "Chloe Bennett", 4 publicações, 868 seguidores

Com foto de perfil, contagens reais, posts reais com legenda, e a lista de DMs com usernames legíveis (aurora_wayfarer, byvalelipz, sammie.bentley, cassiebayes_, stan.flagel…). Só as **prévias de mensagem** estão borradas — a identidade não.

São pessoas físicas exibidas como alvo de espionagem e traição num anúncio pago. É o tipo de coisa que derruba conta: precedente na própria operação é a página **Quinn** no swipe `gram-detect`, que a Meta removeu com os criativos junto.

## Regra de produção

1. **Grave o funil com conta de teste controlada** — perfil próprio, criado pra isso, com fotos que você tem direito de usar.
2. Se a gravação já existe com conta real: **borre identidade, não só conteúdo** — @, nome, foto de perfil, contagens, e a lista de DMs.
3. Telas de "bem-vindo, `<nome>`" ou captura de e-mail: **corte fora**, não dá pra borrar sem matar a tela.
4. Varra a gravação inteira antes de qualquer trecho entrar num corte — ver [[insert-de-funil-real-como-cutaway]].

Vale pra PII do **operador** também: o `ScreenRecording` do funil zapdetect carregava o número e o e-mail do próprio Gusta.

Relacionado: [[nao-imitar-veiculo-real]], [[template-funil-gravado-9-modulos]].
