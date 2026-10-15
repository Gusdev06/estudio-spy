# Compositor PREMIUM da variação Adele: 2 câmeras (chunks alternados) + punch-ins nos cortes do original +
# B-roll original inserido + legenda 2 linhas (principal + parêntese cinza nas frases-chave) + card de correção ❌→✅ + faixa.
# Uso: python3 premium.py <saida.mp4>   (roda de qualquer lugar; caminhos absolutos)
import sys, os, json, subprocess, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

D = os.path.dirname(os.path.abspath(__file__))
S = '/private/tmp/claude-501/-Users-gustagoat-Documents-AIS-OS/e266ecd9-980f-4616-899d-5fa20ca47b92/scratchpad/adele'
OUT = sys.argv[1]
W, H, FPS = 720, 1280, 30
CJK = '/System/Library/Fonts/Supplemental/Hiragino Sans GB.ttc'
ROSA = (255, 45, 150); BRANCO = (255, 255, 255); PRETO = (0, 0, 0); CINZA = (200, 205, 210)
VERDE = (60, 210, 130); VERMELHO = (240, 70, 70)
AUDIO = f'{S}/audio.m4a'
DUR = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',AUDIO],capture_output=True,text=True).stdout)
N = int(round(DUR * FPS))

# ---- fontes ----
_fc = {}
def fonte(sz):
    sz = int(sz)
    if sz not in _fc: _fc[sz] = ImageFont.truetype(CJK, sz)
    return _fc[sz]

# ---- leitor de chunk (frames sob demanda, reabre p/ voltar) ----
class Leitor:
    def __init__(self, path):
        self.path = path
        self.w, self.h = [int(v) for v in subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',path],capture_output=True,text=True).stdout.strip().split(',')]
        self.p=None; self.idx=-1; self.last=None
    def _open(self, t):
        if self.p: self.p.kill()
        self.p = subprocess.Popen(['ffmpeg','-v','error','-ss',f'{t:.3f}','-i',self.path,'-vf',f'fps={FPS}','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
        self.idx = round(t*FPS)-1
    def frame(self, t):
        n = round(t*FPS)
        if self.p is None or n < self.idx or n > self.idx+90: self._open(n/FPS)
        while self.idx < n:
            b = self.p.stdout.read(self.w*self.h*3)
            if len(b) < self.w*self.h*3: break
            self.last = np.frombuffer(b,np.uint8).reshape(self.h,self.w,3); self.idx += 1
        return self.last

CH = {'c0':(0.0,'c0'),'c1':(14.48,'c1'),'c2':(28.88,'c2'),'c3':(43.14,'c3'),'c4':(57.94,'c4'),'c5':(72.18,'c5')}
LE = {k:Leitor(f'{D}/clipes/{k}.mp4') for k in CH}
BROLL = Leitor(f'{D}/clipes/broll-orig.mp4')
def fonte_do_t(t):
    off, key = max((v for v in CH.values() if v[0] <= t), key=lambda v: v[0])
    return LE[key], t - off   # leitor e tempo local no chunk

def cover(fr, scale=1.0, cx=0.5, cy=0.5):
    img = Image.fromarray(fr); fw, fh = img.size
    s = max(W/fw, H/fh) * scale; cw, ch = min(W/s, fw), min(H/s, fh)
    x0 = max(0, min(cx*fw - cw/2, fw-cw)); y0 = max(0, min(cy*fh - ch/2, fh-ch))
    return img.resize((W,H), Image.LANCZOS, box=(x0,y0,x0+cw,y0+ch))

# ---- punch-ins nos cortes do original (escala, cx, cy) ----
CUTS = [0,2.57,5.97,18.49,23.59,28.23,31.53,32.63,35.67,39.57,41.81,43.34,52.35,55.62,58.26,61.23,66.43,68.60,70.54,84.99]
ESTILOS = [(1.02,0.5,0.42),(1.16,0.5,0.40),(1.08,0.44,0.42),(1.22,0.5,0.38),(1.10,0.56,0.42),(1.18,0.5,0.40),(1.05,0.48,0.43)]
def estilo(t):
    i = max(k for k,c in enumerate(CUTS) if c <= t)
    return ESTILOS[i % len(ESTILOS)]

# ---- legendas ----
FIX = {'convenience':'convenient','名費':'免費',"I'm not your life":'',' 這檔':'這場 ','這檔':'這場'}
def corrige(t):
    for a,b in FIX.items(): t=t.replace(a,b)
    return t.strip()
segs = [dict(s,text=corrige(s['text'])) for s in json.load(open(f'{S}/audio-16k.json'))['segments']]
# parênteses cinza nas frases-chave (fiel ao original)
PAR = {5.84:'（不好意思，我這週五不方便）',25.16:'（對我來說不太方便）',26.54:'（我現在有點忙／抽不開身）',
       36.38:'（我很開心）',39.40:'（開心到不行）',40.46:'（不能更開心了）'}
def par_do(seg):
    for k,v in PAR.items():
        if abs(seg['start']-k) < 0.6: return v
    return None

def toks(txt):
    import re; out=[]
    for m in re.finditer(r"[A-Za-z0-9',\.\!\? ]+|[^A-Za-z0-9]+", txt):
        s=m.group(); out.append((s, ROSA if re.search(r'[A-Za-z]',s) else BRANCO))
    return out

def linha(d, tokens, cy, sz, stroke=6, margem=46):
    while sz>20:
        f=fonte(sz); lw=sum(d.textlength(t,font=f) for t,_ in tokens)
        if lw<=W-2*margem: break
        sz-=2
    f=fonte(sz); lw=sum(d.textlength(t,font=f) for t,_ in tokens); x=(W-lw)/2
    bb=f.getbbox('H我'); h=bb[3]-bb[1]
    for t,c in tokens:
        d.text((x,cy-h/2-bb[1]),t,font=f,fill=c,stroke_width=stroke,stroke_fill=PRETO); x+=d.textlength(t,font=f)

def banner(d):
    linha(d,[('「我不方便」你還在 ',ROSA),('I’m not convenient ?',BRANCO)],128,40,5)
    linha(d,[('免費公開課 ',BRANCO),('帶你用英文思考不翻譯！',ROSA)],176,40,5)

def legenda(d, t):
    for s in segs:
        if s['start']<=t<s['end'] and s['text']:
            p = par_do(s)
            linha(d, toks(s['text']), 1044 if p else 1064, 46)
            if p: linha(d,[(p,CINZA)],1104,34,4)
            break

# ---- card de correção ❌ -> ✅ (23.7 - 31.5) ----
def ease(t,t0,dur=0.35):
    k=min(1,max(0,(t-t0)/dur)); return 1-(1-k)**3
def card_correcao(img, t):
    t0,t1=23.7,31.5
    if not (t0<=t<t1): return
    a=ease(t,t0)*(1-ease(t,t1-0.4,0.4))
    if a<=0.02: return
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    bx0,bx1,by0,by1=70,W-70,300,470
    d.rounded_rectangle([bx0,by0,bx1,by1],28,fill=(15,18,24,int(230*a)))
    def x_vermelho(cx,cy,r,al):
        d.line([(cx-r,cy-r),(cx+r,cy+r)],fill=VERMELHO+(al,),width=7); d.line([(cx-r,cy+r),(cx+r,cy-r)],fill=VERMELHO+(al,),width=7)
    def check_verde(cx,cy,r,al):
        d.line([(cx-r,cy),(cx-r*0.2,cy+r*0.8)],fill=VERDE+(al,),width=7); d.line([(cx-r*0.2,cy+r*0.8),(cx+r*1.1,cy-r)],fill=VERDE+(al,),width=7)
    x_vermelho(bx0+52,by0+58,16,int(255*a))
    d.text((bx0+90,by0+34),"I’m not convenient",font=fonte(44),fill=(255,140,140,int(255*a)),stroke_width=3,stroke_fill=(0,0,0,int(255*a)))
    a2=ease(t,25.0)*a
    if a2>0.02:
        check_verde(bx0+52,by0+120,16,int(255*a2))
        d.text((bx0+90,by0+100),"It’s not convenient for me",font=fonte(38),fill=(150,235,175,int(255*a2)),stroke_width=3,stroke_fill=(0,0,0,int(255*a2)))
    img.alpha_composite(ov)

# ---- montar 1 frame ----
def build_frame(t):
    if 3.70 <= t < 5.97:                       # B-roll original
        return cover(BROLL.frame(t-3.70), 1.0).convert('RGBA')
    L, lt = fonte_do_t(t); sc,cx,cy = estilo(t)
    img = cover(L.frame(lt), sc, cx, cy).convert('RGBA')
    d = ImageDraw.Draw(img); banner(d); legenda(d, t); card_correcao(img, t)
    return img

if __name__ == '__main__':
    if OUT.startswith('SAMPLE:'):              # SAMPLE:t1,t2,... -> PNGs no scratchpad
        for t in [float(x) for x in OUT[7:].split(',')]:
            build_frame(t).convert('RGB').save(f'{S}/pframe_{int(t*100):05d}.png')
        print('samples ok')
    else:
        proc = subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
            '-i',AUDIO,'-map','0:v','-map','1:a','-c:v','libx264','-crf','18','-preset','medium','-pix_fmt','yuv420p',
            '-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
        for n in range(N):
            proc.stdin.write(build_frame(n/FPS).convert('RGB').tobytes())
        proc.stdin.close(); proc.wait(); print('ok ->', OUT, N, 'frames')
