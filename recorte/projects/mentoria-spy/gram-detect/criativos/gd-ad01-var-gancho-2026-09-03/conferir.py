# Conferência da variação B contra o original. Roda a partir de projects/mentoria-spy/.
import subprocess, os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
ORIG='criativos-crus/spy-gram/ads-en/GD-AD01.mp4'
NEW='gram-detect/criativos/gd-ad01-var-gancho-2026-09-03/GD-AD01-B-caixa-supposed.mp4'
C='gram-detect/criativos/gd-ad01-var-gancho-2026-09-03/conferencia'
FONT='gram-detect/scripts/fonts/Poppins-Bold.ttf'
os.makedirs(C,exist_ok=True)
FRAMES=[0,30,90,233,234,500,977]
def grab(src,n,out):
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vf',f"select='eq(n,{n})'",'-vsync','0','-frames:v','1',out],check=True)
def load(p): return np.array(Image.open(p).convert('RGB')).astype(int)
def hexs(m): return '#%02X%02X%02X'%tuple(int(v) for v in m)
BX0,BX1,BY0,BY1=106,973,862,1058
res={}
for n in FRAMES:
    o=f'{C}/f{n:03d}-orig.png'; v=f'{C}/f{n:03d}-var.png'
    grab(ORIG,n,o); grab(NEW,n,v)
    O=load(o); V=load(v)
    r,g,b=V[...,0],V[...,1],V[...,2]
    pink=(r>200)&(g<60)&(b>50)&(b<130)
    band=pink[840:1080,:].copy(); band[BY0-840:BY1-840+1,BX0:BX1+1]=False
    inside=pink[BY0:BY1+1,BX0:BX1+1].sum()
    mask=np.ones(O.shape[:2],bool)
    if n<234: mask[BY0-2:BY1+3,BX0-2:BX1+3]=False
    d=np.abs(O-V).max(2)[mask]
    print(f'frame {n:3d} t={n/30:6.3f}s | rosa dentro da caixa {inside:6d} | rosa vazando na faixa y840-1080 fora do retângulo {int(band.sum()):3d} | diff fora da caixa: media {d.mean():.2f} p99.9 {np.percentile(d,99.9):.0f} max {d.max()}')
    if n in (30,90):
        for (a,bb,name) in [(884,966,'linha1'),(964,1050,'linha2')]:
            reg=V[a:bb,112:968]; rr,gg,bb2=reg[...,0],reg[...,1],reg[...,2]
            yel=(rr>200)&(gg>200)&(bb2<90); dark=(rr<150)&(gg<70)&(bb2<110)
            ys,xs=np.where(yel); dy,dx=np.where(dark)
            px=reg[dark]; lum=px.sum(1); core=px[lum<=np.percentile(lum,15)]
            print(f'   {name}: amarelo x {xs.min()+112}-{xs.max()+112} cx {(xs.min()+xs.max())/2+112} y {ys.min()+a}-{ys.max()+a} | mediana {hexs(np.median(reg[yel],0))} | escuro ext L{xs.min()-dx.min()} R{dx.max()-xs.max()} U{ys.min()-dy.min()} D{dy.max()-ys.max()} nucleo {hexs(np.median(core,0))}')
        print(f'   caixa: mediana {hexs(np.median(V[870:895,150:930].reshape(-1,3),0))} (original {hexs(np.median(O[870:895,150:930].reshape(-1,3),0))}) | bbox rosa', end=' ')
        ys,xs=np.where(pink[800:1100]); print(f'x {xs.min()}-{xs.max()} y {ys.min()+800}-{ys.max()+800}')
# lado a lado t=1 s (frame 30) com rótulo
def label(im,txt):
    d=ImageDraw.Draw(im); f=ImageFont.truetype(FONT,44)
    d.rectangle([0,0,im.width,70],fill=(0,0,0)); d.text((20,10),txt,font=f,fill=(255,255,255)); return im
a=label(Image.open(f'{C}/f030-orig.png').convert('RGB'),'A · ORIGINAL  t=1,000 s (frame 30)')
b=label(Image.open(f'{C}/f030-var.png').convert('RGB'),'B · VARIACAO   t=1,000 s (frame 30)')
side=Image.new('RGB',(a.width*2+20,a.height),(20,20,20)); side.paste(a,(0,0)); side.paste(b,(a.width+20,0)); side.save(f'{C}/lado-a-lado-t1s.png')
# recorte 2x da caixa lado a lado
ca=Image.open(f'{C}/f030-orig.png').crop((90,840,990,1080)).resize((1800,480),Image.LANCZOS)
cb=Image.open(f'{C}/f030-var.png').crop((90,840,990,1080)).resize((1800,480),Image.LANCZOS)
z=Image.new('RGB',(1800,480*2+80),(20,20,20)); z.paste(ca,(0,0)); z.paste(cb,(0,480+80))
d=ImageDraw.Draw(z); f=ImageFont.truetype(FONT,36); d.text((20,480+20),'em cima: A original · embaixo: B variacao — recorte x90-990 y840-1080, 2x',font=f,fill=(255,255,255)); z.save(f'{C}/recorte-caixa-2x.png')
# saída da caixa: frame 233 vs 234 na variação
a=label(Image.open(f'{C}/f233-var.png').convert('RGB'),'B · frame 233 (7,767 s) ultimo com caixa')
b=label(Image.open(f'{C}/f234-var.png').convert('RGB'),'B · frame 234 (7,800 s) caixa some')
side=Image.new('RGB',(a.width*2+20,a.height),(20,20,20)); side.paste(a,(0,0)); side.paste(b,(a.width+20,0)); side.save(f'{C}/saida-caixa-f233-f234.png')
# mapa de diferença frame 30 (onde o vídeo mudou)
O=load(f'{C}/f030-orig.png'); V=load(f'{C}/f030-var.png'); d=np.abs(O-V).max(2)
Image.fromarray(np.clip(d*4,0,255).astype(np.uint8)).save(f'{C}/mapa-diferenca-t1s.png')
print('imagens em',C)
