#!/usr/bin/env python3
# Amanda Silva 1680455873461877 (Zap, 960x720, 30 fps, 1817 frames): avatar e cenário novos (25/09). Mesmo molde da var1 (ver README da var1):
#   n 0-733 quadro cheio (rosto cx 370, cy 239, h 307) + card "You Deserve The Truth" n12-211 + light leak n211-215; n 734-1816 split fixo
#   (janela dela x 0-577, rosto cx 291; tela do app original de x 578 em diante).
# DIFERENÇA para a var1, na emenda c2|c3: os clipes se sobrepõem 40,9-41,45 s (n1227-1243), dentro da pausa de fala 40,75-41,65 s.
#   1) a emenda (SEAM) é o frame, entre n1230 e n1240, em que a pose de c2 e c3 mais se parece (5 landmarks YuNet, já enquadrados);
#   2) o enquadramento do c3 começa casado com o do c2 no SEAM (translação medida no quadro já recortado + escala) e volta ao dele em 24 frames;
#   3) crossfade de 3 frames (n SEAM-1..SEAM+1).
# Clipes Pruna 1088x832, 24 fps; frame 0 = imagem parada (pulado). Uso (de projects/mentoria-spy/): python3 .../montar.py <saida.mp4>
import subprocess, sys, json, numpy as np, cv2
D='centerpag-detect/criativos/var4-amanda-silva-1680455873461877-2026-09-25'; REF=f'{D}/REFERENCIA-original.mp4'; OUT=sys.argv[1]
M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'; W,H,N,FPS=960,720,1817,30; CW,CH=1088,832
def ler(p,w,h): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout,np.uint8).reshape(-1,h,w,3)
orig=ler(REF,W,H); assert len(orig)==N
T0={'c1':0.0,'c2':734/30,'c3':40.9}; SPLIT=734; XS=578; RAMP=24
det=cv2.FaceDetectorYN_create(M,'',(CW,CH),0.86,0.3,5000)
def rosto(x):
    d=det.detect(np.ascontiguousarray(x))[1]
    return None if d is None or not len(d) else max(d,key=lambda z:z[-1])
clip={}
for c in T0:
    f=ler(f'{D}/clipes/{c}.mp4',CW,CH); r=[q for q in (rosto(x) for x in f[1::6]) if q is not None]
    r=np.array([(q[0]+q[2]/2,q[1]+q[3]/2,q[3]) for q in r]); clip[c]=(f,*np.median(r,0)); print(c,len(f),'rosto',*np.round(np.median(r,0)))
def idx(c,n): return int(min(max(round((n/FPS-T0[c])*24),1),len(clip[c][0])-1))
def escala(c,th): return max(th/clip[c][3],W/CW,H/CH)
def enquadra(fr,cx,cy,h,tx,ty,th=307,dx=0.0,dy=0.0):
    # escala pra rosto h=th e põe o rosto mediano do clipe em (tx,ty); o recorte é limitado à imagem (clamp). dx/dy: deslocamento extra
    # aplicado DEPOIS do clamp (correção da emenda), também limitado à imagem.
    s=max(th/h,W/CW,H/CH); sw,sh=int(round(CW*s)),int(round(CH*s)); big=cv2.resize(fr,(sw,sh),interpolation=cv2.INTER_LANCZOS4)
    x=min(max(cx*s-tx,0),sw-W); y=min(max(cy*s-ty,0),sh-H)
    if not (dx or dy): return big[int(round(y)):int(round(y))+H,int(round(x)):int(round(x))+W]
    # na correção da emenda o recorte pode passar da borda (clipe já no limite): espelha até 64 px (só perto da emenda, e decai em RAMP frames)
    P=64; big=cv2.copyMakeBorder(big,P,P,P,P,cv2.BORDER_REFLECT101); x=int(round(min(max(x-dx,-P),sw-W+P)))+P; y=int(round(min(max(y-dy,-P),sh-H+P)))+P
    return big[y:y+H,x:x+W]
det_out=cv2.FaceDetectorYN_create(M,'',(XS,H),0.8,0.3,5000)
def lm_saida(c,n,th=307):   # landmarks (5 pts) e altura do rosto do clipe c no frame n, medidos no quadro JÁ ENQUADRADO do split (com clamp, como sai na peça)
    f,cx,cy,h=clip[c]; d=det_out.detect(np.ascontiguousarray(enquadra(f[idx(c,n)],cx,cy,h,291,240,th)[:,:XS].copy()))
    d=d[1] if d[1] is not None else None
    if d is None or not len(d): return None
    q=max(d,key=lambda z:z[-1]); return np.array(q[4:14]).reshape(5,2),q[3]
# escolha da emenda
best=None; log=[]
for n in range(1230,1241):
    a,b=lm_saida('c2',n),lm_saida('c3',n)
    if a is None or b is None: continue
    t=a[0].mean(0)-b[0].mean(0); forma=np.linalg.norm((a[0]-a[0].mean(0))-(b[0]-b[0].mean(0)),axis=1).mean()
    custo=forma+0.3*np.linalg.norm(t)+0.3*abs(a[1]-b[1]); log.append((n,round(float(custo),1),round(float(forma),1),[round(float(v),1) for v in t]))
    if best is None or custo<best[1]: best=(n,custo,t,a[1]/b[1])
SEAM,_,DT,DS=best
b2=lm_saida('c3',SEAM,307*DS); DT=lm_saida('c2',SEAM)[0].mean(0)-b2[0].mean(0)   # deslocamento remedido já com a escala corrigida
print('emenda n',SEAM,'custo',round(float(best[1]),1),'desloc',DT.round(1),'escala',round(float(DS),3)); print(log)
CLIPES=[('c1',0,733),('c2',734,SEAM-1),('c3',SEAM,1816)]
# card (igual à var1)
card=np.zeros((N,H,W),bool); card[27:212,104:482,631:914]=True
for n in range(12,27):
    dif=np.abs(orig[n].astype(int)-orig[11].astype(int)).max(2)[104:482,600:]>30; cols=np.where(dif.mean(0)>0.3)[0]+600
    if len(cols): card[n,104:482,max(cols.min()-6,0):min(cols.max()+7,W)]=True
    esc=np.where((orig[n][110:470,880:].max(2)<30).mean(0)>0.6)[0]+880
    if len(esc): card[n,104:482,max(esc.min()-3,0):W]=True
# light leak (igual à var1)
leak={}; ref=orig[216].astype(np.float32)
for n in range(211,216):
    d=orig[n].astype(np.float32)-ref; g=d.reshape(18,40,24,40,3).transpose(0,2,1,3,4).reshape(18,24,1600,3); g=np.median(g,2)
    L=cv2.GaussianBlur(cv2.resize(np.clip(g-6,0,None),(W,H),interpolation=cv2.INTER_CUBIC),(0,0),25); L[card[n]]=0; leak[n]=np.clip(L,0,None)
def quadro(c,n):
    f,cx,cy,h=clip[c]; fr=f[idx(c,n)]
    if n<SPLIT: return enquadra(fr,cx,cy,h,370,239)
    if c=='c3':   # casa com o c2 na emenda e volta ao próprio enquadramento em RAMP frames
        w=float(np.clip(1-(n-SEAM)/RAMP,0,1)); return enquadra(fr,cx,cy,h,291,240,307*(1+w*(DS-1)),w*DT[0],w*DT[1])
    return enquadra(fr,cx,cy,h,291,240)
enc=subprocess.Popen(['ffmpeg','-hide_banner','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i',REF,
     '-map','0:v','-map','1:a','-c:a','copy','-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709',
     '-color_trc','bt709','-color_range','tv','-movflags','+faststart','-frames:v',str(N),OUT],stdin=subprocess.PIPE)
FADE={SEAM-1:0.25,SEAM:0.5,SEAM+1:0.75}; usado=[]
for n in range(N):
    c=[k for k,a,b in CLIPES if a<=n<=b][0]
    if n in FADE:
        w=FADE[n]; fr=np.clip(quadro('c2',n).astype(np.float32)*(1-w)+quadro('c3',n).astype(np.float32)*w+0.5,0,255).astype(np.uint8); c=f'c2>c3 {w}'
    else: fr=quadro(c,n)
    usado.append((n,c,idx(c.split('>')[0] if '>' not in c else 'c3',n)))
    o=fr.copy()
    if n>=SPLIT: o[:,XS:]=orig[n][:,XS:]
    if n in leak: o=np.clip(o.astype(np.float32)+leak[n],0,255).astype(np.uint8)
    if card[n].any(): o[card[n]]=orig[n][card[n]]
    enc.stdin.write(o.tobytes())
enc.stdin.close(); enc.wait()
json.dump({'emenda':int(SEAM),'desloc':[float(v) for v in DT],'escala':float(DS),'candidatos':log,'frames':usado},open(f'{D}/molde/mapa-frames.json','w')); print('ok ->',OUT)
