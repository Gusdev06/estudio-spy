# Rastreia a caixa original nos frames do chicote: acha deslocamentos (dx,dy) das cópias da camada de legenda.
import numpy as np, cv2, json, sys
sys.path.insert(0,'../scripts'); import comp
f0=cv2.imread('f0000.png').astype(np.int16)
INT=comp.INT.astype(bool)
tb=np.zeros((1280,720),np.float32); tb[INT & (f0.max(2)<12)]=1   # pixels pretos da caixa
tw=np.zeros((1280,720),np.float32); tw[INT & (f0.min(2)>225)]=1  # texto branco
def corr(a,b):
    H,W=1280*2,720*2
    A=np.fft.rfft2(a,(H,W)); B=np.fft.rfft2(b,(H,W))
    return np.fft.irfft2(A*np.conj(B),(H,W))
res={}
for i in range(140,160):
    F=cv2.imread('f%04d.png'%i).astype(np.int16)
    fb=(F.max(2)<12).astype(np.float32); fw=(F.min(2)>225).astype(np.float32)
    c=corr(fb,tb)+corr(fw,tw)*2   # c[dy,dx] = sum F(p+off)*T(p)
    peaks=[]
    cc=c.copy()
    for k in range(4):
        dy,dx=np.unravel_index(np.argmax(cc),cc.shape); v=cc[dy,dx]
        if v<3000: break
        ddy=dy if dy<1280 else dy-2560; ddx=dx if dx<720 else dx-1440
        peaks.append((int(ddx),int(ddy),int(v)))
        cc[max(0,dy-30):dy+30, max(0,dx-60):dx+60]=0
    res[i]=peaks; print(i,peaks,flush=True)
json.dump(res,open('../scripts/picos.json','w'))
