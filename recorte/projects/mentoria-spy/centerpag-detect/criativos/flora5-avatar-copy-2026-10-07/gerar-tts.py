#!/usr/bin/env python3
# TTS ElevenLabs v3 com timing (WaveSpeed): 1 chamada pra voz A (falas 1, 3, 4 separadas por quebra) e 1 pra voz B (fala 2).
# Saída: p17x/audio/voz-A.{out.json,mp3}, voz-B.*; palavras com tempo em voz-X.palavras.json. Uso (desta pasta): python3 gerar-tts.py p172 [p173]
import json, subprocess, sys
for P in sys.argv[1:]:
    E=json.load(open(f'{P}/elenco.json')); L=[l.rstrip('\n').split('\t') for l in open(f'{P}/roteiro.tsv') if l.strip()]
    subprocess.run(['mkdir','-p',f'{P}/audio'])
    txt={'A':'\n\n'.join(t for _,p,t in L if p=='A'),'B':' '.join(t for _,p,t in L if p=='B')}
    procs=[]
    for v in 'AB':
        json.dump({'text':txt[v],'voice_id':E['voz'][v],'stability':0.5},open(f'{P}/audio/voz-{v}.req.json','w'))
        procs.append((v,subprocess.Popen(f'wavespeed run elevenlabs/eleven-v3/timing --input-file {P}/audio/voz-{v}.req.json --json > {P}/audio/voz-{v}.out.json 2> {P}/audio/voz-{v}.log',shell=True)))
    for v,pr in procs:
        pr.wait(); o=json.load(open(f'{P}/audio/voz-{v}.out.json')); r=o['raw']['outputs'][0]; a=r['alignment']
        subprocess.run(['curl','-s','--retry','4','-o',f'{P}/audio/voz-{v}.mp3',r['audio']],check=True)
        ws=[];cur=None
        for c,s,e in zip(a['characters'],a['character_start_times_seconds'],a['character_end_times_seconds']):
            if c.isspace():
                if cur: ws.append(cur); cur=None
            else:
                if cur is None: cur={'w':c,'s':s,'e':e}
                else: cur['w']+=c; cur['e']=e
        if cur: ws.append(cur)
        json.dump(ws,open(f'{P}/audio/voz-{v}.palavras.json','w'),indent=0)
        print(P,v,len(ws),'palavras',f"{ws[-1]['e']:.2f}s")
