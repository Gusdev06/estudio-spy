# Conferência da variação C (P3 corrigido) contra o campeão GD-AD01 e contra o P3 cru. Roda de projects/mentoria-spy/.
import subprocess
from PIL import Image, ImageDraw, ImageFont
import numpy as np
CH='criativos-crus/spy-gram/ads-en/GD-AD01.mp4'; P3='criativos-personagens/AD01 - PERSONAGEM 3.mp4'
C='gram-detect/criativos/gd-ad01-var-rosto-2026-09-03/GD-AD01-C-rosto-p3.mp4'
D='gram-detect/criativos/gd-ad01-var-rosto-2026-09-03/conferencia'; FONT='gram-detect/scripts/fonts/Poppins-Bold.ttf'
def grab(src,t,out): subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',src,'-frames:v','1',out],check=True)
def grabn(src,n,out): subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vf',f"select='eq(n,{n})'",'-vsync','0','-frames:v','1',out],check=True)
def load(p): return np.array(Image.open(p).convert('RGB')).astype(int)
def hexs(m): return '#%02X%02X%02X'%tuple(int(v) for v in m)
def label(im,txt):
    d=ImageDraw.Draw(im); f=ImageFont.truetype(FONT,44); d.rectangle([0,0,im.width,70],fill=(0,0,0)); d.text((20,10),txt,font=f,fill=(255,255,255)); return im
def side(paths,labels,out):
    ims=[label(Image.open(p).convert('RGB'),l) for p,l in zip(paths,labels)]
    W=sum(i.width for i in ims)+20*(len(ims)-1); s=Image.new('RGB',(W,ims[0].height),(20,20,20)); x=0
    for i in ims: s.paste(i,(x,0)); x+=i.width+20
    s.save(out)
for t in [1,2.2,3,3.5]:
    grab(CH,t,f'{D}/t{t}-campeao.png'); grab(P3,t,f'{D}/t{t}-p3-cru.png'); grab(C,t,f'{D}/t{t}-varC.png')
    side([f'{D}/t{t}-campeao.png',f'{D}/t{t}-p3-cru.png',f'{D}/t{t}-varC.png'],[f'A · CAMPEAO t={t},0 s',f'P3 CRU t={t},0 s',f'C · P3 CORRIGIDO t={t},0 s'],f'{D}/lado-a-lado-t{t}s.png')
    V=load(f'{D}/t{t}-varC.png'); r,g,b=V[...,0],V[...,1],V[...,2]
    pink=(r>200)&(g<60)&(b>50)&(b<130); rows=np.where(pink[800:1400].sum(1)>500)[0]+800; cols=np.where(pink[862:1327].sum(0)>300)[0]
    print(f't={t}s C: caixa rosa (linhas >500px / colunas >300px) x {cols.min()}-{cols.max()} y {rows.min()}-{rows.max()} mediana {hexs(np.median(V[870:895,150:930].reshape(-1,3),0))}')
    for (a,bb,name) in [(1010,1094,'linha1'),(1094,1180,'linha2')]:
        reg=V[a:bb,112:968]; rr,gg,bb2=reg[...,0],reg[...,1],reg[...,2]; yel=(rr>200)&(gg>200)&(bb2<90); ys,xs=np.where(yel)
        print(f'   {name}: amarelo x {xs.min()+112}-{xs.max()+112} cx {(xs.min()+xs.max())/2+112} y {ys.min()+a}-{ys.max()+a} mediana {hexs(np.median(reg[yel],0))}')
    white=(r>235)&(g>235)&(b>235); wb=white[1327:1400,40:1040]; rows=np.where(wb.sum(1)>6)[0]+1327
    logo=(r>150)&(b>120)&(g<120); lo=int(logo[862:1327,:40].sum())+int(logo[862:1327,1040:].sum())
    print(f'   branco visível abaixo da caixa (y 1327-1400, x40-1039): {len(rows)} rows {rows.min() if len(rows) else "-"}..{rows.max() if len(rows) else "-"} | logo fora da caixa (x<40 ou x>1039, y862-1326): {lo} px')
# saída da caixa: frames 398 (6,633) e 399 (6,650) da C
grabn(C,398,f'{D}/f398-varC.png'); grabn(C,399,f'{D}/f399-varC.png')
for n in (398,399):
    V=load(f'{D}/f{n:03d}-varC.png'); r,g,b=V[...,0],V[...,1],V[...,2]; pink=(r>200)&(g<60)&(b>50)&(b<130)
    print(f'frame {n} t={n/60:.3f}s: rosa na região da caixa {int(pink[862:1327,40:1040].sum())}')
side([f'{D}/f398-varC.png',f'{D}/f399-varC.png'],['C · frame 398 (6,633 s) ultimo com caixa','C · frame 399 (6,650 s) caixa some'],f'{D}/saida-caixa-f398-f399.png')
# fim: último frame da C vs frame 1752 (29,200) e 1772 do P3 cru
grabn(C,1751,f'{D}/ultimo-varC-f1751.png'); grabn(P3,1751,f'{D}/p3-f1751.png'); grabn(P3,1752,f'{D}/p3-f1752-fade.png'); grabn(P3,1772,f'{D}/p3-f1772-fim.png')
for p in ['ultimo-varC-f1751','p3-f1751','p3-f1752-fade','p3-f1772-fim']: print(p,'luma',round(load(f'{D}/{p}.png').mean(),1))
side([f'{D}/ultimo-varC-f1751.png',f'{D}/p3-f1752-fade.png',f'{D}/p3-f1772-fim.png'],['C · ultimo frame 1751 (29,183 s)','P3 cru · frame 1752 (29,200) fade comeca','P3 cru · frame 1772 (29,533) fim'],f'{D}/fim-corte-seco.png')
# frame 0
grabn(C,0,f'{D}/f000-varC.png')
# recorte 2x da caixa: campeão x C
ca=Image.open(f'{D}/t1-campeao.png').crop((0,840,1080,1360)).resize((1800,867),Image.LANCZOS); cb=Image.open(f'{D}/t1-varC.png').crop((0,840,1080,1360)).resize((1800,867),Image.LANCZOS)
z=Image.new('RGB',(1800,867*2+80),(20,20,20)); z.paste(ca,(0,0)); z.paste(cb,(0,947)); d=ImageDraw.Draw(z); d.text((20,887),'em cima: A campeao · embaixo: C (P3 + caixa 1000x465, y 862-1326) — recorte largura cheia y840-1360',font=ImageFont.truetype(FONT,34),fill=(255,255,255)); z.save(f'{D}/recorte-caixa-2x.png')
print('ok')
