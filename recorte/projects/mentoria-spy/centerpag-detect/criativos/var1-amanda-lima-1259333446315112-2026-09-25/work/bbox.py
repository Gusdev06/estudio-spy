import numpy as np,sys
G=np.load('work/G.npy',mmap_mode='r')
def bbox(n,col,tol,reg,minc=8):
    x0,y0,x1,y1=reg; im=G[n,y0:y1,x0:x1].astype(int)
    m=(np.abs(im-np.array(col)).max(2)<tol)
    r=np.where(m.sum(1)>=minc)[0]; c=np.where(m.sum(0)>=minc)[0]
    if len(r)==0 or len(c)==0: return None
    return (x0+c[0],y0+r[0],x0+c[-1]+1,y0+r[-1]+1,int(m.sum()))
if __name__=='__main__':
    col=tuple(int(sys.argv[1][i:i+2],16) for i in (0,2,4)); tol=int(sys.argv[2]); reg=tuple(map(int,sys.argv[3].split(','))); a,b,st=map(int,sys.argv[4].split(','))
    for n in range(a,b,st): print(n,bbox(n,col,tol,reg))
