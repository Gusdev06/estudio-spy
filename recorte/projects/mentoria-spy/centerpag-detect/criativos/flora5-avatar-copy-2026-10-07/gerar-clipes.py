#!/usr/bin/env python3
# Clipes Pruna (pruna-ai/p-video/avatar, 720p, seed 7, prompt só em positivo + identidade travada) — 1 por bloco de rosto, com o áudio NOVO do bloco.
# Sobe imagem-base e áudio (wavespeed upload), grava req/out/log e baixa; valida decodificando inteiro e, se truncar, rebaixa via `wavespeed show`.
# Uso (desta pasta): python3 gerar-clipes.py p172:a1 p172:b ...   (SEED=7 por padrão)
import json, os, re, subprocess, sys, time
S=int(os.environ.get('SEED','7'))
def up(arq):
    o=subprocess.run(['wavespeed','upload',arq],capture_output=True,text=True).stdout+subprocess.run(['true']).__class__.__name__
    u=re.findall(r'https://\S+',o); assert u,(arq,o); return u[-1]
def ok(arq): return os.path.exists(arq) and os.path.getsize(arq)>50000 and subprocess.run(['ffmpeg','-v','error','-i',arq,'-f','null','-'],capture_output=True,text=True).stderr.strip()==''
procs=[]
for alvo in sys.argv[1:]:
    P,b=alvo.split(':'); E=json.load(open(f'{P}/elenco.json')); T=json.load(open(f'{P}/molde/timeline.json')); p=T['blocos'][b]['papel']
    os.makedirs(f'{P}/clipes',exist_ok=True); cache=f'{P}/clipes/urls.json'; U=json.load(open(cache)) if os.path.exists(cache) else {}
    for k,arq in ((f'img-{p}',f'{P}/base/{p}.png'),(f'aud-{b}',f'{P}/audio/clip-{b}.wav')):
        if k not in U: U[k]=up(arq)
    json.dump(U,open(cache,'w'),indent=1)
    quem='woman' if p=='A' else 'man'; lado='toward the right, where the other host sits off-camera' if p=='A' else 'toward the left, where the other host sits off-camera'
    vp=(f"One continuous full-frame close-up shot in {E['estudio_curto']}; the video fills the whole frame edge to edge from the first frame to the last. "
        f"The {quem} in the image — {E[p]} — wearing black over-ear headphones, speaks into the black podcast microphone, alone in the shot, and stays EXACTLY the same person from the first frame to the last: same face, same hair, same clothes, same framing, same distance from the camera. "
        f"Locked-off camera on a tripod; the background stays still. The {quem} talks {lado}, "
        + ("confident and knowing, explaining something, with small natural head movements." if p=='A' else "curious and surprised, asking a question, with small natural head movements."))
    base=f'{P}/clipes/{b}-s{S}'
    json.dump({'image':U[f'img-{p}'],'audio':U[f'aud-{b}'],'resolution':'720p','video_prompt':vp,'seed':S},open(base+'.req.json','w'))
    procs.append((alvo,base,subprocess.Popen(f"wavespeed run pruna-ai/p-video/avatar --input-file {base}.req.json --json --download {base}.mp4 > {base}.out.json 2> {base}.log",shell=True)))
for alvo,base,pr in procs:
    pr.wait()
    if not ok(base+'.mp4'):
        try:
            pid=json.load(open(base+'.out.json')).get('id') 
        except Exception: pid=None
        if not pid:
            m=re.findall(r'[0-9a-f]{32}',open(base+'.log').read()+open(base+'.out.json').read()); pid=m[0] if m else None
        if pid:
            for _ in range(20):
                sh=json.loads(subprocess.run(['wavespeed','show',pid,'--json'],capture_output=True,text=True).stdout or '{}')
                outs=sh.get('outputs') or sh.get('raw',{}).get('outputs') or []
                if outs: subprocess.run(['curl','-s','--retry','5','-o',base+'.mp4',outs[0]]); break
                time.sleep(15)
    print(alvo,'OK' if ok(base+'.mp4') else 'FALHOU', subprocess.run(['ffprobe','-v','error','-show_entries','stream=width,height,r_frame_rate,duration','-of','csv=p=0',base+'.mp4'],capture_output=True,text=True).stdout.split())
