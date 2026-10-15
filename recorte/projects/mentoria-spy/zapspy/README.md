---
tipo: projeto
atualizado: 2026-08-22
tags: [criativo, swipe, zapspy, split-screen]
---

# ZapSpy — criativo split-screen + 10 variações

## O que tem aqui

- `original/criativo-original.jpg` — o criativo-fonte baixado do CDN do Meta (338×600).
- `criativos/` — a réplica em alta (v00) + **10 variações**, 1080×1920 JPG, prontas pra subir.
- `criativos/manifest.json` — id, alavanca variada, hook e CTA de cada peça.
- `_lib/fotos/` — as 5 fotos reais usadas nos mockups (1 avatar + 4 capas de destaque),
  geradas com **GPT Image 2 via WaveSpeed** em 22/08 (US$ 0,29 no total).
- `galeria.html` — visualizador local auto-contido, com filtro por bloco e download por peça.
- `_build/render.py` — o gerador. Roda tudo de novo com `python3 _build/render.py` + o loop do Chrome.
- `_build/*.html` — o fonte de cada peça (editável, versionável, diff-ável).

⚠️ **Performance não verificada.** O criativo-fonte veio de uma URL de CDN, sem ad_id.
Não sei ROAS/CTR/gasto dele — não é (ainda) um campeão comprovado nesta operação.

## Teardown do criativo-fonte

**Formato:** vertical 9:16, três faixas — headline / comparação / CTA.

**Mecanismo:** *contraste do mesmo objeto*. O mesmo perfil aparece duas vezes lado a lado:
à esquerda dessaturado, tedioso, "tudo normal"; à direita colorido, com cards de alerta,
números específicos e badges vermelhos. Não vende uma feature — **manufatura a suspeita** de
que existe uma camada escondida na conta que a pessoa já tem.

**Alavancas que fazem funcionar:**

1. **Headline de contraste** — "WHAT YOU SEE" vs "WHAT REALLY HAPPENS", com o selo `VS` no
   meio. Estabelece o gap de curiosidade antes de 1 segundo de atenção.
2. **Cinza vs cor** — o dessaturado lê como "o que você tem hoje"; a cor lê como "o desbloqueado".
   Leitura instantânea, sem precisar ler texto.
3. **Números específicos e ímpares** — 47, 12, 23, 03:17 AM. Número redondo cheira a estimativa;
   número quebrado cheira a dado real.
4. **UI nativa do Instagram** — parece um print do app, não um anúncio. Compra atenção no feed
   por parecer conteúdo.
5. **Fotos reais nos slots de foto** — avatar e capas de destaque são fotografias, com anel
   gradiente de story. É isso que faz a peça ler como print, não como ilustração. Placeholder
   de gradiente entrega o truque na hora. As 5 fotos são as mesmas nas 11 peças (parte da DNA);
   o lado cinza usa os mesmos arquivos, dessaturados por filtro CSS.
6. **Value stack em 4 linhas** — cada card é um benefício-revelação distinto (quem viu, DMs
   ocultas, reações desconhecidas, atividade de madrugada).
7. **CTA de identidade, não de ação** — "Stop guessing. Start knowing." + pill "Link in bio ·
   Limited access" (escassez).
8. **Compliance** — tudo é enquadrado como dado *da conta da própria pessoa*, nunca da conta de
   terceiros. Mantive esse enquadramento em todas as 10 variações.

## Matriz de teste — 1 alavanca por variação

DNA travada em todas: layout split-screen, mockup de UI, cinza vs cor, números específicos,
enquadramento "sua conta".

| Peça | Alavanca variada | O que testa |
|---|---|---|
| `v00-replica-baseline` | — (controle) | Réplica do fonte em 1080×1920. Base de comparação. |
| `v01-hook-they-hide` | **Hook** → "What they hide" | Ocultação deliberada (tem um vilão) vs neutro |
| `v02-hook-who-watching` | **Hook** → pergunta direta | "Who's watching you / Now you'll know" |
| `v03-hook-instagram-shows` | **Hook** → vilão nomeado | Culpa o Instagram explicitamente |
| `v04-hook-your-app-vs-real` | **Hook** → app x realidade | "Your app right now / Your account for real" |
| `v05-stack-stalker` | **Value stack** → quem te observa | Ghost followers, buscas pelo seu nome, prints |
| `v06-stack-night` | **Value stack** → ângulo noturno | Recorrência ("27 noites seguidas"), digitou e apagou |
| `v07-cta-before-deleted` | **CTA** → urgência por perda | "See it before they delete it" + "Free check" |
| `v08-cta-30-seconds` | **CTA** → baixo esforço | "Check yours in 30 seconds" + "No password needed" |
| `v09-tema-alerta-vermelho` | **Cor/tema** → alerta vermelho | Quebra o padrão gradiente-IG do feed |
| `v10-tema-neon-verde` | **Cor/tema** → terminal neon | Cara de ferramenta/tech em vez de rede social |

**Como ler o teste:** v01–v04 competem entre si (hook), v05–v06 entre si (stack), v07–v08
entre si (CTA), v09–v10 entre si (tema). Cada bloco contra o v00. Não misture blocos na
mesma leitura — senão você não sabe qual alavanca moveu o número.

⚠️ Piso de volume antes de julgar: abaixo de ~150 impressões, ROAS individual é ruído.

## Por que HTML/CSS e não gerador de imagem

Criativo de mockup de UI tem texto exato, ícones e chrome de app. Modelo de difusão destrói
tipografia e inventa interface. Renderizando em HTML → Chrome headless → PNG: texto perfeito,
1 alavanca isolada por arquivo, e regerar as 11 peças custa ~15 segundos e R$ 0,00.

Regerar tudo:

```bash
cd projects/zapspy
python3 _build/render.py
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for f in _build/v*.html; do id=$(basename "$f" .html)
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --window-size=1080,1920 --virtual-time-budget=3000 \
    --screenshot="_build/${id}@2x.png" "file://$PWD/$f"; done
# depois downscale 2x -> 1080x1920 com PIL (ver histórico da sessão)
```

## Divergência proposital vs o fonte

O criativo-fonte usa **um homem** de boné e mochila no avatar. As 11 peças daqui usam uma
**mulher jovem creator** — escolha do Gusta em 22/08, por espelhar melhor quem consome app de
"quem viu meu perfil". Resto da identidade visual é fiel ao fonte.

## Próximo passo

Idioma: as 11 estão em **inglês**, igual ao fonte. Leads chegam também em ES — trocar os
textos é editar as strings em `_build/render.py` e rodar de novo (~15s, sem custo).
