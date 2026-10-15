#!/usr/bin/env python3
# Timeline do AD02-H2 versão WhatsApp: as fronteiras dos blocos são as MESMAS PALAVRAS do original (medidas em 17/09:
# card até "away", painel A até "and", rosto limpo até "traces"/"clues", painel B até "where", CTA a partir de "Get"),
# só que nos tempos do áudio novo (whisper de molde/vo-16k.json). Escreve molde/timeline.json.
import json,re
P='centerpag-detect/criativos/ad02-h2-zap-2026-09-17'; FPS=30; OFF=6.40; HOOK_FIM=192; CAUDA=0.5
j=json.load(open(f'{P}/molde/vo-16k.json')); W=[w for s in j['segments'] for w in s['words']]
norm=lambda w: re.sub(r"[^a-z']",'',w.lower())
f=lambda i: HOOK_FIM+int(round(W[i]['start']*FPS))
def acha(txt,apos=0):
    for i in range(apos,len(W)):
        if norm(W[i]['word'])==txt: return i
    raise SystemExit('não achei '+txt)
i_but=acha('but'); i_and=acha('and',i_but); i_you=i_and+1; i_behind=acha('behind'); i_to=acha('to',acha('where',i_behind)); i_get=acha('get',i_to)
TOTAL=HOOK_FIM+int(round((W[-1]['end']+CAUDA)*FPS))
T={'fps':FPS,'hook_fim':HOOK_FIM,'total':TOTAL,'card':[HOOK_FIM,f(i_but)],'painelA':[f(i_but),f(i_you)],'limpo':[f(i_you),f(i_behind)],
   'painelB':[f(i_behind),f(i_to)],'final':[f(i_to),TOTAL],'cta':[f(i_get),TOTAL-7],
   'sem_legenda':[[f(i_behind),f(i_behind)+24],[f(i_to),f(i_get)]],'palavras':[{'i':i,'w':w['word'].strip(),'f':f(i)} for i,w in enumerate(W)]}
json.dump(T,open(f'{P}/molde/timeline.json','w'),indent=1)
print({k:v for k,v in T.items() if k!='palavras'})
