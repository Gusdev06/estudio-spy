---
tipo: tecnica
tags: [medicao, ffmpeg, avatar-ia, jump-cut, edicao, metodo]
fontes: [[fonte-teardown-sarah-flores-2026-10-14]]
---

# Costura de clipe de IA por diferença de frame — achar as emendas que o scdet não vê

Talking head de avatar IA é vários clipes curtos costurados no mesmo enquadramento; o `scdet` do ffmpeg só pega a costura com mudança de cena (score 9 vs limiar 10). Medir a diferença média absoluta entre frames **só acima da faixa de legenda** acha todas.

## Receita
```bash
ffmpeg -hide_banner -v error -i original.mp4 -vf "crop=720:900:0:0,scale=180:225" -f rawvideo -pix_fmt gray top.raw
# numpy: d = |diff(frames)|.mean(); picos > ~4× a mediana = costura
```
- Cortar a faixa da legenda fora (no caso, y > 900 de 1280) — senão cada troca de legenda vira "corte".
- Conferir cada pico olhando frame antes/depois (pose/mão muda, enquadramento não).

## Caso ([[criativo-sarah-flores-2284342465689308]])
Mediana 1,6. Doze picos de 7,0 a 27,9: dois com troca de objeto (7,133 carta → embaralhar; 23,567 → 3 cartas na mesa) e dez só de pose, quase todos no início de frase. O `scdet` com limiar 8 achou só 23,567. Na costura de 7,13 s o áudio cai a −64,7 dB (silêncio digital) — outro sinal de emenda.

## Pra que serve
- Pontos de corte "de graça" pro [[mapa-de-recortes-reaproveitaveis]]: cortar na costura não cria jump cut novo.
- Ritmo de corte do original (aqui 1,5 corte / 10 s) pra replicar.

## Conecta com
- [[medir-fronteira-de-bloco-em-video]] — o método geral de fronteira; esta é a variante pra corte seco no mesmo plano
- [[costura-de-clipes-por-tarja-persistente]] — outra forma de esconder emenda
- [[pruna-troca-de-pessoa-no-meio-do-clipe]] — por que clipes curtos de IA são o padrão
