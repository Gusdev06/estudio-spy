# Redesenha o texto fixo do original (branco, Helvetica Neue Medium, sombra leve) na posição medida.
# Cada linha é posicionada pelo topo da maiúscula (cap top) medido no original; tamanho ajustado pela largura da linha de referência.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
H='/System/Library/Fonts/HelveticaNeue.ttc'
idx=next(i for i in range(14) if ImageFont.truetype(H,60,index=i).getname()[1]=='Medium')
def fonte(txt,larg):
    lo,hi=20,140
    while hi-lo>1:
        m=(lo+hi)//2; b=ImageFont.truetype(H,m,index=idx).getbbox(txt)
        (lo,hi)=(m,hi) if b[2]-b[0]<=larg else (lo,m)
    return ImageFont.truetype(H,lo,index=idx)
BLOCO=["Tell me the worst thing","you’ve found on your","boyfriend’s phone. Not “he","liked a photo” I’m talking","the most unhinged thing in","your eyes"]
f=fonte(BLOCO[0],618)
txt=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(txt)
cap=lambda f:f.getbbox('T')[1]
def linha(t,captop):
    b=f.getbbox(t); d.text(((1080-(b[2]-b[0]))//2-b[0], captop-cap(f)), t, font=f, fill=(255,255,255,255))
linha("I’m bored",993)
for i,t in enumerate(BLOCO): linha(t,1139+i*72.8)
sh=Image.new('RGBA',txt.size,(0,0,0,0)); sh.putalpha(txt.getchannel('A').point(lambda a:int(a*0.5)))
sh=sh.filter(ImageFilter.GaussianBlur(3))
out=Image.new('RGBA',txt.size,(0,0,0,0)); out.alpha_composite(sh,(2,3)); out.alpha_composite(txt)
out.save('legendas/texto.png'); print('tamanho',f.size)
