# Alinha a letra (verdade) com as palavras do Whisper (tempo) e gera mapa-de-tempo.json + mapa-de-blocos.md
import json, re, difflib, pathlib
L = pathlib.Path(__file__).resolve().parent.parent
ROT = L.parents[1] / "roteiros/2026-09-28-drama-song-zap"
DUR = 225.2016
norm = lambda w: re.sub(r"[^a-z0-9']", "", w.lower()).replace("'", "")
# letra -> linhas com seção
lines, sec = [], None
for raw in (ROT / "letra.txt").read_text().splitlines():
    raw = raw.strip()
    if not raw: continue
    m = re.match(r"\[(.+)\]", raw)
    if m: sec = m.group(1); continue
    lines.append({"secao": sec, "texto": raw})
ltok = []  # (line_idx, token)
for i, l in enumerate(lines):
    for w in l["texto"].split():
        t = norm(w)
        if t: ltok.append((i, t))
# whisper words
wj = json.load(open(L / "_runs/whisper/cancao-v1.json"))
words = [w for s in wj["segments"] for w in s.get("words", []) if s["start"] < 224]  # 224.56 "Thank you." = alucinação
wtok = [norm(w["word"]) for w in words]
sm = difflib.SequenceMatcher(None, [t for _, t in ltok], wtok, autojunk=False)
hit = {}
for a, b, n in sm.get_matching_blocks():
    for k in range(n): hit[a + k] = b + k
for i, l in enumerate(lines):
    idx = [k for k, (li, _) in enumerate(ltok) if li == i]
    m = [hit[k] for k in idx if k in hit]
    l["palavras_casadas"] = f"{len(m)}/{len(idx)}"
    l["inicio"] = round(words[m[0]]["start"], 2) if m else None
    l["fim"] = round(words[m[-1]]["end"], 2) if m else None
    l["whisper_ouviu"] = "".join(words[j]["word"] for j in range(m[0], m[-1] + 1)).strip() if m else ""
# preencher linhas sem casamento por interpolação simples
for i, l in enumerate(lines):
    if l["inicio"] is None:
        l["inicio"] = lines[i-1]["fim"]; l["fim"] = next(x["inicio"] for x in lines[i+1:] if x["inicio"] is not None); l["obs"] = "sem casamento: interpolado"
# blocos do plano (índice da 1a linha de cada bloco, 0-based, na ordem da letra)
first = lambda s, after=-1: next(i for i, l in enumerate(lines) if i > after and l["texto"].startswith(s))
B = {}
B["B01"] = 0; B["B02"] = first("Sunday dinner"); B["B03"] = first("His phone lit up beside")
B["B04"] = first("I asked him softly"); B["B05"] = first("He slid his phone"); B["B06"] = first("So I swallowed")
B["B07"] = first("I called my best"); B["B08"] = first("I asked a counselor"); B["B09"] = first("So I stopped asking")
B["B10"] = first("So I swallowed", B["B06"]); B["B11"] = first("Then my sister"); B["B12"] = first('"You\'re not crazy')
B["B13"] = first("On the phone"); B["B14"] = first("The conversations"); B["B15"] = first("My hands were")
B["B16"] = first("But the truth"); B["B17"] = first("Week one"); B["B18"] = first("Week three")
B["B19"] = first("No more swallowing"); B["B20"] = first("Sunday dinner", B["B02"]); B["B21"] = first("His phone lit up. He")
B["B22"] = first("I smiled"); B["B23"] = first("If your gut"); B["B24"] = first("This app"); B["B25"] = first("Tap the link")
EST = dict(B01=6,B02=7,B03=7,B04=7,B05=7,B06=13,B07=7,B08=7,B09=13,B10=13,B11=8,B12=8,B13=7,B14=7,B15=7,B16=7,B17=7,B18=8,B19=13,B20=7,B21=7,B22=8,B23=7,B24=9,B25=5)
keys = list(B)
blocos = []
for n, k in enumerate(keys):
    i0 = B[k]; i1 = B[keys[n+1]] if n + 1 < len(keys) else len(lines)
    ini = 0.0 if k == "B01" else lines[i0]["inicio"]
    fim = lines[B[keys[n+1]]]["inicio"] if n + 1 < len(keys) else DUR
    voz_fim = lines[i1-1]["fim"]
    blocos.append({"bloco": k, "linhas": [l["texto"] for l in lines[i0:i1]], "inicio": round(ini, 2), "fim": round(fim, 2),
                   "duracao": round(fim - ini, 2), "voz_ini": lines[i0]["inicio"], "voz_fim": voz_fim, "estimado_plano": EST[k]})
for i, l in enumerate(lines): l["n"] = i + 1
out = {"fonte_audio": "musica/cancao-v1.mp3", "duracao_audio": DUR, "whisper": "mlx-community/whisper-large-v3-turbo (mlx_whisper local, word_timestamps)",
       "regra": "texto = letra.txt (a letra manda); tempos = palavras do Whisper casadas por difflib. Blocos ladrilham a linha do tempo: bloco vai do início da 1a linha dele até o início da 1a linha do próximo (instrumental entra no bloco anterior).",
       "linhas": lines, "blocos": blocos}
json.dump(out, open(L / "mapa-de-tempo.json", "w"), indent=1, ensure_ascii=False)
for l in lines: print(f"{l['n']:2} {l['inicio']:7.2f}-{l['fim']:7.2f} {l['palavras_casadas']:>5} {l['texto'][:45]:45} | {l['whisper_ouviu'][:45]}")
for b in blocos: print(b["bloco"], b["inicio"], b["fim"], b["duracao"], "est", b["estimado_plano"])
