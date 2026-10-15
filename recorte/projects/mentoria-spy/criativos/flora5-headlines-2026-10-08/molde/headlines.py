# Troca SÓ a headline da var5 Flora (27/09). A faixa de título (pílulas brancas, texto preto, y 41-150) é estática,
# exceto no clarão (n 263-284 e piscadas), em que o fundo preto fica laranja e a pílula fica POR CIMA (texto segue preto).
# Então: out = A·(k·faixa) + (1-A)·add, com A = máscara da pílula nova; add = clarão lido no fundo fora da pílula antiga
# e interpolado por linha; k = leve tingimento, medido no branco da pílula antiga.
# 08/10: copiado de centerpag-detect/criativos/var5-flora-959352790554428-2026-09-25/headlines.py; só mudam HEADLINES e caminhos.
# Uso: python3 headlines.py <entrada.mp4> <pasta-saida>
import sys, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
IN, OUTDIR = sys.argv[1], sys.argv[2]
W, H, TH = 360, 640, 168          # TH: altura da faixa de cima (a janela de vídeo começa em y 168)
FONT = '/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/zapspy/_lib/Montserrat-Variable.ttf'
ROXO = (110, 40, 220)             # roxo do karaokê
# cada linha: lista de (texto, destaque?)
HEADLINES = {
    '194-ZAP-flora-quando-nao-olha': [[('WHAT THEIR WHATSAPP', 0)], [('SAYS WHEN YOU\'RE', 0)], [('NOT LOOKING', 1)]],
    '195-ZAP-flora-digitei-numero':  [[('I TYPED THEIR NUMBER', 0)], [('AND SAW ', 0), ('EVERY', 1), (' CHAT', 0)], [('ON MY OWN PHONE', 0)]],
    '196-ZAP-flora-com-quem-fala':   [[('WHO IS YOUR PARTNER', 0)], [('REALLY', 1), (' TEXTING', 0)], [('ON WHATSAPP?', 0)]],
    '197-ZAP-flora-poucos-segundos': [[('THEIR WHATSAPP CHATS', 0)], [('ON YOUR PHONE IN', 0)], [('A FEW ', 0), ('SECONDS', 1)]],
    '198-ZAP-flora-arquivadas':      [[('EVEN THE ', 0), ('ARCHIVED', 1)], [('AND REMOVED CHATS', 0)], [('SHOW UP FOR YOU', 0)]],
}

def faixa(linhas, S=4):
    """Renderiza a faixa 360x168 em S× e reduz (antialias). Pílula por linha, unidas, como no original.
    Medidas do original: caixa-alta ~17 px, passo de linha ~31 px, pílula até ~310 px de largura, bloco centrado em y 95."""
    img = Image.new('RGB', (W*S, TH*S), (0, 0, 0)); d = ImageDraw.Draw(img)
    msk = Image.new('L', (W*S, TH*S), 0); dm = ImageDraw.Draw(msk)
    size = 26*S
    while True:
        f = ImageFont.truetype(FONT, size); f.set_variation_by_axes([700])
        cap = f.getbbox('H')[3] - f.getbbox('H')[1]
        larg = [sum(d.textlength(t, font=f) for t, _ in l) for l in linhas]
        if cap <= 17*S and max(larg) <= 292*S: break
        size -= 1
    lh = min(31*S, cap + 14*S); y0 = int(95.5*S - (lh*(len(linhas)-1) + cap)/2)
    padx, pady, r = 9*S, (lh - cap)//2 + 2*S, 8*S   # pady > meio vão: pílulas se sobrepõem, sem fresta
    for i, lw in enumerate(larg):   # pílulas primeiro (sobrepostas verticalmente = uma forma só)
        x0 = (W*S - lw)/2; y = y0 + i*lh
        box = [x0-padx, y-pady, x0+lw+padx, y+cap+pady]
        d.rounded_rectangle(box, r, fill=(255, 255, 255)); dm.rounded_rectangle(box, r, fill=255)
    for i, (l, lw) in enumerate(zip(linhas, larg)):
        x = (W*S - lw)/2; y = y0 + i*lh - f.getbbox('H')[1]
        for t, hl in l:
            d.text((x, y), t, font=f, fill=ROXO if hl else (0, 0, 0)); x += d.textlength(t, font=f)
    A = np.asarray(msk.resize((W, TH), Image.LANCZOS)).astype(np.float32)[..., None]/255
    return np.asarray(img.resize((W, TH), Image.LANCZOS)).astype(np.float32), A, cap/S

raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', IN, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
V = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3); N = len(V)
top = V[:, :TH].astype(np.float32)
limpa = np.median(top[::20], axis=0)                       # faixa sem clarão
branco = limpa.mean(axis=2) > 200
# fundo = escuro E fora do vão da pílula na linha (as letras pretas dentro da pílula não são fundo)
dentro = np.zeros((TH, W), bool)
for y in range(TH):
    b = np.where(branco[y])[0]
    if len(b): dentro[y, max(b.min()-3, 0):b.max()+4] = True
preto = (limpa.mean(axis=2) < 12) & ~dentro
desvio = np.abs(top - limpa).mean(axis=(1, 2, 3)); afet = np.where(desvio > 2.0)[0]
print('frames', N, 'com clarão na faixa:', afet.tolist())
xs = np.arange(W)
def clarao(fr):
    add = np.zeros_like(fr)
    for y in range(TH):
        m = preto[y]
        for c in range(3): add[y, :, c] = np.interp(xs, xs[m], fr[y, m, c]) if m.any() else 0
    k = np.array([np.median(fr[branco][:, c] / limpa[branco][:, c]) for c in range(3)])   # tingimento da pílula
    return add, np.clip(k, 0, 1.2)

import os; os.makedirs(OUTDIR, exist_ok=True)
modelos = {n: clarao(top[n]) for n in afet}
for nome, linhas in HEADLINES.items():
    F, A, fs = faixa(linhas)
    Image.fromarray(F.astype(np.uint8)).save(f'{OUTDIR}/../faixas/{nome}-faixa.png')
    out = f'{OUTDIR}/{nome}.mp4'
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-',
                          '-i', IN, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '17', '-preset', 'slow', '-pix_fmt', 'yuv420p',
                          '-c:a', 'copy', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for n in range(N):
        fr = V[n].copy()
        if n in modelos: add, k = modelos[n]; fr[:TH] = np.clip(A*F*k + (1-A)*add, 0, 255).astype(np.uint8)
        else: fr[:TH] = F.astype(np.uint8)
        p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()
    print(nome, f'caixa-alta {fs:.1f}px', out)
