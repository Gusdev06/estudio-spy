#!/usr/bin/env python3
# montar-indianos.py <id> [<id>…] — variação de AVATAR do Secret Revealed com o molde do lote de 10/09:
# roda ../zap-secret-revealed-avatar-2026-09-10/remontar-secret.sh sobre o talking head novo (rosto cheio, faixa vermelha
# recortada do original, karaokê Arial Rounded MT Bold 86/tracking 7), confere contra o original, conta silêncios,
# copia pra CRIATIVOS-PRONTOS e escreve a linha no LEIA-ME. Custo zero. De projects/mentoria-spy/.
import os, subprocess, sys
L='centerpag-detect/criativos/zap-secret-revealed-avatar-2026-09-10'
V='centerpag-detect/criativos/zap-secret-revealed-indianos-2026-09-13'
O='centerpag-detect/anuncios/secret-revealed-934941213003855.mp4'
FT='gram-detect/scripts/fonts/Inter-Bold.ttf'; S=os.environ.get('SCRATCH','/tmp')
CAST={l.split('\t')[0]: l.rstrip('\n').split('\t')[1] for l in open(f'{V}/casting.tsv') if l.strip()}
NUM={'i1':47,'i2':48,'i3':49}
run=lambda c: subprocess.run(['ffmpeg','-nostdin','-v','error','-y']+c,check=True,capture_output=True)
for vid in sys.argv[1:]:
    clip=f'{V}/clipes/talking-head-{vid}.mp4'; slug=CAST[vid]
    out=f'{V}/pecas/zap-secret-revealed-{vid}-{slug}.mp4'; os.makedirs(f'{V}/pecas',exist_ok=True)
    r=subprocess.run(['bash',f'{L}/remontar-secret.sh',clip,out],capture_output=True,text=True)
    if r.returncode: print(r.stderr[-900:]); raise SystemExit(1)
    print([l for l in r.stdout.splitlines() if 'talking head' in l][-1])
    # folha original x peça em 8 instantes
    files=[]
    for i,t in enumerate([0.5,2,4,8,12.2,20,25,30]):
        f=f'{S}/si-{vid}-{i}.png'
        run(['-ss',str(t),'-i',O,'-ss',str(t),'-i',out,'-filter_complex',
             f"[0:v]scale=1080:1920:flags=neighbor,drawtext=fontfile={FT}:text='original {t}s':fontsize=40:fontcolor=yellow:box=1:boxcolor=black@0.7:boxborderw=8:x=20:y=300[a];"
             f"[1:v]drawtext=fontfile={FT}:text='{vid} {t}s':fontsize=40:fontcolor=cyan:box=1:boxcolor=black@0.7:boxborderw=8:x=20:y=300[b];[a][b]hstack,scale=540:-1",'-frames:v','1',f])
        files.append(f)
    inp=[]; [inp.extend(['-i',x]) for x in files]
    run(inp+['-filter_complex','concat=n=8:v=1:a=0,tile=4x2:padding=6:color=0x0d0f13','-q:v','3',f'{V}/conferencia/{vid}-folha-8-instantes.jpg'])
    # zoom do karaokê (original em cima, peça embaixo)
    zs=[]
    for t in [2,12.2,20]:
        f=f'{S}/sz-{vid}-{t}.png'
        run(['-ss',str(t),'-i',O,'-ss',str(t),'-i',out,'-filter_complex',
             "[0:v]scale=1080:1920:flags=neighbor,crop=1080:150:0:1210[a];[1:v]crop=1080:150:0:1210[b];[a][b]vstack",'-frames:v','1',f]); zs.append(f)
    inp=[]; [inp.extend(['-i',x]) for x in zs]
    run(inp+['-filter_complex','vstack=inputs=3','-q:v','3',f'{V}/conferencia/{vid}-zoom-karaoke.jpg'])
    sil=subprocess.run(['ffmpeg','-nostdin','-i',out,'-af','silencedetect=n=-35dB:d=0.4','-f','null','-'],capture_output=True,text=True).stderr.count('silence_start')
    dst=f'CRIATIVOS-PRONTOS/{NUM[vid]}-ZAP-secret-revealed-{slug}.mp4'; subprocess.run(['cp',out,dst],check=True)
    p='CRIATIVOS-PRONTOS/LEIA-ME.md'; s=open(p).read()
    if f'| {NUM[vid]} |' not in s:
        row=(f'| {NUM[vid]} | ZAP-secret-revealed-{slug} | Spy Zap | Secret Revealed (20) com mais um avatar indiano '
             f'(Pruna): {slug.replace("-"," ")} — só o rosto muda; áudio, faixa vermelha e karaokê do original | {V}/pecas |\n')
        s=s.replace('\nControles (não copiados)',row+'\nControles (não copiados)',1); open(p,'w').write(s)
    with open(f'{V}/resumo.tsv','a') as f: f.write(f'{vid}\t{slug}\t{sil}\t{os.path.basename(out)}\n')
    print(f'  ok -> {out} · silêncios>=0,4s {sil} · cópia {dst}')
