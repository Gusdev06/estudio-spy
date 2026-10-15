#!/usr/bin/env python3
# Cliente fino do Jev (TypeSafe System One). Lê a key do .env local (server-side, nunca versionado).
# ask(state, questions) -> answers. Retry com backoff em 429/529. Uso como lib ou: python3 jev.py --sonda
import json, os, time, urllib.request, urllib.error

AQUI = os.path.dirname(os.path.abspath(__file__))
ENDPOINT = 'https://api.typesafe.ai/v1/systemone'
MODEL = 'jev-latest'

def _key():
    for line in open(os.path.join(AQUI, '.env')):
        if line.startswith('TYPESAFE_API_KEY='):
            return line.split('=', 1)[1].strip()
    raise RuntimeError('TYPESAFE_API_KEY ausente em typesafe/.env')

def ask(state, questions, model=MODEL, tentativas=5):
    """state: str|dict|list. questions: {id: {type, instructions, criteria}}. Devolve o dict completo (answers + usage)."""
    body = json.dumps({'state': state, 'model': model, 'questions': questions}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method='POST', headers={
        'Authorization': f'Bearer {_key()}', 'Content-Type': 'application/json'})
    erro = None
    for t in range(tentativas):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            erro = f'{e.code} {e.read()[:300].decode(errors="replace")}'
            if e.code in (429, 529): time.sleep(2 ** t); continue
            raise RuntimeError(f'Jev HTTP {erro}')
        except urllib.error.URLError as e:
            erro = str(e); time.sleep(2 ** t)
    raise RuntimeError(f'Jev falhou após {tentativas}: {erro}')

def score_norm(a):
    """Score normalizado 0-1: score / (n_niveis - 1)."""
    return a['score'] / (len(a['legend']) - 1)

if __name__ == '__main__':
    import sys
    if '--sonda' in sys.argv:
        r = ask("She says it's just a friend, but he texts her at 2am and hides the screen.",
                {'ciume': {'type': 'noul', 'instructions': 'Does this trigger jealousy or suspicion of a partner cheating?',
                           'criteria': {'true': 'Evokes suspicion/jealousy about infidelity', 'false': 'No such trigger'}},
                 'forca_hook': {'type': 'score', 'instructions': 'How strong is this as an ad hook to stop the scroll?',
                                'criteria': ['Weak, ignorable', 'Mild interest', 'Strong, emotionally charged']}})
        print(json.dumps(r, indent=2, ensure_ascii=False))
