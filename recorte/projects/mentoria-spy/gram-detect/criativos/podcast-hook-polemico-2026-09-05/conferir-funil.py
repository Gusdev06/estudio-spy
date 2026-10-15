#!/usr/bin/env python3
# Conferência da versão com funil: frame do meio de cada cena, fronteiras de estado (último frame antes × primeiro depois),
# zoom na costura do split (y 960) e legibilidade do funil/karaokê. Saída em conferencia/funil-*. Uso de projects/mentoria-spy/.
import json, subprocess, os
P='gram-detect/criativos/podcast-hook-polemico-2026-09-05'; V=f'{P}/PODCAST-ZAP-hook-faithful-man-funil.mp4'; C=f'{P}/conferencia'
FT='gram-detect/scripts/fonts/Inter-Bold.ttf'; T=json.load(open(f'{P}/molde/timeline.json')); SC=T['scenes']; FPS=T['fps']
def frame(n,out,vf=''):
    subprocess.run(['ffmpeg','-v','error','-y','-i',V,'-vf',f"select=eq(n\\,{n}){','+vf if vf else ''}",'-frames:v','1',out],check=True)
def lab(txt): return f"drawtext=fontfile={FT}:text='{txt}':fontsize=34:fontcolor=yellow:box=1:boxcolor=black@0.65:boxborderw=8:x=12:y=12"
def tile(files,cols,out,w=None):
    inp=[]; [inp.extend(['-i',f]) for f in files]
    sc=f'scale={w}:-1,' if w else ''
    subprocess.run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',f"concat=n={len(files)}:v=1:a=0,{sc}tile={cols}x{-(-len(files)//cols)}:padding=6:color=0x0d0f13",'-q:v','3',out],check=True)
ESTADO={1:'rosto cheio',2:'rosto cheio',3:'SPLIT restoring+mapa',4:'rosto cheio',5:'rosto cheio',6:'SPLIT formulario→backup',7:'SPLIT scan complete+setas'}
mids=[]
for i,s in enumerate(SC,1):
    n=s['out_start']+s['out_frames']//2; f=f'{C}/funil-cena-{i}.png'; frame(n,f,lab(f'cena {i} · f{n} · {n/FPS:.2f}s · {ESTADO[i]}')); mids.append(f)
tile(mids,7,f'{C}/funil-folha-cenas.jpg',360)
# fronteiras: último frame de cada estado × primeiro do seguinte, mais os 3 frames em que o painel 7 e as setas entram
pares=[(265,266),(427,428),(561,562),(747,748),(754,755)]; fr=[]
for a,b in pares:
    for n in (a,b):
        f=f'{C}/funil-borda-f{n}.png'; frame(n,f,lab(f'f{n} · {n/FPS:.3f}s')); fr.append(f)
tile(fr,10,f'{C}/funil-folha-estados.jpg',270)
# costura do split: faixa y 840-1080 em 2x, nos três splits (mostra o karaokê acima do painel e a fronteira em 960)
cost=[]
for n,t in [(300,'cena 3'),(600,'cena 6 landing'),(650,'cena 6 digitando'),(700,'cena 6 backup'),(800,'cena 7')]:
    f=f'{C}/funil-costura-f{n}.png'; frame(n,f,f"crop=1080:240:0:840,scale=2160:480,drawbox=y=240:h=2:w=iw:color=red@0.8:t=fill,{lab(t+f' · f{n} · y 840-1080 ×2 · linha vermelha = y 960')}"); cost.append(f)
tile(cost,1,f'{C}/funil-folha-costura.jpg')
# legibilidade do funil: painel de baixo (y 960-1920) em tamanho real, 5 momentos
leg=[]
for n,t in [(300,'restoring deleted data + TRACKING'),(600,'landing'),(650,'digitando (campo desfocado)'),(700,'accessing cloud backup'),(800,'scan complete + setas')]:
    f=f'{C}/funil-painel-f{n}.png'; frame(n,f,f"crop=1080:960:0:960,{lab(t+f' · f{n}')}"); leg.append(f)
tile(leg,5,f'{C}/funil-folha-paineis.jpg',432)
print('ok')
