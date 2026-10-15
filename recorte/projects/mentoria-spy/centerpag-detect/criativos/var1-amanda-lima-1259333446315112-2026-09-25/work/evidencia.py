import numpy as np,cv2
F=np.load('work/F.npy',mmap_mode='r')
def lab(im,t):
    im=im.copy(); cv2.rectangle(im,(0,0),(im.shape[1],34),(0,0,0),-1); cv2.putText(im,t,(6,24),cv2.FONT_HERSHEY_SIMPLEX,0.62,(0,255,255),2); return im
def crop(n,x,y,w,h,s=2): return cv2.resize(np.ascontiguousarray(F[n][y:y+h,x:x+w]),(w*s,h*s),interpolation=cv2.INTER_NEAREST)
row1=[lab(crop(n,30,820,360,380,1),f'STEP card n{n} ({n/30:.1f}s)') for n in (1256,1300,1345)]
S=np.load('work/S_G.npy'); sv=cv2.cvtColor(np.clip(S[820:1200,30:390]*8,0,255).astype(np.uint8),cv2.COLOR_GRAY2BGR)
row1.append(lab(sv,'std temporal x8 (claro = original vaza)'))
r1=np.hstack(row1)
row2=[lab(crop(n,150,880,180,190,2),f'HIDDEN DATA borda n{n}') for n in (30,120)]
row2.append(lab(cv2.resize(np.ascontiguousarray(F[1100][600:900,0:360]),(360,380)),'painel WhatsApp n1100: degrade'))
S=np.load('work/S_A.npy'); sv=cv2.cvtColor(np.clip(S[840:1240,120:500]*8,0,255).astype(np.uint8),cv2.COLOR_GRAY2BGR)
row2.append(lab(cv2.resize(sv,(360,380)),'std HIDDEN/HOW: card flutua'))
r2=np.hstack([cv2.resize(x,(360,380)) for x in row2])
fl=[lab(cv2.resize(np.ascontiguousarray(F[n]),(180,320)),f'n{n}') for n in range(174,184)]
r3=np.hstack(fl); r3=cv2.resize(r3,(1440,int(320*1440/1800)))
r1=cv2.resize(r1,(1440,int(r1.shape[0]*1440/r1.shape[1]))); r2=cv2.resize(r2,(1440,int(r2.shape[0]*1440/r2.shape[1])))
cv2.imwrite('conferencia/evidencia-bloqueio-mascara.jpg',np.vstack([r1,r2,lab(r3,'flash/gradacao em 7 transicoes (n174-183, 229-236, 400-408, 1057-1064, 1236-1244, 1359-1367, 1460-1467): a mulher original aparece tingida por baixo')]),[cv2.IMWRITE_JPEG_QUALITY,88])
