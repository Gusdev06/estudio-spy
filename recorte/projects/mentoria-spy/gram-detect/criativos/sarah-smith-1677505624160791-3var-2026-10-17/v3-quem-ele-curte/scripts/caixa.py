# Gera a camada da legenda nova do gancho dentro da MESMA silhueta da caixa original.
import numpy as np, cv2
from PIL import Image, ImageFont, ImageDraw
HERE='/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/gram-detect/criativos/sarah-smith-1677505624160791-3var-2026-10-17/v3-quem-ele-curte'
FONT=HERE+'/fontes/OpenSans.ttf'; SIZE=40; WGHT=750; PITCH=56; Y0=958; CX=360
LINES=["“Girl, who’s the girl","he keeps liking pics of?","\U0001F440”"]
def font():
    f=ImageFont.truetype(FONT,SIZE); f.set_variation_by_axes([WGHT,100]); return f
def emoji(ch,h):
    ef=ImageFont.truetype('/System/Library/Fonts/Apple Color Emoji.ttc',160)
    im=Image.new('RGBA',(200,200),(0,0,0,0)); ImageDraw.Draw(im).text((0,0),ch,font=ef,embedded_color=True)
    im=im.crop(im.getbbox()); return im.resize((round(im.width*h/im.height),h),Image.LANCZOS)
def layer(scale=2):
    """RGBA 720x1280: texto branco + emoji, sem a caixa."""
    S=scale; f=ImageFont.truetype(FONT,SIZE*S); f.set_variation_by_axes([WGHT,100])
    big=Image.new('RGBA',(720*S,1280*S),(0,0,0,0)); d=ImageDraw.Draw(big)
    for j,t in enumerate(LINES):
        y=(Y0+j*PITCH)*S
        if '\U0001F440' in t:
            rest=t.replace('\U0001F440','')
            eh=int(SIZE*1.0*S); em=emoji('\U0001F440',eh); gap=int(4*S)
            wr=d.textlength(rest,font=f); W=em.width+gap+wr; x=CX*S-W/2
            # alinhar emoji pela altura de caixa-alta: topo do 'G' ~ y+ascender-cap
            capb=f.getbbox('H'); ytop=y+capb[1]+(capb[3]-capb[1])/2-eh/2
            big.alpha_composite(em,(int(x),int(ytop)))
            d.text((x+em.width+gap,y),rest,font=f,fill=(255,255,255,255))
        else:
            w=d.textlength(t,font=f); d.text((CX*S-w/2,y),t,font=f,fill=(255,255,255,255))
    return big.resize((720,1280),Image.LANCZOS)
if __name__=='__main__':
    sil=np.load(HERE+'/scripts/sil_f0.npy')
    L=np.asarray(layer()).astype(np.float32)/255
    a=L[...,3:]
    # checar se o texto novo cabe no interior (folga >= 10px da borda)
    inner=cv2.erode(sil,np.ones((21,21),np.uint8))
    out=(a[...,0]>0.05)&(inner==0)
    print('pixels de texto fora do interior com folga 10px:',int(out.sum()))
    np.save(HERE+'/scripts/texto_novo.npy',(L*255).astype(np.uint8))
