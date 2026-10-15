import json, os, urllib.request
K=os.environ["KIE"]
VID="https://tempfile.redpandaai.co/kieai/11456724/videos/teste-omni/chunk-20-30.mp4"
AVA="https://cdn.geraew.com.br/storage/v1/object/public/ai-generations/admin_assets/landing/f44addfb-d4d8-42c6-bc63-acbb3ab39983/download.jpeg"
PIM="https://cdn.geraew.com.br/storage/v1/object/public/ai-generations/admin_assets/landing/ede40b1a-28fc-4dd4-82c6-765c75ab4bff/download.png"
PTXT=("Replace the woman in the video with the woman in the reference image. "
      "Keep exactly the same scenery, background, lighting, camera framing, clothing, "
      "head movement and timing. Only the person's identity changes.")

JOBS={
 # a tecnica do Gusta: prompt entregue como imagem
 "omni-img": {"prompt":"read the images","image_urls":[PIM,AVA]},
 # controle: mesmo pedido em texto
 "omni-txt": {"prompt":PTXT,"image_urls":[AVA]},
}
def post(body):
    r=urllib.request.Request("https://api.kie.ai/api/v1/jobs/createTask",
        data=json.dumps(body).encode(),
        headers={"Authorization":"Bearer "+K,"Content-Type":"application/json"})
    try: return json.load(urllib.request.urlopen(r,timeout=60))
    except urllib.error.HTTPError as e: return {"err":e.read().decode()[:400]}

out={}
for name,inp in JOBS.items():
    body={"model":"gemini-omni-video","input":{
        **inp,
        "video_list":[{"url":VID,"start":0,"ends":10}],
        "duration":"10","aspect_ratio":"9:16","resolution":"1080p"}}
    d=post(body)
    tid=(d.get("data") or {}).get("taskId")
    out[name]={"taskId":tid,"raw":None if tid else d}
    print(name, tid or d)
json.dump(out,open("kie_jobs.json","w"),indent=1)
