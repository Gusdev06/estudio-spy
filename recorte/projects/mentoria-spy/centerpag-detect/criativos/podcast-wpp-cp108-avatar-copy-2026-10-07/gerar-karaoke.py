#!/usr/bin/env python3
# Karaokê do clone do podcast WPP (57 s) reconstruído: caixa alta branca com CAIXA ROXA arredondada na palavra falada
# (cor medida no original: 105,18,209; texto branco; capital 39 px; faixa y 967-1031; centralizado em x=360).
# Blocos de até 4 palavras quebrando no fim de frase, 1 PNG por frame (720x140 colado em y=935). De projects/mentoria-spy/.
import json, os, re, shutil, sys, difflib
from PIL import Image, ImageDraw, ImageFont
P='centerpag-detect/criativos/podcast-wpp-cp108-avatar-copy-2026-10-07'; K=sys.argv[1]   # uso: gerar-karaoke.py 170
FPS=30; W,H,Y0=720,140,935; CAP=37; FONTE='gram-detect/scripts/fonts/Poppins-Bold.ttf'
ROXO=(105,18,209,255); BRANCO=(252,252,252,255); CY=999-Y0   # centro das capitais dentro da faixa
j=json.load(open(f'{P}/molde/{K}/vo-16k.json')); WH=[w for s in j['segments'] for w in s['words']]
# o texto exibido é o do ROTEIRO (o whisper ouve 'a link', 'back up'); os tempos vêm do whisper, alinhados por difflib
RT=' '.join(l.rstrip('\n').split('\t')[2] for l in open(f'{P}/roteiro-{K}.tsv') if l.strip()).split()
nz=lambda w: re.sub(r"[^a-z0-9]",'',w.lower())
Wd=[None]*len(RT); sm=difflib.SequenceMatcher(None,[nz(w['word']) for w in WH],[nz(w) for w in RT],autojunk=False)
for tag,a1,a2,b1,b2 in sm.get_opcodes():
    if tag=='insert': continue
    if tag=='delete': continue
    na,nb=a2-a1,b2-b1; ini=WH[a1]['start']; fim=WH[a2-1]['end']
    for q in range(nb):
        if na==nb: Wd[b1+q]={'word':RT[b1+q],'start':WH[a1+q]['start'],'end':WH[a1+q]['end']}
        else: Wd[b1+q]={'word':RT[b1+q],'start':ini+(fim-ini)*q/nb,'end':ini+(fim-ini)*(q+1)/nb}
assert all(Wd), [RT[i] for i,w in enumerate(Wd) if w is None]
for a,b in sm.get_opcodes() and [(o[3],o[4]) for o in sm.get_opcodes() if o[0]!='equal']: print('ajuste:',' '.join(RT[a:b]))
palavra=lambda w: re.sub(r"[^A-Z0-9']",'',w.strip().upper())
for sz in range(30,90):
    f=ImageFont.truetype(FONTE,sz); b=f.getbbox('H')
    if b[3]-b[1]>=CAP: break
FNT=f; BB=FNT.getbbox('H'); ALT=BB[3]-BB[1]
TOTAL=int(round((Wd[-1]['end']+0.15)*FPS))
# blocos de até 4 palavras, quebrando em . ? !
LIMITE=640   # largura máxima da linha (o original nunca passa disso); quebra antes de estourar
def larg(ids):
    ts=[palavra(Wd[i]['word']) for i in ids]
    return sum(FNT.getlength(t) for t in ts)+FNT.getlength(' ')*(len(ts)-1)
BLOCOS=[]; cur=[]
for i,w in enumerate(Wd):
    if cur and (len(cur)==4 or larg(cur+[i])>LIMITE): BLOCOS.append(cur); cur=[]
    cur.append(i)
    if re.search(r'[.?!]$',w['word'].strip()) or i==len(Wd)-1: BLOCOS.append(cur); cur=[]
BLOCOS=[b for b in BLOCOS if b]
estado={}
for bi,ids in enumerate(BLOCOS):
    fim=int(round(Wd[BLOCOS[bi+1][0]]['start']*FPS)) if bi+1<len(BLOCOS) else TOTAL
    for k,i in enumerate(ids):
        a=int(round(Wd[i]['start']*FPS)); b=int(round(Wd[ids[k+1]]['start']*FPS)) if k+1<len(ids) else fim
        for fr in range(a,min(b,TOTAL)): estado[fr]=(bi,k)
out=f'{P}/c{K}/karaoke/frames'; shutil.rmtree(out,ignore_errors=True); os.makedirs(out)
cache={}; vazio=Image.new('RGBA',(W,H),(0,0,0,0))
def render(bi,k):
    ids=BLOCOS[bi]; txts=[palavra(Wd[i]['word']) for i in ids]
    larg=[FNT.getlength(t) for t in txts]; esp=FNT.getlength(' ')
    total=sum(larg)+esp*(len(txts)-1); x=(W-total)/2
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    y=CY-ALT/2-BB[1]
    for i,(t,lw) in enumerate(zip(txts,larg)):
        if i==k: d.rounded_rectangle([x-7,CY-28,x+lw+7,CY+28],radius=5,fill=ROXO)
        d.text((x,y),t,font=FNT,fill=BRANCO,stroke_width=2,stroke_fill=(10,10,10,200) if i!=k else ROXO)
        x+=lw+esp
    return im
for fr in range(TOTAL):
    e=estado.get(fr)
    if e is None: im=vazio
    else:
        if e not in cache: cache[e]=render(*e)
        im=cache[e]
    im.save(f'{out}/{fr:04d}.png',compress_level=1)
print(f'{TOTAL} frames · {len(BLOCOS)} blocos · fonte {sz}px capital {ALT}px')
