#!/usr/bin/env python3
"""Reentrega 9:16 (1080x1920) das 8 pecas spy — recomposicao, sem letterbox.
Toda geometria abaixo foi MEDIDA nas pecas 1170x2532 que shipparam (ver README do lote)."""
import json, subprocess, os, sys

CR="/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/centerpag-detect/criativos"
L3=f"{CR}/lote3-isabella-2026-09-01"; L4D=f"{CR}/lote4-grid-atores-2026-09-01"
KIT=f"{L3}/kit"
W,H = 1080,1920
S = W/1170                      # 0.9230769
def sc(v): return round(v*S)

ENC=["-frames:v","660","-r","30","-c:v","libx264","-profile:v","high","-pix_fmt","yuv420p",
     "-crf","17","-preset","medium","-movflags","+faststart"]

def run(ins, filt, out, amap):
    cmd=["ffmpeg","-v","error","-y"]+ins+["-filter_complex",";".join(filt),
         "-map","[vout]","-map",f"{amap}:a","-c:a","copy"]+ENC+[out]
    subprocess.run(cmd,check=True)

def img(path,t=22): return ["-loop","1","-framerate","30","-t",str(t),"-i",path]

def cards_of(plano_dir):
    return json.load(open(f"{plano_dir}/plano.json"))

# ---------- MOLDE BASE: rosto full-bleed + tarja + bloco (fade) + karaoke ----------
# medido: tarja y0 h498 corte seco ON f0-437 e f589-659 | bloco y1596 h936 fade 12f
#         (f438->450 entra, f576->588 sai) | karaoke y1670 h220
def base(plate, kdir, out, audio):
    cards=cards_of(kdir)
    ins=["-i",plate]+img(f"{KIT}/tarja.png")+img(f"{KIT}/bloco-grafico.png")
    for c in cards: ins+=img(f"{kdir}/{c['id']}.png")
    ins+=["-i",audio]; amap=3+len(cards)
    blo_y=H-sc(936); kar_y=blo_y+sc(1670-1596)
    f=[f"[0:v]scale={W}:{sc(2532)}:flags=lanczos,crop={W}:{H}:0:{sc(2532)-H},format=rgba[base]",
       f"[1:v]scale={W}:{sc(498)}:flags=lanczos,format=rgba[tar]",
       f"[2:v]scale={W}:{sc(936)}:flags=lanczos,format=rgba,"
       f"fade=t=in:st={438/30:.6f}:d={12/30:.6f}:alpha=1,fade=t=out:st={576/30:.6f}:d={12/30:.6f}:alpha=1[blo]",
       "[base][tar]overlay=0:0:enable='between(n,0,437)+between(n,589,659)'[v1]",
       f"[v1][blo]overlay=0:{blo_y}:enable='between(n,438,588)'[v2]"]
    prev="v2"
    for i,c in enumerate(cards):
        f.append(f"[{3+i}:v]scale={W}:{sc(220)}:flags=lanczos,format=rgba[c{i}]")
        f.append(f"[{prev}][c{i}]overlay=0:{kar_y}:enable='between(t,{c['ini']:.3f},{c['fim']:.3f})'[k{i}]")
        prev=f"k{i}"
    f.append(f"[{prev}]format=yuv420p[vout]")
    run(ins,f,out,amap)
    return dict(tarja=(0,sc(498)),bloco=(blo_y,H),karaoke=(kar_y,kar_y+sc(220)),crop_topo=sc(2532)-H)

# ---------- L1: rosto full-bleed + hook + painel screen no rodape + karaoke ----------
def l1(out):
    plate=f"{L3}/lipsync/rosto-lipsync.mp4"; master=f"{L3}/pecas/lote3-isabella-L1.mp4"
    cards=cards_of(f"{KIT}/karaoke")
    ins=["-i",plate]+img(f"{KIT}/hook-l1.png")+["-i",f"{L3}/blocos/screen.mp4"]
    for c in cards: ins+=img(f"{KIT}/{'karaoke'}/{c['id']}.png")
    ins+=["-i",master]; amap=3+len(cards)
    scr_h=sc(624); scr_y=H-scr_h; kar_y=scr_y+sc(2024-1908)
    f=[f"[0:v]scale={W}:{sc(2532)}:flags=lanczos,crop={W}:{H}:0:{sc(2532)-H},format=rgba[base]",
       f"[1:v]scale={W}:{sc(278)}:flags=lanczos,format=rgba[hk]",
       f"[2:v]scale={W}:{scr_h}:flags=lanczos,format=rgba[scr]",
       f"[base][hk]overlay=0:{sc(50)}[v1]",
       f"[v1][scr]overlay=0:{scr_y}[v2]"]
    prev="v2"
    for i,c in enumerate(cards):
        f.append(f"[{3+i}:v]scale={W}:{sc(220)}:flags=lanczos,format=rgba[c{i}]")
        f.append(f"[{prev}][c{i}]overlay=0:{kar_y}:enable='between(t,{c['ini']:.3f},{c['fim']:.3f})'[k{i}]")
        prev=f"k{i}"
    f.append(f"[{prev}]format=yuv420p[vout]")
    run(ins,f,out,amap)
    return dict(hook=(sc(50),sc(50)+sc(278)),screen=(scr_y,H),karaoke=(kar_y,kar_y+sc(220)))

# ---------- L2: screen | faixa | rosto | faixa | broll ----------
# rosto e as duas faixas INTACTOS; os dois paineis decorativos absorvem os 417px
def l2(out):
    plate=f"{L3}/lipsync/rosto-lipsync.mp4"; master=f"{L3}/pecas/lote3-isabella-L2.mp4"
    cards=cards_of(f"{KIT}/karaoke")
    SCR_H, FX, FACE_H, BRO_H = 430, sc(203), sc(961), 229
    y_scr=0; y_fx1=SCR_H; y_face=y_fx1+FX; y_fx2=y_face+FACE_H; y_bro=y_fx2+FX
    ins=["-i",master,"-i",plate]+img(f"{KIT}/faixa-l2-cima.png")+img(f"{KIT}/faixa-l2-baixo.png")
    for c in cards: ins+=img(f"{KIT}/karaoke/{c['id']}.png")
    amap=0
    kar_y=y_face+sc(1500-963)
    f=[f"color=c=black:s={W}x{H}:r=30:d=22,format=rgba[cv]",
       f"[0:v]crop=1170:760:0:0,scale={W}:{sc(760)}:flags=lanczos,crop={W}:{SCR_H}:0:0,format=rgba[scr]",
       f"[0:v]crop=1170:405:0:2127,scale={W}:{sc(405)}:flags=lanczos,crop={W}:{BRO_H}:0:0,format=rgba[bro]",
       f"[1:v]scale={W}:{sc(2532)}:flags=lanczos,crop={W}:{FACE_H}:0:{sc(501)},format=rgba[face]",
       f"[2:v]scale={W}:{FX}:flags=lanczos,format=rgba[f1]",
       f"[3:v]scale={W}:{FX}:flags=lanczos,format=rgba[f2]",
       f"[cv][scr]overlay=0:{y_scr}[a]", f"[a][f1]overlay=0:{y_fx1}[b]",
       f"[b][face]overlay=0:{y_face}[c]", f"[c][f2]overlay=0:{y_fx2}[d]",
       f"[d][bro]overlay=0:{y_bro}[e]"]
    prev="e"
    for i,c in enumerate(cards):
        f.append(f"[{4+i}:v]scale={W}:{sc(220)}:flags=lanczos,format=rgba[c{i}]")
        f.append(f"[{prev}][c{i}]overlay=0:{kar_y}:enable='between(t,{c['ini']:.3f},{c['fim']:.3f})'[k{i}]")
        prev=f"k{i}"
    f.append(f"[{prev}]format=yuv420p[vout]")
    run(ins,f,out,amap)
    return dict(screen=(0,SCR_H),faixa1=(y_fx1,y_fx1+FX),rosto=(y_face,y_face+FACE_H),
                faixa2=(y_fx2,y_fx2+FX),broll=(y_bro,y_bro+BRO_H),karaoke=(kar_y,kar_y+sc(220)))

# ---------- L4: broll | faixa | rosto ----------
def l4(out):
    plate=f"{L3}/lipsync/rosto-lipsync.mp4"; master=f"{L3}/pecas/lote3-isabella-L4.mp4"
    cards=cards_of(f"{KIT}/karaoke")
    BRO_H=sc(760); FX=sc(203); y_fx=BRO_H; y_face=y_fx+FX; FACE_H=H-y_face
    plate_bottom=sc(1950)                       # linha do plate que fecha o painel
    crop_y=plate_bottom-FACE_H
    kar_y=y_face+round((1442-(crop_y/S))*S)     # linha 1442 do plate = topo do karaoke original
    ins=["-i",master,"-i",plate]+img(f"{KIT}/faixa-l4.png")
    for c in cards: ins+=img(f"{KIT}/karaoke/{c['id']}.png")
    amap=0
    f=[f"color=c=black:s={W}x{H}:r=30:d=22,format=rgba[cv]",
       f"[0:v]crop=1170:760:0:0,scale={W}:{BRO_H}:flags=lanczos,format=rgba[bro]",
       f"[1:v]scale={W}:{sc(2532)}:flags=lanczos,crop={W}:{FACE_H}:0:{crop_y},format=rgba[face]",
       f"[2:v]scale={W}:{FX}:flags=lanczos,format=rgba[fx]",
       f"[cv][bro]overlay=0:0[a]", f"[a][fx]overlay=0:{y_fx}[b]", f"[b][face]overlay=0:{y_face}[c]"]
    prev="c"
    for i,cc in enumerate(cards):
        f.append(f"[{3+i}:v]scale={W}:{sc(220)}:flags=lanczos,format=rgba[c{i}]")
        f.append(f"[{prev}][c{i}]overlay=0:{kar_y}:enable='between(t,{cc['ini']:.3f},{cc['fim']:.3f})'[k{i}]")
        prev=f"k{i}"
    f.append(f"[{prev}]format=yuv420p[vout]")
    run(ins,f,out,amap)
    return dict(broll=(0,BRO_H),faixa=(y_fx,y_fx+FX),rosto=(y_face,H),karaoke=(kar_y,kar_y+sc(220)))
