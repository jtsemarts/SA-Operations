# Semantic Arts — Operating System

Organized by **business function**. Each function folder holds its agent(s) and their work product. Otto (Chief of Staff) orchestrates the team from Operations; the COO works primarily through Otto.

```
Agents/                          repo root (mirrored nightly to the SA-Operations GitHub repo)
├── Sales/                       Sales agent + Work/
├── Marketing/
│   └── Brand/                   Brand agent + Work/  (voice, QC, marketing)
├── IT/                          IT agent + Work/
├── HR/                          HR agent + Work/  (Templates/, Recruiting/)
├── Finance & Accounting/        Finance agent + Work/  (+ Financial Evaluation Dashboard)
├── Legal/                       Legal agent + Work/
├── Operations/                  the operating core
│   ├── Otto/                    Chief of Staff + the operating-system files:
│   │                            Operations Playbook, Company Calendar, task board (productivity/),
│   │                            Knowledge hub (Knowledge/), build scripts, Living JDs
│   ├── EA/                      executive assistant (personal productivity, automation hunting)
│   ├── Data/                    analysis of exports, metrics, models
│   └── Research/                market & competitive intelligence, decision memos
└── _Shared/                     cross-agent context + North Star (used sparingly)
```

Each agent folder contains its `SKILL.md`, charter, essential reference/templates, and a `Work/` area for the deliverables it produces.

## How work is filed

Every deliverable (Word, PowerPoint, markdown, HTML) is saved in the **owning function's `Work/` folder** (for example `IT/Work`, `Marketing/Brand/Work`, `Finance & Accounting/Work`, `Operations/Otto/Work`), never left loose at the Documents root. This keeps output organized and ensures it is captured by the nightly GitHub backup, which mirrors this `Agents/` tree. Files are still surfaced to the COO in chat with a file card regardless of where they live.

## Operating model

Otto (Chief of Staff) routes each request to the owning agent, coordinates hand-offs, reviews and quality-checks the drafts, synthesizes, and is the single voice back to the COO. All agents are advisory and draft-only: they prepare work; the COO decides and acts. Stan, the COO's personal chief-of-staff agent, runs in a separate account and is partitioned; handoffs go through the COO.

## Version control and backup

This `Agents/` folder is the operating system for the COO's Claude account and is the source that is mirrored to the **SA-Operations** private GitHub repo. Because this folder lives in iCloud (and git must not live inside iCloud), a nightly launchd job on the COO's Mac copies this tree into a git repo kept outside iCloud (`~/git/SA-Operations`), commits, and pushes. The backup is one way: working copy to GitHub. It is separate from the read-only marketing vault (`~/git/sa-marketing-os`).

- **Private and sensitive.** The repo holds personnel-sensitive material (the 1:1 KB), financials, compensation notes, and internal policy. Keep it private and never commit credentials or tokens.
- **Weekly verification.** A Friday Company Calendar item checks the backup log; Otto helps interpret it.
