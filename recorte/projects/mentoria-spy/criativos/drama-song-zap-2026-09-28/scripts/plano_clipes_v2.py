# Plano de clipes v2: parte o bloco (mapa-de-tempo-v2.json) nos clipes de cenas_v2.S e gera mapa-de-blocos-v2.md + plano-clipes-v2.json
import json, math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from cenas_v2 import S, clip_prompt
L = pathlib.Path(__file__).resolve().parent.parent
M = json.load(open(L / "mapa-de-tempo-v2.json"))
PAD = 0.15  # folga pra cortar frame inicial estático
plano, rows = [], []
for b in M["blocos"]:
    k = b["bloco"]; s = S[k]; t = b["inicio"]; n = len(s["clips"])
    for j, (q0, q1, frac, desc) in enumerate(s["clips"]):
        dur = round(b["duracao"] * frac, 3) if j < n - 1 else round(b["fim"] - t, 3)
        gen = max(3, math.ceil(dur + PAD))
        cid = k if n == 1 else f"{k}{'abcd'[j]}"
        plano.append({"clip": cid, "bloco": k, "inicio": round(t, 3), "dur": dur, "gerar_s": gen, "quadro_ini": q0, "quadro_fim": q1,
                      "prompt": clip_prompt(k, s, desc)})
        t += dur
    rows.append(f"| {k} | {b['inicio']:.2f} | {b['fim']:.2f} | **{b['duracao']:.2f} s** | {b['estimado_plano']} s | {n} | " + " + ".join(f"{p['gerar_s']} s" for p in plano if p['bloco'] == k) + " | " + " / ".join(b["linhas"])[:90] + " |")
json.dump(plano, open(L / "_runs/plano-clipes-v2.json", "w"), indent=1, ensure_ascii=False)
tot = sum(p["gerar_s"] for p in plano)
md = f"""# Mapa de blocos v2 — cancao-v2.mp3 ({M['duracao_audio']:.2f} s)

Gerado por `scripts/mapa_v2.py` (tempos) + `scripts/plano_clipes_v2.py` (clipes). Letra: `letra-v2.txt`. Transcrição: `mlx-community/whisper-large-v3-mlx`, word timestamps (`_runs/whisper-v2/cancao-v2.json`).

Regra dos blocos igual à v1: bloco vai do início da 1ª linha dele até o início da 1ª linha do bloco seguinte; B01 começa em 0 e B25 vai até o fim do arquivo. Blocos > 15 s ou com troca de lugar entre quadros viram 2 clipes (pares de quadros do mesmo lugar). Duração gerada = teto(duração + {PAD} s), mínimo 3 s; o excesso é aparado no ffmpeg.

| Bloco | Início | Fim | Duração | Estimativa Isca | Clipes | Gerar (H3) | Letra |
|---|---|---|---|---|---|---|---|
""" + "\n".join(rows) + f"""

**Total gerado: {len(plano)} clipes, {tot} s → US$ {tot*0.02:.2f} a US$ 0,02/s (H3 480p).**

## Observações da v2
- A cantora cantou a intro falada **duas vezes** (1,34 s e 9,24 s); o alinhamento casa a letra com a 2ª. B01 ficou com 16,9 s e virou 2 clipes. A legenda mostra a linha nas duas vezes.
- **"Jess" audível na revelação**: o Whisper large-v3 ouviu "Not a stranger, it was **Jess**, my best friend **Jess**, the one I knew" (116,5–121,1 s). Não precisou de retry.
- Linha 50: Whisper ouviu "Just was sitting three seats away" (a letra diz "Jess was…"). Na virada (linha 33–34) o nome sai claro; aqui é o mesmo erro de transcrição da v1 em canto rápido — vale ouvir.
- Outras divergências de transcrição (a letra manda): "I blame my heart" (blamed), "She'd live this one" (lived this once), "stopped the" (fights), "Same candle" (candles).
"""
open(L / "mapa-de-blocos-v2.md", "w").write(md)
print(len(plano), "clipes", tot, "s", round(tot * 0.02, 2))
for p in plano: print(p["clip"], p["inicio"], p["dur"], p["gerar_s"], p["quadro_ini"], p["quadro_fim"])
