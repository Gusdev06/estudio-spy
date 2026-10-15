#!/usr/bin/env python3
# Varredura final (25/09): em TODO frame onde o homem original aparece no ORIGINAL (n 0-524), mede quantos pixels da máscara dele
# (segmentação MediaPipe, dilatada 4 px) continuam iguais na peça (|dif| média RGB < 6) e conta rostos (YuNet ≥ 0,86) na peça.
# Uso (desta pasta, venv do mediapipe): <segenv>/bin/python varredura.py
import numpy as np, cv2, json, sys
sys.path.insert(0,'.'); from seg import seg
M='../../../gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'; det=cv2.FaceDetectorYN_create(M,'',(720,1280),0.86,0.3,5000)
R=json.load(open('molde/rostos-original.json')); res=[]
for n in range(601):
    o=cv2.imread(f'frames/full/{n:03d}.png'); p=cv2.imread(f'frames/peca/{n:03d}.png')
    d=det.detect(p)[1]; nf=0 if d is None else len(d)
    if R[str(n)] is None: res.append((n,0,0,nf)); continue
    _,P=seg(o); cx,cy,h=R[str(n)][:3]
    m=np.maximum.reduce([P['hair'],P['face'],P['clothes']])>0.5
    m=cv2.dilate(m.astype(np.uint8),np.ones((9,9),np.uint8))>0
    ig=(np.abs(o.astype(int)-p.astype(int)).mean(2)<6)&m
    res.append((n,int(m.sum()),int(ig.sum()),nf))
json.dump(res,open('conferencia/varredura.json','w'))
r=np.array(res); com=r[r[:,1]>0]
print('frames com o homem no original:',len(com),'| px iguais na peça: médio',com[:,2].mean().round(1),'máx',com[:,2].max(),'no n',com[np.argmax(com[:,2]),0])
print('frames da peça com != 1 rosto (n<=524):',[(int(a),int(d)) for a,b,c,d in r if a<=524 and d!=1][:40])
for a,b in [(0,98),(99,343),(344,447),(448,524)]:
    s=com[(com[:,0]>=a)&(com[:,0]<=b)]; print(f'n {a}-{b}: px iguais médio {s[:,2].mean():.0f} máx {s[:,2].max()} (máscara média {s[:,1].mean():.0f})')
