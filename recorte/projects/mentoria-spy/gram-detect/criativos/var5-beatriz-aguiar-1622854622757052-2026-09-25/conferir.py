# Folha de conferência: linha de cima = original, de baixo = peça, nos frames pedidos. Uso: python3 conferir.py saida.jpg n1 n2 ...
import sys,subprocess,numpy as np,os
from PIL import Image,ImageDraw
os.chdir(os.path.dirname(os.path.abspath(__file__)))
out=sys.argv[1]; ns=[int(x) for x in sys.argv[2:]]; w=240; h=427
def quadros(p):
    sel='+'.join(f'eq(n\\,{n})' for n in ns)
    raw=subprocess.run(['ffmpeg','-v','error','-i',p,'-vf',f"select='{sel}',scale={w}:{h}",'-vsync','0','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,h,w,3)
A=quadros('REFERENCIA-original.mp4'); B=quadros('pecas/variacao.mp4')
S=Image.new('RGB',(w*len(ns),2*h+20),'white'); d=ImageDraw.Draw(S)
for i,n in enumerate(ns):
    S.paste(Image.fromarray(A[i]),(i*w,20)); S.paste(Image.fromarray(B[i]),(i*w,20+h)); d.text((i*w+4,4),f'n {n} ({n/30:.2f}s)',fill='black')
S.save(out,quality=88)
