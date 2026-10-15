# Imagens-base (gpt-image-2/edit, medium, 1k) sobre o frame limpo n60 do original (sem legenda). Troca SÓ a pessoa:
# mesmo quarto (cortina bege, arcos), mesmo enquadramento selfie e tamanho de cabeça. Uso: python3 gerar-bases.py a1 a2 ...
import json,subprocess,sys,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
REF=open('base/url-ref-n60.txt').read().strip()
A={
 'a1':"a Latina woman about 24 years old with warm olive-tan skin, dark-brown eyes and long wavy dark-brown hair falling past her shoulders, wearing a plain black fitted crewneck top",
 'a2':"a Black woman about 25 years old with deep-brown skin, dark-brown eyes and shoulder-length natural curly black hair, wearing a plain white crewneck t-shirt",
 'a3':"a white woman about 23 years old with fair skin, light-blue eyes and straight light-blonde hair just past her shoulders, wearing a plain light-blue knit sweater",
 'a4':"an East Asian woman about 24 years old with light skin, dark eyes and straight shoulder-length black hair with soft curtain bangs, wearing a plain oatmeal-beige knit sweater",
 'a5':"a white woman about 24 years old with fair skin, light freckles across her nose and cheeks, green eyes and wavy copper-red hair just past her shoulders, wearing a plain olive-green cardigan over a white top",
}
def prompt(d): return ("Vertical 9:16 front-camera smartphone selfie video still. Keep EXACTLY the same room, background, curtains, light, camera position, close-up framing, head size and head position as the image. "
  f"REPLACE the woman with a DIFFERENT woman: {d}. She looks straight into the phone camera, mouth relaxed and slightly open as if mid-sentence, natural light makeup. "
  "Only her head, shoulders and upper chest are visible; both of her arms hang relaxed at her sides, out of frame. "
  "She is the only person in the image. No text, no captions, no logos, no watermark. Photorealistic, natural skin texture with visible pores, no retouching, ordinary person, not a model, shot on a front phone camera.")
procs=[]
for k in sys.argv[1:]:
    r={"prompt":prompt(A[k]),"images":[REF],"quality":"medium","resolution":"1k","aspect_ratio":"9:16"}
    json.dump(r,open(f'base/{k}.req.json','w'))
    procs.append((k,subprocess.Popen(f"wavespeed run openai/gpt-image-2/edit --input-file base/{k}.req.json --json --download base/{k}.png > base/{k}.json 2> base/{k}.log",shell=True)))
for n,pr in procs: print(n,'ok' if pr.wait()==0 else 'FALHOU')
