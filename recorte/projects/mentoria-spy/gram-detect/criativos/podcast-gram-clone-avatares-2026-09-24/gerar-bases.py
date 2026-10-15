# 2 imagens-base por elenco: gpt-image-2/edit sobre o frame da janela do original (720x812), MESMA roupa, fone, poltrona e cenário; só a pessoa muda.
import json,subprocess,sys
L='gram-detect/criativos/podcast-gram-clone-avatares-2026-09-24'
url={p:open(f'{L}/base/url-ref-{p}.txt').read().strip() for p in 'AB'}
cena={'A':"sitting in the same brown leather armchair on the left, legs crossed the same way, wearing the SAME cream overshirt over a dark top and the SAME light-blue wide jeans and white sneakers, the SAME black over-ear headphones, the same black podcast microphone in front of her",
      'B':"sitting in the same light-grey armchair, legs crossed the same way, one hand resting on the armrest, wearing the SAME black hoodie and dark trousers and white socks, the SAME black over-ear headphones, the same black podcast microphone on a boom arm in front of her"}
alvo=sys.argv[1:] or None; procs=[]
for line in open(f'{L}/casting.tsv'):
    k,nome,d=line.rstrip('\n').split('\t')
    if alvo and k not in alvo: continue
    desc=dict(zip('AB',[s.strip() for s in d.split('|')]))
    for p in 'AB':
        r={"prompt":("Same dark cozy podcast studio at night, same camera position and framing, same warm dim lamp and candle light, same furniture, shelves, plants and wall exactly as in the image. "
             f"REPLACE the woman with a DIFFERENT woman: {desc[p]}, {cena[p]}. Same position, same posture, same size in the frame, mouth closed, looking toward the person she is talking to off-camera. "
             "She is the only person in the image. Photorealistic video still, natural skin texture, no retouching, ordinary person, not a model, no text, no captions, no logos, no watermark."),
           "images":[url[p]],"quality":"medium","resolution":"1k"}
        open(f'{L}/base/{k}-{p}.txt','w').write(desc[p]); json.dump(r,open(f'{L}/base/{k}-{p}.req.json','w'))
        procs.append((k+p,subprocess.Popen(f"wavespeed run openai/gpt-image-2/edit --input-file {L}/base/{k}-{p}.req.json --json --download {L}/base/{k}-{p}.png > {L}/base/{k}-{p}.json 2> {L}/base/{k}-{p}.log",shell=True)))
for n,pr in procs: print(n,'ok' if pr.wait()==0 else 'FALHOU')
