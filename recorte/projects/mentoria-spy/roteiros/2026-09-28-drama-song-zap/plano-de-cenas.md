# Plano de cenas — drama-song Spy Zap (28/09/2026)

Letra: `letra.txt`, com **~2.373 bytes** (85 linhas, só ASCII, contando as quebras). Contei à mão: a Isca não tinha shell nesta sessão. **Confirmar com `wc -c letra.txt` antes de mandar pro minimax**; o teto é 3000 e a meta desta entrega era ≤ 2.900. `estilo-musical.txt` tem ~251 caracteres (teto de 300). Personagens: `personagens.md` (copiar o bloco DESCRIÇÃO literal em cada shot sheet).

## Como o tempo foi estimado

Estes tempos são **estimativa**. O mapa real sai do Whisper com timestamps por palavra, conferido contra a letra, porque o Whisper erra palavra cantada.

- 110 BPM dá 0,545 s por batida e 2,18 s por compasso.
- Linha cantada de ~8–11 sílabas ≈ 1,5 compasso ≈ **3,3 s**, respiração incluída.
- Linha falada ≈ 3,5 sílabas/s + pausa ≈ **3–4 s**.
- Somando os blocos dá ~3:20. O minimax deve inserir intro e interlúdios instrumentais, então o total real deve ficar entre 3:20 e 3:45. Onde houver instrumental sem voz, estique o bloco vizinho ou use um bloco de respiro (ver o fim do arquivo).

## Molde do shot sheet (1 imagem 2x2 = 1 bloco)

```
A 2x2 grid storyboard in a single image, four sequential moments of the same continuous shot, read left-to-right, top-to-bottom. Thin white gutters between panels. No text, no captions, no panel numbers.
Setting (same in all four panels): {CENÁRIO}.
Characters: {DESCRIÇÃO literal de cada personagem presente}.
Panel 1: {…} Panel 2: {…} Panel 3: {…} Panel 4: {…}
3D animated feature film style, cinematic lighting, shallow depth of field, consistent characters, outfits and lighting across panels, vertical 9:16 framing inside each panel.
```

Pro Seedance: "Animate as one continuous shot moving through the four moments in order. The grid, gutters and panel borders must NOT appear in the video, full-frame 9:16 only. No text, no subtitles, no speech, no lip movement unless stated." Os clipes saem mudos: a música é o único áudio.

**Telas de celular:** nunca pedir interface legível, logo de app ou nome de app. Mostrar só o brilho da tela no rosto ou balões de conversa desfocados sem texto. Diffusion inventa interface, e UI do WhatsApp em anúncio já é problema de política. Os cards de funil entram na edição, se entrarem.

---

## Blocos

### B01. Intro falada (~6 s)
> I was the last one at that table to know...

**Cenário:** sala de jantar de casa de subúrbio americano à noite, mesa longa de madeira, velas, luz âmbar, janela escura ao fundo. Maya ANTES sentada, os outros convidados fora de foco.
1. Close frontal da Maya, olhar perdido, velas bokeh em primeiro plano.
2. Rack focus: o fundo desfocado revela gente rindo à mesa.
3. Maya abaixa os olhos para o prato intacto.
4. Câmera recua devagar e isola Maya no centro de uma mesa cheia.

### B02. V1, linhas 1–2 (~7 s)
> Sunday dinner at his mother's place / Candles lit, a smile on every face

**Cenário:** a mesma sala de jantar (fixa pra B02–B05). Mesa posta, travessa de assado, velas, Linda na cabeceira, Ryan ao lado da Maya, Jess do outro lado da mesa.
1. Plano geral de cima (plongée) da mesa inteira, travessas passando de mão em mão.
2. Linda erguendo a taça, sorrindo.
3. Jess rindo, jogando o cabelo ruivo pra trás.
4. Maya sorrindo por educação, sorriso que não chega aos olhos.

### B03. V1, linhas 3–4 (~7 s)
> His phone lit up beside his plate / He turned it over. "Babe, it's late."

**Cenário:** mesmo da B02, câmera à altura da mesa.
1. Detalhe: celular ao lado do prato do Ryan acende, brilho sem texto legível, relógio prateado no pulso ao lado.
2. A mão do Ryan vira o celular com a tela pra baixo, rápido.
3. Plano médio do Ryan, meio sorriso, olhando a Maya de lado.
4. Contraplano: Maya olhando o celular virado, testa franzida.

### B04. Pré-refrão, linhas 1–2 (~7 s)
> I asked him softly, "Who was that?" / The whole room froze. And then he laughed.

**Cenário:** mesmo da B02.
1. Maya se inclina e fala baixo com o Ryan (boca fechada no quadro: sem lipsync).
2. Plano geral: todos à mesa param, garfos no ar.
3. Close do Ryan jogando a cabeça pra trás numa gargalhada.
4. Linda e os convidados começam a rir junto, desconfortáveis.

### B05. ⭐ CENA SONDA: pré-refrão, linhas 3–4, a humilhação (~7 s)
> He slid his phone to me: "Go on, check. / She's jealous again," he told the rest.

**Por que é a sonda:** duas personagens principais (Maya ANTES e Ryan) no mesmo quadro, com interação física (o celular passando de mão), no cenário que volta na vindicação (B20–B22). Se rosto, roupa e traços marcantes (pinta e argolas da Maya, relógio e meio sorriso do Ryan) se mantêm nos 4 quadros e no clipe animado, o visual do filme inteiro está validado. Não depende de tela legível.

**Cenário:** mesma sala de jantar à noite, mesa longa de madeira, velas, luz âmbar. Maya ANTES e Ryan lado a lado em primeiro plano; Linda e Jess desfocadas ao fundo.
1. Plano médio a dois: Ryan desliza o celular pela toalha até a frente da Maya, meio sorriso.
2. Close da mão da Maya parada acima do celular, sem tocar.
3. Ryan se vira pra mesa, abre os braços e fala pros outros; Maya em primeiro plano, desfocada.
4. Close da Maya, olhos marejados, sorriso forçado; atrás, Ryan e a mesa rindo.

### B06. Refrão 1 (~13 s)
> So I swallowed it, I said I'm fine / I blamed my heart, I blamed my mind / Every night that screen would glow / And I was the last to know

**Cenário:** banheiro da casa da sogra, azulejo verde antigo, luz fria de teto, espelho.
1. Maya fecha a porta e encosta nela, olhos fechados.
2. Maya se olha no espelho e ajeita o cabelo: "I'm fine".
3. Close do reflexo: o sorriso some.
4. Maya apaga a luz; fica só o contorno dela no escuro.

### B07. V2, linhas 1–2 (~7 s)
> I called my best friend Jess at two / She said, "Girl, he'd never hurt you."

**Cenário:** tela dividida só no sentido da montagem. Dois cenários no mesmo sheet, alternados: quarto escuro da Maya (Ryan dormindo de costas) e quarto da Jess (abajur rosa).
1. Maya sentada na beira da cama, celular no ouvido, luz fria da janela.
2. Jess na cama, celular no ouvido, cara de preocupada e sorriso doce.
3. Detalhe do criado-mudo da Jess: **um relógio prateado grande igual ao do Ryan** (pista; não dar zoom demais).
4. Maya concorda com a cabeça, aliviada, abraçando os joelhos.

### B08. V2, linhas 3–4 (~7 s)
> I asked a counselor what was true / She said, "No proof? There's nothing to do."

**Cenário:** consultório pequeno, poltrona, estante, planta, luz de fim de tarde. A conselheira é figurante (mulher de 50 e poucos anos, cabelo grisalho preso, cardigã mostarda) e não precisa de ficha.
1. Maya na poltrona, falando e gesticulando, aflita.
2. Conselheira de pernas cruzadas, prancheta, expressão neutra.
3. A conselheira dá de ombros com as mãos abertas.
4. Maya afunda na poltrona, olhando o chão.

### B09. V3, fundo do poço (~13 s)
> So I stopped asking. Stopped the fights. / Stared at the ceiling every night. / He came home later every week. / I got so quiet I could barely speak.

**Cenário:** quarto do casal à noite, luz azulada da janela, relógio digital no criado-mudo.
1. De cima: Maya deitada de olhos abertos olhando o teto, lado do Ryan vazio.
2. Detalhe do relógio digital, sem número legível, só o brilho vermelho.
3. Porta abre, Ryan entra de sapato na mão com o celular iluminando o rosto; Maya finge dormir.
4. Maya encolhida de lado, pequena no meio da cama grande.

### B10. Refrão 2 (~13 s)
> (refrão repetido)

**Cenário:** cozinha da Maya de manhã cinzenta, chuva na janela.
1. Maya de cardigã cinza segura uma caneca que já esfriou, olhando a chuva.
2. Ryan passa atrás dela digitando no celular, beija o ar perto da cabeça dela e sai.
3. A porta da frente bate; a caneca treme na mão dela.
4. Plano geral: Maya sozinha na cozinha, gotas escorrendo no vidro.

### B11. Ponte falada, linhas 1–2 (~8 s)
> Then my sister Nora came by one night. / She'd lived this once. She held me tight.

**Cenário:** mesma cozinha à noite, luz quente de pendente, dois chás na bancada.
1. Porta abre: Nora entra com duas canecas e a mecha grisalha iluminada pela luz do corredor.
2. Nora encosta as canecas na bancada e olha a Maya.
3. Maya desmorona; Nora a abraça de lado, firme.
4. Close das duas, testa com testa, Nora de olhos fechados.

### B12. Ponte falada, linhas 3–4 (~8 s)
> "You're not crazy. You just can't see. / There's a way to look. Sit here with me."

**Cenário:** mesma cozinha, as duas sentadas à mesa pequena.
1. Nora segura as duas mãos da Maya por cima da mesa.
2. Close da Nora, olhar calmo e firme.
3. Nora puxa a cadeira pra perto e dá tapinhas no assento ao lado.
4. Maya hesita e senta ao lado da irmã.

### B13. V4, linhas 1–2 (~7 s)
> On the phone he'd told me I could check / She showed me how. I held my breath.

**Cenário:** mesma cozinha, as duas lado a lado, luz vindo só do celular.
1. Detalhe: o celular do Ryan (capa azul-marinho) na mesa entre as duas.
2. Nora aponta a tela e explica; Maya olha de lado.
3. Close da Maya prendendo a respiração, luz da tela no rosto.
4. Close da mão da Maya tocando a tela.

### B14. V4, linhas 3–4, a descoberta (~7 s)
> The conversations, all in view. / Not a stranger. Jess. The friend I knew.

**Cenário:** o mesmo da B13. Alternativa de sonda se a B05 falhar por motivo de cena, e não de personagem.
1. Tela fora de foco em primeiro plano com balões de conversa sem texto; o rosto da Maya nítido atrás.
2. Os olhos da Maya se arregalam.
3. Maya tapa a boca com a mão; Nora põe a mão no ombro dela.
4. Inserção de memória: a Jess no jantar da B02 rindo, em tom sépia.

### B15. Pré-refrão 2, a dúvida (~7 s)
> My hands were shaking. What if I'm wrong? / What if the crazy one was me all along?

**Cenário:** banheiro da casa da Maya, espelho, luz fria.
1. Close das mãos da Maya tremendo na borda da pia.
2. Maya se olha no espelho.
3. O reflexo fica levemente desfocado e duplicado (dúvida).
4. Maya fecha os olhos e respira fundo.

### B16. Pré-refrão 2, a virada (~7 s)
> But the truth was right there in my hand / And for the first time, I could stand.

**Cenário:** mesmo banheiro.
1. Maya abre os olhos, e o reflexo volta nítido.
2. Ela solta o coque; o cabelo cai nos ombros.
3. Ela endireita as costas.
4. Maya apaga a luz e sai; a porta deixa passar luz quente do corredor.

### B17. V5, semanas 1–2 (~7 s) — a Maya passa a ser a versão DEPOIS em transição
> Week one, I slept right through the night / Week two, Nora said, "Your eyes look bright."

**Cenário:** montagem no quarto de manhã e num café de bairro.
1. Maya dormindo tranquila com o sol entrando, cardigã cinza jogado na cadeira.
2. Maya abre as cortinas e a luz inunda o quarto.
3. No café, Nora aponta pro rosto da Maya e sorri.
4. Maya ri de verdade pela primeira vez, cabelo solto.

### B18. V5, semanas 3–4 (~8 s)
> Week three, I stopped asking. I just knew. / Week four, his mother asked, "What's new with you?"

**Cenário:** cozinha da Maya de dia e depois a porta da casa da Linda.
1. Ryan olha o celular na bancada; Maya passa por ele serena, sem olhar, de blusa verde.
2. Ryan estranha e observa a Maya de costas.
3. Na porta da casa da Linda, a sogra abre e vê a Maya DEPOIS.
4. Linda inclina a cabeça, curiosa, e segura a mão da nora.

### B19. Refrão final (~13 s)
> No more swallowing, no more "I'm fine" / It was never my heart, never my mind / Let that screen light up and glow / I won't be the last to know

**Cenário:** rua de subúrbio ao entardecer, luz dourada, árvores.
1. Maya DEPOIS caminha na direção da câmera, passo firme, blusa esmeralda.
2. Travelling lateral acompanhando o passo, cabelo balançando.
3. Ela para na calçada em frente à casa da sogra, janela iluminada com a mesa posta.
4. Close: Maya respira fundo e sorri com o canto da boca.

### B20. V6, linhas 1–2 (~7 s)
> Sunday dinner at his mother's place / Same candles, same smile on every face

**Cenário:** **a mesma sala de jantar da B02–B05**, com o mesmo enquadramento em plongée da B02. Espelhamento proposital.
1. A mesma plongée da B02, com a Maya DEPOIS na mesma cadeira.
2. Linda erguendo a taça (espelho da B02).
3. Jess rindo, agora três cadeiras depois da Maya.
4. Maya sorri de verdade, calma.

### B21. V6, linhas 3–4 (~7 s)
> His phone lit up. He reached too late. / Jess was sitting three seats away.

**Cenário:** mesmo da B20, câmera à altura da mesa (espelho da B03).
1. Detalhe: o celular do Ryan acende ao lado do prato.
2. A mão do Ryan corre pra virar o celular, meio segundo atrasada.
3. Maya olha devagar pra Jess.
4. Close da Jess: o sorriso trava.

### B22. V6, linhas 5–6, a VINDICAÇÃO (~8 s)
> I smiled: "Go on. Turn it over, babe. / I already know." And the whole room froze.

**Cenário:** mesmo da B20, enquadramento espelhado da B05.
1. Plano médio a dois (espelho exato da B05 quadro 1): agora é a Maya que empurra o celular do Ryan de volta pra ele, sorrindo.
2. Close do Ryan: o meio sorriso some.
3. Plano geral: todos à mesa congelam, garfos no ar (espelho da B04 quadro 2).
4. Maya se levanta com calma, pega a bolsa e sai de cena; as velas tremulam.

### B23. Outro falado, linhas 1–2, pitch (~7 s)
> If your gut has been whispering for months... / You're not crazy. You deserve to know.

**Cenário:** varanda da casa da Maya à noite, luz quente, Maya DEPOIS sentada no degrau. Ela quebra a quarta parede.
1. Plano médio: Maya sentada no degrau, olhando a rua.
2. Ela vira e olha direto pra câmera.
3. Close frontal, olhar firme e acolhedor.
4. Leve aceno de cabeça, como quem diz "eu sei".

### B24. Outro falado, linhas 3–6 (~9 s)
> This app shows you the conversations. / Clear. In one place. / On a phone you're allowed to open. / No more guessing. No more fights.

**Cenário:** mesma varanda.
1. Maya segura o próprio celular virado pro corpo; só o brilho aparece.
2. Close do brilho da tela no rosto dela, calma.
3. Ela apoia o celular no joelho e olha pra câmera.
4. Ela sorri e se ajeita, relaxada.

Na edição, esse bloco é o lugar de um card do produto, se o Bisturi quiser. Esse card não pode ter UI de WhatsApp legível nem layout L5 (rejeitado pela Meta).

### B25. Outro, CTA (~5 s + end card)
> Tap the link. See the truth for yourself.

**Cenário:** mesma varanda.
1. Maya aponta pra baixo, pro link.
2. Close sorrindo.
3. Ela se levanta e entra em casa; a luz da porta a recorta.
4. Porta entreaberta com luz quente saindo, pra servir de fundo do end card com o CTA na edição.

---

## Blocos de respiro (instrumental sem voz, se o Whisper mostrar buracos)

- **R1:** mãos da Maya girando a aliança no dedo, sobre a toalha da mesa.
- **R2:** velas derretendo em time-lapse.
- **R3:** chuva na janela da cozinha.

Cada um cabe num shot sheet de 4 quadros no mesmo molde.

## Ordem de produção sugerida
1. Fichas: Maya ANTES e Ryan. Linda e Jess só como fundo desfocado na sonda.
2. **B05 (sonda)**: 1 shot sheet + 1 clipe Seedance.
3. Se aprovar: as demais fichas, depois os blocos na ordem.
