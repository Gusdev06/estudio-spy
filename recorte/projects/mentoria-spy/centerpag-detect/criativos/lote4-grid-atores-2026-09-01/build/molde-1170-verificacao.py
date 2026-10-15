#!/usr/bin/env python3
"""Molde base spy: rosto full-bleed + tarja + bloco grafico (com fade) + karaoke.
Parametrizado por largura de saida — 1170x2532 (original) ou 1080x1920 (9:16)."""
import json, subprocess, os, sys

CR="/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/centerpag-detect/criativos"
KIT=f"{CR}/lote3-isabella-2026-09-01/kit"

# --- geometria medida no master 1170x2532 ---
G = dict(
  W0=1170, H0=2532,
  TARJA_Y=0,   TARJA_H=498,
  BLOCO_Y=1596, BLOCO_H=936,
  KARA_Y=1670,  KARA_H=220,
  TARJA_ON=[(0,437),(589,659)],          # frames, corte seco medido
  BLOCO_F=(438,450,576,588),             # fade in ini/fim, fade out ini/fim (frames)
)

def build(plate, cards_dir, plano, out, W, H, crop_top=None, audio_from=None):
    s = W / G["W0"]
    Hs = round(G["H0"] * s)                    # altura do plate reescalado
    if crop_top is None: crop_top = 0
    tar_h = round(G["TARJA_H"]*s)
    blo_h = round(G["BLOCO_H"]*s)
    kar_h = round(G["KARA_H"]*s)
    blo_y = H - blo_h                           # ancorado no rodape
    kar_y = blo_y + round((G["KARA_Y"]-G["BLOCO_Y"])*s)
    tar_y = 0

    cards = json.load(open(plano))
    ins = ["-i", plate,
           "-loop","1","-framerate","30","-t","22","-i", f"{KIT}/tarja.png",
           "-loop","1","-framerate","30","-t","22","-i", f"{KIT}/bloco-grafico.png"]
    for c in cards:
        ins += ["-loop","1","-framerate","30","-t","22","-i", f"{cards_dir}/{c['id']}.png"]

    f=[]
    f.append(f"[0:v]scale={W}:{Hs}:flags=lanczos,crop={W}:{H}:0:{crop_top},format=rgba[base]")
    on = "+".join(f"between(n,{a},{b})" for a,b in G["TARJA_ON"])
    f.append(f"[1:v]scale={W}:{tar_h}:flags=lanczos,format=rgba[tar]")
    fi0,fi1,fo0,fo1 = G["BLOCO_F"]
    f.append(f"[2:v]scale={W}:{blo_h}:flags=lanczos,format=rgba,"
             f"fade=t=in:st={fi0/30:.6f}:d={(fi1-fi0)/30:.6f}:alpha=1,"
             f"fade=t=out:st={fo0/30:.6f}:d={(fo1-fo0)/30:.6f}:alpha=1[blo]")
    f.append(f"[base][tar]overlay={0}:{tar_y}:enable='{on}'[v1]")
    f.append(f"[v1][blo]overlay={0}:{blo_y}:enable='between(n,{fi0},{fo1})'[v2]")
    prev="v2"
    for i,c in enumerate(cards):
        idx=3+i; nxt=f"k{i}"
        f.append(f"[{idx}:v]scale={W}:{kar_h}:flags=lanczos,format=rgba[c{i}]")
        f.append(f"[{prev}][c{i}]overlay={0}:{kar_y}:enable='between(t,{c['ini']:.3f},{c['fim']:.3f})'[{nxt}]")
        prev=nxt
    f.append(f"[{prev}]format=yuv420p[vout]")

    cmd=["ffmpeg","-v","error","-y"]+ins
    if audio_from: cmd += ["-i", audio_from]
    cmd += ["-filter_complex",";".join(f),"-map","[vout]"]
    if audio_from: cmd += ["-map", f"{3+len(cards)}:a","-c:a","copy"]
    cmd += ["-frames:v","660","-r","30","-c:v","libx264","-profile:v","high","-pix_fmt","yuv420p",
            "-crf","17","-preset","medium","-movflags","+faststart", out]
    subprocess.run(cmd, check=True)
    return dict(W=W,H=H,s=round(s,6),Hs=Hs,crop_top=crop_top,tarja=(0,tar_h),
                bloco=(blo_y,blo_y+blo_h),kara=(kar_y,kar_y+kar_h))

if __name__=="__main__":
    pass
