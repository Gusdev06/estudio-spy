# Análise de Criativos (Bid Cap) — 300+ Prompts

**Data:** 2026-07-18 · **Período:** últimos 7 dias (11–17/jul) · **Fonte:** Meta Ads
(nível ad) + UTMify. Moeda BRL. Meta = R$3k/dia de LUCRO via throughput de criativo.

## 🎯 Resumo executivo
O bid cap está funcionando como manda o manual: **1 criativo campeão carrega a conta**,
uma cauda de coadjuvantes ajuda, e a maioria dos ads **é starvada pelo bid** (correto).
O gargalo pra R$3k/dia é claro: **poucos campeões simultâneos**. Você tem provas de que
a conta acha vencedor (sleepers com ROAS 3–13); falta **volume de variação** pra ter
mais campeões rodando ao mesmo tempo — e **folga de bid** (ROAS 2,0 está bem acima do
breakeven ~1,3, dá pra bidar mais alto e comprar volume lucrativo).

## 🏆 CA-DZD · "HOTM - BIDCAP — EN" (a máquina principal)
Campanha: R$4.027 gasto · 177 vendas · valor R$8.132 · **ROAS 2,02** · CTR 7,86% · freq 1,89.
> Obs: ~53% do gasto veio de ads já deletados no período (churn normal de teste). Abaixo,
> os ads vivos que importam.

**👑 CAMPEÃO — varie ESTE primeiro**
- `ad_id 52515797525534` — R$1.011 · **49 vendas** · ROAS **2,39** · CPA R$20,64 · CTR 7,46% · freq 1,22
- Sozinho = 25% do gasto e 28% das vendas da campanha. É o cavalo de tração.

**✅ Coadjuvantes sólidos (ROAS ≥ 2, com volume)**
- `52532819915534` — R$102 · 7 vendas · ROAS 2,62 · CTR 8,63%
- `52532820087534` — R$45 · 3 vendas · ROAS 2,76
- `52532819718934` — R$104 · 5 vendas · ROAS 1,93 (limítrofe)

**🌱 SLEEPERS (ROAS alto, gasto baixo — o bid ainda não escalou; vigiar/variar)**
- `52515796206334` — R$23,8 · 5 vendas · **ROAS 13,43** · CTR 7,28% ⭐ candidato a próximo campeão
- `6999444134130` — R$31,7 · 2 vendas · ROAS 3,33 · CTR 9,12%
- `52534837462334` — R$29 · 3 vendas · ROAS 3,28 · CTR 5,05%

**🔴 34 de 50 ads com 0 venda** — bid starvando os fracos. Isso é o bid cap trabalhando
a favor; não é problema, é a auto-limpeza.

## 🥈 BM-LATAM · "BIDCAP EN 13/07" (segunda máquina, mais nova)
Campanha: R$1.110 gasto · 50 vendas · valor R$1.861 · **ROAS 1,68** · CTR 9,80% · freq 1,51.
CTR mais alto que a CA-DZD, mas ROAS menor — copy/oferta convertendo pior aqui.

- **Melhor:** `120247984578270685` — R$127 · 11 vendas · **ROAS 3,04** · CPA R$11,54 · CTR 7,62%
- Bons: `120247984322070685` (R$28 · ROAS 3,78 · CTR 13,04%), `120247984541050685` (R$31 · ROAS 3,38)
- 🩸 **Sangradores (gastando abaixo do breakeven):** `120247984641660685` (R$78 · ROAS 0,68),
  `120247984641630685` (R$74,6 · ROAS 0,70), `120247984541060685` (R$51 · ROAS 1,03).
  Vigiar — se não corrigirem sozinhos, o bid dessa campanha pode estar alto demais.

## 📈 Leituras estratégicas p/ R$3k/dia de lucro
1. **Folga de bid:** ROAS operacional ~2,0 e breakeven ~1,3 (margem 55%). Há espaço pra
   **subir o bid 15–20% na CA-DZD** e comprar volume — CPA sobe, mas segue lucrativo.
   Alavanca mais rápida de lucro adicional. (Testar em incremento, monitorando CPA.)
2. **Throughput de criativo (alavanca nº1):** poucos campeões simultâneos. Produzir
   variações diárias do campeão `52515797525534` + dos sleepers → mais vencedores ao
   mesmo tempo = mais gasto lucrativo que a campanha absorve sob o bid.
3. **Recuperar cartão recusado (23%)** → mais venda pelo mesmo CPA → ROAS efetivo maior
   → habilita bidar mais alto. (Ver baseline-escala-2026-07-18.md.)
4. **BM-LATAM EN** é 2ª máquina viável (ROAS 1,68 subindo): injetar o campeão da CA-DZD
   e variações pode elevá-la; cortar/observar os 3 sangradores.

## ⏭️ Próximos passos
- [ ] Mapear `ad_id 52515797525534` (+ sleepers) → **qual criativo real** é (puxar
  thumbnail/vídeo via Meta) e cruzar com a pasta `criativos/criativos-en/`.
- [ ] Ligar a esteira: gerar variações diárias do campeão (hook first) com o `copywriter`.
- [ ] Plano de teste de bid (+15–20%) na CA-DZD.
- [ ] Corrigir checkout (cartão recusado).
