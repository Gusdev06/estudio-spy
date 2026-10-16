# Redesenha as legendas do original (branco, Helvetica Neue Medium, sombra leve) nas posições medidas.
# Cada bloco: linhas, topo da tinta de cada linha (px no quadro 1080x1920) e a largura-alvo da 1ª linha (ajusta o tamanho).
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
H='/System/Library/Fonts/HelveticaNeue.ttc'
idx=next(i for i in range(14) if ImageFont.truetype(H,60,index=i).getname()[1]=='Medium')
EMO=ImageFont.truetype('/System/Library/Fonts/Apple Color Emoji.ttc',160)
BLOCOS={
 'titulo':(["How to view your man’s","recent following on IG"],[1236,1311],687,True),
 'ab-frase1':(["If you want to check your","man’s recent following but","you don’t know how to do it,"],[1422,1471,1527],511,False),
 'ab-frase2':(["let me show you exactly how","to do this."],[1451,1506],None,False),
 'fe-frase':(["Try it for yourself and let me","know what you find."],[1443,1506],565,False),
}
def fonte(txt,larg):
    lo,hi=20,120
    while hi-lo>1:
        m=(lo+hi)//2; b=ImageFont.truetype(H,m,index=idx).getbbox(txt)
        (lo,hi)=(m,hi) if b[2]-b[0]<=larg else (lo,m)
    return lo
tam_sub=fonte(BLOCOS['ab-frase1'][0][0],511)
os.makedirs('legendas',exist_ok=True)
for nome,(linhas,topos,larg,emoji) in BLOCOS.items():
    sz=fonte(linhas[0],larg) if larg else tam_sub
    f=ImageFont.truetype(H,sz,index=idx)
    txt=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(txt)
    for i,(l,top) in enumerate(zip(linhas,topos)):
        b=f.getbbox(l); w=b[2]-b[0]
        em=None
        if emoji and i==len(linhas)-1:
            e=Image.new('RGBA',(400,200),(0,0,0,0)); ImageDraw.Draw(e).text((0,0),'👀',font=EMO,embedded_color=True)
            e=e.crop(e.getbbox()); k=(sz*0.78)/e.height; em=e.resize((int(e.width*k),int(e.height*k)),Image.LANCZOS)
        tot=w+(int(sz*0.25)+em.width if em else 0)
        x=(1080-tot)//2-b[0]; y=top-b[1]
        d.text((x,y),l,font=f,fill=(255,255,255,255))
        if em: txt.alpha_composite(em,(x+b[2]+int(sz*0.25), y+f.getbbox('I')[1]+ (f.getbbox('I')[3]-f.getbbox('I')[1]-em.height)//2))
    sh=Image.new('RGBA',txt.size,(0,0,0,0)); sh.putalpha(txt.getchannel('A').point(lambda a:int(a*0.55)))
    sh=sh.filter(ImageFilter.GaussianBlur(3))
    out=Image.new('RGBA',txt.size,(0,0,0,0)); out.alpha_composite(sh,(2,3)); out.alpha_composite(txt)
    out.save(f'legendas/{nome}.png'); print(nome,sz)
