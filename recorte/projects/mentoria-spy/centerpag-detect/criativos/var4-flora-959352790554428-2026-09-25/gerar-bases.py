# var4 — 2 imagens-base (mulher e homem novos, estúdio novo): gpt-image-2/edit sobre o frame da janela do original (360x303 -> 1080x909), mesma pose e enquadramento.
# Uso (de projects/mentoria-spy/): python3 centerpag-detect/criativos/var4-flora-959352790554428-2026-09-25/gerar-bases.py [A B]
import json,subprocess,sys
L='centerpag-detect/criativos/var4-flora-959352790554428-2026-09-25'
ESTUDIO=("a DIFFERENT podcast studio: dark walnut wood-paneled walls, a heavy deep burgundy velvet curtain, a brass floor lamp with a warm glow, a leather armchair in the background, rich dark wood, burgundy and warm gold tones, elegant and moody")
P={'A':('A1',"a Black woman about 40 years old with deep brown skin and natural shoulder-length afro-textured hair, small gold stud earrings, wearing an emerald-green silk blouse",
        "Same camera position, same close-up framing and same pose as the image: she is seen from the chest up, turned three-quarters toward the right side of the frame, "
        "wearing black over-ear headphones, a black podcast microphone on a boom arm in front of her on the right, mouth slightly open as if mid-sentence, looking toward the person off-camera on the right."),
   'B':('B',"a Latino man about 35 years old with tan skin, dark brown hair slicked back and a short dark stubble beard, wearing a dark-navy denim shirt",
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
