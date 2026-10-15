#!/usr/bin/env python3
# Amanda Silva 1680455873461877 (Zap, 960x720, 30 fps, 1817 frames) com avatar E cenário novos (25/09). Composição frame a frame (numpy) -> ffmpeg.
# Molde medido (molde/medidas.json):
#   n 0-733    ela em quadro cheio (rosto cx 370, cy 239, h 307) + card "You Deserve The Truth" entrando da direita em n12-26 e parado em
#              x 632-912 / y 105-480 de n27 a n211; light leak laranja n211-215 (esconde o sumiço do card).
#   n 734-1816 split FIXO: janela dela x 0-577 (mesmo zoom, deslocada: rosto cx 291), tela do app opaca de x 578 até 959.
# Da peça original ficam: card, tela do app (x>=578 no split) e a luz do leak (extraída como camada aditiva suavizada). O resto é a avatar nova.
# Clipes Pruna (1088x832, 24 fps; frame 0 = imagem parada, pulado): c1 = n0-733, c2 = n734-1289, c3 = n1290-1816. Uso (de projects/mentoria-spy/): python3 .../montar.py <saida.mp4>
import subprocess, sys, json, numpy as np, cv2
D='centerpag-detect/criativos/var1-amanda-silva-1680455873461877-2026-09-25'; REF=f'{D}/REFERENCIA-original.mp4'; OUT=sys.argv[1]
M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'; W,H,N,FPS=960,720,1817,30; CW,CH=1088,832
def ler(p,w,h): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout,np.uint8).reshape(-1,h,w,3)
orig=ler(REF,W,H); assert len(orig)==N
CLIPES=[('c1',0,733),('c2',734,1289),('c3',1290,1816)]; SPLIT=734; XS=578
det=cv2.FaceDetectorYN_create(M,'',(CW,CH),0.86,0.3,5000)
clip={}
for c,a,b in CLIPES:
    f=ler(f'{D}/clipes/{c}.mp4',CW,CH); r=[]
    for x in f[1::6]:
        d=det.detect(np.ascontiguousarray(x))[1]
        if d is not None and len(d): q=max(d,key=lambda z:z[-1]); r.append((q[0]+q[2]/2,q[1]+q[3]/2,q[3]))
    cx,cy,h=np.median(np.array(r),0); clip[c]=(f,cx,cy,h,a,b); print(c,len(f),'rosto',round(cx),round(cy),round(h))
def enquadra(fr,cx,cy,h,tx,ty,th=307):
    s=max(th/h,W/CW,H/CH); sw,sh=int(round(CW*s)),int(round(CH*s)); big=cv2.resize(fr,(sw,sh),interpolation=cv2.INTER_LANCZOS4)
    x=int(min(max(cx*s-tx,0),sw-W)); y=int(min(max(cy*s-ty,0),sh-H)); return big[y:y+H,x:x+W]
# card: máscara por frame. Parado (n27-211): retângulo x 631-913, y 104-481. Entrada (n12-26): o que difere do n11 na faixa do card, em retângulo, +6 px.
card=np.zeros((N,H,W),bool); card[27:212,104:482,631:914]=True
for n in range(12,27):
    dif=np.abs(orig[n].astype(int)-orig[11].astype(int)).max(2)[104:482,600:]>30; cols=np.where(dif.mean(0)>0.3)[0]+600
    if len(cols): card[n,104:482,max(cols.min()-6,0):min(cols.max()+7,W)]=True
    esc=np.where((orig[n][110:470,880:].max(2)<30).mean(0)>0.6)[0]+880   # n12: só uma lasca preta na borda direita, fraca demais pra diferença
    if len(esc): card[n,104:482,max(esc.min()-3,0):W]=True
# light leak n211-215: camada aditiva = original - n216, mediana em blocos de 40 px (mata contorno de mão/cabelo), suavizada; só a parte positiva.
leak={}
ref=orig[216].astype(np.float32)
for n in range(211,216):
    d=orig[n].astype(np.float32)-ref; g=d.reshape(18,40,24,40,3).transpose(0,2,1,3,4).reshape(18,24,1600,3); g=np.median(g,2)
    L=cv2.GaussianBlur(cv2.resize(np.clip(g-6,0,None),(W,H),interpolation=cv2.INTER_CUBIC),(0,0),25); L[card[n]]=0; leak[n]=np.clip(L,0,None)
enc=subprocess.Popen(['ffmpeg','-hide_banner','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i',REF,
     '-map','0:v','-map','1:a','-c:a','copy','-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709',
     '-color_trc','bt709','-color_range','tv','-movflags','+faststart','-frames:v',str(N),OUT],stdin=subprocess.PIPE)
usado=[]
for n in range(N):
    c=[k for k,(f,cx,cy,h,a,b) in clip.items() if a<=n<=b][0]; f,cx,cy,h,a,b=clip[c]
    i=int(min(max(round((n-a)/FPS*24),1),len(f)-1)); usado.append((n,c,i))
    fr=enquadra(f[i],cx,cy,h,370,239) if n<SPLIT else enquadra(f[i],cx,cy,h,291,240)
    o=fr.copy()
    if n>=SPLIT: o[:,XS:]=orig[n][:,XS:]
    if n in leak: o=np.clip(o.astype(np.float32)+leak[n],0,255).astype(np.uint8)
    if card[n].any(): o[card[n]]=orig[n][card[n]]
    enc.stdin.write(o.tobytes())
enc.stdin.close(); enc.wait(); json.dump(usado,open(f'{D}/molde/mapa-frames.json','w')); print('ok ->',OUT)
