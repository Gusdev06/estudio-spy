#!/usr/bin/env python3
# conferir-emilly.py [peca.mp4] — folha original (×3, y 185) × peça em 8 instantes + zoom no card/caixa + CTA. Saída conferencia/. Custo zero.
import os, subprocess, sys
L='centerpag-detect/criativos/zap-emilly-avatar-2026-09-09'; C=f'{L}/conferencia'; O='centerpag-detect/anuncios/emilly-bredoff-939122432559594.mp4'
A=sys.argv[1] if len(sys.argv)>1 else f'{L}/pecas/zap-emilly-avatar.mp4'; FT='gram-detect/scripts/fonts/Inter-Bold.ttf'; S=os.environ.get('SCRATCH','/tmp')
run=lambda c:subprocess.run(['ffmpeg','-nostdin','-v','error','-y']+c,check=True,capture_output=True)
lab=lambda t,col:f"drawtext=fontfile={FT}:text='{t}':fontsize=40:fontcolor={col}:box=1:boxcolor=black@0.7:boxborderw=8:x=20:y=20"
files=[]
for i,t in enumerate([0.5,4,9.5,13,20,25,29.5,33]):
    f=f'{S}/emc-{i}.png'; run(['-ss',str(t),'-i',O,'-ss',str(t),'-i',A,'-filter_complex',f"[0:v]scale=1080:1440:flags=neighbor,pad=1080:1920:0:185:black,{lab(f'original {t}s (x3)','yellow')}[a];[1:v]{lab(f'peca {t}s','cyan')}[b];[a][b]hstack,scale=540:-1",'-frames:v','1',f]); files.append(f)
inp=[]; [inp.extend(['-i',x]) for x in files]; run(inp+['-filter_complex','concat=n=8:v=1:a=0,tile=4x2:padding=6:color=0x0d0f13','-q:v','3',f'{C}/folha-8-instantes.jpg'])
run(['-ss','4','-i',A,'-frames:v','1','-vf','crop=1080:1200:0:250,drawbox=x=375:y=0:w=2:h=ih:c=red@0.8:t=fill',f'-q:v','3',f'{C}/zoom-caixa-card-t4.jpg'])
run(['-ss','20','-i',O,'-ss','20','-i',A,'-filter_complex',"[0:v]scale=1080:1440:flags=neighbor,pad=1080:1920:0:185:black,crop=1080:1000:0:250[a];[1:v]crop=1080:1000:0:250[b];[a][b]hstack",'-frames:v','1','-q:v','3',f'{C}/zoom-card-t20.jpg'])
run(['-ss','29.0','-i',A,'-ss','29.3','-i',A,'-ss','31','-i',A,'-filter_complex',"[0:v]scale=360:-1[a];[1:v]scale=360:-1[b];[2:v]scale=360:-1[c];[a][b][c]hstack=inputs=3",'-frames:v','1','-q:v','3',f'{C}/corte-cta-29.0-29.3-31.jpg'])
sil=subprocess.run(['ffmpeg','-nostdin','-i',A,'-af','silencedetect=n=-35dB:d=0.4','-f','null','-'],capture_output=True,text=True).stderr
import re; print('silêncios ≥0,4s na peça:',re.findall(r'silence_start: ([\d.]+)',sil),'(esperado só o CTA, ~28,7 s)')
print('ok ->',C)
