#!/usr/bin/env python3
# Podcast WPP clone, montagem v2 (21/09) — corrige o que o Gusta reprovou nas 91–100: (1) rosto cortado: o recorte da janela era fixo,
# calibrado nos avatares de 13/09; agora o recorte é CENTRADO NO ROSTO de cada clipe (detector YuNet nos 2 primeiros s, mesma altura
# relativa do original: 295/587); (2) "piscava avatares anteriores": o two-shot de 0,5 s mostrava duas mulheres diferentes dos closes —
# substituído por um close A cobrindo 0–2,77 s (bloco-12b); timing por tpad (o setpts deslizava). Faixa, karaokê, painéis, b-roll e
# áudio: do original, intocados. Uso (de projects/mentoria-spy/): CLIPES=<pasta> python3 montar-clone-v2.py <saida.mp4>
import os, subprocess, sys, numpy as np
P='centerpag-detect/criativos/podcast-wpp-clone-avatares-2026-09-13'; REF=f'{P}/REFERENCIA-original-41s.mp4'
CL=os.environ['CLIPES']; OUT=sys.argv[1]; FPS=30; WX,WY,WW,WH=0,347,720,587; ALVO=295/587   # centro do rosto (YuNet) na janela do original: y≈295 de 587
CH=int(round(704*WH/WW))   # 574: recorte na largura inteira do clipe 704x1280, mesma proporção da janela
M='gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'   # detector de rosto (OpenCV YuNet); a heurística de pele confundia parede e colo com rosto
def centro_rosto(clip,t=2.0,fps=4):
    import cv2
    w,h=704,1280
    raw=subprocess.run(['ffmpeg','-hide_banner','-v','error','-t',str(t),'-i',clip,'-vf',f'fps={fps},scale={w}:{h}','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    n=len(raw)//(w*h*3); fr=np.frombuffer(raw[:n*w*h*3],np.uint8).reshape(n,h,w,3)
    det=cv2.FaceDetectorYN_create(M,'',(w,h),0.6,0.3,5000); cs=[]
    for f in fr:
        _,d=det.detect(np.ascontiguousarray(f))
        if d is not None and len(d): x,y,ww,hh=max(d,key=lambda r:r[2]*r[3])[:4]; cs.append(y+hh/2)
    return float(np.median(cs)) if cs else 560.0
def crop_y(clip):
    cy=centro_rosto(clip); y=int(round(cy-ALVO*CH)); return max(0,min(1280-CH,y))
# (início, fim no original, clipe, padding inicial clone em s)
BLOCOS=[(0.0,2.767,f'{CL}/bloco-12b.mp4',0),(4.25,11.75,f'{CL}/bloco-3b.mp4',0),(11.75,16.5,f'{CL}/bloco-4b.mp4',0),(37.3,41.3,f'{CL}/bloco-5b.mp4',0.2)]
inputs=['-i',REF]; fc=[]; cur='[0:v]'
for i,(ini,fim,clip,pad) in enumerate(BLOCOS):
    y=crop_y(clip); n=i+1; inputs+=['-i',clip]
    fc.append(f"[{n}:v]trim=start_frame=1,setpts=PTS-STARTPTS,fps={FPS},crop=704:{CH}:0:{y},scale={WW}:{WH}:flags=lanczos,"
              +(f"tpad=start_mode=clone:start_duration={pad},"  if pad else "")
              +f"tpad=stop_mode=clone:stop_duration=1,trim=end={fim-ini:.4f},setpts=PTS-STARTPTS,format=rgba,"
              f"tpad=start_mode=add:start_duration={ini:.4f}:color=0x00000000[c{n}];")
    fc.append(f"{cur}[c{n}]overlay=x={WX}:y={WY}:eof_action=pass:enable='between(t,{ini:.4f},{fim-1e-4:.4f})'[v{n}];"); cur=f'[v{n}]'
    print(f'  bloco {n}: {os.path.basename(clip)} crop y={y}')
fc[-1]=fc[-1].replace(cur,'[v]')
cmd=['ffmpeg','-hide_banner','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','0:a','-c:a','copy',
     '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT]
open(os.path.join(CL,'ultimo-comando-v2.txt'),'w').write(' '.join(cmd)); subprocess.run(cmd,check=True); print('ok ->',OUT)
