#!/usr/bin/env python3
# DEPRECATED (2026-07-10): board-only view, superseded by ../build_workspace.py,
# which renders the same Task Board plus the Calendar in one page (workspace.html).
# Kept for reference; prefer `python3 build_workspace.py`. Reads the same single
# source of truth (TASKS.md); do not maintain task data anywhere else.
import re, json, sys, datetime, os
HERE=os.path.dirname(os.path.abspath(__file__))
IN=sys.argv[1] if len(sys.argv)>1 else os.path.join(HERE,"TASKS.md")
OUT=sys.argv[2] if len(sys.argv)>2 else os.path.join(HERE,"taskboard.html")

# ---- CUSTOMIZE TAGS HERE (function -> color) ----
PALETTE={
 "Finance":"#0F6B3C","HR":"#8A5A00","Sales":"#1F6FB2","Marketing":"#6A1B9A",
 "IT":"#B03A2E","Data":"#0B6E99","Research":"#2E4D7B","Legal":"#555F6E",
 "Brand":"#C2185B","Ops":"#1F3864","Client":"#00796B","Governance":"#4E342E",
 "Personal":"#546E7A"
}
PRIO={"high":"#c0392b","med":"#c98a00","low":"#3a7d3a"}

lines=open(IN,encoding="utf-8").read().split("\n")
tasks=[]; section=None; cur=None
def flush():
    global cur
    if cur is not None: tasks.append(cur); cur=None
for ln in lines:
    if ln.startswith("## "):
        flush(); section=ln[3:].strip(); continue
    m=re.match(r"^- \[( |x|X)\] (.*)$", ln)
    if m:
        flush()
        done = m.group(1).lower()=="x"
        body=m.group(2)
        tags=re.findall(r"#(\w+)", body)
        due_m=re.search(r"due:(\d{4}-\d{2}-\d{2})", body); due=due_m.group(1) if due_m else ""
        prio_m=re.search(r"!(high|med|low)\b", body); prio=prio_m.group(1) if prio_m else ""
        owners=re.findall(r"@(\w+)", body)
        # title: first **bold**, else text up to " - "
        tm=re.search(r"\*\*(.+?)\*\*", body)
        if tm: title=tm.group(1)
        else: title=re.split(r"\s-\s", body)[0]
        title=re.sub(r"~~(.+?)~~", r"\1", title).strip()
        # description: remove title, tokens, done marker
        desc=body
        desc=re.sub(r"\*\*.+?\*\*","",desc,count=1)
        desc=re.sub(r"~~(.+?)~~", r"\1", desc)
        desc=re.sub(r"\(done:\d{4}-\d{2}-\d{2}\)","",desc)
        desc=re.sub(r"#\w+","",desc); desc=re.sub(r"due:\d{4}-\d{2}-\d{2}","",desc)
        desc=re.sub(r"!(high|med|low)\b","",desc); desc=re.sub(r"@\w+","",desc)
        desc=desc.strip(" -—\t")
        cur={"section":section,"done":done,"title":title,"desc":desc,"tags":tags,"due":due,"prio":prio,"owners":owners,"subs":[]}
    elif cur is not None and re.match(r"^\s+- ", ln):
        cur["subs"].append(re.sub(r"^\s+- ","",ln).strip())
flush()

order=["Active","Waiting On","Someday","Done"]
tasks.sort(key=lambda t: order.index(t["section"]) if t["section"] in order else 99)
gen=datetime.datetime.now().strftime("%B %d, %Y %H:%M")

HEAD="""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Task Board — Semantic Arts (Otto)</title><style>
:root{--navy:#1F3864;--line:#dce3ec;--bg:#f6f8fb;--muted:#6b7280;}
*{box-sizing:border-box}body{margin:0;font:14px/1.5 -apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#1c2430;background:var(--bg)}
header{background:var(--navy);color:#fff;padding:14px 20px}header h1{margin:0;font-size:18px}header .sub{opacity:.8;font-size:12px;margin-top:2px}
.toolbar{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:10px 20px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}
#q{flex:1;min-width:180px;padding:8px 12px;border:1px solid #c4cede;border-radius:8px;font-size:14px}
.chip{cursor:pointer;border:1px solid #c4cede;background:#fff;padding:3px 10px;border-radius:20px;font-size:12px;user-select:none}
.chip.on{color:#fff;border-color:transparent}
.chip.prio.on{background:#444}
.grp{display:flex;gap:6px;align-items:center;flex-wrap:wrap}
.grp .lbl{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin-right:2px}
.btn{cursor:pointer;border:1px solid #c4cede;background:#fff;padding:6px 10px;border-radius:8px;font-size:12px}
.cols{display:flex;gap:14px;padding:16px 20px;align-items:flex-start;overflow-x:auto}
.col{flex:1;min-width:260px;background:#eef2f7;border-radius:12px;padding:10px}
.col h2{margin:2px 4px 10px;font-size:13px;color:var(--navy);text-transform:uppercase;letter-spacing:.04em}
.col h2 .n{color:var(--muted);font-weight:500}
.card{background:#fff;border:1px solid var(--line);border-left:4px solid #c4cede;border-radius:9px;padding:9px 11px;margin:8px 0;box-shadow:0 1px 2px rgba(20,40,80,.05)}
.card.done{opacity:.6}
.card .title{font-weight:600;font-size:14px}
.card.done .title{text-decoration:line-through;color:var(--muted)}
.card .desc{color:#3a4453;font-size:12.5px;margin:4px 0}
.row{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-top:6px}
.tag{font-size:11px;font-weight:600;color:#fff;padding:2px 8px;border-radius:20px}
.due{font-size:11px;font-weight:600;padding:2px 8px;border-radius:20px;background:#eef1f6;color:#556}
.due.over{background:#fde8e6;color:#b0281a}.due.soon{background:#fff3d6;color:#8a5a00}
.owner{font-size:11px;color:var(--muted)}
.subs{margin:6px 0 0;padding-left:16px}.subs li{font-size:12px;color:#4a5568;margin:1px 0}
.pdot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px;vertical-align:middle}
.empty{color:var(--muted);font-size:12px;padding:6px;font-style:italic}
.viewbtn{cursor:pointer;border:1px solid #c4cede;background:#fff;padding:4px 10px;border-radius:8px;font-size:12px}
.viewbtn.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.list{display:block;padding:16px 20px;max-width:900px}
.listgrp{margin-bottom:14px}
.cathdr{font-size:13px;color:var(--navy);text-transform:uppercase;letter-spacing:.04em;border-left:4px solid #c4cede;padding-left:8px;margin:16px 0 6px}
.cathdr .n{color:var(--muted);font-weight:500}
.hide{display:none!important}
.legend{font-size:11px;color:var(--muted);padding:0 20px 16px}
</style></head><body>
<header><h1>Task Board — Semantic Arts</h1><div class="sub">Enhanced view (tags · due dates · priority) &middot; source: TASKS.md &middot; generated GEN_DATE</div></header>
<div class="toolbar">
<input id="q" type="search" placeholder="Search tasks, tags, people…">
<div class="grp"><span class="lbl">Tags</span><span id="tagfilters"></span></div>
<div class="grp"><span class="lbl">Priority</span>
<span class="chip prio" data-p="high">High</span><span class="chip prio" data-p="med">Med</span><span class="chip prio" data-p="low">Low</span></div>
<div class="grp"><span class="lbl">View</span><span class="viewbtn on" data-v="board">Board</span><span class="viewbtn" data-v="due">Today &amp; Overdue</span><span class="viewbtn" data-v="category">By Category</span></div>
<span class="btn" id="sortDue">Sort by due date</span>
<span class="btn" id="hideDone">Hide completed</span>
<span class="btn" id="clear">Clear</span>
</div>
<div class="cols" id="cols"></div>
<div class="legend" id="legend"></div>
<script>
"""
TAIL="""
const SECT=["Active","Waiting On","Someday","Done"];
const today=new Date(); today.setHours(0,0,0,0);
let selTags=new Set(), selPrio=new Set(), sortDue=false, hideDone=false;
function dueClass(d){if(!d)return"";const dt=new Date(d+"T00:00:00");const diff=(dt-today)/86400000;if(diff<0)return"over";if(diff<=3)return"soon";return"";}
function tagColor(t){return PALETTE[t]||"#8894a6";}
function el(h){const d=document.createElement('div');d.innerHTML=h;return d.firstElementChild;}
// build tag filter chips from palette + present tags
const present=new Set(); TASKS.forEach(t=>t.tags.forEach(x=>present.add(x)));
const tagOrder=Object.keys(PALETTE).filter(t=>present.has(t)).concat([...present].filter(t=>!PALETTE[t]));
const tf=document.getElementById('tagfilters');
tagOrder.forEach(t=>{const c=el('<span class="chip" data-t="'+t+'">'+t+'</span>');c.style.borderColor=tagColor(t);c.addEventListener('click',()=>{if(selTags.has(t)){selTags.delete(t);c.classList.remove('on');c.style.background='';}else{selTags.add(t);c.classList.add('on');c.style.background=tagColor(t);}render();});tf.appendChild(c);});
document.querySelectorAll('.chip.prio').forEach(c=>c.addEventListener('click',()=>{const p=c.dataset.p;if(selPrio.has(p)){selPrio.delete(p);c.classList.remove('on');}else{selPrio.add(p);c.classList.add('on');}render();}));
document.getElementById('sortDue').addEventListener('click',function(){sortDue=!sortDue;this.style.background=sortDue?'#dbe4f0':'#fff';render();});
document.getElementById('hideDone').addEventListener('click',function(){hideDone=!hideDone;this.style.background=hideDone?'#dbe4f0':'#fff';render();});
document.getElementById('clear').addEventListener('click',()=>{selTags.clear();selPrio.clear();sortDue=false;hideDone=false;document.getElementById('q').value='';document.querySelectorAll('.chip.on').forEach(c=>{c.classList.remove('on');c.style.background='';});document.getElementById('sortDue').style.background='#fff';document.getElementById('hideDone').style.background='#fff';render();});
document.getElementById('q').addEventListener('input',render);
function match(t){
 const q=document.getElementById('q').value.toLowerCase().trim();
 if(hideDone&&t.done)return false;
 if(selTags.size&&!t.tags.some(x=>selTags.has(x)))return false;
 if(selPrio.size&&!(t.prio&&selPrio.has(t.prio)))return false;
 if(q){const hay=(t.title+' '+t.desc+' '+t.tags.join(' ')+' '+t.owners.join(' ')+' '+t.subs.join(' ')).toLowerCase();if(hay.indexOf(q)<0)return false;}
 return true;
}
function card(t){
 const pc=PRIO[t.prio]||'#c4cede';
 const c=document.createElement('div');c.className='card'+(t.done?' done':'');c.style.borderLeftColor=pc;
 let h='';
 h+='<div class="title">'+(t.prio?'<span class="pdot" style="background:'+pc+'" title="'+t.prio+' priority"></span>':'')+escape(t.title)+'</div>';
 if(t.desc)h+='<div class="desc">'+escape(t.desc)+'</div>';
 h+='<div class="row">';
 t.tags.forEach(x=>h+='<span class="tag" style="background:'+tagColor(x)+'">'+escape(x)+'</span>');
 if(t.due)h+='<span class="due '+dueClass(t.due)+'">due '+t.due+'</span>';
 t.owners.forEach(o=>h+='<span class="owner">@'+escape(o)+'</span>');
 h+='</div>';
 if(t.subs.length){h+='<ul class="subs">';t.subs.forEach(s=>h+='<li>'+escape(s)+'</li>');h+='</ul>';}
 c.innerHTML=h;return c;
}
function escape(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
let view='board';
document.querySelectorAll('.viewbtn').forEach(b=>b.addEventListener('click',function(){document.querySelectorAll('.viewbtn').forEach(x=>x.classList.remove('on'));this.classList.add('on');view=this.dataset.v;render();}));
function byDue(a,b){return (a.due||'9999')<(b.due||'9999')?-1:1;}
function grp(title,arr,host,color){const g=el('<div class="listgrp"></div>');g.appendChild(el('<h3 class="cathdr"'+(color?' style="border-color:'+color+'"':'')+'>'+escape(title)+' <span class="n">('+arr.length+')</span></h3>'));arr.forEach(t=>g.appendChild(card(t)));host.appendChild(g);}
function render(){
 const host=document.getElementById('cols');host.innerHTML='';host.className=(view==='board')?'cols':'list';
 if(view==='board'){
  SECT.forEach(sec=>{
   let items=TASKS.filter(t=>t.section===sec&&match(t));
   if(sortDue)items=items.slice().sort(byDue);
   const col=document.createElement('div');col.className='col';
   col.innerHTML='<h2>'+sec+' <span class="n">('+items.length+')</span></h2>';
   if(!items.length)col.appendChild(el('<div class="empty">Nothing here</div>'));
   items.forEach(t=>col.appendChild(card(t)));
   host.appendChild(col);
  });
 } else if(view==='due'){
  const items=TASKS.filter(t=>match(t)&&!t.done&&t.due);
  const isToday=t=>{const d=new Date(t.due+'T00:00:00');return (d-today)===0;};
  const mine=items.filter(t=>t.section!=='Waiting On');
  const wait=items.filter(t=>t.section==='Waiting On');
  const over=mine.filter(t=>dueClass(t.due)==='over').sort(byDue);
  const tod=mine.filter(isToday).sort(byDue);
  const waitDue=wait.filter(t=>dueClass(t.due)==='over'||isToday(t)).sort(byDue);
  if(over.length)grp('Overdue',over,host);
  if(tod.length)grp('Due today',tod,host);
  if(!over.length&&!tod.length)host.appendChild(el('<div class="empty">Nothing overdue or due today.</div>'));
  if(waitDue.length)grp('Waiting on — to follow up',waitDue,host,'#7a5c00');
 } else {
  const items=TASKS.filter(t=>match(t)&&!t.done);
  const groups={};
  items.forEach(t=>{(t.tags.length?t.tags:['(untagged)']).forEach(tag=>{(groups[tag]=groups[tag]||[]).push(t);});});
  const ord=Object.keys(PALETTE).filter(k=>groups[k]).concat(Object.keys(groups).filter(k=>!PALETTE[k]));
  if(!ord.length)host.appendChild(el('<div class="empty">No tasks.</div>'));
  ord.forEach(tag=>grp(tag,groups[tag].slice().sort(byDue),host,tagColor(tag)));
 }
}
document.getElementById('legend').textContent='Tags are customizable by function (edit the palette in the generator). Priority: high/med/low. Due dates flag red when overdue, amber within 3 days. Recurring items live in the Company Calendar. Edit tasks in TASKS.md; regenerate this board to refresh.';
render();
</script></body></html>"""

html = HEAD.replace("GEN_DATE",gen) + "const TASKS="+json.dumps(tasks)+";\nconst PALETTE="+json.dumps(PALETTE)+";\nconst PRIO="+json.dumps(PRIO)+";\n" + TAIL
open(OUT,"w",encoding="utf-8").write(html)
print("wrote",OUT,"| tasks:",len(tasks))
