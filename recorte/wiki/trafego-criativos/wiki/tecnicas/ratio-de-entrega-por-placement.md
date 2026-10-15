# Ratio de entrega por placement

O Meta reprova criativo por **proporção**, não só por codec — e a lista de placements
reprovados diz qual é o problema.

## O caso que gerou a página (2026-09-02)

Oito peças spy saíram em `1170×2532` = ratio **0,4621** (9:19,47). O Ads Manager marcou
"anúncio não veiculável" em **6 placements** e **não** listou Instagram Reels nem Stories.
Codec estava certo o tempo todo: h264 High, yuv420p, 30fps, aac 44,1k estéreo.

**A lista de reprovados é o diagnóstico.** Se Reels/Stories passam e a família de feed reprova,
é proporção. Se reprovasse em tudo, seria codec ou peso.

## Os tetos que importam

| família | aceita | reprova 9:19,47? | reprova 9:16? |
|---|---|---|---|
| Facebook Reels · Stories | até 9:16 (0,5625) | sim | **não** |
| Instagram Reels · Stories | tolera mais alto | não | não |
| Instagram Feed · Explorar · Feed do perfil · Busca | teto **4:5 (0,8)** | sim | **sim** |

Consequência prática: **corrigir pra 9:16 devolve os placements de Reels/Stories, não a família
de feed.** Pra feed é preciso um segundo asset em 4:5 — e nem todo layout aceita.

## Quando 4:5 é impossível sem redesenhar

Faça a conta antes de prometer. No molde spy, a 1080 de largura:

- tarja do gancho: **460px**
- rodapé (bloco gráfico + card de UI): **864px**
- soma: **1324px**

Num canvas 1080×1350 (4:5) sobram **26px** de rosto — 98,1% da tela é grafismo. Não é escolha de
enquadramento, é aritmética: pra caber em 4:5 alguém tem que **reduzir a tarja ou o card**, o que
muda o criativo e vira outra alavanca. Ver [[variar-uma-alavanca-por-vez]].

**Regra:** some a altura dos grafismos fixos na largura de destino antes de decidir se um formato
é alcançável por corte. Se passar de ~70% do canvas alvo, é redesenho, não reformatação.

## Reformatar é recompor, nunca letterbox

Barra preta lateral encolhe o conteúdo na proporção do canvas perdido (24% no caso 9:19,47→9:16)
e mata a legibilidade do gancho no feed. O certo é **reancorar camada por camada** no canvas novo:
grafismo escala pela **largura** (mantém proporção contra a tela), e a altura que falta sai do
material que aguenta perder — no molde spy, o topo do cabelo.

Detalhe do método em [[recompor-criativo-para-outro-canvas]].

Relacionadas: [[catalogo-de-layouts-spy]] · [[variar-uma-alavanca-por-vez]] ·
[[estimar-custo-de-geracao-antes-de-disparar]]
