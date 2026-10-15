# Esteira de criativos spy — pacote completo (23/09/2026)

Tudo que é preciso para **clonar um criativo de vídeo que já escala e produzir variações** (avatar novo, copy nova, elenco novo) do jeito que a gente produziu 121 peças entre 10 e 23/09/2026.

O princípio, em uma frase: **o criativo campeão é o molde; a gente mede cada camada dele e reconstrói uma por uma**, trocando só o que precisa mudar. Não é "gerar um vídeo com IA": é medir, gerar o rosto, redesenhar as camadas e montar no ffmpeg.

---

## 1. O que instalar (uma vez)

| ferramenta | pra quê | como |
|---|---|---|
| **ffmpeg / ffprobe** | corte, medição e montagem | `brew install ffmpeg` (Mac) · [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) (Windows) |
| **Python 3.9+** com `pillow numpy opencv-python-headless` | desenhar legendas/faixas, medir cor e nitidez, detectar rosto | `pip3 install pillow numpy opencv-python-headless` |
| **wavespeed CLI** | gerar imagem, lipsync e voz | `npm i -g @wavespeed/cli` → `wavespeed login` |
| **uv** (opcional) + **mlx-whisper** (Mac Apple Silicon) | transcrição palavra a palavra | `brew install uv`; o comando já vem nos scripts |
| — alternativa fora do Mac | idem | `pip3 install faster-whisper` e trocar a chamada (ver `metodo/06-troubleshooting.md`) |

Fontes usadas estão em `fontes/` (Poppins, Anton, Oswald, Montserrat, Inter — todas OFL). No Mac, o molde 1 usa também a `Arial Rounded Bold` do sistema.

## 2. Conta e custo

Tudo roda numa conta só: **[wavespeed.ai](https://wavespeed.ai)** (pré-pago, chave em `wavespeed login`). Modelos e preço real medido:

| o que | modelo | preço |
|---|---|---|
| Rosto novo (imagem) | `openai/gpt-image-2/text-to-image` ou `/edit`, `quality=medium`, 9:16 ou 16:9 | **US$ 0,067** por imagem (em `high` custa 0,22 e não melhora numa janela de vídeo) |
| Lipsync (foto + áudio → vídeo falando) | `pruna-ai/p-video/avatar`, `resolution=720p` | **US$ 0,025 por segundo** de clipe |
| Voz | `minimax/speech-2.6-hd` (`Casual_Guy`, `Calm_Woman`, `Wise_Woman`, `Determined_Man`) | **US$ 0,05–0,08** por locução de 30 s |

**Custo por peça pronta: US$ 0,80 a US$ 1,20.** Uma variação só de avatar (mesma copy) custa ~US$ 0,85; copy nova + avatar novo ~US$ 1,20. Lote de 10 = US$ 8 a 12.

> Regra da casa: **estimar antes de disparar**. `wavespeed price <modelo> -i ...` e `wavespeed billings --since <data> --json` mostram o cobrado de verdade.

## 3. O fluxo, do criativo do concorrente até a peça pronta

1. **Pegar o criativo** que já escala (Meta Ad Library) e salvar o arquivo original.
2. **Medir** (`scripts/analisar-estrutura.py` + ffprobe): resolução, duração, onde estão as faixas/janelas, quando corta, onde aparece rosto e onde aparece painel de app.
3. **Transcrever** o áudio palavra a palavra (whisper) — é isso que dá o tempo de cada bloco e do karaokê.
4. **Escrever a copy** (se for mudar) seguindo uma das estruturas de `metodo/03-copy.md` e gerar a voz (TTS), cortando as pausas (`scripts/cortar-pausas-audio.py`).
5. **Gerar o rosto** (gpt-image-2) e o **lipsync** (Pruna) — prompts prontos em `metodo/02-prompts.md`.
6. **Reconstruir as camadas queimadas**: karaokê, faixa de headline, cards, setas, CTA. Nunca recortar um retângulo com fundo do original (ver `metodo/01-regras.md`).
7. **Montar** com o script do molde (`moldes/<n>/montar*.py`), **conferir** (`metodo/04-conferencia.md`) e só então dar por pronta.

## 4. Os 5 moldes prontos (`moldes/`)

| # | molde | como é a peça | o que se troca |
|---|---|---|---|
| **1** | `1-secret-revealed` | rosto em quadro cheio + faixa vermelha de headline no topo + karaokê de 1 palavra | avatar, copy e **headline** (faixa redesenhada) |
| **2** | `2-luiza-split-android` | quadrado 720×720: rosto à esquerda, gravação do funil à direita; **look de celular** calibrado | avatar |
| **3** | `3-podcast-wpp` | layout de post: título fixo + janela de vídeo + karaokê; alterna 2 avatares e painéis do funil; CTA final | avatar(es), copy inteira (diálogo), elenco |
| **4** | `4-ad02-h2-gram` | rosto cheio + caixa de gancho + card/painéis do app + CTA com setas (molde do campeão do Instagram) | avatar, copy, caixa de gancho |
| **5** | `5-ad02-h2-zap` | o mesmo molde 4 adaptado para a oferta de WhatsApp, com os painéis do funil do Zap | avatar, copy |

Cada pasta tem um `README.md` com o comando exato. As referências dos moldes estão em `midia/`.

## 5. Ordem de leitura

0. `metodo/00-comeco-rapido.md` — a primeira peça em 25 minutos, comando a comando.
1. `metodo/01-regras.md` — as 8 regras que custaram caro pra descobrir. **Leia antes de produzir.**
2. `metodo/02-prompts.md` — os prompts de imagem, lipsync e voz que funcionam (e os que estragam).
3. `metodo/03-copy.md` — as 4 estruturas de copy com dado de gasto atrás.
4. `metodo/04-conferencia.md` — o que conferir em cada peça antes de subir.
5. `metodo/05-custos.md` — custo real por peça e por lote.
6. `metodo/06-troubleshooting.md` — os erros que vão aparecer e como resolver.
7. `metodo/wiki/` — as páginas do nosso segundo cérebro sobre criativo (técnicas e evidências).

## 6. Aviso

As peças são para a oferta "spy" (monitorar WhatsApp/Instagram). É um nicho sensível: a promessa pesada **nunca vai na fala** (só na imagem do painel), e nenhuma peça diz "hack", "senha" ou "espionar". Contas caem por causa do que está escrito e falado, não do formato.

---

## 7. Como este pacote chega (3 arquivos)

| zip | o que tem | tamanho |
|---|---|---|
| `esteira-1-metodo-scripts.zip` | **tudo que importa**: método, scripts, moldes, fontes, checklist | 11 MB |
| `esteira-2-midia-referencias.zip` | referências dos moldes 1, 2 e 3 + trilha + 2 peças de exemplo | 29 MB |
| `esteira-3-midia-ad02-gdad01.zip` | referências dos moldes 4 e 5 (AD02-H2 e o campeão GD-AD01) | 26 MB |

Descompacte os três **na mesma pasta** — eles se juntam em `PACOTE-ESTEIRA-CRIATIVOS/`. Só o 1 já permite estudar o método e rodar em cima de criativos novos; 2 e 3 são as referências dos moldes prontos.

---

## 8. Entregar isso pro seu Claude (2 minutos)

O pacote já vem preparado para ser operado por um agente (Claude Code, Cursor, Codex — qualquer um que leia arquivos e rode comandos no terminal).

1. Descompacte os 3 zips na mesma pasta.
2. **Claude Code** (recomendado): `cd` na pasta e rode `claude`. Ele lê o `CLAUDE.md` daqui automaticamente e já sabe as regras.
   **Claude no navegador/app:** crie um Projeto, suba `CLAUDE.md`, `README.md`, `metodo/*.md` e `CHECKLIST.md` como conhecimento do projeto — mas quem gera vídeo é o terminal, então o Claude Code é o caminho.
3. Cole nele o texto de **`COLE-NO-CLAUDE.txt`**. Ele vai ler o método, rodar `bash setup.sh`, instalar o que faltar e pedir o `wavespeed login`.
4. Mande o criativo: *"faz 5 variações desse trocando o avatar"* + o caminho do .mp4. Ele mede, estima o custo, pede seu ok e produz.

`setup.sh` verifica ferramentas, bibliotecas, login e arquivos do pacote; `bash setup.sh --testar` ainda faz um teste real de ffmpeg + PIL + detector de rosto (sem custo).
