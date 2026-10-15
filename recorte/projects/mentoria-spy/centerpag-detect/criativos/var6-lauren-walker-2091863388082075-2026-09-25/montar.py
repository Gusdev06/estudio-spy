#!/usr/bin/env python3
# Lauren Walker 2091863388082075 (Zap, 20,03 s, 601 frames) — var2-6: copiado da var1 (25/09); avatar/cenários em base/elenco.json.
# Molde medido (n = número do frame, 30 fps; rosto YuNet por score em molde/rostos-original.json):
#   A n 0-98    homem em tela cheia (sala borrada) + coração que quica (y 170-450) + caixa "Discover Infidelity IN Minutes." (y 555-725), sem sobrepor o rosto
#   B n 99-447  gravações de celular em tela cheia; o homem é um RECORTE por cima (B1 n 99-343 canto inferior esquerdo, B2 n 344-447 inferior direito).
#               Emojis (berinjela/flor) passam POR TRÁS dele → a camada dele é a de cima; não dá pra recuperar o celular sob ele.
#   C n 448-524 close no carro + seta vermelha (contorno branco) quicando no peito
#   D n 525-600 CTA "ACCESS NOW" sobre celular borrado — sem o homem → original intocado
# Peça: A = clipe c1 em tela cheia + coração/caixa do original por máscara de cor · B = recorte da avatar nova (segmentação) por cima; onde o homem
# antigo (máscara dilatada 12 px) passa do contorno do novo, entra o próprio clipe novo DESFOCADO (halo), nunca pixel do original · C = clipe c2 em
# tela cheia + seta REDESENHADA (sprite sintético vermelho/branco posicionado pela seta do original) · D = original. Áudio copiado.
# Uso (desta pasta, com o venv do mediapipe): <segenv>/bin/python montar.py pecas/variacao.mp4
import subprocess, sys, json, numpy as np, cv2
sys.path.insert(0,'.'); from seg import seg
OUT=sys.argv[1]; W,H=720,1280; M='../../../gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
A0,A1,B0,B1a,B2,B1,C0,C1=0,98,99,343,344,447,448,524
orig=lambda n: cv2.imread(f'frames/full/{n:03d}.png')
# limpeza.json (opcional, var2+): letreiro alucinado pelo Pruna no FUNDO do clipe → a caixa é trocada pela placa limpa (mediana dos 12 primeiros
# frames do MESMO clipe; câmera parada), com borda suave. Só fundo: a caixa fica longe da cabeça. [{"clip":"c1","k0":72,"k1":136,"box":[x0,y0,x1,y1]}]
import os
LIMPA=json.load(open('limpeza.json')) if os.path.exists('limpeza.json') else []
class Clip:
    def __init__(s,p,n0):
        s.p=subprocess.Popen(['ffmpeg','-v','error','-i',p,'-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE); s.i=-1; s.f=None; s.n0=n0
        s.lim=[L for L in LIMPA if f"clipes/{L['clip']}.mp4"==p]
        if s.lim:
            raw=subprocess.run(['ffmpeg','-v','error','-i',p,'-frames:v','12','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
            s.placa=np.median(np.frombuffer(raw,np.uint8).reshape(-1,1280,704,3),axis=0).astype(np.float32)
            for L in s.lim:
                x0,y0,x1,y1=L['box']; a=np.zeros((1280,704),np.float32); a[y0:y1,x0:x1]=1; L['a']=cv2.GaussianBlur(a,(0,0),6)[...,None]
    def at(s,n):
        want=int(round((n-s.n0)/30*24+1))
        while s.i<want:
            b=s.p.stdout.read(704*1280*3)
            if len(b)<704*1280*3: break
            s.f=np.frombuffer(b,np.uint8).reshape(1280,704,3); s.i+=1
            for L in s.lim:
                if L['k0']<=s.i<=L['k1']: s.f=(s.f*(1-L['a'])+s.placa*L['a']).astype(np.uint8)
        return s.f
det=cv2.FaceDetectorYN_create(M,'',(704,1280),0.86,0.3,5000)
def face(img):
    d=det.detect(np.ascontiguousarray(img))[1]
    if d is None or not len(d): return None
    a=max(d,key=lambda r:r[-1]); return (a[0]+a[2]/2,a[1]+a[3]/2,a[3])
def med_clip(path,n0,na,nb):
    c=Clip(path,n0); r=[face(c.at(n)) for n in range(na,nb+1,3)]; return np.median(np.array([x for x in r if x]),axis=0)
R=json.load(open('molde/rostos-original.json')); med_orig=lambda a,b: np.median(np.array([R[str(n)][:3] for n in range(a,b+1) if R[str(n)]]),axis=0)
def affine(src,dst,cover):
    cx,cy,h=src; tx,ty,th=dst; s=th/h
    if cover: s=max(s,W/704,H/1280)
    ox,oy=tx-s*cx,ty-s*cy
    if cover: ox=min(max(ox,W-704*s),0); oy=min(max(oy,H-1280*s),0)
    return np.float32([[s,0,ox],[0,s,oy]]),s
T={}
T['A']=affine(med_clip('clipes/c1.mp4',0,A0,A1),med_orig(A0,A1),True)
T['B1']=affine(med_clip('clipes/c1.mp4',0,B0,B1a),med_orig(B0,B1a),False)
T['B2']=affine(med_clip('clipes/c1.mp4',0,B2,B1),med_orig(B2,B1),False)
T['C']=affine(med_clip('clipes/c2.mp4',C0,C0,C1),med_orig(C0,C1),True)
print({k:(round(v[1],3),v[0][:,2].round(1).tolist()) for k,v in T.items()})
warp=lambda img,m,interp=cv2.INTER_LANCZOS4: cv2.warpAffine(img,m,(W,H),flags=interp,borderMode=cv2.BORDER_CONSTANT,borderValue=0)
def fill(m):
    m=m.astype(np.uint8); ff=m.copy(); h,w=m.shape; mk=np.zeros((h+2,w+2),np.uint8); cv2.floodFill(ff,mk,(0,0),1)
    return m|(1-ff)
# caixa de texto (estática): vermelho da caixa + texto dentro, em y 540-740
f0=orig(0); r,g,b=[f0[...,i].astype(int) for i in (2,1,0)]
red=((r>150)&(g<90)&(b<90)).astype(np.uint8); red[:540]=0; red[740:]=0
red=cv2.morphologyEx(red,cv2.MORPH_CLOSE,np.ones((15,15),np.uint8)); caixa=fill(red).astype(np.float32)
caixa=cv2.GaussianBlur(caixa,(3,3),0.8)
def coracao(f):
    r,g,b=[f[...,i].astype(int) for i in (2,1,0)]
    m=((r>110)&(r>g+60)&(r>b+60)).astype(np.uint8); m[553:]=0   # a caixa começa em y 555; a ponta do coração desce até ~550
    n,l,st,_=cv2.connectedComponentsWithStats(m)
    if n<2: return np.zeros(m.shape,np.float32)
    k=1+np.argmax(st[1:,4]); m=(l==k).astype(np.uint8); m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8)); m=fill(m)
    return cv2.GaussianBlur(m.astype(np.float32),(3,3),0.8)
# seta sintética: forma medida no n 490 (vermelho sólido) + contorno branco 3 px
f=orig(490); r,g,b=[f[...,i].astype(int) for i in (2,1,0)]; sm=((r>150)&(g<90)&(b<90)).astype(np.uint8)
ys,xs=np.where(sm); SX0,SY0=xs.min(),ys.min(); sm=sm[SY0-6:ys.max()+7,SX0-6:xs.max()+7]; sm=fill(cv2.morphologyEx(sm,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8)))
SUP=4; big=cv2.resize(sm*255,None,fx=SUP,fy=SUP,interpolation=cv2.INTER_CUBIC); big=(cv2.GaussianBlur(big,(0,0),SUP*2.0)>127).astype(np.uint8)
out_=cv2.dilate(big,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6*SUP+1,6*SUP+1)))
sh,sw=sm.shape; a_red=cv2.resize(big.astype(np.float32),(sw,sh),interpolation=cv2.INTER_AREA); a_all=cv2.resize(out_.astype(np.float32),(sw,sh),interpolation=cv2.INTER_AREA)
RED=np.array([35,22,235],np.float32)   # BGR medido no miolo da seta
ARGB=np.median(f[ys,xs],axis=0).astype(np.float32); print('vermelho da seta (BGR)',ARGB); RED=ARGB
def seta(dst,f):
    r,g,b=[f[...,i].astype(int) for i in (2,1,0)]; m=(r>150)&(g<90)&(b<90); m[:600]=False
    ys,xs=np.where(m)
    if len(xs)<200: return dst
    x0,y0=xs.min()-6,ys.min()-6; reg=dst[y0:y0+sh,x0:x0+sw].astype(np.float32)
    reg=reg*(1-a_all[...,None])+255*a_all[...,None]; reg=reg*(1-a_red[...,None])+RED*a_red[...,None]
    dst[y0:y0+sh,x0:x0+sw]=np.clip(reg,0,255).astype(np.uint8); return dst
def pessoa_nova(clipf,m):
    p,_=seg(clipf); mm=(p>0.5).astype(np.uint8); n,l,st,_=cv2.connectedComponentsWithStats(mm)
    if n>1: k=1+np.argmax(st[1:,4]); p=p*(l==k)
    return warp(np.clip((p-0.3)/0.4,0,1).astype(np.float32),m,cv2.INTER_LINEAR)
def homem_antigo(f,n):
    _,P=seg(f); cx,cy,h=R[str(n)][:3]
    corpo=P['body'].copy(); zona=np.zeros(corpo.shape,np.float32); cv2.rectangle(zona,(int(cx-0.5*h),int(cy+0.2*h)),(int(cx+0.5*h),H),1,-1)   # pele do corpo só no pescoço/colo (mãos do celular ficam fora)
    p=np.maximum.reduce([P['hair'],P['face'],P['clothes'],corpo*zona])
    # envelope: acima da linha do ombro só vale a coluna da cabeça (tira a mão que segura o celular, que a segmentação junta ao homem)
    env=np.zeros(p.shape,np.float32); env[int(cy+0.45*h):]=1; cv2.ellipse(env,(int(cx),int(cy-0.15*h)),(int(0.95*h),int(1.1*h)),0,0,360,1,-1)   # var2-6: elipse maior — a de 0,85×0,95 cortava os cantos do cabelo antigo (fio escuro na careca da var4)
    env[int(cy):]=np.maximum(env[int(cy):],0); p=p*env
    # var2-6: o MediaPipe deixa buracos no cabelo escuro do homem antigo (topo esquerdo) → "boné": elipse sobre o crânio ∩ pixels escuros
    # (o polegar claro que segura o celular fica de fora). Sem isso, um fio do cabelo antigo aparecia na careca da var4.
    cap=np.zeros(p.shape,np.uint8); cv2.ellipse(cap,(int(cx),int(cy-0.2*h)),(int(0.5*h),int(0.55*h)),0,0,360,1,-1)
    p=np.maximum(p,(cap*(f.max(2)<100)).astype(np.float32)); mm=(p>0.35).astype(np.uint8)
    n_,l,st,_=cv2.connectedComponentsWithStats(mm); k=l[int(cy),int(cx)]
    if k==0: k=1+np.argmax(st[1:,4])
    mm=fill((l==k).astype(np.uint8)); return mm
enc=subprocess.Popen(['ffmpeg','-hide_banner','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30','-i','-','-i','REFERENCIA-original.mp4',
    '-map','0:v','-map','1:a','-c:a','copy','-frames:v','601','-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
c1=Clip('clipes/c1.mp4',0); c2=Clip('clipes/c2.mp4',C0); stats=[]; K12=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(25,25))
for n in range(601):
    f=orig(n)
    if n<=A1:
        o=warp(c1.at(n),T['A'][0]).astype(np.float32)
        for a in (caixa,coracao(f)): o=o*(1-a[...,None])+f*a[...,None]
        o=o.astype(np.uint8)
    elif n<=B1:
        m=T['B1' if n<=B1a else 'B2'][0]; cf=c1.at(n); wc=warp(cf,m); val=warp(np.ones((1280,704),np.float32),m,cv2.INTER_NEAREST)
        a_new=pessoa_nova(cf,m)*val; old=homem_antigo(f,n)
        oldd=cv2.dilate(old,K12).astype(np.float32); a_old=np.maximum(cv2.GaussianBlur(oldd,(0,0),3),oldd*0)*1.0
        a_old=np.maximum(a_old,cv2.dilate(old,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(13,13))).astype(np.float32))
        fora=((old>0)&(val<1)).sum()                       # homem antigo fora da área coberta pelo clipe (deveria ser 0)
        halo=((old>0)&(a_new<0.5)).sum()
        stats.append((n,int(old.sum()),int(halo),int(fora)))
        # halo (onde o homem antigo passava do contorno do novo): reconstruído por inpainting SÓ com o entorno (fora da máscara dilatada),
        # em meia resolução — nenhum pixel do homem antigo entra. (1ª versão usava o clipe novo desfocado: virava um brilho marrom.)
        mk=cv2.resize((a_old>0.01).astype(np.uint8),(W//2,H//2),interpolation=cv2.INTER_NEAREST); mk=cv2.dilate(mk,np.ones((3,3),np.uint8))
        fs=cv2.resize(f,(W//2,H//2),interpolation=cv2.INTER_AREA); fs[mk>0]=0
        blur=cv2.resize(cv2.inpaint(fs,mk,6,cv2.INPAINT_TELEA),(W,H),interpolation=cv2.INTER_CUBIC)
        blur=cv2.GaussianBlur(blur,(0,0),3).astype(np.float32)
        o=f.astype(np.float32)*(1-a_old[...,None])+blur*a_old[...,None]
        o=o*(1-a_new[...,None])+wc.astype(np.float32)*a_new[...,None]; o=o.astype(np.uint8)
    elif n<=C1:
        o=seta(warp(c2.at(n),T['C'][0]),f)
    else: o=f
    enc.stdin.write(np.ascontiguousarray(o).tobytes())
enc.stdin.close(); enc.wait()
json.dump(stats,open('conferencia/cobertura-B.json','w'))
s=np.array(stats); print('B: homem antigo px médio',s[:,1].mean().round(),'| halo (antigo fora do contorno novo) médio',s[:,2].mean().round(),'máx',s[:,2].max(),'| fora do clipe máx',s[:,3].max())
print('ok ->',OUT)
