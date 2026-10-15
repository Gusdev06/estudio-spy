import sys,subprocess,numpy as np
from PIL import Image,ImageDraw
D=sys.argv[1]; out=sys.argv[2]; w,h=144,256; rows=[]
for k in ['s1','s2','s3','eA','eB']:
    c=f'{D}/clipes/{k}.mp4'; n=int(subprocess.run(['ffprobe','-v','error','-count_frames','-select_streams','v','-show_entries','stream=nb_read_frames','-of','csv=p=0',c],capture_output=True,text=True).stdout)
    ns=[int(x) for x in np.linspace(0,n-1,10)]; sel='+'.join(f'eq(n\\,{m})' for m in ns)
    raw=subprocess.run(['ffmpeg','-v','error','-i',c,'-vf',f"select='{sel}',scale={w}:{h}",'-vsync','0','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    a=np.frombuffer(raw,np.uint8).reshape(-1,h,w,3); rows.append(np.concatenate(list(a),1))
Image.fromarray(np.concatenate(rows,0)).save(out,quality=85)
