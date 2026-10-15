import json, os, urllib.request, time, subprocess
K=os.environ["KIE"]
j=json.load(open("full/jobs.json"))
pend={n:j[n]["taskId"] for n in ("B2r1","B2r2")}
for t in range(180):
    for n,tid in list(pend.items()):
        r=urllib.request.Request(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}",headers={"Authorization":"Bearer "+K})
        d=json.load(urllib.request.urlopen(r,timeout=30)).get("data") or {}
        if d.get("state") in ("success","fail","failed","error"):
            urls=[]
            try: urls=json.loads(d.get("resultJson") or "{}").get("resultUrls",[])
            except Exception: pass
            print(n, d.get("state"), "cr:",d.get("creditsConsumed"), d.get("failMsg") or "", flush=True)
            if urls: subprocess.run(["curl","-sL","-A","Mozilla/5.0","-o",f"full/{n}.mp4",urls[0]],check=True)
            del pend[n]
    if not pend: break
    time.sleep(10)
print("FIM", flush=True)
