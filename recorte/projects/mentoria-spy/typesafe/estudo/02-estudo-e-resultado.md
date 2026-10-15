---
tipo: estudo
projeto: mentoria-spy / typesafe (Jev)
criado: 2026-09-28
tags: [spy, criativos, jev, typesafe, previsao-conversao, rubrica]
fontes: [01-evidencia.md, rubrica.py, validacao.py, prever.py]
---

# 02 — Estudo: prever qual criativo converte mais com o Jev

## O método (3 passos)
1. **Rubrica** (`rubrica.py`): 8 dimensões de decisão viram perguntas Jev (Score/Noul), cada uma ancorada num padrão da `01-evidencia.md`. Combinadas por peso em código (composite-scoring).
2. **Validação** (`validacao.py`): pontuei as **8 peças da casa com GASTO REAL** do Gerenciador (único rótulo com dinheiro no corpus) e correlacionei.
3. **Previsão** (`prever.py`): rodei a rubrica nos nossos criativos novos + âncoras do concorrente.

## O que a validação mostrou (n=8, direcional — NÃO estatístico)
- **Composto × log(gasto real): Spearman rho +0,67.** O campeão de US$ 4.074 (GD-AD01) o Jev pôs em 1º; os dois slogans fixos, no fundo. A separação grossa (hook real × slogan) ele acerta.
- **Dimensão mais preditiva de dinheiro: `dor_concreta` (rho +0,83)** > curiosidade (+0,67) > carga emocional (+0,60) > confissão (+0,48) > gancho-vs-slogan (+0,43).
- `transferivel` e `promessa_proibida_na_fala` **não** correlacionam com gasto (+0,05 / +0,14) — são eixos de sobrevivência/política, não de gasto. Por isso `promessa` fica fora do composto e vira só flag de risco.
- **Erros conhecidos:** superestima GD-AD05/AD03 (mid-tier) e subestima a SPY5 — cujo gasto veio do **mecanismo do gancho sumindo aos 8,6 s**, não da copy. A rubrica lê copy, não mecânica de edição. Limitação real.

## Previsão — nossos criativos (ranking por composto)
| # | criativo | composto | leitura |
|---|---|---|---|
| 1 | flora-f5 "I'm not crazy" | 0,830 | confissão 0,96 + curiosidade 0,89 |
| 2 | flora-f1 "Loving you doesn't stop them from cheating" | 0,780 | dor 0,92 + confissão 0,91 |
| 3 | 121 "she says it's a friend" | 0,748 | dor 0,95 + emoção 0,94; confissão baixa (acusação) |
| 4 | flora-f2 "cleanest phones" | 0,658 | curiosidade alta, confissão média |
| 5 | flora-f3 red flags | 0,601 | dor alta, confissão ~0 |
| 6 | flora-f4 podcast | 0,569 | curiosidade/confissão baixas |

Âncoras: slogan fixo L9 = 0,062 (piso, correto). **Secret Revealed (concorrente que escalou) = 0,379** — artificialmente baixo porque o radar **não baixa vídeo**, então só entrou a headline (estrelas+free), sem o hook de tela. **Não ler como "nosso ganha do deles".**

## Ressalvas que não dá pra ignorar
1. **Sem rótulo de conversão real** em lugar nenhum. A validação é contra GASTO (proxy de o quanto a Meta quis entregar), não contra venda. rho +0,67 em n=8 = direcional.
2. **A rubrica lê a COPY do hook.** Os 5 avatares da 121 têm a **mesma** copy → o Jev os pontua igual. A diferença entre eles é avatar/público, que este estudo **não** mede. Precisa de outro sinal (fit avatar↔público) e de teste real.
3. **Não captura mecânica de edição** (gancho sumindo vs fixo, ritmo, split) — só o conteúdo do hook. A SPY5 provou que isso importa.
4. Os pesos são hipótese ancorada; não os re-ajustei pra o gasto (n=8 = overfit garantido).

## Como isso vira previsão de verdade (fechar o loop)
Rodar no Meta os 2-3 do topo (f5, f1, 121), coletar CPA/ROAS/CTR reais via UTMify/Meta, e **re-validar** a rubrica contra venda de verdade. Aí os pesos deixam de ser hipótese. Enquanto não rodar, isto é um **filtro de priorização calibrado**, não um oráculo.
