# Varredura final frame a frame: onde a peça é IGUAL ao original (|dif|<8 nos 3 canais) fora das áreas herdadas de propósito
# (card n12-211, tela do app x>=578 no split), e quantos rostos (score>=0,86) a peça tem fora da tela do app. Aponta os piores frames.
import subprocess,json,numpy as np,cv2
D='centerpag-detect/criativos/var6-amanda-silva-1680455873461877-2026-09-25'; M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
def ler(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout,np.uint8).reshape(-1,720,960,3)
o=ler(f'{D}/REFERENCIA-original.mp4'); p=ler(f'{D}/pecas/variacao.mp4'); med=json.load(open(f'{D}/molde/medidas.json'))
det=cv2.FaceDetectorYN_create(M,'',(960,720),0.86,0.3,5000); res=[]
for n in range(len(o)):
    eq=(np.abs(o[n].astype(int)-p[n].astype(int)).max(2)<8)
    livre=np.ones((720,960),bool)
    if n>=734: livre[:,578:]=False
    if 12<=n<=211: livre[100:486,560:]=False   # card e sua faixa de entrada
    fr=float(eq[livre].mean()); fb=0.0
    if med[n]['faces']:
        x,y,w,h=[int(v) for v in med[n]['faces'][0][:4]]; box=eq[max(y,0):y+h,max(x,0):x+w]; fb=float(box.mean()) if box.size else 0
    d=det.detect(np.ascontiguousarray(p[n] if n<734 else np.where(np.arange(960)[None,:,None]<578,p[n],0).astype(np.uint8)))[1]
    res.append((n,round(fr,4),round(fb,4),0 if d is None else len(d)))
a=np.array(res)
print('frames:',len(a),'| igual ao original fora das áreas herdadas: média',a[:,1].mean().round(4),'máx',a[:,1].max(),'em n',int(a[a[:,1].argmax(),0]))
print('dentro da caixa do rosto original: máx',a[:,2].max(),'em n',int(a[a[:,2].argmax(),0]))
print('rostos na peça (fora da tela do app): min',int(a[:,3].min()),'máx',int(a[:,3].max()),'| frames com !=1:',[int(r[0]) for r in a if r[3]!=1][:30])
print('top 8 por igualdade:',sorted(res,key=lambda r:-r[1])[:8])
json.dump(res,open(f'{D}/conferencia/varredura.json','w'))
