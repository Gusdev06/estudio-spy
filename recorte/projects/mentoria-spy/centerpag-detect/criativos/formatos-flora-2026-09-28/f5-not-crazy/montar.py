# f5 NOT CRAZY: split vertical. Rosto (desabafo em 1ª pessoa) na METADE de cima; painel do funil na metade de baixo
# a partir de "I entered his number". Karaokê na divisa. Headline em pílula no topo. Seta no fim.
import sys, os, json; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../_kit')); from render import *
D = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(D, '../_kit')
pal = json.load(open(f'{D}/voz-apertada.palavras.json')); AUD = f'{D}/voz-apertada.wav'; dur = dur_audio(AUD) + 0.3
rosto = Leitor(f'{D}/lipsync.mp4'); pain = Leitor(f'{K}/paineis.mp4')
HL = headline([[("I'M NOT ", 0), ('CRAZY.', 1)], [('I JUST SAW', 0)], [('THE MESSAGES.', 0)]], cap_alvo=40)
bl = blocos(pal, max_pal=3, size=54)
t_ent = palavra_t(pal, 'entered'); t_link = palavra_t(pal, 'link'); t_every = palavra_t(pal, 'every', 1)
DIV = 700   # y da divisa quando o split abre
out = Saida(f'{D}/f5-not-crazy.mp4', AUD, dur)
for n in range(out.n):
    t = n / FPS
    split = entra(t, t_ent, 0.4)                 # 0 = rosto cheio; 1 = split aberto
    hb = int(H - (H - DIV) * split)              # altura da metade de cima
    top = cobrir(rosto.frame(t), W, hb, zoom=1.12, cx=0.5, cy=0.34).convert('RGBA')
    img = Image.new('RGBA', (W, H), (10, 10, 14, 255)); img.alpha_composite(top, (0, 0))
    if split > 0.02:
        src = 8.0 + (t - t_ent) * 1.0 if t >= t_ent else 8.0
        pn = cobrir(pain.frame(src), W, H - hb, zoom=1.1, cx=0.5, cy=0.5).convert('RGBA')
        img.alpha_composite(pn, (0, hb)); ImageDraw.Draw(img).rectangle([0, hb - 4, W, hb + 4], fill=(230, 40, 40, 255))
    if t < 2.6: colar(img, HL, W / 2, 250)
    else:
        k = entra(t, 2.6, 0.3); hs = HL.resize((int(HL.width * (1 - 0.28 * k)), int(HL.height * (1 - 0.28 * k))), Image.LANCZOS)
        colar(img, hs, W / 2, 210 - 90 * k)
    colar(img, karaoke(bl, t, size=52), W / 2, hb if split > 0.5 else 940)
    if t >= t_link: colar(img, seta(t), W / 2, 1180)
    out.escreve(img)
out.fecha()
