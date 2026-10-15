#!/usr/bin/env python3
# Monta a locução nova no molde da Flora e grava a timeline (frames a 30 fps) que o karaokê e a montagem usam.
#  falas: 1 A (promessa) · 2 B (pergunta) · 3 A (mecanismo; rosto só na 1ª frase, depois clarão + painéis) · 4 A (CTA, rosto)
#  Cada voz normalizada a -18 LUFS; pausas internas do TTS encurtadas a 0,30 s e pausas curtas entre falas (nenhum silêncio >= 0,5 s).
# Saída: p17x/audio/vo.wav, p17x/audio/clip-{a1,b,a2,a3}.wav (áudio de cada clipe Pruna) e p17x/molde/timeline.json.
# Uso (desta pasta): python3 timeline.py p172 [p173]
import json, subprocess, sys, numpy as np
FPS=30; SR=44100
def ler(arq):
    raw=subprocess.run(['ffmpeg','-v','error','-i',arq,'-af','loudnorm=I=-18:TP=-1.5:LRA=11','-ar',str(SR),'-ac','1','-f','f32le','-'],capture_output=True,check=True).stdout
    return np.frombuffer(raw,np.float32).copy()
def aperta(x,maxp=0.30,lim=-33):
    # encurta pausas internas: trechos com RMS(20 ms) < lim dB e mais longos que maxp viram maxp (centrado). Devolve x e o mapa de tempo.
    h=int(0.01*SR); n=len(x)//h; r=np.sqrt(np.array([np.mean(x[i*h:(i+1)*h]**2) for i in range(n)])+1e-12); q=20*np.log10(r)<lim
    corte=[]; i=0
    while i<n:
        if q[i]:
            j=i
            while j<n and q[j]: j+=1
            mx=0.03 if i==0 else (0.06 if j>=n else maxp)   # borda: silêncio de entrada/saída quase todo fora
            if (j-i)*0.01>mx:
                extra=(j-i)*0.01-mx; a=i*0.01+(0 if i==0 else mx/2 if j<n else mx); corte.append((a,a+extra))
            i=j
        else: i+=1
    keep=[]; last=0.0
    for a,b in corte: keep.append(x[int(last*SR):int(a*SR)]); last=b
    keep.append(x[int(last*SR):])
    def mapa(t):
        d=0.0
        for a,b in corte:
            if t>=b: d+=b-a
            elif t>a: d+=t-a
        return t-d
    return np.concatenate(keep),mapa
def grava(arq,x):
    p=subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-','-c:a','pcm_s16le',arq],input=x.astype(np.float32).tobytes(),check=True)
for P in sys.argv[1:]:
    L=[l.rstrip('\n').split('\t') for l in open(f'{P}/roteiro.tsv') if l.strip()]
    A=ler(f'{P}/audio/voz-A.mp3'); B=ler(f'{P}/audio/voz-B.mp3')
    wa=json.load(open(f'{P}/audio/voz-A.palavras.json')); wb=json.load(open(f'{P}/audio/voz-B.palavras.json'))
    # fatias da voz A por fala (corte 20 ms antes da 1ª palavra da fala seguinte)
    i=0; fat=[]
    for n,p,t in L:
        if p!='A': continue
        k=len(t.split()); seg=wa[i:i+k]; nxt=wa[i+k]['s']-0.02 if i+k<len(wa) else len(A)/SR
        fat.append((int(n),max(seg[0]['s']-0.02,0),nxt,seg)); i+=k
    a0={n:(s0,s1,seg) for n,s0,s1,seg in fat}
    pedacos=[]; words=[]; linhas={}; t=0.0
    def poe(n,audio,s0,s1,ws,papel,pausa):
        global t
        x,mp=aperta(audio[int(s0*SR):int(s1*SR)])
        # apara silêncio do fim (> -45 dB), mantendo 60 ms
        e=np.where(np.abs(x)>10**(-45/20))[0]; x=x[:min(len(x),(e[-1] if len(e) else len(x))+int(0.06*SR))]
        linhas[n]={'papel':papel,'ini':t,'fim':t+len(x)/SR}
        for w in ws: words.append({'w':w['w'],'s':t+mp(w['s']-s0),'e':t+mp(w['e']-s0),'linha':n})
        pedacos.append(x); pedacos.append(np.zeros(int(pausa*SR),np.float32)); t+=len(x)/SR+pausa
    s0,s1,seg=a0[1]; poe(1,A,s0,s1,seg,'A',0.15)
    poe(2,B,0,len(B)/SR,wb,'B',0.15)
    s0,s1,seg=a0[3]; poe(3,A,s0,s1,seg,'A',0.12)
    s0,s1,seg=a0[4]; poe(4,A,s0,s1,seg,'A',0.0)
    vo=np.concatenate(pedacos+[np.zeros(int(0.35*SR),np.float32)]); grava(f'{P}/audio/vo.wav',vo)
    DUR=len(vo)/SR; NF=int(round(DUR*FPS))
    # blocos de imagem (frames): a1 rosto A · b rosto B · a2 rosto A até o fim da 1ª frase da fala 3 + 4 fr de clarão · painéis · a3 rosto A (CTA)
    f=lambda s:int(round(s*FPS))
    w3=[w for w in words if w['linha']==3]; fim_frase=next(w['e'] for w in w3 if w['w'].endswith('.'))
    T1=f(linhas[2]['ini'])-1; T2=f(linhas[3]['ini'])-1; TP=f(fim_frase+0.10)+4; T4=f(linhas[4]['ini'])-2
    blocos={'a1':{'papel':'A','f0':0,'f1':T1-1},'b':{'papel':'B','f0':T1,'f1':T2-1},'a2':{'papel':'A','f0':T2,'f1':TP-1},
            'paineis':{'f0':TP,'f1':T4-1,'orig0':267},'a3':{'papel':'A','f0':T4,'f1':NF-1}}
    # áudio de cada clipe Pruna: o trecho da vo que cobre o bloco (mín. 2,5 s, a Pruna falha com < 2 s)
    for b,d in blocos.items():
        if b=='paineis': continue
        s=d['f0']/FPS; e=max((d['f1']+1)/FPS,s+2.5); e=min(e,DUR); d['ss']=s; d['dur']=e-s
        grava(f'{P}/audio/clip-{b}.wav',vo[int(s*SR):int(e*SR)])
    json.dump({'dur':DUR,'nf':NF,'linhas':linhas,'palavras':words,'blocos':blocos},open(f'{P}/molde/timeline.json','w'),indent=1)
    print(P,f'{DUR:.2f}s {NF} fr',{k:(v['f0'],v['f1'],round(v.get('dur',0),2)) for k,v in blocos.items()},'painéis',blocos['paineis']['f1']-blocos['paineis']['f0']+1,'fr')
