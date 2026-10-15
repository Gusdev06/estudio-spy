#!/usr/bin/env python3
# Conserto das peças montadas antes do 2º passo do montar.py: troca o áudio truncado pelo áudio-fonte inteiro (vídeo copiado, sync em t=0 preservado).
# Uso (de projects/mentoria-spy/): python3 remux-audio.py v164 v165 …
import sys,os,json,subprocess,glob
L=os.path.dirname(os.path.abspath(sys.argv[0])); C=json.load(open(f'{L}/copys.json'))
for v in sys.argv[1:]:
    p=glob.glob(f'{L}/pecas/{v[1:]}-ZAP-secret-*.mp4')[0]; aud=f'{L}/audio/{v}-ritmo.mp3'; tmp=p[:-4]+'.remux.mp4'
    dv=float(subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
    subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-i',p,'-i',aud,'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-t',f'{dv:.3f}','-movflags','+faststart',tmp],check=True); os.replace(tmp,p)
    da=float(subprocess.run(['ffprobe','-v','error','-select_streams','a','-show_entries','stream=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
    print(f'{os.path.basename(p)}: vídeo {dv:.2f}s · áudio {da:.2f}s')
