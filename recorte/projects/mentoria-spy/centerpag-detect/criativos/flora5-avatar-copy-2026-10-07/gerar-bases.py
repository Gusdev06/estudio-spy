#!/usr/bin/env python3
# Imagens-base da dupla nova (gpt-image-2/edit medium 1k) sobre o frame da janela do ORIGINAL ampliado 3x (refs da var5: mulher n 30, homem n 150).
# Mesma pose/enquadramento do molde; pessoa e estúdio vêm de p17x/elenco.json. Uso (desta pasta): python3 gerar-bases.py p172:A p172:B p173:A ...
import json, subprocess, sys
POSE={'A':"Same camera position, same close-up framing and same pose as the image: she is seen from the chest up, turned three-quarters toward the right side of the frame, "
          "wearing black over-ear headphones, a black podcast microphone on a boom arm in front of her on the right, mouth slightly open as if mid-sentence, looking toward the person off-camera on the right.",
      'B':"Same camera position, same tight close-up framing and same pose as the image: his face in profile turned toward the left side of the frame, "
          "wearing black over-ear headphones, a black podcast microphone in front of his mouth at the lower left, mouth slightly open as if mid-sentence, looking toward the person off-camera on the left."}
procs=[]
for alvo in sys.argv[1:]:
    P,p=alvo.split(':'); E=json.load(open(f'{P}/elenco.json')); subprocess.run(['mkdir','-p',f'{P}/base'])
    url=open(f'base/url-ref-{p}.txt').read().strip()
    r={"prompt":("Photorealistic video still from a podcast recording. "+POSE[p]+
                 f" REPLACE the person with a DIFFERENT person: {E[p]}. REPLACE the whole background with {E['estudio']}. "
                 "Same size of the head in the frame and same head position as in the image. This person is the only person in the image. "
                 "No monitors, no screens, no text, no logos, no watermark. Natural skin texture with visible pores, no retouching, ordinary person, not a model, soft warm studio light, shallow depth of field."),
       "images":[url],"quality":"medium","resolution":"1k"}
    json.dump(r,open(f'{P}/base/{p}.req.json','w'))
    procs.append((alvo,subprocess.Popen(f"wavespeed run openai/gpt-image-2/edit --input-file {P}/base/{p}.req.json --json --download {P}/base/{p}.png > {P}/base/{p}.json 2> {P}/base/{p}.log",shell=True)))
for n,pr in procs: print(n,'ok' if pr.wait()==0 else 'FALHOU')
