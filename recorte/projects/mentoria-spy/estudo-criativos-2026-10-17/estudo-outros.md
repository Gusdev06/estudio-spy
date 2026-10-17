# Estudo "outros" (concorrentes de outras operações) — 2026-10-17

36 criativos analisados (31 vídeo transcritos via Groq + 5 estáticos). Hosts: love-vision.site (a maior, ~2.100 ads ativos), spygran.site, raygort.site, igyhall.com, socialcatfish.com, deepscanner.app, apps.apple.com (Toxic), play.google.com (Lens AI), acessosegurosite.

## 5 famílias mais fortes

1. **lovevision-roteiro-tutorial (24 peças)** — a máquina da operação. UMA locução fixa ("Here's how to see text messages from your boyfriend's/girlfriend's/husband's/wife's phone using your own phone… digite o número no site → espere clonar → acesso a msgs, fotos, vídeo, localização e apagadas → free check na minha conta pessoal → limitado"), rodada em dezenas de **avatares e layouts** diferentes (mulher cacheada laranja, mulher negra de óculos, homem de gravata, menina no carro, mockup "ZapSpy.ai", etc.). Variação é só presenter/idioma/painel; o roteiro e o funil não mudam. Ids: `2062739147710276`, `2647888292315370`, `1787625328837106`, `1918182765826828`, `28179726865061804`, `1075070088727666`, `1822640478889715`, `884243871425422`, `1677177574122402`, `39512579731688656` (raygort) e +14. Sub-variante que manda BAIXAR app ("Download the app Spy"): `1610986594095004`, `1053672644293900`.

2. **socialcatfish-dare-estatico (5 peças)** — estático tipográfico, zero produção: "If you truly trust your boyfriend/husband… I dare you to enter his phone number here and see if he has hidden profiles" + CTA "SEARCH HIS NUMBER". Gira só o fundo (preto/branco/bordô/cinza) e boyfriend↔husband. deepscanner reaproveita o mesmo ângulo com copy reescrita ("fully trust"/"sneaky profiles"). Ids: `2155258641696139`, `1085399717277321`, `1332281048929624`, `1431495745694214`, `1100765479377961`. Mais barato que existe.

3. **spygran-depoimento-deceived (1, mas forte)** — `1654197269397552`. Talking head + cards lower-third telejornal (HIDDEN DATA DETECTED 310/172 · DECEIVED FOR 5 YEARS · THE TRUTH I DISCOVERED · 100% REMOTE AND ANONYMOUS) + loader "Accessing WhatsApp" + mapa. Depoimento emocional (enganada 5 anos) encaixado no funil. É o L10 do nosso catálogo bem executado.

4. **instagram / people-search (4: `1992989964723745`, `2191993585086576`, `2270093183789403`, + mockups)** — foge do WhatsApp: vigiar Instagram/perfis de dating. GramDetect (screen-rec puro "Girl, your boyfriend won't give you his Instagram?"), Toxic (track IG, stories anônimas, tom fofoca "I'm just a girl") e Lens AI deepsearch ("caught him cheating" buscando o NOME e achando OnlyFans/Tinder). Ângulo de busca-por-nome/username, não por número.

5. **whatsapp-mirror / nova-função (2: `1424266205856533`, `1152365540788750`)** — talking head "DID YOU KNOW IT'S POSSIBLE TO MIRROR ANY WHATSAPP USING JUST A PHONE NUMBER" (legenda queimada palavra-a-palavra) e igyhall "AMAZING NEW FEATURE IN WHATSAPP" (screen-rec de celular na mão, ângulo curiosidade "nova função" em vez de acusação).

## Problemas / notas
- Whisper alucina "Thank you."/"you" em trechos mudos (`1992989964723745` é praticamente mudo — é screen-rec); filtrados.
- `idioma` saiu tudo "en" por simplificação no build; todos os vídeos realmente são locução em inglês, mas o CTA do botão aparece em PT ("Saiba mais"/"Ver detalhes") no Facebook — não confundir com idioma do criativo.
- `ref` sempre "-" (concorrentes, sem PPA nosso). `dias`: só love-vision/raygort/igyhall/socialcatfish têm data de início no manifest; spygran veio sem `inicio` (dias=0).
- Reforço do insight do catálogo: a alavanca de escala deles é **mesma locução, N layouts/avatares** — exatamente o eixo L1–L9 (recombinar blocos na edição). Dá pra clonar o roteiro LV e variar só o presenter/painel.
