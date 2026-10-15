# AD02-H2-INSTA reconstruído com avatar novo · 2026-09-17

Pedido do Gusta: "variação desse: usar o áudio, gerar um novo avatar e copiar a edição". Refaz o lote de 14/09 (peças 50–52, **reprovadas**: "gambiarra, edição errada") pelo caminho certo — **cada camada reconstruída como elemento próprio**, nada recortado com fundo do original.

| | |
|---|---|
| **Peça** | `AD02-H2-reconstruido-a2.mp4` — 1080×1920, 30 fps, 1090 frames, **36,33 s** (igual ao original). Cópia: `CRIATIVOS-PRONTOS/53` |
| Original | `REFERENCIA-original.mov` (md5 `ca528edb89e71cf77d739f64560f1df7`) |
| Avatar | `clipes/a2.mp4` (link para o lote de 14/09): latino ~27, moletom creme, mesmo banheiro — Pruna 30 s, já pago |
| Áudio | o do original, intacto |
| Hook | frames 0–191, o original intacto (clipe de reação + manchete) |

## O que foi reconstruído, e como cada camada foi medida

**Karaokê** (`gerar-karaoke.py` → `karaoke/frames/*.png`, 1 PNG por frame)
- Li **frame a frame** os 34 blocos do original e a cor de cada uma das 90 palavras (`karaoke/folha-0..5.jpg`): blocos de até 3 palavras quebrando onde o editor quebrou (não é regra fixa: "TO GUESS YOU" atravessa a frase; "DETAIL", "LOOK", "IT", "BEHAVIOR" ficam sozinhos), destaque andando palavra a palavra alternando **amarelo (253,226,0)** e **vermelho (253,0,0)**, branco 252, contorno preto 7 px + sombra.
- Fonte: **Oswald Bold** — testadas Anton, Bebas, Oswald, Avenir Next Condensed, Poppins e Montserrat contra o original (`conferencia/fontes-teste*.jpg`); Oswald é a única que bate a largura ("WHEN SOMEONE TRIES" = 665 px a 62 px de capital) sem esticar. Tracking 0, engorda de 1,6 px no preenchimento.
- Capital de 62 px medida. Duas alturas: **1113** enquanto o card "Connecting" ocupa a base (frames 192–311), **1641** no rosto limpo, **1695** sob os painéis, **1666** no bloco final.
- "THEY DELETED EVERYTHING" quebra em 2 linhas como no original (limite de 820 px). Sem pontuação, como no original.
- Dois trechos em que o **original não mostra legenda** (o painel entra por cima em 608–632; "where to look" em 966–1004) ficam sem legenda.
- Tempos: whisper por palavra do áudio (`molde/vo-16k.json`).

**Painéis do app** (`assets/paineis/`)
- Os 4 prints do funil (perfil, "Real-time access/Suspicious data", feed, DMs) estão numa **bbox fixa medida por bordas nítidas: (193,347) · 692×1224**, sem animação de entrada (corte seco). Recorte **justo na borda do print** — não há moldura de fundo — mais **sombra sintética** (retângulo preto blur 28, alfa 110, margem 90), calibrada pela queda de luminância medida ao redor do painel no original.
- Card "Connecting to Instagram" (bloco 1): bbox (147,1369) · 788×398, **máscara de cantos arredondados r=30** + sombra.

**CTA "CLICK THE BELOW"** (`assets/cta/`) — mesma fonte do karaokê (Oswald Bold, capital 90 px, 857 px de largura medidos), preenchimento prateado com gradiente, contorno vermelho (222,4,4) 6 px + glow, 8 fases com letras caindo para ecoar o glitch do original. Frames **999–1082**, medidos.

**Setas** (`assets/setas/`) — 3 chevrons nas medidas do original (x 295–755, topos 545/865/1185, traço 46), 6 fases de pulso. As do original são branco semitransparente (luminância máxima 204), impossíveis de extrair; redesenhadas.

**Avatar** — tela cheia com **zoom + deslocamento por bloco** (o editor foi fechando o plano): 1,0/0 · 1,3/140 · 2,6/450 · 1,9/260 · 2,8/620. **Desfoque gblur σ=18** nos blocos de painel, calibrado para reproduzir a razão de nitidez do original (0,58/0,99).

## Montagem
`montar-reconstrucao.py <clipe> <saida>` — compõe tudo no ffmpeg. Os inputs secundários entram com **`tpad` transparente** (não `setpts`): a 1ª versão com `setpts` deslocou os painéis e atrasou o card; trocado pelo método que já funcionava nos lotes do podcast.

## Custo
**US$ 0** neste lote — avatar, imagem e clipe vieram do lote de 14/09. Montar com os outros dois avatares já gerados (a1 branco de barba, a3 indiano) é custo zero: `python3 montar-reconstrucao.py clipes/a1.mp4 AD02-H2-reconstruido-a1.mp4`.

## Conferência
`conferencia/orig-vs-reconstruido.jpg` (10 instantes), `emendas.jpg` (frame antes/depois de cada troca), `karaoke-orig-vs-novo.jpg` e `karaoke-ajuste.jpg`, `cta-orig-vs-novo.jpg`, `fontes-teste*.jpg`, `frame-700.jpg` (painel em tamanho real).

## O que ainda difere do original (para o olho)
- A fonte do original é ligeiramente mais gorda e arredondada que Oswald Bold; a diferença é de desenho de letra, não de tamanho, cor ou posição.
- O glitch do CTA é uma aproximação (letras caindo em fases), não a animação exata do preset.
- Bloco 4 (rosto limpo, 15,3–20,3 s): o close do original é um pouco mais fechado; `Z4` ajustável por env se incomodar.
