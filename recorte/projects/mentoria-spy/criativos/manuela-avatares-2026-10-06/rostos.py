#!/usr/bin/env python3
# Trilha de rosto (YuNet, meia resolução): cx, cy, h, ângulo dos olhos. Uso: python3 rostos.py original | <clipe> ...
# original: só nos frames de avatar (0-107, 108-145, split 239-447 com rosto abaixo de y 525, 796-845).
import subprocess, sys, os, json, numpy as np, cv2
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M='/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
def frames(c):
    w,h=map(int,subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',c],capture_output=True,text=True).stdout.split(','))
    raw=subprocess.run(['ffmpeg','-v','error','-i',c,'-vf',f'scale={w//2}:{h//2}','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,h//2,w//2,3)
def trilha(f, ymin=None, so=None):
    h,w=f.shape[1:3]; det=cv2.FaceDetectorYN_create(M,'',(w,h),0.6,0.3,5000); out=[]
    for i,x in enumerate(f):
        if so is not None and i not in so: out.append(None); continue
        d=det.detect(np.ascontiguousarray(x))[1]
        if d is not None and ymin is not None and i in ymin: d=[r for r in d if r[1]+r[3]/2>ymin[i]/2]
        if d is None or len(d)==0: out.append(None); continue
        r=max(d,key=lambda r:r[2]*r[3])
        ang=float(np.degrees(np.arctan2(r[7]-r[5],r[6]-r[4])))
        out.append([float(r[0]+r[2]/2)*2,float(r[1]+r[3]/2)*2,float(r[3])*2,ang])
    return out
for alvo in sys.argv[1:]:
    if alvo=='original':
        f=frames('REFERENCIA-original.mp4'); so=set(range(0,146))|set(range(239,448))|set(range(796,846))
        ymin={i:525 for i in range(239,448)}
        json.dump(trilha(f,ymin,so),open('molde/rostos-original.json','w'))
    else:
        json.dump(trilha(frames(f'clipes/{alvo}.mp4')),open(f'molde/rostos-{alvo}.json','w'))
    print('ok',alvo)
