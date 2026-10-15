# Folhas de conferência do podcast: meio de cada cena + setas, cortes (último × primeiro frame), karaokê (início de cada bloco). De projects/mentoria-spy/.
import subprocess, json
from PIL import Image, ImageDraw
P='gram-detect/criativos/podcast-hook-polemico-2026-09-05'; V=f'{P}/PODCAST-ZAP-hook-faithful-man.mp4'; C=f'{P}/conferencia'
T=json.load(open(f'{P}/molde/timeline.json')); TOTAL=T['total_frames']
def grab(t,o): subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{t:.3f}','-i',V,'-frames:v','1',o],check=True)
def grabn(n,o,vf=''): subprocess.run(['ffmpeg','-v','error','-y','-i',V,'-vf',f"select='eq(n,{n})'"+vf,'-vsync','0','-frames:v','1',o],check=True)
tiles=[]
for s in T['scenes']:
    t=(s['out_start']+s['out_frames']//2)/30; o=f"{C}/frame-cena-{s['cena']}.png"; grab(t,o); tiles.append((f"cena {s['cena']} meio · t={t:.2f}s",Image.open(o).convert('RGB').resize((288,512))))
for t in ((TOTAL-80)/30,(TOTAL-15)/30):
    o=f'{C}/frame-setas-{t:.1f}.png'; grab(t,o); tiles.append((f'setas · t={t:.2f}s',Image.open(o).convert('RGB').resize((288,512))))
sh=Image.new('RGB',(288*len(tiles)+80,532),(0,0,0)); d=ImageDraw.Draw(sh)
for i,(n,im) in enumerate(tiles): sh.paste(im,(i*298,20)); d.text((i*298+4,4),n,fill=(255,255,255))
sh.save(f'{C}/folha-cenas.png')
pairs=[(a['out_start']+a['out_frames']-1,b['out_start']) for a,b in zip(T['scenes'][:-1],T['scenes'][1:])]
sh=Image.new('RGB',(2*200+20,(356+22)*len(pairs)),(0,0,0)); d=ImageDraw.Draw(sh)
for k,(fA,fB) in enumerate(pairs):
    for j,f in enumerate((fA,fB)): o=f'{C}/corte-f{f}.png'; grabn(f,o); sh.paste(Image.open(o).convert('RGB').resize((200,356)),(j*220,k*378+22))
    d.text((4,k*378+4),f'corte {k+1}: frame {fA} → {fB} ({fB/30:.2f}s)',fill=(255,255,255))
sh.save(f'{C}/folha-cortes.png')
rows=[l.rstrip('\n').split('\t') for l in open(f'{P}/molde/karaoke.tsv') if not l.startswith('#')]; tiles=[]
for a,b,st,txt in rows:
    f=int(a)+2; o=f'{C}/k-f{f}.png'; y=1130 if int(a)>=T['scenes'][-1]['out_start'] else 1400
    grabn(f,o,f',crop=1080:200:0:{y}'); tiles.append((f'f{f} ({f/30:.2f}s) esperado: {txt}',Image.open(o).convert('RGB').resize((540,100))))
sh=Image.new('RGB',(560,120*len(tiles)),(0,0,0)); d=ImageDraw.Draw(sh)
for k,(n,im) in enumerate(tiles): sh.paste(im,(10,k*120+18)); d.text((10,k*120+3),n,fill=(255,255,0))
sh.save(f'{C}/folha-karaoke.png')
for f in ('folha-cenas','folha-cortes','folha-karaoke'): subprocess.run(['ffmpeg','-v','error','-y','-i',f'{C}/{f}.png','-q:v','4',f'{C}/{f}.jpg'],check=True)
print('folhas ok')
