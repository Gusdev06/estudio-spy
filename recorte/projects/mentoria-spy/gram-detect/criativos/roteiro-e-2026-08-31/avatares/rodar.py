import json, os, subprocess, time, urllib.request, urllib.error
BASE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(BASE)
KEY=[l.split('=',1)[1].strip() for l in open(os.path.expanduser('~/.config/kie/.env')) if l.startswith('KIE_API_KEY')][0]
URLS=dict(l.strip().split('=',1) for l in open(f'{BASE}/urls.txt') if '=' in l)
CLIPS=[('01','c1',15),('02','c2',15),('03','c3c',15),('04','c4',13),('05','c5',8)]

def post(path, body):
    req=urllib.request.Request(f'https://api.kie.ai/api/v1/jobs/{path}',
        data=json.dumps(body).encode(), method='POST',
        headers={'Authorization':f'Bearer {KEY}','Content-Type':'application/json'})
    return json.load(urllib.request.urlopen(req, timeout=90))

def get(tid):
    req=urllib.request.Request(f'https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}',
        headers={'Authorization':f'Bearer {KEY}'})
    return json.load(urllib.request.urlopen(req, timeout=90))

state_path=f'{BASE}/tasks.json'
tasks=json.load(open(state_path)) if os.path.exists(state_path) else {}

# 1) cria
for av,img in URLS.items():
    os.makedirs(f'{BASE}/{av}', exist_ok=True)
    for num,pf,dur in CLIPS:
        k=f'{av}/{num}'
        if k in tasks and tasks[k].get('taskId'): continue
        p=open(f'{ROOT}/v2/prompts/{pf}.txt').read()
        try:
            r=post('createTask', {"model":"kling-3.0-omni/image-to-video","input":{
                "image_urls":[img],"prefer_multi_shots":False,"customize_multi_shots":False,
                "prompt":p,"duration":dur,"audio":True,"resolution":"1080p","aspect_ratio":"auto"}})
            tasks[k]={'taskId':r.get('data',{}).get('taskId'),'dur':dur}
            print('criado',k,tasks[k]['taskId'],flush=True)
        except Exception as e:
            print('ERRO criar',k,e,flush=True)
        json.dump(tasks,open(state_path,'w'),indent=1)
        time.sleep(1.5)

# 2) poll + download
pend=[k for k,v in tasks.items() if not os.path.exists(f'{BASE}/{k}.mp4')]
for _ in range(160):
    pend=[k for k in pend if not os.path.exists(f'{BASE}/{k}.mp4')]
    if not pend: break
    for k in list(pend):
        try:
            d=get(tasks[k]['taskId'])['data']
        except Exception: continue
        if d['state']=='success':
            u=json.loads(d['resultJson'])['resultUrls'][0]
            subprocess.run(['curl','-sL','-o',f'{BASE}/{k}.mp4',u],check=True)
            print('baixado',k,flush=True)
        elif d['state']=='fail':
            print('FALHOU',k,d.get('failMsg'),flush=True); pend.remove(k)
    time.sleep(20)
print('FIM. baixados:',sum(1 for k in tasks if os.path.exists(f'{BASE}/{k}.mp4')),'de',len(tasks),flush=True)
