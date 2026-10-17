import numpy as np, cv2
def o(i): return cv2.imread('tmp/f%04d.png'%i)
def p(i): return cv2.imread('tmp/out/f%04d.png'%i)
def folha(frames,crop,name,ncol):
    y0,y1,x0,x1=crop; cells=[]
    for i in frames:
        c=np.vstack([o(i)[y0:y1,x0:x1],np.full((4,x1-x0,3),255,np.uint8),p(i)[y0:y1,x0:x1]])
        c=cv2.copyMakeBorder(c,30,6,6,6,cv2.BORDER_CONSTANT,value=(255,255,255))
        cv2.putText(c,'f%d  (cima: original / baixo: peca)'%i,(8,22),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,200),2); cells.append(c)
    while len(cells)%ncol: cells.append(np.full_like(cells[0],255))
    rows=[np.hstack(cells[k:k+ncol]) for k in range(0,len(cells),ncol)]
    cv2.imwrite('conferencia/'+name,np.vstack(rows))
folha([0,70,139,140,142,144,145,146,147,148,149,150],(930,1145,0,720),'folha-gancho-e-chicote.png',3)
folha([146,148,150,152,155,200,300,378,379],(860,980,0,720),'folha-legenda-demo.png',3)
