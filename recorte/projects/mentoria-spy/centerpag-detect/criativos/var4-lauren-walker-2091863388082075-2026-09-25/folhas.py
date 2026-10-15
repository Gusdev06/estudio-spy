#!/usr/bin/env python3
# Folhas de conferência (25/09, var2-6): original × peça em 10 instantes, emendas e mapa dos px iguais (vermelho) nos piores frames da varredura.
# Uso (desta pasta, depois de varredura.py): python3 folhas.py
import cv2, numpy as np, json
o=lambda n: cv2.imread(f'frames/full/{n:03d}.png'); p=lambda n: cv2.imread(f'frames/peca/{n:03d}.png')
def lab(im,t): im=im.copy(); cv2.putText(im,t,(12,50),cv2.FONT_HERSHEY_SIMPLEX,1.6,(0,255,255),4); return im
sm=lambda im: cv2.resize(im,(240,427))
N=[20,60,95,130,250,340,380,430,490,560]
cv2.imwrite('conferencia/original-x-peca-10-instantes.jpg',np.vstack([np.hstack([sm(lab(o(n),f'n{n}')) for n in N]),np.hstack([sm(lab(p(n),f'n{n}')) for n in N])]))
E=[98,99,343,344,447,448,524,525]; cv2.imwrite('conferencia/emendas.jpg',np.hstack([sm(lab(p(n),f'n{n}')) for n in E]))
r=json.load(open('conferencia/varredura.json')); pior=[]
for a,b in [(0,98),(99,343),(344,447),(448,524)]:
    s=[x for x in r if a<=x[0]<=b]; pior.append(max(s,key=lambda x:x[2])[0])
ims=[]
for n in pior:
    d=np.abs(o(n).astype(int)-p(n).astype(int)).mean(2)<6; v=p(n).copy(); v[d]=(0,0,255); ims+= [sm(lab(o(n),f'orig n{n}')),sm(lab(p(n),'peca')),sm(v)]
cv2.imwrite('conferencia/varredura-px-iguais-piores.jpg',np.hstack(ims))
print('piores',pior)
