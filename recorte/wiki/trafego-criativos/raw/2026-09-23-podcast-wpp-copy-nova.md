# Podcast WPP 57 s — COPY NOVA + 2 avatares novos · 2026-09-23 → peça 106

Pedido do Gusta: variação do criativo da Ad Library `AQMV-j5b…mp4` (md5 `9d5acf68…`) **mudando avatar e copy**. É a versão cheia (57,1 s) do mesmo criativo que já clonamos em 13/09 e 19–21/09 (o `REFERENCIA-original-41s` era um corte dele).

## Molde medido no original
| camada | medida |
|---|---|
| Título (matte fixa) | caixa branca y 140–270, x 18–702, texto "HOW TO READ YOUR PARTNER'S MESSAGES ON YOUR OWN PHONE" o vídeo inteiro (some no CTA) |
| Janela de vídeo | 720×587 em y 346 |
| Karaokê | caixa alta branca, **caixa roxa (105,18,209) arredondada na palavra falada**, capital 39 px, y 967–1031, centralizado; ≤ 4 palavras por bloco |
| Estrutura | rosto 0–2,8 · painel 2,8–4,4 · rosto 4,4–16,4 · painéis do funil 16,4–37,6 · rosto 37,6–41,4 · **CTA b-roll em quadro cheio 41,4–56,8** (texto amarelo + setas, sem fala, música −28 dB) |
| Elenco | host de blazer sage (fala) + convidada de preto (pergunta) |

## O que foi refeito
- **Copy nova em diálogo** (`roteiro.tsv`, 109 palavras, 9 falas, 2 vozes MiniMax — A `Calm_Woman`, B `Wise_Woman`): abre com promessa concreta ("read every message… without ever touching his phone"), a convidada faz as objeções, o mecanismo aparece ("you type the number, the system pulls the backup"), prova do que se vê e CTA. Cada fala virou um bloco; pausas de 0,12 s (mesmo papel) e 0,24 s (troca de papel).
- **2 avatares novos** (`base/A.png`, `base/B.png`, gpt-image-2/edit sobre os frames do original): latina de blazer creme e asiática de blusa verde-escura, mesmo estúdio. 6 clipes Pruna (um por bloco de fala) com **prompt de identidade travada**; `checar-identidade.py` ok nos 6 (×1,00–1,04).
- **Karaokê redesenhado** (`gerar-karaoke.py`): Poppins Bold 52 px (capital 37) calibrado pela largura medida, caixa roxa arredondada, quebra por fim de frase e por largura (≤ 640 px) — o excesso cortava nas bordas no 1º render.
- **Janela**: recorte **centrado no rosto** (YuNet) respeitando a orientação do clipe (os clipes saem 1280×704; o 1º render usou 704×1280 e cortava a cabeça).
- **Painéis e CTA**: trechos do funil do próprio original reencaixados na nova timeline (16,45 s e 22,0 s) e os 15,4 s de CTA em quadro cheio, com a trilha dele.
- **Áudio**: locução normalizada (`loudnorm I=-16`, o MiniMax saía 6 dB abaixo da mistura do original) + cama de música do próprio original por baixo.

## Peça
`pecas/PODCAST-WPP-copy-nova.mp4` → `CRIATIVOS-PRONTOS/106` — 720×1280 · 30 fps · **49,0 s** · 0 silêncios ≥ 0,5 s. Conferência: `conferencia/final-folha.jpg` (14 instantes), `emendas.jpg` (antes/depois de cada troca de bloco), `varredura-final.jpg` (1 fps), `karaoke-orig-x-novo.png`, `casting.jpg`.

## Custo real: US$ 1,18 (TTS 9 falas 0,13 · 2 imagens 0,13 · 6 clipes Pruna 0,92)
Outra variação de avatar com a mesma copy: só regerar os 6 clipes (≈ US$ 0,9). Outra copy: refazer TTS + karaokê + clipes (≈ US$ 1,2).

## 5 variações de elenco (`var5/`) → peças 107–111 · 23/09
Mesma copy, mesmo áudio e mesma edição da 106, trocando só o par de avatares: negra de locs × latina · ruiva × negra de afro · indiana × loira · árabe de hijab × asiática · mestiça × filipina. Pipeline: 10 imagens (gpt-image-2/edit sobre os frames do original) → 6 clipes Pruna por variação (`var5/gerar-clipes.sh`, prompt de identidade travada) → `montar.py` com `CLIPES=var5/<w>/clipes` → `por-musica.sh` com a trilha de suspense (a validada na peça 06), normalizada em −28,5 dB. 49 s cada.

Conferência: `var5/casting.jpg`, `var5/final-5.jpg` (9 instantes por peça), `var5/w3-drift.jpg`. O detector de drift acusou w3 b4/b6 (×0,82): é a convidada loira virando um pouco o rosto — identidade e enquadramento mantidos, ficou. 1 clipe caiu por rede e foi refeito.

**Custo do lote: ≈ US$ 3,8** (10 imagens 0,67 + 31 clipes 3,1). Com a 106: US$ 5,0 pelas 6 peças.
