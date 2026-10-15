import numpy as np
f=np.load('work/frames_small.npy').astype(int)  # 320x180
B,G,R=f[...,0],f[...,1],f[...,2]
navy=(B>R+40)&(B>G+15)
red=(R>170)&(G<90)&(B<100)
wht=(R>215)&(G>215)&(B>215)&(np.abs(R-B)<14)
for i in range(0,len(f),5):
    n,r,w=navy[i].sum(),red[i].sum(),wht[i].sum()
    print(i,f'{i/30:.2f}',n,r,w)
