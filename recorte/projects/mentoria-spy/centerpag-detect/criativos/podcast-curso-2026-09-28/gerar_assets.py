# Gera do zero os assets do podcast de curso de inglês (CN tradicional): 2 rostos (estúdio podcast) + 8 falas TTS.
import subprocess, json, os, concurrent.futures as cf
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f'{D}/base', exist_ok=True); os.makedirs(f'{D}/audio', exist_ok=True); os.makedirs(f'{D}/clipes', exist_ok=True); os.makedirs(f'{D}/pecas', exist_ok=True)

# --- roteiro: A = professora, B = curioso ---
LINHAS = [
    ('A1', 'A', '你有沒有跟外國人說過 I’m so boring？'),
    ('B1', 'B', '有啊，想表達我覺得很無聊的時候。'),
    ('A2', 'A', '但他們會愣一下，因為你說的其實是「我這個人很無趣」。'),
    ('B2', 'B', '蛤？不是「我覺得無聊」嗎？'),
    ('A3', 'A', '「我覺得無聊」是 I’m bored。加 ing 是形容那個東西無聊，加 ed 才是你的感受。'),
    ('B3', 'B', '差一個字而已欸。'),
    ('A4', 'A', '對，但別人對你的印象差很多。這種逐字翻譯的錯，你可能每天都在犯。'),
    ('A5', 'A', '這場免費公開課，會帶你用英文的邏輯思考，不再逐字翻譯。連結在下面，免費報名。'),
]
json.dump(LINHAS, open(f'{D}/roteiro.json', 'w'), ensure_ascii=False, indent=1)
VOZ = {'A': 'Wise_Woman', 'B': 'Casual_Guy'}

def upload(p):
    return json.loads(subprocess.run(['wavespeed','upload',p,'--json'],capture_output=True,text=True).stdout)['url']

# --- 2 rostos, estúdio de podcast estilo Flora (headphone + mic), CADA UM sozinho no quadro ---
ROSTOS = {
 'A': "Photorealistic vertical 9:16 video still from a podcast recording. A Taiwanese woman about 32 with fair skin, long straight dark hair, light makeup, wearing a cream blazer over a white top, black over-ear headphones, a black podcast microphone on a boom arm in front of her. Modern podcast studio with light-grey acoustic panels and soft warm key light behind her, softly out of focus. She is the ONLY person in the image, seen chest up, turned three-quarters to the right, looking toward the person off-camera on the right, mouth slightly open mid-sentence, friendly and knowledgeable. Natural skin texture, no retouching, ordinary person not a model. No text, no logos.",
 'B': "Photorealistic vertical 9:16 video still from a podcast recording. A Taiwanese man about 30 with short black hair, clean-shaven, wearing a dark grey crewneck, black over-ear headphones, a black podcast microphone in front of him. Modern podcast studio with light-grey acoustic panels and soft warm light, softly out of focus. He is the ONLY person in the image, seen chest up, in profile turned to the left, looking toward the person off-camera on the left, mouth slightly open mid-sentence, curious and surprised. Natural skin texture, no retouching, ordinary person not a model. No text, no logos.",
}
def gen_rosto(k):
    json.dump({'prompt':ROSTOS[k],'aspect_ratio':'9:16','quality':'medium','resolution':'1k'},open(f'{D}/base/{k}.req.json','w'))
    r=subprocess.run(['wavespeed','run','openai/gpt-image-2/text-to-image','--input-file',f'{D}/base/{k}.req.json','--json','--download',f'{D}/base/{k}.png'],capture_output=True,text=True)
    open(f'{D}/base/{k}.out.json','w').write(r.stdout)
    try: u=json.loads(r.stdout)['outputs'][0]; open(f'{D}/base/url-{k}.txt','w').write(u); return f'rosto {k} ok'
    except Exception: return f'rosto {k} FALHOU {r.stderr[-120:]}'

def gen_voz(row):
    tag, papel, txt = row
    r=subprocess.run(['wavespeed','run','minimax/speech-2.6-hd','-i',f'text={txt}','-i',f'voice_id={VOZ[papel]}',
        '-i','speed=1.0','-i','emotion=neutral','-i','language_boost=Chinese','-i','format=mp3','-i','sample_rate=44100',
        '-i','bitrate=128000','-i','channel=1','--json','--download',f'{D}/audio/{tag}.mp3'],capture_output=True,text=True)
    open(f'{D}/audio/{tag}.out.json','w').write(r.stdout)
    ok=os.path.exists(f'{D}/audio/{tag}.mp3') and r.returncode==0
    return f'voz {tag} '+('ok' if ok else 'FALHOU '+r.stderr[-100:])

with cf.ThreadPoolExecutor(max_workers=10) as ex:
    for m in ex.map(gen_rosto, ['A','B']): print(m)
    for m in ex.map(gen_voz, LINHAS): print(m)
