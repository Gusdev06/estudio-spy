# f4 PODCAST MISTAKE: reedição de podcast. Alterna o clipe A (mulher, explica) e B (homem, pergunta) por segmento,
# com cold open (headline grande nos ~2,5 s), leve punch-in por fala, barra de progresso no topo, karaokê embaixo,
# e card do funil quando A fala "enter their number". Áudio = diálogo intercalado.
import sys, os, json; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../_kit')); from render import *
D = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(D, '../_kit')
seg = json.load(open(f'{D}/dialogo.segmentos.json')); pal = json.load(open(f'{D}/dialogo.palavras.json'))
AUD = f'{D}/dialogo.wav'; dur = dur_audio(AUD) + 0.3
A = Leitor(f'{D}/lipsync-A.mp4'); B = Leitor(f'{D}/lipsync-B.mp4'); pain = Leitor(f'{K}/paineis.mp4')
HL = headline([[('EVERY ', 0), ('CHEATER', 1)], [('MAKES THE SAME', 0)], [('MISTAKE.', 0)]], cap_alvo=44)
bl = blocos(pal, max_pal=3, size=56)
t_enter = palavra_t(pal, 'enter'); t_link = palavra_t(pal, 'link'); t_below = palavra_t(pal, 'below', 1)
def seg_em(t):
    for s in seg:
        if s['ini'] <= t < s['fim']: return s
    return min((s for s in seg if s['ini'] >= t), key=lambda s: s['ini'], default=seg[-1])   # no gap, usa o próximo
out = Saida(f'{D}/f4-podcast-mistake.mp4', AUD, dur)
for n in range(out.n):
    t = n / FPS; s = seg_em(t); src = s['src_ini'] + (t - s['ini'])
    L = A if s['papel'] == 'A' else B
    k = min(1, (t - s['ini']) / 3); z = 1.06 + 0.05 * k                # push-in dentro da fala
    img = cobrir(L.frame(src), W, H, zoom=z, cx=0.5, cy=0.42).convert('RGBA')
    # barra de progresso
    ImageDraw.Draw(img).rectangle([0, 0, int(W * t / dur), 10], fill=(230, 40, 40, 255))
    if t < 2.5: colar(img, HL, W / 2, 300)                              # cold open
    else:
        kk = entra(t, 2.5, 0.3); hs = HL.resize((int(HL.width * (1 - 0.35 * kk)), int(HL.height * (1 - 0.35 * kk))), Image.LANCZOS)
        colar(img, hs, W / 2, 250 - 130 * kk)
    if t_enter <= t < t_below:
        kk = entra(t, t_enter, 0.3); c = card(nitido(cobrir(pain.frame(3.0 + (t - t_enter)), 470, 396)), raio=24)
        colar(img, c, W / 2, 660, alpha=kk)
    colar(img, karaoke(bl, t, size=56), W / 2, 940)
    if t >= t_link: colar(img, seta(t), W / 2, 1150)
    out.escreve(img)
out.fecha()
