# f3 RED FLAGS: listicle. Talking head em tela cheia; a cada "number one/two/three" entra um NÚMERO gigante
# no canto + a red flag em pílula; punch-in por item. Card do funil em "enter their number". Seta no fim.
import sys, os, json; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../_kit')); from render import *
D = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(D, '../_kit')
pal = json.load(open(f'{D}/voz-apertada.palavras.json')); AUD = f'{D}/voz-apertada.wav'; dur = dur_audio(AUD) + 0.3
rosto = Leitor(f'{D}/lipsync.mp4'); pain = Leitor(f'{K}/paineis.mp4')
HL = headline([[('IF THEY FLIP THEIR', 0)], [('PHONE ', 0), ('FACE DOWN', 1)], [('WATCH THIS.', 0)]], cap_alvo=38)
bl = blocos(pal, max_pal=3, size=60)
t1 = palavra_t(pal, 'one'); t2 = palavra_t(pal, 'two'); t3 = palavra_t(pal, 'three')
t_enter = palavra_t(pal, 'enter'); t_link = palavra_t(pal, 'link'); t_now = palavra_t(pal, 'now')
ITENS = [(t1, '1', [('ALWAYS', 1), (' FACE DOWN', 0)]), (t2, '2', [('GOES TO THE', 0)]), (t3, '3', [('CHATS ALWAYS', 0), (' EMPTY', 1)])]
def num_big(txt):
    f = fonte(300, 900); img = Image.new('RGBA', (240, 320), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.text((120, 160), txt, font=f, fill=(230, 40, 40), stroke_width=10, stroke_fill=BRANCO, anchor='mm'); return img
out = Saida(f'{D}/f3-red-flags.mp4', AUD, dur)
for n in range(out.n):
    t = n / FPS
    z = 1.12
    for ti, _, _ in ITENS:
        if ti <= t < ti + 0.6: z = 1.12 + 0.12 * (1 - (t - ti) / 0.6)   # pulso no anúncio do item
    img = cobrir(rosto.frame(t), W, H, zoom=z, cx=0.5, cy=0.34).convert('RGBA')
    if t < 2.7: colar(img, HL, W / 2, 250)
    else:
        k = entra(t, 2.7, 0.3); hs = HL.resize((int(HL.width * (1 - 0.25 * k)), int(HL.height * (1 - 0.25 * k))), Image.LANCZOS)
        colar(img, hs, W / 2, 230 - 100 * k)
    # item ativo
    for j, (ti, num, texto) in enumerate(ITENS):
        tf = ITENS[j + 1][0] if j + 1 < len(ITENS) else t_now
        if ti <= t < tf:
            k = entra(t, ti, 0.3); nb = num_big(num); colar(img, nb, 130, 560, alpha=k)
            colar(img, headline([texto], cap_alvo=40), W / 2 + 40, 560, alpha=k)
    if t_enter <= t < t_link:
        k = entra(t, t_enter, 0.3); c = card(nitido(cobrir(pain.frame(3.0 + (t - t_enter)), 500, 421)), raio=26)
        colar(img, c, W / 2, 640, alpha=k)
    colar(img, karaoke(bl, t, size=60), W / 2, 900)
    if t >= t_link: colar(img, seta(t), W / 2, 1130)
    out.escreve(img)
out.fecha()
