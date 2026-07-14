#!/usr/bin/env python3
"""Regenerate the browsable HTML views for the Company Calendar and Operations
Playbook from their markdown sources. Self-locating: derives paths from this
file's own location, so it survives folder moves. Run after editing either .md."""
import os, sys, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))

try:
    import markdown
except Exception:
    subprocess.run([sys.executable, "-m", "pip", "install", "markdown",
                    "--break-system-packages", "-q"], check=False)
    import markdown

DOCS = [
    ("Company_Calendar.md",   "Company_Calendar.html",   "Company Calendar"),
    ("Operations_Playbook.md","Operations_Playbook.html","Operations Playbook"),
    ("Operations_Manager_Living_JD.md","Operations_Manager_Living_JD.html","Operations Manager — Living JD"),
    ("COO_Living_JD.md",      "COO_Living_JD.html",      "COO — Living JD"),
]

CSS = """
:root{--navy:#1F3864;--mid:#2E4D7B;--line:#dce3ec;--bg:#f7f9fc;--muted:#667;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:#222;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;line-height:1.55;}
.wrap{max-width:960px;margin:0 auto;padding:28px 26px 60px;}
h1{color:var(--navy);font-size:28px;margin:0 0 2px;}
h2{color:var(--navy);font-size:20px;margin:28px 0 8px;border-bottom:2px solid var(--line);padding-bottom:4px;}
h3{color:var(--mid);font-size:16px;margin:20px 0 6px;}
.meta{color:var(--muted);font-size:13px;margin-bottom:18px;}
table{border-collapse:collapse;width:100%;margin:10px 0 18px;font-size:14px;}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top;}
th{background:var(--navy);color:#fff;font-weight:600;}
tr:nth-child(even) td{background:#eef2f8;}
code{background:#eef2f5;padding:1px 5px;border-radius:3px;font-size:13px;}
ul,ol{margin:8px 0 14px;padding-left:22px;}
li{margin:3px 0;}
hr{border:none;border-top:1px solid var(--line);margin:22px 0;}
a{color:var(--mid);}
.foot{color:var(--muted);font-size:12px;margin-top:30px;border-top:1px solid var(--line);padding-top:10px;}
"""

TEMPLATE = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Semantic Arts — {title}</title>
<style>{css}</style></head><body><div class="wrap">
{body}
<div class="foot">Generated from {src} on {stamp}. Edit the markdown, then rerun build_docs.py.</div>
</div></body></html>"""

def main():
    stamp = datetime.date.today().isoformat()
    for md_name, html_name, title in DOCS:
        md_path = os.path.join(HERE, md_name)
        if not os.path.exists(md_path):
            print("skip (missing):", md_name); continue
        text = open(md_path, encoding="utf-8").read()
        body = markdown.markdown(text, extensions=["tables", "sane_lists", "fenced_code", "toc"])
        html = TEMPLATE.format(title=title, css=CSS, body=body, src=md_name, stamp=stamp)
        open(os.path.join(HERE, html_name), "w", encoding="utf-8").write(html)
        print("wrote", html_name)

if __name__ == "__main__":
    main()
