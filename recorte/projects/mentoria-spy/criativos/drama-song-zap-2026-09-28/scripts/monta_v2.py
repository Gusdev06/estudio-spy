# Monta a peça v2: clipes (plano-clipes-v2.json) aparados à duração exata + cancao-v2.mp3 como único áudio.
# Saídas: pecas/drama-song-zap-v2-sem-legenda.mp4 e pecas/drama-song-zap-v2-legendado.mp4 (ASS da letra por linha).
# Escolha de take por clipe: _runs/takes-v2.json {"B05": "B05-r1"} (default = id do clipe).
import json, subprocess, pathlib
L = pathlib.Path(__file__).resolve().parent.parent
plano = json.load(open(L / "_runs/plano-clipes-v2.json"))
tk = L / "_runs/takes-v2.json"; takes = json.load(open(tk)) if tk.exists() else {}
M = json.load(open(L / "mapa-de-tempo-v2.json")); DUR = M["duracao_audio"]
tmp = L / "_runs/monta-v2"; tmp.mkdir(exist_ok=True)
CUT = 0.1  # corta o 1º frame/flash
segs = []
for p in plano:
    src = L / f"clipes-v2/{takes.get(p['clip'], p['clip'])}.mp4"
    out = tmp / f"{p['clip']}.mp4"
    vf = (f"trim=start={CUT},setpts=PTS-STARTPTS,scale=740:1280:flags=lanczos,crop=720:1280,fps=30,"
          f"tpad=stop_mode=clone:stop_duration=2,trim=duration={p['dur']:.3f},setpts=PTS-STARTPTS,setsar=1")
    subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", "-i", str(src), "-an", "-vf", vf,
                    "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", str(out)], check=True)
    segs.append(out)
(tmp / "lista.txt").write_text("".join(f"file '{s}'\n" for s in segs))
video = tmp / "video.mp4"
subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "lista.txt"),
                "-c", "copy", str(video)], check=True)

# legenda ASS: 1 linha da letra por vez (a intro foi cantada 2x: 1,34 s e 9,24 s)
def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"
lin = [(l["inicio"], l["fim"], l["texto"]) for l in M["linhas"]]
lin.insert(0, (1.34, 3.82, lin[0][2]))
ev = []
for i, (a, b, t) in enumerate(lin):
    nxt = lin[i + 1][0] if i + 1 < len(lin) else DUR
    end = min(nxt - 0.02, b + 0.8)
    t = t.replace('"', "")
    # quebra em 2 linhas se longa
    w = t.split()
    if len(t) > 26:
        best = min(range(1, len(w)), key=lambda k: abs(len(" ".join(w[:k])) - len(" ".join(w[k:]))))
        t = " ".join(w[:best]) + r"\N" + " ".join(w[best:])
    ev.append(f"Dialogue: 0,{ts(a)},{ts(end)},Letra,,0,0,0,,{t}")
ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Letra,Arial,50,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,4,1,2,50,50,250,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ev) + "\n"
(L / "pecas").mkdir(exist_ok=True)
(L / "pecas/drama-song-zap-v2.ass").write_text(ass)
musica = L / "musica/cancao-v2.mp3"
base = ["ffmpeg", "-hide_banner", "-v", "error", "-y", "-i", str(video), "-i", str(musica), "-map", "0:v", "-map", "1:a",
        "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-b:a", "192k", "-t", f"{DUR:.3f}", "-movflags", "+faststart"]
subprocess.run(base + [str(L / "pecas/drama-song-zap-v2-sem-legenda.mp4")], check=True)
sub = str(L / "pecas/drama-song-zap-v2.ass").replace(":", r"\:")
subprocess.run(base[:13] + ["-vf", f"ass={sub}"] + base[13:] + [str(L / "pecas/drama-song-zap-v2-legendado.mp4")], check=True)
print("ok", len(segs), "segmentos")
