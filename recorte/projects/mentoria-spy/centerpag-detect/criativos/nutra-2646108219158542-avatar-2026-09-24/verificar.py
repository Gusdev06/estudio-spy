"""Verify the actual delivery: source audio, unmodified shots and exact frame count."""
from pathlib import Path
import hashlib
import json
import subprocess
from PIL import Image,ImageDraw
from io import BytesIO

root=Path(__file__).resolve().parent
source=root.parents[2]/'downloads/ad-2646108219158542-2026-09-24/nutra-health-2646108219158542-v1.mp4'
final=root/'master-sem-perdas.mp4'
if not final.exists():
    final=root/'nutra-2646108219158542-variacao-avatar.mp4'
out=root/'conferencia'
out.mkdir(exist_ok=True)

def probe(p):
    return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries',
        'stream=codec_name,width,height,nb_frames,r_frame_rate,duration:format=duration,size','-of','json',str(p)]))

def audio_hash(p):
    raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-map','0:a:0','-c:a','copy','-f','adts','-'])
    return hashlib.sha256(raw).hexdigest()

def video_hashes(p):
    raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-map','0:v:0','-an','-pix_fmt','yuv420p','-f','framemd5','-'],text=True)
    return [line.split(',')[-1].strip() for line in raw.splitlines() if line and not line.startswith('#')]

original_meta,final_meta=probe(source),probe(final)
original_audio,final_audio=audio_hash(source),audio_hash(final)
original_frames,final_frames=video_hashes(source),video_hashes(final)
checks={
    'original':original_meta,'final':final_meta,
    'audio_original_sha256':original_audio,'audio_final_sha256':final_audio,
    'audio_aac_identico':original_audio==final_audio,
    'frames_original':len(original_frames),'frames_final':len(final_frames),
    'mesmo_numero_de_frames':len(original_frames)==len(final_frames)==8141,
    'hook_frames_0_219_identicos':original_frames[:220]==final_frames[:220],
    'cauda_frames_1290_fim_identicos':original_frames[1290:]==final_frames[1290:],
}
(out/'validacao.json').write_text(json.dumps(checks,indent=2))

ns=[0,219,220,227,300,450,600,750,900,1050,1200,1289,1290,1500,7200,8140]
sheet=Image.new('RGB',(8*180,2*348),'#181818');d=ImageDraw.Draw(sheet)
for i,n in enumerate(ns):
    raw=subprocess.check_output(['ffmpeg','-v','error','-ss',str(n/30),'-i',str(final),'-frames:v','1','-f','image2pipe','-vcodec','png','-'])
    im=Image.open(BytesIO(raw));im.save(out/f'frame-{n:04}.png');im.thumbnail((180,320))
    x=(i%8)*180;y=(i//8)*348
    sheet.paste(im,(x,y+28));d.text((x+4,y+6),f'{n/30:.2f}s / f{n}',fill='white')
sheet.save(out/'contato-final.jpg')
print(json.dumps({k:v for k,v in checks.items() if k not in ['original','final']},indent=2))
if not all(checks[k] for k in ['audio_aac_identico','mesmo_numero_de_frames','hook_frames_0_219_identicos','cauda_frames_1290_fim_identicos']):
    raise SystemExit('Validation failed: inspect validacao.json before delivery.')
