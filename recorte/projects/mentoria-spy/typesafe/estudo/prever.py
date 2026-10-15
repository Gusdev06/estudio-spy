# Roda a rubrica validada nos NOSSOS criativos novos + 2 âncoras do concorrente (referência conhecida).
# Ranking por composto = previsão direcional de conversão. Reporta também a flag de risco de política.
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rubrica import RUBRICA, PESOS, NEGATIVAS
from validacao import pontuar

NOSSOS = [
    # Flora formatos 2026-09-28 (hooks distintos)
    ('flora-f1-love',   {'headline': "Loving you doesn't stop them from cheating.", 'primeira_fala': "He said I love you every single night, and every night he cleared his chats before bed. Love isn't proof. Their phone is.", 'angulo': 'suspeita do parceiro', 'formato': 'talking head selfie, bedroom'}),
    ('flora-f2-clean',  {'headline': 'The sweetest partners have the cleanest phones.', 'primeira_fala': "No weird texts. No late-night calls. Nothing. Because it's all deleted.", 'angulo': 'suspeita do parceiro', 'formato': 'sem rosto, painéis do funil, voz sussurrada'}),
    ('flora-f3-redflags',{'headline': 'If they flip their phone face down, watch this.', 'primeira_fala': "Red flag number one: the phone is always face down. Number two: it goes to the bathroom with them. Number three: their chats are always empty.", 'angulo': 'suspeita do parceiro', 'formato': 'listicle, números gigantes, no carro'}),
    ('flora-f4-podcast',{'headline': 'Every cheater makes the same mistake.', 'primeira_fala': "They think deleting a message makes it disappear. It doesn't.", 'angulo': 'suspeita do parceiro', 'formato': 'podcast reeditado, dupla'}),
    ('flora-f5-notcrazy',{'headline': "I'm not crazy. I just saw the messages.", 'primeira_fala': "For months he told me I was paranoid. That I was imagining things. So I stopped asking, and I entered his number.", 'angulo': 'suspeita do parceiro (validação)', 'formato': 'split, rosto + prova, 1ª pessoa'}),
    # 121 secret hook (a copy é a MESMA nos 5 avatares -> pontua como 1 conceito; a diferença entre eles é avatar/público, não hook)
    ('121-secret-amiga',{'headline': "She says it's a friend. Friends don't text at 2am.", 'primeira_fala': "She says it's just a friend. Friends don't text at two in the morning, and friends don't get saved under a fake name.", 'angulo': 'acusação / suspeita do parceiro', 'formato': 'talking head, faixa vermelha, karaokê'}),
]
ANCORAS = [   # concorrente com sinal conhecido, pra situar o ranking
    ('*ancora Secret Revealed (escalou)', {'headline': '⭐️⭐️⭐️⭐️⭐️ (4.9/5.0) — try free, discover the whole truth', 'primeira_fala': 'sem dado (radar não baixa vídeo)', 'angulo': 'prova social / curiosidade', 'formato': 'sem dado'}),
    ('*ancora slogan fixo L9 (não gastou)', {'headline': 'THE WEBSITE IS JUST ONE CLICK AWAY.', 'primeira_fala': 'THE WEBSITE IS JUST ONE CLICK AWAY.', 'angulo': 'produto', 'formato': 'slogan fixo o vídeo todo'}),
]

if __name__ == '__main__':
    res = []
    for nome, est in NOSSOS + ANCORAS:
        v, comp = pontuar(est); v['_nome'] = nome; v['_composto'] = comp; res.append(v)
    res.sort(key=lambda l: -l['_composto'])
    print(f'{"criativo":34} {"composto":>8}  dor  curi  emo  conf  |risco fala')
    for l in res:
        print(f'{l["_nome"]:34} {l["_composto"]:>8.3f}  {l["dor_concreta"]:.2f} {l["loop_curiosidade"]:.2f} {l["carga_emocional"]:.2f} {l["confissao_primeira_pessoa"]:.2f}  |{l["promessa_proibida_na_fala"]:.2f}')
    json.dump(res, open(os.path.join(os.path.dirname(__file__), 'previsao-resultado.json'), 'w'), indent=1, ensure_ascii=False)
