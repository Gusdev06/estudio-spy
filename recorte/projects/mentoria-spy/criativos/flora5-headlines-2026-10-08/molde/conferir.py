# Conferência das 194-198 contra a var5. Uso: python3 conferir.py <mae.mp4> <pasta-pecas> <pasta-conferencia>
import sys, subprocess, glob, os, hashlib, numpy as np
from PIL import Image, ImageDraw
M, P, C = sys.argv[1:4]; W, H, TH = 360, 640, 168
def frames(f):
    r = subprocess.run(['ffmpeg','-v','error','-i',f,'-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True,check=True).stdout
    return np.frombuffer(r,np.uint8).reshape(-1,H,W,3)
def amd5(f):
    return hashlib.md5(subprocess.run(['ffmpeg','-v','error','-i',f,'-map','0:a','-c','copy','-f','data','-'],capture_output=True,check=True).stdout).hexdigest()
def probe(f):
    return subprocess.run(['ffprobe','-v','error','-show_entries','stream=codec_type,width,height,r_frame_rate,nb_frames:format=duration','-of','compact',f],capture_output=True,text=True).stdout.strip().replace('\n',' | ')
def errs(f):
    return subprocess.run(['ffmpeg','-v','error','-xerror','-i',f,'-f','null','-'],capture_output=True,text=True).stderr.strip()
VM = frames(M).astype(np.int16); am = amd5(M); topm = np.median(VM[::20,:TH],axis=0)
oldwhite = topm.mean(axis=2) > 200   # pílula antiga
log = [f'mãe: {probe(M)} | audio md5 {am}']
pecas = sorted(glob.glob(f'{P}/*.mp4')); sheet = []
for f in pecas:
    V = frames(f).astype(np.int16); n = os.path.basename(f)
    ok_n = len(V) == len(VM)
    d = np.abs(V[:, TH:] - VM[:, TH:]).mean(axis=(1,2,3))
    top = np.median(V[::20,:TH],axis=0); newwhite = top.mean(axis=2) > 200
    # resto do antigo: pixels brancos da pílula antiga que ficaram fora da nova devem estar pretos
    novo = np.zeros_like(newwhite)          # pílula nova preenchida por linha + 3 px de borda (antialias)
    for y in range(TH):
        b = np.where(newwhite[max(y-3,0):y+4].any(axis=0))[0]
        if len(b): novo[y, max(b.min()-3,0):b.max()+4] = True
    sobra = oldwhite & ~novo
    resto = top[sobra].max() if sobra.any() else 0
    # título cortado: pílula nova não encosta na borda nem na janela
    ys, xs = np.where(newwhite); corte = ys.min() <= 1 or ys.max() >= TH-2 or xs.min() <= 1 or xs.max() >= W-2
    estat = np.abs(V[:, :TH] - top).mean(axis=(1,2,3)); var = np.where(estat > 2)[0].tolist()
    a = amd5(f); e = errs(f)
    log.append(f'{n}: {probe(f)}\n  decodifica inteira: {"sim" if not e else e} | frames {len(V)} (mãe {len(VM)}) {"OK" if ok_n else "DIFERENTE"} | audio md5 {a} {"=" if a==am else "!="} mãe\n'
               f'  janela/karaokê/painéis (y>=168) vs mãe: média {d.mean():.2f}, máx {d.max():.2f} (frame {d.argmax()})\n'
               f'  título: pílula y {ys.min()}-{ys.max()} x {xs.min()}-{xs.max()} corte={corte} | pixels da pílula antiga fora da nova: {int(sobra.sum())}, brilho máx ali {resto:.0f} (preto≈0)\n'
               f'  frames em que a faixa difere da faixa estática (>2): {var}')
    sheet.append((n, V))
open(f'{C}/conferencia.txt','w').write('\n'.join(log)+'\n'); print('\n'.join(log))
# folha: mãe + 5 peças, colunas = instantes (inclui clarão 265 e 720)
inst = [0, 150, 265, 400, 620, 720, 900, 1020]; s = 0.5; w, h = int(W*s), int(H*s)
rows = [('var5 (mãe)', VM)] + sheet
img = Image.new('RGB', (w*len(inst), (h+18)*len(rows)), (30,30,30)); dr = ImageDraw.Draw(img)
for r, (n, V) in enumerate(rows):
    dr.text((4, r*(h+18)+3), n + '   frames ' + ' '.join(map(str, inst)), fill=(255,255,0))
    for c, k in enumerate(inst):
        img.paste(Image.fromarray(V[k].astype(np.uint8)).resize((w,h), Image.LANCZOS), (c*w, r*(h+18)+18))
img.save(f'{C}/final-5.jpg', quality=88)
# zoom só da faixa de título em tamanho real, incluindo um frame de clarão
z = Image.new('RGB', (W*2, TH*len(rows)), (0,0,0))
for r, (n, V) in enumerate(rows):
    z.paste(Image.fromarray(V[150,:TH].astype(np.uint8)), (0, r*TH)); z.paste(Image.fromarray(V[265,:TH].astype(np.uint8)), (W, r*TH))
z.save(f'{C}/titulos-zoom.png')
