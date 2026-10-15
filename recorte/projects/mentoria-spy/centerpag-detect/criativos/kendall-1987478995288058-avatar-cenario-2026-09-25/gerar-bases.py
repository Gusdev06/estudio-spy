# 1 imagem-base por variação: gpt-image-2/edit sobre o frame em plano aberto do original (t=15,5 s). Muda pessoa E cenário; mantém pose e enquadramento.
import json,subprocess,sys
L='centerpag-detect/criativos/kendall-1987478995288058-avatar-cenario-2026-09-25'; url=open(f'{L}/base/url-ref.txt').read().strip()
alvo=sys.argv[1:] or None; procs=[]
for line in open(f'{L}/casting.tsv'):
    k,nome,pessoa,cena=line.rstrip('\n').split('\t')
    if alvo and k not in alvo: continue
    r={"prompt":("Vertical 9:16 smartphone video still, same camera position, same framing and same pose as the image: a woman seen from head to bare feet, "
                 "sitting and leaning slightly forward, forearms resting on her knees, hands clasped loosely in front of her knees, looking straight into the camera, mouth closed, calm and serious. "
                 f"REPLACE the woman with a DIFFERENT woman: {pessoa}. REPLACE the whole room with a DIFFERENT place: {cena}. "
                 "Same size of the woman in the frame and same head position as in the image. She is the only person in the image. No television, no screens with content, no text, no logos, no watermark. "
                 "Photorealistic, natural skin texture with visible pores, no retouching, ordinary person, not a model, soft natural light, shot on a phone."),
       "images":[url],"quality":"medium","resolution":"1k"}
    open(f'{L}/base/{k}.txt','w').write(pessoa+' | '+cena); json.dump(r,open(f'{L}/base/{k}.req.json','w'))
    procs.append((k,subprocess.Popen(f"wavespeed run openai/gpt-image-2/edit --input-file {L}/base/{k}.req.json --json --download {L}/base/{k}.png > {L}/base/{k}.json 2> {L}/base/{k}.log",shell=True)))
for n,pr in procs: print(n,'ok' if pr.wait()==0 else 'FALHOU')
