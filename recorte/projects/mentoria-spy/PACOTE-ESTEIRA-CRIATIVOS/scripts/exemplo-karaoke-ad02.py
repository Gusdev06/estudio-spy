#!/usr/bin/env python3
# Karaokê do AD02-H2 RECONSTRUÍDO (não recortado): blocos e cores lidos frame a frame do original (karaoke/folha-*.jpg),
# tempos por palavra do whisper (molde/vo-16k.json), fonte Oswald Bold (a mais próxima em largura: "WHEN SOMEONE TRIES"
# = 665 px a 62 px de capital, como no original), cores medidas (branco 252, amarelo 253/226/0, vermelho 253/0/0),
# contorno preto 7 px + sombra. Gera um PNG RGBA por frame (1080x900, a colar em y=950) em karaoke/frames/.
# Uso (de projects/mentoria-spy/): python3 .../gerar-karaoke.py
import json, os, shutil
from PIL import Image, ImageDraw, ImageFont
P='gram-detect/criativos/ad02-h2-reconstrucao-2026-09-17'; FPS=30; OFF=6.40; HOOK_FIM=192; TOTAL=1090
FONTE=f'{P}/fontes/Oswald-Variable.ttf'; CAP=62          # altura da capital medida no original
W,H=1080,900; Y0=950                                       # a faixa gerada cobre y 950-1850 do quadro
BRANCO=(252,252,252,255); AMARELO=(253,226,0,255); VERMELHO=(253,0,0,255); PRETO=(0,0,0,255)
CONTORNO=7; SOMBRA=(4,5); TRACK=0; ESPACO=22; ENGORDA=1.6; LIMITE_LINHA=820   # 'WHEN SOMEONE TRIES' (665) cabe; 'THEY DELETED EVERYTHING' quebra, como no original
# ---- blocos lidos do original: (índices das palavras, cores por palavra) ----
A,V='A','V'
BLOCOS=[
 ([0,1,2],[A,V,A]), ([3],[V]), ([4,5,6],[A,V,A]), ([7,8],[V,A]), ([9,10,11],[A,V,A]), ([12,13,14],[V,A,V]), ([15],[A]),
 ([16,17,18],[A,V,A]), ([19,20,21],[V,A,V]), ([22,23,24],[A,V,A]), ([25,26],[V,A]), ([27,28,29],[A,V,A]), ([30,31,32],[V,A,V]),
 ([33,34,35],[A,V,A]), ([36,37,38],[A,V,A]), ([39,40,41],[V,A,V]), ([42,43,44],[A,V,A]), ([45,46,47],[V,A,V]),
 ([48,49,50],[A,V,A]), ([51],[V]), ([52,53,54],[A,V,A]), ([55,56,57],[V,A,V]), ([58,59],[A,V]), ([60,61,62],[A,V,A]),
 ([63],[V]), ([64,65,66],[A,V,A]), ([67,68,69],[V,A,V]), ([70,71,72],[A,V,A]), ([73,74,75],[A,V,A]), ([76,77,78],[V,A,V]),
 ([81,82,83],[A,V,A]), ([84,85,86],[V,A,V]), ([87,88,89],[A,V,A]),
]
# trechos em que o original NÃO mostra legenda (medido: o painel entra por cima / fim de frase sem legenda)
SEM_LEGENDA=[(608,632),(966,1004)]
# altura do centro das capitais por layout (medida nas amostras): alta no bloco 1 (card embaixo), baixa nos demais
def y_centro(fr):
    if fr<312: return 1113
    if 458<=fr<608: return 1641
    if fr>=967: return 1666
    return 1695
j=json.load(open(f'{P}/molde/vo-16k.json')); Wd=[w for s in j['segments'] for w in s['words']]
import re
palavra=lambda i: re.sub(r"[^A-Z0-9']",'',Wd[i]['word'].strip().upper())   # o original não mostra pontuação
f0=lambda i: HOOK_FIM+int(round((OFF+Wd[i]['start'])*FPS))-int(round(OFF*FPS))
# frame de início de cada palavra no vídeo final (o clipe do avatar começa no frame 192 = 6,40 s)
ini=[int(round((OFF+w['start'])*FPS)) for w in Wd]
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
out=f'{P}/karaoke/frames'; shutil.rmtree(out,ignore_errors=True); os.makedirs(out)
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
