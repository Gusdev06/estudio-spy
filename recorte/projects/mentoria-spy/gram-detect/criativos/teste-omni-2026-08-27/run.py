import json, urllib.request, sys, time, os
K=json.load(open('/Users/gustagoat/Library/Preferences/wavespeed-nodejs/config.json'))['apiKey']
U=dict(l.strip().split('=',1) for l in open('urls.env') if '=' in l)
CHUNK,AVATAR,PIMG=U['CHUNK'],U['AVATAR'],U['PROMPTIMG']
PTXT=("Replace the woman in the video with the woman in the reference image. "
      "Keep exactly the same scenery, background, lighting, camera framing, clothing, "
      "head movement and timing. Only the person's identity changes.")

JOBS=[
 ("p-video-txt","pruna-ai/p-video/replace",
  {"video":CHUNK,"images":[AVATAR],"prompt":PTXT,"resolution":"1080p","save_audio":True}),
 ("p-video-img","pruna-ai/p-video/replace",
  {"video":CHUNK,"images":[PIMG,AVATAR],"prompt":"read the images","resolution":"1080p","save_audio":True}),
 ("skyreels-txt","skywork-ai/skyreels-v4/reference-to-video",
  {"ref_videos":[CHUNK],"images":[AVATAR],"prompt":PTXT,"aspect_ratio":"9:16","duration":10,"resolution":"1080p"}),
 ("kling-o3-txt","kwaivgi/kling-video-o3-pro/reference-to-video",
  {"video":CHUNK,"images":[AVATAR],"prompt":PTXT,"aspect_ratio":"9:16","duration":10,"keep_original_sound":True}),
 ("kling-o3-img","kwaivgi/kling-video-o3-pro/reference-to-video",
  {"video":CHUNK,"images":[PIMG,AVATAR],"prompt":"read the images","aspect_ratio":"9:16","duration":10,"keep_original_sound":True}),
]
def post(path, body):
    r=urllib.request.Request("https://api.wavespeed.ai/api/v3/"+path,
        data=json.dumps(body).encode(),
        headers={"Authorization":"Bearer "+K,"Content-Type":"application/json"})
    try:
        return json.load(urllib.request.urlopen(r,timeout=60))
    except urllib.error.HTTPError as e:
        return {"err":e.read().decode()[:300]}
out={}
for name,model,body in JOBS:
    d=post(model,body)
    jid=d.get("data",{}).get("id") if "data" in d else None
    out[name]={"model":model,"id":jid,"raw":None if jid else d}
    print(name, model, jid or d)
json.dump(out,open("jobs.json","w"),indent=1)
