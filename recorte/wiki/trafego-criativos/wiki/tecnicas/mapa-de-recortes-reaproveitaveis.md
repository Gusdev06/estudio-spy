---
tipo: tecnica
tags: [edicao, recorte, bisturi, whisper, legenda, avatar-ia, metodo, esteira]
fontes: [[fonte-teardown-sarah-flores-2026-10-14]]
---

# Mapa de recortes reaproveitáveis — a tabela que o Bisturi monta sem reabrir o vídeo

Toda referência que vai virar variação por recorte ganha uma tabela: frase inteira com in/out pelos word timestamps, se a frase é gancho autocontido, o que está em cena, e se há costura de clipe dentro. Mais a lista de janelas sem legenda pra tirar frame limpo do rosto.

## Colunas
| campo | de onde vem |
|---|---|
| in / out | word timestamps ([[mapa-de-tempo-por-whisper]]); entrar na pausa ou na costura, nunca no meio de palavra; whisper erra ±0,1 s |
| gancho? | ★★ autocontido e forte · ★ com ajuste mínimo · — depende de contexto (pronome sem referente: "as duas", "a outra", "isso") |
| cena | estado visual do objeto de cena (ex.: carta na mão / embaralhando / cartas na mesa) |
| costura dentro? | [[costura-de-clipe-ia-por-diferenca-de-frame]] |

## Regras
- **A cena tem que bater com a fala depois da emenda.** No [[criativo-sarah-flores-2284342465689308]], "essas três cartas" só existe com UMA carta na mão: não pode vir depois de um recorte que já mostra as três na mesa.
- **Pronome sem referente derruba o gancho.** "A diferença entre as duas…" não abre um ad; "Uma está com o fluxo aberto, a outra carrega um bloqueio" abre.
- **Janela sem legenda ≠ pausa.** A legenda some também nas costuras e em lacunas do gerador no meio de palavra — medir com [[janela-sem-legenda-por-varredura-da-faixa]], conferir olhando.
- Frame limpo pra gerar fala nova: boca fechada, mãos na posição mais frequente do vídeo, cena dominante (no caso, cartas na mesa, 70 % da duração).

## Conecta com
- [[gancho-falado-como-modulo-trocavel]] — os ★★ viram os módulos de gancho
- [[janela-limpa-continua-como-criterio-de-casting]] — mesma família: medir trecho limpo contínuo, não %
- [[medir-fronteira-de-bloco-em-video]] — fronteiras de bloco medidas, não chutadas
- [[paineis-recortados-do-proprio-campeao]] — reaproveitar o próprio original
