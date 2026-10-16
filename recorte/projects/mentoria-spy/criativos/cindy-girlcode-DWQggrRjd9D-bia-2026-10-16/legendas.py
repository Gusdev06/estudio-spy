# Redesenha o texto fixo do original (amarelo-claro medido RGB 253,244,168; Helvetica Neue Medium, sombra leve) na posição medida.
# Medição (1080x1920, mediana temporal de 33 frames, pixels estáveis e amarelados): topo da tinta de cada linha e largura da linha 2.
# Cada linha é posicionada pelo topo da tinta medido; tamanho ajustado pela largura da linha mais larga (781 px).
from PIL import Image, ImageDraw, ImageFont, ImageFilter
H='/System/Library/Fonts/HelveticaNeue.ttc'
idx=next(i for i in range(14) if ImageFont.truetype(H,60,index=i).getname()[1]=='Medium')
def fonte(txt,larg):
    lo,hi=20,140
    while hi-lo>1:
        m=(lo+hi)//2; b=ImageFont.truetype(H,m,index=idx).getbbox(txt)
        (lo,hi)=(m,hi) if b[2]-b[0]<=larg else (lo,m)
    return ImageFont.truetype(H,lo,index=idx)
COR=(253,244,168,255)
LINHAS=[("Resentment is weird",755),("because yes I want to forgive",826),("you whole heartedly but",899),
        ("my mind is struggling to",973),("comprehend why did you",1044),("do that to me",1118)]
# Desenha em 4x e reduz: o PIL só aceita tamanho inteiro e a largura medida cai entre 58 e 59 px.
# 233/4 = 58,25 px: larguras (alfa>200) 540/783/675/356 px x medido no original 540/781/677/353.
K=4; f=ImageFont.truetype(H,233,index=idx)
big=Image.new('RGBA',(1080*K,1920*K),(0,0,0,0)); d=ImageDraw.Draw(big)
for t,topo in LINHAS:
    b=f.getbbox(t); d.text(((1080*K-(b[2]-b[0]))//2-b[0], topo*K-b[1]), t, font=f, fill=COR)
txt=big.resize((1080,1920),Image.LANCZOS)
sh=Image.new('RGBA',txt.size,(0,0,0,0)); sh.putalpha(txt.getchannel('A').point(lambda a:int(a*0.5)))
sh=sh.filter(ImageFilter.GaussianBlur(3))
out=Image.new('RGBA',txt.size,(0,0,0,0)); out.alpha_composite(sh,(2,3)); out.alpha_composite(txt)
out.save('legendas/texto.png'); print('tamanho',f.size/K)
