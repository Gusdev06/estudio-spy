#!/usr/bin/env python3
# Flora var5 (Zap, 360x640, layout de post sobre preto) com COPY NOVA, DUPLA NOVA e ESTÚDIO NOVO — 07/10/2026.
# Tudo RECONSTRUÍDO sobre preto limpo; nada do original é recortado por cima, exceto os painéis do funil (n 267-884 do original),
# que entram inteiros na faixa deles (y 150-500) e encaixados na timeline nova.
#   título ..... redesenhado (pílulas brancas unidas, Montserrat 700, caixa-alta 17 px, passo 31 px, centro y 95,5), frase nova
#   janela .... 360x303 em y 168-470: clipes Pruna da dupla nova, rosto (YuNet, maior score) no centro/altura medidos no original
#   karaokê ... redesenhado palavra a palavra: Poppins Bold 26 (capital 19 px), branco, caixa roxa (98,12,202) na palavra falada,
#               linha ≤ 306 px, 1 linha com capital em y 540-559, 2 linhas em 527-546 / 552-571
#   clarão .... o light leak do original (n 263-270) é lido no fundo preto do original (fora do título/karaokê/janela),
#               interpolado e reaplicado sobre o quadro novo (k·novo + luz), sem trazer pixel da pessoa nem do texto antigo
#   áudio ..... locução nova (vo.wav, ElevenLabs v3, 2 vozes)
# Uso (desta pasta): python3 montar.py p172 pecas/172-....mp4
import json, os, re, subprocess, sys, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
AQUI = os.path.dirname(os.path.abspath(__file__)); os.chdir(AQUI)
P, OUT = sys.argv[1], sys.argv[2]
REF = 'REFERENCIA-flora-original.mp4'
M = '../../../gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
FT = '../../../zapspy/_lib/Montserrat-Variable.ttf'; FK = '../../../gram-detect/scripts/fonts/Poppins-Bold.ttf'
W, H, FPS = 360, 640, 30; WY0, WY1 = 168, 471; WH = WY1 - WY0
PY0, PY1 = 150, 500                      # faixa dos painéis (eles vazam um pouco acima/abaixo da janela no original)
ALVO = {'a1': (161.85, 131.85, 154.64), 'b': (197.29, 140.61, 220.17), 'a2': (160.45, 126.01, 157.64), 'a3': (160.87, 124.80, 152.48)}  # cx,cy,h do rosto (janela), medidos no original
ROXO = (98, 12, 202); BRANCO = (252, 252, 252)
E = json.load(open(f'{P}/elenco.json')); T = json.load(open(f'{P}/molde/timeline.json')); NF = T['nf']; BL = T['blocos']

def ler(arq, w, h, vf=''):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', arq, '-vf', (vf + ',' if vf else '') + 'scale=in_color_matrix=bt709:out_color_matrix=bt709,format=rgb24',
                          '-f', 'rawvideo', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3)
O = ler(REF, W, H); assert len(O) == 1026, len(O)

# ---------- título ----------
def faixa(linhas, S=4, TH=168):
    img = Image.new('RGB', (W*S, TH*S), (0, 0, 0)); d = ImageDraw.Draw(img); msk = Image.new('L', (W*S, TH*S), 0); dm = ImageDraw.Draw(msk)
    size = 26*S
    while True:
        f = ImageFont.truetype(FT, size); f.set_variation_by_axes([700]); cap = f.getbbox('H')[3] - f.getbbox('H')[1]
        larg = [d.textlength(l, font=f) for l in linhas]
        if cap <= 17*S and max(larg) <= 292*S: break
        size -= 1
    lh = min(31*S, cap + 14*S); y0 = int(95.5*S - (lh*(len(linhas)-1) + cap)/2); padx, pady, r = 9*S, (lh - cap)//2 + 2*S, 8*S
    for i, lw in enumerate(larg):
        x0 = (W*S - lw)/2; y = y0 + i*lh; box = [x0-padx, y-pady, x0+lw+padx, y+cap+pady]
        d.rounded_rectangle(box, r, fill=(255, 255, 255)); dm.rounded_rectangle(box, r, fill=255)
    for i, (l, lw) in enumerate(zip(linhas, larg)):
        d.text(((W*S - lw)/2, y0 + i*lh - f.getbbox('H')[1]), l, font=f, fill=(0, 0, 0))
    A = np.asarray(msk.resize((W, TH), Image.LANCZOS)).astype(np.float32)[..., None]/255
    return np.asarray(img.resize((W, TH), Image.LANCZOS)).astype(np.float32), A
TF, TA = faixa(E['titulo']); TFn = TF.astype(np.uint8)

# ---------- karaokê ----------
S = 3; KY0, KY1 = 505, 590   # faixa onde o karaokê é desenhado
FNT = ImageFont.truetype(FK, 26*S); BBH = FNT.getbbox('H'); CAP = (BBH[3]-BBH[1])/S
ESP = FNT.getlength(' ') + 4*S; LMAX = 306
tok = lambda w: re.sub(r"[^A-Z0-9'?!]", '', w.upper().replace('’', "'"))
PW = [dict(w, t=tok(w['w'])) for w in T['palavras']]
larg = lambda ids: (sum(FNT.getlength(PW[i]['t']) for i in ids) + ESP*(len(ids)-1))/S
def linhas_de(ids):
    L = [[]]
    for i in ids:
        if L[-1] and larg(L[-1] + [i]) > LMAX: L.append([])
        L[-1].append(i)
    return L
BLOCOS = []; cur = []
for i, w in enumerate(PW):
    if cur and (len(cur) == 4 or len(linhas_de(cur + [i])) > 2 or PW[cur[-1]]['linha'] != w['linha']): BLOCOS.append(cur); cur = []
    cur.append(i)
    if re.search(r'[.?!]$', w['w']) or (re.search(r',$', w['w']) and len(cur) >= 2): BLOCOS.append(cur); cur = []
if cur: BLOCOS.append(cur)
estado = {}
for bi, ids in enumerate(BLOCOS):
    for k, i in enumerate(ids):
        a = 0 if (bi == 0 and k == 0) else int(round(PW[i]['s']*FPS))
        b = int(round(PW[ids[k+1]]['s']*FPS)) if k+1 < len(ids) else (int(round(PW[BLOCOS[bi+1][0]]['s']*FPS)) if bi+1 < len(BLOCOS) else NF)
        for fr in range(a, min(b, NF)): estado[fr] = (bi, k)
cache = {}
def kar(bi, k):
    if (bi, k) in cache: return cache[(bi, k)]
    L = linhas_de(BLOCOS[bi]); im = Image.new('RGBA', (W*S, (KY1-KY0)*S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    tops = [540] if len(L) == 1 else [527, 552]
    for li, ids in enumerate(L):
        x = (W - larg(ids))/2*S; ct = (tops[li]-KY0)*S
        for i in ids:
            lw = FNT.getlength(PW[i]['t'])
            if i == BLOCOS[bi][k]: d.rounded_rectangle([x-5*S, ct-8*S, x+lw+5*S, ct+(CAP+6)*S], radius=3*S, fill=ROXO+(255,))
            d.text((x, ct-BBH[1]), PW[i]['t'], font=FNT, fill=BRANCO+(255,)); x += lw + ESP
    a = np.asarray(im.resize((W, KY1-KY0), Image.LANCZOS)).astype(np.float32)
    cache[(bi, k)] = (a[..., :3], a[..., 3:]/255); return cache[(bi, k)]

# ---------- clipes ----------
def clipe(b):
    arq = f'{P}/clipes/{b}-s7.mp4'
    cw, chh = [int(v) for v in subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', arq], capture_output=True, text=True).stdout.strip().split(',')]
    f = ler(arq, cw, chh, 'fps=30').copy(); f[0] = f[1]          # 1º frame da Pruna é a imagem parada: troca pelo 2º, sem deslocar o sincronismo
    det = cv2.FaceDetectorYN_create(M, '', (cw, chh), 0.86, 0.3, 5000); r = []
    for x in f[::3]:
        d = det.detect(np.ascontiguousarray(x[..., ::-1]))[1]
        if d is not None and len(d): a = max(d, key=lambda q: q[-1]); r.append((a[0]+a[2]/2, a[1]+a[3]/2, a[3]))
    cx, cy, h = np.median(np.array(r), axis=0); tx, ty, th = ALVO[b]; s = max(th/h, W/cw, WH/chh)
    sw, sh = int(round(cw*s)), int(round(chh*s)); x = int(min(max(cx*s-tx, 0), sw-W)); y = int(min(max(cy*s-ty, 0), sh-WH))
    print(f'{b}: {len(f)} fr, rosto {h:.0f}px -> escala {s:.3f}, crop x{x} y{y} (centro {cx*s-x:.0f},{cy*s-y:.0f} alvo {tx:.0f},{ty:.0f})')
    return f, (sw, sh, x, y)
CL = {b: clipe(b) for b in ('a1', 'b', 'a2', 'a3')}
def janela(b, i):
    f, (sw, sh, x, y) = CL[b]; i = min(i, len(f)-1)
    return cv2.resize(f[i], (sw, sh), interpolation=cv2.INTER_LANCZOS4)[y:y+WH, x:x+W]

# ---------- clarão (light leak) ----------
CONH = np.r_[0:38, 152:166, 476:516, 600:640]           # linhas que no original são só fundo preto (fora do título, janela, painel e karaokê)
LIMPO = O[262].astype(np.float32)
def luz(n):
    f = cv2.GaussianBlur(O[n].astype(np.float32), (0, 0), 3)
    add = np.zeros((H, W, 3), np.float32); ys = np.arange(H)
    for c in range(3):
        v = f[CONH, :, c]                                 # (k, W)
        for x in range(W): add[:, x, c] = np.interp(ys, CONH, v[:, x])
    return cv2.GaussianBlur(add, (0, 0), 6)
LEAK = {}
for n in range(263, 271):
    add = luz(n)
    base = LIMPO[WY0:WY1]; r = O[n, WY0:WY1].astype(np.float32) - add[WY0:WY1]
    kw = np.clip((r*base).sum((0, 1))/(base*base).sum((0, 1)), 0, 1.2)        # escurecimento da janela sob a luz (vs n 262)
    branco = (O[262, 44:150].astype(np.float32).mean(2) > 200)
    kt = np.clip(np.array([np.median(O[n, 44:150][branco][:, c].astype(np.float32)/np.maximum(O[262, 44:150][branco][:, c], 1)) for c in range(3)]), 0, 1.2)
    LEAK[n] = (add, kw, kt)

# ---------- montagem ----------
TP = BL['paineis']['f0']; OR0 = BL['paineis']['orig0']
def orig_de(n):   # frame do original que dita luz/painel neste frame novo
    if TP-4 <= n < TP: return 263 + (n-(TP-4))
    if BL['paineis']['f0'] <= n <= BL['paineis']['f1']: return OR0 + (n-TP)
    return None
def quadro(n):
    fr = np.zeros((H, W, 3), np.float32); no = orig_de(n); lk = LEAK.get(no)
    if lk is not None: fr[:] = lk[0]
    # título
    if lk is None: fr[:168] = TF
    else: fr[:168] = TA*TF*lk[2] + (1-TA)*lk[0][:168]
    # janela / painel
    blk = next(b for b, d in BL.items() if d['f0'] <= n <= d['f1'])
    if blk == 'paineis':
        o = O[no].astype(np.float32); fr[PY0:PY1] = o[PY0:PY1]
    else:
        nv = janela(blk, n - BL[blk]['f0']).astype(np.float32)
        fr[WY0:WY1] = (lk[1]*nv + lk[0][WY0:WY1]) if lk is not None else nv
    # karaokê
    e = estado.get(n)
    if e is not None:
        rgb, a = kar(*e); fr[KY0:KY1] = a*rgb + (1-a)*fr[KY0:KY1]
    return np.clip(fr, 0, 255).astype(np.uint8)
os.makedirs(os.path.dirname(OUT) or '.', exist_ok=True)
p = subprocess.Popen(['ffmpeg', '-hide_banner', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                      '-i', f'{P}/audio/vo.wav', '-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '128k', '-ar', '44100', '-ac', '2',
                      '-vf', 'scale=in_color_matrix=bt709:out_color_matrix=bt709,format=yuv420p', '-c:v', 'libx264', '-preset', 'slow', '-crf', '16',
                      '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv', '-movflags', '+faststart', '-t', f'{NF/FPS:.3f}', OUT],
                     stdin=subprocess.PIPE)
for n in range(NF): p.stdin.write(quadro(n).tobytes())
p.stdin.close(); assert p.wait() == 0
json.dump({'blocos_karaoke': [[PW[i]['t'] for i in b] for b in BLOCOS]}, open(f'{P}/molde/karaoke.json', 'w'), indent=0)
print('ok ->', OUT, NF, 'fr', f'{len(BLOCOS)} blocos de karaokê; capital {CAP:.1f}px')
