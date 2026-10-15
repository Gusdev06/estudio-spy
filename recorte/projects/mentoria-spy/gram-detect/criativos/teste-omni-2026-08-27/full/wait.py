import json, os, urllib.request, time, subprocess
K=os.environ["KIE"]
jobs=json.load(open("full/jobs.json"))
pend={n:v["taskId"] for n,v in jobs.items() if v["taskId"]}
res={}
for t in range(180):
    for n,tid in list(pend.items()):
        r=urllib.request.Request(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}",headers={"Authorization":"Bearer "+K})
        d=json.load(urllib.request.urlopen(r,timeout=30)).get("data") or {}
        st=d.get("state")
        if st in ("success","fail","failed","error"):
            urls=[]
            try: urls=json.loads(d.get("resultJson") or "{}").get("resultUrls",[])
            except Exception: pass
            print(n, st, "cr:",d.get("creditsConsumed"), d.get("failMsg") or "", flush=True)
            if urls:
                subprocess.run(["curl","-sL","-A","Mozilla/5.0","-o",f"full/{n}.mp4",urls[0]],check=True)
            res[n]={"state":st,"credits":d.get("creditsConsumed"),"fail":d.get("failMsg")}
            del pend[n]
    if not pend: break
    time.sleep(10)
for n in pend: print(n,"TIMEOUT",flush=True); res[n]={"state":"timeout"}
json.dump(res,open("full/results.json","w"),indent=1)
print("FIM", flush=True)
