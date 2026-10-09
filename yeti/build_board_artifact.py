# Construiește tabla Yeti ca artifact (media încorporată ca data: URI, fiindcă artifactul blochează linkurile externe).
import base64, html, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "yeti", "board-yeti-artifact.html")
TMP = os.path.join(os.path.dirname(OUT), "_media"); os.makedirs(TMP, exist_ok=True)

def ff(*a): subprocess.run(["ffmpeg", "-loglevel", "error", "-y", *a], check=True)
def uri(path, mime): return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()
def img(src, name, w=540):
    if name.startswith("c-"): w = 1600
    p = os.path.join(TMP, name + ".jpg"); ff("-i", src, "-vf", f"scale={w}:-1", "-q:v", "4", p); return uri(p, "image/jpeg")
def vid(src, name):
    v = os.path.join(TMP, name + ".mp4"); pz = os.path.join(TMP, name + "-p.jpg")
    ff("-i", src, "-vf", "scale=480:-2", "-c:v", "libx264", "-crf", "26", "-preset", "slow", "-an", "-movflags", "+faststart", v)
    ff("-i", src, "-frames:v", "1", "-vf", "scale=480:-2", "-q:v", "5", pz)
    return uri(v, "video/mp4"), uri(pz, "image/jpeg")

R = lambda p: os.path.join(ROOT, p)
import json as _json
_AP = os.path.join(ROOT, "yeti", "board-assets.json")
ASSETS = _json.load(open(_AP)) if os.path.exists(_AP) else {}   # reelN -> url din asset store (MP4 la rezoluție întreagă)
refs = [("Față, închis", "Gluga = capul Yeti, cordon, labe cu degete gri"),
        ("Față, deschis", "Căptușeala albastru-gheață pe toată lungimea"),
        ("Profil", "Același corn, aceeași ureche, fața din profil"),
        ("Spate", "Coarnele și urechile din spate, fără față")]
fixed = [("telecomanda-barbat", "Telecomandă", "Bărbat", "1 → 2 → 3", "1,2–3,6 s", "ok"),
         ("telecomanda-femeie", "Telecomandă", "Femeie", "1 → 2 → 3", "1,4–3,6 s", "ok"),
         ("telecomanda-barbat-inchis", "Telecomandă", "Bărbat · piele închisă", "1 → 2 → 3", "2,9–4,3 s încetinit", "ok"),
         ("conector-barbat", "Conector", "Bărbat", "intră complet", "1,7–3,5 s", "ok"),
         ("conector-femeie", "Conector", "Femeie", "intră complet", "1,7–3,5 s", "ok"),
         ("conector-barbat-inchis", "Conector", "Bărbat · piele închisă", "intră complet", "1,7–3,5 s", "ok")]

ref_cards = "".join(f'''<figure class="shot"><img src="{img(R(f"yeti/refs/yeti-ref{i+1}.png"), f"ref{i+1}")}" alt="{html.escape(t)}">
<figcaption><b>{html.escape(t)}</b><span>{html.escape(d)}</span></figcaption></figure>''' for i, (t, d) in enumerate(refs))
box = img(R("yeti/refs/cutie-heatyeti.png"), "box")

def fixed_cards(kind):
    out = []
    for f, k, who, res, cut, st in fixed:
        if k != kind: continue
        v, p = vid(R(f"output/yeti-fixed/{f}-taiat.mp4"), f)
        out.append(f'''<figure class="clip"><video src="{v}" poster="{p}" muted loop playsinline controls preload="metadata"></video>
<figcaption><b>{html.escape(who)}</b><span class="pill">{html.escape(res)}</span><span class="cut">tăietura {html.escape(cut)}</span></figcaption></figure>''')
    return "".join(out)

concepts = [
 ("A", "Ghețar", "A-ghetar", "Cel mai aproape de HeatGrump: albastru-gheață sus, alb jos, linia dintre ele în formă de țurțuri cu fir argintiu. Gluga e un cap de Yeti cu cornițe, urechi și moț alb."),
 ("B", "Blană de Yeti · ALES", "B-blana", "Tot halatul e blană albă lungă, ca un Yeti adevărat. Manșete-mănușă cu palmă gri și săculeții de jos în formă de labe uriașe cu degete gri."),
 ("C", "Munte", "C-munte", "Alb sus; jos un lanț de munți înzăpeziți pe albastru-ardezie, ca și cum Yeti vine din munți. Arată bine din toate unghiurile, munții se continuă pe spate."),
 ("D", "Gura Yeti", "D-gura", "Gluga e capul Yeti și fața ta iese prin gura lui, cu colți moi pe margine. Burtă albastră pe față, labe de Yeti la tiv. Cel mai amuzant pentru hook-uri."),
 ("E", "Noapte", "E-noapte", "Bleumarin închis sus, blană albă de Yeti jos, cu margine de nămete. Contrast puternic, se vede foarte bine în cadru și la lumină caldă."),
]
def concept_cards():
    out = []
    for k, name, f, d in concepts:
        src = img(R(f"yeti/concepts/{f}.png"), "c-" + f).replace("scale=540", "scale=540")
        out.append(f'''<figure class="sheet"><img src="{src}" alt="Concept {k} {html.escape(name)}">
<figcaption><b>{k} · {html.escape(name)}</b><span>{html.escape(d)}</span></figcaption></figure>''')
    return "".join(out)

OUTFIT = {1: "pijama în carouri bleumarin-gri", 2: "pijama în dungi crem-bleumarin", 3: "bluză bleumarin + pantaloni cu steagul SUA",
          4: "pulover crem împletit + pantaloni flanel albastru deschis", 5: "set lounge gri", 6: "pulover crem + pantaloni flanel (setul 4)",
          7: "pulover crem + blugi în mall, apoi pijama în dungi (setul 2)", 8: "hanorac bleumarin + pantaloni cu steagul SUA (setul 3)", 9: "geacă neagră + pijama în carouri afară, apoi B-roll reel 1", 10: "POV mână în mânecă gri, apoi B-roll reel 5", 11: "angajați în magazin, apoi B-roll reel 7",
          12: "pijama flanel în carouri bleumarin-gri", 13: "pulover crem împletit + pantaloni flanel albastru deschis", 14: "set lounge gri vafe", 15: "pijama în dungi crem-bleumarin"}
HOOK = {1: "tava din cuptor", 2: "desfăcut pe pat (POV)", 3: "rulou cu fundă", 4: "rulou care cade", 5: "aruncat ca o pelerină",
        6: "NOU · 3, 2, 1", 7: "NOU · magazin: îi cade cafeaua, coadă la vitrină", 8: "NOU · gifting „I'm freezing” / „Take this”", 9: "NOU 9 oct · afară în zăpadă, ruloul cade deschis (snuglore)", 10: "NOU 9 oct · POV halatul vidat în pungă (princess 83k)", 11: "NOU 9 oct · angajații trag cearșafurile, rând de capete Yeti (princess 6,7M)",
        12: "NOU v3 · el dă căldura jos la termostat (bip-bip)", 13: "NOU v3 · ruloul cu fundă se desface și cade pe umeri", 14: "NOU v3 · „conceptul”: aeroterma pusă jos, ea tot îngheață", 15: "NOU v3 · STORE HOOK: oamenii fug cu cutii HEAT YETI de pe palet"}
def reel_cards():
    out = []
    for n in range(1, 16):
        V = "v3" if n >= 12 else "v2"; key = f"{V}-reel{n}"
        src = R(f"output/yeti-reel{n}/yeti-reel{n}-{V}-FINAL.mp4"); v = os.path.join(TMP, f"{V}reel{n}.mp4"); pz = os.path.join(TMP, f"{V}reel{n}-p.jpg")
        if not os.path.exists(src): continue
        full = ASSETS.get(key, "")
        if not full:
            ff("-i", src, "-vf", "scale=540:-2", "-c:v", "libx264", "-crf", "27", "-preset", "slow", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", v)
        ff("-ss", "1", "-i", src, "-frames:v", "1", "-vf", "scale=540:-2", "-q:v", "5", pz)
        vsrc = full or uri(v, "video/mp4")
        txt = open(R(f"output/yeti-reel{n}/yeti-reel{n}-{V}.txt")).read().split("\n")
        head = html.escape(next((l.split(": ", 1)[1] for l in txt if l.startswith("TEXT PE ECRAN")), ""))
        cap = next((l[9:] for l in txt if l.startswith("CAPTION: ")), "")
        out.append(f'''<figure class="reel" data-id="{key}" data-file="heatyeti-reel{n}-{V}.mp4" data-src="{html.escape(full)}"><video src="{vsrc}" poster="{uri(pz, "image/jpeg")}" controls playsinline preload="metadata"></video>
<figcaption><b>Reel {n} <em class="st" data-st="none">Nevăzut</em></b><span>Hook: {html.escape(HOOK[n])}</span><span>Text: {head}</span><span>Dedesubt: {html.escape(OUTFIT[n])}</span><span class="cap">{html.escape(cap)}</span></figcaption>
<div class="review" aria-label="Părerea ta despre reel {n}">
  <div class="btns"><button type="button" class="ok" data-act="aprobat">Aprob</button><button type="button" class="no" data-act="refuzat">Refuz</button></div>
  <textarea rows="3" placeholder="Feedback: ce schimb la reel-ul ăsta?"></textarea>
  <div class="btns"><button type="button" class="save">Salvează feedback</button><button type="button" class="dl">Descarcă MP4</button></div>
  <small class="msg" aria-live="polite"></small>
</div></figure>''')
    return "".join(out)

steps = [(x, "gata", "done") for x in ("Hook (cu sunet)", "B1 · îmbracă", "B2 · deschide, cu fața", "Conector", "Telecomandă", "Cozy")]
flow = "".join(f'<li class="{c}"><span>{html.escape(n)}</span><em>{s}</em></li>' for n, s, c in steps)

page = f'''<title>HeatYeti Board</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Figtree:wght@400;500;600&display=swap">
<style>
/* Layout: o coloană lată; fiecare secțiune = o piesă din trusa produsului, în ordinea în care intră în reel */
:root{{--bg:#eef3f8;--paper:#ffffff;--ink:#132433;--mute:#5a6e80;--line:#d3dfea;--ice:#2f78b7;--ok:#1d7f49;--bad:#b3352b;--todo:#8a98a6;
--display:"Bricolage Grotesque",ui-sans-serif,system-ui,sans-serif;--body:"Figtree",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0d1620;--paper:#15212d;--ink:#e4eef7;--mute:#93a7b9;--line:#24384a;--ice:#8cc4f2;--ok:#62d08f;--bad:#ff7d72;--todo:#6f8193;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0d1620;--paper:#15212d;--ink:#e4eef7;--mute:#93a7b9;--line:#24384a;--ice:#8cc4f2;--ok:#62d08f;--bad:#ff7d72;--todo:#6f8193;color-scheme:dark}}
body{{background:var(--bg);color:var(--ink);font:15px/1.5 var(--body);padding:0 16px}}
.wrap{{max-width:1100px;margin:0 auto;padding-block:28px 56px;display:grid;gap:40px}}
header{{display:grid;gap:10px}}
.eyebrow{{font:600 12px/1 var(--body);letter-spacing:.12em;text-transform:uppercase;color:var(--ice)}}
h1{{font:800 clamp(34px,6vw,56px)/1 var(--display);margin:0;text-wrap:balance;letter-spacing:-.01em}}
.lead{{color:var(--mute);max-width:62ch;margin:0}}
.flow{{list-style:none;margin:6px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:8px}}
.flow li{{display:flex;gap:8px;align-items:baseline;border:1px solid var(--line);background:var(--paper);border-radius:999px;padding:6px 12px;font-size:13px}}
.flow li em{{font-style:normal;font-size:12px;color:var(--todo)}}
.flow li.done{{border-color:var(--ok)}}.flow li.done em{{color:var(--ok)}}
section{{display:grid;gap:14px}}
h2{{font:600 24px/1.15 var(--display);margin:0;text-wrap:balance}}
.note{{color:var(--mute);margin:0;max-width:65ch}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,210px),1fr));gap:14px}}
figure{{margin:0;min-width:0;display:grid;gap:8px}}
figure img,figure video{{width:100%;max-width:100%;aspect-ratio:9/16;object-fit:cover;border-radius:10px;background:var(--line);display:block}}
figcaption{{display:flex;flex-wrap:wrap;gap:4px 8px;align-items:baseline;font-size:14px}}
figcaption b{{font-weight:600;width:100%}}figcaption span{{color:var(--mute);font-size:13px}}
.pill{{color:var(--ok)!important;font-weight:600}}
.cut{{font-variant-numeric:tabular-nums;word-break:break-all}}.cap{{color:var(--ink)!important}}
.sheets{{display:grid;gap:22px}}.sheet img{{aspect-ratio:16/9;object-fit:contain;background:var(--paper)}}.sheet figcaption span{{max-width:75ch}}
.boxrow{{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr);gap:24px;align-items:start}}
.reels{{grid-template-columns:repeat(auto-fill,minmax(min(100%,240px),1fr))}}
.reel{{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:10px;align-content:start}}
.reel[data-st="aprobat"]{{border-color:var(--ok)}}.reel[data-st="refuzat"]{{border-color:var(--bad)}}
.st{{font:600 12px/1 var(--body);font-style:normal;padding:4px 8px;border-radius:999px;margin-left:6px;background:var(--line);color:var(--mute);vertical-align:2px}}
.st[data-st="aprobat"]{{background:var(--ok);color:var(--paper)}}.st[data-st="refuzat"]{{background:var(--bad);color:var(--paper)}}
.review{{display:grid;gap:8px}}
.btns{{display:flex;gap:8px}}
.review button{{flex:1;min-height:40px;border-radius:10px;border:1px solid var(--line);background:var(--bg);color:var(--ink);font:600 14px/1 var(--body);cursor:pointer}}
.review button:hover{{border-color:var(--ice)}}
.review button.ok[aria-pressed="true"]{{background:var(--ok);border-color:var(--ok);color:var(--paper)}}
.review button.no[aria-pressed="true"]{{background:var(--bad);border-color:var(--bad);color:var(--paper)}}
.review button:disabled{{opacity:.5;cursor:default}}
.review textarea{{width:100%;box-sizing:border-box;border-radius:10px;border:1px solid var(--line);background:var(--bg);color:var(--ink);font:14px/1.4 var(--body);padding:8px 10px;resize:vertical}}
.msg{{color:var(--mute);min-height:1em}}
.facts{{margin:0;display:grid;grid-template-columns:auto 1fr;gap:8px 16px;font-size:14px}}
.facts dt{{color:var(--mute)}}.facts dd{{margin:0}}
@media (max-width:640px){{.sheets{{display:grid;gap:22px}}.sheet img{{aspect-ratio:16/9;object-fit:contain;background:var(--paper)}}.sheet figcaption span{{max-width:75ch}}
.boxrow{{grid-template-columns:1fr}}}}
</style>
<div class="wrap">
<header>
  <span class="eyebrow">Copia HeatGrump · 3 octombrie</span>
  <h1>HeatYeti</h1>
  <p class="lead">Același halat termic, aceleași reguli și aceeași ordine de montaj ca la Grinch, doar cu designul Yeti. Halatul ales e conceptul B, Blană de Yeti. Mai jos e trusa de bază: halatul, cutia și clipurile fixe. Reel-urile v2 sunt mai jos.</p>
  <ul class="flow" aria-label="Ordinea de montaj">{flow}</ul>
</header>
<section>
  <h2>Reel-urile HeatYeti · v2 (regulile princesscomfortt)</h2>
  <p class="note">Refăcute pe regulile noi: hook după princesscomfortt cu sunet făcut de noi, B2 cu fața, fără unboxing, un singur text sus, muzică de Crăciun. Reel-urile 6, 7, 8 sunt noi. La fiecare: Aprob sau Refuz, scrie ce să schimb și apasă Salvează. Eu citesc direct de aici. Descarcă MP4 îți dă fișierul la rezoluție întreagă.</p>
  <p class="note" id="rvstate"></p>
  <div class="grid reels">{reel_cards()}</div>
</section>
<section>
  <h2>Halatul ales · B, Blană de Yeti</h2>
  <p class="note">Cele 4 referințe finale, făcute din foaia de design B. Gluga e aceeași în toate: două coarne gri, urechi, fața Yeti. Ele intră în fiecare B1, B2, cozy și unboxing.</p>
  <div class="grid">{ref_cards}</div>
</section>
<section>
  <h2>Cutia HEAT YETI</h2>
  <div class="boxrow">
    <figure class="shot"><img src="{box}" alt="Cutia HEAT YETI"></figure>
    <dl class="facts">
      <dt>Format</dt><dd>Identic cu cutia HeatGrump: fereastră transparentă, model pe dreapta, iconițe jos. Prin fereastră se vede blana albă și o labă de Yeti.</dd>
      <dt>Text</dt><dd>HEAT YETI · Heated Wearable Blanket Robe · Stay warm. Stay wild.</dd>
      <dt>Iconițe</dt><dd>6 Heat Levels · Auto-Off Timer · Ultra-Soft Sherpa, la fel ca pe cutia Grinch</dd>
      <dt>În unboxing</dt><dd>Cutia stă pe podea și fereastra se golește când scoate halatul</dd>
    </dl>
  </div>
</section>
<section>
  <h2>Telecomanda</h2>
  <p class="note">Clipurile Grinch aprobate, cu manșeta verde înlocuită în video de blana albă Yeti; luminițele urcă exact ca în originalele aprobate. Se arată bucata de montaj: pornește cu apăsarea, 1 → 2 → 3, una singură aprinsă.</p>
  <div class="grid">{fixed_cards("Telecomandă")}</div>
</section>
<section>
  <h2>Conectorul</h2>
  <p class="note">Gri, în două părți, cu fir la amândouă. Fiecare clip se termină cu conectorul intrat complet, fără gol.</p>
  <div class="grid">{fixed_cards("Conector")}</div>
</section>
<section>
  <h2>Conceptele</h2>
  <p class="note">Cele cinci direcții Yeti. Ai ales B; celelalte rămân ca idei.</p>
  <div class="sheets">{concept_cards()}</div>
</section>
</div>'''
page += "<script>" + open(R("yeti/board-review.js")).read() + "</script>"
open(OUT, "w").write(page)
print(OUT, round(os.path.getsize(OUT) / 1e6, 2), "MB")
