# Redesenho do zero dos cards do Amanda Lima 1259333446315112 (caminho B, 25/09). Nada da mulher original entra aqui:
# cada card é desenhado em PIL (2x supersampling) com as medidas do original (bbox por cor, extensão do texto -> tamanho da fonte
# resolvido pela largura medida, topo da caixa-alta medido). Animações: curvas de slide medidas por frame (work/tracks.json).
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SS = 2
FB = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
FR = '/System/Library/Fonts/Supplemental/Arial.ttf'
_fc = {}
def font(path, px):
    k = (path, px)
    if k not in _fc: _fc[k] = ImageFont.truetype(path, px)
    return _fc[k]

def hexc(h, a=255):
    h = h.lstrip('#'); return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)

def fit_size(path, text, width):
    lo, hi = 4 * SS, 120 * SS
    while hi - lo > 1:
        m = (lo + hi) // 2
        b = font(path, m).getbbox(text)
        if b[2] - b[0] > width * SS: hi = m
        else: lo = m
    return lo

class Layer:
    """Camada RGBA em coordenadas do quadro (1x), desenhada em 2x dentro da caixa (x0,y0,x1,y1)."""
    def __init__(self, box, pad=24):
        self.x0, self.y0 = box[0] - pad, box[1] - pad
        self.w, self.h = box[2] - box[0] + 2 * pad, box[3] - box[1] + 2 * pad
        self.im = Image.new('RGBA', (self.w * SS, self.h * SS), (0, 0, 0, 0))
    def _xy(self, x, y): return ((x - self.x0) * SS, (y - self.y0) * SS)
    def rrect(self, box, r, fill, outline=None, width=0):
        d = ImageDraw.Draw(self.im)
        a = self._xy(box[0], box[1]); b = self._xy(box[2], box[3])
        d.rounded_rectangle([a, b], radius=r * SS, fill=fill, outline=outline, width=int(width * SS))
    def over(self, other):  # compõe outra imagem RGBA (mesmo tamanho) por cima
        self.im = Image.alpha_composite(self.im, other)
    def blank(self): return Image.new('RGBA', self.im.size, (0, 0, 0, 0))
    def rrect_alpha(self, box, r, fill, soft=0):
        t = Image.new('RGBA', self.im.size, tuple(fill[:3]) + (0,)); d = ImageDraw.Draw(t)
        d.rounded_rectangle([self._xy(box[0], box[1]), self._xy(box[2], box[3])], radius=r * SS, fill=fill)
        if soft: t = t.filter(ImageFilter.GaussianBlur(soft * SS))
        self.over(t)
    def shadow(self, box, r, alpha=70, blur=6, dy=3):
        t = self.blank(); d = ImageDraw.Draw(t)
        d.rounded_rectangle([self._xy(box[0], box[1] + dy), self._xy(box[2], box[3] + dy)], radius=r * SS, fill=(0, 0, 0, alpha))
        self.over(t.filter(ImageFilter.GaussianBlur(blur * SS)))
    def poly(self, pts, fill):
        ImageDraw.Draw(self.im).polygon([self._xy(*p) for p in pts], fill=fill)
    def line(self, a, b, fill, width):
        ImageDraw.Draw(self.im).line([self._xy(*a), self._xy(*b)], fill=fill, width=max(1, int(round(width * SS))))
    def circle(self, c, r, fill=None, outline=None, width=0):
        x, y = self._xy(*c)
        ImageDraw.Draw(self.im).ellipse([x - r * SS, y - r * SS, x + r * SS, y + r * SS], fill=fill, outline=outline, width=int(width * SS))
    def text(self, lines, path, width, tops, color, left=None, center=None):
        """lines: textos; width: largura medida da linha mais larga; tops: topo da caixa-alta de cada linha (1x)."""
        wide = max(lines, key=lambda s: font(path, 40).getbbox(s)[2] - font(path, 40).getbbox(s)[0])
        f = font(path, fit_size(path, wide, width))
        capoff = f.getbbox('H')[1]
        d = ImageDraw.Draw(self.im)
        for s, top in zip(lines, tops):
            b = f.getbbox(s)
            if center is not None: x = center * SS - (b[0] + b[2]) / 2
            else: x = left * SS - b[0]
            y = (top - self.y0) * SS - capoff
            d.text((x - self.x0 * SS, y), s, font=f, fill=color)
    def done(self):
        a = np.asarray(self.im).astype(np.float32) / 255.0
        a = np.concatenate([a[..., :3] * a[..., 3:4], a[..., 3:4]], 2)          # pré-multiplica ANTES de reduzir (sem franja escura)
        import cv2
        return (self.x0, self.y0, cv2.resize(a, (self.w, self.h), interpolation=cv2.INTER_AREA))

W = (255, 255, 255, 255)
NAVY = '#0f376c'; NAVY2 = '#0b2f62'; RED = '#f33c35'; INK = '#0d264b'

def build():
    L = {}
    # ---------- A (n 0-177) ----------
    l = Layer((135, 730, 352, 766))
    for a, b in [((140, 735.5), (167, 735.5)), ((140, 735), (140, 762)), ((147, 751), (195, 751))]:
        l.line(a, b, hexc('#e8453f', 235), 1.6)
    l.rrect((196, 734, 348, 762), 14, hexc('#f33c37'))
    l.circle((211, 748), 6, fill=W); l.circle((211, 748), 2.2, fill=hexc('#f33c37'))
    l.text(['EXPERT GUIDE'], FR, 96, [744], W, left=232)
    L['A_pill'] = l.done()
    l = Layer((151, 765, 470, 884))
    l.rrect((151, 765, 470, 884), 8, hexc(NAVY2))
    l.text(['HOW TO READ HIS', 'MESSAGES'], FB, 221, [807, 832], W, center=312.5)
    L['A_navy'] = l.done()
    l = Layer((161, 912, 559, 1212), pad=30)
    l.rrect_alpha((158, 909, 562, 1215), 20, (255, 250, 250, 150), soft=6)         # brilho difuso da borda
    l.rrect_alpha((163, 914, 557, 1210), 18, hexc('#ece6e6', 236), soft=1.2)       # vidro fosco rosado
    l.circle((572, 975), 24, outline=hexc('#bfbfc2', 170), width=9)                # anel cinza que vaza na borda direita
    for bx in [(205, 1037, 338, 1190), (360, 1037, 510, 1190)]:
        l.rrect(bx, 12, hexc('#f3f0f0'), outline=hexc('#e2dcdc'), width=1)
    # lixeira
    red = hexc('#a8393c')
    l.rrect((209, 968, 231, 991), 3, None, outline=red, width=2.2)
    l.line((205, 965), (235, 965), red, 2.2); l.rrect((215, 959, 225, 965), 2, None, outline=red, width=2)
    for x in (216, 220, 224): l.line((x, 971), (x, 987), red, 1.6)
    l.text(['HIDDEN DATA', 'DETECTED'], FB, 153, [950, 985], red, center=383.5)
    l.text(['310'], FB, 63, [1071], hexc('#a13b3d'), center=271.5)
    l.text(['172'], FB, 63 * (font(FB, 80).getbbox('172')[2] - font(FB, 80).getbbox('172')[0]) / (font(FB, 80).getbbox('310')[2] - font(FB, 80).getbbox('310')[0]), [1071], hexc('#a13b3d'), center=434)
    grey = hexc('#8c8d90')
    l.text(['Deleted', 'Messages'], FR, 75, [1128, 1152], grey, center=271.5)
    wm = font(FR, 80).getbbox('Messages'); wp = font(FR, 80).getbbox('Photos/Videos')
    l.text(['Deleted', 'Photos/Videos'], FR, 75 * (wp[2] - wp[0]) / (wm[2] - wm[0]), [1128, 1152], grey, center=434)
    L['A_card'] = l.done()
    # ---------- C (n 236-401) ----------
    l = Layer((80, 878, 504, 1024))
    l.poly([(80, 878), (504, 878), (504, 1024), (94, 1024)], hexc(NAVY))
    l.text(['DECEIVED FOR', '5 YEARS'], FB, 292, [911, 949], hexc('#f1f3f6'), left=107)
    L['C_navy'] = l.done()
    l = Layer((58, 878, 406, 1078))
    l.rrect((60, 880, 66, 1064), 3, hexc('#f23c36'))
    l.rrect((76, 1026, 403, 1075), 9, hexc('#f43c35'))
    l.text(['PLANNING THE WEDDING'], FR, 231, [1045], W, left=124)
    L['C_pill'] = l.done()
    # ---------- D (n 409-693) ----------
    l = Layer((26, 798, 456, 1132))
    l.shadow((27, 844, 456, 1132), 12, alpha=40, blur=5, dy=2)
    l.rrect((27, 844, 456, 1132), 12, hexc('#e9e9e7'))
    l.rrect((26, 798, 254, 852), 3, hexc(RED))
    l.text(['MY STORY'], FR, 122, [817], W, left=80)
    l.text(['THE TRUTH', 'I DISCOVERED'], FB, 280, [884, 925], hexc('#0c2448'), left=73)
    l.rrect((71, 1018, 77, 1098), 3, hexc(RED))
    l.text(['No more lies'], FB, 127, [1027], hexc('#2e6078'), left=96)
    l.text(['Protect your future'], FB, 149, [1071], hexc('#081a33'), left=96)
    L['D'] = l.done()
    # ---------- E (n 701-1056) ----------
    l = Layer((60, 804, 504, 1074))
    l.rrect((60, 848, 504, 1074), 12, hexc(NAVY), outline=hexc('#3d6597'), width=1.2)
    l.rrect((82, 804, 344, 858), 10, hexc(RED))
    l.text(['GLOBAL ACCESS'], FR, 169, [824], W, left=128)
    l.text(['100% REMOTE AND', 'ANONYMOUS'], FB, 324, [888, 927], hexc('#f1f3f6'), left=95)
    l.rrect((92, 1008, 374, 1044), 7, hexc('#345e8a'))
    l.circle((111, 1025), 6, fill=hexc('#35c49c'))
    l.text(['SECURE PROTOCOL ACTIVE'], FB, 196, [1020], hexc('#e6f1fb'), left=145)
    L['E'] = l.done()
    # ---------- G (n 1239-1358) + barra do topo até 1459 ----------
    l = Layer((24, 28, 500, 84))
    l.shadow((24, 28, 500, 84), 12, alpha=90, blur=5, dy=4)
    l.rrect((24, 28, 500, 84), 12, hexc('#f33c34'))
    l.circle((52, 52), 5, fill=W)
    l.text(['ENCRYPTED CONNECTION'], FR, 224, [48], W, left=161)
    L['G_top'] = l.done()
    l = Layer((39, 830, 388, 1172))
    l.rrect_alpha((48, 830, 388, 1172), 10, (16, 16, 24, 150))
    l.rrect((48, 830, 388, 1172), 10, None, outline=(255, 255, 255, 40), width=1.2)
    l.rrect((39, 830, 46, 1172), 2, hexc('#f03d37'))
    l.circle((70, 859), 5, fill=hexc('#ee3b42'))
    l.text(['TUTORIAL SERIES'], FR, 127, [853], hexc('#ee3b42'), left=86)
    l.text(['STEP-BY-STEP', 'GUIDE'], FB, 204, [915, 937], hexc('#f4f4f6'), center=174)
    l.rrect((69, 1086, 360, 1144), 8, hexc('#efefef'))
    l.circle((91, 1112), 3.2, outline=hexc('#555555'), width=1.2); l.line((93.3, 1114.3), (96, 1117), hexc('#555555'), 1.2)
    l.text(['How to get started...'], FR, 151, [1105], hexc('#3b3c3e'), left=117)
    L['G_card'] = l.done()
    for i, (lab, y0, y1, top) in enumerate([('PHOTOS', 868, 930, 888), ('VIDEOS', 968, 1032, 988), ('MAPS', 1070, 1134, 1090)]):
        l = Layer((466, y0, 692, y1))
        l.rrect((466, y0, 692, y1), 13, hexc('#0f376e'))
        cy = (y0 + y1) / 2; wc = (235, 240, 248, 255)
        if lab == 'PHOTOS':
            l.rrect((490, cy - 4, 500, cy + 4), 1, None, outline=wc, width=1); l.circle((493, cy - 1), 1, fill=wc)
        elif lab == 'VIDEOS':
            l.rrect((490, cy - 3.5, 497, cy + 3.5), 1, None, outline=wc, width=1); l.poly([(497, cy), (501, cy - 3), (501, cy + 3)], None)
            l.line((497.5, cy), (501, cy - 2.5), wc, 1); l.line((501, cy - 2.5), (501, cy + 2.5), wc, 1)
        else:
            l.circle((495, cy - 1.5), 3, outline=wc, width=1.1); l.line((495, cy + 1.5), (495, cy + 4.5), wc, 1.1)
        wv = font(FR, 80).getbbox(lab); wph = font(FR, 80).getbbox('PHOTOS')
        l.text([lab], FR, 90 * (wv[2] - wv[0]) / (wph[2] - wph[0]), [top], (240, 244, 250, 255), left=523)
        L[f'G_b{i+1}'] = l.done()
    # ---------- H: moldura do card do mapa (o miolo opaco vem do original, erodido 8 px) ----------
    l = Layer((112, 830, 608, 1198), pad=4)
    l.rrect((112, 830, 608, 1198), 2, hexc('#eeeeed'))
    L['H_frame'] = l.done()
    # ---------- I (n 1467-1613) ----------
    l = Layer((62, 838, 530, 887))
    l.rrect((62, 838, 304, 886), 24, hexc('#0b2f61'))
    l.circle((80, 859), 5, fill=hexc('#eff6fc'))
    l.text(['LIVE VERIFICATION'], FB, 143, [856], W, left=122)
    l.rrect((324, 838, 530, 887), 24, hexc(RED))
    l.circle((345, 859), 5, fill=hexc('#fd887d'))
    l.text(['LIMITED TIME'], FB, 99, [856], W, left=388)
    L['I_pills'] = l.done()
    l = Layer((40, 897, 639, 1068))
    l.rrect_alpha((54, 897, 639, 1029), 12, hexc('#e6e6e3', 245))
    l.rrect((118, 936, 597, 990), 0, hexc('#ebeceb'))
    l.text(['FREE CONSULTATION'], FB, 465, [947], hexc('#0c1f38'), left=125)
    l.rrect((54, 1062, 318, 1066), 0, hexc('#f03f36')); l.rrect((318, 1062, 638, 1066), 0, hexc('#0c305f'))
    L['I_card'] = l.done()
    # ---------- J (n 1620-1821) ----------
    l = Layer((58, 42, 212, 248))
    l.shadow((58, 42, 212, 248), 8, alpha=80, blur=5, dy=3)
    l.rrect((58, 42, 212, 248), 8, hexc(NAVY2))
    l.text(['DISCOVER', 'THE TRUTH', 'TODAY'], FB, 121, [125, 149, 173], hexc('#f1f3f6'), center=134.5)
    l.line((79, 46), (193, 69), hexc('#f2202a'), 4.5)
    L['J_top'] = l.done()
    l = Layer((40, 865, 521, 1010))
    l.shadow((40, 865, 521, 1010), 10, alpha=45, blur=5, dy=2)
    l.rrect((40, 865, 521, 1010), 10, hexc('#ebe8e5'))
    l.text(["DON'T SPEND ANOTHER DAY", 'BEING DECEIVED'], FB, 377, [911, 946], hexc('#0b2448'), center=280.5)
    L['J_card'] = l.done()
    l = Layer((258, 1024, 654, 1132))
    l.shadow((260, 1026, 652, 1130), 52, alpha=60, blur=5, dy=3)
    l.rrect((259, 1025, 653, 1131), 53, hexc('#fef2ee'))
    l.rrect((262, 1028, 650, 1128), 50, hexc('#ec180b'))
    l.text(['TAP BELOW'], FB, 156, [1069], W, center=456)
    L['J_btn'] = l.done()
    return L

# ---------------- animação (medida no original, work/tracks.json) ----------------
IN12 = [-424, -352, -282, -218, -162, -115, -76, -46, -25, -10, -2, 0]            # slide de entrada padrão (12 frames, ease-out)
OUT12 = [0, -3, -14, -32, -57, -92, -134, -183, -240, -303, -372, -445]         # saída padrão pela esquerda (ease-in)
TOP_IN = [-480, -442, -404, -368, -332, -296, -262, -232, -202, -174, -148, -124, -102, -82, -66, -52, -40, -28, -19, -13, -7, -3, -1, 0]
SRCH_IN = [-383, -317, -251, -191, -138, -95, -61, -35, -17, -6, -1, 0]
I_OUT = [0, -4, -13, -29, -49, -77, -109, -148, -193, -242, -297, -356, -419, -483, -548, -620]
J_CARD_IN = [-550, -507, -463, -420, -378, -336, -296, -258, -221, -187, -157, -129, -103, -81, -62, -46, -33, -22, -14, -7, -3, -1, 0]
J_BTN_IN = [-625, -593, -562, -534, -510, -487, -463, -440, -416, -392, -370, -346, -324, -302, -281, -260, -239, -219, -201, -183, -165, -149,
            -134, -120, -107, -93, -81, -71, -61, -52, -43, -36, -29, -23, -19, -14, -10, -7, -5, -3, -1, 0]
J_OUT = [0, -2, -15, -41, -83, -139, -209, -293, -388, -488, -590, -700]
JT_OUT = [0, -3, -21, -54, -106, -175, -260]

def seq(n, s, e, ins=None, i0=None, outs=None, o0=None):
    """(visível, dx) com entrada ins a partir de i0 e saída outs a partir de o0; visível em [s,e]."""
    if n < s or n > e: return None
    if ins is not None and i0 <= n < i0 + len(ins): return ins[n - i0]
    if outs is not None and o0 <= n:
        k = n - o0
        return outs[k] if k < len(outs) else None
    return 0

ANIM = {
    'A_pill': lambda n: -210 if n == 178 else seq(n, 4, 177, IN12, 4),     # n178: começa a sair (medido), some no flash
    'A_navy': lambda n: -210 if n == 178 else seq(n, 4, 177, IN12, 4),
    'A_card': lambda n: seq(n, 0, 178),
    'C_navy': lambda n: seq(n, 236, 401, IN12, 236, OUT12, 390),
    'C_pill': lambda n: seq(n, 236, 401, IN12, 236, OUT12, 390),
    'D': lambda n: seq(n, 409, 693, IN12, 409, OUT12, 682),
    'E': lambda n: seq(n, 701, 1059, IN12, 701),                # até 1059 some no branco do flash (vai por baixo dele)
    'G_top': lambda n: seq(n, 1246, 1459, TOP_IN, 1246, OUT12, 1448),
    'G_card': lambda n: seq(n, 1244, 1358, SRCH_IN, 1244, OUT12, 1348),
    'G_b1': lambda n: seq(n, 1239, 1358, None, None, OUT12, 1348),
    'G_b2': lambda n: seq(n, 1239, 1358, None, None, OUT12, 1348),
    'G_b3': lambda n: seq(n, 1239, 1358, None, None, OUT12, 1348),
    'I_pills': lambda n: seq(n, 1467, 1613, IN12, 1467, I_OUT, 1599),
    'I_card': lambda n: seq(n, 1467, 1613, IN12, 1467, I_OUT, 1599),
    'J_top': lambda n: seq(n, 1620, 1817, IN12, 1620, JT_OUT, 1811),
    'J_card': lambda n: seq(n, 1620, 1821, J_CARD_IN, 1620, J_OUT, 1810),
    'J_btn': lambda n: seq(n, 1621, 1821, J_BTN_IN, 1621, J_OUT, 1810),
}
ORDER = ['A_card', 'A_navy', 'A_pill', 'C_navy', 'C_pill', 'D', 'E', 'G_card', 'G_b1', 'G_b2', 'G_b3', 'G_top',
         'I_card', 'I_pills', 'J_card', 'J_btn', 'J_top']

def extra(name, n):
    """Botões G: entram no lugar com borrão vertical que some (medido: bbox 8-10 px maior em cima/baixo em n1244, 0 em ~1262)."""
    if name.startswith('G_b') and 1239 <= n < 1262:
        k = (1262 - n) / 23.0
        return {'vblur': 18 * k, 'dy': -3 * k}
    if name.startswith('G_b') and 1262 <= n < 1279:
        return {'dy': -2 * (1279 - n) / 17.0}
    return {}

def _hblur(a, L):
    if L < 1.0: return a
    k = int(round(L)); c = np.cumsum(np.pad(a, ((0, 0), (k, k), (0, 0))), axis=1)
    return (c[:, 2 * k:] - c[:, :-2 * k])[:, :a.shape[1]] / (2 * k) if k > 0 else a

def _vblur(a, L):
    if L < 1.0: return a
    return _hblur(a.transpose(1, 0, 2), L).transpose(1, 0, 2)

class Compositor:
    def __init__(self):
        self.L = build(); self.prev = {}
    def apply(self, frame, n, only=None, skip=()):
        """frame: float32 HxWx3 (0-1). Compõe os cards visíveis no frame n."""
        H, Wd = frame.shape[:2]
        for name in ORDER:
            if (only and name not in only) or name in skip: continue
            dx = ANIM[name](n)
            if dx is None: continue
            x0, y0, a = self.L[name]
            ex = extra(name, n); dy = ex.get('dy', 0)
            pdx = ANIM[name](n - 1); v = abs(dx - pdx) if pdx is not None else 0
            # sem borrão de movimento: no original os slides são nítidos (n12, n395)
            if ex.get('vblur'): a = _vblur(a, ex['vblur'])
            X = x0 + int(round(dx)); Y = y0 + int(round(dy))
            ax0, ay0 = max(0, -X), max(0, -Y); ax1 = min(a.shape[1], Wd - X); ay1 = min(a.shape[0], H - Y)
            if ax1 <= ax0 or ay1 <= ay0: continue
            sub = a[ay0:ay1, ax0:ax1]; fx, fy = X + ax0, Y + ay0
            reg = frame[fy:fy + sub.shape[0], fx:fx + sub.shape[1]]
            reg *= (1 - sub[..., 3:4]); reg += sub[..., :3]
        return frame
