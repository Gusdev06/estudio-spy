#!/usr/bin/env python3
# cortar-pausas.py <clipe.mp4> <saida.mp4> [--blocos molde/blocos.tsv] — regra de ritmo (Gusta, 05/09): todo silêncio ≥ 0,4 s
# (silencedetect −35 dB) fica com 0,25 s, cortando vídeo e áudio juntos (mantém o lipsync). Escreve molde/pausas.json com os
# trechos removidos e, se --blocos, remapeia as fronteiras do blocos.tsv pro tempo novo (guarda o original em blocos-com-pausas.tsv).
import json, os, re, subprocess, sys
src,out=sys.argv[1],sys.argv[2]; bl=sys.argv[4] if len(sys.argv)>4 and sys.argv[3]=='--blocos' else None
PAUSA_MAX=float(os.environ.get('PAUSA_MAX',0.4)); PAUSA_KEEP=float(os.environ.get('PAUSA_KEEP',0.25)); DB=os.environ.get('DB','-35')
L=os.path.dirname(os.path.abspath(sys.argv[0])); M=f'{L}/molde'
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
log=subprocess.run(['ffmpeg','-nostdin','-i',src,'-af',f'silencedetect=n={DB}dB:d={PAUSA_MAX}','-f','null','-'],capture_output=True,text=True).stderr
st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',log)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',log)]
if len(en)<len(st): en.append(dur)
sil=list(zip(st,en)); removed=[]
for a,b in sil:
    d=b-a
    if d<PAUSA_MAX: continue
    if a<0.05: removed.append((0.0,b-PAUSA_KEEP))                  # silêncio inicial: deixa só o respiro
    elif b>dur-0.05: removed.append((a+PAUSA_KEEP,dur))             # silêncio final
    else: k=PAUSA_KEEP/2; removed.append((a+k,b-k))                 # no meio: tira o miolo, deixa PAUSA_KEEP
keep=[]; t=0.0
for a,b in removed: keep.append((t,a)); t=b
keep.append((t,dur)); keep=[(a,b) for a,b in keep if b-a>0.01]
tot=sum(b-a for a,b in removed); new=dur-tot
print(f'{len(sil)} silêncios ≥ {PAUSA_MAX}s · {len(removed)} cortes · −{tot:.2f}s · {dur:.2f} → {new:.2f}s')
json.dump(dict(src=src,dur=dur,new=new,removed=removed,keep=keep,pausa_max=PAUSA_MAX,pausa_keep=PAUSA_KEEP,db=DB),open(f'{M}/pausas.json','w'),indent=1)
fc=[]; labels=''
for i,(a,b) in enumerate(keep):
    fc.append(f"[0:v]trim=start={a:.4f}:end={b:.4f},setpts=PTS-STARTPTS[v{i}];[0:a]atrim=start={a:.4f}:end={b:.4f},asetpts=PTS-STARTPTS[a{i}];"); labels+=f'[v{i}][a{i}]'
fc.append(f"{labels}concat=n={len(keep)}:v=1:a=1[v][a]")
subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-i',src,'-filter_complex',''.join(fc),'-map','[v]','-map','[a]','-c:v','libx264','-preset','slow','-crf','12','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k',out],check=True)
print('ok ->',out)
def remap(t):
    r=0.0
    for a,b in removed:
        if t>=b: r+=b-a
        elif t>a: r+=t-a
    return t-r
if bl:
    orig=f'{M}/blocos-com-pausas.tsv'
    if not os.path.exists(orig): os.rename(bl,orig)
    lines=[]
    for l in open(orig):
        if l.startswith('#') or not l.strip(): lines.append(l); continue
        c=l.rstrip('\n').split('\t'); c[0]=f'{remap(float(c[0])):.2f}'; c[1]=f'{remap(float(c[1])):.2f}'; lines.append('\t'.join(c)+'\n')
    lines.insert(0,f'# FRONTEIRAS REMAPEADAS por cortar-pausas.py ({len(removed)} cortes, −{tot:.2f}s; original em blocos-com-pausas.tsv)\n')
    open(bl,'w').write(''.join(lines)); print('blocos remapeados ->',bl)
    for l in lines:
        if not l.startswith('#') and l.strip(): c=l.split('\t'); print(f'  {c[0]}–{c[1]} {c[2]}')
