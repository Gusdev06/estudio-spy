#!/usr/bin/env python3
# Clone do talking head WhatsApp "HOW TO SEE YOUR PARTNER'S MESSAGES ON YOUR OWN PHONE" com avatar indiano novo.
# Layout de post sobre fundo preto: faixa de título (y 113-199), JANELA DE VÍDEO 708x674 (y 298-971) e karaokê (y ~1028-1154).
# Só a janela muda, e só enquanto o homem está em quadro (frames 0-951). O b-roll final, a faixa, o karaokê e o áudio são os
# do original. O "estouro" branco do original (frames 647-790, alpha 0,851 medido) é reaplicado sobre o avatar para não
# desfazer a edição. Uso (de projects/mentoria-spy/):  python3 .../montar-indiano.py <clipe.mp4> <saida.mp4>
import os, subprocess, sys
P='centerpag-detect/criativos/talkinghead-wpp-indianos-2026-09-13'
REF=f'{P}/REFERENCIA-original.mp4'
CLIPE=sys.argv[1] if len(sys.argv)>1 else f'{P}/clipes/i1.mp4'
OUT=sys.argv[2] if len(sys.argv)>2 else f'{P}/TALKINGHEAD-WPP-i1.mp4'
WIN=dict(x=0,y=298,w=708,h=674)      # janela de vídeo no frame 708x1274
CROP=os.environ.get('CROP','704:670:0:380')   # recorte do Pruna (704x1280) que reproduz o enquadramento do original
FPS=30
ROSTO_FIM=952        # frame em que o b-roll final entra (corte de cena medido em 31,73 s)
LAV_INI,LAV_FIM=652,790   # estouro branco com alpha constante 0,851 (o fade de 5 frames, 647-651, fica o do original)
ALPHA=0.851
g=1-ALPHA; off=round(255*ALPHA,1)    # out = in*(1-a) + 255*a
fc=[]
# avatar recortado para a janela, em duas versões: normal e "estourada"
fc.append(f"[1:v]crop={CROP},scale={WIN['w']}:{WIN['h']}:flags=lanczos,fps={FPS},format=yuv420p,split=2[av][avl];")
fc.append(f"[avl]lutrgb=r='val*{g:.3f}+{off}':g='val*{g:.3f}+{off}':b='val*{g:.3f}+{off}'[avlav];")
# avatar normal onde o original está normal; avatar estourado onde o original está estourado
fc.append(f"[0:v][av]overlay=x={WIN['x']}:y={WIN['y']}:eof_action=pass:"
          f"enable='between(n,0,{LAV_INI-1})+between(n,{LAV_FIM+1},{ROSTO_FIM-1})'[v1];")
fc.append(f"[v1][avlav]overlay=x={WIN['x']}:y={WIN['y']}:eof_action=pass:"
          f"enable='between(n,{LAV_INI},{LAV_FIM})'[v]")
cmd=['ffmpeg','-hide_banner','-v','error','-y','-i',REF,'-i',CLIPE,'-filter_complex',''.join(fc),
 '-map','[v]','-map','0:a','-c:a','copy',
 '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p',
 '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',
 '-movflags','+faststart',OUT]
open(f'{P}/conferencia/ultimo-comando.txt','w').write(' '.join(cmd))
subprocess.run(cmd,check=True)
print('ok ->',OUT)
