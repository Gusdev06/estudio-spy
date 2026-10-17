"""Monta V1: gancho iMessage (f0-139) + push-wipe do original (f140-154, metade esquerda
trocada pelo chat empurrado) + original intacto f155-1094 + trilha original inteira.
Uso: python3 render_gancho.py && python3 montar.py
"""
import os, subprocess
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, "..", "REFERENCIA-original.mp4")
# 17/10: demo com "Copy her @" vem da V3 (igual ao original fora da legenda a partir do f150)
HER = os.path.join(HERE, "..", "v3-quem-ele-curte", "pecas", "v3-quem-ele-curte.mp4")
CHAT = os.path.join(HERE, "work", "chat")
WIPE = os.path.join(HERE, "work", "wipe")
OUT = os.path.join(HERE, "pecas", "v1-chat-bros.mp4")
os.makedirs(WIPE, exist_ok=True)

W0, W1 = 140, 154          # frames do push-wipe no original
CLEAN = 155                # primeiro frame 100% original

def boundary(f):           # medido: borda vertical em x = 708 - 48*(f-140)
    return 708 - 48 * (f - 140)

# extrai os frames do wipe do original
subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", "-i", REF,
                "-vf", f"select='between(n,{W0},{W1})'", "-vsync", "0",
                "-start_number", str(W0), os.path.join(WIPE, "o%04d.png")], check=True)
subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", "-i", HER,
                "-vf", "select='between(n,150,154)'", "-vsync", "0",
                "-start_number", "150", os.path.join(WIPE, "o%04d.png")], check=True)

last = np.asarray(Image.open(os.path.join(CHAT, "c0139.png")).convert("RGB"))
# A caixa de legenda do café ("Girl, how do I...") é outra camada no original e vaza por cima
# da demo nos frames 141-149 (medido: some no f150). Tapa a faixa y 860-1145 do lado da demo
# com o recorte do f155 (primeiro frame limpo) deslocado como no push, borda suave em cima/embaixo.
subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", "-i", HER,
                "-vf", f"select='eq(n,{CLEAN})'", "-vsync", "0", "-frames:v", "1",
                os.path.join(WIPE, "clean.png")], check=True)
clean = np.asarray(Image.open(os.path.join(WIPE, "clean.png")).convert("RGB")).astype(float)
LEAK = range(141, 150)
Y0, Y1, FE = 860, 1145, 24
alpha = np.zeros((1280, 1), float)
alpha[Y0:Y1] = 1.0
alpha[Y0 - FE:Y0, 0] = np.linspace(0, 1, FE)
alpha[Y1:Y1 + FE, 0] = np.linspace(1, 0, FE)
for f in range(W0, W1 + 1):
    o = np.asarray(Image.open(os.path.join(WIPE, f"o{f:04d}.png")).convert("RGB")).copy()
    b = boundary(f)
    shift = 720 - b                      # chat empurrado pra esquerda, igual ao café no original
    if f in LEAK:
        # a demo entra empurrada: o lado da demo no frame f ~ f155 deslocado b+4 px (medido)
        sh = b + 4
        src = np.zeros_like(clean); src[:, sh:] = clean[:, :720 - sh]
        o[:, sh:] = (o[:, sh:] * (1 - alpha[:, :, None]) + src[:, sh:] * alpha[:, :, None]).round().astype(np.uint8)
    o[:, :b] = last[:, shift:shift + b]
    Image.fromarray(o).save(os.path.join(WIPE, f"w{f:04d}.png"))

# lista concat: chat 0-139, wipe 140-154 como sequência de imagens; resto direto do original
lst = os.path.join(HERE, "work", "frames.txt")
with open(lst, "w") as fh:
    for t in range(0, W0):
        fh.write(f"file '{os.path.join(CHAT, f'c{t:04d}.png')}'\nduration 0.0333333\n")
    for f in range(W0, W1 + 1):
        fh.write(f"file '{os.path.join(WIPE, f'w{f:04d}.png')}'\nduration 0.0333333\n")
    fh.write(f"file '{os.path.join(WIPE, f'w{W1:04d}.png')}'\n")   # repete o último (concat ignora a duração final)

# um único encode: [imagens 0-154] + [original 155-1094] concatenados por filtro
fc = (f"[0:v]fps=30,setsar=1,format=yuv420p,trim=end_frame={W1+1},setpts=PTS-STARTPTS[a];"
      f"[1:v]trim=start_frame={CLEAN},setpts=PTS-STARTPTS,setsar=1,format=yuv420p[b];"
      f"[a][b]concat=n=2:v=1:a=0[v]")
subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y",
                "-f", "concat", "-safe", "0", "-i", lst, "-i", HER,
                "-filter_complex", fc, "-map", "[v]", "-map", "1:a",
                "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p",
                "-r", "30", "-frames:v", "1095",
                "-c:a", "copy", "-movflags", "+faststart", OUT], check=True)
print("ok", OUT)
