import numpy as np, cv2, sys
HERE='/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/gram-detect/criativos/sarah-smith-1677505624160791-3var-2026-10-17/v3-quem-ele-curte'
def o(i): return cv2.imread(HERE+'/tmp/f%04d.png'%i)
def p(i): return cv2.imread(HERE+'/tmp/out/f%04d.png'%i)
def sheet(frames,crop,name,scale):
    y0,y1,x0,x1=crop; cols=[]
    for i in frames:
        a=o(i)[y0:y1,x0:x1]; b=p(i)[y0:y1,x0:x1]
        col=np.vstack([a,np.full((6,x1-x0,3),255,np.uint8),b])
        col=cv2.resize(col,None,fx=scale,fy=scale,interpolation=cv2.INTER_AREA)
        cv2.putText(col,'f%d'%i,(5,22),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        cols.append(col); cols.append(np.full((col.shape[0],4,3),255,np.uint8))
    cv2.imwrite(HERE+'/conferencia/'+name,np.hstack(cols))
sheet([0,60,120,139,140,141,143],(880,1150,0,720),'gancho-a-original-em-cima.png',0.5)
sheet([144,145,146,147,148,149,150],(880,1150,0,720),'gancho-b-chicote-original-em-cima.png',0.5)
sheet([146,148,150,152,154,155],(870,980,0,720),'demo-a-chicote-original-em-cima.png',0.5)
sheet([156,200,250,300,350,378,379],(870,980,120,600),'demo-b-original-em-cima.png',0.6)
# fora das areas editadas
import comp, demo
ed=np.zeros((1280,720),bool)
worst=[]
for i in range(1095):
    a=o(i).astype(int); b=p(i).astype(int); d=np.abs(a-b).max(2)
    m=np.zeros((1280,720),bool)
    if i<150: m[930:1150,:]=True
    if 144<=i<=378: m[880:945,:]=True
    worst.append((i,float(d[~m].mean()),int(np.percentile(d[~m],99.9)),float(d[m].mean()) if m.any() else 0))
w=np.array([x[1] for x in worst]); q=np.array([x[2] for x in worst])
print('fora das areas: diff media por frame max %.2f, media %.2f; p99.9 max %d'%(w.max(),w.mean(),q.max()))
for x in sorted(worst,key=lambda t:-t[1])[:5]: print(x)
