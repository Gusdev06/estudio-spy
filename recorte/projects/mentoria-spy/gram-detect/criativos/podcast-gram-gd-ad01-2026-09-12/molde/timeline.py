#!/usr/bin/env python3
# Timeline do podcast Gram com REMOÇÃO DE PAUSAS (regra do Gusta, 05/09): cada cena = clipe cortado no fim da última palavra + RESPIRO,
# e todo silêncio >= PAUSA_MAX dentro da fala é reduzido a PAUSA_KEEP (vídeo e áudio cortados juntos → lipsync mantido).
# Fonte dos tempos: whisper no áudio embutido do clipe (audio/clip-cena-N.json) + ffmpeg silencedetect (-35 dB).
# Escreve molde/timeline.json e molde/timeline.tsv. Uso (de projects/mentoria-spy/): python3 timeline.py [pasta_dos_clipes]
import subprocess, os, sys, json, re
P='gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12'; FPS=30
RESP=float(os.environ.get('RESPIRO','0.3')); PMAX=float(os.environ.get('PAUSA_MAX','0.4')); PKEEP=float(os.environ.get('PAUSA_KEEP','0.25'))
CL=sys.argv[1] if len(sys.argv)>1 else f'{P}/clipes'
AUD=os.environ.get('AUD',f'{P}/audio')   # variante: pasta com clip-cena-1.json próprio
def silences(c):
    r=subprocess.run(['ffmpeg','-hide_banner','-v','info','-i',c,'-af',f'silencedetect=n=-35dB:d={PMAX}','-f','null','-'],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',r)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',r)]
    return list(zip(st,en+[9e9]*(len(st)-len(en))))
scenes=[]; f0=0; log=[]
for i in range(1,8):
    c=f'{CL}/cena-{i}.mp4'; js=f'{AUD}/clip-cena-{i}.json'
    cd=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',c],capture_output=True,text=True).stdout.strip())
    if os.path.exists(js):
        w=[x for s in json.load(open(js))['segments'] for x in s['words']]; w0=w[0]['start']; wend=w[-1]['end']
    else: w0=0.0; wend=cd-RESP
    fim=min(wend+RESP,cd)
    removed=[]
    for a,b in silences(c):
        b=min(b,cd)
        if a<0.05 and b>0.25 and b<wend: removed.append((0.1,round(b-0.05,3)))            # silêncio inicial: fica 0,1 s
        elif a>0.05 and b<=wend+0.05 and (b-a)>=PMAX: removed.append((round(a+PKEEP,3),round(b,3)))  # pausa interna: fica PKEEP
    removed=[r for r in removed if r[1]-r[0]>0.05]
    segs=[]; cur=0.0
    for a,b in removed:
        if a>cur: segs.append((cur,a))
        cur=b
    if fim>cur: segs.append((cur,fim))
    frames=[max(1,int(round((e-s)*FPS))) for s,e in segs]; tot=sum(frames)
    scenes.append({'cena':i,'clip':c,'clip_s':cd,'fala_fim':wend,'corte':fim,'segments':[[s,e] for s,e in segs],'seg_frames':frames,'removed':removed,'out_start':f0,'out_frames':tot})
    log.append(f'  cena {i}: fala até {wend:.2f}s, corta em {fim:.2f}s de {cd:.2f}s; pausas removidas {[(round(a,2),round(b,2)) for a,b in removed]} → {tot} frames ({tot/FPS:.2f}s), sai no frame {f0}')
    f0+=tot
J={'fps':FPS,'respiro':RESP,'pausa_max':PMAX,'pausa_keep':PKEEP,'total_frames':f0,'scenes':scenes}
json.dump(J,open(os.environ.get('TL',f'{P}/molde/timeline.json'),'w'),indent=1)
with open(os.environ.get('TL',f'{P}/molde/timeline.json').replace('.json','.tsv'),'w') as f:
    f.write('# cena\tframe_ini\tframes\tini_s\tfim_s\tcorte_no_clipe_s\tclipe_s\tpausas_removidas\n')
    for s in scenes: f.write(f"{s['cena']}\t{s['out_start']}\t{s['out_frames']}\t{s['out_start']/FPS:.3f}\t{(s['out_start']+s['out_frames'])/FPS:.3f}\t{s['corte']:.3f}\t{s['clip_s']:.3f}\t{len(s['removed'])}\n")
print('\n'.join(log),file=sys.stderr)
print(f"timeline: total {f0} frames = {f0/FPS:.2f}s | cortes em "+' · '.join(f"{(s['out_start']+s['out_frames'])/FPS:.2f}" for s in scenes[:-1])+f" | pausas removidas: {sum(len(s['removed']) for s in scenes)} ({sum(b-a for s in scenes for a,b in s['removed']):.2f}s)")
