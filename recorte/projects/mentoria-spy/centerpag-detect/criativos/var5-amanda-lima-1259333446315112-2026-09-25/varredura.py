# Varredura final: sobra pixel da mulher original? Compara peça x original frame a frame.
# (1) na caixa do rosto original (YuNet, medida.tsv, expandida) -> fração de pixels quase iguais (|dif| < 10 nos 3 canais);
# (2) no quadro inteiro, fora dos cards redesenhados e dos miolos permitidos (painel y>=772 em 1060-1239, mapa em 1364-1460).
import subprocess, numpy as np, json, sys
from cards import Compositor
import flash
P = sys.argv[1] if len(sys.argv) > 1 else 'pecas/variacao.mp4'
FP = json.load(open('work/flash-params.json')); comp = Compositor()
G = np.load('work/G.npy', mmap_mode='r')
med = {int(l.split('\t')[0]): l.split('\t') for l in open('work/medida.tsv')}
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', P, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
res = []
for n in range(1822):
    b = p.stdout.read(1280 * 720 * 3); x = np.frombuffer(b, np.uint8).reshape(1280, 720, 3).astype(np.int16); o = G[n].astype(np.int16)
    same = (np.abs(x - o).max(2) < 10)
    cm = flash.cardmask(comp, n)
    if 1060 <= n <= 1239: cm[772:] = True
    if 1364 <= n <= 1460: cm[826:1202, 108:612] = True
    white = o.min(2) > 225                                   # pico branco do flash: igual por saturação, não por conteúdo
    free = ~cm & ~white
    fr_all = same[free].mean() if free.any() else 0
    m = med[n]; fr_face = np.nan
    if m[6] != '-':
        cx, cy, h = float(m[6]), float(m[7]), float(m[8]); x0, x1 = int(max(cx - h * .8, 0)), int(min(cx + h * .8, 720)); y0, y1 = int(max(cy - h * .9, 0)), int(min(cy + h * .9, 1280))
        f = free[y0:y1, x0:x1]; fr_face = same[y0:y1, x0:x1][f].mean() if f.sum() > 500 else np.nan
    res.append((n, fr_all, fr_face, str(n) in FP))
r = np.array([(a, b, c) for a, b, c, _ in res], float)
print('quadro inteiro (fora de cards/miolos): fração |dif|<10  média %.4f  máx %.4f em n%d' % (np.nanmean(r[:, 1]), np.nanmax(r[:, 1]), r[np.nanargmax(r[:, 1]), 0]))
print('caixa do rosto original:                fração |dif|<10  média %.4f  máx %.4f em n%d' % (np.nanmean(r[:, 2]), np.nanmax(r[:, 2]), r[np.nanargmax(r[:, 2]), 0]))
top = r[np.argsort(-np.nan_to_num(r[:, 2]))[:8]]; print('piores frames (rosto):', ', '.join('n%d %.3f' % (a, c) for a, b, c in top))
np.savetxt('work/varredura.tsv', r, fmt='%.4f', delimiter='\t')
