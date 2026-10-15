#!/usr/bin/env python3
"""medir-olhos.py <video|png> [frames…]  — olhos (y %), largura do rosto (%), queixo (y %) via Haar (OpenCV).
Roda no venv do scratchpad (cv2). Para vídeo: frames dados; para png: só a imagem."""
import sys, subprocess, numpy as np, cv2
p=sys.argv[1]; idx=[int(x) for x in sys.argv[2:]] or [0]
face=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
def load(i):
    if p.lower().endswith('.png') or p.lower().endswith('.jpg'):
        return cv2.imread(p)
    W,H=[int(x) for x in subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','csv=p=0',p],capture_output=True,text=True).stdout.strip().split(',')]
    raw=subprocess.run(['ffmpeg','-v','error','-i',p,'-vf',f"select='eq(n\\,{i})'",'-vsync','0','-frames:v','1','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(H,W,3).copy()
for i in idx:
    img=load(i); H,W=img.shape[:2]; g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(g,1.05,5,minSize=(W//6,W//6))
    if len(faces)==0: print(f'{p} frame {i}: sem rosto'); continue
    x,y,w,h=max(faces,key=lambda f:f[2]*f[3])
    roi=g[y:y+int(h*0.6),x:x+w]
    eyes=eye.detectMultiScale(roi,1.05,4,minSize=(w//10,w//10))
    eyes=sorted(eyes,key=lambda e:e[0])
    ey=[y+e[1]+e[3]/2 for e in eyes]; ex=[x+e[0]+e[2]/2 for e in eyes]
    eyy=np.median(ey) if ey else float('nan')
    print(f'{p} frame {i}: {W}x{H} · rosto x{x}-{x+w} y{y}-{y+h} (largura {w} = {100*w/W:.1f} % da largura; queixo≈y{y+h} = {100*(y+h)/H:.1f} %) · olhos n={len(eyes)} y≈{eyy:.0f} = {100*eyy/H:.1f} % · x={[round(v) for v in ex]}')
    # anotar
    out=img.copy(); cv2.rectangle(out,(x,y),(x+w,y+h),(0,255,255),3)
    for e in eyes: cv2.circle(out,(int(x+e[0]+e[2]/2),int(y+e[1]+e[3]/2)),12,(0,0,255),3)
    if ey: cv2.line(out,(0,int(eyy)),(W,int(eyy)),(0,0,255),2)
    cv2.imwrite(f"medicao/olhos-{p.split('/')[-1].rsplit('.',1)[0]}-f{i}.jpg",out,[cv2.IMWRITE_JPEG_QUALITY,80])
