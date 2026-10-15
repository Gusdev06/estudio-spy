import subprocess,numpy as np,cv2,sys
raw=subprocess.run(['ffmpeg','-v','error','-i','REFERENCIA-original.mp4','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
F=np.frombuffer(raw,np.uint8).reshape(-1,1280,720,3)
def strip(ns,out,w=240):
    ims=[]
    for n in ns:
        x=cv2.resize(F[n],(w,int(1280*w/720)),interpolation=cv2.INTER_AREA).copy()
        cv2.putText(x,f'n{n}',(5,28),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,255),2); ims.append(x)
    cv2.imwrite(out,np.hstack(ims),[cv2.IMWRITE_JPEG_QUALITY,85])
strip(range(0,11),'work/anim_0.jpg'); strip(range(236,247),'work/anim_236.jpg'); strip(range(698,710),'work/anim_700.jpg')
strip(range(1243,1254),'work/anim_1243.jpg'); strip(range(1600,1624,2),'work/anim_1600.jpg'); strip(range(174,186),'work/flash_174.jpg')
