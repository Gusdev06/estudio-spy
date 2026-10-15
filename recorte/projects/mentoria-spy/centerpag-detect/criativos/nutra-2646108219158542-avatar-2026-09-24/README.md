# Nutra Health 2646108219158542 — uma variação de avatar

Pedido em 24/09/2026: uma variação, mesma edição e hook, só outro avatar.

**Estado: entregue em 24/09/2026 após aprovação “OK” do avatar com camiseta verde-escura e do custo. Uma geração, cobrança real US$ 0,90.**

Vídeo final: `nutra-2646108219158542-variacao-avatar.mp4` (4min31s, 360×640, 30fps, 9,04 MB). Master sem perdas: `master-sem-perdas.mp4`.

## Referência e escopo

- Fonte: https://www.facebook.com/ads/library/?id=2646108219158542 — versão 1 de 2 do catálogo.
- Original: `../../../downloads/ad-2646108219158542-2026-09-24/nutra-health-2646108219158542-v1.mp4`.
- Original: 360×640, 30 fps, 8.141 frames, 271,371 s com áudio AAC.
- Hook preservado nos frames 0–219; frame 220 é preto na transição.
- Avatar: frames 220–1289, 7,333333–43 s, 1.070 frames / 35,666667 s.
- Contagem regressiva e cauda: preservar a partir do frame 1290 (43 s).
- Áudio final: copiar a faixa original sem regravar, cortar pausas ou mudar velocidade.
- Uma única entrega com voz original. Não produzir a versão de voz nova da skill: isso contrariaria o pedido.

## Imagem e prévia

`avatar-base.png`: imagem gerada com a ferramenta nativa de imagem do Codex, editando o frame original. Homem fictício de aproximadamente 42 anos, pele morena, cabelo curto ondulado, barba curta e óculos. Preservados suéter azul-marinho, gola clara, microfone, cadeira e ambiente iluminado em roxo. Imagem sem textos, para composição posterior.

Prévia lado a lado: `preparo/comparacao-360.jpg` (frame 360, 12s). Demais comparações cobrem entrada e diferentes legendas. Ainda são imagens estáticas, não lipsync.

`preparar.py` extrai a arte opaca das caixas de texto em cada frame, com alfa transparente fora das caixas; não cola faixas de fundo ou rosto do original. A camada é `preparo/legendas-alpha.mov`; geometria/tempos em `preparo/timeline.json`. Foram encontradas legendas inferiores em 1.047 dos 1.070 frames, a verificar novamente no vídeo final. A entrada tem fade de 7 frames medido pelo branco do título.

## Planejamento da geração — registro anterior à aprovação

- Modelo consultado ao vivo: `pruna-ai/p-video/avatar`, WaveSpeed, resolução 720p.
- Áudio de entrada preparado: `preparo/audio-avatar.wav`, 35,666667 s, mono/44,1 kHz.
- Preço consultado em 24/09: US$ 0,025 por segundo, arredondando a duração para cima. 36 × 0,025 = **US$ 0,90** por chamada, sem regerações incluídas.
- Fonte de preço: https://wavespeed.ai/models/pruna-ai/p-video/avatar . Cobrança final do job prevalece.
- Nenhum job de vídeo pago foi disparado nesta preparação. Imagem feita pela ferramenta nativa do Codex, sem cobrança WaveSpeed atribuída.
- Prompt de movimento proposto: `One man speaks directly to the camera in a continuous fixed medium close-up. Natural lip movements driven by the supplied audio, subtle blinks and small head movements. Same glasses, clothes, microphone and room. Both arms stay relaxed below the frame. Stable framing, no camera motion. Exactly one person throughout.`
- Após aprovação, gerar `avatar-animado.mp4`, inspecionar identidade/mãos/boca, executar `montar.py` e validar os cortes, a duração, o áudio e as legendas.

## Limitações identificadas na preparação

A referência disponível é 360×640; o resultado planejado mantém essa resolução. A geração muda a atuação dentro do trecho de avatar. Partículas/grão sobrepostos ao rosto no original ainda não foram reconstruídos como camada separada; não declarar a edição inteira pixel a pixel. Hook, cauda e áudio devem ser verificados por comparação após renderizar.

## Revisão de figurino — 24/09/2026 (histórico)

Gusta pediu “muda a roupa dele”. `avatar-base.png` agora tem camiseta lisa verde-escura, gola redonda. Mesmo avatar, cenário, óculos e microfone. Gerada pela ferramenta nativa de imagem do Codex; prompt em `prompt-troca-roupa.txt`. Base anterior preservada em `avatar-base-v1-sueter.png`; prévias refeitas com o novo figurino. Aprovação da imagem final e gasto de US$ 0,90 continuam pendentes; pedido de troca de roupa não foi tratado como aprovação do gasto.

## Entrega e validações — 24/09/2026

- Aprovação explícita: “OK” após a prévia com camiseta verde-escura e a pergunta sobre US$ 0,90.
- Job: `fde1b08e0fb54de3b41c818a791fc559`, `pruna-ai/p-video/avatar`, uma chamada; geração concluída em aproximadamente 289s. Resultado bruto em `video-result.json`.
- Cobrança real: **US$ 0,90**, registro de billing do próprio job e chave `macbook`, em `custo.json`. Nenhuma regeração.
- Avatar gerado: 704×1280, 24fps, 36,042s. Montagem usa os primeiros 35,667s, converte para 30fps e para os 360×640 do original.
- Arquivo entregue: H.264 High, yuv420p, CRF 16, faststart, 9.044.521 bytes; duração 271,370s, 8.141 frames. O milissegundo de diferença do contêiner original não altera a duração das faixas.
- **Áudio AAC idêntico ao original por SHA-256**, inclusive no arquivo de entrega.
- **Hook (frames 0–219) e cauda (1290–8140) pixel a pixel idênticos no master sem perdas**, verificados com hash de cada frame. A cópia compacta de entrega sofre apenas a recompressão de vídeo.
- Legendas isoladas como caixas opacas, sem recortes de fundo; conferidas em 10/12/15/20/30/40s e nas lacunas. Conteúdo, posição e tempos mantidos.
- Recuperadas partículas claras sobre roupa e bordas como camada de luminosidade com alfa. A região do rosto foi excluída dessa extração para não carregar brilhos/traços do rosto antigo. Portanto, não se afirma que o grão/partículas sobre o rosto sejam idênticos.
- Inspeção visual amostral: 12 frames do avatar e 16 da montagem. Identidade, óculos e figurino consistentes; gestos ocasionais nas bordas inferiores, sem oclusão do rosto. A atuação é nova, conduzida pelo áudio original.
- Evidências: `conferencia/validacao-master.json`, `conferencia/validacao-entrega.json`, `conferencia/contato-final.jpg` e `conferencia/comparacao-legendas.jpg`.
- Sem publicação em campanha e sem métricas de performance verificadas.

O pedido inicial era só trocar o avatar; a troca de roupa foi acrescentada explicitamente pelo Gusta e aprovada na prévia. Resultado testa rosto + figurino, não apenas rosto.
