# Frames lado a lado campeão × variação D nos 8 blocos + zoom nas costuras. Roda de projects/mentoria-spy/.
import subprocess
from PIL import Image, ImageDraw, ImageFont
CH='criativos-crus/spy-gram/ads-en/GD-AD01.mp4'; A='gram-detect/criativos/gd-ad01-var-avatar-2026-09-03'
D=f'{A}/GD-AD01-D-avatar-omnihuman.mp4'; C=f'{A}/conferencia'; FONT='gram-detect/scripts/fonts/Poppins-Bold.ttf'
def grab(src,t,out): subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',src,'-frames:v','1',out],check=True)
def label(im,txt):
    d=ImageDraw.Draw(im); f=ImageFont.truetype(FONT,40); d.rectangle([0,0,im.width,64],fill=(0,0,0)); d.text((16,10),txt,font=f,fill=(255,255,255)); return im
tiles=[]
for t,bl in [(1,'A'),(3,'A'),(9,'B'),(13,'C1'),(17.5,'E'),(24,'D1'),(27.5,'C3'),(31,'8')]:
    grab(CH,t,f'{C}/t{t}-campeao.png'); grab(D,t,f'{C}/t{t}-D.png')
    ca=label(Image.open(f'{C}/t{t}-campeao.png').convert('RGB'),f'A campeao · bloco {bl} · t={t}s'); dd=label(Image.open(f'{C}/t{t}-D.png').convert('RGB'),f'D omnihuman · bloco {bl} · t={t}s')
    pair=Image.new('RGB',(1080*2+16,1920),(20,20,20)); pair.paste(ca,(0,0)); pair.paste(dd,(1096,0)); pair.save(f'{C}/lado-a-lado-D-t{t}s.png'); tiles.append(pair.resize((544,480)))
sheet=Image.new('RGB',(544*4+30,480*2+30),(0,0,0))
for i,tl in enumerate(tiles): sheet.paste(tl,((i%4)*554,(i//4)*500))
sheet.save(f'{C}/folha-D.png')
# zoom costuras
rows=[('t3',(0,1080,1080,1280),'A degrade painel y1150-1230'),('t24',(0,900,1080,1060),'D1 costura y957 + karaoke'),('t31',(0,1040,1080,1200),'bloco 8 topo do card + karaoke'),('t31',(0,1700,1080,1920),'bloco 8 base do card / laterais'),('t9',(0,150,1080,330),'B topo do card sobre fundo desfocado'),('t13',(150,1430,930,1570),'C karaoke')]
out=Image.new('RGB',(1400,len(rows)*260),(0,0,0)); d=ImageDraw.Draw(out); y=0
for t,box,name in rows:
    for j,src in enumerate(('campeao','D')):
        im=Image.open(f'{C}/{t}-{src}.png').crop(box); w,h=im.size; s=min(690/w,220/h); im=im.resize((int(w*s),int(h*s)))
        out.paste(im,(j*700,y+22)); d.text((j*700+4,y+4),f'{name} — {src}',fill=(255,255,255))
    y+=260
out.save(f'{C}/zoom-costuras-D.png'); print('ok')
