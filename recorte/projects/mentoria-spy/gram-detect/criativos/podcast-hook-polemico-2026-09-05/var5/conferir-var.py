#!/usr/bin/env python3
# conferir-var.py — folha com a cena 1 das 5 variações lado a lado (meio da cena 1 + último frame antes do corte), zoom das 5 caixas,
# silêncios ≥ 0,4 s por peça, duração. Saída var5/conferencia/. Uso de projects/mentoria-spy/.
import json, glob, os, re, subprocess
P='gram-detect/criativos/podcast-hook-polemico-2026-09-05'; V=f'{P}/var5'; C=f'{V}/conferencia'; FT='gram-detect/scripts/fonts/Inter-Bold.ttf'
S=os.environ.get('SCRATCH','/tmp'); run=lambda c:subprocess.run(['ffmpeg','-nostdin','-v','error','-y']+c,check=True,capture_output=True)
pecas=sorted(glob.glob(f'{V}/PODCAST-ZAP-v*.mp4')); mids=[]; caixas=[]; rows=[]
for f in pecas:
    vid=re.search(r'PODCAST-ZAP-(v\d)',f).group(1); T=json.load(open(f'{V}/molde/timeline-{vid}.json')); n1=T['scenes'][0]['out_frames']; tot=T['total_frames']
    sil=subprocess.run(['ffmpeg','-nostdin','-i',f,'-af','silencedetect=n=-35dB:d=0.4','-f','null','-'],capture_output=True,text=True).stderr.count('silence_start')
    dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
    rows.append((vid,os.path.basename(f),n1,tot,dur,sil))
    m=f'{S}/var-mid-{vid}.png'; run(['-i',f,'-vf',f"select='eq(n,{n1//2})+eq(n,{n1-1})',drawtext=fontfile={FT}:text='{vid} · cena 1 · {n1} fr ({n1/30:.2f}s) · {tot/30:.2f}s':fontsize=36:fontcolor=cyan:box=1:boxcolor=black@0.7:boxborderw=8:x=20:y=300,scale=300:-1,tile=2x1",'-frames:v','1',m]); mids.append(m)
    c=f'{S}/var-caixa-{vid}.png'; run(['-i',f,'-vf',f"select='eq(n,{n1//2})',crop=1080:260:0:830",'-frames:v','1',c]); caixas.append(c)
inp=[]; [inp.extend(['-i',x]) for x in mids]; run(inp+['-filter_complex',f"concat=n={len(mids)}:v=1:a=0,tile={len(mids)}x1:padding=6:color=0x0d0f13",'-q:v','3',f'{C}/folha-cena-1-5-variacoes.jpg'])
inp=[]; [inp.extend(['-i',x]) for x in caixas]; run(inp+['-filter_complex',f"concat=n={len(caixas)}:v=1:a=0,tile=1x{len(caixas)}:padding=4:color=0x0d0f13",'-q:v','3',f'{C}/caixas-5-variacoes.jpg'])
with open(f'{C}/resumo.tsv','w') as f:
    f.write('# var\tarquivo\tcena1_frames\ttotal_frames\tduracao_s\tsilencios>=0.4s\n')
    for r in rows: f.write('\t'.join(str(x) for x in r)+'\n')
for r in rows: print(f'{r[0]}: cena 1 {r[2]} fr ({r[2]/30:.2f}s) · total {r[3]} fr = {r[4]:.2f}s · silêncios ≥0,4s: {r[5]} · {r[1]}')
