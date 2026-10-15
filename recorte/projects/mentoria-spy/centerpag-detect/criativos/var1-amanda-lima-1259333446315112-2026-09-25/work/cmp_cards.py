# lado a lado: original (esq) x redesenho sobre o MESMO frame original (dir), por bloco
import numpy as np,cv2,sys
sys.path.insert(0,'.'); from cards import Compositor
G=np.load('work/G.npy',mmap_mode='r'); C=Compositor()
B=[(90,(120,720,600,1225)),(300,(30,860,520,1090)),(550,(15,790,470,1140)),(800,(50,795,515,1085)),(1300,(15,20,700,1180)),(1540,(30,830,650,1080)),(1700,(30,30,670,1140))]
for n,(x0,y0,x1,y1) in B:
    o=np.ascontiguousarray(G[n]).astype(np.float32)/255; r=C.apply(o.copy(),n)
    a=(o[y0:y1,x0:x1]*255).astype(np.uint8); b=(r[y0:y1,x0:x1]*255).astype(np.uint8)
    im=np.hstack([a,np.full((y1-y0,6,3),255,np.uint8),b])
    cv2.imwrite(f'work/cmp_{n}.png',cv2.cvtColor(im,cv2.COLOR_RGB2BGR))
