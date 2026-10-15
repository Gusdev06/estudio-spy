#!/usr/bin/env python3
# Monta a variação (caminho B, 25/09): avatar/cenário novos (4 clipes Pruna, áudio original) + cards REDESENHADOS (cards.py) +
# painel "Accessing WhatsApp" redesenhado (fundo, degradê e deslocamento do vídeo) com o conteúdo de tela do original só no miolo opaco +
# moldura do card do mapa redesenhada com o miolo opaco do original erodido 8 px + flashes refeitos como filtro (flash.py).
# Tudo em streaming (1 frame por vez) direto pro ffmpeg. Uso (da pasta da peça): python3 montar.py pecas/variacao.mp4
import subprocess, sys, json, numpy as np, cv2
from cards import Compositor
import flash
OUT = sys.argv[1] if len(sys.argv) > 1 else 'pecas/variacao.mp4'
LIM = int(sys.argv[2]) if len(sys.argv) > 2 else 1822          # pra testes: só os primeiros N frames
REF = 'REFERENCIA-original.mp4'; N = 1822; W, H = 720, 1280
CLIPS = [('clipes/c1.mp4', 0, 403), ('clipes/c2.mp4', 404, 1059), ('clipes/c3.mp4', 1060, 1462), ('clipes/c4.mp4', 1463, 1821)]
# emendas por NÚMERO DE FRAME, todas dentro de flash do original (n 404 no F3, 1060 no pico branco do F4, 1463 no F7)
S = W / 704.0; SW, SH = W, int(round(1280 * S))                # 720x1309: cobre o quadro; rosto no alto (y0 = 0)
PANEL = (1060, 1239); SHIFT = 215                              # vídeo sobe 215 px (medido na luminária: -215 de n1061 a n1231)
PC = np.array([224, 224, 226], np.float32)                     # cor do painel (mediana do miolo liso)
PY0, PY1 = 714, 758                                            # degradê vídeo -> painel (medido: alfa 0 -> 1)
PIN = 772                                                      # conteúdo do original só de y >= 772 (14 px abaixo do fim do degradê)
PCLEAN = (1066, 1233)                                          # frames do painel sem flash (fonte do conteúdo)
MAP = (1364, 1462)                                             # o mapa fica por BAIXO do flash na entrada e na saída (sai tingido, como no original)
MCLEAN = (1367, 1458); MIN = (120, 838, 600, 1190)   # card do mapa (112,830)-(608,1198) erodido 8 px
G = np.load('work/G.npy', mmap_mode='r')
FP = json.load(open('work/flash-params.json'))
comp = Compositor()

yy = np.arange(H, dtype=np.float32)[:, None, None]
t = np.clip((yy - PY0) / (PY1 - PY0), 0, 1); PALPHA = (t * t * (3 - 2 * t))   # smoothstep

def clip_reader(path):
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', path, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    k = -1; cur = None
    def get(idx):
        nonlocal k, cur
        while k < idx:
            b = p.stdout.read(704 * 1280 * 3)
            if len(b) < 704 * 1280 * 3: return cur          # fim do clipe: congela o último
            cur = np.frombuffer(b, np.uint8).reshape(1280, 704, 3); k += 1
        return cur
    return get

enc = subprocess.Popen(['ffmpeg', '-hide_banner', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30',
                        '-i', '-', '-i', REF, '-map', '0:v', '-map', '1:a', '-c:a', 'copy', '-c:v', 'libx264', '-preset', 'slow', '-crf', '16',
                        '-pix_fmt', 'yuv420p', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv',
                        '-movflags', '+faststart', OUT], stdin=subprocess.PIPE)
readers = {}
for n in range(min(N, LIM)):
    path, a, b = next(c for c in CLIPS if c[1] <= n <= c[2])
    if path not in readers: readers = {path: clip_reader(path)}
    src = readers[path](int(round((n - a) / 30.0 * 24.0)))
    big = cv2.resize(src, (SW, SH), interpolation=cv2.INTER_LANCZOS4)
    shift = SHIFT if PANEL[0] <= n <= PANEL[1] else 0
    f = big[shift:shift + H].astype(np.float32)
    if f.shape[0] < H: f = np.pad(f, ((0, H - f.shape[0]), (0, 0), (0, 0)), mode='edge')   # abaixo de y 758 o painel é opaco
    if shift:
        f = f * (1 - PALPHA) + PC * PALPHA
        m = min(max(n, PCLEAN[0]), PCLEAN[1]); o = G[m, PIN:].astype(np.float32)
        mk = (np.abs(o - PC).max(2) > 8).astype(np.uint8)
        mk = cv2.dilate(mk, np.ones((9, 9), np.uint8)).astype(np.float32)
        mk = cv2.GaussianBlur(mk, (0, 0), 1.5)[..., None]
        f[PIN:] = f[PIN:] * (1 - mk) + o * mk
    # ordem medida: flash tinge o vídeo e o painel (camada de vídeo); os cards ficam POR CIMA do flash (k=0 medido nos cards A e G),
    # exceto o card E na saída n1056-1059 (k=1 medido), que vai por baixo.
    def draw_map(img):
        x0, y0, a_ = comp.L['H_frame']
        reg = img[y0:y0 + a_.shape[0], x0:x0 + a_.shape[1]]; reg *= (1 - a_[..., 3:4]); reg += a_[..., :3] * 255.0
        m = min(max(n, MCLEAN[0]), MCLEAN[1]); X0, Y0, X1, Y1 = MIN
        img[Y0:Y1, X0:X1] = G[m, Y0:Y1, X0:X1]
    inmap = MAP[0] <= n <= MAP[1]
    if n in (1056, 1057, 1058, 1059): f = comp.apply(f / 255.0, n, only=['E']) * 255.0
    if inmap: draw_map(f)
    if str(n) in FP: f = flash.apply(f, FP[str(n)])
    fr = comp.apply(f / 255.0, n, skip=(['E'] if n in (1056, 1057, 1058, 1059) else [])) * 255.0
    enc.stdin.write(np.clip(fr + 0.5, 0, 255).astype(np.uint8).tobytes())
    if n % 200 == 0: print('frame', n, flush=True)
enc.stdin.close(); enc.wait(); print('ok ->', OUT)
