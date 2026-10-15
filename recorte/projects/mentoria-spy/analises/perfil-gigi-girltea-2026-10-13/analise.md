# @gigi.girltea — teardown do perfil (2026-10-13)

Fonte: Apify (`instagram-profile-scraper` + `instagram-reel-scraper`, conta `vocational_eucalyptus`), 100 reels de 27/08 a 13/10/2026. Dados brutos em `raw/`, top 8 em `top8.jpg`.

## O que vende
**FollowOtter** (followotter.com): digita o @ de alguém e vê quem a pessoa seguiu por último, posts e destaques, com alerta contínuo. Assinatura (preço não aparece na home; "Get started" leva pro pricing). Mesma categoria do Spy Gram. Bio: "Visit the link for the tea ☕ / FollowOtter ⬇️" → linktr.ee/followotter.

## Números
- 1.333 seguidores, segue 43, 405 posts, conta pessoal (não business).
- 100 reels = **32,7 M views** em ~47 dias. Mediana 29,8 mil; topo 6,19 M (DdujCyqhBgD).
- 15 reels acima de 600 mil. Pior faixa: ~1 mil views. Distribuição de cauda longa: o volume compra os outliers.
- 2-4 reels por dia. Duração média 8 s. 100% "Original audio".
- Views/seguidor no topo: ~4.600x. A conta não precisa de base: o alcance vem do feed de não-seguidores.

## Por que funciona
1. **O vídeo não vende nada.** Mulher fazendo rotina banal (cozinhar, cortar legume, maquiagem), plano fixo de celular, 7-8 s, sem fala. Prende pelo movimento e pelo loop curto.
2. **A frase na tela é meme de relacionamento**, opinião forte sobre homem/traição/ex ("I'll trust 4 bald tires before I trust a bald man"). Gera identificação, compartilhamento entre amigas e comentário de debate. Nada de produto.
3. **A venda mora na legenda.** Toda legenda planta a palavra-chave: "just check his followspy", "FollowOtter.com exposed him". Quem se identificou com o meme lê a legenda e vai pro link.
4. **Hashtags fixas de nicho**: #lust #microcheating #cheatingex #breakup #breakuptok — empurra pro público feminino em contexto de desconfiança, que é exatamente o comprador.
5. **Volume + formato fixo.** Mesmo molde 100 vezes, só troca frase e cena. Barato de produzir, e cada post é um bilhete de loteria.
6. **Conta "persona"** (girl + tea = fofoca), não marca. Não parece anúncio, então não sofre o desconto de atenção que anúncio sofre.

## Risco que vi
Todos os vídeos mostram a mesma mulher em cozinha/banheiro de casa, com cara de conteúdo de outra criadora reaproveitado. Se for repost, é risco de denúncia por direitos autorais e queda de conta. Recriar a cena com avatar de IA (o teste de hoje em `criativos/Deaen6FBTXu-avatar-novo-2026-10-13/` é exatamente um reel desta conta) elimina esse risco.

## Como replicar pro Spy Gram
- Conta persona feminina (nicho fofoca/relacionamento), sem cara de marca, bio com o link.
- Vídeo: rotina banal 7-8 s, câmera fixa, sem fala, gerado com avatar próprio (Seedance video-edit = fidelidade; MiniMax H3 = barato).
- Frase na tela: meme de relacionamento, sem citar produto. Banco de frases é o ativo; testar 3-4 por dia.
- Legenda: frase-gatilho + palavra-chave do produto ("check his [Spy Gram]") + 5 hashtags fixas do nicho.
- Medir por mediana e por taxa de outlier (>500 mil), não por post.
- Em PT-BR e EN: o formato não depende da língua do vídeo, só da frase.
