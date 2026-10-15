# Podcast WPP — CP108 com avatar + copy novos · 2026-10-07 → peças 170 e 171

Pedido do Gusta: "2 variações dos melhores criativos, dessa vez de avatar e de copy". Base: **CP108** (`CRIATIVOS-PRONTOS/108-ZAP-podcast-wpp-copy-nova-branca-ruiva-x-negra-afro.mp4`, 2º em vendas: 31 vendas, ROAS 4,02). Cada peça troca o **par de avatares** e a **copy do diálogo**. O resto segue o molde da 108: título fixo, janela 720×587 em y 346, karaokê com caixa roxa, painéis do funil, CTA b-roll de 15,4 s e trilha de suspense. Pipeline herdado de `../podcast-wpp-57s-copy-nova-2026-09-23/` (106/var5/var6).

## Peças
| peça | arquivo | par (A host × B convidada) | duração |
|---|---|---|---|
| 170 | `pecas/170-ZAP-podcast-wpp-copy-apagadas-japonesa-bob-x-negra-raspado.mp4` | japonesa ~38, bob com franja, blazer caramelo × negra ~34, cabelo raspado, argola dourada, blusa lilás | 52,3 s |
| 171 | `pecas/171-ZAP-podcast-wpp-copy-intuicao-persa-x-branca-47-pixie.mp4` | persa ~36, cabelo longo liso, blazer preto × branca ~47, pixie grisalho, blusa coral | 53,4 s |

O título ficou igual ("HOW TO READ YOUR PARTNER'S MESSAGES ON YOUR OWN PHONE"), porque as duas copies se encaixam nele. Os painéis são os mesmos trechos do original que a 108 usa (16,45 s na fala 2 e 22,0 s na fala 7), reencaixados na nova timeline. O CTA entra na fala 9. As vozes são as mesmas da 108 (A `Calm_Woman`, B `Wise_Woman`). As peças ficaram 3–4 s mais longas que a 108 (49 s) porque as falas novas são um pouco maiores (116/115 palavras contra 109).

## Roteiros (mesmo esqueleto: promessa → objeções → mecanismo → prova → CTA)
**170 — ângulo "ele apaga tudo"** (`roteiro-170.tsv`)
1. A: If he clears his WhatsApp every night, you can still read every one of those chats.
2. B: The ones he already deleted? Without his phone? *(painel)*
3. A: Without his phone. All you need is his number, and it takes about a minute.
4. B: And he won't notice anything?
5. A: Nothing changes on his side. No alert, no code, his phone stays in his pocket the whole time.
6. B: So what do I do first?
7. A: You type his number, the system pulls the backup, and the conversations load right on your screen. *(painel)*
8. A: Names, times, voice notes, even the photos he swore he never sent. It's all there.
9. A: The link is just below. Put in his number and see it with your own eyes. *(CTA)*

**171 — ângulo "intuição"** (`roteiro-171.tsv`)
1. A: If your gut says something is off, you can see his WhatsApp conversations on your own phone today.
2. B: On my phone? He never lets that thing out of his sight. *(painel)*
3. A: He doesn't have to. You never touch his phone. All you need is his number.
4. B: That's it? Just the number?
5. A: That's it. Archived chats, deleted messages, and who he texts at night while you're asleep.
6. B: Alright. Show me how it works.
7. A: You type the number, the system pulls the backup, and his conversations open right on your screen. *(painel)*
8. A: Every name, every timestamp, every message he thought was gone forever. No more guessing.
9. A: Tap the link below, type in his number and finally get your answer. *(CTA)*

## Receita (de `projects/mentoria-spy/`, pasta `D` = esta)
1. `bash D/gerar-tts.sh 170` → `audio/170/l*.mp3`
2. `python3 D/gerar-timeline.py 170` apara o silêncio de cada fala e limita as pausas internas a ~0,32 s. Junta as falas com pausas de 0,12 s (mesma pessoa) ou 0,24 s (troca de pessoa) e gera `vo.wav`, `molde/170/linhas.json`, `blocos.json` e o mp3 de cada bloco. Depois vem o whisper: `uvx --from mlx-whisper mlx_whisper molde/170/vo-16k.wav --model mlx-community/whisper-large-v3-turbo --word-timestamps True --language en --output-format json --output-dir molde/170`.
3. `python3 D/gerar-bases.py 170-A 170-B` (gpt-image-2/edit, o mesmo request da var5). **As URLs antigas dos frames de referência expiraram (403)**, então os frames foram re-subidos e estão em `base/url-ref-*.txt`.
4. `bash D/gerar-clipes.sh 170` gera os 6 clipes Pruna com o prompt de identidade travada da var6 (seed 21) e já valida cada um decodificando o arquivo inteiro.
5. `python3 D/gerar-karaoke.py 170`: o texto exibido vem do **roteiro**, não do whisper (ele ouviu "a link", "back up"). Os tempos vêm do whisper, alinhados por difflib.
6. `python3 D/montar.py 170 D/c170/sem-musica.mp4`, depois `bash D/por-musica.sh D/c170/sem-musica.mp4 <trilhas/suspense.m4a da pasta-mãe> D/c170/final.mp4 <início da fala 9>`

## Conferência (rodada, não suposta)
- As duas peças decodificam inteiras sem erro, em 720×1280 a 30 fps (1570 e 1602 frames).
- **0 silêncios ≥ 0,5 s** medidos com `-hide_banner` a −35 dB. O detector funciona: a −20 dB/0,3 s ele acha 7 e 9 trechos. Volume médio −19,9 e −19,7 dB, com a trilha de suspense por baixo (−17,3 dB de ganho, mesmo nível da 108).
- **Clipes** (`checar-clipes.py`, YuNet ≥ 0,8 a 4 fps, clipe inteiro): 1 rosto por frame e sem troca de identidade (altura do rosto ×0,93–1,14). Folhas em `conferencia/clipes-170.jpg` e `clipes-171.jpg`.
- **Defeito do Pruna, fora da janela:** ele inventou um homem entrando pela esquerda (170 b4 e 171 b6) e mãos na borda esquerda (171 b1/b3/b5/b8). Isso fica em x < ~300 do clipe, e a janela começa em x ≥ 359. Para confirmar, a faixa de 80 px da borda esquerda da janela na peça varia no máximo 2,7 níveis de cinza por bloco, e a folha `conferencia/bordas-intrusos.jpg` está limpa.
- **Peça** (`conferir-peca.py`, janela a 6 fps até o CTA): nenhum frame com mais de 1 rosto. O rosto fica centrado em x 347–417 (a janela tem 720), e o karaokê não encosta na borda.
- Para conferir a olho: `conferencia/final-2.jpg` (12 instantes por peça, com título, falas, painéis, karaokê e CTA) e `conferencia/casting.jpg` (os 4 avatares).

## Custo real: US$ 1,86 (chave `macbook`, somado por prediction id no `wavespeed billings`)
TTS 18 falas US$ 0,12 · 4 imagens US$ 0,27 · 12 clipes Pruna US$ 1,48 (170: US$ 0,73, já com a sonda b1; 171: US$ 0,75). A tentativa de imagem que falhou com 403 foi estornada. Fica ≈ US$ 0,93 por peça, dentro do teto de US$ 3,00.
