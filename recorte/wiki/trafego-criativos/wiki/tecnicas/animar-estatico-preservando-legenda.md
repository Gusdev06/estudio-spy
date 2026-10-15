---
tipo: tecnica
tags: [video, i2v, ltx, wavespeed, legenda, esteira, custo]
fontes: [[fonte-teste-video-ltx-fr-2026-08-22]]
---

# Animar estático preservando a legenda

Dá pra transformar criativo estático em vídeo **sem destruir o overlay de texto**. Testado em
22/08 com `wavespeed-ai/ltx-2.3/image-to-video`: **3 de 3 mantiveram a legenda** nítida,
legível e inalterada do frame 0 ao 4,8s — incluindo selo colorido com texto dentro.

## Por que importa

O medo padrão de animar criativo de esteira é o modelo derreter o texto (letra troca, borra,
o selo entorta). Não aconteceu. O overlay se comporta como camada travada: não escala junto
com a cena, não sofre o push-in da câmera.

## Receita

Modelo `wavespeed-ai/ltx-2.3/image-to-video`, 720p, 5s. Prompt que funcionou:

> Locked-off static camera, no zoom, no pan, no cuts. The woman holds the same pose and only
> breathes softly, with one subtle blink and a micro head movement; her hair moves slightly.
> Everything else stays identical to the source image. **The white text and the orange banner
> overlay must remain perfectly static, sharp, legible and completely unchanged, frozen exactly
> as in the source frame.** Photorealistic amateur phone photo look, same natural lighting, no
> style change, no added text, no captions.

Pós-processamento obrigatório (saída vem 832×1024 = 0,8125, não 4:5):

```bash
ffmpeg -i in.mp4 -vf "crop=819:1024,scale=1080:1350:flags=lanczos" -an -c:v libx264 -crf 20 out.mp4
```

## Custo

**$0,10 por vídeo.** Uma esteira de 70 sai **~$7 (~R$38)** — menos de 1% de um dia de budget
da BIDCAP FR. Custo **não é** barreira aqui. Alternativa mais barata: `lightricks/ltx-2-fast`
a $0,04.

## Armadilhas

- **O modelo dá push-in mesmo com "no zoom" no prompt.** Elemento perto da borda sai do quadro
  (num teste os pés da modelo sumiram). Conferir sempre o **último** frame, não o primeiro.
- Sai com faixa de áudio, mas em silêncio digital (−90 dB). Remover com `-an`.
- Leve deriva de identidade do rosto ao longo dos 5s.

## Subida no Meta (o que a API exige)

- `bulk_upload_ad_videos` puxa por **URL pública** — mesma rota de CDN das imagens.
- No criativo, **não** passe `image_hash` junto com `video_id`: a API recusa com
  *"Only one media source allowed"*. A Meta gera o thumbnail do 1º frame — que é justamente
  a arte estática original, então o resultado é o desejado de qualquer jeito.
- Converter pra 4:5 **antes** de subir (a saída do LTX é 832×1024).

## O que continua não respondido

Se vídeo converte mais que estático. Animar **não herda validação** —
ver [[arte-nova-nao-herda-validacao]]. Só o leilão responde, e com
[[piso-de-volume-antes-de-julgar-criativo]].

Relacionado: [[throughput-de-criativo]], [[legenda-em-lote-por-script]].
