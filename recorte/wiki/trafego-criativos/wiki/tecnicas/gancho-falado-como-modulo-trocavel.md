---
tipo: tecnica
tags: [locucao, hook, producao-em-escala, variacao, spy-gram]
fontes: [[fonte-roteiro-gram-l9-2026-09-01]]
---

# Gancho falado como módulo trocável

Grave o **primeiro beat da locução em arquivo separado** dos outros. Trocar o gancho falado passa a custar 3,8s de áudio em vez de uma regravação inteira — e o eixo mais forte do criativo vira testável pelo preço do mais fraco.

## O problema que resolve

[[roteiro-mestre-com-n-vozes]] barateia rosto e faixa a quase zero, mas deixa a locução como bloco monolítico: mudar a primeira frase obriga a regravar os 29s. Resultado prático é que ninguém testa gancho falado — testa-se o que é barato, e o gancho falado fica parado.

## Como fazer

1. Cortar o roteiro em beats numerados (no molde L9: B1 gancho · B2 problema · B3 objeções · B4 mecanismo · B5 payoff · B6 recolocação · B7 CTA).
2. Renderizar **B1 sozinho** e **B2–B7 como um bloco**, com a duração de B1 travada ao frame (no L9: 3,8s).
3. Escrever N versões de B1 na mesma duração. Concatenar: `B1-variante + B2..B7` = peça nova.
4. Se a duração de uma variante não fechar, ajustar a variante — nunca o bloco. Duração é eixo próprio e não pode se mexer junto com o gancho ([[variar-uma-alavanca-por-vez]]).

Vale pra locução gravada e pra TTS igual. Com [[kling-3-fala-o-roteiro]] a divisão é ainda mais direta: B1 é uma geração curta e independente.

## Ordem de teste

Faixa de hook primeiro (custa 1 PNG), gancho falado depois com a faixa vencedora travada, rosto por último. Ver [[eixos-de-variacao-de-criativo]].

## Conecta com

- [[tres-camadas-de-gancho-sem-repeticao]] — B1 é a camada falada; ela precisa continuar não repetindo as outras duas a cada variante
- [[faixa-de-hook-fixa-sem-legenda]] — o eixo mais barato, que vem antes deste
- [[molde-de-edicao-n-atores]] — a mesma lógica de molde, aplicada ao áudio
- [[gancho-como-alavanca-unica-matte-mais-call-out]] — 🆕 (11/09) o B1 à parte é o que deixa girar matte + call-out como par pelo preço de um PNG e ~5 s de áudio
