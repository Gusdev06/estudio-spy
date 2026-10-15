#!/usr/bin/env python3
# Portão Jev da esteira: pontua ganchos/roteiros por conversão-provável antes de gastar em geração.
# Entrada: um JSON {nome: {headline, primeira_fala, angulo, formato}} (campos livres; quanto mais estado, melhor).
# Uso (de projects/mentoria-spy/): python3 typesafe/pontuar_ganchos.py ganchos.json
# Rubrica validada em estudo/ contra gasto real (rho +0,67, n=8 — direcional, lê a COPY do hook, não a edição).
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'estudo'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jev import ask, score_norm
from rubrica import RUBRICA, PESOS, NEGATIVAS

def pontuar(estado):
    r = ask(estado, RUBRICA)['answers']; v = {}
    for k, a in r.items():
        v[k] = score_norm(a) if a['type'] == 'score' else a['noul']
    comp = sum(PESOS[k] * (1 - v[k] if k in NEGATIVAS else v[k]) for k in PESOS)
    return v, comp

def rankear(ganchos):
    out = []
    for nome, est in ganchos.items():
        v, comp = pontuar(est); v['_nome'] = nome; v['_composto'] = comp; out.append(v)
    return sorted(out, key=lambda l: -l['_composto'])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('uso: python3 typesafe/pontuar_ganchos.py <ganchos.json>  [--json]'); sys.exit(1)
    ganchos = json.load(open(sys.argv[1])); res = rankear(ganchos)
    if '--json' in sys.argv:
        print(json.dumps(res, indent=1, ensure_ascii=False)); sys.exit(0)
    print(f'{"gancho":30} {"conv?":>6}  dor  curi  emo  conf   risco-fala')
    for l in res:
        risco = ' ⚠️' if l['promessa_proibida_na_fala'] >= 0.5 else ''
        print(f'{l["_nome"]:30} {l["_composto"]:>6.3f}  {l["dor_concreta"]:.2f} {l["loop_curiosidade"]:.2f} {l["carga_emocional"]:.2f} {l["confissao_primeira_pessoa"]:.2f}   {l["promessa_proibida_na_fala"]:.2f}{risco}')
    print('\ncomposto = previsão direcional (não oráculo). risco-fala ≥0,50 = revisar blindagem de política.')
