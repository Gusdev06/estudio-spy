#!/usr/bin/env python3
# Confere cada clipe baixado (ffprobe acusa "partial file" quando o download foi cortado) e rebaixa da URL do out.json com curl.
import json, glob, subprocess, sys, os
def partial(f):
    r=subprocess.run(['ffmpeg','-v','error','-i',f,'-f','null','-'],capture_output=True,text=True); return bool(r.stderr.strip())
pats=sys.argv[1:]
for pat in pats:
    for oj in sorted(glob.glob(pat)):
        mp4=oj.replace('.out.json','.mp4')
        if os.path.exists(mp4) and not partial(mp4): continue
        try: url=json.load(open(oj))['outputs'][0]
        except Exception as e: print('sem url',oj); continue
        subprocess.run(['curl','-sL','--retry','3','-o',mp4,url],check=True)
        print(('REBAIXADO ' if not partial(mp4) else 'AINDA PARCIAL ')+mp4, os.path.getsize(mp4))
