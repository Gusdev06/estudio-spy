import subprocess,numpy as np,cv2
M='/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
raw=subprocess.run(['ffmpeg','-v','error','-i','REFERENCIA-original.mp4','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
f=np.frombuffer(raw,np.uint8).reshape(-1,1280,720,3); print(len(f))
np.save('work/frames_small.npy',f[:,::4,::4])
det=cv2.FaceDetectorYN_create(M,'',(720,1280),0.6,0.3,5000)
out=open('work/medida.tsv','w'); prev=None
for i,x in enumerate(f):
    d=det.detect(np.ascontiguousarray(x))[1]
    g=x.astype(np.float32)
    dif=0 if prev is None else np.abs(g-prev).mean(); prev=g
    b,gg,r=g[...,0].mean(),g[...,1].mean(),g[...,2].mean()
    if d is not None and len(d):
        a=max(d,key=lambda q:q[-1]); fs=f'{a[0]+a[2]/2:.0f}\t{a[1]+a[3]/2:.0f}\t{a[3]:.0f}\t{a[-1]:.2f}\t{len(d)}'
    else: fs='-\t-\t-\t-\t0'
    out.write(f'{i}\t{i/30:.2f}\t{dif:.1f}\t{r:.0f}\t{gg:.0f}\t{b:.0f}\t{fs}\n')
