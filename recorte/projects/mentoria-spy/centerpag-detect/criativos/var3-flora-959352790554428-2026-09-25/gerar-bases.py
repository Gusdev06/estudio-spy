# var3 — 2 imagens-base (mulher e homem novos, estúdio novo): gpt-image-2/edit sobre o frame da janela do original (360x303 -> 1080x909), mesma pose e enquadramento.
# Uso (de projects/mentoria-spy/): python3 centerpag-detect/criativos/var3-flora-959352790554428-2026-09-25/gerar-bases.py [A B]
import json,subprocess,sys
L='centerpag-detect/criativos/var3-flora-959352790554428-2026-09-25'
ESTUDIO=("a DIFFERENT podcast studio: a bright Scandinavian room with clean white walls, light oak wooden slat panels, a pale linen sofa, a large green monstera plant, soft natural daylight from a window, airy light beige, white and oak tones")
P={'A':('A1',"a woman about 38 years old with fair skin, straight honey-blonde shoulder-length hair tucked behind one ear, wearing a cream cable-knit sweater",
        "Same camera position, same close-up framing and same pose as the image: she is seen from the chest up, turned three-quarters toward the right side of the frame, "
        "wearing black over-ear headphones, a black podcast microphone on a boom arm in front of her on the right, mouth slightly open as if mid-sentence, looking toward the person off-camera on the right."),
   'B':('B',"a South Asian man about 36 years old with warm brown skin, black wavy hair and a short black beard, wearing a light-blue oxford button-down shirt",
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
