# Nomenclatura de campanhas — oferta spy (desde 30/09/2026)

Separador ` - ` (nunca `|`: a UTMify grava `nome|ID` na UTM). Ordem fixa, sempre maiúsculas nos códigos.

## Campanha
`[CONTA] - [ESTRUTURA] - [OFERTA] - [CANAL] - [DD-MM] - [OBJETIVO]`
- CONTA: `N1` `N2` `N3` (contas novas = pastas conta-1/2/3), `7518`, `9313`, `2587`, `NOEL`
- ESTRUTURA: `CBO 1-1-5`, `CBO 1-1-1`, `ABO`
- OFERTA: `ZAP` ou `GRAM` · CANAL: `WPP` ou `IG`
- OBJETIVO: `ESCALA` (só campeões) · `TESTE` (criativo novo) · `DUP2`, `DUP3`… (duplicata de campanha vencedora)
Ex.: `N1 - CBO 1-1-5 - ZAP - WPP - 30-09 - ESCALA`

## Conjunto
`CJ[n] - [GEO] - [PÚBLICO]` — ex.: `CJ1 - MUNDO - ABERTO`

## Anúncio
`[PEÇA] - [FAMÍLIA] - [CONTA]` — ex.: `CP77 - SECRET - N1`
- PEÇA: código da Biblioteca (`CP77`, `CP108`…) ou apelido: `FLORA5` (Flora var5), `LAUREN6` (Lauren var6).
  Apelidos novos: `lib/anuncios.ts → APELIDOS` no hub.
- FAMÍLIA: `SECRET`, `PODCAST`, `HOOK22`, `DRAMA`…

O Spy Hub liga o anúncio à peça pelo código (sem export do Gerenciador) e a análise de estrutura lê a ESTRUTURA do nome da campanha.
