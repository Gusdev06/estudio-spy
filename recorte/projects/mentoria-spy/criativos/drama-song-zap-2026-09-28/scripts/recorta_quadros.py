# Recorta os 4 quadros de um shot sheet 2x2 (acha as calhas brancas pela média de brilho), inset 6 px, escala 720x1280.
# uso: python3 recorta_quadros.py B01 [B02 ...]  -> quadros-v2/B01-q1.png .. q4.png
import sys, pathlib, numpy as np
from PIL import Image
L = pathlib.Path(__file__).resolve().parent.parent
out = L / "quadros-v2"; out.mkdir(exist_ok=True)
def gutter(prof, n):
    mid = n // 2; win = range(int(n * 0.4), int(n * 0.6))
    hi = [i for i in win if prof[i] > 200]
    if not hi:  # sem calha branca: usa o meio
        return mid - 2, mid + 2
    # maior sequência contígua mais perto do meio
    runs, cur = [], [hi[0]]
    for i in hi[1:]:
        if i == cur[-1] + 1: cur.append(i)
        else: runs.append(cur); cur = [i]
    runs.append(cur)
    r = min(runs, key=lambda r: abs((r[0] + r[-1]) / 2 - mid))
    return r[0], r[-1]
for k in sys.argv[1:]:
    im = Image.open(L / f"shot-sheets-v2/{k}.png").convert("RGB"); a = np.asarray(im.convert("L")).astype(float)
    H, W = a.shape
    c0, c1 = gutter(a.mean(0), W); r0, r1 = gutter(a.mean(1), H)
    I = 6
    boxes = [(I, I, c0 - I, r0 - I), (c1 + 1 + I, I, W - I, r0 - I), (I, r1 + 1 + I, c0 - I, H - I), (c1 + 1 + I, r1 + 1 + I, W - I, H - I)]
    for q, b in enumerate(boxes, 1):
        im.crop(b).resize((720, 1280), Image.LANCZOS).save(out / f"{k}-q{q}.png")
    print(k, W, H, "calhas col", (c0, c1), "lin", (r0, r1))
