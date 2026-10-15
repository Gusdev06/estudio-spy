# Imagem-base: gpt-image-2/edit sobre o frame n360 do original (quadro cheio 960x720, sem painel). Troca pessoa E cômodo; mesma pose e enquadramento.
import json,subprocess
D='centerpag-detect/criativos/var3-amanda-silva-1680455873461877-2026-09-25'; url=open(f'{D}/base/url-ref.txt').read().strip()
pessoa=open(f'{D}/base/pessoa.txt').read().strip(); cena=open(f'{D}/base/cena.txt').read().strip()
r={"prompt":("Horizontal 4:3 webcam-style video still, same camera position, same framing and same pose as the image: a young woman seen from the chest up, "
             "centered slightly left of the middle, head at the same height and the same size in the frame, looking straight into the camera, mouth closed, calm and serious. "
             f"REPLACE the woman with a DIFFERENT woman: {pessoa}. REPLACE the whole room behind her with a DIFFERENT place: {cena}. "
             "She is the only person in the image. No television, no screens with content, no text, no letters, no logos, no watermark. "
             "Photorealistic, natural skin texture with visible pores, light natural makeup, ordinary person, not a model, soft natural indoor light, shot on a phone front camera."),
   "images":[url],"quality":"medium","resolution":"1k"}
json.dump(r,open(f'{D}/base/base.req.json','w'))
subprocess.run(f"wavespeed run openai/gpt-image-2/edit --input-file {D}/base/base.req.json --json --download {D}/base/base.png > {D}/base/base.json 2> {D}/base/base.log",shell=True,check=True)
