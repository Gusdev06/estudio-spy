# Legenda de abertura (frames 0-101) REDESENHADA: Poppins Black, tracking negativo, degradê branco -> cinza no último terço da letra,
# entrada com blur, palavras/letras surgindo e sublinhado vermelho com glow crescendo da esquerda. Geometria e tempos medidos no original.
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
W,H=720,1280
FONTE='fontes/Poppins-Black.ttf'
def _fit(txt,cap,largura):
    for s in range(40,90):
        F=ImageFont.truetype(FONTE,s); capH=F.getbbox('I')[3]-F.getbbox('I')[1]
        if capH>=cap: break
    nsp=sum(1 for c in txt if c!=' '); tr=(largura-F.getlength(txt))/max(nsp-1,1); return F,tr
def _linha(txt,cap_top,cx,largura,cap,vis=None):
    """máscara (alpha) da linha; vis[i] = opacidade da letra i"""
    F,tr=_fit(txt,cap,largura); m=np.zeros((H,W),np.float32)
    bI=F.getbbox('I'); x=cx-largura/2; y=cap_top-bI[1]
    for i,ch in enumerate(txt):
        a=1.0 if vis is None else vis[i]
        if a>0:
            im=Image.new('L',(W,H),0); ImageDraw.Draw(im).text((x,y),ch,font=F,fill=255)
            m=np.maximum(m,np.asarray(im,np.float32)/255*a)
        x+=F.getlength(ch)+(0 if ch==' ' else tr)
    return m,cap_top,cap_top+cap
def _cor(m,top,bot):
    g=np.ones(H,np.float32)*252; yy=np.arange(H)
    k=np.clip((yy-(top+0.62*(bot-top)))/(0.38*(bot-top)),0,1); g=g-(252-160)*k
    return np.repeat(g[:,None],W,1)
LIN={'A':("If you think someone",929,360,596,44),'B':("from you",993,358,268,40),'C':("don't dismiss that",882,359,488,39),'D':("that feeling too quickly.",944,360,620,38)}
CACHE={}
def linha(k,vis=None):
    key=(k,None if vis is None else tuple(np.round(vis,2)))
    if key not in CACHE:
        t,top,cx,w,cap=LIN[k]; m,a,b=_linha(t,top,cx,w,cap,vis=vis); CACHE[key]=(m,_cor(m,a,b))
    return CACHE[key]
def _rev(txt,f0,f1,n):   # letras surgem uma a uma com fade de 3 frames
    L=len(txt); return [float(np.clip((n-(f0+(f1-f0)*i/max(L-1,1)))/3,0,1)) for i in range(L)]
def sublinhado(y,x0,x1):
    m=np.zeros((H,W),np.float32); cv2.line(m,(int(x0),y),(int(x1),y),1.0,5)
    glow=cv2.GaussianBlur(m,(0,0),6)*2.2
    return np.clip(m,0,1),np.clip(glow,0,1)
def estado(n):
    """devolve (rgb, alpha) da legenda 1 no frame n (n>101 congela no 101)"""
    n=min(n,101); camadas=[]
    def add(k,vis=None,blur=0,op=1.0):
        m,c=linha(k,vis)
        if blur>0: m=cv2.GaussianBlur(m,(0,0),blur)
        camadas.append((c,m*op))
    if 8<=n<=42:  add('A',blur=max(0,(16-n)*1.6),op=min(1,0.25+(n-8)*0.1))
    if 44<=n<=55:
        add('B',vis=_rev("from you",44,50,n))
        if n>=52: u,g=sublinhado(1050,224,224+(492-224)*min(1,(n-51)/3)); camadas.append(('ul',(u,g)))
    if 64<=n:
        add('C',blur=max(0,(72-n)*1.6),op=min(1,0.25+(n-64)*0.1))
        if n>=80: add('D',vis=_rev("that feeling too quickly.",80,97,n))
        if n>=88: u,g=sublinhado(1011,34,34+(685-34)*min(1,(n-87)/5)); camadas.append(('ul',(u,g)))
    rgb=np.zeros((H,W,3),np.float32); a=np.zeros((H,W),np.float32)
    for c,m in camadas:
        if isinstance(c,str):
            u,g=m; cg=np.array([235,70,55],np.float32); cu=np.array([255,190,170],np.float32)
            for col,al in ((cg,g*0.85),(cu,u)):
                rgb=rgb*(1-al[...,None])*1+col*al[...,None]*1; a=a+al*(1-a)
            continue
        sh=np.roll(cv2.GaussianBlur(m,(0,0),3),(3,0),(0,1))*0.45     # sombra suave
        rgb=rgb*(1-sh[...,None]); a=a+sh*(1-a)
        rgb=rgb*(1-m[...,None])+np.repeat(c[...,None],3,2)*m[...,None]; a=a+m*(1-a)
    return rgb/np.maximum(a[...,None],1e-6)*(a[...,None]>0), a
