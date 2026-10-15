# "Super criativo" Spy Zap — copy com os 10 elementos, decidida pelo dado · 2026-09-19

Pedido do Gusta: "e do WhatsApp?" + "usa esses elementos para fazer a copy" (post @felipenonino_ / @the.filemon: 10 elementos de um criativo que escala — curiosidade, promessa, segmentação, problema, spoiler do mecanismo, autoridade, benefício, prova social, urgência, dupla CTA).

## Copy (`roteiro-10-elementos.txt`, 142 palavras, 43 s com pausas cortadas) — elemento a elemento
| # | elemento | trecho |
|---|---|---|
| 1 | Curiosidade | There's one thing on WhatsApp that gives a cheater away every single time |
| 2 | Promessa | and in sixty seconds you'll see it with your own eyes |
| 3 | Segmentação | If you're the one lying awake at two a.m. while their phone lights up face down |
| 4 | Problema | you already know something is wrong. You just can't prove it |
| 5 | Spoiler do mecanismo | they can delete a chat, but the backup keeps a copy, and that is where the traces live |
| 6 | Autoridade | It's the same recovery method investigators use, and now it's one tap away |
| 7 | Benefício | You don't touch their phone. You don't fight. You just type their number |
| 8 | Prova social | Thousands of people did it this week, and most of them had been lied to for months |
| 9 | Urgência | It won't stay online for long |
| 10 | Dupla CTA | Tap the link below and check the number now. If it's nothing, you sleep tonight. If it's something, you finally know |

Sem palavra proibida (hack/senha/espionar) — a promessa pesada fica nos painéis ([[promessa-pesada-so-na-imagem]]).

## Casca (mesma lógica do super Gram, com o dado do swipe Zap)
- **Gancho escrito:** caixa rosa com a família **A + B'** do [[mapa-de-ganchos-zap-26-escalados]] — "What their WhatsApp is hiding... / see this before it's too late" (as duas de maior lastro transferível: #1 de 87 e 107 peça-dias). Some em 7,8 s. Não repete a fala (3 camadas de gancho).
- **Avatar:** a mesma mulher ~28 sem maquiagem no quarto (`../../gram-detect/criativos/super-gram-2026-09-19/base/s1.png`), voz MiniMax Calm_Woman 1,1×, look de celular calibrado.
- **Edição:** molde reconstruído do AD02-H2 Zap (peça 59): card "Accessing cloud backup" → mapa TRACKING → rosto limpo → chats "257 deleted messages" + relatório → CTA + setas; painéis regerados da gravação real do funil com as durações da nova timeline (`gerar-paineis.sh`).
- Blocos nas palavras: card até "eyes", mapa até "prove it", rosto limpo até "away" (mecanismo + autoridade), painel B até "long", CTA em "Tap".

## Produção
Pruna recusou o áudio de 43 s duas vezes (saída vazia / indisponível, estornado). Solução: **áudio partido em 2 na fronteira do bloco de rosto limpo (16,27 s)**, dois clipes da mesma imagem, emendados (`clipes/s1-p1.mp4` + `s1-p2.mp4` → `s1.mp4`); a emenda cai num corte de bloco e não aparece. Gesto breve de mão no rodapé em ~37 s (bloco final), deixado.

## Peça: `SUPER-ZAP-10-elementos-s1.mp4` → `CRIATIVOS-PRONTOS/67` — 1080×1920 · 43,0 s · 1290 frames
Conferência: `conferencia/final-folha.jpg`, `hook-f60.jpg`, `varredura-s1*.jpg`. **Custo real: ≈ US$ 1,35** (TTS 0,05+0,08, Pruna 0,43+0,68; a tentativa de 43 s foi estornada).

Outra variação: `python3 montar-super-zap.py clipes/<clipe>.mp4 saida.mp4` (env `CAIXA_L1/L2`, `BOXSZ`, look).
