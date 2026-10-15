#!/usr/bin/env python3
# Varredura final frame a frame: peça x original. Dupla original (n 0-266, 885-1025) não pode sobrar na janela; fora da janela e painéis = original.
# Gera conferencia/orig-vs-peca-10.jpg, emendas.jpg, leak-transicao.jpg. Uso (de projects/mentoria-spy/): python3 .../varredura.py
import subprocess, numpy as np, cv2, os
L=os.path.relpath(os.path.dirname(os.path.abspath(__file__))); REF=f'{L}/REFERENCIA-original.mp4'; PEC=f'{L}/pecas/variacao.mp4'
M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'; W,H=360,640; WY0,WY1=168,471
def ler(a):
    raw=subprocess.run(['ffmpeg','-v','error','-i',a,'-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,H,W,3)
def md5(a): return subprocess.run(['ffmpeg','-v','error','-i',a,'-map','0:a','-f','md5','-'],capture_output=True,text=True).stdout.strip()
O=ler(REF); P=ler(PEC); fps=subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=r_frame_rate','-of','csv=p=0',PEC],capture_output=True,text=True).stdout.strip()
print('frames',len(O),len(P),'fps',fps,'audio',md5(REF),md5(PEC))
D=list(range(0,267))+list(range(885,1026)); PN=range(267,885)
def bordas(x):
    g=cv2.cvtColor(x,cv2.COLOR_BGR2GRAY).astype(np.float32); m=cv2.magnitude(cv2.Sobel(g,cv2.CV_32F,1,0),cv2.Sobel(g,cv2.CV_32F,0,1)); m-=m.mean(); return m/(np.linalg.norm(m)+1e-6)
dif=np.array([np.abs(O[n,WY0:WY1].astype(int)-P[n,WY0:WY1]).mean() for n in D])
cor=np.array([(bordas(O[n,WY0:WY1])*bordas(P[n,WY0:WY1])).sum() for n in D])
fora=max(max(np.abs(O[n,:WY0].astype(int)-P[n,:WY0]).mean(),np.abs(O[n,WY1:].astype(int)-P[n,WY1:]).mean()) for n in range(len(O)))
pain=max(np.abs(O[n].astype(int)-P[n]).mean() for n in PN)
det=cv2.FaceDetectorYN_create(M,'',(W,H),0.86,0.3,5000); nf=[]
for x in P:
    d=det.detect(np.ascontiguousarray(x))[1]; nf.append(0 if d is None else len(d))
nf=np.array(nf)
print(f'dupla ({len(D)} fr): dif janela mediana {np.median(dif):.1f} min {dif.min():.1f} (n {D[int(dif.argmin())]}); corr bordas max {cor.max():.2f} (n {D[int(cor.argmax())]}) mediana {np.median(cor):.2f}')
print(f'fora da janela dif max {fora:.1f}; painéis dif max {pain:.1f}; YuNet rostos/frame max {nf.max()} (frames com >1: {list(np.where(nf>1)[0])[:10]}); dupla sem rosto: {int((nf[D]==0).sum())} fr')
C=f'{L}/conferencia'
def lab(x,t):
    x=x.copy(); cv2.putText(x,t,(6,20),cv2.FONT_HERSHEY_SIMPLEX,0.55,(0,255,255),2); return x
def folha(ns,arq):
    cv2.imwrite(f'{C}/{arq}',np.vstack([np.hstack([lab(O[n],f'orig {n}') for n in ns]),np.hstack([lab(P[n],f'peca {n}') for n in ns])]),[cv2.IMWRITE_JPEG_QUALITY,80])
folha([10,60,110,140,200,240,262,900,960,1020],'orig-vs-peca-10.jpg')
folha([115,116,117,118,224,225,226,227],'emendas-1.jpg'); folha([264,265,266,267,883,884,885,886],'emendas-2.jpg')
folha([260,261,262,263,264,265,266,267],'leak-transicao.jpg')
