# Gera as 2 imagens-base de cada elenco da var6 (gpt-image-2/edit sobre o frame do original, mesmo prompt da var5).
import json,subprocess,sys,os
V='var6'; T={p:json.load(open(f'var5/base/w5-{p}.req.json')) for p in 'AB'}
old={p:open(f'var5/base/w5-{p}.txt').read().strip() for p in 'AB'}
procs=[]
for line in open(f'{V}/casting.tsv'):
    k,nome,d=line.rstrip('\n').split('\t'); desc=dict(zip('AB',[s.strip() for s in d.split('|')]))
    for p in 'AB':
        r=dict(T[p]); r['prompt']=T[p]['prompt'].replace(old[p],desc[p]); assert desc[p] in r['prompt']
        open(f'{V}/base/{k}-{p}.txt','w').write(desc[p]); json.dump(r,open(f'{V}/base/{k}-{p}.req.json','w'))
        cmd=f"wavespeed run openai/gpt-image-2/edit --input-file {V}/base/{k}-{p}.req.json --json --download {V}/base/{k}-{p}.png > {V}/base/{k}-{p}.json 2> {V}/base/{k}-{p}.log"
        procs.append((k+p,subprocess.Popen(cmd,shell=True)))
for n,pr in procs: print(n,'ok' if pr.wait()==0 else 'FALHOU')
