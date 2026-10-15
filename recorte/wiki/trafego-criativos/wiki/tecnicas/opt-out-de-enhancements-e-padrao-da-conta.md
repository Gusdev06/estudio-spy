---
tipo: tecnica
tags: [meta-ads, api, criativo, enhancements, advantage-plus, armadilha]
fontes: [[fonte-comparativo-mensal-jul-ago-2026-08-22]]
---

# Opt-out de enhancements já é o padrão da conta

Na conta CA-DZD **não é preciso mandar `creative_features_spec`** ao criar criativo pela API:
a Meta já devolve **todos os ~80 enhancements com `enroll_status: OPT_OUT`** por padrão.
Verificado em 22/08 criando um criativo sem o campo e lendo de volta com `get_creative_details`
— resultado idêntico ao do campeão FR validado.

## Por que isso importa

Mandar o spec inteiro em cada criativo infla o payload em ~1,1 KB por item. Numa esteira de 70
criativos são ~77 KB de payload à toa, o que estoura limites de resposta e obriga a quebrar em
muitos lotes. Sem o campo, o payload cai ~75%.

## A armadilha do `standard_enhancements`

A chave-guarda-chuva `standard_enhancements` **aparece no GET mas é rejeitada no POST**:

> `O recurso de inclusão do campo de aprimoramentos padrão no criativo foi descontinuado.
> Defina recursos individuais.` (error_subcode 3858504)

Se precisar mesmo forçar opt-out, só estas **18 chaves são graváveis** para criativo de link:
`image_touchups`, `text_optimizations`, `inline_comment`, `image_templates`, `music_generation`,
`image_background_gen`, `description_automation`, `creative_stickers`, `video_auto_crop`,
`product_extensions`, `site_extensions`, `profile_card`, `image_uncrop`, `add_text_overlay`,
`pac_relaxation`, `reveal_details_over_time`, `show_destination_blurbs`, `show_summary`.

## Regra prática

1. Criar sem `creative_features_spec`.
2. Conferir **um** criativo com `get_creative_details` antes de subir o lote inteiro.
3. Só mandar as 18 chaves se a conferência mostrar algo em OPT_IN.

Relacionado: [[legenda-em-lote-por-script]], [[throughput-de-criativo]].
