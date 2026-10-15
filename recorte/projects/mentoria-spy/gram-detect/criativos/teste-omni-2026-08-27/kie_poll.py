import json, os, urllib.request, time
K=os.environ["KIE"]
jobs=json.load(open("kie_jobs.json"))
pending={n:v["taskId"] for n,v in jobs.items() if v["taskId"]}
res={}
for t in range(120):
    for n,tid in list(pending.items()):
        r=urllib.request.Request(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}",
            headers={"Authorization":"Bearer "+K})
        d=json.load(urllib.request.urlopen(r,timeout=30)).get("data") or {}
        st=d.get("state")
        if st in ("success","fail","failed","error"):
            urls=[]
            try: urls=json.loads(d.get("resultJson") or "{}").get("resultUrls",[])
            except Exception: pass
            res[n]={"state":st,"credits":d.get("creditsConsumed"),"fail":d.get("failMsg") or d.get("failCode"),"urls":urls}
            print(n, st, d.get("creditsConsumed"), d.get("failMsg") or "", urls[:1], flush=True)
            if urls:
                urllib.request.urlretrieve(urls[0], f"out/{n}.mp4"); print("  baixado", flush=True)
            del pending[n]
    if not pending: break
    time.sleep(10)
for n in pending: print(n,"TIMEOUT",flush=True)
json.dump(res,open("kie_results.json","w"),indent=1)
