"""Compose the approved generated avatar, preserving source hook, tail and audio."""
from pathlib import Path
import json
import subprocess

import sys
batch=Path(__file__).resolve().parent
control=batch.parent/"nutra-2646108219158542-avatar-2026-09-24"
root=batch/sys.argv[1]
source=control.parents[2]/'downloads/ad-2646108219158542-2026-09-24/nutra-health-2646108219158542-v1.mp4'
avatar=root/'avatar-animado.mp4'
output=root/'master-sem-perdas.mp4'
if not avatar.exists():
    raise SystemExit('Falta avatar-animado.mp4: requer aprovação e geração paga.')
meta=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(avatar)]))
if float(meta['format']['duration']) < 35.6:
    raise SystemExit('Avatar gerado está curto: verificar job antes da montagem.')
filters=(
    '[0:v]split=2[hooksrc][tailsrc];'
    '[hooksrc]trim=end_frame=220,setpts=PTS-STARTPTS,setsar=1[hook];'
    '[tailsrc]trim=start_frame=1290,setpts=PTS-STARTPTS,setsar=1[tail];'
    '[1:v]fps=30,scale=360:640:flags=lanczos,setsar=1,'
    'tpad=stop_mode=clone:stop_duration=0.1,trim=end_frame=1070,setpts=PTS-STARTPTS,'
    'fade=t=in:start_frame=0:nb_frames=7[face];'
    '[2:v]setpts=PTS-STARTPTS[art];'
    '[face][art]overlay=shortest=1:format=auto,format=yuv420p[middle];'
    '[hook][middle][tail]concat=n=3:v=1:a=0,format=yuv420p[out]'
)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(source),'-i',str(avatar),'-i',str(control/'preparo/legendas-alpha.mov'),
    '-filter_complex',filters,'-map','[out]','-map','0:a:0','-c:v','libx264','-preset','medium','-crf','0',
    '-c:a','copy','-movflags','+faststart',str(output)],check=True)
delivery=root/(root.name+'-nutra-2646108219158542.mp4')
subprocess.run(['ffmpeg','-v','error','-y','-i',str(output),'-map','0:v:0','-map','0:a:0',
    '-c:v','libx264','-preset','slow','-crf','16','-profile:v','high','-pix_fmt','yuv420p',
    '-c:a','copy','-movflags','+faststart',str(delivery)],check=True)
print(delivery)
