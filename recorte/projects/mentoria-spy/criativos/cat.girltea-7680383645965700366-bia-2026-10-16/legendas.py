# Redesenha o texto fixo do original (branco, Helvetica Neue Medium, sombra leve) na posição medida.
# Medição (min de 17 frames, pixels >215 nas 3 cores): topo da tinta, centro x e largura de cada linha.
# Ajuste fino +1 px x / +2 px y = melhor sobreposição (varredura de deslocamento contra a máscara).
# Tamanho 72 = mediana do ajuste pela largura medida de cada linha (70–73).
from PIL import Image, ImageDraw, ImageFont, ImageFilter
H='/System/Library/Fonts/HelveticaNeue.ttc'
idx=next(i for i in range(14) if ImageFont.truetype(H,60,index=i).getname()[1]=='Medium')
f=ImageFont.truetype(H,72,index=idx)
# (texto, topo da tinta medido, centro x medido)
LINHAS=[("I asked him to",608,540.5),("unfollow a girl",699,539.0),("and he told me it",790,539.5),
        ("was his cousin.",880,537.0),("The whole time it",972,539.5),("was my fake account",1063,539.0)]
txt=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(txt)
for t,top,cx in LINHAS:
    b=f.getbbox(t)
    d.text((cx+1-(b[0]+b[2])/2, top+2-b[1]), t, font=f, fill=(255,255,255,255))
sh=Image.new('RGBA',txt.size,(0,0,0,0)); sh.putalpha(txt.getchannel('A').point(lambda a:int(a*0.5)))
sh=sh.filter(ImageFilter.GaussianBlur(3))
out=Image.new('RGBA',txt.size,(0,0,0,0)); out.alpha_composite(sh,(2,3)); out.alpha_composite(txt)
out.save('legendas/texto.png'); print('ok')
