# Imagens-base (gpt-image-2/edit, medium, 1k) sobre frames limpos do original. Troca pessoa E ambiente; mantém pose/enquadramento. Uso: python3 gerar-bases.py homem mulherA | mulherB
import json,subprocess,sys,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
U=lambda f: open(f'base/url-{f}.txt').read().strip()
HOMEM="a man about 24 years old with light-brown skin, short straight dark-brown hair neatly cut with a low fade, a short well-trimmed dark stubble beard, wearing a plain heather-grey crewneck sweatshirt"
CENA_H="sitting on a sofa in a dim living room at night: a plain warm-beige wall behind him, the edge of a tall bookshelf out of focus on one side, a small warm table lamp glowing softly off to the side, the rest of the room in shadow"
MULHER="a woman about 25 years old with medium-brown skin and long loose curly dark-brown hair, wearing an oversized plain pastel-pink hoodie and light-grey sweatpants"
CENA_A="a narrow apartment hallway with light sage-green painted walls and a dark walnut-wood door with a black handle, a small framed photo on the wall, warm ceiling light"
R={
 'homem':(['ref-n700'],"Vertical 9:16 smartphone selfie video still, same camera position, same close-up framing and same head size, head position and pose as the image: a man looking straight into the phone camera, mouth relaxed and slightly open as if mid-sentence. "
   f"REPLACE the man with a DIFFERENT man: {HOMEM}. REPLACE the background with a DIFFERENT place: {CENA_H}. Keep the same dark moody low-light look and the same crop (top of the head touching the top edge). "
   "He is the only person in the image. No text, no captions, no logos, no watermark. Photorealistic, natural skin texture with visible pores, no retouching, ordinary person, not a model, shot on a front phone camera."),
 'mulherA':(['in-n30'],"Vertical 9:16 handheld smartphone video still, same camera position, same framing, same pose and same size in frame as the image: a woman standing in front of a closed door, holding her phone out in one hand, the other arm moving, mouth open mid-shout, annoyed and dramatic expression. "
   f"REPLACE the woman with a DIFFERENT woman: {MULHER}. REPLACE the place with a DIFFERENT place: {CENA_A}. "
   "She is the only person in the image. No text, no captions, no logos, no print on clothes, no watermark. Photorealistic amateur phone footage look, natural skin texture, ordinary person, slight motion softness."),
}
alvo=sys.argv[1:]
if 'mulherB' in alvo:
    R['mulherB']=(['in-n250','mulherA'],"Vertical 9:16 handheld smartphone video still. Use the FIRST image for the exact camera position, wide framing, composition and the woman's pose (leaning with her back against the edge of an open doorway, holding a phone in one hand, looking up, mouth open, dramatic). "
       "Use the SECOND image for the woman's identity and clothes and for the place: the SAME woman, same face, same curly hair, same pastel-pink hoodie and grey sweatpants, in the SAME hallway with sage-green walls and the dark walnut door, now seen wider: the open door shows a small bedroom corner with a bed with a light-grey duvet. "
       "She is the only person in the image. No text, no captions, no logos, no print on clothes, no watermark. Photorealistic amateur phone footage look, natural skin texture.")
procs=[]
for k in alvo:
    imgs,p=R[k]; r={"prompt":p,"images":[U(i) for i in imgs],"quality":"medium","resolution":"1k","aspect_ratio":"9:16"}
    json.dump(r,open(f'base/{k}.req.json','w'))
    procs.append((k,subprocess.Popen(f"wavespeed run openai/gpt-image-2/edit --input-file base/{k}.req.json --json --download base/{k}.png > base/{k}.json 2> base/{k}.log",shell=True)))
for n,pr in procs: print(n,'ok' if pr.wait()==0 else 'FALHOU')
