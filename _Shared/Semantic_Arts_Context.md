# Semantic Arts — Firm Operating Profile (shared context for all agents)

**Maintained by:** Otto · **Last updated:** July 3, 2026 · Living document
**Purpose:** The common, firm-specific grounding every agent should use so recommendations and drafts fit Semantic Arts, not a generic company. Every agent should read this before producing work.

**North Star:** the firm's beliefs, vision, mission, values, employee-governance model, and goals live in `Semantic_Arts_North_Star.md` (this folder). It is the CEO/President-authored North Star every agent aligns work to. Otto stewards alignment; Brand guards how it is expressed. Read it alongside this profile.

**Marketing vault (reference):** Lucas's Marketing Intelligence OS is connected read-only at `~/git/sa-marketing-os`. See the Marketing KB (`Otto/Knowledge/Marketing_KB.md`) for how to navigate it. It is read-only and PII-sensitive; Airtable is the system of record for structured data.

## What we do

Semantic Arts is a specialist consulting firm in data, ontology, and knowledge-graph / semantic technology. We created the **gist** upper ontology and are recognized thought leaders in the **data-centric** movement (Dave McComb's *The Data-Centric Revolution*). We help enterprises model their data once, in a shared business language, so it can be reused across systems and, increasingly, power trustworthy AI. Our audience is senior and technical: data architects, chief data officers, and enterprise leaders.

## Size, structure, and footprint

- **~30 people**, privately held **S-corporation**, headquartered in **Fort Collins, Colorado**.
- **Time zone: Mountain Time (America/Denver).** JT and the firm operate on Mountain Time; interpret "today", "tomorrow", and all due dates accordingly.
- Clients in **nearly all US states** and some overseas; **Canada and UK subsidiary** considerations exist.
- Governance is transitional: a founder-CEO, an elected President, a COO, and an emerging **Governance Committee** with **trustees**.

## Leadership, roles, and governance (source of truth: the Governance Functions matrix)

- **CEO / Founder** — strategy, vision, product ownership of gist, brand and company vision/mission/values, final decision on acquisitions, sets incentive systems and billing/target-utilization, most senior client and owner/landlord relationships. Non-voting member of the Governance Committee.
- **President** — senior operating leader; owns client delivery and production; **final decision on hiring/firing, promotion, and pay rates**; **final signature authority on all proposals and customer contracts**; **P&L responsibility and bank-account signing authority**; approves payroll and the training budget; owns gist marketing and the major-accounts methodology. Elected, accountable to the Governance Committee.
- **COO (JT Metcalf)** — operations, HR, marketing operations, sales logistics, most of finance operations, IT/security, compliance, facilities, vendor management, and all financial/operational reporting. Direct reports: **Lucas** (Growth Marketing Manager) and **Amanda** (Operations Manager). Reports to the President. **There is no separate IT or compliance department; the COO performs these functions directly**, so IT/compliance work cannot be delegated to a department (levers are automation, vendor support, mechanical steps to Amanda, and AI/agent assistance).
- **Governance Committee** — selects and assesses the President, decides on CEO succession, owns the employee bonus program and coaching strategy, and gradually assumes CEO-level strategy, growth-target, and budget ownership. Administers its own elections (COO handles logistics).

## Decision & spending authority

- COO approves any single financial commitment **under $2,500** (except the training budget).
- President and COO **jointly approve $2,500 and above**.
- CEO gives final approval on **new debt over $100,000**.
- President holds bank-account signing authority and approves payroll and the training budget (may delegate the training budget to the COO for non-technical staff).

## Business model

Consulting delivery is the core business. Consultant pay is based on **billing rate and averaged chargeability** (an incentivized hourly model, paid for all hours including overtime, holidays, and PTO), which makes **utilization and realization** the metrics that drive both firm margin and individual pay. As a boutique with scarce senior ontology expertise, we can command premium rates. An **annual, profit-based bonus** rewards non-chargeable firmwide contribution (recruiting, sales, marketing) in cash-profitable years.

**Payroll and workweek (important, non-standard).** Payroll runs **every 4 weeks, not monthly**, which gives **13 pay periods per year**. The **workweek runs Thursday to Friday**: a week ends Thursday at midnight and starts Friday morning. So each pay period **starts on a Friday and ends on a Thursday** (a 4-week/28-day span), the payroll is **processed the Friday after the period ends**, and pay lands about 10-11 days later. The specific dated schedule for the year lives in the Company Calendar ("2026 pay periods"). Do not assume monthly payroll or a Monday-Sunday week when reasoning about pay, timesheets, or deadlines.

## Tools and systems

Rippling (HRIS/payroll), Microsoft 365, Confluence (knowledge base), GitHub, Expensify, Zoho (CRM / marketing automation), Spark (time/consultant system), AllegroGraph (product), QuickBooks, Employee Navigator (benefits), Human Interest (retirement), Constant Contact (newsletter), Vista Print, bgsecured (background checks). Background: the firm has intentionally **held off on most Claude connectors pending a company policy**, so the agents currently run **connector-free and draft-only**.

## Benefits (competitive, and relevant to comp/positioning)

Unlimited PTO; low-employee-cost health/dental/vision; BYOD device-purchase assistance (firm pays half of computer hardware); IRA with up to 3% match; $3,000/year individual training budget; student-loan repayment aid up to $100/month.

## Recurring operating rhythm

Daily standups and office hours; weekly executive, sales, staff, ops, and knowledge-exchange meetings; monthly company update, coaches meeting, and gist development; a Governance Committee cadence; quarterly trustee reporting and distributions; and the annual calendar (tax, benefits, HR rituals, budget). See the Company Calendar for dates.

## How the firm operates with Claude (the agent model)

**Otto** is the Chief of Staff and manages the agent team (**EA** plus specialists **Legal, Brand, HR, Finance, Sales, IT, Data, Research**). All agents are **advisory and draft-only**: they prepare work, and a human (COO, and where required the President) decides and acts. Agents coordinate **through Otto and the COO**, not directly with each other. The personal chief-of-staff agent, **Stan**, runs in JT's personal account and is **partitioned**; handoffs go through JT. Each agent keeps its charter, skill, essentials, and work in its own folder under `Documents/Agents/`.

**Brand QC applies to every agent, on a risk-tiered path** (see "Shared operating rules" below for the full rule). Every deliverable must meet the Brand writing rules and the SA22 Brand Kit. The review path depends on stakes: external, client-facing, or visual work gets a mandatory Brand review; internal quick items self-check against the writing rules and skip the Brand round-trip; when unsure, route to Brand. Otto enforces which tier applies.

**All agent use is governed by the Semantic Arts AI Usage Policy (v1.1).** Company-managed tools only for client data, IP, and deliverables; minimize and anonymize sensitive data; do not use AI to design ontologies/schemas/models or to make business decisions; keep AI in propose-don't-execute mode with human approval; connect to company systems only through company-managed, company-approved integrations; never store credentials in AI-accessible locations; disclose AI use in client work. Legal screens proposed actions against the policy — see `Agents/Legal/AI_Usage_Policy_Compliance.md` (policy PDF in `Agents/_Shared/`).

## Shared operating rules (all agents)

These rules apply to every agent; individual SKILL files reference this section rather than restating it.

**Draft, don't dispatch.** All agent work is advisory and draft-only. Agents prepare work; a human (the COO, and where required the President) decides and acts. No external actions, no connectors, pending the company connector policy.

**Brand QC (risk-tiered).** Quality is required, but the review path depends on stakes:

- **External, client-facing, or visual deliverables → mandatory Brand review** before returning to the COO. Brand checks against the writing rules and the SA22 Brand Kit (no em dashes; consistent terminology and capitalization; plain language; substantiated claims; voice on profile; and color/logo/typography/imagery conformance for anything visual). Brand returns a "pass" or a "fix list".
- **Internal quick items** (task/board edits, KB updates, routine internal notes and memos) → the drafting agent **self-checks** against the writing rules below and skips the Brand round-trip.
- **When unsure, route to Brand.** Otto enforces which tier applies.

*Writing rules (self-check list):* no em dashes; consistent terminology and capitalization (e.g., gist lowercase); plain language; substantiate claims; keep the firm's voice; concise and direct.

## Market position (useful for client-facing agents)

The data-centric, ontology-as-shared-language thesis Semantic Arts has advanced for two decades is now echoed by **BCG, EY, Forrester, and Gartner** (2025–2026), driven by enterprise and agentic AI needing a governed semantic layer. We differentiate on **execution and gist** against advice-only consultancies, and on **neutrality and depth** against tool-led vendors (TopQuadrant, Stardog, Ontotext, data.world, Enterprise Knowledge, Franz/AllegroGraph).
