#!/usr/bin/env python3
# Ritmo: todo silêncio ≥ 0,3 s (−35 dB) fica com 0,25 s (respiro ≤ 0,3 s). Cópia do cortar-pausas-audio.py de ad02-h2-zap com limiar 0,3.
# pra que o clipe do Pruna já nasça no ritmo certo. Uso: python3 cortar-pausas-audio.py <in.mp3> <out.wav>
import re,subprocess,sys,json
src,out=sys.argv[1],sys.argv[2]; PMAX,KEEP=0.3,0.25
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
log=subprocess.run(['ffmpeg','-nostdin','-i',src,'-af',f'silencedetect=n=-35dB:d={PMAX}','-f','null','-'],capture_output=True,text=True).stderr
st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',log)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',log)]
if len(en)<len(st): en.append(dur)
removed=[]
for a,b in zip(st,en):
    if a<0.05: removed.append((0.0,b-KEEP))
    elif b>dur-0.05: removed.append((a+KEEP,dur))
    else: removed.append((a+KEEP/2,b-KEEP/2))
keep=[]; t=0.0
for a,b in removed: keep.append((t,a)); t=b
keep.append((t,dur)); keep=[(a,b) for a,b in keep if b-a>0.01]
fc=''.join(f'[0:a]atrim={a:.4f}:{b:.4f},asetpts=PTS-STARTPTS[s{i}];' for i,(a,b) in enumerate(keep))+''.join(f'[s{i}]' for i in range(len(keep)))+f'concat=n={len(keep)}:v=0:a=1[a]'
subprocess.run(['ffmpeg','-hide_banner','-v','error','-y','-i',src,'-filter_complex',fc,'-map','[a]','-ar','44100','-ac','1',out],check=True)
json.dump({'removidos':removed,'mantidos':keep},open(out.rsplit('.',1)[0]+'-pausas.json','w'),indent=1)
print(f'{len(removed)} pausas cortadas, -{sum(b-a for a,b in removed):.2f} s')
