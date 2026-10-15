# var10 — 2 imagens-base (mulher e homem novos, estúdio novo): gpt-image-2/edit sobre o frame da janela do original (360x303 -> 1080x909), mesma pose e enquadramento.
# Uso (de projects/mentoria-spy/): python3 centerpag-detect/criativos/var10-flora-959352790554428-2026-09-27/gerar-bases.py [A B]
import json,subprocess,sys
L='centerpag-detect/criativos/var10-flora-959352790554428-2026-09-27'
ESTUDIO=("a DIFFERENT podcast studio: walls covered with light-grey hexagonal acoustic felt panels, a small softbox light, a light grey fabric backdrop, clean neutral cool-white light, minimal modern look, grey and white tones")
P={'A':('A1',"a South Asian woman about 40 years old with medium-brown skin, long black hair in a loose side braid over one shoulder, a tiny gold nose stud, wearing a deep-teal blouse",
        "Same camera position, same close-up framing and same pose as the image: she is seen from the chest up, turned three-quarters toward the right side of the frame, "
        "wearing black over-ear headphones, a black podcast microphone on a boom arm in front of her on the right, mouth slightly open as if mid-sentence, looking toward the person off-camera on the right."),
   'B':('B',"a Black man about 40 years old with dark skin, a clean-shaven head and a short black beard with a few grey hairs, wearing a white henley shirt",
        "Same camera position, same tight close-up framing and same pose as the image: his face in profile turned toward the left side of the frame, "
        "wearing black over-ear headphones, a black podcast microphone in front of his mouth at the lower left, mouth slightly open as if mid-sentence, looking toward the person off-camera on the left.")}
alvo=sys.argv[1:] or list(P); procs=[]
for p in alvo:
    ref,pessoa,pose=P[p]; url=open(f'{L}/base/url-ref-{ref}.txt').read().strip()
    r={"prompt":("Photorealistic video still from a podcast recording. "+pose+
                 f" REPLACE the person with a DIFFERENT person: {pessoa}. REPLACE the whole background with {ESTUDIO}. "
                 "Same size of the head in the frame and same head position as in the image. This person is the only person in the image. "
                 "No monitors, no screens, no text, no logos, no watermark. Natural skin texture with visible pores, no retouching, ordinary person, not a model, soft warm studio light, shallow depth of field."),
       "images":[url],"quality":"medium","resolution":"1k"}
    open(f'{L}/base/{p}.txt','w').write(pessoa); json.dump(r,open(f'{L}/base/{p}.req.json','w'))
    procs.append((p,subprocess.Popen(f"wavespeed run openai/gpt-image-2/edit --input-file {L}/base/{p}.req.json --json --download {L}/base/{p}.png > {L}/base/{p}.json 2> {L}/base/{p}.log",shell=True)))
for n,pr in procs: print(n,'ok' if pr.wait()==0 else 'FALHOU')
