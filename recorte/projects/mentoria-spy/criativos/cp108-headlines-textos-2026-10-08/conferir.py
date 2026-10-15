import subprocess, glob, numpy as np
from PIL import Image
MAE='CRIATIVOS-PRONTOS/108-ZAP-podcast-wpp-copy-nova-branca-ruiva-x-negra-afro.mp4'; L='criativos/cp108-headlines-textos-2026-10-08'
def frames(p):
    r=subprocess.run(['ffmpeg','-v','error','-i',p,'-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True)
    assert not r.stderr, r.stderr[:300]
    return np.frombuffer(r.stdout,np.uint8).reshape(-1,1280,720,3)
def md5a(p): return subprocess.run(['ffmpeg','-v','error','-i',p,'-map','0:a','-c','copy','-f','md5','-'],capture_output=True,text=True).stdout.strip()
def probe(p): return subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height,r_frame_rate,nb_frames:format=duration','-of','csv=p=0','-count_frames' if False else '-hide_banner',p],capture_output=True,text=True).stdout.split()
m=frames(MAE); am=md5a(MAE); print('mae',m.shape,am,probe(MAE))
# referência: 108 recodificada sem mudança nenhuma -> piso de compressão
rows=[]; tops=[]; ctas=[]
for p in sorted(glob.glob(f'{L}/pecas/*.mp4')):
    n=p.split('/')[-1][:3]; f=frames(p); a=md5a(p)
    jan=np.abs(f[:1009,346:].astype(np.int16)-m[:1009,346:]).mean(axis=(1,2,3))
    cta=np.abs(f[1009:].astype(np.int16)-m[1009:]).mean(axis=(1,2,3))
    t=np.array(Image.open(f'{L}/titulos/{n}.png').convert('RGB')).astype(np.int16)
    top=np.abs(f[:1009,:346].astype(np.int16)-t).mean(axis=(1,2,3))
    # resto do texto antigo: pixels escuros dentro da caixa onde o título novo é claro e o antigo era escuro
    old=(m[5,139:272,30:690].mean(2)<100)&(t[139:272,30:690].mean(2)>200)
    resto=(f[:1009,139:272,30:690].mean(3)[:,old]<200).sum(1).max()
    print(n,f.shape,probe(p),'audio==',a==am,f'jan/kar media {jan.mean():.2f} max {jan.max():.2f}',f'cta media {cta.mean():.2f} max {cta.max():.2f}',f'faixa vs png media {top.mean():.2f} max {top.max():.2f}','px resto antigo max',resto)
    tops.append(f[150,:346]); ctas.append(f[1100])
# folha: topo (frame 150) + CTA (frame 1100) de cada peça
W=360; cols=[]
for tp,ct in zip(tops,ctas):
    a=Image.fromarray(tp).resize((W,173)); b=Image.fromarray(ct).resize((W,640)); c=Image.new('RGB',(W,173+640+8),(40,40,40)); c.paste(a,(0,0)); c.paste(b,(0,181)); cols.append(c)
F=Image.new('RGB',(len(cols)*(W+8),cols[0].height),(40,40,40))
for i,c in enumerate(cols): F.paste(c,(i*(W+8),0))
F.save(f'{L}/conferencia/final-5.jpg',quality=88)
