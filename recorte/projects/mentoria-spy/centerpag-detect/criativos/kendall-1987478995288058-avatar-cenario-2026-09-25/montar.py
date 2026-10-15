#!/usr/bin/env python3
# Kendall 1987478995288058 (Zap, 20,2 s) com avatar E cenário novos (25/09). Do original, intocados: áudio, faixa amarela (y 549-704, 0-7,83 s),
# funil sob a faixa (2,67-7,83), painéis (7,83-15,07) e CTA (16,0-20,2). O rosto aparece em 3 enquadramentos, reproduzidos pelo rosto medido no
# original (centro x,y e altura, YuNet): A 0-2,67 tela cheia (357,292,h214) · B 2,67-7,83 só y 0-549 (360,180,h172) · C 15,07-16,0 tela cheia sem
# faixa (356,353,h180). Escala = h alvo / h do rosto no clipe (mín. o que cobre 720x1254). Uso (de projects/mentoria-spy/): python3 .../montar.py k1 <saida.mp4>
import json, subprocess, sys, numpy as np, cv2
L='centerpag-detect/criativos/kendall-1987478995288058-avatar-cenario-2026-09-25'; REF=f'{L}/REFERENCIA-original.mp4'
M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'; k,OUT=sys.argv[1],sys.argv[2]; W,H,FPS=720,1254,30
def rosto(clip,ss,t):
    raw=subprocess.run(['ffmpeg','-v','error','-ss',str(ss),'-t',str(t),'-i',clip,'-vf','fps=6','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    f=np.frombuffer(raw,np.uint8).reshape(-1,1280,704,3); det=cv2.FaceDetectorYN_create(M,'',(704,1280),0.86,0.3,5000); r=[]
    for x in f:
        d=det.detect(np.ascontiguousarray(x))[1]
        if d is not None and len(d): a=max(d,key=lambda q:q[-1]); r.append((a[0]+a[2]/2,a[1]+a[3]/2,a[3]))
    return np.median(np.array(r),axis=0)
def enquadra(clip,ss,t,tx,ty,th,ch):
    cx,cy,h=rosto(clip,ss,t); s=max(th/h,W/704,H/1280); sw,sh=int(round(704*s/2))*2,int(round(1280*s/2))*2
    x=int(min(max(cx*s-tx,0),sw-W)); y=int(min(max(cy*s-ty,0),sh-ch)); return f'scale={sw}:{sh}:flags=lanczos,crop={W}:{ch}:{x}:{y}',s
c1,c2=f'{L}/{k}/clipes/c1.mp4',f'{L}/{k}/clipes/c2.mp4'
fa,sa=enquadra(c1,0,2.6,357,292,214,H); fd,sd=enquadra(c1,0,2.6,356,353,180,H); fb,sb=enquadra(c1,2.7,5,360,180,172,549); fc_,sc=enquadra(c2,1.0,1.0,356,353,180,H)
print(f'{k}: escala A {sa:.3f} · B {sb:.3f} · C {sc:.3f}')
def trecho(n,ss,dur,filtro,ini,tag):   # pega do clipe [ss, ss+dur) e posiciona em t=ini
    return (f"[{n}:v]trim=start_frame=1,setpts=PTS-STARTPTS,fps={FPS},trim=start={ss:.4f}:end={ss+dur:.4f},setpts=PTS-STARTPTS,{filtro},"
            f"tpad=stop_mode=clone:stop_duration=1,trim=end={dur:.4f},setpts=PTS-STARTPTS,format=rgba,tpad=start_mode=add:start_duration={ini:.4f}:color=0x00000000[{tag}];")
# Emendas por NÚMERO DE FRAME (25/09, Gusta: "piscando o avatar anterior"): em segundos arredondados sobravam 7 frames do rosto original
# (n 80 no buraco entre A e B; n 235-239 porque a mulher vai até 8,00 s e não até o corte de 7,83; n 452 antes do C). Rosto no original: n 0-239 e 452-479.
A0,A1,B0,B1,C0,C1=0,79,80,239,452,479
# Painéis (n 240-451): o fundo em volta do celular era a mulher original desfocada (plano aberto, gaussiano σ≈12, ganho 1,0; medido contra o n 452).
# Agora: avatar nova no plano aberto, mesmo desfoque, e o celular do original por cima via máscara fixa (molde/mascara-celular.png, x 49-670, y 76-1177).
D0,D1=240,451
fc=["[0:v]split=3[o][of][ocel];[of]crop=720:156:0:549[faixa];[4:v]format=gray[mk];[ocel][mk]alphamerge[cel];",
    trecho(3,0,(D1-D0+1)/FPS,fd+',gblur=sigma=12',D0/FPS,'d'),
    trecho(1,A0/FPS,(A1-A0+1)/FPS,fa,A0/FPS,'a'), trecho(1,B0/FPS,(B1-B0+1)/FPS,fb,B0/FPS,'b'), trecho(2,1.0,(C1-C0+1)/FPS,fc_,C0/FPS,'c'),
    f"[o][a]overlay=0:0:eof_action=pass:enable='between(n,{A0},{A1})'[v1];",
    f"[v1][b]overlay=0:0:eof_action=pass:enable='between(n,{B0},{B1})'[v2];",
    f"[v2][faixa]overlay=0:549:enable='between(n,{A0},{B1})'[v3];",
    f"[v3][c]overlay=0:0:eof_action=pass:enable='between(n,{C0},{C1})'[v4];",
    f"[v4][d]overlay=0:0:eof_action=pass:enable='between(n,{D0},{D1})'[v5];",
    f"[v5][cel]overlay=0:0:enable='between(n,{D0},{D1})'[v]"]
cmd=['ffmpeg','-hide_banner','-v','error','-y','-i',REF,'-i',c1,'-i',c2,'-i',c1,'-loop','1','-i',f'{L}/molde/mascara-celular.png','-filter_complex',''.join(fc),'-map','[v]','-map','0:a','-c:a','copy','-frames:v','602',
     '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT]
subprocess.run(cmd,check=True); print('ok ->',OUT)
