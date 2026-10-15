#!/usr/bin/env python3
# Conferência final de cada peça: decodifica inteira, 1080x1920, silêncios >=0,5 s (-hide_banner, não -v error), rostos por frame (YuNet >=0,8, 6 fps,
# escolhido por score) no vídeo inteiro, e karaokê × copy (palavras do legenda.tsv contra o texto da copy). Uso: python3 conferir-pecas.py pecas/*.mp4
import sys,os,re,json,subprocess,difflib,numpy as np,cv2
os.chdir(os.path.dirname(os.path.abspath(__file__))); M='/Users/gustagoat/Documents/AIS-OS/projects/mentoria-spy/gram-detect/scripts/modelos/face_detection_yunet_2023mar.onnx'
C=json.load(open('copys.json')); ruim=0
for p in sys.argv[1:]:
    p=os.path.relpath(os.path.abspath(p)); v='v'+os.path.basename(p).split('-')[0]; prob=[]
    err=subprocess.run(['ffmpeg','-v','error','-i',p,'-f','null','-'],capture_output=True,text=True).stderr.strip()
    if err: prob.append('decode: '+err[:80])
    wh=subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height,nb_frames','-of','csv=p=0',p],capture_output=True,text=True).stdout.strip()
    dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
    if not wh.startswith('1080,1920'): prob.append('tamanho '+wh)
    log=subprocess.run(['ffmpeg','-hide_banner','-i',p,'-af','silencedetect=n=-35dB:d=0.5','-f','null','-'],capture_output=True,text=True).stderr
    sil=re.findall(r'silence_duration: ([\d.]+)',log)
    if sil: prob.append(f'{len(sil)} silêncios >=0,5 s {sil}')
    raw=subprocess.run(['ffmpeg','-v','error','-i',p,'-vf','fps=6,scale=540:960','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    f=np.frombuffer(raw,np.uint8).reshape(-1,960,540,3); det=cv2.FaceDetectorYN_create(M,'',(540,960),0.8,0.3,5000); n=[]
    for x in f: d=det.detect(np.ascontiguousarray(x))[1]; n.append(0 if d is None else len(d))
    if max(n)>1: prob.append(f'{max(n)} rostos em {n.index(max(n))/6:.1f}s')
    if min(n)==0: prob.append(f'sem rosto em {n.index(0)/6:.1f}s ({n.count(0)} amostras)')
    tsv=f'pecas/molde-{os.path.basename(p)[:-4]}/legenda.tsv'
    kw=[l.split('\t')[2].strip() for l in open(tsv) if not l.startswith('#')]
    cw=[re.sub(r"[^A-Za-z0-9'\-]","",w).upper() for w in C[v]['txt'].split()]; cw=[w for w in cw if w]
    r=difflib.SequenceMatcher(None,kw,cw).ratio()
    if r<0.9: prob.append(f'karaokê × copy {r:.2f}')
    ruim+=bool(prob)
    print(f"{os.path.basename(p)}: {'OK' if not prob else 'PROBLEMA: '+'; '.join(prob)} · {wh} · {dur:.2f}s · rostos/frame {min(n)}-{max(n)} · karaokê×copy {r:.2f} ({len(kw)}/{len(cw)} palavras)")
sys.exit(1 if ruim else 0)
