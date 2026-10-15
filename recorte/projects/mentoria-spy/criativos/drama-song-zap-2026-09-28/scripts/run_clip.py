# Gera 1 clipe H3 480p a partir do plano (_runs/plano-clipes-v2.json). uso: python3 run_clip.py B02 [sufixo_retry] [prompt_override_file]
import json, sys, subprocess, pathlib
L = pathlib.Path(__file__).resolve().parent.parent
cid = sys.argv[1]; suf = sys.argv[2] if len(sys.argv) > 2 else ""
p = next(x for x in json.load(open(L / "_runs/plano-clipes-v2.json")) if x["clip"] == cid)
prompt = open(sys.argv[3]).read().strip() if len(sys.argv) > 3 else p["prompt"]
k = p["bloco"]
def up(f):
    r = subprocess.run(["wavespeed", "upload", str(f), "--json"], capture_output=True, text=True)
    try: d = json.loads(r.stdout)
    except Exception: raise SystemExit(f"upload falhou {f}: {r.stdout} {r.stderr}")
    return d[0]["url"] if isinstance(d, list) else d.get("url") or d["urls"][0]
inp = {"prompt": prompt, "image": up(L / f"quadros-v2/{k}-q{p['quadro_ini']}.png"), "resolution": "480p", "duration": p["gerar_s"]}
if p["quadro_fim"]: inp["last_image"] = up(L / f"quadros-v2/{k}-q{p['quadro_fim']}.png")
name = cid + suf
json.dump(inp, open(L / f"_runs/clip-v2-{name}.json", "w"), indent=1, ensure_ascii=False)
with open(L / f"_runs/clip-v2-{name}.out.json", "w") as o, open(L / f"_runs/clip-v2-{name}.err", "w") as e:
    rc = subprocess.run(["wavespeed", "run", "wavespeed-ai/minimax-h3/image-to-video", "--input-file", str(L / f"_runs/clip-v2-{name}.json"),
                         "--json", "--download", str(L / f"clipes-v2/{name}.mp4")], stdout=o, stderr=e).returncode
ok = subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-i", str(L / f"clipes-v2/{name}.mp4"), "-f", "null", "-"], capture_output=True, text=True)
print(name, "rc", rc, "decode_err", repr(ok.stderr[:200]) if ok.stderr or ok.returncode else "ok")
