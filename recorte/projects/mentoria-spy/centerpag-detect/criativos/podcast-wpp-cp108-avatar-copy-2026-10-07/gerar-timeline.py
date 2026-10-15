#!/usr/bin/env python3
# Timeline de uma copy: apara o silêncio de cada fala, junta com pausas de 0,12 s (mesmo papel) e 0,24 s (troca de papel),
# grava vo.wav, molde/<k>/linhas.json + blocos.json (b1,b3,b4,b5,b6,b8 = falas com clipe de rosto) e o mp3 de cada bloco.
# Uso (de projects/mentoria-spy/): python3 .../gerar-timeline.py 170
import json, os, subprocess, sys
D='centerpag-detect/criativos/podcast-wpp-cp108-avatar-copy-2026-10-07'; k=sys.argv[1]
A=f'{D}/audio/{k}'; M=f'{D}/molde/{k}'; os.makedirs(M,exist_ok=True)
rows=[l.rstrip('\n').split('\t') for l in open(f'{D}/roteiro-{k}.tsv') if l.strip()]
SR=44100; dur=lambda f: float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
TRIM='silenceremove=stop_periods=-1:stop_duration=0.38:stop_threshold=-40dB:stop_silence=0.32,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.03,areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.06,areverse'
linhas=[]; t=0.0; prev=None; parts=[]
for i,p,txt in rows:
    w=f'{A}/t{i}.wav'
    subprocess.run(['ffmpeg','-hide_banner','-v','error','-y','-i',f'{A}/l{i}.mp3','-af',TRIM,'-ar',str(SR),'-ac','1',w],check=True)
    if prev is not None:
        pa=0.12 if p==prev else 0.24; parts.append(('sil',pa)); t+=pa
    d=dur(w); linhas.append({'i':int(i),'papel':p,'txt':txt,'ini':round(t,3),'fim':round(t+d,3)}); parts.append(('w',w)); t+=d; prev=p
# concat
inp=[];fc='';n=0;lab=''
for kind,v in parts:
    if kind=='w': inp+=['-i',v]
    else: inp+=['-f','lavfi','-t',f'{v}','-i',f'anullsrc=r={SR}:cl=mono']
    lab+=f'[{n}:a]'; n+=1
subprocess.run(['ffmpeg','-hide_banner','-v','error','-y']+inp+['-filter_complex',f'{lab}concat=n={n}:v=0:a=1[a]','-map','[a]','-ar',str(SR),'-ac','1',f'{A}/vo.wav'],check=True)
subprocess.run(['ffmpeg','-hide_banner','-v','error','-y','-i',f'{A}/vo.wav','-ar','16000','-ac','1',f'{M}/vo-16k.wav'],check=True)
json.dump(linhas,open(f'{M}/linhas.json','w'),indent=1,ensure_ascii=False)
bl={}
for l in linhas:
    if l['i'] in (1,3,4,5,6,8):
        b=f"b{l['i']}"; bl[b]={'papel':l['papel'],'ini':l['ini'],'fim':l['fim']}
        subprocess.run(['ffmpeg','-hide_banner','-v','error','-y','-i',f"{A}/t{l['i']}.wav",'-c:a','libmp3lame','-b:a','192k',f'{A}/{b}.mp3'],check=True)
json.dump(bl,open(f'{M}/blocos.json','w'),indent=1)
for l in linhas: print(l['i'],l['papel'],l['ini'],l['fim'],round(l['fim']-l['ini'],2))
print('vo',round(dur(f'{A}/vo.wav'),3),'· clipes',round(sum(v['fim']-v['ini'] for v in bl.values()),2),'s')
