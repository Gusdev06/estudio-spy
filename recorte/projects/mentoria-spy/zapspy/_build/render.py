# -*- coding: utf-8 -*-
"""Gera as variacoes do criativo ZapSpy (split-screen 'what you see vs what really happens').
Renderiza HTML -> PNG via Chrome headless. Uma alavanca variada por vez."""
import os, json
from string import Template

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(BASE, "_lib", "Montserrat-Variable.ttf")
FOTO = lambda n: "file://" + os.path.join(BASE, "_lib", "fotos", n + ".png")

# ---------------------------------------------------------------- icons (svg)
def ico(name, c="#fff"):
    p = {
      "eye":  '<circle cx="12" cy="12" r="3.2"/><path d="M1.5 12S5 5.5 12 5.5 22.5 12 22.5 12 19 18.5 12 18.5 1.5 12 1.5 12Z" fill="none" stroke="%s" stroke-width="2"/>' % c,
      "chat": '<path d="M3 5h18v12H8l-5 4V5Z"/>',
      "heart":'<path d="M12 21s-8-5.1-8-10.2A4.8 4.8 0 0 1 12 7.6 4.8 4.8 0 0 1 20 10.8C20 15.9 12 21 12 21Z"/>',
      "moon": '<path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z"/>',
      "bolt": '<path d="M13 2 4 14h6l-1 8 9-12h-6l1-8Z"/>',
      "pin":  '<path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/>',
      "search":'<circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="%s" stroke-width="2"/><path d="m15.5 15.5 5 5" stroke="%s" stroke-width="2"/>' % (c, c),
      "ghost":'<path d="M12 2a8 8 0 0 0-8 8v12l3-2 3 2 2-2 2 2 3-2 3 2V10a8 8 0 0 0-8-8Zm-3 8.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3Zm6 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3Z"/>',
      "clock":'<circle cx="12" cy="12" r="9" fill="none" stroke="%s" stroke-width="2"/><path d="M12 7v5.4l3.6 2.1" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round"/>' % (c, c),
      "check":'<path d="M20 6 9 17l-5-5" fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>' % c,
    }[name]
    return '<svg viewBox="0 0 24 24" fill="%s">%s</svg>' % (c, p)

CHEV = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m9 5 7 7-7 7"/></svg>'
IGGLYPH = ('<svg class="igg" viewBox="0 0 24 24" fill="none" stroke="url(#ig)" stroke-width="2">'
 '<defs><linearGradient id="ig" x1="0" y1="1" x2="1" y2="0">'
 '<stop offset="0" stop-color="#F9CE34"/><stop offset=".45" stop-color="#EE2A7B"/><stop offset="1" stop-color="#6228D7"/>'
 '</linearGradient></defs><rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/>'
 '<circle cx="12" cy="12" r="4.6"/><circle cx="17.6" cy="6.4" r="1.2" fill="url(#ig)" stroke="none"/></svg>')

# ---------------------------------------------------------------- html blocks
def alerts_html(items, grad):
    out = []
    for it in items:
        badge = ('<span class="badge">%s</span>' % it["badge"]) if it.get("badge") else ""
        big   = ('<div class="big">%s</div>' % it["big"]) if it.get("big") else ""
        out.append(
            '<div class="alert" style="background:%s">'
            '<div class="ai">%s%s</div>'
            '<div class="atx"><div class="at">%s</div>%s<div class="as">%s</div></div>'
            '%s</div>' % (grad, ico(it["icon"]), badge, it["title"], big, it["sub"], CHEV))
    return "\n".join(out)

def calm_html(items):
    out = []
    for it in items:
        if it.get("check"):
            out.append('<div class="calm"><div class="ci">%s</div>'
                       '<div class="ctx"><div class="ct">%s</div><div class="cs">%s</div>'
                       '<div class="cs">%s</div></div></div>'
                       % (ico("check", "#9aa0a6"), it["title"], it["sub"], it.get("sub2", "")))
        else:
            out.append('<div class="calm row"><div class="ctx"><div class="ct">%s</div>'
                       '<div class="cs">%s</div></div><div class="cnum">%s</div></div>'
                       % (it["title"], it["sub"], it["num"]))
    return "\n".join(out)

HILITES_L = ["Travel", "Life", "Work", "Moments"]
HL_FOTOS = ["travel", "life", "work", "moments"]

TPL = Template(r"""
<style>
@font-face{font-family:M;src:url("file://$FONT");font-weight:100 900;}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:1080px;height:1920px;overflow:hidden;background:#fff;
  font-family:M,"Helvetica Neue",Arial,sans-serif;-webkit-font-smoothing:antialiased;}
.wrap{width:1080px;height:1920px;display:flex;flex-direction:column;}

/* ---------- header ---------- */
.head{height:246px;background:$HEAD_GRAD;display:flex;align-items:center;position:relative;flex:0 0 246px;}
.head .h{flex:1;display:flex;align-items:center;justify-content:center;padding:0 70px 0 34px;}
.head .h+.h{padding:0 34px 0 70px;}
.head .h span{color:#fff;font-weight:900;font-size:$HSIZE;line-height:.94;text-transform:uppercase;
  text-align:center;letter-spacing:-1px;white-space:nowrap;text-shadow:0 3px 14px rgba(0,0,0,.22);}
.divider{position:absolute;left:50%;top:26px;bottom:26px;width:2px;margin-left:-1px;background:rgba(255,255,255,.35);}
.vs{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:86px;height:86px;border-radius:50%;
  background:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:34px;
  color:$VSCOLOR;box-shadow:0 6px 22px rgba(0,0,0,.28);letter-spacing:-.5px;}

/* ---------- body ---------- */
.body{flex:1;display:flex;gap:6px;background:$RING;}
.pane{width:537px;height:100%;overflow:hidden;position:relative;}
.left{background:#ededed;filter:grayscale(1) contrast(.94);}
.right{background:$RIGHT_BG;}

.tb{display:flex;align-items:center;justify-content:space-between;padding:26px 26px 6px;}
.tb .nm{font-size:25px;font-weight:600;}
.tb .ar,.tb .dots{font-size:30px;font-weight:400;}
.left .tb{color:#1a1a1a;} .right .tb{color:#fff;}

.prow{display:flex;align-items:center;padding:16px 26px 0;gap:26px;}
.avw{width:120px;height:120px;flex:0 0 120px;border-radius:50%;padding:4px;}
.av{width:100%;height:100%;border-radius:50%;background-image:url("$AVATAR_URL");
  background-size:cover;background-position:center 35%;}
.left .avw{background:#c9c9c9;} .left .av{border:3px solid #ededed;}
.right .avw{background:$RING;} .right .av{border:3px solid rgba(10,4,18,.72);}
.stats{display:flex;flex:1;justify-content:space-around;text-align:center;}
.stats b{display:block;font-size:26px;font-weight:700;}
.stats i{font-style:normal;font-size:19px;opacity:.72;}
.left .stats{color:#1a1a1a;} .right .stats{color:#fff;}

.bio{padding:20px 26px 0;line-height:1.42;}
.bio .n{font-size:24px;font-weight:700;}
.bio .l{font-size:21px;opacity:.78;}
.left .bio{color:#1a1a1a;} .right .bio{color:#fff;}

.btns{display:flex;gap:14px;padding:22px 26px 0;}
.btns div{flex:1;text-align:center;font-size:21px;font-weight:600;padding:15px 0;border-radius:10px;}
.left .btns div{background:#efefef;color:#1a1a1a;}
.right .btns div{background:transparent;border:2px solid $BTN;color:#fff;}

.hls{display:flex;gap:20px;padding:26px 26px 0;}
.hl{flex:1;text-align:center;}
.hl .cw{width:100%;aspect-ratio:1;border-radius:50%;padding:3px;margin-bottom:9px;}
.hl .c{width:100%;height:100%;border-radius:50%;background-size:cover;background-position:center;}
.hl .t{font-size:18px;}
.left .hl .cw{background:#c9c9c9;} .left .hl .c{border:2px solid #ededed;}
.left .hl .t{color:#333;}
.right .hl .cw{background:$RING;} .right .hl .c{border:2px solid rgba(10,4,18,.72);}
.right .hl .t{color:#fff;opacity:.9;}

.tabs{display:flex;margin-top:28px;border-top:1px solid rgba(128,128,128,.35);}
.tab{flex:1;padding:18px 0;display:flex;justify-content:center;}
.tab svg{width:32px;height:32px;opacity:.4;}
.tab.on svg{opacity:1;}
.tab.on{border-bottom:3px solid currentColor;}
.left .tabs{color:#1a1a1a;} .right .tabs{color:#fff;}

.list{padding:20px 20px 0;display:flex;flex-direction:column;gap:$GAP;}

/* calm cards (left) */
.calm{background:#fff;border:1px solid #e6e6e6;border-radius:14px;padding:22px 22px;display:flex;gap:16px;align-items:center;}
.calm.row{justify-content:space-between;}
.ci{width:34px;height:34px;flex:0 0 34px;}
.ci svg{width:100%;height:100%;}
.ct{font-size:22px;font-weight:700;color:#2b2b2b;}
.cs{font-size:17px;color:#9aa0a6;line-height:1.35;}
.cnum{font-size:30px;font-weight:700;color:#b9b9b9;}

/* alert cards (right) */
.alert{border-radius:16px;padding:20px 18px;display:flex;align-items:center;gap:16px;
  box-shadow:0 10px 26px rgba(0,0,0,.28);}
.ai{position:relative;width:52px;height:52px;flex:0 0 52px;border-radius:13px;
  background:rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center;}
.ai svg{width:31px;height:31px;}
.badge{position:absolute;top:-9px;right:-9px;min-width:30px;height:30px;border-radius:15px;background:#fff;
  color:#d62828;font-size:18px;font-weight:800;display:flex;align-items:center;justify-content:center;padding:0 7px;}
.atx{flex:1;color:#fff;}
.at{font-size:22px;font-weight:800;line-height:1.15;}
.big{font-size:40px;font-weight:900;line-height:1.05;margin:2px 0 1px;}
.as{font-size:17px;opacity:.92;line-height:1.3;}
.chev{width:26px;height:26px;flex:0 0 26px;}

/* ---------- footer ---------- */
.foot{flex:0 0 338px;background:$FOOT_BG;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:34px;padding:0 40px;}
.cta{font-weight:900;font-size:$CSIZE;line-height:.98;text-transform:uppercase;text-align:center;
  color:$CTA_COLOR;letter-spacing:-1.5px;}
.pill{display:flex;align-items:center;gap:16px;background:$PILL_BG;border-radius:999px;padding:19px 40px;
  border:3px solid transparent;background-image:linear-gradient($PILL_BG,$PILL_BG),$PILL_BORDER;
  background-origin:border-box;background-clip:padding-box,border-box;}
.pill span{font-size:29px;font-weight:700;color:$PILL_TXT;}
.igg{width:40px;height:40px;}
</style>

<div class="wrap">
  <div class="head">
    <div class="h"><span>$HL_LEFT</span></div>
    <div class="divider"></div>
    <div class="h"><span>$HL_RIGHT</span></div>
    <div class="vs">$VS</div>
  </div>

  <div class="body">
    <!-- LEFT -->
    <div class="pane left">
      <div class="tb"><div class="ar">&lsaquo;</div><div class="nm">your.profile</div><div class="dots">&#8943;</div></div>
      <div class="prow"><div class="avw"><div class="av"></div></div>
        <div class="stats"><div><b>128</b><i>Posts</i></div><div><b>2,543</b><i>Followers</i></div><div><b>562</b><i>Following</i></div></div>
      </div>
      <div class="bio"><div class="n">Your Profile</div><div class="l">Digital creator</div>
        <div class="l">Living the dream &#10024;</div><div class="l">&#128205; Everywhere</div></div>
      <div class="btns"><div>Edit Profile</div><div>Share Profile</div></div>
      <div class="hls">$HL_GRAY</div>
      <div class="tabs"><div class="tab on"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18"/><path d="M9 3v18M15 3v18M3 9h18M3 15h18"/></svg></div><div class="tab"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M3 8.5h18M8.5 3l3 5.5M15 3l3 5.5"/><path d="m11 12 4.5 2.6L11 17.2V12Z" fill="currentColor" stroke="none"/></svg></div><div class="tab"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 5.5h18v13H3z"/><circle cx="12" cy="10.5" r="2.6"/><path d="M7.5 18.5a4.5 4.5 0 0 1 9 0"/></svg></div></div>
      <div class="list">$CALM</div>
    </div>

    <!-- RIGHT -->
    <div class="pane right">
      <div class="tb"><div class="ar">&lsaquo;</div><div class="nm">your.profile</div><div class="dots">&#8943;</div></div>
      <div class="prow"><div class="avw"><div class="av"></div></div>
        <div class="stats"><div><b>128</b><i>Posts</i></div><div><b>2,543</b><i>Followers</i></div><div><b>562</b><i>Following</i></div></div>
      </div>
      <div class="bio"><div class="n">Your Profile</div><div class="l">Digital creator</div>
        <div class="l">Living the dream &#10024;</div><div class="l">&#128205; Everywhere</div></div>
      <div class="btns"><div>Edit Profile</div><div>Share Profile</div></div>
      <div class="hls">$HL_COLOR</div>
      <div class="tabs"><div class="tab on"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18"/><path d="M9 3v18M15 3v18M3 9h18M3 15h18"/></svg></div><div class="tab"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M3 8.5h18M8.5 3l3 5.5M15 3l3 5.5"/><path d="m11 12 4.5 2.6L11 17.2V12Z" fill="currentColor" stroke="none"/></svg></div><div class="tab"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 5.5h18v13H3z"/><circle cx="12" cy="10.5" r="2.6"/><path d="M7.5 18.5a4.5 4.5 0 0 1 9 0"/></svg></div></div>
      <div class="list">$ALERTS</div>
    </div>
  </div>

  <div class="foot">
    <div class="cta">$CTA</div>
    <div class="pill">$IG<span>$PILL</span></div>
  </div>
</div>
""")

def hl_html(color):
    out = []
    for i, t in enumerate(HILITES_L):
        out.append('<div class="hl"><div class="cw"><div class="c" style="background-image:url(\'%s\')"></div></div>'
                   '<div class="t">%s</div></div>' % (FOTO(HL_FOTOS[i]), t))
    return "".join(out)

# ---------------------------------------------------------------- base DNA
IG_GRAD   = "linear-gradient(100deg,#7b2ff7 0%,#c2179b 38%,#f0327a 62%,#ff8a00 100%)"
ALERT_IG  = "linear-gradient(95deg,#e0355a,#f07022)"
RIGHT_DARK= "linear-gradient(175deg,#1b0f2b 0%,#3a1440 45%,#6b2340 78%,#a83a2c 100%)"

CALM_BASE = [
  dict(check=1, title="No suspicious activity", sub="Your account activity is normal", sub2="Everything looks good!"),
  dict(title="Story Views", sub="Last 24 hours", num="86"),
  dict(title="Reactions", sub="No new reactions", num="0"),
  dict(title="Profile Visits", sub="Nothing unusual", num="0"),
]
CALM_SHORT = CALM_BASE[:3] + [dict(title="Unknown viewers", sub="None detected", num="0")]

ALERTS_BASE = [
  dict(icon="eye",  title="Secret story views", big="47", sub="People viewed your stories without being seen"),
  dict(icon="chat", title="Hidden DM conversations", badge="12", sub="12 conversations hidden from your inbox"),
  dict(icon="heart",title="Reactions from unknown accounts", badge="23", sub="23 reactions from people you don't follow"),
  dict(icon="moon", title="Stories watched at 3AM", sub="Someone watched your stories at 03:17 AM"),
]
ALERTS_STALKER = [
  dict(icon="ghost", title="Ghost followers watching you", big="31", sub="Accounts that watch everything and never like"),
  dict(icon="search",title="Profile searched by name", badge="9", sub="9 people looked you up this week"),
  dict(icon="eye",   title="Screenshots of your stories", badge="4", sub="4 stories saved before they expired"),
  dict(icon="pin",   title="Viewers outside your city", sub="Views from 3 locations you don't know"),
]
ALERTS_NIGHT = [
  dict(icon="moon", title="Late night viewers", big="18", sub="18 people opened your stories after 1 AM"),
  dict(icon="clock",title="Same account, every night", badge="27", sub="One profile watched you 27 nights in a row"),
  dict(icon="eye",  title="Watched right after posting", badge="6", sub="6 accounts open your story in under 60s"),
  dict(icon="chat", title="Typing... then deleted", sub="Someone started a DM at 03:41 AM and stopped"),
]

def variant(**kw):
    v = dict(
        FONT=FONT, HEAD_GRAD=IG_GRAD, VSCOLOR="#e0355a", VS="VS", HSIZE="54px",
        HL_LEFT="What<br>you see", HL_RIGHT="What really<br>happens",
        RIGHT_BG=RIGHT_DARK, AVATAR="linear-gradient(160deg,#ff9a5a,#c2185b 60%,#2b1740)",
        RING=IG_GRAD, BTN="rgba(255,255,255,.34)",
        ALERT_GRAD=ALERT_IG, ALERTS=ALERTS_BASE, CALM=CALM_BASE, GAP="16px",
        FOOT_BG="#ffffff", CTA_COLOR="#111111", CTA="Stop guessing.<br>Start knowing.", CSIZE="76px",
        PILL="Link in bio &#183; Limited access", PILL_BG="#ffffff", PILL_TXT="#111111",
        PILL_BORDER=IG_GRAD,
    )
    v.update(kw)
    return v

# ---------------------------------------------------------------- 10 variacoes
V = []
def add(vid, lever, **kw):
    V.append((vid, lever, variant(**kw)))

add("v00-replica-baseline", "nenhuma (replica do campeao, controle do teste)")

add("v01-hook-they-hide", "HOOK do topo -> promessa de ocultacao deliberada",
    HL_LEFT="What<br>you see", HL_RIGHT="What they<br>hide", VS="VS")

add("v02-hook-who-watching", "HOOK do topo -> pergunta direta (curiosidade)",
    HL_LEFT="Who's<br>watching you", HL_RIGHT="Now you'll<br>know", VS="&#8594;", HSIZE="49px")

add("v03-hook-instagram-shows", "HOOK do topo -> vilao nomeado (Instagram esconde)",
    HL_LEFT="What Instagram<br>shows you", HL_RIGHT="What Instagram<br>hides", HSIZE="41px")

add("v04-hook-your-app-vs-real", "HOOK do topo -> comparacao app x realidade",
    HL_LEFT="Your app<br>right now", HL_RIGHT="Your account<br>for real", HSIZE="49px")

add("v05-stack-stalker", "VALUE STACK -> revelacoes sobre quem te observa (ghost followers)",
    ALERTS=ALERTS_STALKER, CALM=CALM_SHORT)

add("v06-stack-night", "VALUE STACK -> angulo noturno (horario / recorrencia)",
    ALERTS=ALERTS_NIGHT, CALM=CALM_SHORT,
    HL_LEFT="What<br>you see", HL_RIGHT="What happens<br>at 3 AM", HSIZE="49px")

add("v07-cta-before-deleted", "CTA de baixo -> urgencia por perda (dado some)",
    CTA="See it before<br>they delete it.", PILL="Link in bio &#183; Free check")

add("v08-cta-30-seconds", "CTA de baixo -> baixo esforco / tempo (30 segundos)",
    CTA="Check yours in<br>30 seconds.", CSIZE="72px", PILL="Link in bio &#183; No password needed")

add("v09-tema-alerta-vermelho", "COR/TEMA -> alerta vermelho (quebra o padrao do feed IG)",
    HEAD_GRAD="linear-gradient(100deg,#8e0e1f 0%,#d21f2b 45%,#ff5a1f 100%)",
    VSCOLOR="#d21f2b", ALERT_GRAD="linear-gradient(95deg,#b3122a,#ff5a1f)",
    RIGHT_BG="linear-gradient(175deg,#1a0709 0%,#3d0d14 50%,#7d1a1c 100%)",
    RING="linear-gradient(100deg,#d21f2b,#ff5a1f)",
    AVATAR="linear-gradient(160deg,#ff7a45,#b3122a 60%,#2a0a0d)",
    FOOT_BG="#111111", CTA_COLOR="#ffffff", PILL_BG="#111111", PILL_TXT="#ffffff",
    PILL_BORDER="linear-gradient(100deg,#d21f2b,#ff5a1f)")

add("v10-tema-neon-verde", "COR/TEMA -> terminal neon verde (cara de ferramenta/tech)",
    HEAD_GRAD="linear-gradient(100deg,#06281f 0%,#0b6b4a 45%,#19e08a 100%)",
    VSCOLOR="#0b6b4a", ALERT_GRAD="linear-gradient(95deg,#0b6b4a,#19e08a)",
    RIGHT_BG="linear-gradient(175deg,#04120f 0%,#062a22 55%,#0a4a37 100%)",
    RING="linear-gradient(100deg,#19e08a,#0b6b4a)",
    AVATAR="linear-gradient(160deg,#19e08a,#0b6b4a 60%,#04120f)",
    FOOT_BG="#04120f", CTA_COLOR="#ffffff", PILL_BG="#04120f", PILL_TXT="#ffffff",
    PILL_BORDER="linear-gradient(100deg,#19e08a,#0b6b4a)")

# ---------------------------------------------------------------- write html
manifest = []
for vid, lever, v in V:
    html = TPL.substitute(
        FONT=v["FONT"], AVATAR_URL=FOTO("avatar"), HEAD_GRAD=v["HEAD_GRAD"], VSCOLOR=v["VSCOLOR"], VS=v["VS"], HSIZE=v["HSIZE"],
        HL_LEFT=v["HL_LEFT"], HL_RIGHT=v["HL_RIGHT"], RIGHT_BG=v["RIGHT_BG"], AVATAR=v["AVATAR"],
        RING=v["RING"], BTN=v["BTN"], GAP=v["GAP"],
        HL_GRAY=hl_html(False), HL_COLOR=hl_html(True),
        CALM=calm_html(v["CALM"]), ALERTS=alerts_html(v["ALERTS"], v["ALERT_GRAD"]),
        FOOT_BG=v["FOOT_BG"], CTA_COLOR=v["CTA_COLOR"], CTA=v["CTA"], CSIZE=v["CSIZE"],
        PILL=v["PILL"], PILL_BG=v["PILL_BG"], PILL_TXT=v["PILL_TXT"], PILL_BORDER=v["PILL_BORDER"],
        IG=IGGLYPH)
    p = os.path.join(BASE, "_build", vid + ".html")
    open(p, "w").write(html)
    manifest.append(dict(id=vid, alavanca=lever,
                         hook=v["HL_LEFT"].replace("<br>", " ") + " / " + v["HL_RIGHT"].replace("<br>", " "),
                         cta=v["CTA"].replace("<br>", " "), pill=v["PILL"].replace("&#183;", "-")))
open(os.path.join(BASE, "criativos", "manifest.json"), "w").write(json.dumps(manifest, indent=2, ensure_ascii=False))
print("\n".join(m["id"] for m in manifest))
