#!/usr/bin/env python3
"""conferir-regioes.py A.mp4 B.mp4 [--frames n,n,...] [--json out]
Diferença média absoluta por canal (/255) entre duas peças L9 1170×2532, por região e por frame,
+ fronteiras da faixa medidas pela COR CHAPADA (linha 1211/1212/1497/1498, coluna 461/462).
Regiões: head y0–1212 · faixa y1212–1498 · funil y1498–2532 x0–462 · broll x462–1170 · cauda (frames ≥ 940, quadro cheio)."""
import sys, subprocess, json, numpy as np
W,H=1170,2532
def frames(path, idx):
    sel='+'.join(f'eq(n\\,{i})' for i in idx)
    raw=subprocess.run(['ffmpeg','-v','error','-i',path,'-vf',f"select='{sel}'",'-vsync','0','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    a=np.frombuffer(raw,np.uint8)
    n=len(a)//(W*H*3); assert n==len(idx), (n,len(idx))
    return a.reshape(n,H,W,3)
def main():
    a,b=sys.argv[1],sys.argv[2]
    idx=[0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,930,939,940,941,950,960,974]
    out=None
    if '--frames' in sys.argv: idx=[int(x) for x in sys.argv[sys.argv.index('--frames')+1].split(',')]
    if '--json' in sys.argv: out=sys.argv[sys.argv.index('--json')+1]
    A=frames(a,idx); B=frames(b,idx)
    # cor chapada da faixa: mediana do canto da faixa (x 0–40, y 1220–1260) em A
    mag=np.median(A[0,1220:1260,0:40].reshape(-1,3),axis=0)
    def frac(img,row=None,col=None):
        if row is not None: px=img[row,:,:]
        else: px=img[1498:2532,col,:]
        return float((np.abs(px.astype(int)-mag).max(axis=1)<=12).mean())
    rows=[]; agg={}
    print(f'faixa chapada (A, mediana canto): RGB {mag.astype(int).tolist()}')
    print(f"{'fr':>4} {'head':>7} {'faixa':>7} {'funil':>7} {'broll':>7} {'cauda':>7} | A:1211 1212 1497 1498 x461 x462 | B: idem")
    for k,i in enumerate(idx):
        d=np.abs(A[k].astype(np.int16)-B[k].astype(np.int16)).astype(np.float32)
        r={'frame':i}
        if i<940:
            r['head']=float(d[0:1212].mean()); r['faixa']=float(d[1212:1498].mean())
            r['funil']=float(d[1498:,0:462].mean()); r['broll']=float(d[1498:,462:].mean()); r['cauda']=None
            fa=[frac(A[k],row=1211),frac(A[k],row=1212),frac(A[k],row=1497),frac(A[k],row=1498)]
            # coluna 461/462: dentro do painel a fronteira funil|broll não é chapada; medimos a fração de pixels que
            # diferem entre as colunas 461 e 462 (a fronteira existe se a coluna 462 for "outro conteúdo")
            fb=[frac(B[k],row=1211),frac(B[k],row=1212),frac(B[k],row=1497),frac(B[k],row=1498)]
            r['faixaA']=fa; r['faixaB']=fb
            print(f"{i:4d} {r['head']:7.3f} {r['faixa']:7.3f} {r['funil']:7.3f} {r['broll']:7.3f} {'-':>7} | {fa[0]:.3f} {fa[1]:.3f} {fa[2]:.3f} {fa[3]:.3f} | {fb[0]:.3f} {fb[1]:.3f} {fb[2]:.3f} {fb[3]:.3f}")
        else:
            r['cauda']=float(d.mean()); r['head']=r['faixa']=r['funil']=r['broll']=None
            fa=[frac(A[k],row=1211),frac(A[k],row=1212)]; fb=[frac(B[k],row=1211),frac(B[k],row=1212)]
            r['faixaA']=fa; r['faixaB']=fb
            print(f"{i:4d} {'-':>7} {'-':>7} {'-':>7} {'-':>7} {r['cauda']:7.3f} | {fa[0]:.3f} {fa[1]:.3f}  (faixa deve ser 0 aqui) | {fb[0]:.3f} {fb[1]:.3f}")
        rows.append(r)
    for key in ['head','faixa','funil','broll','cauda']:
        v=[r[key] for r in rows if r[key] is not None]
        agg[key]={'mean':float(np.mean(v)),'max':float(np.max(v)),'n':len(v)}
        print(f"{key:>6}: média {agg[key]['mean']:.3f}/255 · máx {agg[key]['max']:.3f} · n={len(v)}")
    # fronteira x=462 no painel: perfil de diferença horizontal médio (penhasco) em A e B, frames < 940
    for name,X in (('A',A),('B',B)):
        ks=[k for k,i in enumerate(idx) if i<940]
        prof=np.mean([np.abs(np.diff(X[k,1498:,:,:].astype(np.int16),axis=1)).mean(axis=(0,2)) for k in ks],axis=0)
        j=int(np.argmax(prof[440:480]))+440
        print(f"{name}: penhasco horizontal no painel (argmax |col j+1 - col j|, janela 440–480): entre x={j} e x={j+1} · valor {prof[j]:.1f} · 2º {np.sort(prof[440:480])[-2]:.1f}")
    if out: json.dump({'frames':rows,'agg':agg,'magenta':mag.tolist()},open(out,'w'),indent=1)
main()
