# As 8 regras (cada uma custou dinheiro ou uma peça reprovada)

## 1. Reconstruir, não recortar
Camada queimada no original (legenda, card, faixa, CTA) se **redesenha** — ou se recorta **justo na borda do elemento**, quando ele é sólido e está sobre fundo liso. Recortar um retângulo "com fundo" traz pedaço do rosto antigo, emenda visível e zoom trocado. Um lote inteiro (3 peças) foi reprovado por isso em 16/09: *"ficou horrível, tudo errado a edição"*.

## 2. Medir, nunca chutar
Fronteira de bloco, bbox de painel, cor, altura de capital, nível de áudio: tudo sai de análise de frame (ffmpeg + PIL/numpy), não do olho. Exemplos do que a gente mede em toda peça: onde a faixa começa e termina em px, em que frame o painel entra, qual a largura de uma palavra do karaokê, qual o mean_volume da fala e da música.

## 3. O rosto manda no recorte
Quando o avatar novo entra numa janela, o recorte é **centrado no rosto detectado** (YuNet/OpenCV, `scripts/checar-identidade.py` tem o código), nunca um recorte fixo. Recorte fixo calibrado em outro avatar corta a cabeça — foi o motivo de 10 peças serem refeitas em 21/09.

## 4. O frame 0 do lipsync é a imagem, não o vídeo
O Pruna devolve a imagem-base parada no primeiro frame (enquadramento diferente do resto). **Pule o frame 0** na montagem (`trim=start_frame=1`).

## 5. Travar a identidade no prompt do lipsync
Em ~15 % dos clipes o Pruna **troca de pessoa** depois do frame 0 (outro cabelo, outra roupa, tira o hijab, aproxima a câmera). O prompt que resolve descreve a pessoa e trava: *"The woman in the image — <descrição> — stays EXACTLY the same person from the first frame to the last: same face, same hair, same clothes, same framing and distance from the camera."* E nunca peça pose diferente da imagem ("talks straight to the camera" com imagem em 3/4 faz o modelo reimaginar a cena).

## 6. Pose em positivo, sem citar o objeto proibido
Mão na lente e celular em quadro se resolvem **descrevendo a pose que se quer**, não proibindo: *"Both of his arms hang relaxed at his sides, completely out of frame, for the whole clip, and nothing is held in front of him or shown to the camera."* Citar "phone … out of frame" faz o modelo mostrar o celular.

## 7. Conferir o clipe inteiro, não o primeiro frame
Toda geração de vídeo passa por uma **folha de frames do clipe inteiro** (16–24 quadros) antes de montar. Defeitos (mão na lente, segunda pessoa, troca de identidade, glitch de fundo) aparecem a partir do segundo 2, nunca no frame 0.

## 8. Validar o download
A CLI da WaveSpeed grava arquivo pela metade quando a rede oscila, **sem dar erro** (um clipe de 11 MB vira 270 KB e o ffprobe ainda mostra a duração certa). Depois de todo lote: `ffmpeg -v error -i clipe -f null -` (stderr vazio = íntegro) e, se falhar, rebaixe com `scripts/rebaixar.py` a partir da URL que fica no `.out.json`. Upload também falha: use retry de 5 tentativas.

---

### Regras de conteúdo (protegem a conta)
- **Promessa pesada só na imagem.** A fala nunca diz hack, senha, invadir, espionar. Quem promete é o painel do funil na tela.
- **Avatar segue o gênero da voz.** Voz feminina → rosto feminino. Trocar isso já queimou US$ 4,66 num lote.
- **PII fora.** Telefone, e-mail e nome real que aparecem em gravação de funil: desfocar ou não usar.
- **Karaokê é pré-requisito** no WhatsApp (o #1 do swipe usa), e o gancho escrito pesa mais que o roteiro falado (mesma copy, cascas diferentes: US$ 4.074 × US$ 0,63 de gasto).
