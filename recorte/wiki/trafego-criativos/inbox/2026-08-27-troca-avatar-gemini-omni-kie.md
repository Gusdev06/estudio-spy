# Troca de avatar em criativo via Gemini Omni Flash (Kie.ai) — 2026-08-27

Fonte completa: `projects/gram-detect/criativos/teste-omni-2026-08-27/README.md`

Técnica nova pra recriar criativo campeão com outro rosto, mantendo cenário, roupa e áudio.
Testada de ponta a ponta num criativo de 57s do nicho "pegar traição".

## O que ficou provado

- **WaveSpeed não serve pra isso**: o `google/gemini-omni-flash/reference-to-video` de lá aceita
  só imagens, não vídeo. O que aceita vídeo+imagens+prompt lá é o Kling O3.
  Quem tem o modo "reference video" do Omni de verdade é o **Kie.ai** (`gemini-omni-video`,
  campo `video_list` com `start`/`ends`).
- **Prompt entregue como IMAGEM bate prompt em texto** — no Gemini. Com o pedido no campo
  `prompt` o modelo ignora e devolve a pessoa original; renderizado como imagem + `"read the images"`,
  executa. No Kling é o contrário: imagem de texto vira referência visual e estraga o resultado.
- **Estreitar o replace, não ampliar o keep.** "Replace the face and hair… do not change anything
  else" funciona. "Keep everything exactly as in the video" faz ele preservar o rosto também.
- **Vídeo tem que ir sem áudio** — o safety do Google barra áudio de nicho agressivo.
- **Legenda queimada é redesenhada e embaralha no miolo.** Rodar em talking head limpo e
  recompor overlay depois.
- **A troca é estocástica**: confira clipe a clipe, regere o que falhar.

Custo: $0,84 por janela de 10s (Kie). Kling O3 Pro sai $0,56 e preserva legenda melhor,
mas só obedece texto.

Relacionado: [[trocar-avatar]] · [[clonar-edicao]]
