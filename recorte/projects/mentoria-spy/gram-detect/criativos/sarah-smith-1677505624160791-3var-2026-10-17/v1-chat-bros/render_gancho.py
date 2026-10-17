"""Gancho V1: conversa estilo iMessage (modo escuro), 720x1280, 30 fps.
Gera frames 0..139 em work/chat/ (PNG) a 2x e reduz. Uso: python3 render_gancho.py
"""
import math, os
from PIL import Image, ImageDraw, ImageFont

S = 2                      # supersample
W, H = 720 * S, 1280 * S
OUT = os.path.join(os.path.dirname(__file__), "work", "chat")
os.makedirs(OUT, exist_ok=True)
N = 140                    # frames 0..139 (o push-wipe começa no f140)

SF = "/System/Library/Fonts/SFNS.ttf"
EMO = "/System/Library/Fonts/Apple Color Emoji.ttc"

def sf(size, weight="Regular"):
    f = ImageFont.truetype(SF, size * S)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f

F_MSG = sf(42)
F_NAME = sf(24)
F_SMALL = sf(20, "Semibold")
F_STAMP = sf(20)
F_POV = sf(32)
F_TIME = sf(28, "Semibold")
EMOJI_FONT = ImageFont.truetype(EMO, 160)
_emoji_cache = {}

BG = (0, 0, 0)
GRAY = (38, 38, 41)
BLUE = (10, 132, 255)
WHITE = (255, 255, 255)
SUB = (142, 142, 147)

def is_emoji(ch):
    return ord(ch) >= 0x1F000

def emoji_img(ch, px):
    k = (ch, px)
    if k not in _emoji_cache:
        im = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((0, 0), ch, font=EMOJI_FONT, embedded_color=True)
        bb = im.getbbox()
        im = im.crop(bb)
        r = px / im.height
        _emoji_cache[k] = im.resize((max(1, round(im.width * r)), px), Image.LANCZOS)
    return _emoji_cache[k]

def seg_width(text, font):
    w = 0
    for ch in text:
        if is_emoji(ch):
            w += int(font.size * 1.05) + 2
        else:
            w += font.getlength(ch)
    return w

def text_w(text, font):
    # medir trechos sem emoji de uma vez (kerning)
    w, buf = 0, ""
    for ch in text:
        if is_emoji(ch):
            w += font.getlength(buf); buf = ""
            w += int(font.size * 1.05) + 2
        else:
            buf += ch
    return w + font.getlength(buf)

def draw_rich(img, xy, text, font, fill):
    d = ImageDraw.Draw(img)
    x, y = xy
    buf = ""
    asc = font.getmetrics()[0]
    for ch in text + "\0":
        if ch == "\0" or is_emoji(ch):
            if buf:
                d.text((x, y), buf, font=font, fill=fill)
                x += font.getlength(buf); buf = ""
            if ch != "\0":
                px = int(font.size * 1.05)
                e = emoji_img(ch, px)
                img.alpha_composite(e, (int(x + 1), int(y + asc - px * 0.86)))
                x += px + 2
        else:
            buf += ch

def wrap(text, font, maxw):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if text_w(t, font) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    return lines

PADX, PADY, LH = 30 * S, 16 * S, 52 * S
MAXW = 560 * S

def bubble_sprite(text, color, tail_right, tail=True):
    lines = wrap(text, F_MSG, MAXW - 2 * PADX)
    tw = max(text_w(l, F_MSG) for l in lines)
    bw, bh = int(tw + 2 * PADX), int(len(lines) * LH + 2 * PADY)
    m = 14 * S
    im = Image.new("RGBA", (bw + 2 * m, bh + m), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    r = min(36 * S, bh // 2)
    d.rounded_rectangle((m, 0, m + bw, bh), r, fill=color)
    if tail:
        # cauda estilo iOS: polígono por duas curvas de Bézier
        def bez(p0, p1, p2, n=24):
            return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0], (1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1]) for t in [i/n for i in range(n+1)]]
        e = m + bw  # borda direita
        pts = bez((e - 2*S, bh - 34*S), (e - 1*S, bh - 4*S), (e + 12*S, bh)) + \
              bez((e + 12*S, bh), (e - 8*S, bh + 1*S), (e - 30*S, bh - 6*S))
        pts += [(e - 34*S, bh - 30*S)]
        if not tail_right:
            cx2 = m + bw / 2
            pts = [(2*cx2 - x, y) for x, y in pts]
        d.polygon(pts, fill=color)
    yy = PADY + 3 * S
    for l in lines:
        draw_rich(im, (m + PADX, yy), l, F_MSG, WHITE)
        yy += LH
    return im, m

def typing_sprite(t):
    bw, bh = 120 * S, 76 * S
    m = 14 * S
    im = Image.new("RGBA", (bw + 2 * m, bh + m), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((m, 0, m + bw, bh), bh // 2, fill=GRAY)
    d.ellipse((m - 10 * S, bh - 18 * S, m + 8 * S, bh), fill=GRAY)
    d.ellipse((m - 22 * S, bh + 0 * S, m - 12 * S, bh + 10 * S), fill=GRAY)
    for i in range(3):
        ph = (t * 0.32 - i * 0.9)
        a = 0.45 + 0.55 * max(0, math.sin(ph))
        c = tuple(int(90 + (160 - 90) * a) for _ in range(3))
        cx = m + 34 * S + i * 26 * S
        d.ellipse((cx - 8 * S, bh // 2 - 8 * S, cx + 8 * S, bh // 2 + 8 * S), fill=c)
    return im, m

def ease_back(p):
    p = max(0.0, min(1.0, p))
    c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (p - 1) ** 3 + c1 * (p - 1) ** 2

def ease_out(p):
    p = max(0.0, min(1.0, p)); return 1 - (1 - p) ** 3

# roteiro: (frame_entrada, quem, texto)  quem: "him" (cinza, esquerda) / "me" (azul, direita)
MSGS = [
    (8,   "him", "bro how do I see who my girl is talking to on insta without her knowing??"),
    (48,  "me",  "copy her @"),
    (64,  "me",  "put it on Gram Detect"),
    (114, "him", "wait that works?? 😳"),
]
TYPING = [(0, 8, "him"), (92, 114, "him")]   # (ini, fim, quem)

SPR = []
for i, (f, who, txt) in enumerate(MSGS):
    nxt_same = i + 1 < len(MSGS) and MSGS[i + 1][1] == who
    SPR.append(bubble_sprite(txt, GRAY if who == "him" else BLUE, who == "me", tail=not nxt_same))

TOP0 = 400 * S          # topo da pilha de bolhas
GAP_SAME, GAP_OTHER = 8 * S, 28 * S

def header(img):
    d = ImageDraw.Draw(img)
    # barra de status genérica
    d.text((62 * S, 22 * S), "9:41", font=F_TIME, fill=WHITE)
    for i in range(4):
        h = (8 + i * 5) * S
        d.rounded_rectangle((566 * S + i * 11 * S, 46 * S - h, 574 * S + i * 11 * S, 46 * S), 2 * S, fill=WHITE)
    d.rounded_rectangle((622 * S, 24 * S, 668 * S, 46 * S), 6 * S, outline=WHITE, width=2 * S)
    d.rounded_rectangle((626 * S, 28 * S, 656 * S, 42 * S), 3 * S, fill=WHITE)
    d.rounded_rectangle((670 * S, 31 * S, 674 * S, 39 * S), 1 * S, fill=WHITE)
    # fundo do cabeçalho
    d.rectangle((0, 70 * S, W, 236 * S), fill=(22, 22, 24))
    d.line((0, 236 * S, W, 236 * S), fill=(48, 48, 52), width=S)
    # voltar
    d.line((40 * S, 132 * S, 24 * S, 150 * S), fill=BLUE, width=5 * S)
    d.line((24 * S, 150 * S, 40 * S, 168 * S), fill=BLUE, width=5 * S)
    d.text((50 * S, 132 * S), "12", font=sf(30), fill=BLUE)
    # avatar
    cx, cy, r = 360 * S, 130 * S, 44 * S
    av = Image.new("RGBA", (2 * r, 2 * r), (0, 0, 0, 0))
    ad = ImageDraw.Draw(av)
    for yy in range(2 * r):
        k = yy / (2 * r)
        c = (int(160 - 50 * k), int(164 - 50 * k), int(176 - 50 * k), 255)
        ad.line((0, yy, 2 * r, yy), fill=c)
    mask = Image.new("L", (2 * r, 2 * r), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, 2 * r - 1, 2 * r - 1), fill=255)
    av.putalpha(mask)
    f = sf(42, "Semibold")
    tw = f.getlength("M")
    ImageDraw.Draw(av).text((r - tw / 2, r - 28 * S), "M", font=f, fill=WHITE)
    img.alpha_composite(av, (cx - r, cy - r))
    name = "Mike 🏈"
    nw = text_w(name, F_NAME)
    draw_rich(img, (cx - nw / 2 - 6 * S, 184 * S), name, F_NAME, WHITE)
    x = cx + nw / 2 + 2 * S
    d.line((x, 192 * S, x + 6 * S, 198 * S), fill=SUB, width=2 * S)
    d.line((x + 6 * S, 198 * S, x, 204 * S), fill=SUB, width=2 * S)
    # rodapé: campo de mensagem
    d.rounded_rectangle((96 * S, 1172 * S, 690 * S, 1226 * S), 27 * S, outline=(58, 58, 62), width=2 * S)
    d.text((120 * S, 1184 * S), "Message", font=sf(26), fill=(99, 99, 104))
    d.ellipse((24 * S, 1176 * S, 70 * S, 1222 * S), fill=(44, 44, 46))
    d.line((47 * S, 1188 * S, 47 * S, 1210 * S), fill=(160, 160, 165), width=3 * S)
    d.line((36 * S, 1199 * S, 58 * S, 1199 * S), fill=(160, 160, 165), width=3 * S)
    d.rounded_rectangle((250 * S, 1258 * S, 470 * S, 1266 * S), 4 * S, fill=WHITE)

def overlays(img):
    d = ImageDraw.Draw(img)
    pov = "pov: men talk about women"
    tw = F_POV.getlength(pov)
    d.text(((W - tw) / 2, 282 * S), pov, font=F_POV, fill=(255, 255, 255))
    st = "Today 9:41 PM"
    tw = F_STAMP.getlength(st)
    d.text(((W - tw) / 2, 350 * S), st, font=F_STAMP, fill=SUB)

def frame(t):
    img = Image.new("RGBA", (W, H), BG + (255,))
    header(img)
    overlays(img)
    y = TOP0
    prev = None
    for i, (f0, who, txt) in enumerate(MSGS):
        sp, m = SPR[i]
        gap = 0 if prev is None else (GAP_SAME if prev == who else GAP_OTHER)
        # typing indicator ocupando o lugar antes da bolha
        typ = [tp for tp in TYPING if tp[2] == who and tp[1] == f0]
        if t < f0:
            if typ and typ[0][0] <= t:
                ts, tm = typing_sprite(t)
                p = ease_back((t - typ[0][0]) / 5)
                yy = y + gap
                s = max(0.01, p)
                ts2 = ts.resize((max(1, int(ts.width * s)), max(1, int(ts.height * s))), Image.LANCZOS)
                img.alpha_composite(ts2, (int(24 * S - tm + tm * (1 - s)), int(yy + ts.height - ts2.height)))
            break
        p = (t - f0) / 6
        y += gap
        if who == "him":
            s = 0.55 + 0.45 * ease_back(p)
            sp2 = sp.resize((max(1, int(sp.width * s)), max(1, int(sp.height * s))), Image.LANCZOS)
            x = 24 * S - m
            img.alpha_composite(sp2, (int(x), int(y + sp.height - sp2.height)))
        else:
            # enviada: sobe de baixo e assenta
            off = (1 - ease_out(p)) * 120 * S
            a = ease_out(min(1, p * 1.6))
            sp2 = sp.copy()
            if a < 1:
                al = sp2.getchannel("A").point(lambda v: int(v * a))
                sp2.putalpha(al)
            x = W - 24 * S - sp.width + m
            img.alpha_composite(sp2, (int(x), int(y + off)))
        y += sp.height - m
        prev = who
    return img.convert("RGB").resize((720, 1280), Image.LANCZOS)

if __name__ == "__main__":
    for t in range(N):
        frame(t).save(os.path.join(OUT, f"c{t:04d}.png"))
    print("ok", N)
