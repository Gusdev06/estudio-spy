#!/usr/bin/env python3
# Imagens-base dos 2 elencos (gpt-image-2/edit sobre o frame do original, mesmo request da var5/var6, só troca a descrição).
# As URLs de upload antigas expiram (403): os frames de referência foram re-subidos (base/url-ref-A/B.txt).
# Uso (de projects/mentoria-spy/): python3 .../gerar-bases.py 170-A [170-B 171-A 171-B]
import json,subprocess,sys
N='centerpag-detect/criativos/podcast-wpp-57s-copy-nova-2026-09-23'; D='centerpag-detect/criativos/podcast-wpp-cp108-avatar-copy-2026-10-07'
T={p:json.load(open(f'{N}/var5/base/w5-{p}.req.json')) for p in 'AB'}; old={p:open(f'{N}/var5/base/w5-{p}.txt').read().strip() for p in 'AB'}
cast={l.split('\t')[0]:dict(zip('AB',[s.strip() for s in l.rstrip('\n').split('\t')[2].split('|')])) for l in open(f'{D}/casting.tsv') if l.strip()}
procs=[]
for kp in sys.argv[1:]:
    k,p=kp.split('-'); desc=cast[k][p]; r=dict(T[p]); r['images']=[open(f'{D}/base/url-ref-{p}.txt').read().strip()]; r['prompt']=T[p]['prompt'].replace(old[p],desc); assert desc in r['prompt']
    open(f'{D}/base/{kp}.txt','w').write(desc); json.dump(r,open(f'{D}/base/{kp}.req.json','w'))
    cmd=f"wavespeed run openai/gpt-image-2/edit --input-file {D}/base/{kp}.req.json --json --download {D}/base/{kp}.png > {D}/base/{kp}.json 2> {D}/base/{kp}.log"
    procs.append((kp,subprocess.Popen(cmd,shell=True)))
for n,pr in procs: print(n,'ok' if pr.wait()==0 else 'FALHOU')
