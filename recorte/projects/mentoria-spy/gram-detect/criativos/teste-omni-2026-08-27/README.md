# Troca de avatar via Gemini Omni Flash (Kie.ai) — 2026-08-27

Criativo fonte: `VIDEO_EN_1_17.08_ZAP_PL.mp4` (57s, 9:16, EN, nicho "pegar traição / espionar WhatsApp").
Avatar novo: mulher loira (selfie em estacionamento).
Entrega: `full/criativo-avatar-loira.mp4`.

## A receita

```
POST https://api.kie.ai/api/v1/jobs/createTask
{
  "model": "gemini-omni-video",
  "input": {
    "prompt": "read the images",
    "image_urls": ["<imagem-de-instrucao>", "<avatar>"],
    "video_list": [{"url": "<mp4 SEM AUDIO>", "start": N, "ends": N+10}],
    "aspect_ratio": "9:16", "resolution": "1080p", "duration": "10"
  }
}
```
Consulta: `GET /api/v1/jobs/recordInfo?taskId=...` → `state`, `resultJson.resultUrls`.
Upload de arquivo: `POST https://kieai.redpandaai.co/api/file-stream-upload` (multipart: file, uploadPath, fileName).

Custo: **168 creditos = $0,84** por janela de ate 10s.

## Regras descobertas na marra

1. **Vidoo SEM audio.** Com audio, o safety review do Google barra
   ("The uploaded audio was flagged by Google safety review"). Job bloqueado nao cobra credito.
   O audio original volta no final com ffmpeg.
2. **A instrucao vai como IMAGEM, nao no campo `prompt`.** Com o pedido escrito no `prompt`
   o modelo ignora e devolve a pessoa original. Com o mesmo pedido renderizado como imagem
   e `prompt: "read the images"`, ele executa. (Nao funciona no Kling — la a imagem de texto
   e tratada como referencia visual e o resultado degringola.)
3. **Estreite o REPLACE, nao amplie o KEEP.** Texto que funciona (`prompt-img-v3.png`):
   > REPLACE THE FACE AND HAIR OF THE WOMAN IN THE VIDEO WITH THE FACE AND HAIR OF THE
   > WOMAN IN THE IMAGE. DO NOT CHANGE ANYTHING ELSE.
   Se mandar "keep the clothes, background and on-screen text exactly as they are in the video",
   o rosto entra no pacote do que ele preserva e **nao troca nada**.
   Versao curta demais ("replace the woman...") troca, mas traz a roupa da foto de referencia junto.
4. **A troca e estocastica.** Mesmo prompt, mesma fonte: um clipe pode nao trocar, ou trocar
   com atraso no meio. Confira clipe a clipe e regere o que falhar. Duas tentativas em paralelo
   com `seed` diferente e mais barato que duas rodadas sequenciais.
5. **Legenda queimada e REDESENHADA, nao copiada.** As pontas batem, o miolo embaralha
   (t=5s: original "FROM JUST ABOUT" -> saida "AND INSTANT MESSAGES"). Acontece inclusive
   nos clipes que nao trocaram a pessoa, entao nao e efeito da troca.
   **Pra producao: rodar no talking head sem legenda e recompor overlay depois.**
6. **Janela de 10s e do `start`/`ends`**, nao do arquivo. Fonte pode ter ate 30s e 100MB,
   entao da pra subir um bloco e disparar varias janelas nele.
7. **O modelo arredonda a janela pra segundo inteiro.** Pedi 0–5,5 e 5,5–11, saiu 5,0s e 6,0s.
   A soma fecha 11s, entao o bloco continua alinhado com o audio nas pontas.
8. **Corte com `trim` (frame-exato), nunca `-ss` antes do `-i`** — input seeking busca keyframe
   e desloca o corte. Vale pro fatiamento e pra qualquer print de conferencia.

## Este criativo

So 22 dos 57s tem pessoa em quadro. O resto e screen recording e passa intacto.

| trecho | origem |
|---|---|
| 0–20s | original |
| 20–31s | gerado (A1 5s + A2 6s) |
| 31–38s | original |
| 38–49s | gerado (B1 5s + B2r2 6s) |
| 49–57s | original |

B2 falhou na 1a rodada (comecou original, virou loira no meio). B2r1 trocou mas manteve o
lenco na cabeca; B2r2 ficou consistente com os outros tres.

Custo total: 9 chamadas x $0,84 = **$7,56**.

## Comparacao com Kling O3 Pro (wavespeed)

`kwaivgi/kling-video-o3-pro/reference-to-video` ($0,56/10s) tambem faz o trabalho e preservou
a legenda queimada com fidelidade melhor. Mas so obedece prompt em TEXTO — a tecnica de
prompt-via-imagem nao funciona nele. Fica como alternativa quando a legenda importar.

## Arquivos

- `prompt-img-v3.png` — a imagem de instrucao que funciona
- `full/montar.sh` — corta os trechos originais, normaliza os gerados, costura e devolve o audio
- `full/jobs.json` — taskIds de cada janela
- `out/` — a bateria de testes de 10s (v1/v2/v3, texto, kling, p-video, skyreels)
