import json, html, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = json.load(open("board-data.json")); B = D["base"]

def card(it):
    url = B + it["src"]; lab = html.escape(it["label"])
    media = (f'<video src="{url}" controls muted loop playsinline preload="metadata"></video>' if url.endswith(".mp4")
             else f'<a href="{url}" target="_blank" rel="noopener"><img src="{url}" alt="{lab}" loading="lazy"></a>')
    warn = " warn" if it["status"].startswith("provizoriu") else ""
    cut = f'<span class="cut">tăietură {html.escape(it["cut"])}</span>' if it.get("cut") else ""
    return f'''<li class="card"><div class="frame">{media}</div>
<div class="meta"><span class="lbl">{lab}</span><span class="pill{warn}">{html.escape(it["status"])}</span>{cut}
<a class="lnk" href="{url}" target="_blank" rel="noopener">deschide</a></div></li>'''

secs = "\n".join(f'''<section><h2>{html.escape(s["title"])}</h2><p class="note">{html.escape(s["note"])}</p>
<ul class="grid">{"".join(card(i) for i in s["items"])}</ul></section>''' for s in D["sections"])

open("board-yeti.html","w").write(f'''<!doctype html><html lang="ro"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>HeatYeti Board</title>
<style>
:root{{--bg:#f4f7fb;--card:#fff;--ink:#14212e;--mute:#5b6b7b;--line:#dbe4ee;--acc:#3b7fc4;--ok:#1f8a4c;--warn:#b26a00}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0f1720;--card:#17222e;--ink:#e6eef6;--mute:#93a4b5;--line:#253445;--acc:#7db6ee;--ok:#5ccf8c;--warn:#f0b35a}}}}
:root[data-theme="dark"]{{--bg:#0f1720;--card:#17222e;--ink:#e6eef6;--mute:#93a4b5;--line:#253445;--acc:#7db6ee;--ok:#5ccf8c;--warn:#f0b35a}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 system-ui,-apple-system,Segoe UI,sans-serif}}
header{{padding:24px 16px 8px;max-width:1200px;margin:auto}}h1{{margin:0;font-size:24px}}header p{{color:var(--mute);margin:4px 0 0}}
section{{max-width:1200px;margin:auto;padding:16px}}h2{{font-size:18px;margin:8px 0 2px}}.note{{color:var(--mute);margin:0 0 12px}}
.grid{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}}
.frame{{aspect-ratio:9/16;background:#0002}}.frame img,.frame video{{width:100%;height:100%;object-fit:cover;display:block}}
.meta{{padding:10px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}}.lbl{{font-weight:600;width:100%}}
.pill{{font-size:12px;padding:2px 8px;border-radius:99px;background:color-mix(in srgb,var(--ok) 15%,transparent);color:var(--ok)}}
.pill.warn{{background:color-mix(in srgb,var(--warn) 15%,transparent);color:var(--warn)}}
.cut{{font-size:12px;color:var(--mute)}}.lnk{{margin-left:auto;font-size:13px;color:var(--acc)}}
</style></head><body><header><h1>HeatYeti · tabla</h1><p>Copia HeatGrump cu halatul Yeti · {len(D["sections"])-1} secțiuni gata</p></header>
{secs}</body></html>''')
print("ok")
