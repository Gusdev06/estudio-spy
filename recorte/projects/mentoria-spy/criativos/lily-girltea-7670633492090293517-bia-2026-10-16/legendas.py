# Redesenha o texto fixo do original (branco, Helvetica Neue Medium, sombra leve) na posição medida.
# Medição: mínimo temporal de 31 frames (6 fps) do original, limiar >238 — o texto é a única coisa branca que não se mexe.
# Cada linha: topo da tinta (y, +2 px pelo melhor alinhamento por correlação) e centro (x) medidos no original; tamanho ajustado pela largura média das 8 linhas.
# O erro de digitação do original ("embarrasing", "mwhile") é mantido de propósito.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
H='/System/Library/Fonts/HelveticaNeue.ttc'
idx=next(i for i in range(14) if ImageFont.truetype(H,60,index=i).getname()[1]=='Medium')
# (texto, topo da tinta, x0, x1) medidos no original 1080x1920
L=[("Men are so embarrasing",873,214,865),("bc wdym you hide and",947,231,847),
   ("sit on the toilet while",1020,256,823),("scrolling through your",1094,242,838),
   ("phone looking at girls",1168,248,831),("mwhile your actual girl is",1242,207,874),
   ("waiting for you in the",1316,252,827),("other room",1391,388,689)]
def larg(s): f=ImageFont.truetype(H,s,index=idx); return sum((lambda b:b[2]-b[0])(f.getbbox(t)) for t,*_ in L)
alvo=sum(x1-x0+1 for _,_,x0,x1 in L)
lo,hi=40.0,80.0
for _ in range(30):
    m=(lo+hi)/2; (lo,hi)=(m,hi) if larg(m)<=alvo else (lo,m)
f=ImageFont.truetype(H,lo,index=idx)
txt=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(txt)
for t,top,x0,x1 in L:
    b=f.getbbox(t); cx=(x0+x1+1)/2
    d.text((cx-(b[2]-b[0])/2-b[0], top+2-b[1]), t, font=f, fill=(255,255,255,255))
sh=Image.new('RGBA',txt.size,(0,0,0,0)); sh.putalpha(txt.getchannel('A').point(lambda a:int(a*0.5)))
sh=sh.filter(ImageFilter.GaussianBlur(3))
out=Image.new('RGBA',txt.size,(0,0,0,0)); out.alpha_composite(sh,(2,3)); out.alpha_composite(txt)
out.save('legendas/texto.png'); print('tamanho',round(lo,2))
