#!/usr/bin/env python3
# Karaokê do AD02-H2 versão WHATSAPP (copy nova): mesmo desenho do karaokê reconstruído do AD02-H2 (17/09) — blocos de até 3
# palavras quebrando no fim de frase, destaque alternando amarelo/vermelho — nos tempos do áudio novo (molde/timeline.json).
# Fonte Oswald Bold (a mais próxima em largura: "WHEN SOMEONE TRIES"
# = 665 px a 62 px de capital, como no original), cores medidas (branco 252, amarelo 253/226/0, vermelho 253/0/0),
# contorno preto 7 px + sombra. Gera um PNG RGBA por frame (1080x900, a colar em y=950) em karaoke/frames/.
# Uso (de projects/mentoria-spy/): python3 .../gerar-karaoke.py
import json, os, shutil, re
from PIL import Image, ImageDraw, ImageFont
P='gram-detect/criativos/super-gram-2026-09-19'; VAR=os.environ.get('VAR',''); T=json.load(open(f'{P}/molde/timeline{VAR}.json')); FPS=30; OFF=6.40; HOOK_FIM=T['hook_fim']; TOTAL=T['total']
FONTE=f'{P}/fontes/Oswald-Variable.ttf'; CAP=62          # altura da capital medida no original
W,H=1080,900; Y0=950                                       # a faixa gerada cobre y 950-1850 do quadro
BRANCO=(252,252,252,255); AMARELO=(253,226,0,255); VERMELHO=(253,0,0,255); PRETO=(0,0,0,255)
CONTORNO=7; SOMBRA=(4,5); TRACK=0; ESPACO=22; ENGORDA=1.6; LIMITE_LINHA=820   # 'WHEN SOMEONE TRIES' (665) cabe; 'THEY DELETED EVERYTHING' quebra, como no original
# ---- blocos automáticos: até 3 palavras, quebra no fim de frase (. ? !) e na vírgula; 4 sobrando viram 2+2; cores alternam ----
A,V='A','V'
_j=json.load(open(f'{P}/molde/vo{VAR}-16k.json')); _W=[w['word'].strip() for s_ in _j['segments'] for w in s_['words']]
def _frases():
    fr=[]; cur=[]
    for i,w in enumerate(_W):
        cur.append(i)
        if re.search(r"[.?!,]$",w): fr.append(cur); cur=[]
    if cur: fr.append(cur)
    return fr
BLOCOS=[]
for fr in _frases():
    while fr:
        n=3 if len(fr)!=4 else 2
        BLOCOS.append(fr[:n]); fr=fr[n:]
BLOCOS=[(ids,[(A if (bi+k)%2==0 else V) for k in range(len(ids))]) for bi,ids in enumerate(BLOCOS)]
# trechos em que o original NÃO mostra legenda (medido: o painel entra por cima / fim de frase sem legenda)
SEM_LEGENDA=[tuple(x) for x in T['sem_legenda']]
# altura do centro das capitais por layout (medida nas amostras): alta no bloco 1 (card embaixo), baixa nos demais
def y_centro(fr):
    if fr<T['card'][1]: return 1165   # abaixo da caixa rosa (y 862-1058) e acima do card (1369)
    if T['limpo'][0]<=fr<T['limpo'][1]: return 1641
    if fr>=T['final'][0]: return 1666
    return 1695
j=json.load(open(f'{P}/molde/vo{VAR}-16k.json')); Wd=[w for s in j['segments'] for w in s['words']]
import re
palavra=lambda i: re.sub(r"[^A-Z0-9']",'',Wd[i]['word'].strip().upper())   # o original não mostra pontuação
f0=lambda i: HOOK_FIM+int(round((OFF+Wd[i]['start'])*FPS))-int(round(OFF*FPS))
# frame de início de cada palavra no vídeo final (o clipe do avatar começa no frame 192 = 6,40 s)
ini=[HOOK_FIM+int(round(w['start']*FPS)) for w in Wd]
for sz in range(40,140):
    fnt=ImageFont.truetype(FONTE,sz); fnt.set_variation_by_name('Bold')
    b=fnt.getbbox('H')
    if b[3]-b[1]>=CAP: break
FNT=fnt; print(f'Oswald Bold {sz}px → capital {b[3]-b[1]}px')
def largura(txt): return sum(FNT.getlength(c) for c in txt)+TRACK*(len(txt)-1)
def desenha_palavra(d,x,y,txt,cor):
    for c in txt:
        for dx in range(-CONTORNO,CONTORNO+1):
            for dy in range(-CONTORNO,CONTORNO+1):
                if dx*dx+dy*dy<=CONTORNO*CONTORNO: d.text((x+dx+SOMBRA[0]*0.5,y+dy+SOMBRA[1]*0.5),c,font=FNT,fill=PRETO)
        x+=FNT.getlength(c)+TRACK
def desenha_fill(d,x,y,txt,cor):
    for c in txt:
        d.text((x,y),c,font=FNT,fill=cor,stroke_width=int(round(ENGORDA)),stroke_fill=cor); x+=FNT.getlength(c)+TRACK
def render_estado(idx_bloco,idx_dest,fr):
    ids,cores=BLOCOS[idx_bloco]; txts=[palavra(i) for i in ids]
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    # quebra em 2 linhas se não couber em ~980 px
    larg=[largura(t) for t in txts]; total=sum(larg)+ESPACO*(len(txts)-1)
    linhas=[list(range(len(txts)))] if total<=LIMITE_LINHA else [[0,1],[2]] if len(txts)==3 else [[0],[1]]
    yc=y_centro(fr)-Y0; bb=FNT.getbbox('H'); alt=bb[3]-bb[1]; nl=len(linhas); passo=alt+27
    for li,linha in enumerate(linhas):
        ltot=sum(larg[k] for k in linha)+ESPACO*(len(linha)-1); x=(W-ltot)/2
        y=yc-(nl-1)*passo/2+li*passo-bb[1]-alt/2
        for k in linha: desenha_palavra(d,x,y,txts[k],None); x+=larg[k]+ESPACO
        x=(W-ltot)/2
        for k in linha:
            cor=(AMARELO if cores[k]==A else VERMELHO) if k==idx_dest else BRANCO
            desenha_fill(d,x,y,txts[k],cor); x+=larg[k]+ESPACO
    return im
out=f'{P}/karaoke{VAR}/frames'; shutil.rmtree(out,ignore_errors=True); os.makedirs(out)
# mapa frame -> (bloco, palavra destacada)
estado={}
for bi,(ids,cores) in enumerate(BLOCOS):
    fim_bloco=ini[BLOCOS[bi+1][0][0]] if bi+1<len(BLOCOS) else TOTAL
    for k,i in enumerate(ids):
        a=ini[i]; b=ini[ids[k+1]] if k+1<len(ids) else fim_bloco
        for fr in range(a,min(b,TOTAL)): estado[fr]=(bi,k)
for a,b in SEM_LEGENDA:
    for fr in range(a,b): estado.pop(fr,None)
cache={}; vazio=Image.new('RGBA',(W,H),(0,0,0,0))
for fr in range(HOOK_FIM,TOTAL):
    e=estado.get(fr)
    if e is None: im=vazio
    else:
        key=(e[0],e[1],y_centro(fr))
        if key not in cache: cache[key]=render_estado(e[0],e[1],fr)
        im=cache[key]
    im.save(f'{out}/{fr:04d}.png',compress_level=1)
print(f'{TOTAL-HOOK_FIM} frames em {out} · {len(cache)} estados distintos · sem legenda em {SEM_LEGENDA}')
