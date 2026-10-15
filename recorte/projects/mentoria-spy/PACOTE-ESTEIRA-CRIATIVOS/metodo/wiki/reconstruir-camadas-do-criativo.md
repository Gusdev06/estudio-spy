---
tipo: tecnica
tags: [clone, troca-de-avatar, karaoke, camadas, metodo]
fontes: [[fonte-ad02-h2-var-avatar-2026-09-14]]
---

# Reconstruir as camadas do criativo

Regra da casa desde 16/09/2026, depois de um lote reprovado ([[recortar-camada-queimada-em-vez-de-recriar]]): quando o criativo tem karaokê, painéis ou CTA **queimados sobre o rosto**, a troca de avatar exige **reconstruir cada camada**, não recortá-la.

O que isso significa na prática:
- **Karaokê:** medir fonte (corpo, tracking, contorno, sombra), as cores do destaque, as alturas usadas e os tempos por palavra; redesenhar bloco a bloco, com o destaque andando palavra a palavra se for esse o padrão. O molde do Secret Revealed (`remontar-secret.py`) já faz isso em PIL e serve de base.
- **Painéis do app:** remontar como elemento próprio, sobre fundo limpo, e compor — não recortar a região do original.
- **Camadas semitransparentes** (setas, faixas com alfa): redesenhar sempre; não existe extração limpa.
- **Zoom do editor:** se o original fecha o plano ao longo do vídeo, o avatar precisa acompanhar com crop e offset por bloco, calibrados contra o original.

O custo é maior e é o padrão aceito. Composição por recorte de região não é entregável.

## Como foi feito na prática (17/09, peça 53)
1. **Ler o karaokê frame a frame**, não deduzir regra: uma folha por palavra (`karaoke/folha-*.jpg`) e registrar bloco + cor de cada uma. O agrupamento do editor não é determinístico ("TO GUESS YOU" atravessa a frase; "DETAIL" fica sozinho).
2. **Escolher a fonte por largura medida**, não por aparência: testar candidatas renderizando a mesma frase na mesma altura de capital ao lado do original. Oswald Bold bateu 665 px; Poppins/Montserrat passaram de 1900.
3. **Medir cores por mediana** dos pixels da máscara (amarelo 253/226/0, vermelho 253/0/0), contorno pelo perfil de luminância.
4. **Painéis:** achar a bbox por bordas nítidas em vários frames; se for fixa, recorte justo na borda + sombra sintética calibrada pela luminância ao redor. Sem margem de fundo.
5. **Desfoque:** medir a razão de nitidez desfocado/nítido no original e escolher o σ que reproduz a razão no avatar.
6. **Timing dos inputs secundários no ffmpeg:** `tpad` transparente, nunca `setpts` — o `setpts` deslocou painéis e atrasou o card na 1ª montagem.

## Conecta com
- [[lote-ad02-h2-var-avatar]] — o caso que originou a regra
- [[lote-secret-revealed-indianos]] — molde onde o karaokê já é reconstruído
- [[criativo-como-layout-de-post]] — quando as camadas vivem fora da janela, nada disso é necessário
