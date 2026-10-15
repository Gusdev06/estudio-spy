import json, os, urllib.request, time
K=os.environ["KIE"]
pend={n:v["taskId"] for n,v in json.load(open("kie_jobs.json")).items() if n.startswith("mudo") and v["taskId"]}
res={}
for t in range(150):
    for n,tid in list(pend.items()):
        r=urllib.request.Request(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}",headers={"Authorization":"Bearer "+K})
        d=json.load(urllib.request.urlopen(r,timeout=30)).get("data") or {}
        st=d.get("state")
        if st in ("success","fail","failed","error"):
            urls=[]
            try: urls=json.loads(d.get("resultJson") or "{}").get("resultUrls",[])
            except Exception: pass
            print(n, st, "creditos:",d.get("creditsConsumed"), d.get("failMsg") or "", urls[:1], flush=True)
            if urls:
                urllib.request.urlretrieve(urls[0], f"out/{n}.mp4"); print("  baixado", flush=True)
            res[n]={"state":st,"credits":d.get("creditsConsumed"),"fail":d.get("failMsg"),"urls":urls}
            del pend[n]
    if not pend: break
    time.sleep(10)
for n in pend: print(n,"TIMEOUT",flush=True)
json.dump(res,open("kie_results2.json","w"),indent=1)
