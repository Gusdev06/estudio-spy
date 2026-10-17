# Swipe por palavra-chave na Ad Library: concorrentes da mentoria spy (17/10/2026)

Busca no Chrome logado, anúncios ativos, todos os países, ordenados por impressões. De cada busca entram só os ~30 anúncios do topo, porque a rolagem infinita não carregou mais nada com a aba em segundo plano. `coleta/` guarda o JSON cru de cada busca. `baixar.py` filtra as operações relevantes e baixa a mídia para `anuncios/`, nomeando cada arquivo como `<host>__<pagina>-<id>`. `manifest.json` traz página, data de início, link, copy e md5. `folha-contato.jpg` mostra os 63 criativos únicos.

| Busca (frase exata) | Resultados | O que trouxe |
|---|---|---|
| the truth always leaves traces / You don't need to accuse anyone / what the words are trying to hide | ~340 cada | a mesma operação: **love-vision.site** (Amanda suzana, Ariela Santos, Agatha Pereira) + raygort.site e igyhall.com com a mesma copy |
| love-vision.site (domínio) | **~2.100** | love-vision (+ página Emily Collins) |
| Analyze any @username | ~65 | **tryfidelo.com** (Silvia Amorin, Tori Larowe, Sarah Smith, Megan Rodriguez) + **spygran.site** (Sofia Rodriguez) |
| enter his phone number | ~1.600 | socialcatfish, reverselookup, deepscanner.app e muitos apps de localização (ruído) |
| without touching his phone | ~120 | reverselookup, apps de GPS e Lens AI (ruído) |
| without him knowing / sin que él lo sepa | ~270 / ~460 | quase tudo ruído (apps da Play Store) |
| who he's really talking to / see who he follows | 1 / 1 | Alicent (acessosegurosite.site) / app Toxic |

Performance não verificada: a Ad Library não expõe gasto. O único proxy de que o anúncio está funcionando é o tempo no ar (`inicio`) e quantas vezes o mesmo criativo se repete.
