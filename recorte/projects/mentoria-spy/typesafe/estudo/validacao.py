# Valida a rubrica contra o ÚNICO rótulo com dinheiro real: gasto do Gerenciador das peças da casa (Spy Gram).
# Pontua cada peça com o Jev, correlaciona cada dimensão e o composto vs log10(gasto). n=8 => direcional, não estatístico.
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jev import ask, score_norm
from rubrica import RUBRICA, PESOS, NEGATIVAS

# Peças da casa com GASTO REAL (US$), da tabela de referência da 01-evidencia.md. Estado = o gancho + formato.
CASA = [
    ('GD-AD01', 4074.43, {'primeira_fala': "I found something I wasn't even looking for...", 'formato': 'talking head, woman ~28, bedroom, confession to camera', 'angulo': 'suspeita do parceiro', 'gancho_dura': 'caixa some aos 7-8s (não fixa)'}),
    ('SPY5',    1663.00, {'primeira_fala': 'a slogan line that fades out around 8.6s (not fixed)', 'formato': 'talking head, woman, car at night', 'angulo': 'suspeita do parceiro', 'gancho_dura': 'some aos 8,6s'}),
    ('GD-AD04',  610.92, {'primeira_fala': "You know when something just feels off...", 'formato': 'talking head, man ~30', 'angulo': 'suspeita do parceiro', 'gancho_dura': 'confissão'}),
    ('GD-AD05',  306.91, {'primeira_fala': "I kept thinking I would be the first to know...", 'formato': 'talking head, woman ~25, teary', 'angulo': 'suspeita do parceiro', 'gancho_dura': 'confissão'}),
    ('L9-slogan-alto', 50.00, {'primeira_fala': 'THE WEBSITE IS JUST ONE CLICK AWAY.', 'formato': 'fixed slogan on screen the whole video', 'angulo': 'produto', 'gancho_dura': 'fixo o vídeo todo'}),
    ('GD-AD03',   33.22, {'primeira_fala': "The worst part is realizing it was happening right in front of me...", 'formato': 'talking head, woman 45-55', 'angulo': 'suspeita do parceiro (passado)', 'gancho_dura': 'confissão morna, passado'}),
    ('GD-AD02',    9.09, {'primeira_fala': "You start noticing the little things...", 'formato': 'talking head, man ~35', 'angulo': 'suspeita do parceiro', 'gancho_dura': '1ª pessoa mas morno, sem promessa'}),
    ('L9-slogan-piso', 0.63, {'primeira_fala': 'THE WEBSITE IS JUST ONE CLICK AWAY.', 'formato': 'fixed slogan on screen the whole video', 'angulo': 'produto', 'gancho_dura': 'fixo o vídeo todo'}),
]

def pontuar(estado):
    r = ask(estado, RUBRICA)['answers']; v = {}
    for k, a in r.items():
        v[k] = score_norm(a) if a['type'] == 'score' else a['noul']
    comp = sum(PESOS[k] * (1 - v[k] if k in NEGATIVAS else v[k]) for k in PESOS)
    return v, comp

def spearman(xs, ys):
    def rank(z):
        o = sorted(range(len(z)), key=lambda i: z[i]); r = [0] * len(z)
        for pos, i in enumerate(o): r[i] = pos
        return r
    rx, ry = rank(xs), rank(ys); n = len(xs)
    d2 = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return 1 - 6 * d2 / (n * (n * n - 1))

if __name__ == '__main__':
    linhas = []
    for nome, gasto, est in CASA:
        v, comp = pontuar(est); v['_composto'] = comp; v['_gasto'] = gasto; v['_nome'] = nome
        linhas.append(v); print(f'{nome:18} gasto US${gasto:8.2f} composto {comp:.3f}')
    log_gasto = [math.log10(l['_gasto'] + 1) for l in linhas]
    print('\nCorrelação de Spearman (dimensão × log gasto real), n=8:')
    dims = [k for k in RUBRICA] + ['_composto']
    for d in sorted(dims, key=lambda d: -spearman([l[d] for l in linhas], log_gasto)):
        print(f'  {d:26} rho={spearman([l[d] for l in linhas], log_gasto):+.2f}')
    json.dump(linhas, open(os.path.join(os.path.dirname(__file__), 'validacao-resultado.json'), 'w'), indent=1, ensure_ascii=False)
    # ranking previsto vs real
    prev = sorted(linhas, key=lambda l: -l['_composto']); real = sorted(linhas, key=lambda l: -l['_gasto'])
    print('\nranking previsto (composto)  |  ranking real (gasto)')
    for a, b in zip(prev, real): print(f'  {a["_nome"]:18} | {b["_nome"]}')
