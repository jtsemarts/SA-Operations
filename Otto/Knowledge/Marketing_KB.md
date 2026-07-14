# Knowledge Base — Marketing

**Maintained by:** Otto (for the COO) · **Living document** · **Last updated:** 2026-07-07
**Related:** Operations Playbook (Marketing SOPs); Brand agent (voice, style guide, QC).

## Overview

Reference hub for marketing operations. Brief for now; more to come.

## Current state

- **Lucas (Growth Marketing Manager)** is driving marketing day to day and is setting up the shared marketing projects using the Operations Playbook as the process backbone.
- Marketing operations sit under the COO (oversight of website, campaigns, budget priorities, DCAF and EDTS); the Brand agent handles voice and QC.

## Marketing Intelligence OS vault (read-only reference)

Lucas maintains a marketing knowledge vault, the **Marketing Intelligence OS (MIOS)** — about 166 markdown notes. It is the **narrative and operational layer**; **Airtable is the system of record** for structured data (statuses, scores, dates). It is connected to Cowork as a **read-only** reference at `~/git/sa-marketing-os` (one-way sync: Lucas's vault → GitHub → JT's clone, auto-pulled every 30 minutes). **Never write to it**; edits do not sync and are overwritten on the next pull.

**Start here when using it:** read `00-System/JT-Vault-Guide.md` (folder map and the "if you're looking for…" index), then `10-MIOS/MIOS-Home.md` (orientation to the five systems).

**Folder map (real paths, no wiki links):**
- `00-System/` — how the vault works (guides, conventions, Airtable map).
- `10-MIOS/` — the operating system; `MIOS-Home.md` plus `Systems/<System Name>/` (each has a Hub, System-Docs, and Session-Log). Five systems: `ABM-Lead-Intelligence`, `Competitor-Intelligence`, `Conference-and-Events-Intelligence`, `Content-Intelligence`, `News-and-Social-Intelligence`.
- `20-Campaigns/` — Marketing OS narrative (initiatives / campaigns / projects).
- `30-Content/` — content briefs, drafts, voice-and-style references.
- `40-Intelligence/` — the long-form material used most: `Accounts/` (ABM profiles as `account-<slug>.md`), `Competitors/`, `Events/`, `Briefs/` (weekly), `Trends/`.
- `50-Resources/` — evergreen positioning, brand, voice/style, ICP, segments, Deck Doctor.
- `80-Archive/`, `90-Attachments/`, `Bases/`, `Dashboards/` — usually skip.

**Two Obsidian conventions to handle:** `[[wiki links]]` are not real paths (resolve them via the folder map above); files under `Bases/` and ` ```dataview ` blocks render as inert query text outside Obsidian — for live/structured values go to Airtable (Marketing OS `app60pT0HRYgEH9aH`, Marketing Intelligence `appw4SKvDMeeeUjPz`), matching a note's `airtable_id`/`airtable_base` front matter.

**Sensitivity:** the vault intentionally contains marketing and sales-lead **PII** (names, emails, LinkedIn URLs, account intelligence). Company-managed access only; do not copy PII into external or lower-control outputs, consistent with the AI Usage Policy.

**When to use it:** for marketing narrative and reasoning — account/competitor/event intelligence, positioning, briefs, content context. Otto routes marketing questions here; Brand (voice), Sales (accounts/pipeline), and Research (competitive/market) draw on it. Prefer the vault for narrative, Airtable for current structured values.

## To add later

- Campaign calendar and channel detail (website, Constant Contact newsletter, gist Forum, DCAF, EDTS).
- Lead-nurturing and MQL workflows (in progress with Lucas).
- Metrics and reporting.

## Change log

| Date | Change |
|---|---|
| 2026-07-07 | Created; noted Lucas driving day-to-day marketing and standing up shared projects against the playbook. |
| 2026-07-10 | Registered Lucas's Marketing Intelligence OS (MIOS) vault as a read-only reference connected at `~/git/sa-marketing-os`: folder map, the JT-Vault-Guide entry point, Obsidian/Airtable conventions, and the PII note. |
