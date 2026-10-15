#!/usr/bin/env python3
# montar-var4.py vN [vM…] — variação de AVATAR do Secret Revealed (Pruna p-video/avatar, 704x1280, sujeito centrado, rosto cheio como o original):
# roda ../remontar-secret.sh, confere (8 instantes + zoom do karaokê), conta silêncios, copia pra CRIATIVOS-PRONTOS/NN-… e escreve a linha no LEIA-ME. Custo zero.
import os, re, subprocess, sys
L='centerpag-detect/criativos/zap-secret-revealed-avatar-2026-09-10'; V=f'{L}/var4'; O='centerpag-detect/anuncios/secret-revealed-934941213003855.mp4'
FT='gram-detect/scripts/fonts/Inter-Bold.ttf'; S=os.environ.get('SCRATCH','/tmp')
SLUG={'v2':'homem-negro-oculos','v3':'homem-branco-loiro','v4':'homem-indiano','v5':'homem-branco-grisalho-oculos'}; NUM={'v2':21,'v3':22,'v4':23,'v5':24}
run=lambda c:subprocess.run(['ffmpeg','-nostdin','-v','error','-y']+c,check=True,capture_output=True)
for vid in sys.argv[1:]:
    clip=f'{V}/clipes/talking-head-{vid}.mp4'; slug=SLUG[vid]; out=f'{V}/pecas/zap-secret-revealed-{vid}-{slug}.mp4'
    r=subprocess.run(['bash',f'{L}/remontar-secret.sh',clip,out],capture_output=True,text=True); print([l for l in r.stdout.splitlines() if 'talking head' in l][-1] if r.returncode==0 else r.stderr[-800:])
    if r.returncode: raise SystemExit(1)
    files=[]
    for i,t in enumerate([0.5,2,4,8,12.2,20,25,30]):
        f=f'{S}/s4c-{vid}-{i}.png'; run(['-ss',str(t),'-i',O,'-ss',str(t),'-i',out,'-filter_complex',f"[0:v]scale=1080:1920:flags=neighbor,drawtext=fontfile={FT}:text='original {t}s':fontsize=40:fontcolor=yellow:box=1:boxcolor=black@0.7:boxborderw=8:x=20:y=300[a];[1:v]drawtext=fontfile={FT}:text='{vid} {t}s':fontsize=40:fontcolor=cyan:box=1:boxcolor=black@0.7:boxborderw=8:x=20:y=300[b];[a][b]hstack,scale=540:-1",'-frames:v','1',f]); files.append(f)
    inp=[]; [inp.extend(['-i',x]) for x in files]; run(inp+['-filter_complex','concat=n=8:v=1:a=0,tile=4x2:padding=6:color=0x0d0f13','-q:v','3',f'{V}/conferencia/{vid}-folha-8-instantes.jpg'])
    zs=[]
    for t in [2,12.2,20]:
        f=f'{S}/s4z-{vid}-{t}.png'; run(['-ss',str(t),'-i',O,'-ss',str(t),'-i',out,'-filter_complex',"[0:v]scale=1080:1920:flags=neighbor,crop=1080:150:0:1210[a];[1:v]crop=1080:150:0:1210[b];[a][b]vstack",'-frames:v','1',f]); zs.append(f)
    inp=[]; [inp.extend(['-i',x]) for x in zs]; run(inp+['-filter_complex','vstack=inputs=3','-q:v','3',f'{V}/conferencia/{vid}-zoom-karaoke.jpg'])
    sil=subprocess.run(['ffmpeg','-nostdin','-i',out,'-af','silencedetect=n=-35dB:d=0.4','-f','null','-'],capture_output=True,text=True).stderr.count('silence_start')
    dst=f'CRIATIVOS-PRONTOS/{NUM[vid]}-ZAP-secret-revealed-{vid}-{slug}.mp4'; subprocess.run(['cp',out,dst],check=True)
    p='CRIATIVOS-PRONTOS/LEIA-ME.md'; s=open(p).read()
    if f'| {NUM[vid]} |' not in s:
        row=f'| {NUM[vid]} | ZAP-secret-revealed-{vid}-{slug} | Spy Zap | Secret Revealed (20) com outro avatar (Pruna p-video/avatar): {slug.replace("-"," ")} — só o rosto muda | centerpag-detect/criativos/zap-secret-revealed-avatar-2026-09-10/var4/pecas |\n'
        s=s.replace('\nControles (não copiados)',row+'\nControles (não copiados)',1); open(p,'w').write(s)
    with open(f'{V}/resumo.tsv','a') as f: f.write(f'{vid}\t{slug}\t{sil}\t{os.path.basename(out)}\n')
    print(f'  ok -> {out} · silêncios≥0,4s {sil} · cópia {dst}')
