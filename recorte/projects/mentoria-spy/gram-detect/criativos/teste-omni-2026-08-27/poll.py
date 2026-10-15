import json, urllib.request, time
K=json.load(open('/Users/gustagoat/Library/Preferences/wavespeed-nodejs/config.json'))['apiKey']
jobs=json.load(open('jobs.json'))
def get(i):
    r=urllib.request.Request(f"https://api.wavespeed.ai/api/v3/predictions/{i}/result",
        headers={"Authorization":"Bearer "+K})
    return json.load(urllib.request.urlopen(r,timeout=30))["data"]
pending={n:v["id"] for n,v in jobs.items() if v["id"]}
res={}
for t in range(80):
    for n,i in list(pending.items()):
        d=get(i); s=d["status"]
        if s in ("completed","failed"):
            res[n]={"status":s,"error":d.get("error"),"outputs":d.get("outputs"),"secs":d.get("timings",{}).get("inference")}
            print(f"{n:14} {s:9} {d.get('error','')[:70]} {(d.get('outputs') or [''])[0]}")
            del pending[n]
    if not pending: break
    time.sleep(12)
for n,i in pending.items(): res[n]={"status":"timeout"}; print(n,"TIMEOUT")
json.dump(res,open("results.json","w"),indent=1)
