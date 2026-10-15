# Lote 3 — Isabella / CenterPag

Peça-base do molde dos 35 dias. Quatro peças em `pecas/`:

| peça | layout |
|---|---|
| `lote3-isabella-s-en-a.mp4` | **molde base** — rosto full-bleed + tarja + bloco gráfico + karaokê |
| `lote3-isabella-L1.mp4` | rosto full-bleed + hook no topo + painel de screen no rodapé |
| `lote3-isabella-L2.mp4` | pilha de 5: screen · faixa vermelha · rosto · faixa vermelha · b-roll |
| `lote3-isabella-L4.mp4` | pilha de 3: b-roll · faixa vermelha · rosto |

Todas **1170×2532 · 660 frames · 22,000000s · 30fps**.

---

# REENTREGA 9:16 — 2026-09-02

As quatro foram **reprovadas no Meta Ads** junto com as 4 do lote 4: ratio 0,4621 contra o
mínimo 0,5625 do 9:16. Reentregues em **1080×1920** com sufixo `-9x16.mp4`, ao lado das
originais. **Nada foi sobrescrito** — as 1170×2532 são o registro do que foi medido.

Recomposição (não letterbox): cada camada reancorada no canvas novo, grafismo escalado por
1080/1170 = 0,923077. Custo US$ 0.

## Geometria medida nestas peças

Nenhuma delas tinha a geometria registrada. Medida agora, contra as próprias peças:

| peça | camadas e posições no master 1170×2532 |
|---|---|
| base | tarja y0 h498 (ON f0–437 e f589–659, corte seco) · bloco y1596 h936 (**fade 12f**: f438→450 e f576→588) · karaokê y**1670** h220 |
| L1 | rosto 1:1 rows 0–1907 · `hook-l1.png` y50 (sempre no ar) · `screen.mp4` 1170×624 y1908 (1:1, ancorado no rodapé) · karaokê y2024 |
| L2 | painel screen y0–760 · `faixa-l2-cima.png` y760 · rosto y963–1924 (= plate rows **501–1462**) · `faixa-l2-baixo.png` y1924 · painel b-roll y2127–2532 · karaokê y1500 |
| L4 | painel b-roll y0–760 · `faixa-l4.png` y760 · rosto y963–2532 (= plate rows **381–1950**) · karaokê y2024 |

As faixas e o hook **não têm janela de tempo** — ficam no ar os 660 frames. L1/L2/L4 **não usam**
tarja nem bloco gráfico.

O `bloco-grafico.png` é um **degradê**, não um painel chapado: alpha 0 em y1596 subindo até ~230
em y2000, com o card de UI (a lista de chat) em y1890–2502.

## Pilha 9:16 de cada variante

Os split-screens não aceitam "corte no rosto" — são pilhas e todos os painéis perderiam altura.
Orçamento de 417px decidido por painel:

| peça | pilha 1080×1920 | de onde saíram os 417px |
|---|---|---|
| base | rosto full-bleed · tarja 0–460 · bloco 1056–1920 · karaokê 1124–1327 | corte no topo do rosto (cabelo) |
| L1 | rosto 0–1344 · screen 1344–1920 | topo do rosto; painel screen intacto |
| L2 | screen 430 · faixa 187 · rosto 887 · faixa 187 · b-roll 229 | **só dos painéis decorativos**; rosto e faixas intactos |
| L4 | b-roll 702 · faixa 187 · rosto 1031 | topo do rosto |

No L2 o rosto já é uma fresta de 887px (só os olhos) — tirar dele mataria a peça. Os cortes de
screen e b-roll mantêm o **topo**: preservam o header "Accessing WhatsApp", o título "Chats" e
os dois rostos do b-roll.

## Verificação

- ffprobe das 4: `1080 × 1920 · 660 frames · 30/1 · 22,000000s` · h264 High · yuv420p · aac 44100 estéreo
- frames de prova em `medicao/9x16-*-f100-tarja-no-ar.png` e `-f510-bloco-no-ar.png`
- o modelo do molde base foi validado reconstruindo a `s-en-a` em 1170×2532 e diferenciando
  contra a original: **2,83/255** global (piso de ruído do H.264 ~2,10)

Detalhe completo, script de build e a conversa sobre placements em
`../lote4-grid-atores-2026-09-01/README.md`.
