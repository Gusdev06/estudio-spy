#!/usr/bin/env python3
# Confere as peças contra a mãe. Uso (de projects/mentoria-spy/): python3 conferir.py [nº…]
# Por peça: decodifica inteira sem erro · 1080x1920 30 fps · |áudio − vídeo| < 0,35 s · md5 do stream de áudio = mãe ·
# PSNR da região abaixo da faixa (y 420–1920: avatar + karaokê) contra a mãe, frame a frame · resto de vermelho da faixa fora da faixa nova ·
# e a folha conferencia/final-15.jpg (frame em 0,5 s de cada peça, faixa inteira visível).
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
L=os.path.dirname(os.path.abspath(sys.argv[0])); H=json.load(open(f'{L}/headlines.json'))
MAE={'77':'CRIATIVOS-PRONTOS/77-ZAP-secret-revealed-filipino-jovem-moletom.mp4','112':'CRIATIVOS-PRONTOS/112-ZAP-secret-hook-ela-te-trai-voce-nao-quer-ver.mp4','121':'CRIATIVOS-PRONTOS/121-ZAP-secret-hook-ela-disse-que-e-amiga.mp4'}
run=lambda c: subprocess.run(c,capture_output=True,text=True)
probe=lambda f,*a: run(['ffprobe','-v','error',*a,'-of','csv=p=0',f]).stdout.strip()
md5=lambda f,s: run(['ffmpeg','-nostdin','-v','error','-i',f,'-map',f'0:{s}','-c','copy','-f','md5','-']).stdout.strip()
def frame(f,t):
    d=subprocess.run(['ffmpeg','-nostdin','-v','error','-ss',str(t),'-i',f,'-frames:v','1','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    return np.frombuffer(d,np.uint8).reshape(1920,1080,3)
ids=sys.argv[1:] or sorted(H); ok_all=True; rows=[]; thumbs=[]
for k in ids:
    v=H[k]; f=f'{L}/pecas/{k}-ZAP-secret-{v["slug"]}.mp4'; m=MAE[v['mae']]; prob=[]
    err=run(['ffmpeg','-nostdin','-v','error','-i',f,'-f','null','-']).stderr.strip()
    if err: prob.append('erro ao decodificar: '+err[:120])
    w,h,r=probe(f,'-select_streams','v','-show_entries','stream=width,height,r_frame_rate').split(',')
    if (w,h,r)!=('1080','1920','30/1'): prob.append(f'formato {w}x{h} {r}')
    nf=int(probe(f,'-select_streams','v','-count_frames','-show_entries','stream=nb_read_frames')); nfm=int(probe(m,'-select_streams','v','-count_frames','-show_entries','stream=nb_read_frames'))
    dv=float(probe(f,'-select_streams','v','-show_entries','stream=duration')); da=float(probe(f,'-select_streams','a','-show_entries','stream=duration'))
    if nf!=nfm: prob.append(f'{nf} frames ≠ mãe {nfm}')
    if abs(dv-da)>=0.35: prob.append(f'áudio {da:.2f} × vídeo {dv:.2f}')
    am=md5(f,'a')==md5(m,'a')
    if not am: prob.append('áudio ≠ mãe')
    # avatar + karaokê (abaixo da faixa) contra a mãe, todos os frames
    ps=run(['ffmpeg','-nostdin','-hide_banner','-i',f,'-i',m,'-lavfi','[0:v]crop=1080:1500:0:420[a];[1:v]crop=1080:1500:0:420[b];[a][b]psnr=stats_file=-','-f','null','-']).stdout
    vals=[float(x.split(':')[1].replace('inf','99')) for x in ps.split() if x.startswith('psnr_avg:')]
    pmin,pmed=min(vals),sum(vals)/len(vals)
    if len(vals)!=nfm or pmin<40: prob.append(f'abaixo da faixa: psnr min {pmin:.1f} em {len(vals)} fr')
    # resto de faixa antiga: vermelho saturado na região da faixa (y 90–420) onde a faixa nova é transparente, em 5 instantes
    alpha=np.asarray(Image.open(f'{L}/molde/selo-{k}.png'))[...,3]>0; resto=0
    for t in (0.5,dv*0.25,dv*0.5,dv*0.75,dv-0.5):
        a=frame(f,t).astype(int)[90:420]; red=(a[...,0]>150)&(a[...,1]<70)&(a[...,2]<70)&~alpha[90:420]; resto=max(resto,int(red.sum()))
    if resto>200: prob.append(f'{resto} px vermelhos fora da faixa nova')
    ok=not prob; ok_all&=ok
    rows.append(f'| {k} | mãe {v["mae"]} | {nf} fr | vídeo {dv:.2f} s · áudio {da:.2f} s | áudio md5 = mãe: {"sim" if am else "NÃO"} | avatar+karaokê psnr méd {pmed:.1f} / mín {pmin:.1f} dB | resto vermelho {resto} px | {"OK" if ok else "; ".join(prob)} |')
    print(rows[-1],flush=True)
    im=Image.fromarray(frame(f,0.5)).resize((270,480),Image.LANCZOS); d=ImageDraw.Draw(im); d.rectangle([0,452,270,480],fill=(0,0,0)); d.text((6,457),f'{k} · mãe CP{v["mae"]}',fill=(255,255,255),font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',18)); thumbs.append(im)
if len(ids)==len(H):
    sh=Image.new('RGB',(270*5,480*3),'white')
    for i,t in enumerate(thumbs): sh.paste(t,((i%5)*270,(i//5)*480))
    os.makedirs(f'{L}/conferencia',exist_ok=True); sh.save(f'{L}/conferencia/final-15.jpg',quality=90)
    open(f'{L}/conferencia/conferencia.md','w').write('| nº | mãe | frames | duração | áudio | abaixo da faixa × mãe | resto da faixa antiga | resultado |\n|---|---|---|---|---|---|---|---|\n'+'\n'.join(rows)+'\n')
print('TUDO OK' if ok_all else 'HÁ PROBLEMAS')
