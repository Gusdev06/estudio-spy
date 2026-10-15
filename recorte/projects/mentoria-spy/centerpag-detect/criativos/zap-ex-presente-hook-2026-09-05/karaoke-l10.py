#!/usr/bin/env python3
# karaoke-l10.py <whisper.json> <saida.tsv> — blocos de 2–4 palavras (quebra em pontuação e a cada 4), caixa alta,
# '|' vira segunda linha quando o bloco passa de 16 caracteres (medido no wpp-01: 1 linha até "THE OTHER PERSON", 2 linhas em "AND INSTANT|MESSAGES").
# Saída: ini_s<TAB>fim_s<TAB>TEXTO. Custo zero.
import json, sys, re
src, out = sys.argv[1], sys.argv[2]; lista = sys.argv[4] if len(sys.argv)>4 and sys.argv[3]=='--blocos' else None
words=[(w['word'].strip(), w['start'], w['end']) for s in json.load(open(src))['segments'] for w in s['words'] if w['word'].strip()]
blocos=[]; cur=[]
def norm(w): return re.sub(r"[^a-z0-9']","",w.lower().replace('’',"'"))
if lista:   # casa cada linha da lista com as palavras do whisper, em ordem
    k=0
    for l in open(lista):
        l=l.strip()
        if not l or l.startswith('#'): continue
        st=en=None
        for t in [norm(x) for x in l.split()]:
            j=k
            while j<len(words) and not (norm(words[j][0])==t or norm(words[j][0]).startswith(t) or t.startswith(norm(words[j][0]))): j+=1
            if j>=len(words): print(f'AVISO: "{t}" de "{l}" não achada no whisper',file=sys.stderr); break
            if st is None: st=words[j][1]
            en=words[j][2]; k=j+1
        if st is None: st=blocos[-1][1] if blocos else 0.0; en=st+0.5
        blocos.append((st,en,l))
    words=[]
def flush():
    if cur: blocos.append((cur[0][1], cur[-1][2], ' '.join(w[0] for w in cur))); cur.clear()
for w in words:
    cur.append(w)
    if len(cur)>=4 or re.search(r'[.,!?;:]$', w[0]): flush()
flush()
def fmt(t):
    t=re.sub(r'[.,!?;:]','',t).upper()
    if len(t)>16:
        ws=t.split(); best=None
        for i in range(1,len(ws)):
            a,b=' '.join(ws[:i]),' '.join(ws[i:]); d=abs(len(a)-len(b))
            if best is None or d<best[0]: best=(d,a+'|'+b)
        t=best[1]
    return t
with open(out,'w') as f:
    f.write('# ini_s\tfim_s\ttexto ("|" = quebra de linha)\n')
    for a,b,t in blocos: f.write(f'{a:.2f}\t{b:.2f}\t{fmt(t)}\n')
print(f'{len(blocos)} blocos -> {out}')
