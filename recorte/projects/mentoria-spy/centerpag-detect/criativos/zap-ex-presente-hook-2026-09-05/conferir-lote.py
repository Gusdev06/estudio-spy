#!/usr/bin/env python3
# conferir-lote.py [peca-A.mp4] — folha 8 instantes campeão × peça (fases equivalentes), zoom matte/card/karaokê/CTA, mattes A/B/C.
# Saída em conferencia/lote-*. Uso de projects/mentoria-spy/. Custo zero.
import subprocess, sys, os
L='centerpag-detect/criativos/zap-ex-presente-hook-2026-09-05'; C=f'{L}/conferencia'; W='centerpag-detect/escalados/whatsapp/01-esther-vicman-1762552938111855.mp4'
A=sys.argv[1] if len(sys.argv)>1 else f'{L}/pecas/zap-ex-presente-A.mp4'; FT='gram-detect/scripts/fonts/Inter-Bold.ttf'
S=os.environ.get('SCRATCH','/tmp'); run=lambda c:subprocess.run(['ffmpeg','-nostdin','-v','error','-y']+c,check=True)
lab=lambda t,col:f"drawtext=fontfile={FT}:text='{t}':fontsize=44:fontcolor={col}:box=1:boxcolor=black@0.7:boxborderw=10:x=20:y=300"
# instantes: campeão (fase) × peça (mesma fase): F1 · F2 formulário · F2 acesso · F2 fim · F3 · F4 · F4 · F5
pares=[(2,2.5,'F1 chats'),(12,7.0,'F2 formulario'),(20,11.0,'F2 accessing'),(28,16.5,'F2 fim, rosto'),(33,19.0,'F3 card cheio'),(45,23.5,'F4 payoff'),(47,26.7,'F4 dating'),(53,29.5,'F5 CTA')]
files=[]
for i,(tc,tp,nome) in enumerate(pares):
    f=f'{S}/lote-par-{i}.png'
    run(['-ss',str(tc),'-i',W,'-ss',str(tp),'-i',A,'-filter_complex',f"[0:v]scale=1080:1920:flags=neighbor,{lab(f'campeao {tc}s · {nome}','yellow')}[a];[1:v]{lab(f'peca A {tp}s','cyan')}[b];[a][b]hstack,scale=540:-1",'-frames:v','1',f]); files.append(f)
inp=[]; [inp.extend(['-i',f]) for f in files]
run(inp+['-filter_complex',f"concat=n={len(files)}:v=1:a=0,tile=4x2:padding=6:color=0x0d0f13",'-q:v','3',f'{C}/lote-folha-8-instantes.jpg'])
# zoom: matte (y 0-330), card (y 1200-1920) em t=13, karaokê cheio em t=24,5 (y 850-1050), CTA em t=35
run(['-ss','13','-i',W,'-ss','11','-i',A,'-filter_complex',"[0:v]scale=1080:1920:flags=neighbor,crop=1080:720:0:1200[a];[1:v]crop=1080:720:0:1200[b];[a][b]hstack",'-frames:v','1','-q:v','3',f'{C}/lote-zoom-card-t11.jpg'])
run(['-ss','33','-i',W,'-ss','19','-i',A,'-filter_complex',"[0:v]scale=1080:1920:flags=neighbor,crop=1080:300:0:800[a];[1:v]crop=1080:300:0:800[b];[a][b]vstack",'-frames:v','1','-q:v','3',f'{C}/lote-zoom-karaoke-cheio.jpg'])
run(['-ss','53','-i',W,'-ss','29.5','-i',A,'-filter_complex',"[0:v]scale=1080:1920:flags=neighbor[a];[1:v]copy[b];[a][b]hstack,scale=1080:-1",'-frames:v','1','-q:v','3',f'{C}/lote-zoom-cta.jpg'])
P=A.rsplit('-A.mp4',1)[0]
run(['-ss','2','-i',f'{P}-A.mp4','-ss','2','-i',f'{P}-B.mp4','-ss','2','-i',f'{P}-C.mp4','-filter_complex',"[0:v]crop=1080:330:0:0[a];[1:v]crop=1080:330:0:0[b];[2:v]crop=1080:330:0:0[c];[a][b][c]vstack=inputs=3",'-frames:v','1','-q:v','3',f'{C}/lote-mattes-abc.jpg'])
# meio de cada bloco da peça
bl=[]
for l in open(f'{L}/molde/blocos.tsv'):
    if l.startswith('#') or not l.strip(): continue
    c=l.split('\t'); bl.append((float(c[0]),float(c[1]),c[2]))
files=[]
for i,(a,b,fase) in enumerate(bl):
    f=f'{S}/lote-blk-{i}.png'; run(['-ss',str((a+b)/2),'-i',A,'-frames:v','1','-vf',f"{lab(f'{a:.2f}–{b:.2f} s · {fase}','cyan').replace('fontsize=44','fontsize=40')},scale=300:-1",f]); files.append(f)
inp=[]; [inp.extend(['-i',f]) for f in files]
run(inp+['-filter_complex',f"concat=n={len(files)}:v=1:a=0,tile=6x2:padding=6:color=0x0d0f13",'-q:v','3',f'{C}/lote-folha-blocos.jpg'])
print('ok ->',C,'lote-folha-8-instantes · lote-zoom-card-t11 · lote-zoom-karaoke-cheio · lote-zoom-cta · lote-mattes-abc · lote-folha-blocos')
