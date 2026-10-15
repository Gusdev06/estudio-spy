# A rubrica do estudo: cada dimensão de decisão vira uma pergunta Jev, ancorada num padrão da evidência (01-evidencia.md).
# O estado de cada criativo é um objeto: {hook_na_tela, primeira_fala, headline, angulo, mecanismo, formato}.
# Score = situação concreta por nível (não intensidade). Noul = condição vale ou não.
# Uso: from rubrica import RUBRICA, PESOS, NEGATIVAS

RUBRICA = {
    # #7 gasto real: confissão inacabada = maior gasto; slogan fixo = menor. É a dimensão mais lastreada em dinheiro.
    'gancho_vs_slogan': {'type': 'score',
        'instructions': 'This is the very first thing a viewer sees and hears in a short social ad. Which best describes how it opens?',
        'criteria': [
            'A fixed product slogan or call-to-action shown on screen the whole video (e.g. "the website is one click away")',
            'A generic statement describing the product or what it does',
            'A statement of the viewer\'s pain or a curiosity gap about a partner',
            'A first-person confession that opens a personal story ("I found something I wasn\'t even looking for...")']},
    # #7 e C: confissão em 1ª pessoa é o maior correlato de gasto
    'confissao_primeira_pessoa': {'type': 'noul',
        'instructions': 'Does the opening sound like a real person confessing something that happened to them, rather than commanding or selling to the viewer?',
        'criteria': {'true': 'First-person confession/story ("I...", "he...", something that happened to me)',
                     'false': 'Command, question at the viewer, or product pitch'}},
    # família A: curiosidade sobre o objeto foi a headline que mais cresceu
    'loop_curiosidade': {'type': 'noul',
        'instructions': 'Does the hook open a curiosity gap the viewer feels they must close (what is being hidden / what was found)?',
        'criteria': {'true': 'Opens an unresolved loop about something hidden or discovered',
                     'false': 'States everything plainly, no open loop'}},
    # força do hook (parar o scroll)
    'carga_emocional': {'type': 'score',
        'instructions': 'How emotionally charged is this hook for someone who suspects their partner is cheating?',
        'criteria': [
            'Informational, calm, no emotional charge',
            'Mild concern or curiosity',
            'Strong emotion: jealousy, fear of betrayal, hurt',
            'Raw accusation or anger aimed at the viewer\'s situation']},
    # dor concreta do cotidiano (2am, celular virado, chats apagados)
    'dor_concreta': {'type': 'noul',
        'instructions': 'Does it point to a concrete everyday scene of suspicion the viewer would recognize?',
        'criteria': {'true': 'Concrete scene (texts at 2am, phone face down, deleted chats, fake contact name)',
                     'false': 'Abstract or vague, no specific scene'}},
    # #9 blindagem: promessa pesada só na imagem = sobrevive; falar hack/senha = risco de política (NEGATIVA)
    'promessa_proibida_na_fala': {'type': 'noul',
        'instructions': 'Do the SPOKEN words (not on-screen UI) explicitly claim hacking, spying, cloning, passwords, or location tracking?',
        'criteria': {'true': 'Spoken line claims hack/spy/clone/password/tracking',
                     'false': 'Spoken line stays emotional; any heavy claim is only shown in on-screen UI'}},
    # device: número/detalhe quebrado = "foi medido, não chutado"
    'especificidade': {'type': 'score',
        'instructions': 'How specific and concrete are the details in the creative (numbers, times, names)?',
        'criteria': [
            'Vague or round, no concrete detail',
            'Some concrete detail',
            'Broken specific details (e.g. "147 deleted, 52 recovered", "03:17 AM")']},
    # B intransferível: comando com palavra proibida não migra entre páginas; dor/curiosidade migra
    'transferivel': {'type': 'noul',
        'instructions': 'Is the core hook idea a reusable pain/curiosity angle that could run on many pages, rather than tied to a banned product command?',
        'criteria': {'true': 'Reusable pain/curiosity idea',
                     'false': 'Depends on an explicit product command that platforms reject'}},
}

# Combinação em código (composite-scoring): peso por dimensão. Negativas entram invertidas.
# Pesos iniciais = hipótese ancorada no gasto real (confissão/gancho pesam mais); serão RE-AJUSTADOS na validação.
PESOS = {
    'gancho_vs_slogan': 0.28,
    'confissao_primeira_pessoa': 0.20,
    'loop_curiosidade': 0.14,
    'carga_emocional': 0.14,
    'dor_concreta': 0.10,
    'especificidade': 0.06,
    'transferivel': 0.08,
    'promessa_proibida_na_fala': 0.00,   # não entra no score de conversão; é flag de risco à parte
}
NEGATIVAS = {'promessa_proibida_na_fala'}   # quanto MAIOR, PIOR (risco de política) — reportada separada
