#!/usr/bin/env python3
# Clone do podcast Gram ("HOW TO ACCESS YOUR PARTNER'S INSTAGRAM FROM YOUR PHONE", 52,1 s) com avatares novos (24/09).
# Do original, intocados: áudio, faixa de título (y 101-245), legenda (sobre preto, y 1063-1135), painéis do Gram Detect (18,27-37,47) e CTA (44,1-52,1).
# Só a janela de vídeo (720x812 em y 250) muda nos 4 blocos de rosto. Clipe Pruna 896x1024 -> 720x823 -> corta 812 no meio (mesmo
# enquadramento da imagem-base, que é edit do próprio frame da janela). Uso (de projects/mentoria-spy/): python3 .../montar.py <elenco> <saida.mp4>
import json, subprocess, sys
L='gram-detect/criativos/podcast-gram-clone-avatares-2026-09-24'; REF=f'{L}/REFERENCIA-original.mp4'
k,OUT=sys.argv[1],sys.argv[2]; FPS=30; WY,WW,WH=250,720,812
B=json.load(open(f'{L}/molde/blocos.json')); inputs=['-i',REF]; fc=[]; cur='[0:v]'
for n,(b,d) in enumerate(B.items(),1):
    ini,fim=d['ini'],d['fim']; inputs+=['-i',f'{L}/{k}/clipes/{b}.mp4']
    fc.append(f"[{n}:v]trim=start_frame=1,setpts=PTS-STARTPTS,fps={FPS},scale={WW}:823:flags=lanczos,crop={WW}:{WH}:0:5,"
              f"tpad=stop_mode=clone:stop_duration=1,trim=end={fim-ini:.4f},setpts=PTS-STARTPTS,format=rgba,"
              f"tpad=start_mode=add:start_duration={ini:.4f}:color=0x00000000[c{n}];")
    fc.append(f"{cur}[c{n}]overlay=x=0:y={WY}:eof_action=pass:enable='between(t,{ini:.4f},{fim-1e-4:.4f})'[v{n}];"); cur=f'[v{n}]'
fc[-1]=fc[-1].replace(cur,'[v]')
cmd=['ffmpeg','-hide_banner','-v','error','-y']+inputs+['-filter_complex',''.join(fc),'-map','[v]','-map','0:a','-c:a','copy',
     '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv','-movflags','+faststart',OUT]
subprocess.run(cmd,check=True); print('ok ->',OUT)
