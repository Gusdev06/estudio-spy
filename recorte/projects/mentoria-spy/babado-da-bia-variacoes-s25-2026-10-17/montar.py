# Variações do lote Seedance 2.5 (17/10): clipe limpo da réplica + texto vencedor no estilo da própria réplica + áudio original.
# uso (da pasta mentoria-spy): python3 babado-da-bia-variacoes-s25-2026-10-17/montar.py
import json, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(D, "..", "criativos")
H = "/System/Library/Fonts/HelveticaNeue.ttc"
idx = next(i for i in range(14) if ImageFont.truetype(H, 60, index=i).getname()[1] == "Medium")
# pasta, clipe limpo, áudio, fonte, passo de linha, centro y, largura máx, cor (medidos dos legendas.py das réplicas)
BASES = {
 "lily5":    ("lily-girltea-7670633492090293517-bia-2026-10-16", "bia.mp4", "original-h264.mp4", 64, 74, 1130, 700, (255,255,255)),
 "cindy":    ("cindy-girlcode-DWQggrRjd9D-bia-2026-10-16", "bia.mp4", "original.mp4", 58, 72, 935, 760, (253,244,168)),
 "kourtney": ("kourtney-girlcode-DVt8gtCkY9f-bia-2026-10-16", "bia.mp4", "original-h264.mp4", 54, 60, 990, 780, (250,248,247)),
 "cat":      ("cat.girltea-7680383645965700366-bia-2026-10-16", "bia.mp4", "original-h264.mp4", 72, 91, 835, 700, (255,255,255)),
 "lily7":    ("lily-girltea-7674103997178907918-bia-2026-10-16", "bia-limpo.mp4", "original-h264.mp4", 64, 80, 862, 780, (250,249,244)),
}
def png(texto, tam, passo, cy, larg, cor, saida):
    f = ImageFont.truetype(H, tam, index=idx); L, c = [], ""
    for w in texto.split():
        s = (c + " " + w).strip()
        if f.getbbox(s)[2] - f.getbbox(s)[0] <= larg: c = s
        else: L.append(c); c = w
    L.append(c)
    txt = Image.new("RGBA", (1080, 1920), (0,0,0,0)); d = ImageDraw.Draw(txt)
    top = cy - (len(L) * passo) // 2; cap = f.getbbox("T")[1]
    for i, l in enumerate(L):
        b = f.getbbox(l); d.text(((1080 - (b[2]-b[0])) // 2 - b[0], top + i*passo - cap), l, font=f, fill=cor + (255,))
    sh = Image.new("RGBA", txt.size, (0,0,0,0)); sh.putalpha(txt.getchannel("A").point(lambda a: int(a*0.5)))
    sh = sh.filter(ImageFilter.GaussianBlur(3))
    out = Image.new("RGBA", txt.size, (0,0,0,0)); out.alpha_composite(sh, (2,3)); out.alpha_composite(txt); out.save(saida)
for it in json.load(open(os.path.join(D, "lote.json"))):
    pasta, clipe, aud, tam, passo, cy, larg, cor = BASES[it["base"]]; p = os.path.join(C, pasta)
    pngp = os.path.join(D, "legendas-png", it["id"] + ".png"); png(it["texto"], tam, passo, cy, larg, cor, pngp)
    open(os.path.join(D, "legendas", it["id"] + ".txt"), "w").write(it["legenda"])
    out = os.path.join(D, "videos", f"{it['id']}-{it['base']}.mp4")
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",os.path.join(p,"clipes",clipe),"-i",os.path.join(p,"original",aud),"-i",pngp,
        "-filter_complex","[0:v]scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,fps=30,setsar=1,format=yuv420p[v0];[v0][2]overlay[v]",
        "-map","[v]","-map","1:a","-c:v","libx264","-crf","17","-preset","slow","-profile:v","high","-c:a","aac","-b:a","128k","-ar","44100","-shortest","-movflags","+faststart",out], check=True)
    print("ok", out)
