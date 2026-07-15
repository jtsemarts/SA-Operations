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

This folder is the live working copy of the COO's Claude operating system. It is backed up to the **SA-Operations** private GitHub repo (`jtsemarts/SA-Operations`) so history is preserved and the workspace can be restored. It is separate from the read-only marketing vault.

- **How the backup works.** This folder lives in iCloud, and a git repo must not live inside iCloud (iCloud's sync corrupts git internals). So a nightly launchd job on the COO's Mac mirrors this folder (via `rsync`, excluding junk) into a git repo kept outside iCloud at `~/git/SA-Operations`, then commits and pushes to GitHub. The backup is therefore one way: working copy to GitHub.
- **Schedule and logs.** Runs nightly at 8:30pm via `~/Library/LaunchAgents/com.semanticarts.sa-ops-backup.plist` (script: `~/bin/sa-ops-nightly-backup.sh`, log: `~/Library/Logs/sa-ops-backup.log`). To force a run: `launchctl start com.semanticarts.sa-ops-backup`.
- **Private and sensitive.** The repo contains personnel-sensitive material (the 1:1 KB), financial figures, compensation notes, and internal policy. Keep it private, limit collaborators, and never commit credentials or tokens (the push token lives in `~/.config/sa-ops/git-credentials`, outside the repo).
- **Weekly verification.** Every Friday, confirm the backup is running: `tail -n 5 ~/Library/Logs/sa-ops-backup.log` should show recent dated runs (each line ends in `no changes` or `backup pushed`). This is a Company Calendar item; Otto surfaces it and helps interpret the log.
- **Marketing vault unchanged.** That vault is a separate read-only clone; this is the operations backup.
