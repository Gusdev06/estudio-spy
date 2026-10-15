---
tipo: tecnica
tags: [medicao, legenda, frame-limpo, ffmpeg, avatar-ia, edicao, metodo]
fontes: [[fonte-teardown-sarah-flores-2026-10-14]]
---

# Janela sem legenda por varredura da faixa — achar frame limpo do rosto em vídeo com legenda queimada

Pra gerar fala nova a partir do avatar do original é preciso um frame sem texto queimado. Varrer só a faixa da legenda a 10 fps e contar pixels do contorno preto (+ cor da keyword) dá todas as janelas limpas em segundos; depois confirma olhando.

## Receita
```bash
ffmpeg -hide_banner -v error -i original.mp4 -vf "fps=10,crop=720:120:0:940" -f rawvideo -pix_fmt rgb24 band.raw
# numpy por frame: pretos = (R+G+B < 30).sum(); amarelos = (R>200 & G>170 & B<90).sum()
# legenda presente: milhares de pretos + amarelo > 0; ausente: < ~1.100 pretos e amarelo 0
```
Depois: extrair frames full-res na janela (passo 0,1–0,2 s), montar um tile e olhar — escolher boca fechada e mãos na pose dominante.

## O que o caso ensinou ([[criativo-sarah-flores-2284342465689308]])
- A legenda some em **toda pausa e toda costura**, mas também em lacunas do gerador no meio da fala (2,1 · 8,1–8,7 · 38,2–38,7 · 49,1–49,5 s). Janela sem legenda não é sinônimo de pausa.
- Janelas curtas: 0,2–0,7 s. A maior é o fim (79,2–79,9 s) e a pausa antes do CTA (73,4–74,0 s).
- Objeto escuro na faixa (baralho, mãos) dá algumas centenas de pretos sem legenda — por isso o limiar e a checagem de amarelo.

## Conecta com
- [[mapa-de-recortes-reaproveitaveis]] — onde as janelas entram
- [[recortar-camada-queimada-em-vez-de-recriar]] — a alternativa quando não há janela limpa
- [[reconstruir-camadas-do-criativo]] — reconstruir a legenda por cima depois
- [[frame-1-sem-piscar]] — critério de frame de abertura
