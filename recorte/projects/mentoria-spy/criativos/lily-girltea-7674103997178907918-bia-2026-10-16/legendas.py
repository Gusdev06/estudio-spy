# Redesenha o texto fixo do original (branco levemente quente, Helvetica Neue Medium 64 px, sombra leve) na posição medida.
# Medição: máscara dos pixels claros e estáveis em todos os frames do original (texto fixo), depois
# busca por linha da origem (x,y) que maximiza a sobreposição (IoU) entre o texto renderizado e a máscara.
# Tamanho 64 foi o de maior IoU médio entre 62-66. Cor medida no original: mediana RGB (250,249,244).
from PIL import Image, ImageDraw, ImageFont, ImageFilter
H='/System/Library/Fonts/HelveticaNeue.ttc'
idx=next(i for i in range(14) if ImageFont.truetype(H,60,index=i).getname()[1]=='Medium')
f=ImageFont.truetype(H,64,index=idx)
LINHAS=[("When I forgive him for the",159,662),
        ("5th time but suddenly his",170,741),
        ("jokes irritate me, he’s not",167,820),
        ("that attractive and his",223,900),
        ("absence gives me relief",181,979)]
txt=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(txt)
for t,x,y in LINHAS: d.text((x,y), t, font=f, fill=(250,249,244,255))
sh=Image.new('RGBA',txt.size,(0,0,0,0)); sh.putalpha(txt.getchannel('A').point(lambda a:int(a*0.5)))
sh=sh.filter(ImageFilter.GaussianBlur(3))
out=Image.new('RGBA',txt.size,(0,0,0,0)); out.alpha_composite(sh,(2,3)); out.alpha_composite(txt)
out.save('legendas/texto.png'); print('ok')
