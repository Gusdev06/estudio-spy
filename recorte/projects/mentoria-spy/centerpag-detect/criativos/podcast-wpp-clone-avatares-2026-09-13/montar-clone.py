#!/usr/bin/env python3
# Clone do podcast WhatsApp "HOW TO READ YOUR PARTNER'S MESSAGES ON YOUR OWN PHONE" com avatares novos.
# O original é um layout de post sobre fundo preto: faixa de título (y 139-271), JANELA DE VÍDEO 720x587 (y 347-933)
# e karaokê queimado (y ~944-1055). Só a JANELA muda, e só nos blocos de rosto — faixa, karaokê, painéis, b-roll e
# áudio são os do original, intocados. Uso (de projects/mentoria-spy/): python3 .../montar-clone.py [saida.mp4]
import json, os, subprocess, sys
P='centerpag-detect/criativos/podcast-wpp-clone-avatares-2026-09-13'
REF=f'{P}/REFERENCIA-original-41s.mp4'
OUT=sys.argv[1] if len(sys.argv)>1 else f'{P}/PODCAST-WPP-avatares-novos.mp4'
CL=os.environ.get('CLIPES',f'{P}/clipes')   # variação: pasta com bloco-{1..5}b.mp4 próprios
WIN=dict(x=0,y=347,w=720,h=587)      # janela de vídeo dentro do frame 720x1280 (medida no original)
FPS=30
# bloco: (início no original, fim no original, clipe, crop no clipe 704x1280 como w:h:x:y)
# o áudio de cada clipe começa no início do bloco, então o offset dentro do clipe é 0
BLOCOS=[
 (0.00, 0.50, f'{CL}/bloco-1b.mp4', '704:574:0:430'),   # two-shot, as duas
 (0.50, 2.75, f'{CL}/bloco-2b.mp4', '650:530:42:467'),  # close A
 (4.25,11.75, f'{CL}/bloco-3b.mp4', '704:574:0:440'),   # close B
 (11.75,16.50,f'{CL}/bloco-4b.mp4', '650:530:42:467'),  # close A
 (37.50,41.25,f'{CL}/bloco-5b.mp4', '650:530:42:467'),  # close A
]
inputs=['-i',REF]; fc=[]; cur='[0:v]'
for i,(ini,fim,clip,crop) in enumerate(BLOCOS):
    inputs+=['-i',clip]; n=i+1; dur=fim-ini
    # recorta a faixa do clipe, escala pra janela, corta na duração do bloco e atrasa até o instante certo
    fc.append(f"[{n}:v]crop={crop},scale={WIN['w']}:{WIN['h']}:flags=lanczos,fps={FPS},"
              f"trim=start=0:end={dur:.4f},setpts=PTS-STARTPTS+{ini:.4f}/TB,format=yuv420p[c{n}];")
    prox=f'[v{n}]'
    fc.append(f"{cur}[c{n}]overlay=x={WIN['x']}:y={WIN['y']}:eof_action=pass:"
              f"enable='between(t,{ini:.4f},{fim-1e-4:.4f})'{prox};")
    cur=prox
fc[-1]=fc[-1].replace(cur,'[v]')
cmd=['ffmpeg','-hide_banner','-v','error','-y']+inputs+['-filter_complex',''.join(fc),
 '-map','[v]','-map','0:a','-c:a','copy',
 '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p',
 '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',
 '-movflags','+faststart',OUT]
os.makedirs(f'{P}/molde',exist_ok=True); open(os.path.join(CL,'ultimo-comando.txt'),'w').write(' '.join(cmd))
subprocess.run(cmd,check=True)
print('ok ->',OUT)
