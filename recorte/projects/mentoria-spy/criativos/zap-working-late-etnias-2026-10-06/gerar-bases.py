# Imagens-base (gpt-image-2/edit, medium, 1k, 1:1) sobre o frame 5 s da caixa da cabeça (x0-336 y119-443). Troca SÓ a pessoa;
# mantém quarto, camiseta preta, pose e enquadramento. Uso: python3 gerar-bases.py v1-branco v2-latino ...
import json,subprocess,sys,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
E=json.load(open('elenco.json'))
if not os.path.exists('base/url-ref.txt'):
    open('base/url-ref.txt','w').write(subprocess.run(['wavespeed','upload','base/ref-head.png'],capture_output=True,text=True).stdout.strip().split()[-1])
ref=open('base/url-ref.txt').read().strip()
P=lambda d:("Smartphone selfie video still. Keep EXACTLY the same camera position, framing, crop, head size, head position and pose as the image: "
 "a young man sitting on the edge of a bed, leaning slightly toward the phone, looking straight into the camera, mouth slightly open mid-sentence, plain black crew-neck t-shirt. "
 f"REPLACE the man with a DIFFERENT man: {d}. Keep the SAME room exactly: white door on the left with a dark jacket hanging on it, beige wall, white bed sheets, same soft daylight. "
 "He is the only person in the image. No text, no captions, no logos, no watermark. Photorealistic, natural skin texture with visible pores, no retouching, ordinary person, not a model, front phone camera.")
procs=[]
for k in sys.argv[1:]:
    json.dump({"prompt":P(E[k]),"images":[ref],"quality":"medium","resolution":"1k","aspect_ratio":"1:1"},open(f'base/{k}.req.json','w'))
    procs.append((k,subprocess.Popen(f"wavespeed run openai/gpt-image-2/edit --input-file base/{k}.req.json --json --download base/{k}.png > base/{k}.json 2> base/{k}.log",shell=True)))
for k,pr in procs:
    ok=pr.wait()==0
    if ok:
        j=json.load(open(f'base/{k}.json')); open(f'base/url-{k}.txt','w').write(j['outputs'][0]); open('prediction-ids.txt','a').write(f"{j['id']} img {k}\n")
    print(k,'ok' if ok else 'FALHOU')
