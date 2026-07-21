# Semantic Arts Operating System — System Documentation & Build Record

**Maintained by:** Otto (for the COO) · **Last updated:** 2026-07-20
**Audience:** the COO, and any future maintainer — including a migration to a **Claude Code** implementation.
**Scope:** what this system is, why it was built the way it was, where every source file lives, and how the moving parts fit together. Read `README.md` (repo root) for the short version; this is the deep reference.

---

## 1. What this is

This repository (`Agents/`) is a **file-based operating system for the COO of Semantic Arts**, run through a team of Claude agents. It replaces ad-hoc chat with a durable, version-controlled workspace: the COO brings a request to **Otto** (the Chief of Staff agent), Otto routes it to the owning specialist agent, the specialist drafts in its own `Work/` folder, Otto reviews and synthesizes, and a single filtered answer comes back. Nothing is dispatched externally — every agent is **advisory and draft-only**; the COO (and where required the President) decides and acts.

The system is deliberately **connector-free** today: no live email, calendar, drive, or CRM access, pending a company connector policy. All state lives in Markdown and is rendered to HTML for reading. This is a constraint, not an accident (see §3).

### Goals

1. **Nothing falls through the cracks.** A single task board plus a recurring-events calendar, reconciled daily, so deadlines are never missed for lack of tracking.
2. **Durable over disposable.** Knowledge, SOPs, and decisions live in files that survive any single chat, are searchable, and are backed up to GitHub nightly.
3. **Delegation, not a reference shelf.** Specialist agents do the domain work; Otto orchestrates and synthesizes. The COO talks to one coordinator.
4. **Right-sized quality.** Brand QC and confidentiality are enforced on a risk tier, so internal edits stay fast and external/visual work stays polished and on-brand.
5. **Policy-aligned.** Everything conforms to the Semantic Arts AI Usage Policy (company-managed, minimize sensitive data, propose-don't-execute, no stored credentials).

---

## 2. Repository map (where everything lives)

Organized **by business function**. Each function folder holds its agent(s) — `SKILL.md`, a charter, essential reference, and a `Work/` area for deliverables.

```
Agents/                                 repo root (mirrored nightly to GitHub: SA-Operations)
├── README.md                           short orientation
├── SYSTEM_DOCUMENTATION.md             this file
│
├── Sales/                              Sales agent (SKILL, Sales_Charter, Knowledge_Base) + Work/
├── Marketing/
│   └── Brand/                          Brand agent: SKILL, Brand_Agent_Charter, Knowledge_Base,
│                                       Semantic_Arts_Brand_Kit.md, semanticarts-style-guide.md,
│                                       semanticarts-voice-profile.md, Work/ (website rebuild v3–v8)
├── IT/                                 IT agent (SKILL, IT_Charter, Knowledge_Base) + Work/ (cyber docs)
├── HR/                                 HR agent (SKILL, HR_Agent_Charter, HR_Plugin_Binding,
│                                       Knowledge_Base) + Recruiting/, Work/
├── Finance & Accounting/               Finance agent (SKILL, Finance_Charter, Knowledge_Base)
│                                       + Financial_Evaluation_Dashboard_PROTOTYPE.html
├── Legal/                              Legal agent (SKILL, Legal_Agent_Charter, Knowledge_Base,
│                                       AI_Usage_Policy_Compliance.md) + Work/
├── Operations/                         the operating core
│   ├── Otto/                           Chief of Staff + the OS files (detail below)
│   ├── EA/                             executive assistant (personal productivity, automation)
│   ├── Data/                           analysis of exports, metrics, models
│   └── Research/                       market & competitive intelligence, decision memos
└── _Shared/                            cross-agent context (used sparingly)
    ├── README.md
    ├── Semantic_Arts_Context.md        firm operating profile — every agent reads this first
    └── Semantic_Arts_North_Star.md     CEO/President-authored beliefs/vision/values
```

### Inside `Operations/Otto/` (the operating-system files)

```
Operations/Otto/
├── Otto_Charter.md                     full definition of the Chief-of-Staff role (v1.8)
├── SKILL.md                            Otto's operating rules: routing map, dates, task store, QC
├── Today_and_Rollup_Logic.md           canonical spec for the daily list and weekly rollup
├── Operations_Playbook.md / .html      SOPs (Sales, Marketing, HR, Admin, Finance, IT)
├── Company_Calendar.md / .html         recurring tax/compliance/payroll/HR/operating deadlines
├── COO_Living_JD.md / .html            as-built COO role description (auto-updated)
├── Operations_Manager_Living_JD.md/.html   as-built Ops Manager (Amanda) role description
├── Knowledge_Base.md                   Otto's own reference
├── build_workspace.py                  TASKS.md + Company_Calendar.md  → workspace.html
├── build_docs.py                       Playbook/Calendar/Living-JD .md → .html (with anchors)
├── workspace.html                      canonical rendered view (Task Board + Calendar tabs)
├── productivity/
│   ├── TASKS.md                        THE task board (single source of truth)
│   ├── CLAUDE.md                       productivity-plugin working memory
│   ├── build_taskboard.py              LEGACY board-only renderer (superseded)
│   ├── taskboard.html / dashboard.html legacy/aux views
│   └── memory/                         context/company.md, glossary.md
├── Knowledge/                          the Knowledge hub (KBs) — see §6
│   ├── INDEX.md                        index + workflows (rollup, cross-linking, reporting)
│   ├── Coaching_Program_KB.md, Clients_KB.md, Partners_KB.md, Marketing_KB.md,
│   │   Meeting_Intelligence_KB.md, AI_Cyber_Taskforce_KB.md, IT_KB.md,
│   │   Direct_Report_1on1_KB.md, President_1on1_KB.md
│   └── Government-Contracting/         Government-Contracting-KB, RGI-KB, DNI-KB, FedScale-KB
├── Work/                               Otto's deliverables (to-do docs, briefs, agendas)
├── Drafts/                             awaiting COO review
└── Archive/                            acted-on items (never delete; archive)
```

---

## 3. Core design principles and build decisions (with rationale)

**Markdown is the source of truth; HTML is output only.** Every fact lives in a `.md` file. The `.html` files exist purely for the COO's browser and are regenerated from the Markdown. Agents always read the `.md`, never a generated `.html`. *Why:* one canonical copy, clean diffs, no drift, git-friendly.

**Function-first folder structure.** Top level is the business function (`Sales`, `Marketing/Brand`, `IT`, `HR`, `Finance & Accounting`, `Legal`, `Operations`), with agents nested inside. *Why:* it mirrors how the COO thinks about the work and keeps each function's output together. (Migrated 2026-07-17 from an earlier agent-first layout where each agent was a top-level folder.)

**Filing rule: every deliverable goes in the owning function's `Work/` folder.** Never loose at the Documents root. *Why:* organization, and the nightly backup only mirrors the `Agents/` tree — loose files at the Documents root would not be captured.

**Delegation-first orchestration.** Otto's default is to route each request to the owning specialist (per the routing map in `SKILL.md`), have it draft in its `Work/` folder, then review and synthesize. Otto does work directly only for true chief-of-staff tasks. *Why:* an audit (2026-07-10) found agents were being used as passive reference shelves; v1.8 of the charter corrected this.

**Connector-free, draft-only.** No live integrations; all output is a draft for the COO to execute. *Why:* the firm is holding off on Claude connectors pending a company policy, and the AI Usage Policy requires company-managed integrations and propose-don't-execute behavior. A prior experimental integration (`fs-sa-tasks-kit`, a personal-account task connector holding a credential) was **retired 2026-07-03** for policy alignment.

**Risk-tiered Brand QC.** External/client-facing/visual work gets a mandatory Brand review; internal quick items self-check and skip the round-trip. *Why:* quality where it matters without slowing routine edits.

**Dates come from the live clock, never memory.** Always run `TZ=America/Denver date +"%Y-%m-%d %A"` before dating anything. *Why:* the environment's "Today's date" snapshot goes stale in long/multi-day sessions and caused repeated mis-dating; the live sandbox clock reflects real elapsed time.

**Confidentiality partitioning.** Personnel- and executive-sensitive KBs (the 1:1 KBs) are kept COO-scoped in Otto's folder, not in `_Shared/`. The personal chief-of-staff agent **Stan** runs in a separate account and is partitioned; handoffs go through the COO.

---

## 4. The agent model

**Otto (Chief of Staff)** is the single point of contact. It routes, coordinates hand-offs, reviews/QCs drafts, synthesizes, stewards the living documents, keeps the task board current, and produces the daily to-do. Definition: `Operations/Otto/Otto_Charter.md` (v1.8) and `SKILL.md`.

**Routing map (owner → domain):**

- **Legal** → contracts, NDAs, data privacy, compliance issue-spotting, policy review.
- **Brand** → voice and QC, content/copy, brand assets, editorial.
- **HR** → recruiting, offers, onboarding, comp and benefits, personnel, coaching admin.
- **Finance** → FP&A, models, reporting, budgeting, the financial dashboard (with Data).
- **Sales** → pipeline, proposals and SOWs, RevOps, nurturing, partner materials.
- **IT** → access, tooling, security, Microsoft 365 admin, deep security research (advisory; the COO executes as IT).
- **Data** → analysis of exports, metrics, model building, dashboard data.
- **Research** → market/competitive intelligence, decision memos, talent sourcing.
- **EA** → the COO's personal productivity, scheduling logistics, automation hunting.

Every agent reads `_Shared/Semantic_Arts_Context.md` (firm operating profile) and `Semantic_Arts_North_Star.md` before producing work. Each agent has: `SKILL.md` (its trigger + operating rules), a charter (full role), a `Knowledge_Base.md`, and a `Work/` folder.

---

## 5. Rendering pipeline (generators)

All generators are **self-locating** (they resolve paths from their own location via `os.path.dirname(__file__)`), so they run from anywhere. They live in `Operations/Otto/`.

- **`build_workspace.py`** — reads `productivity/TASKS.md` + `Company_Calendar.md`, writes `workspace.html` (the canonical Task Board + Calendar view). Parses the task token grammar (see §6), color-codes by function tag and priority. Run after any edit to `TASKS.md` or `Company_Calendar.md`.
- **`build_docs.py`** — regenerates the HTML for `Operations_Playbook.md`, `Company_Calendar.md`, and the two Living JDs. Uses the Python `markdown` library with the **`toc` extension**, which generates heading anchor ids (e.g. `#sop-coaching-program`) used for SOP deep-links in the to-do Word docs. Run after editing the Playbook, Calendar, or a Living JD.
- **`productivity/build_taskboard.py`** — **legacy** board-only renderer (`taskboard.html`), superseded by `build_workspace.py`. Kept for reference.

**Regeneration discipline:** make all edits for a turn first, then regenerate once (don't rebuild after each change). Dependency: `markdown` (auto-installed with `--break-system-packages` if missing).

**Word deliverables** (to-do lists, briefs) are built with the `docx` npm library (`NODE_PATH=$(npm root -g)`), then verified by rendering to PDF (LibreOffice `soffice` → `pdftoppm`) and a regex check that confirms zero em/en dashes (brand rule). To-do docs deep-link each task to its SOP anchor in `Operations_Playbook.html`.

---

## 6. Task board and the daily list

**`productivity/TASKS.md` is the single task store.** Recurring items live in the Company Calendar, not the board. Sections: `## Active`, `## Waiting On`, `## Someday`, `## Done`.

**Token grammar** (parsed by `build_workspace.py`):

```
- [ ] **Title** - description. #Function !priority due:YYYY-MM-DD @Owner
        (indented sub-bullets = subtasks/notes)
- [x] ~~Title~~ (done:YYYY-MM-DD) #Function
```

- `#Function` tags: Finance, HR, Sales, Marketing, IT, Data, Research, Legal, Brand, Ops, Client, Governance, Personal.
- `!high | !med | !low` priority; `@Owner` for waiting-on items; `due:` in ISO date.

**Daily "today" list and weekly rollup** follow one canonical spec: `Today_and_Rollup_Logic.md`. Definitions: *overdue* = due before today; *due today* = due equals today; no-due-date items are omitted from the daily list. Sources, in order: TASKS.md (Active + Waiting On) → Company Calendar items landing today → open KB items (as confirm-first candidates). Each actionable item is checked against the Playbook for an active SOP (link it, or flag "no SOP yet"), and gets an automate/delegate/eliminate suggestion where one clearly applies. QuickBooks export and the Zoho check are COO-only and never suggested for delegation.

---

## 7. Knowledge hub (KBs)

Index at `Operations/Otto/Knowledge/INDEX.md`, which also defines the workflows (Monday rollup, Monday archive pass, cross-linking, reporting shortcuts). Current KBs:

| KB | Purpose | Sensitivity |
|---|---|---|
| `Coaching_Program_KB.md` | Coaching program: cadence, agenda, roster | Internal |
| `Clients_KB.md` | Client relationships (growing) | Internal |
| `Partners_KB.md` | Commercial partners (AIM) | Internal |
| `Government-Contracting/` | Gov-contracting bucket + RGI, DNI, FedScale partner KBs | Internal |
| `Marketing_KB.md` | Marketing ops; how to navigate Lucas's read-only marketing vault | Internal |
| `Meeting_Intelligence_KB.md` | Decisions/open items from standing meetings | Internal |
| `AI_Cyber_Taskforce_KB.md` | AI & Cyber Task Force: agendas, recommendations, action items (JT chairs) | Internal (security-sensitive) |
| `IT_KB.md` | COO IT reference; admin consoles; runbooks; vendor selection | Internal |
| `Direct_Report_1on1_KB.md` | 1:1s with Lucas & Amanda | **Restricted** (personnel; COO-scoped) |
| `President_1on1_KB.md` | 1:1 with the President (Rebecca) | **Restricted** (executive; COO-scoped) |

Cross-linking rule: when a KB open item becomes a board task or calendar entry, it is linked both ways so nothing is double-tracked.

---

## 8. Governance and policy constraints

Source of truth for roles/authority: the Governance Functions matrix, summarized in `_Shared/Semantic_Arts_Context.md`. Key facts a maintainer needs:

- **COO (JT)** owns operations, HR, marketing ops, sales logistics, most finance ops, IT/security, compliance — there is **no separate IT or compliance department**, so those cannot be delegated to a team (levers: automation, vendor support, mechanical steps to Amanda, AI/agents).
- **President (Rebecca)** holds final signature authority, P&L, hiring/pay decisions; approves payroll. Firm-wide policies are adopted at her level.
- **Spending authority:** COO < $2,500; COO+President jointly ≥ $2,500; CEO on new debt > $100k.
- **Payroll is non-standard:** every 4 weeks (13 periods/year); the workweek runs Thursday→Friday. Dated schedule in the Company Calendar.
- **AI Usage Policy v1.1** (owner: President) governs all agent use; Legal screens against it (`Legal/AI_Usage_Policy_Compliance.md`).

---

## 9. Version control and backup

- The working copy lives in **iCloud** (`Documents/.../Agents/`). Git must not live inside iCloud, so a **nightly launchd job** on the COO's Mac rsyncs the `Agents/` tree into a git repo kept outside iCloud (`~/git/SA-Operations`), commits, and pushes to the private GitHub repo **`jtsemarts/SA-Operations`**.
- The backup is **one-way** (working copy → GitHub). Token stored at `~/.config/sa-ops/git-credentials` (never in the repo).
- A **Friday** Company Calendar item verifies the backup ran (glance at `~/Library/Logs/sa-ops-backup.log`).
- Separate from the read-only marketing vault (`~/git/sa-marketing-os`, Lucas's Marketing Intelligence OS, connected read-only).

---

## 10. Build milestones (chronological)

- **2026-06-29** — Otto created as an Executive Assistant (charter v1.0).
- **2026-07-03** — Promoted Otto to **Chief of Staff**; added EA + specialists (Legal, Brand, HR, Finance, Sales, IT, Data, Research); moved to a per-agent folder tree; retired the `fs-sa-tasks-kit` connector for policy alignment; folded the AI Usage Policy into Legal.
- **2026-07-06 to 07-10** — Efficiency audit → delegation-first operating model (charter v1.8); added the Knowledge hub, the two Living JDs, the `Today_and_Rollup_Logic` spec; `workspace.html` became the canonical view.
- **2026-07-10/14** — Financial Evaluation Dashboard prototype; brand kit/style guide/voice profile built into Brand; records-retention policy; SOP build-out.
- **2026-07-14/16** — AI & Cyber Task Force KB + kickoff; monthly 3rd-Thursday cadence; nightly GitHub backup wired.
- **2026-07-16/17** — Dates fixed to the live clock; **function-first folder migration**; website rebuild redesign iterations (v3 editorial → v8 tiered graph); cyber workstream (personal-device guide, BYOD policy, password-manager & VPN vendor research, Microsoft Defender briefing); Government-Contracting KBs (RGI/DNI/FedScale) + AIXM/SWIM research for DNI.
- **2026-07-20** — President 1:1 KB; password/VPN vendor shortlist brief (Nord, 1Password, Dashlane) placed in the IT KB as a COO+President decision.

---

## 11. Known gaps / open items

- Several `[DRAFT]` SOP placeholders remain in the Operations Playbook (tracked as a Someday task).
- Backup procedures for Microsoft 365 and Box are to be documented with external IT (Jason).
- No live task-system connector; any future one must be company-managed and company-approved.
- Scheduled automations (weekday-morning to-do, first-Monday task suggestions) are **paused**; the behavior lives in Otto's charter and runs when Otto is engaged.

---

## 12. Migration notes — moving to Claude Code

This system maps cleanly onto Claude Code primitives. Recommended mapping:

**Project instructions → `CLAUDE.md` at the repo root.** Fold the load-bearing rules (dates-from-live-clock, filing rule, Markdown-is-truth, regeneration discipline, Brand QC tiering, connector-free/draft-only) into a root `CLAUDE.md` so every session inherits them. Point it at this file and `README.md`.

**Agents → subagents (`.claude/agents/*.md`).** Each specialist becomes a subagent whose system prompt is its existing charter + `Knowledge_Base.md`, with a description that encodes the routing trigger. Otto becomes the top-level orchestrator that delegates via the Task tool. The existing routing map (§4) is the delegation table.

**SKILL.md files → skills.** The per-agent `SKILL.md` files already follow the skill format (frontmatter name/description + instructions). They can be dropped into `.claude/skills/` (or a plugin) largely as-is. The document-format skills (docx/pptx/xlsx/pdf) used for deliverables are already standard.

**Generators stay as-is.** `build_workspace.py` and `build_docs.py` are plain, self-locating Python; run them from Bash or wire them to a Claude Code **hook** (e.g., a post-edit hook that regenerates `workspace.html` whenever `TASKS.md` changes) to remove the manual regenerate step.

**Recurring behavior → scheduled triggers or hooks.** The paused daily-to-do and Monday rollup can be re-armed as scheduled tasks (or launchd/cron invoking a Claude Code headless run) that read `Today_and_Rollup_Logic.md` as the spec.

**Backup is already Git-native.** In a Claude Code world the repo can *be* the working copy (no iCloud/launchd rsync indirection needed) — commit and push directly, keeping the same private `SA-Operations` remote and the same "never commit credentials" rule.

**Connectors (future).** When the company connector policy lands, add MCP servers (Microsoft 365, QuickBooks, Zoho, Expensify) as company-managed integrations, and relax the draft-only constraint per the policy. Legal's compliance checklist already anticipates this.

**Keep the invariants.** Whatever the implementation: Markdown as source of truth; one task store; live-clock dates; filing into `Work/`; risk-tiered Brand QC; draft-only until policy says otherwise; personnel/executive KBs kept COO-scoped.
