---
name: gerar-criativo-imagem
description: "Produz a imagem de um criativo — o método PREFERIDO é variar o criativo CAMPEÃO (achar o campeão, baixar a imagem real, entender por que funcionou, gerar variações image-to-image a partir dele). Também gera do zero por prompt quando não há campeão. Use quando precisar PRODUZIR a imagem de um anúncio, variar um criativo vencedor, ou montar a arte final. Roda via GERAEW/Higgsfield."
---

# Gerar Criativo de Imagem

Produz a **imagem do criativo** e monta a arte final. É o passo de produção (o "como"),
acionado pelo agente `creative-producer`.

## ⭐ Fluxo PREFERIDO: variar o campeão (imagem→imagem)
Sempre que existir um criativo campeão, varie ELE em vez de gerar do zero — a variação
herda o que já ganha. Passos:

1. **Achar o campeão** (com o `analista-trafego`): ad de maior ROAS/gasto no Meta.
2. **Baixar a imagem real** do campeão: `get_ad_creatives(ad_id)` → pegar `image_url` →
   `curl` com User-Agent de navegador + `Referer: https://www.facebook.com/` (senão o
   FB CDN devolve lixo). Salvar em `paid/criativos/campeoes-ref/`. (Futuro: vídeo via
   `get_ad_video`.)
3. **Entender por que funcionou** (teardown): abrir a imagem (Read), mapear hook visual,
   overlay/value stack, expressão, luz, ângulo, truques de compliance. Salvar teardown.
4. **Gerar variações a partir dele (image-to-image):** subir a imagem do campeão via
   `geraew_upload_image` → passar a URL retornada em `image_urls` do
   `geraew_generate_image`, **variando UMA alavanca por vez** (modelo/etnia, cenário,
   expressão, ou hook do overlay). Mantém a DNA vencedora.
   ⚠️ GOTCHA: **NÃO** passe a URL do CDN do Facebook direto em `image_urls` — o
   servidor do GERAEW não consegue baixar dela (dá timeout). Sempre **suba a imagem**
   (widget `geraew_upload_image` ou host público) e use a URL de lá.
5. **Salvar** em `paid/criativos/`.

## 🚨 REGRA: texto na imagem vai NO PROMPT (não em overlay separado)
Quando o criativo campeão tem **texto embutido na imagem** (value stack, hook, preço),
**NÃO** montar overlay depois (nada de ImageMagick/Canva — fica com retrabalho e nunca
idêntico). Em vez disso, **especifique no próprio prompt de geração** para reproduzir o
texto **EXATO** — mesmas palavras, fonte, cor, tamanho, posição — pra a imagem já sair
com o **criativo pronto**.
- Aproveite o image-to-image: a referência do campeão **já tem o texto**, então instrua
  a **manter o texto exatamente** e trocar só a alavanca (modelo/cena/expressão).
- Descreva o texto no prompt literalmente: cada linha, cor (ex: barra laranja #F5A623),
  peso (bold), e posição (ex: terço inferior, centralizado).
- Modelo: **GPT Image 2** (padrão, melhor tipografia); fallback Geraew Unlocked só se recusar.

## Fluxo alternativo: gerar do zero (sem campeão)
Quando não há referência, use a skill `gpt-image-2-prompt` p/ o prompt e gere por texto.

## Entrada
- Um prompt de imagem já otimizado (normalmente de `gpt-image-2-prompt`).
- O contexto de marca do cliente (`projects/<cliente>/context/brand-brief.md`).

## Passo 1 — Gerar a imagem (CADEIA DE FALLBACK)

🚨 **REGRA DE MODELO (usuário) — nesta ordem:**
1. **GERAEW `geraew_generate_image` com `model: "GPT Image 2"`** (padrão — melhor tipografia).
2. **Se o GPT Image 2 FALHAR** (erro / timeout / "not compliant" / aspect ratio) →
   **WaveSpeed CLI** (skill `wavespeed`) com **Seedream 5.0 Pro** (IDs confirmados):
   - text-to-image: `bytedance/seedream-v5.0-pro`
   - edit (image-to-image, variar de referência): `bytedance/seedream-v5.0-pro/edit`
     (requer `images=["<url>"]` — subir a ref antes: `wavespeed upload <arquivo> --json`)
   - Params úteis: `-i aspect_ratio="4:5"` (suporta!), `-i resolution="2k"`, `--json --download`.
   - ✅ Comprovado: aceita o conteúdo sexy do 300+ Prompts, tipografia excelente,
     ~$0,045/img (bem mais barato que GERAEW). Auth via `wavespeed login`.
3. Último recurso p/ conteúdo sexy que os dois recusarem: **GERAEW `Geraew Unlocked`**
   (uncensored — comprovadamente aceita o conteúdo do 300+ Prompts).

⚠️ Nota prática: pra clientes de conteúdo sexy (ex: 300+ Prompts), o GPT Image 2 tende
a recusar ("not compliant") → o fluxo cai no Seedream/Unlocked. Confirmar créditos/custo
antes de gastar.

Regras ao gerar:
- Antes de gastar créditos, **confirme com o usuário** (qual ferramenta / quantas
  imagens) — geração custa.
- Peça **vertical 9:16**, realismo (a skill de prompt já cuida disso).
- Gere 2–4 variações de cena por ângulo quando a meta for encher a esteira.

## Passo 2 — Montar o criativo final (overlay)
A imagem-base sai limpa (GPT Image 2/geradores renderizam texto mal). O texto do
criativo entra na montagem:
- **Overlay de hook** no topo (ex: "100% AI 🤖 — she's not real").
- **Selo de prova social** no canto (ex: ⭐⭐⭐⭐⭐ 4.7/5) — replica o que já converte.
- Respeitar o **espaço negativo** deixado no prompt (topo/base).
- Montagem: via editor (Canva) OU, se disponível, via ImageMagick no Bash
  (`convert`/`magick` com `-annotate`). Se não der pra montar aqui, entregue a
  imagem-base + a especificação exata do overlay pro usuário finalizar.

## Passo 3 — Salvar e registrar
- Salvar em `projects/<cliente>/paid/criativos/` com nome descritivo + data
  (ex: `v1-shes-not-real-2026-07-18.png`).
- Anotar qual prompt/ângulo gerou, pra cruzar com a performance depois (o
  `analista-trafego` fecha o loop).

## Regras de marca (obrigatórias)
- Ultrarealista e sexy, vertical, **sem "+18"/"18+"** na imagem.
- Nada de cara plástica/oversharpen. Realismo "parece foto de celular".
- Sem watermark ou logo não relacionado (recomendação de ads).
