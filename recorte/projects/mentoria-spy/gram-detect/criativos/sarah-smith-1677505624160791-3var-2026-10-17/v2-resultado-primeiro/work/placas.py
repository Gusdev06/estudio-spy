# Gera as placas de texto (PNG RGBA 720x1280) do gancho da V2.
# Placa preta arredondada (estilo da caixa do gancho original) que cobre a
# area do "Done! Now you can see..." (x 58-660, y 160-240 no original).
import os
from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(AQUI, "Montserrat-Variable.ttf")
EMOJI = "/System/Library/Fonts/Apple Color Emoji.ttc"
W, H = 720, 1280
SZ = 54

def font():
    f = ImageFont.truetype(FONTE, SZ)
    f.set_variation_by_name("ExtraBold")
    return f

def emoji_img(ch, size):
    ef = ImageFont.truetype(EMOJI, 160)
    im = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((10, 10), ch, font=ef, embedded_color=True)
    im = im.crop(im.getbbox())
    r = size / im.height
    return im.resize((round(im.width * r), size), Image.LANCZOS)

def placa(linhas, saida, box=(30, 130, 690, 300)):
    """linhas: lista de (texto, emoji_ou_None)."""
    f = font()
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, radius=26, fill=(0, 0, 0, 255))
    lh = SZ + 14
    total = lh * len(linhas) - 14
    y0 = (box[1] + box[3]) // 2 - total // 2
    for i, (txt, emo) in enumerate(linhas):
        tw = d.textlength(txt, font=f)
        e = emoji_img(emo, int(SZ * 0.95)) if emo else None
        gap = 12 if e else 0
        full = tw + gap + (e.width if e else 0)
        x = (W - full) / 2
        y = y0 + i * lh
        d.text((x, y), txt, font=f, fill="white", anchor="la",
               stroke_width=2, stroke_fill="black")
        if e:
            asc = f.getbbox("A")
            im.alpha_composite(e, (int(x + tw + gap), int(y + asc[1] + (asc[3] - asc[1]) / 2 - e.height / 2)))
    im.save(saida)

if __name__ == "__main__":
    placa([("he said she was", None), ("“just a friend”", "\U0001F642")],
          os.path.join(AQUI, "placa1.png"))
    placa([("so I checked", None), ("her account", "\U0001F447")],
          os.path.join(AQUI, "placa2.png"))
