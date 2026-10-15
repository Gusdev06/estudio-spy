"""Validate master boundaries and source audio, decode deliveries, save contact sheets."""
from pathlib import Path
import hashlib,json,subprocess,sys
from PIL import Image,ImageDraw
from io import BytesIO
b=Path(__file__).resolve().parent
control=b.parent/'nutra-2646108219158542-avatar-2026-09-24'
source=control.parents[2]/'downloads/ad-2646108219158542-2026-09-24/nutra-health-2646108219158542-v1.mp4'
def probe(p):
 return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','stream=codec_name,profile,width,height,nb_frames,r_frame_rate,duration:format=duration,size','-of','json',str(p)]))
def ah(p):
 return hashlib.sha256(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-map','0:a:0','-c:a','copy','-f','adts','-'])).hexdigest()
def vh(p):
 raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-map','0:v:0','-an','-pix_fmt','yuv420p','-f','framemd5','-'],text=True)
 return [l.split(',')[-1].strip() for l in raw.splitlines() if l and not l.startswith('#')]
cache=b/'referencia-hashes.json'
if not cache.exists():cache.write_text(json.dumps({'audio':ah(source),'frames':vh(source)}))
ref=json.loads(cache.read_text())
variants=[b/sys.argv[1]] if len(sys.argv)>1 else sorted(p for p in b.glob('v0*') if p.is_dir())
for p in variants:
 master=p/'master-sem-perdas.mp4';delivery=p/(p.name+'-nutra-2646108219158542.mp4')
 out=p/'conferencia';out.mkdir(exist_ok=True)
 frames=vh(master);dm=probe(delivery);mm=probe(master)
 checks={'master_metadata':mm,'delivery_metadata':dm,'audio_source_sha256':ref['audio'],'audio_master_sha256':ah(master),'audio_delivery_sha256':ah(delivery),'frames_master':len(frames)}
 checks['audio_original_preservado']=checks['audio_source_sha256']==checks['audio_master_sha256']==checks['audio_delivery_sha256']
 checks['hook_identico_no_master']=frames[:220]==ref['frames'][:220]
 checks['cauda_identica_no_master']=frames[1290:]==ref['frames'][1290:]
 checks['duracao_frames_preservada']=len(frames)==len(ref['frames'])==8141 and int(dm['streams'][0]['nb_frames'])==8141
 decoded=subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(delivery),'-f','null','-'],capture_output=True,text=True)
 checks['delivery_decodifica_inteiro']=decoded.returncode==0 and not decoded.stderr.strip()
 checks['decode_stderr']=decoded.stderr
 ns=[227,300,450,600,750,900,1050,1200,1289,1290]
 sheet=Image.new('RGB',(5*216,2*410),'#181818');d=ImageDraw.Draw(sheet)
 for i,n in enumerate(ns):
  raw=subprocess.check_output(['ffmpeg','-v','error','-ss',str(n/30),'-i',str(delivery),'-frames:v','1','-f','image2pipe','-vcodec','png','-'])
  im=Image.open(BytesIO(raw));im.save(out/f'frame-{n:04}.png');im.thumbnail((216,384))
  x=(i%5)*216;y=(i//5)*410;sheet.paste(im,(x,y+26));d.text((x+3,y+5),f'{p.name} / {n/30:.2f}s',fill='white')
 sheet.save(out/'contato-final.jpg',quality=94)
 (out/'validacao.json').write_text(json.dumps(checks,indent=2))
 keys=['audio_original_preservado','hook_identico_no_master','cauda_identica_no_master','duracao_frames_preservada','delivery_decodifica_inteiro']
 print(p.name,json.dumps({k:checks[k] for k in keys}),flush=True)
 assert all(checks[k] for k in keys),p.name+' falhou'
