"""Estáticos 'dare' no desenho do SocialCatfish 1085399717277321 (448x600 -> 1080x1446).
Medidas tiradas da referência por pixel (escala S=1080/448):
- fundo #000; texto branco Helvetica Neue Bold, alinhado à esquerda, margem esq 33px ref
- maiúscula 'I' com 40px de altura -> calibra o corpo; linha 'If you truly trust' com 378px de tinta
  -> a ref é ~10% mais apertada que a Helvetica Neue Bold padrão: calibra o tracking negativo
- passo de linha 53.3px ref; topo da tinta da 1a linha em y=91 ref; largura máx da linha 380px ref
- rodapé Helvetica Neue Regular, caixa alta, altura de maiúscula 11px ref, topo em y=563, centralizado
Uso: python3 montar.py  (gera pecas/*.png e conferencia.jpg)"""
from PIL import Image, ImageDraw, ImageFont
import os
HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, '../../../swipe-keywords-2026-10-17/anuncios/socialcatfish-com__socialcatfish-com-1085399717277321.jpg')
FONT = '/System/Library/Fonts/HelveticaNeue.ttc'
W, H = 1080, round(600 * 1080 / 448)
S = W / 448

TRACK = 0.0
def ink_w(font, s, track=None):
    t = TRACK if track is None else track
    b = font.getbbox(s); return b[2] - b[0] + t * (len(s) - 1)

def draw_tracked(d, xy, s, font, track):
    x, y = xy
    for i, ch in enumerate(s):
        d.text((x + font.getlength(s[:i]) + i * track, y), ch, font=font, fill='white')

# calibra: tracking fixo de -2,5% do corpo (a ref é mais apertada que o padrão), corpo pela largura de 'If you truly trust' = 378px ref.
# (calibrar pela altura da maiúscula, 40px na ref, deixava as letras coladas: o JPEG infla a altura medida)
size = 50
while True:
    f = ImageFont.truetype(FONT, size + 1, index=1)
    if ink_w(f, 'If you truly trust', -0.025 * (size + 1)) > 378 * S: break
    size += 1
BODY = ImageFont.truetype(FONT, size, index=1)
TRACK = -0.025 * size
PITCH = round(53.3 * S); LEFT = round(33 * S); TOP = round(91 * S)
MAXW = 950  # ref: 381px*S=918; folga de 3% pra 'your boyfriend...' caber numa linha como na ref
# rodapé: altura do 'H' = 11px ref
fs = 10
while (lambda f: f.getbbox('H')[3] - f.getbbox('H')[1])(ImageFont.truetype(FONT, fs, index=0)) < 11 * S: fs += 1
FOOT = ImageFont.truetype(FONT, fs, index=0); FOOT_TOP = round(563 * S)

def wrap(text):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if ink_w(BODY, t) <= MAXW: cur = t
        else: lines.append(cur); cur = w
        if w.endswith('...'): lines.append(cur); cur = ''  # a ref quebra depois das reticências
    return [l for l in lines + [cur] if l]

def render(text, foot, out):
    im = Image.new('RGB', (W, H), 'black'); d = ImageDraw.Draw(im)
    lines = wrap(text)
    asc = BODY.getbbox('I')[1]  # offset do topo da tinta
    # bloco de 7 linhas fica no topo da ref; se mudar a contagem, mantém o centro do bloco
    y0 = TOP + (7 - len(lines)) * PITCH / 2
    for i, l in enumerate(lines):
        draw_tracked(d, (LEFT - BODY.getbbox(l)[0], y0 + i * PITCH - asc), l, BODY, TRACK)
    fb = FOOT.getbbox(foot)
    d.text(((W - (fb[2] - fb[0])) / 2 - fb[0], FOOT_TOP - FOOT.getbbox('H')[1]), foot, font=FOOT, fill='white')
    im.save(out); return lines

PECAS = [
 ('2a-dare-ig-boyfriend.png', "If you truly trust your boyfriend... I dare you to type his @ here and see who he's really talking to.", 'SEARCH HIS @'),
 ('2b-dare-girlfriend.png', "If you truly trust your girlfriend... I dare you to type her @ here and see who she's really talking to.", 'SEARCH HER @'),
 ('2c-dare-wpp-number.png', "If you truly trust your husband... I dare you to enter his number here and see who he's really texting.", 'SEARCH HIS NUMBER'),
]
if __name__ == '__main__':
    print('canvas', W, H, 'corpo', size, 'tracking', round(TRACK, 1), 'passo', PITCH, 'margem', LEFT, 'rodapé', fs)
    outs = []
    for nome, txt, foot in PECAS:
        p = os.path.join(HERE, 'pecas', nome); print(nome, render(txt, foot, p)); outs.append(p)
    # folha de conferência: ref + 3 peças, mesma altura
    ref = Image.open(REF).convert('RGB').resize((W, H))
    sheet = Image.new('RGB', (W * 4 + 60, H), (128, 128, 128))
    for i, p in enumerate([ref] + [Image.open(o) for o in outs]): sheet.paste(p, (i * (W + 20), 0))
    sheet.resize((sheet.width // 2, H // 2)).save(os.path.join(HERE, 'conferencia.jpg'), quality=88)
