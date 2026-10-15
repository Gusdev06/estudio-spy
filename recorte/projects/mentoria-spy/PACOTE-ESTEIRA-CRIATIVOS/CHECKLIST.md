# Checklist por peça (imprima e siga)

**Antes de gastar**
- [ ] Original baixado, md5 anotado, duração e resolução medidas
- [ ] Estrutura medida: onde tem rosto, onde tem painel, onde corta
- [ ] Áudio transcrito palavra a palavra (se for reaproveitar) ou copy escrita e gravada
- [ ] Custo estimado (`wavespeed price`) e anotado

**Gerando**
- [ ] Descrição do avatar: etnia, idade, cabelo, pelo facial, roupa lisa
- [ ] Prompt do lipsync com **identidade travada** e **pose em positivo**
- [ ] Gênero da voz = gênero do avatar

**Antes de montar**
- [ ] Download íntegro (`ffmpeg -v error -i x -f null -`)
- [ ] Folha do clipe inteiro olhada (mão, segunda pessoa, troca de identidade)
- [ ] `checar-identidade.py` sem DRIFT

**Antes de subir**
- [ ] Frames e duração corretos
- [ ] Emendas conferidas (antes/depois de cada bloco)
- [ ] Original × novo lado a lado
- [ ] Áudio: 0 silêncios longos, fala ~−18 dB, música ~−28 dB
- [ ] Sem PII na tela, sem palavra proibida na fala
- [ ] Custo real anotado (`wavespeed billings --since ...`)
