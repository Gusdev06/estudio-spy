# Mede o molde: por frame -> diff vs anterior, rosto (YuNet por score), borda esquerda do painel escuro (split) e caixa escura flutuante.
import subprocess,numpy as np,cv2,json,sys
D='centerpag-detect/criativos/var4-amanda-silva-1680455873461877-2026-09-25'; M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
raw=subprocess.run(['ffmpeg','-v','error','-i',f'{D}/REFERENCIA-original.mp4','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
f=np.frombuffer(raw,np.uint8).reshape(-1,720,960,3); print(len(f))
det=cv2.FaceDetectorYN_create(M,'',(960,720),0.6,0.3,5000); out=[]; prev=None
for i,x in enumerate(f):
    g=cv2.cvtColor(x,cv2.COLOR_BGR2GRAY).astype(np.float32)
    d=0 if prev is None else float(np.abs(g[::4,::4]-prev[::4,::4]).mean()); prev=g
    r=det.detect(np.ascontiguousarray(x))[1]; faces=[] if r is None else sorted([[float(v) for v in q[:4]]+[float(q[-1])] for q in r],key=lambda q:-q[-1])
    dark=(g<45).mean(0)  # fração de linhas escuras por coluna
    out.append({'n':i,'diff':round(d,2),'faces':[[round(v,1) for v in q] for q in faces[:3]],'dark':[round(float(v),2) for v in dark[::8]]})
json.dump(out,open(f'{D}/molde/medidas.json','w'))
