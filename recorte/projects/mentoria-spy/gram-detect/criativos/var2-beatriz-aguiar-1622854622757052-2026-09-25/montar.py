#!/usr/bin/env python3
# Beatriz Aguiar 1622854622757052 (Gram, 46,0 s, 1380 frames 30 fps) com PESSOAS e CENÁRIOS novos (25/09).
# Tudo por NÚMERO DE FRAME (molde medido, ver README):
#   0-308     esquete (vídeo em y 112-1279, faixa preta 0-111 + título branco estático): 0-214 plano da porta (eA),
#             215-221 chicote colorido, 222-308 plano aberto (eB). Cor 215-235 ajustada à média do original (flash roxo/amarelo).
#   309-428   homem em cima (linhas 0-861) + painel do app embaixo (original, linhas >= 862; 426-428 o painel sobe)
#   429-641   painel do app (x 128-591, y 231-1048, original) sobre o homem desfocado
#   642-827   homem em tela cheia (642-644 transição borrada)
#   828-1186  painéis sobre o homem desfocado
#   1187-1379 homem em tela cheia (1187-1189 borrado); CTA 1296-1379: "CLICK THE BELOW" no topo + 3 setas animadas
# Camadas redesenhadas por cima do vídeo novo: legenda karaokê (glifos do original recoloridos + contorno/sombra sintéticos,
# nada do fundo antigo), título da esquete (máscara estática + brilho escuro sintético), texto do CTA (corpo opaco + glow
# vermelho sintético) e setas (desenhadas do molde de forma, posição/opacidade medidas por frame).
# Enquadramento do homem: por frame, o rosto novo (YuNet) é levado ao centro/altura/inclinação do rosto original suavizados.
# Uso: python3 montar.py pecas/variacao.mp4
import json, subprocess, sys, os, numpy as np, cv2
os.chdir(os.path.dirname(os.path.abspath(__file__)))
OUT=sys.argv[1] if len(sys.argv)>1 else 'pecas/variacao.mp4'
W,H,N,FPS=720,1280,1380,30
REF='REFERENCIA-original.mp4'
PX0,PY0,PX1,PY1=128,231,591,1048          # retângulo dos painéis (inclui a linha escura de 1-2 px da borda)
SPLIT=862                                 # 309-425: painel de baixo começa na linha 862
SPLIT_T={426:856,427:850,428:850}

def ler(c):
    w,h=map(int,subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',c],capture_output=True,text=True).stdout.split(','))
    raw=subprocess.run(['ffmpeg','-v','error','-i',c,'-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,h,w,3)
C={k:ler(f'clipes/{k}.mp4') for k in ['s1','s2','s3','eA','eB']}

def suaviza(arr,k=5):
    a=np.array(arr,float); o=a.copy()
    for i in range(len(a)): o[i]=a[max(0,i-k//2):i+k//2+1].mean(0)
    return o
def trilha_clip(k):
    t=json.load(open(f'molde/rostos-{k}.json')); last=None
    for i,v in enumerate(t):
        if v is None: t[i]=last
        else: last=v
    return suaviza([v[:4] for v in t])
TC={k:trilha_clip(k) for k in ['s1','s2','s3']}
RO=json.load(open('molde/rostos-original.json'))
def trilha_orig(a,b):   # frames a..b do original (só detecções com 1 rosto grande), interpolado e suavizado
    ns=[n for n in range(a,b+1) if str(n) in RO and RO[str(n)][2]>300]
    v=np.array([RO[str(n)][:4] for n in ns]); out=np.array([[np.interp(n,ns,v[:,j]) for j in range(4)] for n in range(a,b+1)])
    return suaviza(out,5)
TO={}
for a,b in [(309,428),(642,827),(1187,1379)]:
    for i,v in enumerate(trilha_orig(a,b)): TO[a+i]=v
for n in (642,643,644):   # transição borrada: o YuNet pega mal, usa o 1º frame nítido
    TO[n]=TO[645]
for n in (1187,1188,1189): TO[n]=TO[1190]

def enquadra(img,src,dst,Hout=H):
    """leva o rosto src=(x,y,h,ang) do clipe a dst=(x,y,h,ang) no quadro W x Hout, sem deixar borda vazia"""
    sh,sw=img.shape[:2]; k=dst[2]/src[2]; d=np.radians(dst[3]-src[3]); sc=np.array(src[:2],float); tc=np.array(dst[:2],float)
    for _ in range(60):
        R=np.array([[np.cos(d),-np.sin(d)],[np.sin(d),np.cos(d)]])
        cs=np.array([[0,0],[W,0],[0,Hout],[W,Hout]],float)
        src_c=(np.linalg.inv(R)@((cs-tc).T)).T/k+sc
        lo=src_c.min(0); hi=src_c.max(0); span=hi-lo
        if span[0]>sw-1 or span[1]>sh-1: k*=1.02; continue
        sh_x=-lo[0] if lo[0]<0 else (sw-1-hi[0] if hi[0]>sw-1 else 0)
        sh_y=-lo[1] if lo[1]<0 else (sh-1-hi[1] if hi[1]>sh-1 else 0)
        if sh_x==0 and sh_y==0: break
        sc=sc+np.array([sh_x,sh_y])
    M=np.zeros((2,3)); M[:,:2]=k*R; M[:,2]=tc-k*R@sc
    return cv2.warpAffine(img,M,(W,Hout),flags=cv2.INTER_LANCZOS4,borderMode=cv2.BORDER_REFLECT)

def quadro_clip(k,t):
    a=C[k]; i=int(np.clip(round(t*24),0,len(a)-1)); return a[i],i
def homem(k,t,dst,Hout=H):
    f,i=quadro_clip(k,t); return enquadra(f,TC[k][i],dst,Hout)
BG_SEQ=[('s2',i) for i in range(len(C['s2']))]+[('s3',i) for i in range(len(C['s3']))]
BG_SEQ=BG_SEQ+BG_SEQ[::-1]
def fundo_borrado(j):   # homem novo bem aproximado e desfocado (como o fundo dos painéis no original: zoom ~1,45, σ≈14, ganho 0,85)
    k,i=BG_SEQ[j%len(BG_SEQ)]; f=enquadra(C[k][i],TC[k][i],(360,560,740*1.45,0))
    return np.clip(cv2.GaussianBlur(f.astype(np.float32),(0,0),14)*0.85,0,255)

# ---------- camadas de texto ----------
EL=lambda r: cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*r+1,2*r+1))
CIANO=None
def legenda(o,reg):
    """legenda karaokê: só os pixels do GLIFO (branco em degradê / ciano) + contorno preto e sombra sintéticos. Devolve (rgb, alpha)."""
    r,g,b=[o[...,i].astype(np.int16) for i in range(3)]; mn=np.minimum(np.minimum(r,g),b); mx=np.maximum(np.maximum(r,g),b)
    wc=(mn>=140)&((mx-mn)<40)&reg
    cc=(b>=150)&(g>=130)&(r<120)&((b-r)>70)&reg
    core=(wc|cc).astype(np.uint8)
    n,l,st,_=cv2.connectedComponentsWithStats(core)
    for i in range(1,n):
        if st[i,4]<14 or st[i,3]>75: core[l==i]=0          # ruído ou traço comprido (não é letra)
    if core.sum()==0: return None
    glifo=cv2.dilate(core,EL(1)).astype(np.float32)
    fill=np.clip(glifo*np.clip(o.max(2).astype(np.float32)/130,0,1),0,1)   # borda AA do glifo contra o traço preto
    traco=cv2.GaussianBlur(cv2.dilate(core,EL(6)).astype(np.float32),(0,0),1.0)
    sombra=np.roll(cv2.GaussianBlur(cv2.dilate(core,EL(7)).astype(np.float32),(0,0),2.2),(5,4),(0,1))*0.8
    a_preto=np.clip(traco+sombra-traco*sombra,0,1)
    alpha=np.clip(fill+a_preto*(1-fill),0,1)
    rgb=o.astype(np.float32)*(fill/np.maximum(alpha,1e-6))[...,None]
    return rgb,alpha

freq=np.load('molde/titulo-freq.npy')
def _titulo():
    core=(freq>=290).astype(np.uint8)
    med=np.load('molde/titulo-mediana.npy').astype(np.float32)
    fill=np.clip((med-120)/(245-120),0,1)*cv2.dilate(core,EL(2)); fill=np.maximum(fill,core)
    brilho=np.clip(cv2.GaussianBlur(cv2.dilate(core,EL(4)).astype(np.float32),(0,0),5)*1.1,0,0.92)
    alpha=np.clip(fill+brilho*(1-fill),0,1); rgb=np.zeros((H,W,3),np.float32); rgb[...]=255*fill[...,None]/np.maximum(alpha,1e-6)[...,None]
    return rgb,alpha
TIT=_titulo()

def cta_texto(o):
    reg=np.zeros((H,W),bool); reg[120:240,30:700]=True
    r,g,b=[o[...,i].astype(np.int16) for i in range(3)]; mn=np.minimum(np.minimum(r,g),b); mx=np.maximum(np.maximum(r,g),b)
    claro=(mn>=175)&(mx-mn<60)&reg
    if claro.sum()<200: return None
    corpo=cv2.morphologyEx(claro.astype(np.uint8),cv2.MORPH_CLOSE,EL(7))
    ff=corpo.copy(); m=np.zeros((H+2,W+2),np.uint8); cv2.floodFill(ff,m,(0,0),1); corpo=(corpo|(ff==0)).astype(np.uint8)
    paleta=((mx-mn<45)&(mn>=85))|claro|(mx<70)|((r>140)&(g<90)&(b<90))    # cromado/branco, traço preto, extrusão vermelha
    corpo=(corpo.astype(bool)&paleta&reg)
    corpo=cv2.morphologyEx(corpo.astype(np.uint8),cv2.MORPH_OPEN,EL(1))
    a_corpo=cv2.GaussianBlur(corpo.astype(np.float32),(0,0),0.7)
    glow=cv2.GaussianBlur(cv2.dilate(corpo,EL(7)).astype(np.float32),(0,0),7)*0.85
    return a_corpo,glow

TPL=np.load('molde/chevron-templates.npy').astype(np.float32)
CHV=json.load(open('molde/chevrons.json'))
def setas(n):
    ns=[m for m in range(max(1296,n-1),min(1379,n+1)+1)]
    out=np.zeros((H,W),np.float32)
    for k in range(3):
        dy=np.mean([CHV[str(m)][k][0] for m in ns]); al=np.mean([CHV[str(m)][k][1] for m in ns])
        M=np.float32([[1,0,0],[0,1,dy]]); t=cv2.warpAffine(cv2.GaussianBlur(TPL[k],(0,0),0.8),M,(W,H))
        out=np.maximum(out,t*al)
    return out

def comp(base,rgb,alpha):
    a=alpha[...,None]; return base*(1-a)+rgb*a

# ---------- loop ----------
orig=subprocess.Popen(['ffmpeg','-v','error','-i',REF,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-hide_banner','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i',REF,
     '-map','0:v','-map','1:a','-c:a','copy','-frames:v',str(N),'-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p',
     '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
meanA=None
for n in range(N):
    o=np.frombuffer(orig.stdout.read(W*H*3),np.uint8).reshape(H,W,3)
    of=o.astype(np.float32)
    if n<=308:                                            # esquete
        fr=np.zeros((H,W,3),np.float32)
        if n<=214: src,_=quadro_clip('eA',0.87+n/FPS)
        else: src,_=quadro_clip('eB',max(0,(n-222))/FPS)
        s=max(W/src.shape[1],1168/src.shape[0]); v=cv2.resize(src,(int(round(src.shape[1]*s)),int(round(src.shape[0]*s))),interpolation=cv2.INTER_LANCZOS4)
        y0=(v.shape[0]-1168)//2; x0=(v.shape[1]-W)//2; v=v[y0:y0+1168,x0:x0+W].astype(np.float32)
        if 215<=n<=221: v=cv2.GaussianBlur(v,(0,0),[30,26,22,18,14,10,7][n-215]); v=cv2.blur(v,(1,61))
        if 215<=n<=235:                                   # flash de cor do chicote: ganho por canal até a média do original
            g=of[112:].reshape(-1,3).mean(0)/np.maximum(v.reshape(-1,3).mean(0),1); w=1.0 if n<=229 else (235-n)/6
            v=np.clip(v*(1+(g-1)*w),0,255)
        fr[112:]=v; fr=comp(fr,*TIT)
    else:
        if 309<=n<=428:
            fr=of.copy(); b=SPLIT_T.get(n,SPLIT)
            fr[:b]=homem('s1',(n-309)/FPS,TO[n],b)[:b]
            reg=np.zeros((H,W),bool); reg[690:b]=True
        elif 429<=n<=641 or 828<=n<=1186:
            fr=fundo_borrado(n-429 if n<=641 else n-828+213)
            fr[PY0:PY1+1,PX0:PX1+1]=of[PY0:PY1+1,PX0:PX1+1]
            reg=np.zeros((H,W),bool); reg[PY1+1:]=True
        else:
            k,t0=('s2',642) if n<=827 else ('s3',1187)
            fr=homem(k,(n-t0)/FPS,TO[n]).astype(np.float32)
            if n in (642,643,644,1187,1188,1189): fr=cv2.GaussianBlur(fr,(0,0),{642:10,643:6,644:3,1187:10,1188:6,1189:3}[n])
            reg=np.zeros((H,W),bool); reg[990:]=True
            if n>=1296:
                a=setas(n); fr=comp(fr,np.full((H,W,3),224,np.float32),a)
                ct=cta_texto(o)
                if ct:
                    a_c,glow=ct; fr=comp(fr,np.array([225,18,18],np.float32)[None,None,:]*np.ones((H,W,1),np.float32),glow)
                    fr=comp(fr,of,a_c)
        L=legenda(o,reg)
        if L: fr=comp(fr,*L)
    enc.stdin.write(np.clip(fr,0,255).astype(np.uint8).tobytes())
    if n%100==0: print('frame',n,flush=True)
enc.stdin.close(); enc.wait(); print('ok ->',OUT)
