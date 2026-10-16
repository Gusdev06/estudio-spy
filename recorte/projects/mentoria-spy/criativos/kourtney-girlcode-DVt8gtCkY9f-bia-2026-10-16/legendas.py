# Redesenha o texto fixo do original (branco, Helvetica Neue Medium, sombra leve) na posição medida.
# Medido no original 720x1280 (pixels brancos min(RGB)>232, frames 0,0 s e 3,0 s; texto fixo o vídeo todo), escalado x1,5:
# topo da ascendente de cada linha y=547,587,626,666,705,745; linha 1 x=182..537 (centro 360); bloco centralizado.
# larguras medidas (x1,5): 533,532,543,630,627,338. Tamanho = o que melhor casa a soma das larguras (a fonte do IG é um pouco mais larga que a Helvetica).
# Cada linha é posicionada pelo topo da ascendente ('h') medido.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
H='/System/Library/Fonts/HelveticaNeue.ttc'
idx=next(i for i in range(14) if ImageFont.truetype(H,60,index=i).getname()[1]=='Medium')
def fonte(txt,larg):
    lo,hi=20,140
    while hi-lo>1:
        m=(lo+hi)//2; b=ImageFont.truetype(H,m,index=idx).getbbox(txt)
        (lo,hi)=(m,hi) if b[2]-b[0]<=larg else (lo,m)
    return ImageFont.truetype(H,lo,index=idx)
BLOCO=["he could tell me a million","times he loves me but i’ll","never believe him bc you","don’t lust after other women","when you genuinely love the","one you’re with"]
TOPOS=[547,587,626,666,705,745]
LARG=[533,532,543,630,627,338]
soma=lambda n:sum(ImageFont.truetype(H,n,index=idx).getbbox(t)[2]-ImageFont.truetype(H,n,index=idx).getbbox(t)[0] for t in BLOCO)
n=min(range(30,80),key=lambda n:abs(soma(n)-sum(LARG)))
f=ImageFont.truetype(H,n,index=idx)
txt=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(txt)
asc=f.getbbox('h')[1]
for t,y in zip(BLOCO,TOPOS):
    b=f.getbbox(t); d.text((540-(b[2]-b[0])/2-b[0], y*1.5-asc), t, font=f, fill=(250,248,247,255))
    print(t, 'largura', b[2]-b[0])
sh=Image.new('RGBA',txt.size,(0,0,0,0)); sh.putalpha(txt.getchannel('A').point(lambda a:int(a*0.5)))
sh=sh.filter(ImageFilter.GaussianBlur(3))
out=Image.new('RGBA',txt.size,(0,0,0,0)); out.alpha_composite(sh,(2,3)); out.alpha_composite(txt)
out.save('legendas/texto.png'); print('tamanho',f.size)
