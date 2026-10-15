# Folha de conferência original (em cima) x peça (embaixo) em instantes-chave. Uso: python3 conferir.py <peca.mp4> <saida.jpg> n1 n2 ...
import subprocess, sys, numpy as np, cv2
P, OUT = sys.argv[1], sys.argv[2]; NS = [int(x) for x in sys.argv[3:]]
def frames(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-vf', "select='" + '+'.join(f'eq(n\\,{n})' for n in NS) + "'", '-vsync', '0',
                          '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, 1280, 720, 3)
A, B = frames('REFERENCIA-original.mp4'), frames(P); w = 200; h = int(1280 * w / 720); cols = []
for n, a, b in zip(NS, A, B):
    a = cv2.resize(a, (w, h), interpolation=cv2.INTER_AREA); b = cv2.resize(b, (w, h), interpolation=cv2.INTER_AREA)
    for im in (a, b): cv2.putText(im, f'n{n}', (4, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 2)
    cols.append(np.vstack([a, np.full((4, w, 3), 255, np.uint8), b]))
cv2.imwrite(OUT, np.hstack(cols), [cv2.IMWRITE_JPEG_QUALITY, 88])
