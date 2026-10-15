# Kit de montagem dos 5 formatos da Flora (28/09). Tudo em 720x1280, 30 fps, quadro a quadro em PIL e direto pro ffmpeg por pipe:
# nenhuma peça guarda os frames na memória (ver memória "montagem com karaokê estoura a memória").
# Estilo da casa (herdado da Flora): headline em pílula branca + Montserrat preta, destaque roxo; karaokê branco com a palavra ativa em caixa roxa.
import subprocess, json, math, os, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 720, 1280, 30
AQUI = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(AQUI, '../../../../zapspy/_lib/Montserrat-Variable.ttf')
ROXO = (110, 40, 220); BRANCO = (255, 255, 255); PRETO = (0, 0, 0)

def fonte(size, peso=800):
    f = ImageFont.truetype(FONT, int(size)); f.set_variation_by_axes([peso]); return f

# ---------- vídeo de entrada: leitor só pra frente, reabre com -ss se precisar voltar ----------
class Leitor:
    def __init__(self, path, ini=0.0):
        self.path, self.ini = path, ini
        w, h = [int(v) for v in subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', path], capture_output=True, text=True).stdout.strip().split(',')]
        self.w, self.h = w, h; self.p = None; self.idx = -1; self.last = None
        self.dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path], capture_output=True, text=True).stdout)
    def _abre(self, t):
        if self.p: self.p.kill()
        self.p = subprocess.Popen(['ffmpeg', '-v', 'error', '-ss', f'{t:.3f}', '-i', self.path, '-vf', f'fps={FPS}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
        self.base = round(t * FPS); self.idx = self.base - 1
    def frame(self, t):
        """frame (numpy HxWx3) no tempo t da fonte; t é preso ao fim do arquivo."""
        t = min(max(t, 0), self.dur - 1.5 / FPS); n = round(t * FPS)
        if self.p is None or n < self.idx or n > self.idx + 90: self._abre(n / FPS)
        while self.idx < n:
            b = self.p.stdout.read(self.w * self.h * 3)
            if len(b) < self.w * self.h * 3: break
            self.last = np.frombuffer(b, np.uint8).reshape(self.h, self.w, 3); self.idx += 1
        return self.last

def cobrir(fr, w, h, zoom=1.0, cx=0.5, cy=0.5):
    """recorta/escala fr pra cobrir w x h (object-fit: cover) com zoom e centro (cx, cy) em fração da fonte."""
    img = Image.fromarray(fr); fw, fh = img.size
    s = max(w / fw, h / fh) * zoom; cw, ch = min(w / s, fw), min(h / s, fh)
    x0 = max(0, min(cx * fw - cw / 2, fw - cw)); y0 = max(0, min(cy * fh - ch / 2, fh - ch))
    return img.resize((w, h), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))

def nitido(img, r=1.2, p=90): return img.filter(ImageFilter.UnsharpMask(radius=r, percent=p, threshold=2))

# ---------- headline em pílulas (mesma medida da Flora, escala 2x) ----------
def headline(linhas, larg_max=600, cap_alvo=34, peso=800):
    """linhas: [[(texto, destaque), ...], ...] -> RGBA recortada no tamanho da pílula."""
    S = 2; d0 = ImageDraw.Draw(Image.new('L', (1, 1)))
    size = int(cap_alvo * 1.45) * S
    while True:
        f = fonte(size, peso); bb = f.getbbox('H'); cap = bb[3] - bb[1]
        larg = [sum(d0.textlength(t, font=f) for t, _ in l) for l in linhas]
        if cap <= cap_alvo * S and max(larg) <= larg_max * S: break
        size -= 1
    lh = cap + 28 * S; padx, pady, r = 18 * S, (lh - cap) // 2 + 4 * S, 16 * S
    Wd = int(max(larg) + 2 * padx + 8 * S); Hd = int(lh * (len(linhas) - 1) + cap + 2 * pady + 8 * S)
    img = Image.new('RGBA', (Wd, Hd), (0, 0, 0, 0)); d = ImageDraw.Draw(img); y0 = pady + 4 * S
    for i, lw in enumerate(larg):
        x0 = (Wd - lw) / 2; y = y0 + i * lh
        d.rounded_rectangle([x0 - padx, y - pady, x0 + lw + padx, y + cap + pady], r, fill=BRANCO + (255,))
    for i, (l, lw) in enumerate(zip(linhas, larg)):
        x = (Wd - lw) / 2; y = y0 + i * lh - bb[1]
        for t, hl in l: d.text((x, y), t, font=f, fill=ROXO if hl else PRETO); x += d.textlength(t, font=f)
    return img.resize((Wd // S, Hd // S), Image.LANCZOS)

# ---------- karaokê ----------
def blocos(pal, max_pal=3, max_larg=560, size=58):
    """agrupa palavras em blocos de até max_pal, quebrando em pontuação; devolve [(ini, fim, [palavras])]."""
    f = fonte(size, 900); d0 = ImageDraw.Draw(Image.new('L', (1, 1))); out = []; cur = []
    for i, p in enumerate(pal):
        if cur and d0.textlength(' '.join(x['w'].upper() for x in cur + [p]), font=f) > max_larg: out.append(cur); cur = []
        cur.append(p); txt = ' '.join(x['w'].upper() for x in cur)
        fim_frase = p['w'][-1] in '.?!,:;'
        prox_gap = pal[i + 1]['s'] - p['e'] if i + 1 < len(pal) else 9
        if len(cur) >= max_pal or fim_frase or prox_gap > 0.25 or d0.textlength(txt, font=f) > max_larg:
            out.append(cur); cur = []
    if cur: out.append(cur)
    res = []
    for j, b in enumerate(out):
        ini = b[0]['s']; fim = out[j + 1][0]['s'] if j + 1 < len(out) else b[-1]['e'] + 0.6
        res.append((ini, min(fim, b[-1]['e'] + 0.6), b))
    return res

def karaoke(bl, t, size=58, stroke=7, cor_ativa=ROXO, pop=True):
    """RGBA do bloco ativo no tempo t (ou None). Palavra ativa ganha caixa roxa; bloco entra com pop de escala."""
    for ini, fim, b in bl:
        if ini <= t < fim: break
    else: return None
    f = fonte(size, 900); d0 = ImageDraw.Draw(Image.new('L', (1, 1)))
    ws = [x['w'].upper().strip('"') for x in b]; esp = d0.textlength(' ', font=f)
    larg = [d0.textlength(w, font=f) for w in ws]; tot = sum(larg) + esp * (len(ws) - 1)
    bb = f.getbbox('H'); cap = bb[3] - bb[1]; pad = 14
    img = Image.new('RGBA', (int(tot + 2 * pad + 2 * stroke + 20), int(cap + 2 * pad + 2 * stroke + 30)), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    x = pad + stroke + 10; y = pad + stroke + 10 - bb[1]
    for w, lw, p in zip(ws, larg, b):
        if p['s'] <= t < p['e'] + 0.08 or (p is b[-1] and t >= p['s']):
            if p['s'] <= t: d.rounded_rectangle([x - 10, y + bb[1] - 10, x + lw + 10, y + bb[3] + 10], 10, fill=cor_ativa + (255,))
        d.text((x, y), w, font=f, fill=BRANCO, stroke_width=stroke, stroke_fill=PRETO); x += lw + esp
    if pop:
        k = min(1.0, (t - ini) / 0.12); s = 0.86 + 0.14 * (1 - (1 - k) ** 3)
        if s < 0.999: img = img.resize((max(1, int(img.width * s)), max(1, int(img.height * s))), Image.LANCZOS)
    return img

# ---------- peças gráficas ----------
def card(img, raio=28, borda=6, sombra=True):
    """moldura de celular/card: cantos arredondados, borda branca e sombra."""
    w, h = img.size; W2, H2 = w + 2 * borda, h + 2 * borda
    out = Image.new('RGBA', (W2 + 40, H2 + 40), (0, 0, 0, 0))
    if sombra:
        sh = Image.new('L', out.size, 0); ImageDraw.Draw(sh).rounded_rectangle([20, 26, 20 + W2, 26 + H2], raio + borda, fill=150)
        out.putalpha(sh.filter(ImageFilter.GaussianBlur(14)))
    base = Image.new('RGBA', (W2, H2), BRANCO + (255,)); m = Image.new('L', (W2, H2), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, W2 - 1, H2 - 1], raio + borda, fill=255)
    mi = Image.new('L', (w, h), 0); ImageDraw.Draw(mi).rounded_rectangle([0, 0, w - 1, h - 1], raio, fill=255)
    base.paste(img.convert('RGB'), (borda, borda), mi); out.alpha_composite(Image.composite(base, Image.new('RGBA', (W2, H2)), m), (20, 20))
    return out

def entra(t, t0, dur=0.25):
    """0->1 com ease-out a partir de t0."""
    k = min(1.0, max(0.0, (t - t0) / dur)); return 1 - (1 - k) ** 3

def seta(t, cor=BRANCO, tam=90):
    """seta pra baixo quicando (CTA 'link below')."""
    img = Image.new('RGBA', (tam + 20, tam + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    dy = 12 * abs(math.sin(t * 6)); c = tam / 2 + 10
    pts = [(c - tam / 2, 10 + dy), (c + tam / 2, 10 + dy), (c, 10 + tam * 0.75 + dy)]
    d.polygon(pts, fill=cor + (255,), outline=PRETO + (255,)); d.rectangle([c - tam * 0.16, dy - 20, c + tam * 0.16, 12 + dy], fill=cor + (255,))
    return img

def colar(base, ov, cx, cy, alpha=1.0):
    """cola RGBA ov centrado em (cx, cy)."""
    if ov is None: return
    if alpha < 1: ov = ov.copy(); ov.putalpha(ov.getchannel('A').point(lambda a: int(a * alpha)))
    base.alpha_composite(ov, (int(cx - ov.width / 2), int(cy - ov.height / 2)))

# ---------- saída ----------
class Saida:
    def __init__(self, path, audio, dur):
        self.n = round(dur * FPS); self.path = path
        self.p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                                   '-i', audio, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
                                   '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-shortest', '-movflags', '+faststart', path],
                                  stdin=subprocess.PIPE)
    def escreve(self, img): self.p.stdin.write(img.convert('RGB').tobytes())
    def fecha(self): self.p.stdin.close(); self.p.wait(); print('ok ->', self.path, self.n, 'frames')

def dur_audio(a): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', a], capture_output=True, text=True).stdout)
def palavra_t(pal, alvo, n=1):
    """tempo de início da n-ésima ocorrência da palavra alvo (sem pontuação, minúscula)."""
    k = 0
    for p in pal:
        if p['w'].lower().strip('.,!?:;"\'') == alvo.lower():
            k += 1
            if k == n: return p['s']
    raise KeyError(alvo)
