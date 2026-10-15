# -*- coding: utf-8 -*-
"""Monta a galeria HTML auto-contida (imagens em base64) pra visualizar e baixar as pecas."""
import base64, glob, os, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

META = {
 "v00-replica-baseline":      ("Controle", "Baseline", "Réplica fiel do criativo-fonte em 1080×1920. É a régua: toda leitura de teste é contra esta peça.", "Nenhuma"),
 "v01-hook-they-hide":        ("Hook", "What they hide", "Troca o hook neutro por ocultação deliberada — passa a existir um vilão escondendo algo de você.", "Headline do topo"),
 "v02-hook-who-watching":     ("Hook", "Who's watching you", "Hook em pergunta direta + seta no lugar do selo VS. Aponta pra pessoa em vez de descrever a tela.", "Headline do topo"),
 "v03-hook-instagram-shows":  ("Hook", "Instagram shows / hides", "Nomeia o vilão. Mais específico e mais atritado — testa se citar a plataforma aumenta ou queima.", "Headline do topo"),
 "v04-hook-your-app-vs-real": ("Hook", "Your app vs for real", "Contrasta app x realidade em vez de ver x acontecer. Enquadra como falha da ferramenta.", "Headline do topo"),
 "v05-stack-stalker":         ("Value stack", "Quem te observa", "Troca as 4 revelações: ghost followers, buscas pelo seu nome, prints dos stories, viewers de fora da cidade.", "As 4 revelações"),
 "v06-stack-night":           ("Value stack", "Ângulo noturno", "Stack todo em torno de horário e recorrência: 27 noites seguidas, abriu em menos de 60s, digitou e apagou às 03:41.", "As 4 revelações + hook"),
 "v07-cta-before-deleted":    ("CTA", "Before they delete it", "CTA por urgência de perda — o dado some. Pill vira \"Free check\" pra baixar a barreira.", "Chamada do rodapé"),
 "v08-cta-30-seconds":        ("CTA", "In 30 seconds", "CTA por baixo esforço em vez de urgência. \"No password needed\" mata a objeção de segurança.", "Chamada do rodapé"),
 "v09-tema-alerta-vermelho":  ("Tema", "Alerta vermelho", "Sai do gradiente Instagram e vira vermelho de alerta, rodapé preto. Quebra padrão no feed.", "Paleta inteira"),
 "v10-tema-neon-verde":       ("Tema", "Terminal neon", "Verde neon sobre preto: lê como ferramenta técnica, não como rede social. Público diferente.", "Paleta inteira"),
}
COLORS = {"Controle":"#8b8b9a","Hook":"#f0327a","Value stack":"#ff8a00","CTA":"#19e08a","Tema":"#7b2ff7"}

def b64(p):
    return "data:image/jpeg;base64," + base64.b64encode(open(p,"rb").read()).decode()

cards, chips = [], []
files = sorted(glob.glob(os.path.join(BASE,"criativos","v*.jpg")))
for f in files:
    vid = os.path.basename(f).replace("-2026-08-22.jpg","")
    bloco, titulo, desc, alav = META[vid]
    cards.append(f'''
    <article class="card" data-b="{bloco}">
      <button class="shot" title="Ver em tamanho real">
        <img src="{b64(f)}" alt="{titulo}" data-name="{os.path.basename(f)}">
      </button>
      <div class="meta">
        <div class="tagrow"><span class="tag" style="--c:{COLORS[bloco]}">{bloco}</span><span class="vid">{vid.split('-')[0]}</span></div>
        <h2>{titulo}</h2>
        <p>{desc}</p>
        <div class="lev"><span>Alavanca variada</span><b>{alav}</b></div>
        <button class="dl">Baixar JPG</button>
      </div>
    </article>''')

orig = b64(os.path.join(BASE,"original","criativo-original.jpg"))

HTML = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ZapSpy — 11 criativos</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#0b0714;--card:#161022;--line:#2a2038;--tx:#f4f1f8;--mut:#9b93ab}}
body{{background:var(--bg);color:var(--tx);font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Helvetica,sans-serif;-webkit-font-smoothing:antialiased}}
header{{position:sticky;top:0;z-index:9;background:rgba(11,7,20,.88);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}}
.hin{{max-width:1560px;margin:0 auto;padding:20px 28px;display:flex;align-items:center;gap:24px;flex-wrap:wrap}}
.brand{{display:flex;align-items:baseline;gap:12px}}
.brand h1{{font-size:20px;font-weight:800;letter-spacing:-.4px}}
.brand span{{color:var(--mut);font-size:13px}}
.filters{{display:flex;gap:8px;flex-wrap:wrap;margin-left:auto}}
.f{{border:1px solid var(--line);background:transparent;color:var(--mut);padding:7px 15px;border-radius:999px;font-size:13px;font-weight:600;cursor:pointer;transition:.15s}}
.f:hover{{color:var(--tx);border-color:#453660}}
.f.on{{background:var(--tx);color:#0b0714;border-color:var(--tx)}}
.acts{{display:flex;gap:10px}}
.btn{{display:inline-flex;align-items:center;gap:8px;padding:9px 18px;border-radius:10px;font-size:13.5px;font-weight:700;text-decoration:none;border:1px solid var(--line);color:var(--tx);cursor:pointer;background:transparent;font-family:inherit;transition:.15s}}
.btn:hover{{border-color:#5a4780}}
.btn.p{{background:linear-gradient(100deg,#7b2ff7,#f0327a 60%,#ff8a00);border:none;color:#fff}}
.btn.p:hover{{filter:brightness(1.12)}}
main{{max-width:1560px;margin:0 auto;padding:32px 28px 80px}}
.intro{{display:grid;grid-template-columns:190px 1fr;gap:32px;align-items:start;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:26px;margin-bottom:36px}}
.intro img{{width:100%;border-radius:12px;display:block}}
.intro h2{{font-size:17px;margin-bottom:10px;letter-spacing:-.2px}}
.intro p{{color:#c8c1d6;max-width:78ch;margin-bottom:12px}}
.intro .warn{{color:#ffb27a;font-size:13.5px;border-left:2px solid #ff8a00;padding-left:12px}}
.intro .src{{color:var(--mut);font-size:12.5px;margin-top:14px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:26px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;display:flex;flex-direction:column;transition:.18s}}
.card:hover{{transform:translateY(-3px);border-color:#453660}}
.card.hide{{display:none}}
.shot{{display:block;background:#000;border:0;padding:0;cursor:zoom-in;width:100%;font:inherit}}
.shot img{{width:100%;display:block;aspect-ratio:9/16;object-fit:cover}}
.meta{{padding:18px 18px 20px;display:flex;flex-direction:column;gap:9px;flex:1}}
.tagrow{{display:flex;align-items:center;gap:9px}}
.tag{{font-size:10.5px;font-weight:800;letter-spacing:.9px;text-transform:uppercase;color:var(--c);border:1px solid color-mix(in srgb,var(--c) 45%,transparent);padding:3px 9px;border-radius:999px}}
.vid{{font-size:12px;color:var(--mut);font-weight:700;font-variant-numeric:tabular-nums}}
.meta h2{{font-size:17px;font-weight:700;letter-spacing:-.3px}}
.meta p{{font-size:13.5px;color:#b4abc4;flex:1}}
.lev{{border-top:1px solid var(--line);padding-top:11px;display:flex;justify-content:space-between;gap:12px;font-size:12px}}
.lev span{{color:var(--mut)}} .lev b{{text-align:right}}
.dl{{margin-top:4px;text-align:center;padding:10px;border-radius:10px;background:#221a33;color:var(--tx);text-decoration:none;font-size:13px;font-weight:700;transition:.15s}}
.dl:hover{{background:#2e2445}}
.dl{{border:0;cursor:pointer;font-family:inherit;width:100%}}
#lb{{position:fixed;inset:0;z-index:99;background:rgba(6,3,12,.94);display:none;align-items:center;justify-content:center;cursor:zoom-out;padding:28px}}
#lb.on{{display:flex}}
#lb img{{max-height:100%;max-width:100%;border-radius:10px;box-shadow:0 30px 90px rgba(0,0,0,.6)}}
footer{{max-width:1560px;margin:0 auto;padding:0 28px 60px;color:var(--mut);font-size:13px}}
footer code{{background:var(--card);padding:2px 7px;border-radius:5px;font-size:12px}}
@media(max-width:860px){{.intro{{grid-template-columns:1fr}} .filters{{margin-left:0}}}}
</style></head><body>

<header><div class="hin">
  <div class="brand"><h1>ZapSpy</h1><span>11 peças · 1080×1920</span></div>
  <div class="filters">
    <button class="f on" data-f="all">Todas</button>
    <button class="f" data-f="Controle">Controle</button>
    <button class="f" data-f="Hook">Hook</button>
    <button class="f" data-f="Value stack">Value stack</button>
    <button class="f" data-f="CTA">CTA</button>
    <button class="f" data-f="Tema">Tema</button>
  </div>
  <div class="acts">
    <a class="btn" href="criativos-zapspy-2026-08-22.zip" download>Baixar .zip</a>
    <button class="btn p" id="all">Baixar as 11</button>
  </div>
</div></header>

<div id="lb"><img alt=""></div>

<main>
  <section class="intro">
    <img src="{orig}" alt="Criativo original">
    <div>
      <h2>O criativo-fonte e o que foi variado</h2>
      <p><b>Mecanismo:</b> contraste do mesmo objeto. O mesmo perfil aparece duas vezes — cinza e
      "tudo normal" à esquerda, colorido e cheio de alertas à direita. Não vende uma feature:
      manufatura a suspeita de que existe uma camada escondida na conta que a pessoa já tem.</p>
      <p><b>DNA travada nas 11:</b> layout split-screen, mockup de UI nativa, cinza vs cor,
      números quebrados (47, 12, 23, 03:17) e o enquadramento "sua própria conta" — que é o que
      mantém o ângulo vendável. Cada variação mexe em <b>uma alavanca só</b>.</p>
      <p><b>Como ler o teste:</b> os blocos competem internamente (Hook: v01–v04 · Value stack:
      v05–v06 · CTA: v07–v08 · Tema: v09–v10), cada um contra o v00. Não misture blocos na mesma
      leitura ou você não sabe qual alavanca moveu o número.</p>
      <p class="warn">Performance não verificada: o fonte veio como URL de CDN, sem ad_id. Não é
      campeão validado — é referência estrutural. E respeite o piso de ~150 impressões antes de
      julgar peça individual.</p>
      <p class="src">Fonte: scontent.fbkk25-1.fna.fbcdn.net · 338×600 · baixado em 22/08/2026</p>
    </div>
  </section>
  <div class="grid">{"".join(cards)}</div>
</main>

<footer>Gerado por <code>_build/render.py</code> + <code>_build/galeria.py</code> · regerar as 11 peças custa ~15s e R$&nbsp;0,00 · <code>projects/zapspy/</code></footer>

<script>
document.querySelectorAll('.f').forEach(b=>b.onclick=()=>{{
  document.querySelectorAll('.f').forEach(x=>x.classList.remove('on'));
  b.classList.add('on');
  const f=b.dataset.f;
  document.querySelectorAll('.card').forEach(c=>
    c.classList.toggle('hide', f!=='all' && c.dataset.b!==f));
}});
const grab=c=>c.closest('.card').querySelector('img');
const save=img=>{{
  const a=document.createElement('a');
  a.href=img.src; a.download=img.dataset.name;
  document.body.appendChild(a); a.click(); a.remove();
}};
document.querySelectorAll('.dl').forEach(b=>b.onclick=()=>save(grab(b)));
const lb=document.getElementById('lb');
document.querySelectorAll('.shot').forEach(b=>b.onclick=()=>{{
  lb.querySelector('img').src=b.querySelector('img').src; lb.classList.add('on');
}});
lb.onclick=()=>lb.classList.remove('on');
addEventListener('keydown',e=>{{if(e.key==='Escape')lb.classList.remove('on')}});
document.getElementById('all').onclick=()=>{{
  const imgs=[...document.querySelectorAll('.card img')];
  imgs.forEach((img,i)=>setTimeout(()=>save(img), i*400));
}};
</script>
</body></html>'''

out = os.path.join(BASE, "galeria.html")
open(out,"w").write(HTML)
print(out, round(os.path.getsize(out)/1024/1024,2), "MB")
