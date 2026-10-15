---
tipo: referencia-criativo
atualizado: 2026-09-09
tags: [teardown, edicao, spy-zap, centerpag, whatsapp, faixa-verde, card-flutuante, troca-avatar]
fonte: https://www.facebook.com/ads/library/?id=939122432559594
ad_id: "939122432559594"
arquivo_peca: centerpag-detect/anuncios/emilly-bredoff-939122432559594.mp4
---

# Teardown de EDIÇÃO — Emilly Bredoff (939122432559594)

34,07s · 360×480 · 30fps · locução masculina em inglês.

Este teardown cobre **só a edição** — layout, medidas, fases, cortes e o que dá pra reaproveitar —
pra guiar a **troca de avatar** (áudio e copy ficam os do original). Mesmo formato do teardown de
edição do wpp-01 (`2026-09-01-teardown-edicao-wpp01-esther-vicman.md`).

> ⚠️ **Alvo do lote:** trocar SÓ o rosto. Toda a locução, a faixa verde, o card do app, o karaokê
> (não existe — ver abaixo) e o CTA ficam idênticos ao original. O que muda é o talking head.

## Arquivo da peça

Caminhos **relativos a `projects/mentoria-spy/`**:

| O que | Caminho |
|---|---|
| **Vídeo (fonte)** | `centerpag-detect/anuncios/emilly-bredoff-939122432559594.mp4` |
| Registro | `centerpag-detect/manifest.json` → `ad_id 939122432559594` |
| Frames por fase | `centerpag-detect/referencias/frames/emilly-f1..f8-*.jpg` |

`.mp4` 809.132 bytes, md5 `e00cc6a45215ee7413a982c591f1442d`. Ad Library:
<https://www.facebook.com/ads/library/?id=939122432559594>

⚠️ Mídia pesada não entra no git — o portal referencia o arquivo no disco.

## Sinal de escala

#3 de 87 em impressões no swipe da Ad Library, **16,1 dias no ar**, ângulo `Free Test ✅` (mesmo
grupo do wpp-01 Esther Vicman, que é #1). É o **mesmo proxy de sempre**: a Meta não publica gasto,
CTR, CPA nem ROAS. 16 dias no ar é sobrevivência de verdade (um anúncio que não paga é pausado
antes), mas continua sendo *sinal de sobrevivência*, não campeão medido.

No teardown do wpp-01, esta peça já tinha sido classificada como "matte curta, limítrofe" na
varredura de formato — e é: a faixa aqui é **verde e mais fina**, não a matte preta de 15% do
vencedor. É um molde de edição **próprio**, mais simples que o do wpp-01.

---

## Layout medido (360×480)

```
┌──────────────────────────────┐  y 0
│  (margem preta)              │  y 0–28   ← preto chapado (0,0,0)
│  ██ FAIXA VERDE + HOOK ██    │  y 29–84  ← 11,7%, verde #04F919, texto preto, 2 linhas
│     "How to catch someone    │              caixa mista, bold, fixa 0–28,9s
│      hiding the truth"       │
├──────────────────────────────┤  y 85
│                              │
│   TALKING HEAD (ESQUERDA)    │   ┌────────────────┐
│   plano cheio, homem +       │   │  CARD DO APP   │  ← composto POR CIMA,
│   microfone, quarto escuro   │   │  (DIREITA)     │     semitransparente, cantos
│   com luz quente atrás       │   │  ZapSpy.ai →   │     arredondados, SEM borda dura.
│                              │   │  terminal →    │     Ocupa ~x150–360.
│   olhos ≈ y180–200           │   │  chats         │
│                              │   └────────────────┘
└──────────────────────────────┘  y 480
```

**Fronteiras medidas (por cor/cobertura no frame de 2s):**

| Elemento | Medida | Método |
|---|---|---|
| Margem preta do topo | `y 0–28` | preto 100% (0,0,0) |
| **Faixa verde** | `y 29–84` (h 56px = **11,7%**) | cobertura verde > 50% por linha |
| Cor da faixa | **#04F919** (verde puro) | mediana dos pixels verdes |
| Texto da faixa | **#000000** (preto) | pixels escuros dentro da faixa |
| Card do app (acentos verdes) | `x 188–359`, começa ~`y 120` | botões/checks verdes do card |

⚠️ **As laterais do card não são medíveis** (é composição com alpha, borda em gradiente, não
degrau) — mesma armadilha do wpp-01. O card fica na **metade direita** (x ≈ 150–360); o rosto fica
na esquerda. Não é split com fronteira dura: é 1 plano + overlay semitransparente.

- **Faixa verde:** verde chapado com o hook fixo `How to catch someone hiding the truth` em preto,
  2 linhas, caixa mista, bold. **Nunca muda** de 0 a 28,9s; some no corte pro CTA. Fonte sans bold
  (Poppins/Montserrat-like), ~28px, centralizada.
- **Talking head:** homem negro, ~30 anos, barba, camiseta escura, **microfone de podcast à
  frente**, quarto escuro com uma luz quente (abajur/vela) atrás do ombro direito. Enquadramento
  busto, rosto na **metade esquerda**, olhos em ≈ y180–200. Olha pra câmera, gesticula. Presente
  **0 → 28,9s** (85% da peça).
- **Legenda karaokê:** **não existe.** Medido: 0 pixels de texto amarelo abaixo da faixa em 6
  frames amostrados (t4/8/12/18/22/26s). O único texto fixo é a faixa verde; o resto do texto é a
  UI do card. Isso é mais simples que o wpp-01 (que tem karaokê sobre o card).
- **Watermark:** `ZapSpy.ai` no topo do card (não é falada).

**Diferença estrutural pro wpp-01:** lá a matte é preta e 15%; aqui é **verde e 11,7%**, com margem
preta acima. Lá o rosto sai aos 30,8s (46% com rosto); aqui o rosto fica até 28,9s (**85% com
rosto**) e some só no CTA. Sem karaokê aqui. Card na direita, não centralizado.

---

## As fases de tela (corte medido por detecção de cena)

**Só existe UM corte de quadro inteiro: `28,93s`** (o CTA). Tudo antes disso é o mesmo plano
(rosto esquerda + faixa verde) com o **card da direita trocando de conteúdo por alpha**, sem corte.

| Fase | Tempo | Rosto | O que roda no card (direita) | Fala por cima |
|---|---|---|---|---|
| **1 — Discover / features** | 0,0–~9,5 | sim | `ZapSpy.ai · Discover What They're Hiding From You` · `Recover deleted messages, photos and videos` · barra vermelha `2,911 suspicious activities detected today` · lista `Read all messages / Recover DELETED messages / View photos & videos` · `Enter the phone number to spy` | abertura + "no need to have physical access" + "she'll never find out she's being spied on" |
| **2 — Entrada do número** | ~9,5–11,5 | sim | número sendo digitado `33479…`, teclado numérico, botão verde `Start Spying` | "first enter your partner's number on the site below" |
| **3 — Acesso + perfil** | ~11,5–14,5 | sim | `Accessing WhatsApp +1 3347950651` + checklist (`Connecting to WhatsApp servers / Verifying phone number / Loading profile data / Scanning for deleted messages`) → card do perfil `+13347950651 · Registered on WhatsApp · Online · 54 Deleted Messages · Start Recovery & Spy · Change Number` | "wait a few seconds while the site tracks and clones the messages" |
| **4 — Terminal** | ~14,5–22 | sim | terminal vermelho `root@zapspy:~# sync --all --export` · `[ALERT] Suspicious keywords detected` · `1,847 messages synchronized / 254 media files / 13 suspicious conversations flagged / 7 shared locations recovered` · `ACCESS GRANTED — LOADING DATA` · barra verde `Finalizing access` · badge `SMS INTERCEPTED` com `7▓-▓▓▓` mascarado | "done! now you have access to all messages, photos, videos, real-time location, and even deleted messages" |
| **5 — Lista de chats** | ~22–28,9 | sim | UI `Chats` do WhatsApp, contatos borrados, tarja `147 deleted messages recovered`, barra verde `Unlock all conversations`, conversas com badges vermelhos (`Old F***`, `Lov***`) | "I'll leave a link below where you can run a free check using my personal account. But be quick because it's limited." |
| **6 — CTA** | **28,9–34,07** | **não** | corte seco. Fundo vira **b-roll borrado** (rosto de mulher, plano desfocado), **setas brancas ⌄⌄ pulsando** no centro, texto amarelo itálico `…AND SEE THE TRUTH NOW.` no topo (`y 96–111`, x 48–311) | "tap the button below and type the number you want to spy on" |

**O corte que importa é o de 28,93s** — único da peça. O rosto abre e sustenta os 28,9s inteiros
(a prova roda ao lado dele, não no lugar dele), e só no CTA final de ~5s o rosto some e entra o
b-roll borrado com as setas. É o inverso do wpp-01, onde o rosto sai no meio e a UI toma a tela.

---

## Transcrição com tempo (whisper local)

Método: áudio extraído com ffmpeg (mono 16kHz), transcrito com `mlx-whisper`
(`whisper-small.en`) — nada saiu da máquina. 112 palavras, **258 wpm** (fala rápida, corrida).

| Tempo | Fala |
|---|---|
| 0,0–5,3 | Here's how to see text messages from your boyfriend's, girlfriend's, husband's, or wife's phone using your own phone. |
| 5,6–7,1 | No need to have physical access to the phone. |
| 7,3–10,0 | And the best part? She'll never find out she's being spied on. |
| 10,2–12,4 | Look, first enter your partner's number on the site below. |
| 12,6–15,0 | Wait a few seconds while the site tracks and clones the messages. |
| 15,4–15,6 | Done! |
| 16,1–21,5 | Now you have access to all messages, photos, videos, real-time location, and even deleted messages. |
| 21,8–24,6 | I'll leave a link below where you can run a free check using my personal account. |
| 24,9–26,1 | But be quick because it's limited. |
| 26,5–28,7 | Tap the button below and type the number you want to spy on. |

**Texto corrido:** Here's how to see text messages from your boyfriend's, girlfriend's, husband's,
or wife's phone using your own phone. No need to have physical access to the phone. And the best
part? She'll never find out she's being spied on. Look, first enter your partner's number on the
site below. Wait a few seconds while the site tracks and clones the messages. Done! Now you have
access to all messages, photos, videos, real-time location, and even deleted messages. I'll leave a
link below where you can run a free check using my personal account. But be quick because it's
limited. Tap the button below and type the number you want to spy on.

⚠️ **Trava de política — esta locução é a mais exposta do acervo.** Diferente do wpp-01 (que nunca
diz "hackear/espionar" e joga a promessa pesada só na imagem), a fala aqui diz explicitamente
**"spied on"**, **"tracks and clones the messages"**, **"the number you want to spy on"**. Como o
Gusta quer manter o áudio original, isso não muda neste lote — mas **registrar**: é o áudio que mais
arrisca derrubar conta. Se em algum momento for regravar, é este o eixo a suavizar.

---

## Frames exportados por fase

Em `centerpag-detect/referencias/frames/`:

| Fase | Frame |
|---|---|
| 1 — Discover | `emilly-f1-chats-0.5s.jpg` |
| 2 — Teclado | `emilly-f2-keypad-10.0s.jpg` |
| 3 — Accessing/perfil | `emilly-f3-accessing-12.8s.jpg` |
| 4 — Terminal | `emilly-f4-terminal-16.0s.jpg` · `emilly-f5-sms-20.0s.jpg` |
| 5 — Lista de chats | `emilly-f6-chatslist-24.0s.jpg` · `emilly-f7-conversas-26.5s.jpg` |
| 6 — CTA | `emilly-f8-cta-29.5s.jpg` |

Folha de contato completa (1 fps) no scratchpad da sessão.

---

## Reaproveitável por recorte vs. o que refazer

O objetivo do lote é **trocar só o rosto**. O que dá pra manter do original:

**Reaproveitável direto (não precisa refazer):**
- **Áudio inteiro** — é a locução original, ordem do Gusta.
- **Faixa verde do topo** (`y 0–84`, verde #04F919 + texto preto): é uma faixa chapada com texto
  fixo. Dá pra **recortar do original** (crop `y 0–84, x 0–360`) e sobrepor no vídeo novo, ou
  redesenhar idêntica (retângulo #04F919 em y29–84 sobre margem preta y0–28 + texto). Fixa os 28,9s.
- **Card do app inteiro** (metade direita, todas as fases 1–5): é overlay semitransparente que não
  depende do rosto. Recortar a região do card do original e compor sobre o rosto novo. Como o card
  é alpha e o fundo é escuro, a emenda some se o quarto novo também for escuro.
- **CTA final** (28,9–34,07s): o b-roll borrado + setas + texto amarelo **não tem o rosto** — é
  reaproveitável 100%, cola direto no fim do vídeo novo.

**Precisa ser refeito (é o trabalho do Bisturi):**
- **O talking head** (metade esquerda, 0–28,9s): gerar o rosto novo em plano cheio 360×480 (ou
  gerar maior e reenquadrar), com lipsync **sobre a locução original**. É o único lipsync do lote —
  26,5s de fala (0–28,7s), então estimar o custo por `duração × preço unitário` e mostrar antes de
  disparar (saldo apertado; regra da casa). Enquadramento a bater: busto na esquerda, olhos ≈
  y180–200, microfone de podcast à frente, quarto escuro com luz quente atrás — pra o card e a faixa
  reaproveitados casarem sem reenquadrar.
- **Enquadramento/escala** do rosto novo pra ele ocupar a esquerda sem invadir o card (x até ~150).

**Ordem de montagem sugerida:** rosto novo (lipsync) na base → card do original (crop, fases 1–5)
por cima na direita → faixa verde (crop ou redesenho) no topo → CTA original (28,9–34s) coladinho no
fim. Uma alavanca do lote: **o rosto**. Nada mais muda.

---

## O que o Bisturi precisa saber antes de montar

1. **Não empilhe blocos.** É 1 plano (rosto) + overlays alpha (faixa verde no topo, card na
   direita). Igual ao wpp-01, o molde de blocos empilhados (L9) não serve.
2. **Faixa verde `y 0–84`** (#04F919, texto preto) é o único bloco com fronteira dura medida —
   reaproveitável por crop.
3. **Rosto fica até 28,9s** (85% da peça), na **esquerda**; o card fica na **direita**. Um corte só,
   em 28,93s, pro CTA.
4. **Sem karaokê** — não recriar legenda; a peça não tem.
5. **CTA (28,9–34s)** não tem rosto — reaproveitável 100%.
6. **Só 26,5s têm fala/rosto** — o lipsync não cobre os 34s. Estimar custo (duração × preço
   unitário) e reportar antes de gerar. Nada pago dispara sem a conta mostrada.

---

## Reconciliação com o Bisturi (09/09) — medidas conferidas

As medidas do Bisturi batem com as minhas; onde divergem, a dele é mais fina (mediu bordas que eu
só estimei). Vale a dele:

| Item | Peneira | Bisturi | Vale |
|---|---|---|---|
| Faixa verde (y) | y 29–84 | y 29–83, 2 linhas pretas (y 35–51 / 57–78), cantos arredondados | **Bisturi** |
| Faixa verde (x) | não medi | **x 43–316** | Bisturi |
| Cor da faixa | #04F919 | #00FD11 | qualquer — verde puro; texto **#000000** |
| Card (borda esquerda) | ~x150 | **x ≈ 125** até a borda, y ≈ 95 até o rodapé (corre pra fora), alfa | **Bisturi** |
| Karaokê | 0 px em 6 frames | **0 px em 14 frames** | **confirmado: não existe** |
| Corte pro CTA | 28,93s | 29,1s | ~29s (ambos) |
| CTA | texto amarelo y 96–111 | topo preto y 0–95, `AND SEE THE TRUTH NOW.` y 96–111, chevrons x 127–233 · y 315–424 | **Bisturi** |

**Confirmações:** karaokê não existe (não recriar). Card é alfa sem borda dura (não empilhar).
Faixa verde e CTA são recortáveis do original.

### Enquadramento 9:16 do Bisturi — aprovado, com uma ressalva

O original é 360×480 (4:3 retrato), que fica com tarja preta em Reels/Stories. Rebuild em 9:16
(1080×1920) é a decisão certa — a regra da casa é **refazer, não cortar** peça 4:3 pra vertical. A
matemática do Bisturi fecha (×3 centrado, offset y 240): caixa `x 129–948 · y 327–489`, card
`x 375–1080 · y 525–1680` com fade nos últimos 200px, CTA refeito em tela cheia. Endossado.

⚠️ **Única ressalva de composição:** no original o rosto fica na **metade esquerda** e o card cobre
a **direita** sobre o quarto escuro — o card nunca fica sobre o rosto. Se o talking head novo for
gerado em 1080×1920 **cheio**, o card (x 375–1080, 65% da direita) vai cair **sobre o lado direito
do rosto novo**. Pra reproduzir o original, gerar/reenquadrar o rosto novo com o **sujeito à
esquerda** (rosto até ~x 375) e o lado direito sendo o quarto escuro, pra o card alfa ler sobre
fundo, não sobre a cara. Se o rosto vier centralizado, empurrar pra esquerda no reenquadre.

**Sobre o CTA em 2 linhas:** o original 4:3 só expõe `…AND SEE THE TRUTH NOW.` (a 1ª linha fica
acima do corte). Restaurar `CLICK THE LINK BELOW / AND SEE THE TRUTH NOW.` no rebuild 9:16 é ok — é
o CTA padrão da casa (idêntico ao wpp-01) e provavelmente é o que está no asset original acima do
crop. Manter a redação exata, sem inventar palavra a mais.
