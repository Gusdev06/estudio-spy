# f2 CLEAN PHONE: formato sem rosto. Fundo = os PAINÉIS do funil da Flora original (celular na mão, formulário e chats)
# em tela cheia, escurecidos, com a headline em pílula no topo e o karaokê grande embaixo. Kicker de texto por frase.
# Não desenha interface de chat: reaproveita o que já existe na peça original.
import sys, os, json; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../_kit')); from render import *
D = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(D, '../_kit')
pal = json.load(open(f'{D}/voz-apertada.palavras.json')); AUD = f'{D}/voz-apertada.wav'; dur = dur_audio(AUD) + 0.3
pain = Leitor(f'{K}/paineis.mp4')
HL = headline([[('THE ', 0), ('SWEETEST', 1), (' PARTNERS', 0)], [('HAVE THE ', 0), ('CLEANEST', 1)], [('PHONES.', 0)]], cap_alvo=42)
bl = blocos(pal, max_pal=3, size=58)
t_enter = palavra_t(pal, 'enter'); t_link = palavra_t(pal, 'link'); t_but = palavra_t(pal, 'but')
# percorre os painéis: começa nos chats (fala de mensagens), vai pro formulário quando fala "enter their number"
def src_painel(t):
    if t < t_but: return 6.5 + t * 0.4          # chats / conversas
    if t < t_enter: return 11.0 + (t - t_but) * 0.3
    return 3.0 + (t - t_enter) * 0.8            # formulário "enter the number"
out = Saida(f'{D}/f2-clean-phone.mp4', AUD, dur)
for n in range(out.n):
    t = n / FPS
    base = cobrir(pain.frame(src_painel(t)), W, H, zoom=1.15, cx=0.5, cy=0.5).convert('RGBA')
    dark = Image.new('RGBA', (W, H), (8, 12, 16, 150)); base.alpha_composite(dark)   # véu escuro pra ler texto
    colar(base, HL, W / 2, 250)
    colar(base, karaoke(bl, t, size=58), W / 2, 980)
    if t >= t_link: colar(base, seta(t), W / 2, 1120)
    out.escreve(base)
out.fecha()
