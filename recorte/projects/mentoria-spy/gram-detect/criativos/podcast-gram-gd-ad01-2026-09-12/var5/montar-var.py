#!/usr/bin/env python3
# Monta as 5 variações de hook do podcast Gram: chama montar-gram.py por variante com a cena 1 nova, a caixa nova e o karaokê
# da cena 1 novo (envs CLIPES/AUD/TL/KAR/KDIR/CAIXA_L1/CAIXA_L2/BOXSZ/BLOCOS1). Cenas 2-7, painéis, setas e música idênticos.
# Uso (de projects/mentoria-spy/):  python3 .../var5/montar-var.py [v1 v2 ...]      Custo: zero.
import json, os, subprocess, sys
P='gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12'; V=f'{P}/var5'
H=[l.rstrip('\n').split('\t') for l in open(f'{V}/hooks.tsv') if not l.startswith('#') and l.strip()]
alvo=sys.argv[1:] or [h[0] for h in H]
res=[]
for v,l1,l2,sz,fala,blocos,slug in H:
    if v not in alvo: continue
    os.makedirs(f'{V}/molde/{v}',exist_ok=True)
    out=f'{V}/PODCAST-GRAM-{v}-{slug}.mp4'
    env=dict(os.environ, CLIPES=f'{V}/clipes/{v}', AUD=f'{V}/audio/{v}', TL=f'{V}/molde/{v}/timeline.json',
             KAR=f'{V}/molde/{v}/karaoke.tsv', KDIR=f'{V}/molde/{v}/k', CAIXA_L1=l1, CAIXA_L2=l2, BOXSZ=sz, BLOCOS1=blocos)
    r=subprocess.run(['python3',f'{P}/montar-gram.py',out],env=env,capture_output=True,text=True)
    if r.returncode: print(r.stdout[-800:],r.stderr[-800:]); sys.exit(f'falhou {v}')
    T=json.load(open(f'{V}/molde/{v}/timeline.json')); c1=T['scenes'][0]; sil=[x for x in c1['removed']]
    res.append((v,slug,T['total_frames'],T['total_frames']/30,c1['out_frames'],len(sil),out))
    print(f"{v}: cena 1 = {c1['out_frames']} fr ({c1['out_frames']/30:.2f}s, {len(sil)} pausa(s) cortada(s)) · peça {T['total_frames']} fr = {T['total_frames']/30:.2f}s -> {out}")
with open(f'{V}/conferencia/resumo.tsv','w') as f:
    f.write('# var\tslug\tframes\tsegundos\tcena1_frames\tpausas_cortadas_c1\tarquivo\n')
    for r in res: f.write('\t'.join(str(x) for x in r)+'\n')
print(f'{len(res)} peças · resumo em {V}/conferencia/resumo.tsv')
