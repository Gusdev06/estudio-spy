# Troca "his" -> "her" na 1a legenda da demo: apaga a linha 1 inteira (inpaint) e redesenha "Copy her @ and use" centrada.
import numpy as np, cv2
from PIL import Image, ImageFont, ImageDraw
HERE='/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/gram-detect/criativos/sarah-smith-1677505624160791-3var-2026-10-17/v3-quem-ele-curte'
REF=HERE+'/tmp/f0200.png'
S=4; SIZE=36.5; WGHT=800; STROKE=3
import json, os
P=json.load(open(HERE+'/scripts/demo_params.json')) if os.path.exists(HERE+'/scripts/demo_params.json') else {'track':-1.0,'dy':0.0,'dx':0.0,'size':SIZE}
LX0,LX1,LY0,LY1=175,535,893,934   # linha 1 (tinta branca) no f200
ref=cv2.imread(REF).astype(np.int16)
white=(ref.min(2)>230); white[:LY0]=0; white[LY1+1:]=0; white[:,:LX0]=0; white[:,LX1+1:]=0
# a linha 2 começa em ~940; o descendente do 'p'/'y' chega a ~934
M_OLD=cv2.dilate(white.astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)))
w2=(ref.min(2)>230); w2[:937]=0; w2[975:]=0; w2[:,:150]=0; w2[:,570:]=0   # linha 2 (fica intacta)
M_L2=cv2.dilate(w2.astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)))
L2_CORE=cv2.dilate(w2.astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7)))  # tinta + contorno de 3px da linha 2
ys,xs=np.where(white); CX=(xs.min()+xs.max())/2; TOP=ys.min()
def render(text, size=None, track=None):
    size=size or P['size']; track=P['track'] if track is None else track
    f=ImageFont.truetype(HERE+'/fontes/Montserrat.ttf',size*S); f.set_variation_by_axes([WGHT])
    def draw(d,x,y,**kw):
        for ch in text: d.text((x,y),ch,font=f,**kw); x+=f.getlength(ch)+track*S
    tmp=Image.new('L',(720*S,200*S),0); draw(ImageDraw.Draw(tmp),40*S,40*S,fill=255)
    a=np.asarray(tmp)>128; xs=np.where(a.any(0))[0]; ys=np.where(a.any(1))[0]
    ox=(CX+P['dx'])*S-(xs.min()+xs.max())/2; oy=(TOP+P['dy'])*S-ys.min()
    im=Image.new('RGBA',(720*S,1280*S),(0,0,0,0))
    draw(ImageDraw.Draw(im),40*S+ox,40*S+oy,fill=(255,255,255,255),stroke_width=STROKE*S,stroke_fill=(0,0,0,255))
    return np.asarray(im.resize((720,1280),Image.LANCZOS)).astype(np.float32)/255
NEW=render("Copy her @ and use")
def sh(a,dx):
    M=np.float32([[1,0,dx],[0,1,0]]); return cv2.warpAffine(a,M,(720,1280),flags=cv2.INTER_NEAREST,borderValue=0)
def patch(frame,dx=0,new=None):
    new=NEW if new is None else new
    m=sh(M_OLD,dx) if dx else M_OLD
    if not m.any(): return frame
    m2=sh(M_L2,dx) if dx else M_L2
    # inpaint com a linha 2 também mascarada (pra não puxar o contorno preto dela), mas só aplica na área da linha 1
    inp=cv2.inpaint(frame,(m|m2).astype(np.uint8),6,cv2.INPAINT_TELEA)
    core=sh(L2_CORE,dx) if dx else L2_CORE
    out=frame.copy(); mb=m.astype(bool)&~(core.astype(bool)); out[mb]=inp[mb]
    n=sh(new,dx) if dx else new
    a=n[...,3:]; rgb=n[...,2::-1]*255
    o=out.astype(np.float32)*(1-a)+rgb*a
    return np.clip(o+0.5,0,255).astype(np.uint8)
