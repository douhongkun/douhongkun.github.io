# -*- coding: utf-8 -*-
"""Generate a polished static HTML preview of the academic homepage."""
from pathlib import Path
import re
import html
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "preview"
OUT.mkdir(exist_ok=True)
(OUT / "images").mkdir(exist_ok=True)
for name in ("profile.jpg", "profile.png"):
    src = ROOT / "images" / name
    if src.exists():
        shutil.copy2(src, OUT / "images" / name)

def read_md_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2].strip()
    text = re.sub(r"\{%.*?%\}", "", text, flags=re.S)
    text = re.sub(r"\{\{.*?\}\}", "", text, flags=re.S)
    return text.strip()

def inline(t: str) -> str:
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', t)
    return t

def md_to_html(md: str) -> str:
    md = re.sub(r"^(.+)\n======\s*$", r"## \1", md, flags=re.M)
    lines = md.splitlines()
    out, para = [], []
    in_ul = False

    def flush_para():
        nonlocal para
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para = []

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    for i, line in enumerate(lines):
        if line.startswith("### "):
            flush_para(); close_ul()
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            flush_para(); close_ul()
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("* ") or line.startswith("- "):
            flush_para()
            if not in_ul:
                out.append("<ul>"); in_ul = True
            out.append(f"<li>{inline(line[2:])}</li>")
        elif line.startswith("  * "):
            out.append(f"<ul class='sub'><li>{inline(line[4:])}</li></ul>")
        elif line.strip() == "":
            flush_para(); close_ul()
        else:
            para.append(line)
    flush_para(); close_ul()
    return "\n".join(out)

def parse_publications():
    pubs = {"manuscripts": [], "conferences": []}
    for path in Path(ROOT / "_publications").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        meta = {}
        if text.startswith("---"):
            for line in text.split("---", 2)[1].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip("'\"")
        cat = meta.get("category", "manuscripts")
        citation = meta.get("citation", "").replace("&quot;", '"')
        citation = citation.replace("<i>", "<em>").replace("</i>", "</em>")
        citation = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", citation)
        pubs.setdefault(cat, []).append({
            "title": meta.get("title", path.stem),
            "venue": meta.get("venue", ""),
            "citation": citation,
            "date": meta.get("date", ""),
            "first": "**Dou, H.**" in meta.get("citation", "") and meta.get("citation", "").lstrip().startswith("**Dou") or meta.get("citation", "").startswith("Dou, H."),
        })
    for k in pubs:
        pubs[k].sort(key=lambda x: x["date"], reverse=True)
    return pubs

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Hongkun Dou</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&family=Source+Serif+4:opsz,wght@8..60,500;8..60,650&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #f3f6f9;
  --card: #ffffff;
  --ink: #1b2838;
  --muted: #5b6b7c;
  --accent: #1f4e79;
  --accent-soft: #e8f0f7;
  --line: #d7e0ea;
  --shadow: 0 10px 30px rgba(27,40,56,.06);
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font-family: "Source Sans 3", "Segoe UI", sans-serif;
  color: var(--ink);
  line-height: 1.65;
  background:
    radial-gradient(1200px 500px at 10% -10%, #dceaf5 0%, transparent 55%),
    radial-gradient(900px 400px at 100% 0%, #eef3f8 0%, transparent 45%),
    var(--bg);
}}
.wrap {{
  max-width: 1100px; margin: 0 auto; padding: 28px 20px 64px;
  display: grid; grid-template-columns: 260px 1fr; gap: 28px;
}}
@media (max-width: 880px) {{ .wrap {{ grid-template-columns: 1fr; }} .sidebar {{ position: static; }} }}
.sidebar {{
  background: var(--card); border: 1px solid var(--line); border-radius: 16px;
  padding: 24px 20px; height: fit-content; position: sticky; top: 18px;
  box-shadow: var(--shadow);
}}
.avatar {{
  width: 148px; height: 148px; border-radius: 50%; object-fit: cover;
  display: block; margin: 0 auto 14px; background: #cbd2d9;
  border: 3px solid #fff; box-shadow: 0 8px 20px rgba(27,40,56,.14);
}}
.sidebar h1 {{
  font-family: "Source Serif 4", Georgia, serif;
  font-size: 1.35rem; margin: 0 0 6px; text-align: center; font-weight: 650;
}}
.cname {{ text-align: center; color: var(--muted); margin: 0 0 10px; font-size: .95rem; }}
.bio {{ color: var(--muted); font-size: .92rem; text-align: center; margin: 0 0 16px; }}
.meta {{ font-size: .9rem; color: var(--muted); border-top: 1px solid var(--line); padding-top: 12px; }}
.meta div {{ margin: 8px 0; }}
.meta a {{ color: var(--accent); text-decoration: none; }}
.nav {{
  display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px;
  padding-bottom: 14px; border-bottom: 1px solid var(--line);
}}
.nav a {{
  text-decoration: none; color: var(--accent); background: var(--accent-soft);
  padding: 7px 14px; border-radius: 999px; font-weight: 600; font-size: .9rem;
}}
.nav a.active {{ background: var(--accent); color: #fff; }}
.main {{
  background: var(--card); border: 1px solid var(--line); border-radius: 16px;
  padding: 30px 34px; box-shadow: var(--shadow);
}}
.main h1 {{
  font-family: "Source Serif 4", Georgia, serif;
  margin: 0 0 14px; font-size: 1.85rem; font-weight: 650;
}}
.main h2 {{
  font-family: "Source Serif 4", Georgia, serif;
  margin: 1.7rem 0 .7rem; font-size: 1.28rem; font-weight: 650;
  border-bottom: 1px solid var(--line); padding-bottom: .35rem;
}}
.main h3 {{
  font-family: "Source Serif 4", Georgia, serif;
  margin: 1.25rem 0 .35rem; font-size: 1.08rem; font-weight: 650;
}}
.main a {{ color: var(--accent); }}
.main p {{ margin: .7rem 0; }}
.main ul {{ padding-left: 1.15rem; }}
.main li {{ margin: .35rem 0; }}
.pub {{
  margin: 0 0 14px; padding: 12px 0;
  border-bottom: 1px solid var(--line);
}}
.pub:last-child {{ border-bottom: 0; }}
.pub .title {{ font-weight: 700; }}
.pub .venue {{ color: var(--muted); font-size: .9rem; margin: 3px 0 5px; }}
.badge {{
  display: inline-block; font-size: .72rem; font-weight: 700;
  letter-spacing: .03em; text-transform: uppercase;
  background: var(--accent-soft); color: var(--accent);
  padding: 2px 8px; border-radius: 999px; margin-right: 6px;
}}
.note {{ color: var(--muted); font-size: .82rem; margin-top: 28px; border-top: 1px solid var(--line); padding-top: 12px; }}
</style>
</head>
<body>
<div class="wrap">
  <aside class="sidebar">
    <img class="avatar" src="images/profile.jpg" alt="Hongkun Dou">
    <h1>Hongkun Dou</h1>
    <p class="cname">窦泓焜</p>
    <p class="bio">Assistant Professor<br>Zhongguancun Academy</p>
    <div class="meta">
      <div>Beijing, China</div>
      <div>Zhongguancun Academy</div>
      <div><a href="mailto:douhongkun@bza.edu.cn">douhongkun@bza.edu.cn</a></div>
    </div>
  </aside>
  <section class="main">
    <nav class="nav">
      <a href="index.html" class="{active_about}">About</a>
      <a href="publications.html" class="{active_pubs}">Publications</a>
      <a href="research.html" class="{active_research}">Research</a>
    </nav>
    {content}
    <p class="note">Content preview · Academic Pages theme applies fully on GitHub Pages / Jekyll build.</p>
  </section>
</div>
</body>
</html>
"""

def page(name, title, content, active):
    html_page = SHELL.format(
        title=title,
        content=content,
        active_about="active" if active == "about" else "",
        active_pubs="active" if active == "pubs" else "",
        active_research="active" if active == "research" else "",
    )
    (OUT / name).write_text(html_page, encoding="utf-8")

pubs = parse_publications()

about_html = md_to_html(read_md_body(ROOT / "_pages" / "about.md"))
page("index.html", "About", about_html, "about")

research_html = md_to_html(read_md_body(ROOT / "_pages" / "research.md"))
page("research.html", "Research", research_html, "research")

blocks = ['<h1>Publications</h1>',
          '<p style="color:var(--muted)">Ordered by year (newest first); within each year, first-author and stronger venues are listed higher.</p>']
for cat, label in [("manuscripts", "Journal Articles"), ("conferences", "Conference Papers")]:
    blocks.append(f"<h2>{label}</h2>")
    for p in pubs.get(cat, []):
        badge = '<span class="badge">First Author</span>' if p["citation"].startswith("<strong>Dou, H.</strong>") else ""
        year = p["date"][:4] if p["date"] else ""
        blocks.append(
            f'<div class="pub">{badge}<div class="title">{html.escape(p["title"])}</div>'
            f'<div class="venue">{html.escape(p["venue"])} · {year}</div>'
            f'<div>{p["citation"]}</div></div>'
        )
page("publications.html", "Publications", "\n".join(blocks), "pubs")
print(f"Wrote preview to {OUT}")
print("journals", len(pubs["manuscripts"]), "conferences", len(pubs["conferences"]))