import subprocess,sys,json,numpy as np,cv2
p,seam=sys.argv[1],int(sys.argv[2]); M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
a,b=seam-20,seam+20
raw=subprocess.run(['ffmpeg','-v','error','-i',p,'-vf',f'select=between(n\\,{a}\\,{b})','-vsync','0','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
f=np.frombuffer(raw,np.uint8).reshape(-1,720,960,3)[:,:,:578]
det=cv2.FaceDetectorYN_create(M,'',(578,720),0.8,0.3,5000); L=[]
for x in f:
    d=det.detect(np.ascontiguousarray(x))[1]; q=max(d,key=lambda z:z[-1]); L.append(np.array(q[4:14]).reshape(5,2))
L=np.array(L); mv=np.linalg.norm(np.diff(L,axis=0),axis=2).mean(1)  # mv[i] = movimento de n(a+i) -> n(a+i+1)
k=seam-a; janela=mv[k-3:k+2]
print(np.round(mv[k-6:k+6],1)); print(f'{p.split("/")[-3][:4]} emenda n{seam}: salto máx {janela.max():.1f}px/frame na emenda | movimento típico (mediana ±20 fr) {np.median(mv):.1f} | p90 {np.percentile(mv,90):.1f}')
