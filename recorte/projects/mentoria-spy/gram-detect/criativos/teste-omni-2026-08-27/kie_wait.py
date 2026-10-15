import json, os, urllib.request, time, subprocess, sys
K=os.environ["KIE"]; name=sys.argv[1]
tid=json.load(open("kie_jobs.json"))[name]["taskId"]
for t in range(150):
    r=urllib.request.Request(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}",headers={"Authorization":"Bearer "+K})
    d=json.load(urllib.request.urlopen(r,timeout=30)).get("data") or {}
    if d.get("state") in ("success","fail","failed","error"):
        urls=[]
        try: urls=json.loads(d.get("resultJson") or "{}").get("resultUrls",[])
        except Exception: pass
        print(name, d.get("state"), "creditos:",d.get("creditsConsumed"), d.get("failMsg") or "", flush=True)
        if urls:
            subprocess.run(["curl","-sL","-A","Mozilla/5.0","-o",f"out/{name}.mp4",urls[0]],check=True)
            print("baixado", flush=True)
        break
    time.sleep(10)
else: print("timeout", flush=True)
