#!/usr/bin/env python3
# Conferência das peças 172/173: decodifica inteiro, dimensões/fps, silêncios >= 0,5 s (-hide_banner), rostos por frame (YuNet >= 0,86),
# sobra do original (bordas da janela/título/karaokê correlacionadas com o original), painéis = original, karaokê casando com a fala.
# Uso (desta pasta): python3 conferir.py p172=pecas/172-....mp4 p173=pecas/173-....mp4
import json, os, re, subprocess, sys, numpy as np, cv2
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M = '../../../gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'; W, H = 360, 640
def ler(a):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', a, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
O = ler('REFERENCIA-flora-original.mp4')
def bordas(x):
    g = cv2.cvtColor(np.ascontiguousarray(x), cv2.COLOR_BGR2GRAY).astype(np.float32); m = cv2.magnitude(cv2.Sobel(g, cv2.CV_32F, 1, 0), cv2.Sobel(g, cv2.CV_32F, 0, 1)); m -= m.mean(); return m/(np.linalg.norm(m)+1e-6)
def lab(x, t):
    x = x.copy(); cv2.putText(x, t, (6, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 2); return x
linhas = []
for arg in sys.argv[1:]:
    P, PEC = arg.split('='); T = json.load(open(f'{P}/molde/timeline.json')); BL = T['blocos']
    err = subprocess.run(['ffmpeg', '-v', 'error', '-i', PEC, '-f', 'null', '-'], capture_output=True, text=True).stderr.strip()
    info = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=width,height,r_frame_rate,nb_frames', '-of', 'csv=p=0', PEC], capture_output=True, text=True).stdout.strip()
    sil = subprocess.run(['ffmpeg', '-hide_banner', '-i', PEC, '-af', 'silencedetect=n=-35dB:d=0.5', '-f', 'null', '-'], capture_output=True, text=True).stderr
    nsil = len(re.findall('silence_start', sil)); dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', PEC], capture_output=True, text=True).stdout)
    V = ler(PEC); N = len(V)
    det = cv2.FaceDetectorYN_create(M, '', (W, H), 0.86, 0.3, 5000); nf = []
    for x in V:
        d = det.detect(np.ascontiguousarray(x))[1]; nf.append(0 if d is None else len(d))
    nf = np.array(nf)
    rosto = [n for b, d in BL.items() if b != 'paineis' for n in range(d['f0'], d['f1']+1)]
    pain = range(BL['paineis']['f0'], BL['paineis']['f1']+1)
    # sobra da dupla original: correlação de bordas da janela com TODOS os frames da dupla no original (pior caso)
    Od = [n for n in list(range(0, 263))+list(range(885, 1026))]
    Ob = np.array([bordas(O[n, 168:471]) for n in Od[::6]])
    cor_j = max(float((Ob*bordas(V[n, 168:471])).sum((1, 2)).max()) for n in rosto[::5])
    # título e karaokê antigos: bordas da faixa vs a mesma faixa do original (qualquer frame)
    Ot = bordas(O[100, 0:160]); cor_t = max(float((Ot*bordas(V[n, 0:160])).sum()) for n in range(0, N, 10))
    Ok = np.array([bordas(O[n, 505:590]) for n in range(0, 1026, 4)])
    cor_k = max(float((Ok*bordas(V[n, 505:590])).sum((1, 2)).max()) for n in range(0, N, 5))
    # painéis = original
    dp = max(float(np.abs(V[n, 150:500].astype(int) - O[267+n-BL['paineis']['f0'], 150:500]).mean()) for n in pain if 267+n-BL['paineis']['f0'] > 270)
    r = (f"{P} {PEC}: decodifica {'OK' if not err else 'ERRO '+err[:80]} · {info} · {dur:.2f}s · silêncios>=0,5s: {nsil} · "
         f"rostos/frame max {nf.max()} (frames >1: {list(np.where(nf>1)[0])[:8]}) · frames de rosto sem rosto: {int((nf[rosto]==0).sum())} · "
         f"bordas janela x dupla original max {cor_j:.2f} · título x original {cor_t:.2f} · karaokê x original max {cor_k:.2f} · painéis dif max {dp:.1f}")
    print(r); linhas.append(r)
    # folha de sincronia do karaokê: no início de algumas palavras, o frame da peça (a palavra em roxo deve ser a escrita embaixo)
    pw = T['palavras']; idx = np.linspace(0, len(pw)-1, 10).astype(int)
    folha = [lab(V[min(int(round(pw[i]['s']*30))+2, N-1)], pw[i]['w'][:14]) for i in idx]
    cv2.imwrite(f'conferencia/karaoke-sync-{P}.jpg', np.hstack(folha), [cv2.IMWRITE_JPEG_QUALITY, 80])
    # emendas e clarão
    TP = BL['paineis']['f0']; em = [BL['b']['f0']-1, BL['b']['f0'], BL['a2']['f0']-1, BL['a2']['f0'], TP-5, TP-4, TP-2, TP, TP+2, TP+4, BL['a3']['f0']-1, BL['a3']['f0']]
    cv2.imwrite(f'conferencia/emendas-{P}.jpg', np.hstack([lab(V[n], str(n)) for n in em]), [cv2.IMWRITE_JPEG_QUALITY, 80])
open('conferencia/conferencia.txt', 'w').write('\n'.join(linhas)+'\n')
