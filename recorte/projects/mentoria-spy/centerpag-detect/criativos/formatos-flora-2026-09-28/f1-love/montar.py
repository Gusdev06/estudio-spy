# f1 LOVE: talking head solo em tela cheia, punch-in por frase, karaokê grande no centro-baixo,
# card do funil (formulário -> chats) quando fala "enter their number", seta de CTA no fim.
import sys, os, json; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../_kit')); from render import *
D = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(D, '../_kit')
pal = json.load(open(f'{D}/voz-apertada.palavras.json')); AUD = f'{D}/voz-apertada.wav'; dur = dur_audio(AUD) + 0.3
rosto = Leitor(f'{D}/lipsync.mp4'); pain = Leitor(f'{K}/paineis.mp4')
HL = headline([[("LOVING YOU DOESN'T", 0)], [('STOP THEM FROM', 0)], [('CHEATING.', 1)]], cap_alvo=40)
bl = blocos(pal, max_pal=3, size=62)
# frases -> zoom alternado (corte seco de enquadramento a cada frase = ritmo de edição)
frases = [0.0, palavra_t(pal, 'he'), palavra_t(pal, 'love', 2), palavra_t(pal, 'just'), palavra_t(pal, 'even'), palavra_t(pal, 'link')]
ZOOM = [1.18, 1.0, 1.25, 1.06, 1.12, 1.0]
t_card = palavra_t(pal, 'enter'); t_card_fim = palavra_t(pal, 'link') - 0.1; t_chats = palavra_t(pal, 'see')
t_cta = palavra_t(pal, 'link')
out = Saida(f'{D}/f1-love.mp4', AUD, dur)
for n in range(out.n):
    t = n / FPS; i = max(k for k, f in enumerate(frases) if f <= t)
    z = ZOOM[i] + 0.03 * min(1, (t - frases[i]) / 3)          # leve push-in dentro da frase
    img = cobrir(rosto.frame(t), W, H, zoom=z, cx=0.5, cy=0.36).convert('RGBA')
    # headline: grande no hook (0-2,9 s), depois sobe e fica pequena no topo o vídeo todo
    if t < 2.8: colar(img, HL, W / 2, 250)
    else:
        k = entra(t, 2.8, 0.3); hs = HL.resize((int(HL.width * (1 - 0.22 * k)), int(HL.height * (1 - 0.22 * k))), Image.LANCZOS)
        colar(img, hs, W / 2, 250 - 115 * k)
    if t_card <= t < t_card_fim:                                  # card do funil
        k = entra(t, t_card, 0.3); src = 3.0 + (t - t_card) if t < t_chats else 8.0 + (t - t_chats) * 1.2
        c = card(nitido(cobrir(pain.frame(src), 520, 438, zoom=1.0)), raio=26)
        colar(img, c, W / 2, 610 + (1 - k) * 120, alpha=k)
    y_leg = 1000 if t_card <= t < t_card_fim else 900
    colar(img, karaoke(bl, t, size=62), W / 2, y_leg)
    if t >= t_cta: colar(img, seta(t), W / 2, 1130)
    out.escreve(img)
out.fecha()
