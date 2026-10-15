# Fonte crua — reentrega 9:16 das 8 peças spy (2026-09-02)

Origem: correção de entrega pedida pelo Maestro depois de as 8 peças (lote3 L1/L2/L4/s-en-a +
lote4 slots 1–4) serem **reprovadas no Meta Ads**. Executado pelo Bisturi. Custo US$ 0.

## Diagnóstico (medido pelo Maestro, confirmado aqui)
- Todas 1170×2532 = ratio 0,4621 (9:19,47), mais alto que 9:16 (0,5625).
- 6 placements reprovados: FB Reels, FB Stories, IG Feed, IG Explorar, IG Feed do perfil, IG Busca.
- IG Reels e IG Stories **não** listados → assinatura de proporção, não de codec.
- Codec já correto: h264 High, yuv420p, 30fps, aac 44,1k estéreo.

## Geometria medida no master 1170×2532
- tarja: y0 h498, corte **seco**, ON f0–437 e f589–659
- bloco gráfico: y1596 h936, **fade de 12 frames** em cada ponta (f438→450 e f576→588);
  é um **degradê** (alpha 0 em y1596 → ~230 em y2000) com card de UI em y1890–2502
- karaokê: y**1670** h220 (o README do lote 4 dizia 1676 — errado por 6px)
- L1: rosto 1:1 rows 0–1907 · hook y50 (sempre) · screen.mp4 1170×624 y1908 · karaokê y2024
- L2: screen y0–760 · faixa y760 · rosto y963–1924 (plate 501–1462) · faixa y1924 · b-roll y2127 · karaokê y1500
- L4: b-roll y0–760 · faixa y760 · rosto y963–2532 (plate 381–1950) · karaokê y2024
- faixas e hook **não têm janela** — ficam no ar os 660 frames; L1/L2/L4 não usam tarja nem bloco

## Validação do modelo antes de usar
Reconstruí a s-en-a em 1170×2532 a partir das fontes e diferenciei contra a que shippou.
1ª tentativa: **15,52/255** na faixa do karaokê (card 6px baixo). Corrigido: **2,83/255** global,
faixa do karaokê **2,18** contra piso de ruído **2,10**.

## Saída 9:16 (1080×1920, escala do grafismo 0,923077)
- base: rosto cortado 417px no topo · tarja 0–460 · bloco 1056–1920 · karaokê 1124–1327
- L1: rosto 0–1344 · screen 1344–1920
- L2: screen 430 · faixa 187 · rosto 887 · faixa 187 · b-roll 229 (417px só dos decorativos)
- L4: b-roll 702 · faixa 187 · rosto 1031

## Verificação
- ffprobe das 8: 1080×1920 · 660 frames · 30/1 · 22,000000s · h264 High · yuv420p · aac 44100 estéreo
- áudio: md5 do PCM **idêntico** ao original nos 4 slots (-c:a copy)
- tarja: janela OFF f438–588 **idêntica** nas 5 peças do molde base
- karaokê: **193/193** fronteiras de card trocam no mesmo frame que no original
- md5 do frame 300: 4 distintos nos slots do lote 4

## Ressalva de placement (confirmada pro Maestro)
9:16 devolve **2 dos 6**: FB Reels e FB Stories. IG Feed/Explorar/Perfil/Busca capam em 4:5 (0,8)
e continuam fora. 4:5 é impossível por corte neste layout: tarja 460 + rodapé 864 = 1324 de 1350
= **98,1%**, sobram 26px de rosto.

Ingerido em [[ratio-de-entrega-por-placement]] e [[recompor-criativo-para-outro-canvas]].
