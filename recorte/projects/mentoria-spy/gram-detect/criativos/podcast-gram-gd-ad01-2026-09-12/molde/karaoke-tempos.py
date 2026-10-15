#!/usr/bin/env python3
# molde/karaoke.tsv (frame_ini, frame_fim, C, texto): blocos do roteiro Gram × tempos por palavra do whisper no áudio do clipe,
# remapeados pro tempo de saída da timeline (pausas removidas). Uso: python3 karaoke-tempos.py [--fallback]
import json, os, re, sys
P='gram-detect/criativos/podcast-gram-gd-ad01-2026-09-12'; GAP=3
BLOCOS={
 1: ["there's a detail","on Instagram","that gives","almost everyone away"],
 2: ["yeah","I found something","I wasn't even","looking for","I didn't touch","their phone","I just typed","the username"],
 3: ["whoever hides something","leaves small traces","messages","contacts","strange behavior","even what they think","they deleted"],
 4: ["you don't need","to guess","you don't need","to argue","you don't need","to grab their phone"],
 5: ["you just need","to know","where to look"],
 6: ["there's a tool","that shows it","in seconds","you type","the username","nothing goes","to their phone","the first check","is free"],
 7: ["the access is","right below","while this tool","is still available"],
}
AUD=os.environ.get('AUD',f'{P}/audio'); TL=os.environ.get('TL',f'{P}/molde/timeline.json'); KAR=os.environ.get('KAR',f'{P}/molde/karaoke.tsv')
if os.environ.get('BLOCOS1'): BLOCOS[1]=json.loads(os.environ['BLOCOS1'])   # variante: karaokê da cena 1 nova
T=json.load(open(TL)); FPS=T['fps']
def norm(w): return re.sub(r"[^a-z0-9']","",w.lower().replace('’',"'"))
def to_out(sc,t):
    rem=0.0
    for a,b in sc['removed']:
        if t>=b: rem+=b-a
        elif t>a: rem+=t-a
    return sc['out_start']+int(round((t-rem)*FPS))
out=[]; fallback='--fallback' in sys.argv
for sc in T['scenes']:
    i=sc['cena']; blocos=BLOCOS[i]; js=f"{AUD}/clip-cena-{i}.json"; words=None
    if os.path.exists(js) and not fallback:
        words=[(norm(w['word']),w['start'],w['end']) for s in json.load(open(js))['segments'] for w in s['words']]; words=[w for w in words if w[0]]
    if words:
        k=0; times=[]
        for b in blocos:
            st=None; en=None
            for t in [norm(x) for x in b.split()]:
                j=k
                while j<len(words) and words[j][0]!=t and not words[j][0].startswith(t) and not t.startswith(words[j][0]): j+=1
                if j>=len(words): print(f'AVISO cena {i}: "{t}" de "{b}" não achada no whisper',file=sys.stderr); break
                if st is None: st=words[j][1]
                en=words[j][2]; k=j+1
            if st is None: st=(times[-1][1] if times else 0.0); en=st+0.5
            times.append((st,en))
        end_frame=sc['out_start']+sc['out_frames']
        for n,(b,(st,en)) in enumerate(zip(blocos,times)):
            f0=to_out(sc,st); f1=(to_out(sc,times[n+1][0])-GAP) if n+1<len(times) else min(to_out(sc,en)+6,end_frame)
            out.append((f0,max(f1,f0+2),b)); src='whisper'
    else:
        n=len(blocos); d=sc['out_frames']/n
        for q,b in enumerate(blocos): out.append((sc['out_start']+int(q*d),sc['out_start']+int((q+1)*d)-GAP,b)); src='FALLBACK'
    print(f'cena {i}: {len(blocos)} blocos ({src})',file=sys.stderr)
with open(KAR,'w') as f:
    f.write('# frame_ini\tframe_fim(excl)\testado\ttexto\n')
    for f0,f1,b in out: f.write(f'{f0}\t{f1}\tC\t{b}\n')
print(f'{len(out)} blocos → {KAR}')
