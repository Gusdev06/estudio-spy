# Trilha do rosto nos clipes s* (mesma convenção de molde/rostos-original.json): YuNet em meia resolução, por frame do clipe (24 fps):
# [cx, cy, h, ângulo dos olhos em graus, score] em pixels do clipe; None quando não acha. Uso: python3 rostos.py s1 s2 s3
import subprocess,sys,os,json,numpy as np,cv2
os.chdir(os.path.dirname(os.path.abspath(__file__))); M='../../scripts/modelos/face_detection_yunet_2023mar.onnx'
for k in sys.argv[1:]:
    c=f'clipes/{k}.mp4'; w,h=map(int,subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',c],capture_output=True,text=True).stdout.split(','))
    raw=subprocess.run(['ffmpeg','-v','error','-i',c,'-vf',f'scale={w//2}:{h//2}','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    f=np.frombuffer(raw,np.uint8).reshape(-1,h//2,w//2,3); det=cv2.FaceDetectorYN_create(M,'',(w//2,h//2),0.5,0.3,5000); out=[]
    for x in f:
        d=det.detect(np.ascontiguousarray(x))[1]
        if d is None or not len(d): out.append(None); continue
        r=max(d,key=lambda r:r[-1]); bx,by,bw,bh=[float(v)*2 for v in r[:4]]; le=r[4:6]*2; re=r[6:8]*2
        out.append([bx+bw/2,by+bh/2,bh,float(np.degrees(np.arctan2(re[1]-le[1],re[0]-le[0]))),float(r[-1])])
    json.dump(out,open(f'molde/rostos-{k}.json','w')); print(k,len(out),'frames, sem rosto:',sum(v is None for v in out))
