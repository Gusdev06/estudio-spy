import subprocess,numpy as np,cv2
raw=subprocess.run(['ffmpeg','-v','error','-i','REFERENCIA-original.mp4','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
F=np.frombuffer(raw,np.uint8).reshape(-1,1280,720,3)
np.save('work/F.npy',F)
idx=[n for n in range(0,1822,3) if not (1057<=n<=1245) and not any(a<=n<=a+10 for a in [174,229,400,1359,1460])]
plate=np.median(F[idx],axis=0).astype(np.uint8); cv2.imwrite('work/plate.png',plate)
iv={'A':(12,170),'C':(246,395),'D':(416,684),'E':(711,1050),'F':(1068,1232),'G':(1256,1350),'H':(1370,1452),'I':(1476,1600),'J':(1635,1812)}
for k,(a,b) in iv.items():
    X=F[a:b+1:2].astype(np.float32); M=np.median(X,axis=0); S=X.std(0).mean(2)
    cv2.imwrite(f'work/M_{k}.png',M.astype(np.uint8)); np.save(f'work/S_{k}.npy',S)
    Sv=np.clip(S*8,0,255).astype(np.uint8)
    D=np.clip(np.abs(M-plate.astype(np.float32)).mean(2)*3,0,255).astype(np.uint8)
    im=np.hstack([M.astype(np.uint8),cv2.cvtColor(Sv,cv2.COLOR_GRAY2BGR),cv2.cvtColor(D,cv2.COLOR_GRAY2BGR)])
    cv2.imwrite(f'work/est_{k}.jpg',cv2.resize(im,(1080,640)))
