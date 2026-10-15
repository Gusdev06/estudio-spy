# Flashes/gradações laranja do original refeitos como FILTRO (25/09). Para cada frame tingido n, estima contra o frame limpo vizinho P
# (antes ou depois, o que ajustar melhor): out_c = a_c(n) * P_c + B_c(n; x, y), com ganho global por canal (fit nas regiões de fundo, sem a
# mulher) e um campo aditivo suave (células 80 px, suavizado) que carrega o vazamento de luz. O filtro é reaplicado sobre o quadro NOVO.
import numpy as np, cv2, json
WIN = [(174, 182), (228, 235), (399, 406), (1056, 1065), (1234, 1243), (1358, 1366), (1459, 1466)]
CELL = 80
def cellmean(x, w=None):  # 1280x720xC -> 16x9xC, média ponderada; células sem peso herdam das vizinhas
    if w is None: return x.reshape(16, CELL, 9, CELL, -1).mean((1, 3))
    s = (x * w[..., None]).reshape(16, CELL, 9, CELL, -1).sum((1, 3)); c = w.reshape(16, CELL, 9, CELL).sum((1, 3))[..., None]
    for sg in (0.0, 0.8, 1.6, 3.0):
        if sg: s2, c2 = cv2.GaussianBlur(s, (0, 0), sg), cv2.GaussianBlur(c, (0, 0), sg)[..., None]
        else: s2, c2 = s, c
        if sg == 0: m = s2 / np.maximum(c2, 1e-6); ok = (c2 > CELL * CELL * 0.15)
        else: m = np.where(ok, m, s2 / np.maximum(c2, 1e-6)); ok = ok | (c2 > 1)
    return m
def cardmask(comp, n):
    """pixels cobertos por card (redesenho) no frame n -> fora do ajuste: no original os cards ficam POR CIMA do flash."""
    f = np.zeros((1280, 720, 3), np.float32); comp.apply(f, n); a = np.zeros((1280, 720, 3), np.float32) + 1
    comp.apply(a, n); m = (np.abs(a - 1).max(2) + f.max(2)) > 0.02
    if 1362 <= n <= 1461: m[826:1202, 108:612] = True       # card do mapa
    return cv2.dilate(m.astype(np.uint8), np.ones((15, 15), np.uint8)) > 0
def fit(G):
    from cards import Compositor
    comp = Compositor(); out = {}
    bg0 = np.zeros((1280, 720), bool); bg0[:430] = True; bg0[:, :110] = True; bg0[:, 630:] = True
    for a, b in WIN:
        pre, post = G[a - 1].astype(np.float32), G[b + 1].astype(np.float32)
        for n in range(a, b + 1):
            o = G[n].astype(np.float32); best = None
            cands = ((pre, a - 1), (post, b + 1))
            # nas trocas de camada de vídeo (painel entra em 1060, sai em 1240) o proxy tem de ser do MESMO lado da troca
            if a == 1056: cands = cands[:1] if n < 1060 else cands[1:]
            if a == 1234: cands = cands[:1] if n < 1240 else cands[1:]
            for P, tag in cands:
                w = ~(cardmask(comp, n) | cardmask(comp, tag)); bgmask = bg0 & w
                Pm, Om = cellmean(P, w.astype(np.float32)), cellmean(o, w.astype(np.float32))
                dP = P - cv2.resize(Pm, (720, 1280), interpolation=cv2.INTER_LINEAR)
                dO = o - cv2.resize(Om, (720, 1280), interpolation=cv2.INTER_LINEAR)
                g = []
                for c in range(3):
                    x, y = dP[..., c][bgmask], dO[..., c][bgmask]
                    g.append(float(np.clip((x * y).sum() / ((x * x).sum() + 1e-3), 0.0, 1.6)))
                g = np.array(g, np.float32)
                # ganho por célula, puxado pro ganho global (ridge): célula com textura estável (ex.: conteúdo do painel) mantém o
                # contraste que o original mantém; célula onde a pessoa se mexe fica com o ganho global.
                wf = w.astype(np.float32)
                cov = cellmean(dP * dO, wf); var = cellmean(dP * dP, wf); LAM = 150.0
                A = np.clip((cov + LAM * g) / (var + LAM), 0, 1.6)
                A = cv2.GaussianBlur(A, (0, 0), 0.8)
                B = Om - A * Pm
                B = cv2.GaussianBlur(B, (0, 0), 0.8)
                pred = P * cv2.resize(A, (720, 1280), interpolation=cv2.INTER_CUBIC) + cv2.resize(B, (720, 1280), interpolation=cv2.INTER_CUBIC)
                err = float(np.abs(np.clip(pred, 0, 255) - o)[bgmask].mean())
                if best is None or err < best[0]: best = (err, tag, A.tolist(), B.tolist())
            out[n] = {'err': best[0], 'proxy': best[1], 'g': best[2], 'B': best[3]}
    return out
def apply(frame255, prm):
    """frame255: float32 1280x720x3 (0-255) -> tingido."""
    B = cv2.resize(np.array(prm['B'], np.float32), (720, 1280), interpolation=cv2.INTER_CUBIC)
    A = cv2.resize(np.array(prm['g'], np.float32), (720, 1280), interpolation=cv2.INTER_CUBIC)
    return np.clip(frame255 * A + B, 0, 255)
if __name__ == '__main__':
    G = np.load('work/G.npy', mmap_mode='r'); P = fit(G)
    json.dump(P, open('work/flash-params.json', 'w'))
    for n, p in P.items(): print(n, 'proxy', p['proxy'], 'err %.1f' % p['err'], 'ganho médio', np.array(p['g']).mean((0, 1)).round(2).tolist())
