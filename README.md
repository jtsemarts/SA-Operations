# Semantic Arts — Agents

Each agent has its own folder holding everything essential to it, so work is preserved independently of any single Claude chat. **Otto** is the Chief of Staff and manages the rest of the team; **EA** and the specialists do the hands-on work; the COO works primarily through Otto.

```
Agents/
├── Otto/     Chief of Staff (manages the team) — charter, skill, living docs, work
│   ├── Otto_Charter.md, SKILL.md
│   ├── Operations_Playbook.md / .html     (living)
│   ├── Company_Calendar.md / .html        (living)
│   ├── COO_Living_JD.md, Operations_Manager_Living_JD.md   (as-built role trackers)
│   ├── Knowledge/   operational KBs Otto maintains (coaching, clients, partners, marketing, meeting intelligence, 1:1s; see INDEX.md)
│   └── Work/
├── EA/       Executive assistant — personal productivity + automation hunting
│   ├── EA_Charter.md, SKILL.md
│   └── Work/
├── Legal/    Legal issue-spotting (not legal advice)
├── Brand/    Voice & consistency  (+ style-guide & voice-profile, living)
├── HR/       Human resources  (+ Templates/, Recruiting/)
├── Finance/  FP&A, reporting, models
├── Sales/    Pipeline, proposals, RevOps  (+ Templates/)
├── IT/       Access, tooling, security
├── Data/     Analysis of exports, metrics, models
├── Research/ Market & competitive intelligence, decision memos
└── _Shared/  Cross-agent reference material (use sparingly)
```

Each agent folder contains its `SKILL.md` (skill definition), its charter, any essential reference/templates, and a `Work/` area for the deliverables it produces. Templates live within the owning agent's folder; `_Shared/` is only for material several agents genuinely rely on.

**Operating model.** Otto (Chief of Staff) is the primary cross-collaborator for every agent: it delegates, coordinates, reviews, and synthesizes, and is the single voice back to the COO. All agents are advisory and draft-only, they prepare work; the COO decides and acts. Stan, the COO's personal chief-of-staff agent, runs in a separate account and is partitioned; handoffs go through the COO.

The Financial Evaluation Dashboard (`Financial_Evaluation_Dashboard_PROTOTYPE.html`) lives at the root of this folder.

## Version control and backup

This folder is the **SA-Operations** private GitHub repository. It is the operating system for the COO's Claude account and is version-controlled so history is preserved and the workspace can be restored. It is separate from the read-only marketing vault.

- **Private and sensitive.** The repo contains personnel-sensitive material (the 1:1 KB), financial figures, compensation notes, and internal policy. Keep it private, limit collaborators, and never commit credentials or tokens.
- **Nightly backup.** A launchd job on the COO's Mac commits and pushes changes once a day; ad hoc commits can be made any time with `git add -A && git commit -m "..." && git push`.
- **One-way discipline for the marketing vault stays unchanged.** That vault is a separate read-only clone; this repo is the read-write operations workspace.
