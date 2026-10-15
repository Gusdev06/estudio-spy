# Aperta os silêncios da voz (TTS com respiro longo mata o ritmo do hook) e remapeia o timing das palavras.
# Silêncio = trecho abaixo de -35 dB por >= MIN s; cada um vira ALVO s (metade antes, metade depois do corte).
# Uso (da pasta do lote): python3 _kit/apertar.py f1-love/voz 0.3  -> f1-love/voz-apertada.wav + .palavras.json
import sys, json, subprocess, re, numpy as np
b, ALVO = sys.argv[1], float(sys.argv[2]); MIN = max(ALVO + 0.05, 0.3); SR = 48000
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', b + '.mp3', '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.float32)
log = subprocess.run(['ffmpeg', '-hide_banner', '-i', b + '.mp3', '-af', f'silencedetect=n=-35dB:d={MIN}', '-f', 'null', '-'], capture_output=True, text=True).stderr
ss = [float(v) for v in re.findall(r'silence_start: ([\d.]+)', log)]; se = [float(v) for v in re.findall(r'silence_end: ([\d.]+)', log)]
dur = len(x) / SR; cortes = []   # (ini, fim) do trecho REMOVIDO
for s, e in zip(ss, se):
    if s <= 0.01 or e >= dur - 0.01: continue          # pontas: tratadas abaixo
    tira = (e - s) - ALVO
    if tira > 0: m = s + ALVO / 2; cortes.append((m, m + tira))
ini = max(0.0, se[0] - 0.08) if ss and ss[0] <= 0.01 else 0.0   # respiro inicial máx 80 ms
fim = dur
if ss and se and len(se) < len(ss): fim = min(dur, ss[-1] + 0.25)    # silêncio final vira 250 ms
keep = []; t = ini
for a, z in cortes:
    keep.append((t, a)); t = z
keep.append((t, fim))
y = np.concatenate([x[int(a * SR):int(z * SR)] for a, z in keep])
def mapa(tt):
    acc = 0.0
    for a, z in keep:
        if tt < a: return acc
        if tt <= z: return acc + tt - a
        acc += z - a
    return acc
w = json.load(open(b + '.palavras.json'))
for p in w: p['s'] = round(mapa(p['s']), 3); p['e'] = round(mapa(p['e']), 3)
out = b + '-apertada'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-c:a', 'pcm_s16le', out + '.wav'], input=y.tobytes(), check=True)
json.dump(w, open(out + '.palavras.json', 'w'), indent=0)
print(b, f'{dur:.2f}s -> {len(y)/SR:.2f}s', f'{len(cortes)} pausas apertadas')
