---
tipo: tecnica
tags: [avatar, casting, lipsync, custo, spy-zap, spy-gram, regra-da-casa]
fontes: [[fonte-casting-gram01-var-avatar-5-rostos-2026-09-11]], [[fonte-plano-replica-gram01-var-avatar-2026-09-11]]
---

# Avatar segue o gênero da voz

Antes de gerar um rosto sobre uma locução pronta, meça o f0 da VO e case o gênero do avatar com ele — o erro custou US$ 4,66 em 10/09 e a "prova" de que não precisava casar era uma leitura errada de frame.

## Onde a regra nasceu

10/09, lote var4 da Emilly (STATUS): a primeira leva tinha **3 mulheres pra uma voz masculina**;
o maestro cancelou, mas um job do OmniHuman (US$ 0,16/s × 29 s) já tinha sido cobrado —
**US$ 4,66 perdidos** por um rosto que nunca ia entrar na peça. Regra registrada no mesmo dia:
"avatar segue o gênero da voz original".

## A prova em contrário que caiu (11/09)

O teardown de 01/09 do "vencedor" GRAM dizia que a peça #10 tinha **voz feminina sobre rosto
masculino** ("homem de óculos") — e disso o [[roteiro-mestre-com-n-vozes]] tirou a leitura "o rosto
não precisa ser quem fala, é B-roll de rosto". Conferido em 11/09 no frame 0, aos 15 s e aos 25 s:
**a #10 é mulher** (cachos, moletom cinza). O homem de óculos com `IF YOU SUSPECT` é a **#13**, de
outra página (VolutPay) e outro roteiro. Nas 4 peças do roteiro mestre o gênero do rosto **casa**
com o da voz: #1 e #10 mulher / 258 Hz; #3 e #6 homem / 112–138 Hz.

Duas lições no mesmo erro: (1) atributo de ator sai do **frame**, não da tabela
([[nome-de-pagina-nao-e-nome-do-ator]]); (2) a `TRANSCRICOES.md` já dizia "mulher" — quando duas
fontes da casa divergem, olhe o vídeo antes de escolher uma.

## Como aplicar

1. Extraia o áudio e estime o f0 mediano dos trechos vozeados (autocorrelação local, sem custo).
   Zona de fronteira: ~155–170 Hz — aí o desempate é o rosto original da peça, se houver.
2. Escreva o gênero na nota de casting **antes** do prompt da imagem-base.
3. Se a locução vai ser trocada por TTS, escolha a voz primeiro e o rosto depois — nunca o inverso.
4. Se o lote quer os dois gêneros, são **duas VOs** (uma por gênero), não um rosto trocado sobre a
   mesma voz — é o que a família de 16/07 fez ([[familia-criativos-spy-gram-16-julho]]).

No [[lote-gram01-l9-var-avatar-5-rostos]] a VO mestre EN mede f0 mediano 170 Hz (p25 150 / p75 195)
e o rosto do controle é mulher: os 5 avatares são mulheres, e uma eventual correção do Gusta
acontece **antes** da fase paga.

## Conecta com

- [[estimar-custo-de-geracao-antes-de-disparar]] — o rosto errado é custo de geração jogado fora
- [[roteiro-mestre-com-n-vozes]] — a página que carregava a leitura antiga, corrigida
- [[molde-de-edicao-n-atores]] — N atores, sim; mas do gênero da voz
- [[matriz-genero-x-idioma]] — gênero da VO é eixo próprio, não se mistura com rosto
