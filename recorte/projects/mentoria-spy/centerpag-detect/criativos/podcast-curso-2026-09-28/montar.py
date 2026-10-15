# Monta o podcast do curso no estilo Flora: faixa em pílulas (branca, destaque roxo) + karaokê palavra-a-palavra
# (ativa em caixa roxa) + corte pra quem fala + card de correção ❌ I'm boring / ✅ I'm bored. 720x1280, 30fps.
# Uso: python3 montar.py <saida.mp4>
import sys, os, json, subprocess, re
import numpy as np
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]
W, H, FPS = 720, 1280, 30
CJK = '/System/Library/Fonts/Supplemental/Hiragino Sans GB.ttc'
ROXO = (150, 60, 245); BRANCO = (255,255,255); PRETO=(0,0,0); CINZA=(205,210,216); VERDE=(60,210,130); VERM=(240,80,80)
AUD = f'{D}/dialogo.mp3'
DUR = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',AUD],capture_output=True,text=True).stdout)
N = int(round(DUR*FPS))
shots = json.load(open(f'{D}/shots.json'))
words = [w for s in json.load(open(f'{D}/dialogo-16k.json'))['segments'] for w in s['words'] if w['word'].strip()]
_fc={}
def F(sz):
    sz=int(sz); _fc.setdefault(sz, ImageFont.truetype(CJK,sz)); return _fc[sz]

class Leitor:
    def __init__(s,p):
        s.p=p; s.w,s.h=[int(v) for v in subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',p],capture_output=True,text=True).stdout.strip().split(',')]
        s.proc=None; s.idx=-1; s.last=None
    def _o(s,t):
        if s.proc: s.proc.kill()
        s.proc=subprocess.Popen(['ffmpeg','-v','error','-ss',f'{t:.3f}','-i',s.p,'-vf',f'fps={FPS}','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE); s.idx=round(t*FPS)-1
    def frame(s,t):
        n=round(t*FPS)
        if s.proc is None or n<s.idx or n>s.idx+90: s._o(n/FPS)
        while s.idx<n:
            b=s.proc.stdout.read(s.w*s.h*3)
            if len(b)<s.w*s.h*3: break
            s.last=np.frombuffer(b,np.uint8).reshape(s.h,s.w,3); s.idx+=1
        return s.last
LE={s['tag']:Leitor(f"{D}/clipes/{s['tag']}.mp4") for s in shots}
def shot_de(t):
    for s in shots:
        if s['ini']<=t<s['fim']: return s
    return shots[-1] if t>=shots[-1]['fim'] else shots[0]
def cover(fr,scale=1.06,cx=0.5,cy=0.42):
    im=Image.fromarray(fr); fw,fh=im.size; s=max(W/fw,H/fh)*scale; cw,ch=min(W/s,fw),min(H/s,fh)
    x0=max(0,min(cx*fw-cw/2,fw-cw)); y0=max(0,min(cy*fh-ch/2,fh-ch))
    return im.resize((W,H),Image.LANCZOS,box=(x0,y0,x0+cw,y0+ch))

# ---- faixa em pílulas ----
def pill_line(d, tokens, cy, sz=34, padx=14, pady=9, r=16):
    f=F(sz); larg=[d.textlength(t,font=f) for t,_ in tokens]; tot=sum(larg); x0=(W-tot)/2
    bb=f.getbbox('H我'); cap=bb[3]-bb[1]
    d.rounded_rectangle([x0-padx, cy-cap/2-pady, x0+tot+padx, cy+cap/2+pady], r, fill=BRANCO)
    x=x0
    for (t,hl),lw in zip(tokens,larg):
        if hl: d.rounded_rectangle([x-4, cy-cap/2-pady+3, x+lw+4, cy+cap/2+pady-3], r-4, fill=ROXO)
        d.text((x, cy-cap/2-bb[1]), t, font=f, fill=BRANCO if hl else PRETO); x+=lw
def banner(d):
    pill_line(d,[('「我很無聊」',1),('你還在說 ',0),("I'm boring？",0)],92,32)
    pill_line(d,[('免費公開課 ',0),('用英文思考不翻譯',1)],140,32)

# ---- karaokê: usa o ROTEIRO (tradicional), tokens = char CJK ou palavra ASCII, timing linear no span da fala ----
def tokenizar(txt):
    txt=txt.replace('’',"'").strip()
    return [m.group() for m in re.finditer(r"[A-Za-z0-9'’.!?]+|[^\sA-Za-z0-9]", txt) if m.group().strip()]
def karaoke(d, t):
    s=shot_de(t); toks=tokenizar(s['txt'])
    if not toks: return
    dur=max(s['fim']-s['ini'],0.1); k_ativo=int((t-s['ini'])/dur*len(toks))
    # escolhe fonte e quebra em linhas que cabem (até 3)
    for sz in range(46,28,-2):
        f=F(sz); esp=6
        linhas=[[]]; cur=0
        for tk in toks:
            lw=d.textlength(tk,font=f)
            if cur+lw+esp>W-56 and linhas[-1]: linhas.append([]); cur=0
            linhas[-1].append((tk,lw)); cur+=lw+esp
        if len(linhas)<=3: break
    bb=f.getbbox('H我'); cap=bb[3]-bb[1]; lh=cap+30; y=1044-(len(linhas)-1)*lh/2
    gi=0
    for ln in linhas:
        tot=sum(lw for _,lw in ln)+esp*(len(ln)-1); x=(W-tot)/2
        for tk,lw in ln:
            ativa=(gi==k_ativo)
            if ativa: d.rounded_rectangle([x-7,y-cap/2-7,x+lw+7,y+cap/2+7],9,fill=ROXO)
            d.text((x,y-cap/2-bb[1]),tk,font=f,fill=BRANCO,stroke_width=0 if ativa else 5,stroke_fill=PRETO); x+=lw+esp; gi+=1
        y+=lh

def ease(t,t0,dr=0.35): k=min(1,max(0,(t-t0)/dr)); return 1-(1-k)**3
def card(img,t):
    t0,t1=16.2,22.9
    if not(t0<=t<t1): return
    a=ease(t,t0)*(1-ease(t,t1-0.4,0.4))
    if a<=0.02: return
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov); x0,x1,y0,y1=64,W-64,360,540
    d.rounded_rectangle([x0,y0,x1,y1],26,fill=(15,18,24,int(230*a)))
    def X(cx,cy,r,al): d.line([(cx-r,cy-r),(cx+r,cy+r)],fill=VERM+(al,),width=7); d.line([(cx-r,cy+r),(cx+r,cy-r)],fill=VERM+(al,),width=7)
    def CK(cx,cy,r,al): d.line([(cx-r,cy),(cx-r*.2,cy+r*.8)],fill=VERDE+(al,),width=7); d.line([(cx-r*.2,cy+r*.8),(cx+r*1.1,cy-r)],fill=VERDE+(al,),width=7)
    X(x0+42,y0+44,15,int(255*a)); d.text((x0+74,y0+22),"I'm boring  =  你很無趣",font=F(34),fill=(255,150,150,int(255*a)),stroke_width=3,stroke_fill=(0,0,0,int(255*a)))
    a2=ease(t,17.6)*a
    if a2>0.02:
        CK(x0+42,y0+112,15,int(255*a2)); d.text((x0+74,y0+90),"I'm bored  =  你覺得無聊",font=F(34),fill=(150,235,175,int(255*a2)),stroke_width=3,stroke_fill=(0,0,0,int(255*a2)))
    img.alpha_composite(ov)

CX={'A':0.5,'B':0.5}
def build(t):
    s=shot_de(t); L=LE[s['tag']]; lt=min(t-s['ini'], L.h/1)
    img=cover(L.frame(t-s['ini']), 1.06, 0.5, 0.40).convert('RGBA')
    d=ImageDraw.Draw(img); banner(d); karaoke(d,t); card(img,t)
    return img

if __name__=='__main__':
    if OUT.startswith('SAMPLE:'):
        S='/private/tmp/claude-501/-Users-gustagoat-Documents-AIS-OS/e266ecd9-980f-4616-899d-5fa20ca47b92/scratchpad/ref'
        for t in [float(x) for x in OUT[7:].split(',')]: build(t).convert('RGB').save(f'{S}/pod_{int(t*100):05d}.png')
        print('samples ok')
    else:
        p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i',AUD,'-map','0:v','-map','1:a','-c:v','libx264','-crf','18','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
        for n in range(N): p.stdin.write(build(n/FPS).convert('RGB').tobytes())
        p.stdin.close(); p.wait(); print('ok ->',OUT,N)
