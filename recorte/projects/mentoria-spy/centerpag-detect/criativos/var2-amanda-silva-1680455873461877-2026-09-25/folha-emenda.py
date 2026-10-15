import subprocess,sys,json,numpy as np,cv2
D=sys.argv[1]; s=json.load(open(f'{D}/molde/mapa-frames.json'))['emenda']; a,b=s-3,s+3
raw=subprocess.run(['ffmpeg','-v','error','-i',f'{D}/pecas/variacao.mp4','-vf',f'select=between(n\\,{a}\\,{b})','-vsync','0','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
f=np.frombuffer(raw,np.uint8).reshape(-1,720,960,3)
ims=[cv2.putText(cv2.resize(np.ascontiguousarray(x[:,:578]),(289,360)),f'n{a+i}',(5,25),0,0.8,(0,0,255),2) for i,x in enumerate(f)]
cv2.imwrite(sys.argv[2],np.hstack(ims),[cv2.IMWRITE_JPEG_QUALITY,85])
