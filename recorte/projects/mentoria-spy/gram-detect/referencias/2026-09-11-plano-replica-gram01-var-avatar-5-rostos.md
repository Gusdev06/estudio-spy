---
tipo: plano-replica
atualizado: 2026-09-11
lote: ../criativos/gram01-l9-var-avatar-2026-09-11/
controle: ../criativos/gram01-l9-faixa-2026-09-01/pecas/gram01-l9-en-01-v2.mp4
casting: 2026-09-11-casting-gram01-var-avatar-5-rostos.md
alavanca: avatar (só o rosto muda)
autor: Peneira
tags: [plano-replica, spy-gram, L9, avatar, gram01, pruna]
---

# Plano de réplica — GRAM 01 · L9 · alavanca AVATAR · 5 rostos

Controle: `gram01-l9-en-01-v2.mp4` (1170×2532 · 975 frames · 32,500 s · 30 fps · colapso no
frame 940). V1..V5: **tudo idêntico menos o bloco de rosto** (head 0–1212 nos frames 0–939 +
cauda em quadro cheio nos frames 940–974). Casting e prompts em
`2026-09-11-casting-gram01-var-avatar-5-rostos.md`. Itens marcados **PROPOSTA** são decisão
do maestro/Gusta, não minha.

---

## (a) Por que o controle vende — 10 linhas

1. **Não sabemos se vende.** O controle nunca teve métrica; foi modelado na peça #1 da Ad Library
   ([[criativo-gram01-1761247818659822]]), cujo "ranking" é proxy de sobrevivência (3,2 dias, sem
   flag `<100`, rank de impressões) — e essa peça **é a nossa SPY 4** ([[swipe-que-mediu-a-propria-operacao]]),
   que nem entrou entre as 10 que gastaram na nossa conta; os L9 irmãos (SPY 1, 2, 7) fizeram US$ 47 / 0,63 / 50
   ([[familia-criativos-spy-gram-16-julho]]).
2. O que **tem** dado é o roteiro: o mesmo texto ("There's one detail on Instagram…") está no nosso
   campeão real GD-AD01 (US$ 4.074, [[criativo-gd-ad01]]) e em 5 peças abaixo de US$ 50 —
   [[roteiro-igual-gasto-diferente]]: o roteiro é condição, a casca decide.
3. A estrutura de 29 s é resposta direta completa: curiosidade → 3 objeções mortas ("guess / argue /
   touch anyone's phone") → mecanismo (quem esconde escorrega) → payoff social → CTA de direção +
   escassez ([[roteiro-mestre-com-n-vozes]]).
4. A fala nunca diz espionar/DM/senha; quem promete é o painel do funil ([[promessa-pesada-so-na-imagem]]).
5. Três camadas de gancho que não se repetem — faixa fixa (lê no mudo), B1 falado, wizard já
   preenchido ([[tres-camadas-de-gancho-sem-repeticao]], [[banco-de-hooks-gram-l9]]).
6. Funil e dor rodam lado a lado o tempo todo ([[dor-e-mecanismo-em-paralelo]], [[funil-gravado-como-painel-lateral]]).
7. O colapso aos 31,333 s devolve o rosto sozinho em cima do CTA falado — o único momento sem
   painel pra olhar; é a versão L9 de [[fechar-o-argumento-antes-do-rosto-sair]]: o argumento
   fechou, o rosto vem selar.
8. Arquétipo "amiga que descobriu": rosto de gente comum em cômodo de casa, sem credencial
   ([[autoridade-por-enquadramento]] pela via oposta). Nos 4 que gastaram na nossa conta o rosto é
   sempre 25–30 em cômodo íntimo.
9. O que o controle **não** tem e o campeão tem: karaokê ([[legenda-karaoke-e-pre-requisito]]) e
   alternância rosto↔app. A faixa fixa sem legenda é a marca dos L9 que morreram ([[slogan-fixo-nao-e-gancho]]).
10. Portanto a leitura honesta: este lote testa **rosto dentro de uma casca que, na nossa conta, é
    fraca**. Um vencedor aqui prova rosto; um empate geral prova casca — e isso já é resposta.

## (b) O que o head precisa PRESERVAR pra alavanca ser só o rosto

| Dimensão | Controle (medido) | Regra pras V1..V5 |
|---|---|---|
| Duração / frames | 975 frames · 32,500 s · 30 fps (`ffprobe` da peça) | idêntico ao frame; cortar o clipe do Pruna em 32,500 s (ele devolve ~0,7 s a mais — var4: 33,04 s pra 32,37 s de áudio) |
| Colapso | frame **940** (31,333 s): faixa some, painel some, rosto em quadro cheio | idêntico; cauda = frames 940–974 (35 frames) |
| Head | `y 0–1212`, olhos mediana **47,3 %** (572 px), p25–p75 43,9–49,1 %; rosto **47,9 %** da largura (560 px); queixo 87 %; ombros cortados nas laterais, mãos fora | imagem-base com olhos a **27 %** do 9:16 e rosto a 48 % da largura; recorte do topo 704×730 → ×1,662 (conta na seção 2 do casting) |
| Cauda | 1170×2532, olhos **44,2 %** (1117 px), rosto 48,5 % (567 px) — mesma escala do head, 545 px mais baixo | **PROPOSTA:** escalar pela largura (1170×2127) e descer 544 px com preenchimento de topo — casa escala e altura. Alternativa: escalar pela altura (olhos a 26,9 %, rosto 57 %) — sem preenchimento, geometria diferente |
| Movimento | cabeça passeia: olhos 38–59 %, nariz 35–76 % da largura ao longo dos 31 s (63 frames a 2 fps) | o Pruna gera o próprio movimento; não medir amplitude é aceitável, mas **rosto parado 32 s** reprova (lê como stock — seção 7 do roteiro) |
| Luz / câmera | frontal de celular, um pouco abaixo do olho, luz disponível fria, subexposta | mesma gramática; temperatura pode variar com o cômodo, ring light nunca |
| Arquétipo | mulher ~25, casa, sem credencial | mulheres 25–40, casa; sem jaleco, sem estúdio |
| Gênero | rosto feminino; VO f0 mediano 170 Hz (maestro) | feminino nas 5 ([[avatar-segue-o-genero-da-voz]]) |
| Boca | v2 tem lipsync (`lipsync-2-pro`) | Pruna sincroniza a partir da VO inteira; **uma chamada por avatar sobre os 32,5 s** (decisão 4 do maestro) — sem costura no colapso |
| VO, funil, b-roll, faixa | `vo-master-en.m4a`, `funil-painel.mp4`, `broll-painel.mp4`, `en-01.png` | bit-idênticos (md5 igual ao do controle na conferência) |

Trava herdada: nada de cortar pausa na VO (0 silêncios ≥ 0,4 s a −35 dB, medido pelo maestro).

## (c) O que a casa já sabe dos lotes de avatar anteriores

| Lote | Modelo | Custo real | O que aprendeu |
|---|---|---|---|
| `gd-ad01-var-avatar-2026-09-03` (D) | OmniHuman 1.5 | **US$ 5,28** (0,16/s × 32,6 s + imagem 0,06) | clipe cru 718×1286 25 fps; olhos vieram a ~28 % e o rosto menor que o do campeão → zoom 1,25× e recorte pelo topo pra levar a ~35 %; 25→30 fps por duplicação; **"718 px × 1,88 de escala: mais macio"** registrado como contaminação; mãos fora do quadro |
| `zap-emilly-avatar-2026-09-09` | OmniHuman 1.5 | **US$ 4,72** (0,16 × 29,1 s + 0,06) | gerar só o trecho com rosto cortou 15 %; o clipe veio **centrado** e o rosto 410 px contra ~300 do original → `--th-x −330`; conferência por folha de 8 instantes |
| `zap-emilly-avatar` var4 (10/09) | OmniHuman 1.5 ×4 | **≈ US$ 18,84** | **erro: 3 mulheres pra voz masculina; 1 job já cobrado = US$ 4,66 perdidos** → regra "avatar segue o gênero da voz original" (STATUS 10/09) |
| `zap-secret-revealed-avatar-2026-09-10` | OmniHuman 1.5 | **US$ 5,24** | rosto cheio o vídeo inteiro; molde reproduz faixa e karaokê |
| idem `var4/` (10/09) | **Pruna p-video/avatar** ×4 | **≈ US$ 3,50** (0,025 × 32,37 s × 4 + 0,24 de imagens) ≈ 0,81 por avatar | saída **704×1280, 25 fps, 33,04 s** pra 32,37 s de áudio (segura o último frame / corta); sujeitos centrados; 4 rostos (negro de óculos, loiro, indiano, grisalho de óculos) montados por vigília de pasta |
| `_teste-lipsync-2026-09-10` | 5 modelos, 8 s | ≈ US$ 1,70 | Gusta **escolheu o Pruna como padrão** (6× mais barato que OmniHuman); modelos "lipsync" (sync/veed/kling) exigem vídeo, não foto |
| `zap-wpp01-clone-3-ganchos-2026-09-11` | Pruna só no trecho com rosto (21+22+21 s) | **US$ 1,60** (lote 1,75) | avatar GPT Image 2 no padrão de prompt da casa (olhos a 37 %, câmera baixa); Gusta liberou com "SIM PODE GERA O LYPSYNC COM O PRUNA"; **aceitou H3 mostrando as mãos por ~2 s aos 7 s**; briefing registra 24 fps nesta rodada (var4 diz 25 — conferir no arquivo) |

O que o Gusta aceitou/decidiu: Pruna como padrão; lotes de "mesmo áudio, rosto novo" sobem **no
mesmo conjunto com o original como controle** (Emilly 15–19); mão visível por 2 s passou; na
rodada de 10/09 disse "não me pergunte nada, está liberado" — **mas o invariante deste canvas é
que pago pára na estimativa** (briefing, invariante 1): não herdar aquela liberação.

Estimativa da fase C: **5 × 32,5 s × US$ 0,025 = US$ 4,06** (+ US$ 0,30–0,60 de imagens já
autorizadas). Saldo na abertura: US$ 20,37 (`key:macbook`).

## (d) Riscos deste lote

1. **Nitidez como segunda variável.** O head do controle foi *reduzido* de 2160 px de largura; o
   dos V1..V5 será *ampliado* de 704 → 1170 (×1,66). V×V é limpo (as 5 têm o mesmo defeito);
   **V×controle carrega "rosto" + "textura mais macia"**. PROPOSTA: registrar como contaminação
   conhecida (igual à variação D) e não tentar corrigir com sharpen — sharpen artificial lê como IA.
2. **Mãos.** Prompt corta no peito; o Pruna pode animar ombros. Precedente aceito: 2 s de mão no H3
   do wpp-01. Conferir no clipe, não na imagem.
3. **Cauda.** As duas montagens da seção (b) são diferentes do controle em algo (preenchimento de
   topo ou geometria). Decidir antes de gerar, não depois.
4. **Deriva de identidade** ao longo de 32,5 s no Pruna: nunca medida na casa (lotes anteriores
   tinham 29–33 s e ninguém mediu). Conferir folha de 8 instantes por avatar.
5. **fps.** 24/25 → 30 por duplicação (1 em 5 ou 1 em 4 repete). Contaminação leve, igual nos 5.
6. **Meta.** A página Quinn foi banida; a **conta do Gerenciador do print de 03/09 está desabilitada**
   (`proprios-2026-09-03/00-ranking-comparativo.md`). Não está dito em qual conta este lote sobe.
   PROPOSTA: decidir a conta antes da fase C, senão são US$ 4 pra peça sem onde rodar.
7. **Nenhuma métrica verificada do controle** — leitura é V×controle dentro do mesmo conjunto, com
   piso de volume antes de julgar ([[piso-de-volume-antes-de-julgar-criativo]]).
8. **Gênero da voz.** 170 Hz é zona de fronteira (masculino típico 85–155, feminino 165–255). O rosto
   original do head é mulher, então "feminino" é coerente; e a "prova" de que o rosto não precisa
   casar com a voz (a #10 "homem de óculos") **caiu** — a #10 é mulher (ver HANDOFF pro Isca). Se o
   Gusta corrigir o gênero, é antes da fase C.
9. **Proporção da imagem-base.** Se o GPT Image 2 devolver 2:3, a conta de olhos a 27 % não vale sem
   recortar pra 9:16 antes.
10. **Copy da Meta** continua a do "vencedor" palavra por palavra (invariante 6) — e ela é a nossa
    copy de julho. Sem número inventado, sem depoimento.

## (e) Matriz do teste

| Peça | Head + cauda | Tudo o mais | Status |
|---|---|---|---|
| **Controle** | `gram01-l9-en-01-v2.mp4` — mulher negra ~25, tranças, sofá, luz fria | — | pronto, nunca rodou |
| V1 `v1-branca-25-quarto` | rosto-tipo do GD-AD01 | idêntico | imagem → Pruna |
| V2 `v2-latina-32-cozinha` | latina ~32 | idêntico | imagem → Pruna |
| V3 `v3-asiatica-27-vaidade` | reteste SPY 7 fora do L9 mudo | idêntico | imagem → Pruna |
| V4 `v4-branca-40-sala` | eixo idade (40) | idêntico | imagem → Pruna |
| V5 `v5-negra-30-mesa-luz-quente` | réplica dentro da demografia do controle | idêntico | imagem → Pruna |

**PROPOSTA de leitura:** 6 peças no **mesmo conjunto**, copy da Meta igual, controle incluído
(precedente Emilly 15–19). Ler thumbstop 3 s, hold até o colapso (31,3 s), CTR e CPA; nada é
lido abaixo do piso de volume. Duas perguntas, em ordem: (1) alguma V ganha do controle? — rosto é
alavanca; (2) V5 fica com o controle e V1–V4 se afastam? — a alavanca é demografia, não pessoa.
Se tudo empata dentro do ruído, a resposta é da casca (L9 fixo sem legenda), e o próximo lote
troca de casca, não de rosto.

Fases (do briefing): A custo zero (molde provado contra o controle) → B centavos (5 imagens +
stand-ins com a imagem parada no lugar do head) → **C pago: US$ 4,06, para na estimativa**.

## Passagem de bola

- **Bisturi:** casting seção 2 (a conta dos olhos) e o parágrafo "o que o Bisturi confere"; decidir a
  cauda antes da fase C.
- **Isca:** HANDOFF sobre a #10 (`HANDOFF-peneira-para-isca.md`).
- **Maestro/Gusta:** conta em que o lote roda; gênero da voz (confirmar feminino); cauda; V5 ou reserva.
