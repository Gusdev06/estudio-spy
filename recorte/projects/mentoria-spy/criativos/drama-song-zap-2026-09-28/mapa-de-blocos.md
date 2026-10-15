# Mapa de blocos — durações reais (cancao-v1.mp3, 3:45,2)

Gerado por `scripts/mapa.py` a partir de `mapa-de-tempo.json`. O plano da Isca (`roteiros/2026-09-28-drama-song-zap/plano-de-cenas.md`) não foi editado; aqui só entram as durações medidas.

Regra: cada bloco vai do início da 1ª linha dele até o início da 1ª linha do bloco seguinte. O instrumental entre linhas entra no bloco anterior, e com isso a linha do tempo fica coberta de 0 a 225,2 s sem buraco. B01 começa em 0 (intro instrumental de 0,74 s). B25 vai até o fim do arquivo (219,7 → 225,2 s é cauda instrumental, boa pro end card).

| Bloco | Início | Fim | Duração real | Estimativa da Isca | Δ | Voz (1ª→última palavra) | Clipes Seedance |
|---|---|---|---|---|---|---|---|
| B01 | 0.00 | 7.18 | **7.18 s** | ~6 s | +1.2 | 0.74→3.32 | 1 |
| B02 | 7.18 | 14.72 | **7.54 s** | ~7 s | +0.5 | 7.18→14.14 | 1 |
| B03 | 14.72 | 22.22 | **7.50 s** | ~7 s | +0.5 | 14.72→20.50 | 1 |
| B04 | 22.22 | 27.92 | **5.70 s** | ~7 s | -1.3 | 22.22→27.88 | 1 |
| B05 ⭐ | 27.92 | 34.82 | **6.90 s** | ~7 s | -0.1 | 27.92→33.88 | 1 |
| B06 | 34.82 | 53.94 | **19.12 s** | ~13 s | +6.1 | 34.82→51.52 | 2 (>15 s) |
| B07 | 53.94 | 62.60 | **8.66 s** | ~7 s | +1.7 | 53.94→60.26 | 1 |
| B08 | 62.60 | 71.08 | **8.48 s** | ~7 s | +1.5 | 62.60→68.70 | 1 |
| B09 | 71.08 | 83.92 | **12.84 s** | ~13 s | -0.2 | 71.08→82.58 | 1 |
| B10 | 83.92 | 103.24 | **19.32 s** | ~13 s | +6.3 | 83.92→100.72 | 2 (>15 s) |
| B11 | 103.24 | 108.72 | **5.48 s** | ~8 s | -2.5 | 103.24→108.72 | 1 |
| B12 | 108.72 | 116.28 | **7.56 s** | ~8 s | -0.4 | 108.72→113.40 | 1 |
| B13 | 116.28 | 121.62 | **5.34 s** | ~7 s | -1.7 | 116.28→121.62 | 1 |
| B14 | 121.62 | 128.70 | **7.08 s** | ~7 s | +0.1 | 121.62→127.14 | 1 |
| B15 | 128.70 | 135.90 | **7.20 s** | ~7 s | +0.2 | 128.70→135.46 | 1 |
| B16 | 135.90 | 144.36 | **8.46 s** | ~7 s | +1.5 | 135.90→141.04 | 1 |
| B17 | 144.36 | 151.36 | **7.00 s** | ~7 s | +0.0 | 144.36→151.36 | 1 |
| B18 | 151.36 | 160.90 | **9.54 s** | ~8 s | +1.5 | 151.36→160.00 | 1 |
| B19 | 160.90 | 178.18 | **17.28 s** | ~13 s | +4.3 | 160.90→177.08 | 2 (>15 s) |
| B20 | 178.18 | 182.86 | **4.68 s** | ~7 s | -2.3 | 178.18→182.86 | 1 |
| B21 | 182.86 | 187.74 | **4.88 s** | ~7 s | -2.1 | 182.86→187.74 | 1 |
| B22 | 187.74 | 197.16 | **9.42 s** | ~8 s | +1.4 | 187.74→194.56 | 1 |
| B23 | 197.16 | 202.70 | **5.54 s** | ~7 s | -1.5 | 197.16→202.70 | 1 |
| B24 | 202.70 | 215.06 | **12.36 s** | ~9 s | +3.4 | 202.70→215.06 | 1 |
| B25 | 215.06 | 225.20 | **10.14 s** | ~5 s | +5.1 | 215.06→219.74 | 1 |

## O que mudou em relação à estimativa

- Total real 225,2 s (3:45), no teto da faixa prevista pela Isca (3:20–3:45).
- Os refrões cresceram: B06 19,1 s, B10 19,3 s, B19 17,3 s (estimados em 13 s). O minimax meteu instrumental depois de cada refrão. Cada um passa de 15 s, o limite do Seedance, e precisa de **2 clipes** ou de um bloco de respiro (R1–R3 do plano) no fim.
- Encolheram: B04 5,7 s, B11 5,5 s, B13 5,3 s, B20 4,7 s, B21 4,9 s, B23 5,5 s. B20 e B21 ficam perto do mínimo de 4 s do Seedance; com o ~1 s de grade a descartar (ver README), gerar 6 s e aparar.
- B24 (12,4 s) e B25 (10,1 s) ficaram maiores: o outro falado tem pausas. B25 inclui 5,5 s de cauda instrumental, que vira o end card.
- Não há buraco instrumental longo no meio (silencedetect a −35 dB/1,5 s não achou nenhum). Os blocos de respiro R1–R3 só entram se a edição quiser dividir os refrões longos.

## Linhas que o Whisper ouviu diferente (a letra manda, mas vale ouvir)

| Linha | Letra | Whisper ouviu | Risco |
|---|---|---|---|
| 7 (25.8 s) | The whole room froze. And then he laughed. | The whole room frozen, then he laughed. | provável erro de transcrição |
| 11 (38.8 s) | I blamed my heart, I blamed my mind | I blame my heart, I blame my mind | blame/blamed: comum em canto |
| 12 (43.7 s) | Every night that screen would glow | Every night that scream would glow | scream/screen: erro de transcrição (no 2º refrão ouviu certo) |
| 16 (62.6 s) | I asked a counselor what was true | I asked her counseling what was true | **ouvir**: a cantora pode ter cantado 'counseling' |
| 18 (71.1 s) | So I stopped asking. Stopped the fights. | So I stopped asking, stopped the | 'fights' sumiu no Whisper |
| 27 (107.0 s) | She'd lived this once. She held me tight. | lived this one, she held me tight | **ouvir**: 'She'd lived this once' pode ter saído 'lived this one' |
| 33 (123.7 s) | Not a stranger. Jess. The friend I knew. | Not a stranger, just a friend I knew | **ouvir, é crítico**: 'Jess' virou 'just'. Se a cantora engoliu o nome, a revelação da trama (a amiga é a outra) não fica clara no áudio |
| 47 (180.4 s) | Same candles, same smile on every face | Same candle, same smile on every face | candle/candles: menor |
| 54 (202.7 s) | This app shows you the conversations. | This app shows you the conversation's | 'conversations. Clear.' virou "conversation's clear": a pausa entre as frases pode ter sumido |

Alucinação do Whisper descartada: "Thank you." em 224,56 s (cauda instrumental).
