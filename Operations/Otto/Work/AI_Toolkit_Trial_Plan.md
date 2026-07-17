# Trial Plan: Anthropic Productivity & HR Plugins

**Prepared by:** Otto · **For:** JT Metcalf, COO · **Date:** July 3, 2026 · Living document
**Scope:** A two-week, low-risk trial of two Anthropic knowledge-work plugins in our company Claude/Cowork account: **Productivity** (mapped to Operations/Otto/EA) and **HR** (mapped to the HR agent). Draft-only, connector-free, human-approved throughout.

## Objective

Decide whether either plugin earns a place in our setup by testing two things: does it save real time, and does its structure improve on what we have already built (charters, SOPs, living documents), without adding policy risk.

## Shared guardrails (apply to both trials)

- Run only in the **company-managed Claude/Cowork account** (Sec. 4.2).
- **Disable or do not configure any connectors/MCP** the plugin ships with; use the skills/workflows only. Any connector needs company-level approval first (Sec. 9.4). Our trial stays connector-free.
- **Draft-only, human-approved.** Nothing is sent, posted, or committed; the COO (and President where required) approves outputs (Sec. 8, 9.1).
- **Data discipline.** Use non-sensitive or anonymized inputs; for HR, apply Sec. 7.3 to any PII or compensation data (minimize, anonymize, company tool only). No client data.
- Legal's checklist item 11 governs adoption; flag anything that trips it before proceeding.

---

## Trial A — Productivity plugin (Otto / EA)

**Why:** It provides Cowork-native task management (a `TASKS.md` with a dashboard tracking Active / Waiting On / Someday / Done) and a "workplace memory" that learns our people, projects, and internal shorthand. That maps directly onto Otto's deliverable tracking and EA's productivity role.

**Setup (Day 1)**
- Install the Productivity plugin from Anthropic's knowledge-work-plugins into the company Cowork account.
- Point its task file at Otto's workspace; seed the workplace memory from `_Shared/Semantic_Arts_Context.md` (people: JT, Lucas, Amanda, President, CEO; projects; gist/data-centric terms).
- Confirm no connectors are enabled.

**What to test (Weeks 1–2)**
- Run the existing **first-Monday task review** and JT's weekly priorities through the plugin's task/dashboard model instead of ad hoc tracking.
- Have EA capture the week's deliverables and "waiting on" items in `TASKS.md`; check whether the dashboard is clearer than our current markdown trackers.
- Test the memory: does it correctly decode SA shorthand and reduce re-explaining context?

**Success measures**
- Time saved per week on tracking/status (target: a noticeable reduction).
- Fewer dropped or forgotten items; the dashboard is genuinely used, not ignored.
- Memory reduces context repetition without storing anything sensitive.

**Owner:** Otto (with EA). **Risk:** low (no connectors, no sensitive data).

---

## Trial B — HR plugin (HR agent)

**Why:** It covers recruiting pipeline, onboarding plans, performance reviews, compensation benchmarking, and offer-letter drafting — the exact SOPs we built for HR. Because we already have the SA context, charters, and templates, we can customize it quickly.

**Setup (Day 1)**
- Install the HR plugin (skills only) into the company Cowork account; **do not enable external-data connectors** (e.g., market-data feeds) during the trial.
- Load our real assets so the plugin works the SA way, not generically: the Consultant offer template (`HR/Templates/`), the Onboarding and Personnel-file SOPs, and the compensation-survey methodology.

**What to test (Weeks 1–2)**
- **Offer materials:** run "draft all offer materials for a sample candidate" and compare against our current Job Offer SOP output. Does it match our template and flags, and save time? (President still signs; drafts only.)
- **Onboarding plan:** generate an onboarding plan for a sample role; compare to our populated Onboarding SOP.
- **Compensation benchmarking:** run a sample role and compare its method to our BLS-anchored, multi-source approach — does it triangulate or lean on a single source? Use anonymized/sample inputs only.
- **Performance review template:** generate one; check fit and defensibility.

**Success measures**
- Offer and onboarding drafts are accurate to our templates and faster to produce.
- Comp benchmarking is sound and sourced (not single-source or overconfident).
- No PII/compensation data leaves the company account; Sec. 7.3 respected throughout.

**Owner:** HR agent (via Otto); JT approves; President approves any offer content. **Risk:** low-to-moderate (PII/comp sensitivity — mitigated by anonymized inputs and company-account-only).

---

## Timeline

- **Day 1:** Install both (company account), disable connectors, seed with our context/templates.
- **Week 1:** Productivity in daily use (Operations/Otto/EA); HR runs the offer + onboarding tests.
- **Week 2:** Continue Productivity; HR runs comp-benchmarking + performance-review tests.
- **End of Week 2:** Go / no-go review with JT.

## Go / no-go decision

For each plugin, keep it only if it clears three bars: (1) measurable time saved, (2) output at least as good as our current SOP-driven work and ideally better-structured, and (3) no policy friction (connector-free, data-clean, human-approved). Otherwise, harvest any useful patterns into our own SOPs and drop the plugin.

## Rollback

Both are additive and connector-free, so rollback is simply removing the plugin. No data migration or system change is involved. If adopted, Otto records the decision, folds the plugin's best workflows into the relevant charters/SOPs, and Legal notes the adoption (and confirms no connector was enabled).
