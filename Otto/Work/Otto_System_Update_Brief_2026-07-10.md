# Otto — System Update Brief (2026-07-10)

**For:** Otto (Chief of Staff) · **From:** JT (COO), via an efficiency review
**Purpose:** These changes were applied directly to your files. Please adopt them going forward and confirm you've read them. Nothing here changes your scope — it removes duplication, closes a date bug, and tiers your QC so routine work is faster.

---

## What changed and what to do

### 1. Always check the date first (reliability fix)
Previously some tasks were dated from assumption and landed in the past (phantom "overdue"). New rule, now in `Otto/SKILL.md`:

> Before dating, comparing, or scheduling anything, run `TZ=America/Denver date +"%Y-%m-%d %A %H:%M"` and use that result. Every session — never carry a date forward from earlier in the chat.

**Do:** run the date check before touching any due date, "today" list, or week math.

### 2. One source of truth for grounding/memory
The firm profile was duplicated across four files. Now:
- **Canonical firm profile:** `_Shared/Semantic_Arts_Context.md` (now also holds the shared operating rules).
- **Decoder ring:** `Otto/productivity/memory/glossary.md`.
- `Otto/productivity/CLAUDE.md` and `memory/context/company.md` are trimmed to **pointers** — don't restate content there.

**Do:** when firm facts change, update `_Shared/Semantic_Arts_Context.md` only.

### 3. Brand QC is now risk-tiered (faster routine work)
The full rule lives in `_Shared/Semantic_Arts_Context.md` → "Shared operating rules"; each agent's `SKILL.md` now references it instead of repeating it.
- **External / client-facing / visual work →** mandatory Brand review (unchanged).
- **Internal quick items** (task/board edits, KB updates, routine internal notes/memos) → the drafting agent **self-checks** the writing rules and **skips** the Brand round-trip.
- **When unsure → route to Brand.** You enforce which tier applies.

**Do:** stop routing every internal note through Brand; self-check instead.

### 4. Single task store + regenerate once
Now documented in `Otto/SKILL.md`:
- **`Otto/productivity/TASKS.md` is the only task store.** Recurring items live in `Company_Calendar.md`.
- **`.html` files are output only** — never read a generated `.html` into context to answer a question; read the underlying `.md`.
- **Canonical rendered view: `workspace.html`** (Task Board + Calendar), built by `build_workspace.py`. `build_docs.py` rebuilds the Calendar, Playbook, and Living-JD HTML.
- **Batch:** make all edits for a turn first, then regenerate **once** at the end. (`build_taskboard.py` is deprecated — use `build_workspace.py`.)

**Do:** stop rebuilding the board after every single edit; regenerate once per turn.

### 5. Operations Playbook trimmed (790 → ~400 lines)
All **active SOPs are preserved verbatim.** The empty `[DRAFT]` placeholders became compact per-section **"Backlog (to write)"** lists, plus a new "Index of active SOPs." To write a new SOP, copy the template and fill it in on my go-ahead.

**Do:** treat the Backlog lists as the SOP roadmap; nothing was lost.

### 6. Financial dashboard update checklist (new)
New file: `Otto/Work/Financial_Dashboard_Update_Checklist.md`, cross-linked from the "Cash & Staff Plan" SOP. It documents how to update `Financial_Evaluation_Dashboard_PROTOTYPE.html` (edit only the "REAL INPUTS" block; keyed by absolute week number). Note the current known gap: `anticipatedWagesByWeek` is empty, so projected margin stays blank until it's filled.

**Do:** follow this checklist for the weekly dashboard update; flag when anticipated wages become available.

---

## Files changed
- `Otto/SKILL.md` — date rule; task-store/regeneration section; tiered Brand QC.
- `_Shared/Semantic_Arts_Context.md` — new "Shared operating rules" (draft-only + tiered Brand QC + writing rules).
- `Data|EA|Finance|HR|IT|Legal|Research|Sales /SKILL.md` — Brand QC block replaced with a one-line reference.
- `Otto/productivity/CLAUDE.md` and `memory/context/company.md` — reduced to pointers.
- `Otto/Operations_Playbook.md` — trimmed to active SOPs + backlog lists (v1.8); `.html` regenerated.
- `Otto/productivity/build_taskboard.py` — marked deprecated (use `build_workspace.py`).
- `Otto/Work/Financial_Dashboard_Update_Checklist.md` — new.
- `Otto/Work/Otto_System_Update_Brief_2026-07-10.md` — this brief.

## Suggested reply from Otto
Please read the files above and confirm: (a) you'll run the date check before any dating, (b) you'll self-check internal items and reserve Brand for external/visual, (c) you'll use `TASKS.md` + `workspace.html` and batch regeneration, and (d) whether the Charter should be bumped to note the tiered Brand QC and single-store conventions.
