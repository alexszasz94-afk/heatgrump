import json, html, datetime

D = json.load(open("./data.json"))
BASE = D["base_media"]
ORDER = [("UNBOXING","Unboxing"),("B1","B1 · îmbracă halatul"),("B2","B2 · deschide halatul"),("CONECTOR","Conector"),("TELECOMANDA","Telecomandă"),("COZY","Cozy")]
STATUS = {"video":("gata","ok"),"plate":("placă · de aprobat","plate"),"pending":("se reface","pend")}

def slot(i, key, label, c):
    kind = c["kind"]; url = c.get("url","")
    st, cls = STATUS[kind]
    if kind == "video":
        media = f'<video src="{url}" controls muted playsinline preload="metadata"></video>'
    elif kind == "plate":
        media = f'<a href="{url}" target="_blank" rel="noopener"><img src="{url}" alt="{html.escape(label)}"></a>'
    else:
        media = '<div class="empty">se reface</div>'
    links = ""
    if url:
        links = (f'<a class="lnk" href="{url}" target="_blank" rel="noopener">deschide</a>'
                 f'<button class="lnk cp" type="button" data-url="{url}">copiază link</button>')
    return f'''<li class="slot {cls}">
  <div class="slot-head"><span class="num">{i}</span><span class="lbl">{html.escape(label)}</span></div>
  <div class="frame">{media}</div>
  <div class="slot-foot"><span class="pill {cls}">{st}</span><span class="links">{links}</span></div>
</li>'''

def reel(r):
    n = r["n"]; ch = r["char"]; rm = r["room"]
    clips = r["clips"]
    done = sum(1 for k,_ in ORDER if clips[k]["kind"]=="video")
    plates = sum(1 for k,_ in ORDER if clips[k]["kind"]=="plate")
    pend = sum(1 for k,_ in ORDER if clips[k]["kind"]=="pending")
    slots = "\n".join(slot(i+1,k,l,clips[k]) for i,(k,l) in enumerate(ORDER))
    return f'''<section class="reel" id="reel{n}">
  <header class="reel-head">
    <h2>Reel {n}</h2>
    <span class="chip">B2 {html.escape(r["b2"])}</span>
    <span class="counts"><b>{done}</b> clipuri gata · <b>{plates}</b> plăci de aprobat{(' · <b>'+str(pend)+'</b> se reface') if pend else ''}</span>
  </header>
  <div class="reel-body">
    <aside class="refs">
      <div class="ref"><span class="eyebrow">Personaj</span><div class="frame"><a href="{BASE}{ch}.jpg" target="_blank" rel="noopener"><img src="{BASE}{ch}.jpg" alt="Personaj reel {n}"></a></div><code>{ch[:8]}</code></div>
      <div class="ref"><span class="eyebrow">Cameră</span><div class="frame"><a href="{BASE}{rm}.jpg" target="_blank" rel="noopener"><img src="{BASE}{rm}.jpg" alt="Cameră reel {n}"></a></div><code>{rm[:8]}</code></div>
    </aside>
    <ol class="strip">
{slots}
    </ol>
  </div>
{hooks_block(r)}
</section>'''

HOOK_KIND = {"problem":"problem vs solution","reaction":"reacție","twist":"neașteptat"}

def hook_card(i, h):
    url = h.get("frame","")
    if h.get("status") == "pending":
        media = '<div class="empty">se generează</div>'; links = ""
    else:
        media = f'<a href="{url}" target="_blank" rel="noopener"><img src="{url}" alt="{html.escape(h["title"])}"></a>'
        links = (f'<a class="lnk" href="{url}" target="_blank" rel="noopener">deschide</a>'
                 f'<button class="lnk cp" type="button" data-url="{url}">copiază link</button>')
    if h.get("video"):
        media = f'<video src="{h["video"]}" controls muted playsinline preload="metadata"></video>'
        links = (f'<a class="lnk" href="{h["video"]}" target="_blank" rel="noopener">deschide</a>'
                 f'<button class="lnk cp" type="button" data-url="{h["video"]}">copiază link</button>')
    st = "hook animat" if h.get("video") else "start frame"
    cls = "ok" if h.get("video") else "hook"
    return f'''<li class="hook">
  <div class="frame">{media}</div>
  <div class="hook-text">
    <div class="hook-head"><span class="num">{i}</span><span class="lbl">{html.escape(h["title"])}</span><span class="chip">{HOOK_KIND.get(h["kind"], h["kind"])}</span></div>
    <p class="cadru"><b>Cadrul:</b> {html.escape(h["frame_desc"])}</p>
    <p class="miscare"><b>Acțiunea (4–5 s):</b> {html.escape(h["motion"])}</p>
    <p class="linia"><b>Text CapCut:</b> <span class="en">{html.escape(h["line"])}</span></p>
    {('<p class="linia"><b>Variantă text:</b> <span class="en">'+html.escape(h["alt"])+'</span></p>') if h.get("alt") else ''}
    {('<p class="bridge"><b>Legătura cu B-roll:</b> '+html.escape(h["bridge"])+'</p>') if h.get("bridge") else ''}
    <p class="dece"><b>De ce:</b> {html.escape(h["why"])}</p>
    <div class="slot-foot"><span class="pill {cls}">{st}</span><span class="links">{links}</span></div>
  </div>
</li>'''

def hooks_block(r):
    hs = r.get("hooks") or []
    if not hs: return ""
    cards = "\n".join(hook_card(i+1,h) for i,h in enumerate(hs))
    return f'''  <div class="hooks">
    <div class="hooks-head"><span class="eyebrow">3 idei de hook · fără halat în cadru · un start frame, o acțiune · textul îl pui în CapCut</span></div>
    <ol class="hook-list">
{cards}
    </ol>
  </div>'''

tot_v = sum(1 for r in D["reels"] for k,_ in ORDER if r["clips"][k]["kind"]=="video")
tot_p = sum(1 for r in D["reels"] for k,_ in ORDER if r["clips"][k]["kind"]=="plate")
tot_x = sum(1 for r in D["reels"] for k,_ in ORDER if r["clips"][k]["kind"]=="pending")
stamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

page = f'''<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Grinch Reel Board</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Barlow:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
:root{{
  color-scheme:light;
  --bg:#F4F2EC; --panel:#FBFAF7; --ink:#1B1D1B; --muted:#6C7066; --line:#D9D6CC;
  --green:#5E7B36; --green-ink:#FFFFFF; --red:#B23A2E; --amber:#B7791F; --amber-bg:#F6E9CF; --green-bg:#E4ECD5; --red-bg:#F3DCD8;
  --shadow:0 1px 2px rgba(20,22,18,.08), 0 8px 24px -12px rgba(20,22,18,.25);
}}
@media (prefers-color-scheme:dark){{
  :root:not([data-theme="light"]){{
    color-scheme:dark;
    --bg:#131512; --panel:#1B1E1A; --ink:#ECEAE2; --muted:#9BA094; --line:#2E322B;
    --green:#A3C36A; --green-ink:#131512; --red:#E4705F; --amber:#E0A84A; --amber-bg:#3A2E14; --green-bg:#26331A; --red-bg:#3F1F1A;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -12px rgba(0,0,0,.6);
  }}
}}
:root[data-theme="dark"]{{
  color-scheme:dark;
  --bg:#131512; --panel:#1B1E1A; --ink:#ECEAE2; --muted:#9BA094; --line:#2E322B;
  --green:#A3C36A; --green-ink:#131512; --red:#E4705F; --amber:#E0A84A; --amber-bg:#3A2E14; --green-bg:#26331A; --red-bg:#3F1F1A;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -12px rgba(0,0,0,.6);
}}
*{{box-sizing:border-box}}
html,body{{margin:0}}
body{{background:var(--bg);color:var(--ink);font:15px/1.5 "Barlow",system-ui,sans-serif;padding-block:0 48px;padding-inline:clamp(16px,3vw,40px)}}
h1,h2{{font-family:"Barlow Condensed","Arial Narrow",sans-serif;text-transform:uppercase;letter-spacing:.02em;margin:0;text-wrap:balance}}
.top{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding-block:14px 12px;display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 22px}}
.top h1{{font-size:clamp(26px,4vw,38px);font-weight:700;line-height:1}}
.top h1 em{{font-style:normal;color:var(--red)}}
.top .meta{{color:var(--muted);font-size:13px}}
.top nav{{margin-left:auto;display:flex;gap:6px;flex-wrap:wrap}}
.top nav a{{font-family:"Barlow Condensed",sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:.04em;font-size:14px;color:var(--ink);text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:2px 11px;background:var(--panel)}}
.top nav a:hover,.top nav a:focus-visible{{border-color:var(--green);outline:none}}
.legend{{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;padding-block:14px 6px;color:var(--muted);font-size:13.5px}}
.legend .order{{font-weight:600;color:var(--ink)}}
.legend .order span{{color:var(--muted);font-weight:400}}
.reel{{margin-top:28px;background:var(--panel);border:1px solid var(--line);border-radius:14px;box-shadow:var(--shadow);overflow:hidden}}
.reel-head{{display:flex;flex-wrap:wrap;align-items:center;gap:8px 16px;padding:14px 18px 10px;border-bottom:1px solid var(--line)}}
.reel-head h2{{font-size:30px;font-weight:700;line-height:1}}
.chip{{font-family:"Barlow Condensed",sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:.05em;font-size:13px;border:1px solid var(--line);border-radius:999px;padding:2px 10px;color:var(--muted)}}
.counts{{margin-left:auto;color:var(--muted);font-size:13.5px;font-variant-numeric:tabular-nums}}
.counts b{{color:var(--ink);font-weight:600}}
.reel-body{{display:flex;gap:0;align-items:stretch}}
.refs{{flex:0 0 auto;display:flex;gap:12px;padding:16px 18px;border-right:1px dashed var(--line);background:color-mix(in srgb,var(--panel) 70%,var(--bg))}}
.ref{{display:flex;flex-direction:column;gap:6px;width:112px}}
.ref .frame{{aspect-ratio:9/16}}
.ref code{{font:12px "JetBrains Mono",ui-monospace,monospace;color:var(--muted)}}
.eyebrow{{font-family:"Barlow Condensed",sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:.08em;font-size:12.5px;color:var(--muted)}}
.strip{{list-style:none;margin:0;padding:16px 18px;display:flex;gap:0;overflow-x:auto;flex:1 1 auto;scroll-snap-type:x proximity}}
.slot{{flex:0 0 auto;width:176px;display:flex;flex-direction:column;gap:8px;position:relative;padding-right:30px;scroll-snap-align:start}}
.slot+.slot::before{{content:"";position:absolute;left:-30px;top:calc(50% - 8px);width:30px;height:0;border-top:2px solid var(--line)}}
.slot+.slot::after{{content:"";position:absolute;left:-9px;top:calc(50% - 13px);width:8px;height:8px;border-right:2px solid var(--line);border-top:2px solid var(--line);transform:rotate(45deg)}}
.slot:last-child{{padding-right:0}}
.slot-head{{display:flex;align-items:baseline;gap:8px;min-height:2.6em}}
.num{{font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:20px;line-height:1;color:var(--green)}}
.slot.plate .num{{color:var(--amber)}} .slot.pend .num{{color:var(--red)}}
.lbl{{font-weight:600;font-size:14px;line-height:1.2}}
.frame{{width:100%;aspect-ratio:9/16;max-width:100%;background:#0e100e;border-radius:8px;overflow:hidden;border:1px solid var(--line)}}
.frame img,.frame video{{width:100%;height:100%;object-fit:cover;display:block}}
.frame .empty{{height:100%;display:grid;place-items:center;color:var(--red);font-family:"Barlow Condensed",sans-serif;text-transform:uppercase;letter-spacing:.06em;font-size:16px;background:repeating-linear-gradient(135deg,transparent 0 10px,rgba(255,255,255,.04) 10px 20px)}}
.slot-foot{{display:flex;flex-direction:column;gap:6px}}
.pill{{align-self:flex-start;font-family:"Barlow Condensed",sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:.05em;font-size:12.5px;border-radius:999px;padding:2px 9px}}
.pill.ok{{background:var(--green-bg);color:var(--green)}} .pill.plate{{background:var(--amber-bg);color:var(--amber)}} .pill.pend{{background:var(--red-bg);color:var(--red)}}
.links{{display:flex;gap:10px;font-size:13px}}
.lnk{{color:var(--green);text-decoration:underline;text-underline-offset:2px;background:none;border:0;padding:0;font:inherit;cursor:pointer}}
.lnk:focus-visible{{outline:2px solid var(--green);outline-offset:2px;border-radius:2px}}
.hooks{{border-top:1px dashed var(--line);padding:14px 18px 18px;background:color-mix(in srgb,var(--panel) 85%,var(--bg))}}
.hooks-head{{margin-bottom:10px}}
.hook-list{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:16px}}
.hook{{display:flex;gap:14px;align-items:flex-start}}
.hook .frame{{flex:0 0 150px;width:150px}}
.hook-text{{flex:1 1 auto;min-width:0;display:flex;flex-direction:column;gap:6px;font-size:13.5px;line-height:1.45}}
.hook-text p{{margin:0}}
.hook-head{{display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.hook-head .num{{color:var(--red)}}
.hook-text .en{{font-style:italic}}
.pill.hook{{background:var(--red-bg);color:var(--red)}}
@media (max-width:720px){{.hook{{flex-direction:column}} .hook .frame{{width:100%;flex-basis:auto}}}}
.toast{{position:fixed;left:50%;bottom:calc(18px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:8px 14px;border-radius:999px;font-size:13px;opacity:0;transition:opacity .2s;pointer-events:none}}
.toast.show{{opacity:1}}
@media (max-width:720px){{
  .reel-body{{flex-direction:column}}
  .refs{{border-right:0;border-bottom:1px dashed var(--line)}}
  .slot{{width:150px}}
}}
@media (prefers-reduced-motion:reduce){{.toast{{transition:none}}}}
</style>
</head>
<body>
<header class="top">
  <h1>Heat<em>Grump</em> · 5 reel-uri</h1>
  <span class="meta">actualizat {stamp} · {tot_v} clipuri gata · {tot_p} plăci de aprobat{(' · '+str(tot_x)+' se refac') if tot_x else ''}</span>
  <nav>{"".join(f'<a href="#reel{r["n"]}">Reel {r["n"]}</a>' for r in D["reels"])}</nav>
</header>
<p class="legend">
  <span class="order">Ordinea de montaj <span>(după reel-ul 5 aprobat; hook-ul îl pui tu în față):</span> unboxing → B1 → B2 → conector → telecomandă → cozy</span>
  <span><span class="pill ok">gata</span> clip final, 1080p</span>
  <span><span class="pill plate">placă · de aprobat</span> start frame; videoul se face după ok-ul tău</span>
  <span><span class="pill pend">se reface</span> respins de filtru, retrimis</span>
</p>
{"".join(reel(r) for r in D["reels"])}
<div class="toast" id="toast" role="status" aria-live="polite">Link copiat</div>
<script>
(function(){{
  var toast=document.getElementById('toast'),t;
  function show(msg){{toast.textContent=msg;toast.classList.add('show');clearTimeout(t);t=setTimeout(function(){{toast.classList.remove('show')}},1400)}}
  document.addEventListener('click',function(e){{
    var b=e.target.closest('.cp');if(!b)return;
    var url=b.getAttribute('data-url');
    var p=(navigator.clipboard&&navigator.clipboard.writeText)?navigator.clipboard.writeText(url):Promise.reject();
    p.then(function(){{show('Link copiat')}}).catch(function(){{
      var ta=document.createElement('textarea');ta.value=url;document.body.appendChild(ta);ta.select();
      try{{document.execCommand('copy');show('Link copiat')}}catch(err){{show('Nu s-a putut copia — deschide linkul')}}
      document.body.removeChild(ta);
    }});
  }});
  // pause other videos when one starts
  document.addEventListener('play',function(e){{
    if(e.target.tagName!=='VIDEO')return;
    document.querySelectorAll('video').forEach(function(v){{if(v!==e.target)v.pause()}});
  }},true);
}})();
</script>
</body>
</html>'''
open("./grinch-reel-board.html","w").write(page)
print("written", len(page))
