#!/usr/bin/env python3
# montar-var4.py vN [vM…] — variação de AVATAR da Emilly: mede o rosto no clipe (coluna de luma na faixa dos olhos), calcula o --th-x que
# põe o rosto na metade esquerda (borda direita do rosto em x 375 sem cortar a bochecha esquerda), roda remontar-emilly.sh,
# conferência (8 instantes + linha do card), cópia pra CRIATIVOS-PRONTOS/NN-ZAP-emilly-avatar-vN-<slug>.mp4 + linha no LEIA-ME. Custo zero.
import os, re, subprocess, sys, numpy as np
L='centerpag-detect/criativos/zap-emilly-avatar-2026-09-09'; V=f'{L}/var4'; O='centerpag-detect/anuncios/emilly-bredoff-939122432559594.mp4'
FT='gram-detect/scripts/fonts/Inter-Bold.ttf'; S=os.environ.get('SCRATCH','/tmp')
SLUG={'v3':'homem-branco-barba-grisalha','v6':'homem-negro-careca-barba','v7':'homem-asiatico','v8':'homem-loiro-barba'}; NUM={'v3':16,'v6':17,'v7':18,'v8':19}   # correção do Maestro: voz masculina → 4 homens
run=lambda c,**k:subprocess.run(['ffmpeg','-nostdin','-v','error','-y']+c,check=True,capture_output=True,**k)
def face_bbox(clip,t=5.0):
    # frame escalado a 1080 de largura; faixa dos olhos/bochechas (y 520–820); rosto = trecho claro contíguo (buracos ≤ 20 px) que contém x 540
    d=subprocess.run(['ffmpeg','-nostdin','-v','error','-ss',str(t),'-i',clip,'-frames:v','1','-vf','scale=1080:-2','-f','rawvideo','-pix_fmt','gray','-'],capture_output=True).stdout
    h=len(d)//1080; a=np.frombuffer(d,np.uint8).reshape(h,1080).astype(float); col=a[520:820].mean(0); m=col>60; runs=[]; x=0
    while x<1080:
        if m[x]:
            s=x
            while x<1080 and (m[x] or (x+20<1080 and m[x:x+20].any())): x+=1
            runs.append((s,x-1))
        else: x+=1
    for s,e in runs:
        if s<=540<=e: return s,e,h
    s,e=max(runs,key=lambda r:r[1]-r[0]); return s,e,h
for arg in sys.argv[1:]:
    vid,_,force=arg.partition('=')   # vN=THX força o --th-x (ex.: pele escura engana o detector)
    clip=f'{V}/clipes/talking-head-{vid}.mp4'; slug=SLUG[vid]; out=f'{V}/pecas/zap-emilly-avatar-{vid}-{slug}.mp4'
    l,r,h=face_bbox(clip); thx=int(force) if force else max(375-r,-l); print(('FORÇADO ' if force else '')+f'{vid}: rosto x {l}–{r} (largura {r-l}) → --th-x {thx} (rosto vai pra x {l+thx}–{r+thx}; card começa em 375)')
    subprocess.run(['bash',f'{L}/remontar-emilly.sh',clip,out,'--th-x',str(thx)],check=True,capture_output=True)
    files=[]
    for i,t in enumerate([0.5,4,9.5,13,20,25,29.5,33]):
        f=f'{S}/v4c-{vid}-{i}.png'; run(['-ss',str(t),'-i',O,'-ss',str(t),'-i',out,'-filter_complex',f"[0:v]scale=1080:1440:flags=neighbor,pad=1080:1920:0:185:black,drawtext=fontfile={FT}:text='original {t}s':fontsize=40:fontcolor=yellow:box=1:boxcolor=black@0.7:boxborderw=8:x=20:y=20[a];[1:v]drawtext=fontfile={FT}:text='{vid} {t}s':fontsize=40:fontcolor=cyan:box=1:boxcolor=black@0.7:boxborderw=8:x=20:y=20[b];[a][b]hstack,scale=540:-1",'-frames:v','1',f]); files.append(f)
    inp=[]; [inp.extend(['-i',x]) for x in files]; run(inp+['-filter_complex','concat=n=8:v=1:a=0,tile=4x2:padding=6:color=0x0d0f13','-q:v','3',f'{V}/conferencia/{vid}-folha-8-instantes.jpg'])
    run(['-ss','4','-i',out,'-frames:v','1','-vf',f"crop=1080:1200:0:250,drawbox=x=375:y=0:w=2:h=ih:c=red@0.8:t=fill,drawtext=fontfile={FT}:text='{vid} · rosto x {l+thx}–{r+thx} · card 375':fontsize=36:fontcolor=cyan:box=1:boxcolor=black@0.7:boxborderw=8:x=20:y=20",'-q:v','3',f'{V}/conferencia/{vid}-zoom-linha-card.jpg'])
    sil=subprocess.run(['ffmpeg','-nostdin','-i',out,'-af','silencedetect=n=-35dB:d=0.4','-f','null','-'],capture_output=True,text=True).stderr.count('silence_start')
    dst=f'CRIATIVOS-PRONTOS/{NUM[vid]}-ZAP-emilly-avatar-{vid}-{slug}.mp4'; subprocess.run(['cp',out,dst],check=True)
    p='CRIATIVOS-PRONTOS/LEIA-ME.md'; s=open(p).read()
    if f'| {NUM[vid]} |' not in s:
        row=f'| {NUM[vid]} | ZAP-emilly-avatar-{vid}-{slug} | Spy Zap | Emilly (15) com outro avatar: {slug.replace("-"," ")} — só o rosto muda | centerpag-detect/criativos/zap-emilly-avatar-2026-09-09/var4/pecas |\n'
        s=s.replace('\nControles (não copiados)',row+'\nControles (não copiados)',1); open(p,'w').write(s)
    with open(f'{V}/resumo.tsv','a') as f: f.write(f'{vid}\t{slug}\t{l}\t{r}\t{thx}\t{sil}\t{os.path.basename(out)}\n')
    print(f'  ok -> {out} · silêncios≥0,4s {sil} · cópia {dst}')
