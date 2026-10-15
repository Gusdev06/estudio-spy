import subprocess, sys, os, json
from PIL import Image
import numpy as np

def frames(f, n=7):
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],
        capture_output=True,text=True).stdout.strip())
    out=[]
    for i in range(n):
        t=d*(0.12+0.72*i/(n-1))
        p=f"/tmp/_m{i}.png"
        subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',f,'-frames:v','1','-vf','scale=360:-1',p,'-y'],capture_output=True)
        if os.path.exists(p): out.append(np.asarray(Image.open(p).convert('RGB'),dtype=float))
    return out

def bandas(f):
    fr=frames(f)
    if not fr: return None
    H,Wd,_=fr[0].shape
    # 1) fronteiras: linhas onde a diferenca vertical e alta EM TODOS os frames (borda fixa de painel)
    edge=np.ones(H-1)*1e9
    for a in fr:
        dv=np.abs(a[1:]-a[:-1]).mean(axis=(1,2))
        edge=np.minimum(edge,dv)
    thr=max(12, np.percentile(edge,99.2))
    lim=[i for i,v in enumerate(edge) if v>thr]
    # agrupa fronteiras vizinhas
    grp=[]
    for i in lim:
        if grp and i-grp[-1][-1]<=3: grp[-1].append(i)
        else: grp.append([i])
    fron=[int(np.mean(g)) for g in grp]
    # 2) barras chapadas: linhas de variancia horizontal ~0 em todos os frames
    flat=np.ones(H)*1e9
    for a in fr: flat=np.minimum(flat, a.std(axis=1).mean(axis=1))
    barras=[]
    run=None
    for y in range(H):
        if flat[y]<9:
            run=[y,y] if run is None else [run[0],y]
        elif run:
            if run[1]-run[0]>=3: barras.append(tuple(run))
            run=None
    if run and run[1]-run[0]>=3: barras.append(tuple(run))
    return {"h":H,"w":Wd,"fronteiras_pct":[round(y/H*100,1) for y in fron],
            "barras_chapadas_pct":[(round(a/H*100,1),round(b/H*100,1)) for a,b in barras]}

if __name__=="__main__":
    print(json.dumps(bandas(sys.argv[1]),ensure_ascii=False))
