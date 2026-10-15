#!/usr/bin/env python3
# Manuela Freitas 1575322357678875 (35,37 s, 846 frames, 24 fps): troca SÓ a avatar. Molde medido por número de frame:
#   0-101    avatar tela cheia, legenda estilo 1 REDESENHADA (legenda1.py: Poppins Black, degradê, blur de entrada, sublinhado com glow)   -> clipe s1
#   102-107  flash (light leak); 104-106 quase brancos ficam do original; 102,103,107 misturam por brancura           -> s1
#   108-145  avatar tela cheia, legenda estilo 2 (branca com sombra)                                                    -> s1
#   146-238  b-roll do casal (original). 237-238 flash sobre o b-roll (original)
#   239-447  split: em cima a menina chorando (original), embaixo a avatar a partir de y~525 (rampa 520-536)            -> s2
#            239-241 e 445-447 brancos (original); 242, 443, 444 misturam por brancura
#   448-792  explicativo animado (original); 791-792 flash sobre ele (original)
#   793-845  avatar tela cheia (793-795 brancos = original, 796 mistura), CTA botão Learn More/redirecting + cursor     -> s3
# Áudio: stream original copiado. s1 = áudio 0-6,25 s (frame n -> clipe n), s2 = 9,9167 s (frame 238), s3 = 32,8333 s (frame 788).
# Camadas copiadas do original por cima do vídeo novo, só pixels do glifo/botão/cursor (nada do fundo antigo); sombra da legenda 2 sintética.
# Uso: python3 montar.py a1 [saida.mp4]
import json, subprocess, sys, os, numpy as np, cv2
os.chdir(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,'.'); import legenda1
A=sys.argv[1]; OUT=sys.argv[2] if len(sys.argv)>2 else f'pecas/manuela-{A}.mp4'
W,H,N,FPS=720,1280,846,24
REF='REFERENCIA-original.mp4'
SEG={'s1':0,'s2':238,'s3':788}
def ler(c):
    w,h=map(int,subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',c],capture_output=True,text=True).stdout.split(','))
    raw=subprocess.run(['ffmpeg','-v','error','-i',c,'-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,h,w,3)
C={s:ler(f'clipes/{A}-{s}.mp4') for s in SEG}
def suaviza(a,k=5):
    a=np.array(a,float); o=a.copy()
    for i in range(len(a)): o[i]=a[max(0,i-k//2):i+k//2+1].mean(0)
    return o
def preenche(t):
    t=list(t); idx=[i for i,v in enumerate(t) if v]
    for i in range(len(t)):
        if not t[i]: t[i]=t[min(idx,key=lambda j:abs(j-i))]
    return t
TC={s:suaviza(preenche(json.load(open(f'molde/rostos-{A}-{s}.json')))) for s in SEG}
RO=json.load(open('molde/rostos-original.json')); TO={}
for a,b in [(0,146),(239,448),(796,846)]:
    for i,v in enumerate(suaviza(preenche(RO[a:b]),9)): TO[a+i]=v
for n in range(793,796): TO[n]=TO[796]

def enquadra(img,src,dst):
    """leva o rosto src=(cx,cy,h,ang) do clipe a dst no quadro W x H, sem borda vazia (aumenta o zoom se preciso)"""
    sh,sw=img.shape[:2]; k=dst[2]/src[2]; d=np.radians(dst[3]-src[3]); sc=np.array(src[:2],float); tc=np.array(dst[:2],float)
    R=np.array([[np.cos(d),-np.sin(d)],[np.sin(d),np.cos(d)]])
    for _ in range(80):
        cs=np.array([[0,0],[W,0],[0,H],[W,H]],float)
        s=(np.linalg.inv(R)@((cs-tc).T)).T/k+sc; lo=s.min(0); hi=s.max(0)
        if hi[0]-lo[0]>sw-1 or hi[1]-lo[1]>sh-1: k*=1.02; continue
        dx=-lo[0] if lo[0]<0 else (sw-1-hi[0] if hi[0]>sw-1 else 0); dy=-lo[1] if lo[1]<0 else (sh-1-hi[1] if hi[1]>sh-1 else 0)
        if dx==0 and dy==0: break
        sc=sc+np.array([dx,dy])
    M=np.zeros((2,3)); M[:,:2]=k*R; M[:,2]=tc-k*R@sc
    return cv2.warpAffine(img,M,(W,H),flags=cv2.INTER_LANCZOS4,borderMode=cv2.BORDER_REFLECT)
O60=np.array([358.,643.,483.])                  # rosto da original no frame n60, de onde saiu a imagem-base
CM={s:np.median(TC[s][:,:3],0) for s in SEG}     # rosto mediano do clipe (enquadramento da imagem-base)
S0=W/704
def avatar(s,n):
    i=int(np.clip(n-SEG[s],1,len(C[s])-1))      # pula o frame 0 (é a imagem-base)
    t=TO[n]; kr=t[2]/O60[2]                      # transformação GLOBAL: segue zoom/posição da câmera da original RELATIVO ao n60,
    src=(CM[s][0],CM[s][1],CM[s][2],0)            # sem prender o rosto novo quadro a quadro (o movimento dela fica natural)
    dst=(t[0]+(CM[s][0]*S0-O60[0])*kr, t[1]+(CM[s][1]*S0-O60[1])*kr, CM[s][2]*S0*kr, 0)
    return enquadra(C[s][i],src,dst).astype(np.float32)

EL=lambda r: cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*r+1,2*r+1))
def comp(base,rgb,a): a=a[...,None]; return base*(1-a)+rgb*a
def limpa(m,minarea=10,maxh=90):
    m=m.astype(np.uint8); n,l,st,_=cv2.connectedComponentsWithStats(m)
    for i in range(1,n):
        if st[i,4]<minarea or st[i,3]>maxh: m[l==i]=0
    return m
def banda(y0,y1):
    b=np.zeros((H,W),bool); b[y0:y1]=True; return b
def leg1(o,of):
    """estilo 1: glifo claro neutro (degradê branco->cinza, inclusive borrado) + sublinhado vermelho com glow"""
    r,g,b=[o[...,i].astype(np.int16) for i in range(3)]; mn=np.minimum(np.minimum(r,g),b); mx=np.maximum(np.maximum(r,g),b)
    reg=banda(860,1110); reg[:,:3]=False; reg[:,712:]=False
    seed=limpa((mn>=212)&((mx-mn)<20)&reg,12,110)                       # núcleo do glifo (a cortina neutra fica < 212)
    core=((mn>=165)&((mx-mn)<24)&reg&(cv2.dilate(seed,EL(3))>0)).astype(np.uint8)   # cresce pro degradê/borrão só colado no núcleo
    a=cv2.GaussianBlur(cv2.dilate(core,EL(1)).astype(np.float32),(0,0),0.8)*np.clip((mn.astype(np.float32)-120)/60,0,1)
    red=((r>200)&(g>60)&((r-b)>45)&reg)
    rows=np.nonzero(red.sum(1)>120)[0]
    if len(rows):
        xs=np.nonzero(red[rows].any(0))[0]; s=np.zeros((H,W),np.float32); s[max(rows.min()-10,0):rows.max()+11,xs.min():xs.max()+1]=1
        core_l=(mn>215)&(np.abs(np.arange(H)[:,None]-rows.mean())<=4)                  # miolo claro do traço
        ar=s*np.clip((r.astype(np.float32)-150)/80,0,1)*np.clip(((r-g).astype(np.float32)-75)/35+core_l,0,1)   # só glow vermelho (pele tem r-g < 75)
        a=np.maximum(a,ar)
    return of,np.clip(a,0,1)
def leg2(o,of,reg):
    """estilo 2: glifo branco + sombra escura sintética"""
    r,g,b=[o[...,i].astype(np.int16) for i in range(3)]; mn=np.minimum(np.minimum(r,g),b); mx=np.maximum(np.maximum(r,g),b)
    core=limpa((mn>=222)&((mx-mn)<30)&reg,10,70)
    if core.sum()==0: return None
    fill=cv2.GaussianBlur(cv2.dilate(core,EL(1)).astype(np.float32),(0,0),0.7)
    sombra=np.roll(cv2.GaussianBlur(cv2.dilate(core,EL(2)).astype(np.float32),(0,0),2.5),(3,2),(0,1))*0.6
    alpha=np.clip(fill+sombra*(1-fill),0,1)
    rgb=np.zeros((H,W,3),np.float32)+np.array([40,40,40],np.float32); rgb=comp(rgb,np.full((H,W,3),252,np.float32),fill/np.maximum(alpha,1e-6))
    return rgb,alpha
def cta(o,of):
    """botão (rosa Learn More / verde redirecting, retângulo animado) + cursor de mão (branco com contorno preto)"""
    r,g,b=[o[...,i].astype(np.int16) for i in range(3)]; mn=np.minimum(np.minimum(r,g),b); mx=np.maximum(np.maximum(r,g),b)
    top=banda(120,330)
    btn=(((r>190)&(r-g>55)&(b<190))|((g>60)&(g-r>30)&(g-b>30)))&top
    btn=cv2.morphologyEx(btn.astype(np.uint8),cv2.MORPH_CLOSE,EL(4))
    n,l,st,_=cv2.connectedComponentsWithStats(btn); a=np.zeros((H,W),np.float32)
    if n<2: return None
    i=1+int(np.argmax(st[1:,4]))
    if st[i,4]<1500: return None
    x,y,w,h=st[i,:4]; m=np.zeros((H,W),np.uint8); m[y:y+h,x:x+w]=1
    m=cv2.morphologyEx(((l==i)|(m.astype(bool)&((mn>=200)|(l==i)))).astype(np.uint8),cv2.MORPH_CLOSE,EL(6))
    ff=m.copy(); mk=np.zeros((H+2,W+2),np.uint8); cv2.floodFill(ff,mk,(0,0),1); m=(m|(ff==0)).astype(np.uint8)   # fecha o texto dentro do botão
    a=np.maximum(a,cv2.GaussianBlur(m.astype(np.float32),(0,0),0.7))
    # cursor: componentes brancos abaixo/encostados no botão, depois branco+preto dentro da caixa deles
    reg=np.zeros((H,W),bool); reg[y+h-40:min(H,y+h+110),max(0,x-20):min(W,x+w+20)]=True
    wh=limpa((mn>=235)&((mx-mn)<25)&reg&(m==0),30,200)
    if wh.sum():
        ys,xs=np.nonzero(wh); cx0,cx1,cy0,cy1=max(xs.min()-6,0),xs.max()+7,max(ys.min()-6,0),ys.max()+7
        bx=np.zeros((H,W),bool); bx[cy0:cy1,cx0:cx1]=True
        cur=((wh>0)|((mx<60)&bx)); cur=cv2.morphologyEx(cur.astype(np.uint8),cv2.MORPH_CLOSE,EL(1))
        n2,l2,_,_=cv2.connectedComponentsWithStats(cur)
        keep=np.isin(l2,np.unique(l2[wh>0]))&(l2>0)
        a=np.maximum(a,cv2.GaussianBlur(keep.astype(np.float32),(0,0),0.6))
    return of,np.clip(a,0,1)
VIZ={102:101,103:101,107:108,242:243,443:442,444:442,796:797}
REFF=None
def flash(nv,n,of):
    nb=REFF[VIZ[n]].astype(np.float32)
    T=np.clip((255-of)/np.maximum(255-nb,1),0,1); T=cv2.GaussianBlur(T,(0,0),14)   # borrado: só a luz do flash, sem traço da pessoa
    return 255-(255-nv)*T

REFF=np.load('/private/tmp/claude-501/-Users-gustagoat-Documents-AIS-OS-projects-mentoria-spy/f3178e71-4f6d-4595-b5eb-81ed7e871241/scratchpad/ref.npy',mmap_mode='r')
def fonte(n,o,of):
    if n not in VIZ: return o,of
    v=np.ascontiguousarray(REFF[VIZ[n]]); return v,v.astype(np.float32)
PURO={104,105,106,237,238,239,240,241,445,446,447,448,791,792,793,794,795}
orig=subprocess.Popen(['ffmpeg','-v','error','-i',REF,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-hide_banner','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i',REF,
     '-map','0:v','-map','1:a','-c:a','copy','-frames:v',str(N),'-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p',
     '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
RAMPA=np.clip((np.arange(H)-520)/16,0,1).astype(np.float32)[:,None]
for n in range(N):
    o=np.frombuffer(orig.stdout.read(W*H*3),np.uint8).reshape(H,W,3); of=o.astype(np.float32); fr=of
    if n in PURO or 146<=n<=236 or 448<=n<=792: pass
    elif n<=145:
        fr=avatar('s1',n); lo,lof=fonte(n,o,of)       # no flash a legenda vem do vizinho e passa pelo mesmo flash
        if n<=103: fr=comp(fr,*legenda1.estado(n))
        else:
            L=leg2(lo,lof,banda(900,1110))
            if L: fr=comp(fr,*L)
        if n in VIZ: fr=flash(fr,n,of)
    elif 242<=n<=444:
        nv=avatar('s2',n); fr=comp(of,nv,RAMPA*np.ones((1,W),np.float32))
        lo,lof=fonte(n,o,of); L=leg2(lo,lof,banda(440,620)|banda(900,1110))
        if L: fr=comp(fr,*L)
        if n in VIZ: fr=flash(fr,n,of)
    else:  # 796-845
        fr=avatar('s3',n)
        lo,lof=fonte(n,o,of); c=cta(lo,lof)
        if c: fr=comp(fr,*c)
        L=leg2(lo,lof,banda(900,1110))
        if L: fr=comp(fr,*L)
        if n in VIZ: fr=flash(fr,n,of)
    enc.stdin.write(np.clip(fr,0,255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait(); print('ok ->',OUT)
