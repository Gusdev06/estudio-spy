#!/usr/bin/env python3
# Clone do podcast WPP 57 s com COPY NOVA e AVATARES NOVOS (23/09). Tudo reconstruído sobre o molde medido do original:
#   título (y 130-275) ..... estático, recortado do original (fica sobre preto, sem fundo por trás)
#   janela (y 346, 720x587)  blocos de rosto = clipes Pruna dos 2 avatares novos (recorte centrado no rosto, YuNet);
#                            blocos de painel = trechos do funil do próprio original, reencaixados na nova timeline
#   karaokê (y 935) ........ redesenhado palavra a palavra no estilo medido (branco + caixa roxa 105,18,209)
#   CTA final .............. os 15,4 s de b-roll+setas do original, em quadro cheio, com a trilha dele
#   áudio .................. locução nova (2 vozes MiniMax) + cama de música do próprio original por baixo
# Uso (de projects/mentoria-spy/): python3 .../montar.py <saida.mp4>
import json, os, subprocess, sys, numpy as np, cv2
# 07/10: versão das peças 170/171 — copy e timeline por peça (molde/<k>), clipes em c<k>/clipes. Uso: montar.py <k> <saida.mp4>
P='centerpag-detect/criativos/podcast-wpp-cp108-avatar-copy-2026-10-07'; REF='centerpag-detect/criativos/podcast-wpp-57s-copy-nova-2026-09-23/REFERENCIA-original.mp4'
K=sys.argv[1]; OUT=sys.argv[2]
CL=f'{P}/c{K}/clipes'
FPS=30; W,H=720,1280; WX,WY,WW,WH=0,346,720,587; M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
ALVO=295/587   # altura relativa do rosto na janela, medida no original
tl={l['i']:l for l in json.load(open(f'{P}/molde/{K}/linhas.json'))}
CTA=tl[9]['ini']                      # o b-roll de CTA entra na última fala
FIM=CTA+15.4                          # + os 15,4 s de cauda do original
# (linha, fonte) — clipe de rosto ou trecho de painel do original (ss no original)
BLOCOS=[(1,('clipe',f'{CL}/b1.mp4')),(2,('painel',16.45)),(3,('clipe',f'{CL}/b3.mp4')),
        (4,('clipe',f'{CL}/b4.mp4')),(5,('clipe',f'{CL}/b5.mp4')),(6,('clipe',f'{CL}/b6.mp4')),
        (7,('painel',22.0)),(8,('clipe',f'{CL}/b8.mp4'))]
def recorte(clip):
    """Recorte da janela (720x587) centrado no rosto detectado, respeitando a orientação real do clipe."""
    cw,ch=[int(x) for x in subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',clip],capture_output=True,text=True).stdout.strip().split(',')]
    raw=subprocess.run(['ffmpeg','-hide_banner','-v','error','-t','2','-i',clip,'-vf','fps=4','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    n=len(raw)//(cw*ch*3); fr=np.frombuffer(raw[:n*cw*ch*3],np.uint8).reshape(n,ch,cw,3)
    det=cv2.FaceDetectorYN_create(M,'',(cw,ch),0.6,0.3,5000); cx=[];cy=[]
    for f in fr:
        _,d=det.detect(np.ascontiguousarray(f))
        if d is not None and len(d):
            x,y,ww,hh=max(d,key=lambda r:r[-1])[:4]; cx.append(x+ww/2); cy.append(y+hh/2)   # mais confiável, não o maior: o YuNet acha 'rosto' nas plantas (score ~0,65, caixa maior) — var6 x3/x5, 24/09
    fx=float(np.median(cx)) if cx else cw/2; fy=float(np.median(cy)) if cy else ch*0.45
    # maior recorte 720:587 que cabe no clipe
    rw=min(cw,int(round(ch*WW/WH))); rh=int(round(rw*WH/WW))
    if rh>ch: rh=ch; rw=int(round(rh*WW/WH))
    x=max(0,min(cw-rw,int(round(fx-rw/2)))); y=max(0,min(ch-rh,int(round(fy-ALVO*rh))))
    print('recorte',os.path.basename(clip),f'{rw}:{rh}:{x}:{y}',flush=True); return f'{rw//2*2}:{rh//2*2}:{x}:{y}'
inputs=['-i',REF,'-framerate',str(FPS),'-start_number','0','-i',f'{P}/c{K}/karaoke/frames/%04d.png','-i',f'{P}/audio/{K}/vo.wav']
fc=[f"color=c=black:s={W}x{H}:r={FPS}:d={FIM+0.5:.2f}[base];",
    f"[0:v]trim=start=6:end=6.04,setpts=PTS-STARTPTS,crop={W}:145:0:130,loop=loop=-1:size=1,fps={FPS},format=rgba[tit];",
    f"[base][tit]overlay=0:130:eof_action=pass:enable='lt(t,{CTA:.3f})'[v0];"]
cur='[v0]'; n=3
for li,(tipo,src) in BLOCOS:
    ini=tl[li]['ini']; fim=(tl[li+1]['ini'] if li+1 in tl else CTA)   # cobre a pausa até a próxima linha
    dur=fim-ini
    if tipo=='clipe':
        cr=recorte(src); inputs+=['-i',src]
        fc.append(f"[{n}:v]fps={FPS},crop={cr},scale={WW}:{WH}:flags=lanczos,trim=start_frame=1,setpts=PTS-STARTPTS,"
                  f"tpad=stop_mode=clone:stop_duration=2,trim=end={dur:.3f},setpts=PTS-STARTPTS,format=rgba,tpad=start_mode=add:start_duration={ini:.3f}:color=0x00000000[b{li}];")
    else:
        inputs+=['-ss',str(src),'-t',f'{dur+0.5:.3f}','-i',REF]
        fc.append(f"[{n}:v]fps={FPS},crop={WW}:{WH}:{WX}:{WY},trim=end={dur:.3f},setpts=PTS-STARTPTS,format=rgba,tpad=start_mode=add:start_duration={ini:.3f}:color=0x00000000[b{li}];")
    fc.append(f"{cur}[b{li}]overlay={WX}:{WY}:eof_action=pass:enable='between(t,{ini:.3f},{fim-0.001:.3f})'[w{li}];"); cur=f'[w{li}]'; n+=1
fc.append(f"[1:v]format=rgba[kar];{cur}[kar]overlay=0:935:eof_action=pass:enable='lt(t,{CTA:.3f})'[vk];")
inputs+=['-ss','41.4','-t','15.4','-i',REF]
fc.append(f"[{n}:v]fps={FPS},scale={W}:{H},format=rgba,tpad=start_mode=add:start_duration={CTA:.3f}:color=0x00000000[cta];[vk][cta]overlay=0:0:eof_action=pass:enable='gte(t,{CTA:.3f})'[v];")
# áudio: voz nova + cama de música do original (cauda sem fala), e a trilha da cauda no CTA
# a locução do MiniMax sai ~6 dB abaixo da mistura do original (-23,5 vs -17,6): normaliza a voz e põe a cama por baixo
fc.append(f"[2:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,loudnorm=I=-16:TP=-1.5:LRA=11,apad=whole_dur={FIM:.3f}[voz];"
          f"[{n}:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,aloop=loop=-1:size=2e6,atrim=0:{FIM:.3f},asetpts=PTS-STARTPTS,volume=0.55[cama];"
          f"[voz][cama]amix=inputs=2:duration=first:dropout_transition=0:weights='1 0.55':normalize=0[a]")
cmd=['ffmpeg','-hide_banner','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','[a]','-c:a','aac','-b:a','192k',
     '-t',f'{FIM:.3f}','-c:v','libx264','-preset','slow','-crf','18','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT]
open(f'{P}/c{K}/comando-montagem.txt','w').write(' '.join(cmd)); subprocess.run(cmd,check=True); print('ok ->',OUT,f'· {FIM:.1f}s')
