#!/usr/bin/env python3
# Custo real deste lote: casa os prediction ids dos .json/.out.json desta pasta com `wavespeed billings` (conta compartilhada; delta de saldo não serve).
import json,glob,os,subprocess,re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ids={}
for f in glob.glob('audio/*.json')+glob.glob('base/*.out.json')+glob.glob('clipes/*.out.json')+glob.glob('clipes/*.json'):
    try: t=open(f).read()
    except: continue
    for m in re.findall(r'"id"\s*:\s*"([0-9a-f]{32})"',t): ids[m]=f
    for m in re.findall(r'"prediction_id"\s*:\s*"([0-9a-f]{32})"',t): ids[m]=f
since=open('inicio-utc.txt').read().strip(); tot=0; achados=set()
for p in range(1,8):
    d=json.loads(subprocess.run(['wavespeed','billings','--limit','100','--page',str(p),'--since',since,'--json'],capture_output=True,text=True).stdout)
    for i in d['items']:
        u=i['prediction']['uuid']
        if u in ids:
            s=-1 if i['billing_type']=='refund' else 1; tot+=s*i['price']; achados.add(u); print(f"{ids[u]:28s} {i['prediction']['model_uuid']:36s} {s*i['price']:.4f} {i['access_key_name']}")
    if not d['has_more']: break
print(f'TOTAL US$ {tot:.3f} · {len(achados)}/{len(ids)} predições cobradas encontradas')
