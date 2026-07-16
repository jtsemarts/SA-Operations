# Semantic Arts Operations Playbook

**Maintained by:** Otto (for JT Metcalf, COO)
**Type:** Living document · **Version:** 2.3 · **Last updated:** July 15, 2026

The single source of truth for how Semantic Arts runs internally: standard operating procedures (SOPs) across Sales, Client/Delivery, Marketing, HR, Administration, IT, Finance, Legal & Compliance, Knowledge Management, and Governance & Risk. This document holds the SOPs that are written and in use. Each section also carries a **Backlog (to write)** list — the SOPs we intend to document but haven't yet — so the scaffold stays lean while the roadmap is preserved. Otto proposes new SOPs as work surfaces them; JT confirms and Otto writes them.

## How to use this

- Each function has its own section. Written SOPs follow the **standard template** below.
- Status tags: `[DRAFT]` not yet reviewed · `[ACTIVE]` in use · `[NEEDS REVIEW]` due for a refresh.
- The **Backlog (to write)** list under each section names SOPs planned but not yet written. To promote one, copy the template and fill it in on JT's go-ahead.
- Otto reviews this playbook quarterly (see Company Calendar) and proposes updates; nothing changes without JT's sign-off.

### Standard SOP template (copy this for new SOPs)

```
### SOP: <name>
- Status: [DRAFT]
- Owner: <role>
- Trigger / frequency: <when this runs>
- Purpose: <what and why, one or two sentences>
- Steps:
  1. ...
  2. ...
- Tools / templates: <links or file names>
- Related: <other SOPs, calendar entries, charters>
- Last updated: <YYYY-MM-DD>
```

---

## 1. Sales

*Scope: lead handling, pricing, proposals, contracts, pipeline. Authority note (per governance matrix): the President holds final signature authority on proposals and customer contracts; the COO manages sales logistics and the sales team.*

**Backlog (to write):** Lead intake & qualification · Pricing & rate-setting (incl. discount approval) · Scoping & SOW drafting (templates) · Proposal creation & approval (President holds final signature) · Contract execution (MSA/SOW) · Sales-to-delivery handoff · Renewals & account expansion · Pipeline tracking & reporting · Win/loss review.

---

## 2. Client / Delivery Operations

*Scope: how client engagements are run from kickoff to closeout. Authority note: the President owns the consulting/delivery side and client deliverables; the COO supports logistics, reporting, onboarding admin, and invoicing. (Scope confirmation pending: confirm how much delivery process lives here vs. in a separate delivery-led document.)*

### SOP: Mid-contract client satisfaction check-in (keep / stop / start)
- Status: [ACTIVE]
- Owner: Operations Manager (Amanda) runs the check-in; President owns overall client satisfaction and handles escalations; COO (JT) runs the monthly review.
- Trigger / frequency: Roughly the midpoint of each client contract. Caught via a monthly review on the 1st (see Company Calendar) that flags contracts reaching their midpoint.
- Purpose: A light, structured check-in with the client sponsor partway through an engagement, to catch issues early and confirm the client is happy.
- Steps:
  1. On the 1st of each month, review active contracts and flag any near their midpoint that are due for a check-in. Otto surfaces this in the monthly calendar reminder; JT confirms the list.
  2. The Operations Manager emails the sponsor using the standard check-in email template (**to be drafted**) to request a brief call.
  3. Coordinate calendars and schedule the 1:1 call.
  4. On the call, ask the three questions: what should we **keep** doing, what should we **stop** doing, and what should we **start** doing.
  5. Capture the responses and make an explicit read on whether the client is happy. Log the outcome and any follow-up actions.
  6. Escalate any red flags to the President (owner of client satisfaction and final negotiator on contentious issues).
- Tools / templates: Client check-in email template (**to be drafted**, placeholder). Log outcomes alongside the engagement record.
- Related: Company Calendar (1st-of-month review and JT coordination reminder); SOP: Client satisfaction & NPS (backlog).
- Last updated: 2026-07-03

**Backlog (to write):** Engagement kickoff & client onboarding · Project & status management · Deliverable QA & review · Scope-change / change-order management · Client satisfaction & NPS · Project closeout & lessons learned.

---

## 3. Marketing

*Scope: website, campaigns, content, events, gist promotion, brand consistency. Authority note: COO holds day-to-day management of the marketing team, spend, and metrics; President owns gist marketing and ensures alignment to strategy; Brand agent reviews voice and consistency.*

**Backlog (to write):** Content production & review (Brand voice/consistency pass) · Thought-leadership publishing workflow · Campaign planning & execution (incl. DCAF, EDTS) · gist Forum / community management · Marketing-to-sales lead handoff · Event & conference sponsorship · Website & brand asset management · Brand & template library governance.

---

## 4. Human Resources

*Scope: recruiting, onboarding, performance, coaching, compensation, leave, benefits, compliance, offboarding. Authority note: President holds final hire/fire and sets pay rates; COO manages the HR function, recruiting, 360 feedback, and coaching operations. The **HR agent** supports and can execute every SOP in this section on command (draft-only) and flags gaps through Otto for the COO's review.*

### SOP: Candidate sourcing & talent-pool channels (ontology / knowledge-graph)
- Status: [ACTIVE]
- Owner: COO / Lucas (operator); JT approves any outreach
- Trigger / frequency: On an open need, plus a standing weekly sourcing pass (see the Talent Sourcing Tracker and the weekly scheduled task)
- Purpose: A reference for where and how to find ontology and knowledge-graph practitioners from public sources, for pipeline building.
- Capability note: Sourcing is limited to **public professional information**. LinkedIn is not accessible in the current setup (login-gated, terms of service, no connector), so LinkedIn people-search and the "Open to Work" signal are unavailable until connector tooling is approved. Highest-yield public sources are conference speakers, authors/publications, open-source contributors, and company team pages. Reliable identification of specifically junior/entry-level individuals is limited; treat career-stage as an inference to verify.
- Open-source ecosystems (where practitioners, including newer ones, are visible):
  - OBO Foundry / bio-ontologies, plus the OBO Academy that trains newcomers (biggest on-ramp for new ontologists)
  - LinkML (approachable modern entry point for semantic data modeling)
  - RDFLib (Python developers crossing into RDF/semantics)
  - Protégé (Stanford; students and new practitioners via mailing lists and plugins)
  - Also: kg-construct resources, Knowledge Graph Hub, PyKEEN, kglab; the `awesome-ontology` list is a good ecosystem map
  - Spotting early-career contributors: first-time or recent contributors, "good first issue" resolvers, docs/tutorial contributors, and learner-level questions on the mailing lists and issue trackers
- Posting & positioning venues (beyond company career pages):
  - Niche / community (highest signal, lowest cost): Knowledge Graph Conference (KGC); W3C "Semantic Web Job Mart" and the W3C "Ontologies and Knowledge Graphs in Industry" Community Group; Semantic Web Journal; Lotico; Code4Lib (strong for entry-level / library-metadata crossover); mailing lists (OBO, Protégé, semantic-web@w3.org, public-lod)
  - Mainstream boards (volume): LinkedIn, Indeed, Glassdoor, ZipRecruiter, Dice, Built In, regional boards (Tech:NYC), Wellfound for startups
  - Community chat / vendor ecosystems: Neo4j, Stardog, Ontotext GraphDB, TigerGraph communities; Wikidata; r/semanticweb
- Positioning for maximum exposure (leverage SA's credibility, not ad spend):
  - Own the KGC channel: speak, sponsor, and post roles there
  - Turn thought leadership into a talent magnet: pair postings with SA's published work (gist, Data-Centric) and the external validation now echoing it (BCG, EY, Forrester)
  - Use public gist open-source repos with well-labeled "good first issues" as a recruiting funnel that also lets SA observe contributors before outreach
  - Seed the niche boards for near-free targeted reach; reserve LinkedIn/Indeed for volume
- Governance: public information only; no private contact details captured; route any scaled data collection or storage of candidate personal data through Legal (privacy, GDPR for non-US, source terms of service) before it grows.
- Related: Talent Sourcing Tracker (`Agents/HR/Recruiting/Talent_Sourcing_Tracker.md`); SA Claude Implementation Proposal; Legal agent charter.
- Last updated: 2026-07-02

### SOP: Job offer & offer letter
- Status: [ACTIVE], uses Semantic Arts' standard Consultant offer template; recommended changes are flagged below for JT/Legal.
- Owner: President (approves and signs offers; final hiring authority) / COO (prepares and manages the process) / HR agent (drafts the offer letter and related materials on command from the standard templates) / Legal agent (reviews language and multi-state flags; this is not legal advice)
- Standard template: Semantic Arts Consultant offer letter (`OntologistOfferTemplate`), signed by the President. Related documents to include/attach: the Employee Agreement (confidentiality / IP assignment; its signature is a stated contingency), the Breakdown of Consultant Pay, the Benefits Book/summary, and the employee handbook (provided on signing). Use this exact template; do not redraft it. Fill every placeholder (`<Insert Date>`, `<Insert Name>`, `<Enter Position>`, `<Enter Bill Rate>`) each time.
- On command: an instruction such as "draft all offer materials for &lt;candidate&gt;" prompts the HR agent to assemble the offer letter and related documents from these templates, populated with the candidate's details, and returned as labeled drafts for review. Nothing is sent.
- Trigger / frequency: After a successful interview loop and a decision to hire
- Purpose: Make every offer consistent, complete, contingent on the right checks, and sound across the states SA hires in.
- Process:
  1. President approves the hire; confirm role, compensation, FLSA status, start date, and work location/state.
  2. COO prepares the offer letter using the standard elements below.
  3. Legal agent reviews at-will language, FLSA classification, and state-specific requirements (pay transparency; the Montana at-will exception); escalate anything gray to counsel.
  4. Attach a copy of the job description and the separate agreements to be signed (confidentiality / IP-assignment; arbitration if used).
  5. President signs; send to the candidate for signature with an expiration date.
  6. On acceptance, initiate contingencies (background check with FCRA notice/consent, reference checks, proof of work eligibility). Complete Form I-9 (Section 1 by day one, Section 2 within 3 business days); run E-Verify if applicable.
  7. File the signed offer and agreements; hand off to Onboarding and IT access provisioning.
- Required elements (checklist):
  - Position title and FLSA status (exempt vs. non-exempt; for exempt, note not eligible for overtime and show the per-pay-period equivalent of the annual salary)
  - Start date; full-/part-time; work location / remote and the state of employment
  - Reporting relationship
  - Compensation: base pay and frequency; any bonus/variable/commission; a brief benefits summary that references plan documents rather than restating them as guarantees
  - At-will statement (clear; either party may end the relationship at any time; Montana is the exception)
  - Contingencies (see below)
  - Requirement to sign the separate confidentiality / IP-assignment agreement (and arbitration agreement, if used) before start
  - Offer expiration date
  - Candidate signature line to accept
  - Attachment: a copy of the job description
- Standard contingencies (customize for SA):
  - Satisfactory completion of a background check (with the required FCRA notice and consent forms)
  - Satisfactory reference checks
  - Proof of identity and legal authorization to work in the US (Form I-9; E-Verify if applicable)
  - Drug screening (only if SA chooses to require it; commonly omitted for professional roles)
  - Execution of the confidentiality and IP-assignment agreement prior to the start date
- Cautions (route through Legal before finalizing):
  - Avoid promissory or fixed-term language. Quote pay per pay period rather than "annual salary of $X," and avoid words like "permanent" or "career," so the letter is not read as a contract overriding at-will.
  - Multi-state: several states require pay ranges in postings and/or on request, and new-hire notice rules vary; confirm for the candidate's work state.
  - Work-authorization sponsorship or international candidates need separate handling.
- SA-specific additions (for JT to fill in): _[e.g., benefits summary wording, unlimited-PTO policy reference, device-purchase-assistance note, equity/profit-share if any, relocation, remote-work policy, any required disclosures or certifications]_
- Flags / recommended changes to the current template (for JT + Legal to decide; the template is usable as-is in the meantime):
  1. **Add an explicit at-will statement** (either party may end employment at any time), with the Montana exception noted. The current template has no at-will language. (Legal to word.)
  2. **State FLSA classification explicitly.** The consultant model pays an incentivized hourly rate for all hours worked including overtime, holidays, and PTO, which reads as non-exempt; confirm and state the classification.
  3. **Add a work-authorization contingency.** Current contingencies are a background check and signature of the Employee Agreement; add proof of identity and authorization to work in the US (Form I-9; E-Verify if enrolled).
  4. **Confirm the Employee Agreement covers confidentiality and IP/invention assignment** and is executed before the start date (it is already named as a contingency).
  5. **Consider an offer expiration / response-by date**, separate from the deliberately flexible start date.
  6. **Attach the referenced documents** with the offer where possible: the Breakdown of Consultant Pay, the Benefits summary, and a copy of the job description.
  7. **Clean placeholders and typos each use:** the stray "?" in "<Enter Bill Rate?>", "until we get your up to speed" → "you," and the run-together "President / Semantic Arts, Inc." sign-off line.
  8. **Cross-check the job posting** that led to the offer for Colorado / multi-state pay-transparency compliance (posting-side, not the letter).
  9. **Soften "we expect to revisit this within your first year"** so it is not read as a guaranteed raise.
- Related: Recruiting & sourcing SOPs; Onboarding; IT & Access provisioning; Company Calendar; Legal agent (privacy, multi-state, work authorization); HR agent (drafts and assembles offer materials).
- Last updated: 2026-07-03

### SOP: Onboarding new hires
- Status: [ACTIVE]
- Owner: COO / Office Manager (executes most steps) / HR agent (drafts & tracks)
- Trigger / frequency: On offer acceptance
- Purpose: Bring a new hire fully online, compliant, equipped, and connected, using the firm's tools and checklist.
- First steps: run the background check (bgsecured portal; select the correct package, not "a la carte"); start the new hire in Rippling (send required documents first, since later steps depend on it); move files from the candidate folder to a new employee folder (add a "Recruiting" sub-folder for interview notes/resume).
- Compliance: complete Colorado New Hire Reporting (Employer Services Portal) within a few days of hire regardless of the employee's work state (needs PII); employee completes the I-9 in Rippling and the employer verifies documents (schedule a visual verification), then completes the employer portion; complete E-Verify after the I-9; set up state & local tax accounts (Rippling generates after first payroll) and send info back to Rippling.
- Orientation & benefits: payroll setup; benefits via Employee Navigator (send election invite); retirement via Human Interest (through Rippling; auto-starts ~4%); HSA via an individual Optum account if a HDHP is selected (collect the account number to add to the group).
- Systems & access (coordinate with IT & Access provisioning): Microsoft 365 (create user, temp password to personal email, apply licenses, add to distribution lists "Ontologists/Developers" and "SA Staff", forward meeting invites); AllegroGraph WebView (consultants only); Spark (create the profile; request the user account from Jamie); Confluence (invite via SA email, required before the handbook/onboarding-resource steps); Expensify (invite; revoke on exit); GitHub (invite; buy a seat if none free).
- Handbook & training: notify the employee the handbook is on Confluence (assumed read); point them to the Confluence onboarding guidelines / getting-started.
- People & meetings: schedule day-1, ~1-week, and ~1-month check-ins; set intro calls with their team; add to the staff plan (page, chart, capacity) and assign projects; assign a go-to person (a newer employee in a similar role; meet day 1) and a coach (at the next coaches meeting; send an email intro).
- Office & presence: office key, hall key, bathroom combo, garage/parking info if local; order business cards (Vista Print template); TagSwag gift card (ask Dave); request a short website bio + headshot; ONTOLOGY ONLY, add name + GitHub link to the gist Team wiki page; add to the Constant Contact newsletter list; post a welcome on the company LinkedIn; introduce to staff (Dave often does this at a staff meeting).
- Subsidiary-specific (CAN/UK, etc.): research/process region-specific forms; Canada health insurance (Sunlife) application; UK National Insurance (auto-deducted); set up regional tax accounts and check local labor law.
- Tools / templates: bgsecured (background check); Rippling (HRIS); Employee Navigator; Human Interest; Optum; Microsoft 365 admin; AllegroGraph; Spark; Confluence; Expensify; GitHub; Vista Print; Constant Contact.
- Related: Job offer SOP; IT & Access Management; Personnel file & records retention; Company Calendar (CO new-hire reporting, tax setup); Offboarding.
- Last updated: 2026-07-03

### SOP: Compensation review & salary surveys
- Status: [ACTIVE]
- Owner: COO (runs surveys, provides input) / President (sets rates)
- Trigger / frequency: Annual, before the compensation review cycle; or ad hoc when hiring/leveling a role
- Purpose: Benchmark and position pay using defensible, multi-source data rather than a single aggregator, and document the basis so decisions hold up to scrutiny.
- Inputs to confirm before starting (ask JT):
  1. Roles to benchmark.
  2. Geography basis: national, local (Fort Collins / Colorado), or national with a local cost-of-labor adjustment.
  3. Compensation scope: base only, base + bonus (total cash), or total comp including equity/profit-share.
  4. Firm revenue band (drives executive pay more than headcount).
  5. Peer framing: specialist professional-services/consulting, technology/data-services, or both compared.
  6. Percentiles to report (default 25th / 50th / 75th).
- Steps:
  1. **Anchor to actual-wage data first.** Pull BLS OEWS percentiles for the relevant occupation (e.g., Chief Executives 11-1011, General & Operations Managers 11-1021) and industry cut (e.g., NAICS 541600, Management/Scientific/Technical Consulting). BLS reflects real paid wages across all firm sizes and is the strongest central anchor.
  2. **Cross-check with commercial aggregators** (Payscale, ZipRecruiter, Glassdoor, Salary.com, SalaryCube), but discount sources that oversample large, VC/PE-backed, or enterprise firms. Identify which population each source reflects and exclude the outliers.
  3. **Apply an affordability lens.** Check executive comp as a percent of revenue for the firm's revenue band, and sanity-check the combined cost of overhead executives against typical consulting operating margins (roughly 15 to 30%).
  4. **Apply the total-rewards / benefits offset.** Quantify above-market benefits (unlimited PTO, low-employee-cost insurance, device-purchase assistance; roughly $12K to $24K of differentiated value) and position cash modestly below the market median (about 5%) where total reward stays competitive.
  5. **Triangulate** to a defensible range per role (25th / 50th / 75th) plus a single planning point, preserving internal-equity hierarchy across roles.
  6. **Keep owner distributions separate** from wage benchmarks; do not blend them.
  7. **Document** sources, assumptions, and caveats. Note BLS data aging (add roughly 3 to 5% wage growth to the latest finalized year) and apply a Colorado adjustment if localizing.
  8. **For board / compensation-committee actions**, validate the triangulated figures against one purchased professional-services survey (e.g., Croner, Empsight, or Gallagher) for a named third-party citation.
- Tools / templates: Prior worked example saved in Documents (`Executive_Salary_Surveys_Final_Position.docx` and the supporting markdown memos: initial pass, grounded position, final position).
- Related: Company Calendar (annual salary-survey reminder); Executive Job Descriptions (internal-equity hierarchy).
- Last updated: 2026-06-30

### SOP: Coaching program
- Status: [ACTIVE]
- Owner: COO (manages and chairs the program; contributes but is not a coach) / President (selects coaches with COO)
- Trigger / frequency: Monthly coaches meeting on the 3rd Friday
- Related: Coaching Program KB (`Agents/Otto/Knowledge/`); agenda archive `Coaches_Meeting_Agendas.docx`; Company Calendar
- Key facts:
  - The COO manages the program and contributes but does not coach. The President and CEO attend the meeting but do not coach directly.
  - Coaches meet monthly on the 3rd Friday, using the standard agenda (open & accountability; 30m open discussion; 15m two questions from a rotating coach; 15m book chapter; close with commitments/action items).
  - Current reading: "The Coaching Habit" (just starting).
- Process:
  1. **Monday before the meeting**, ask a designated coach to prepare 2 questions to discuss (rotate the responsibility).
  2. **Thursday before the meeting**, email the agenda to attendees.
  3. **3rd Friday**, run the meeting per the agenda template; capture commitments and action items.
  4. After the meeting, the COO follows up on action items (assign coaches to coachees, send announcements, rotate next month's question-bringer).
- Last updated: 2026-07-07

### SOP: Personnel file & records retention
- Status: [ACTIVE]
- Owner: COO / HR agent (maintains) / Legal agent (state-specific overlays)
- Trigger / frequency: Ongoing; review annually
- Purpose: Keep required employment records for the correct period and store sensitive items appropriately. Federal minimums are below; state laws may require longer, confirm with Legal for the states SA employs in.
- Storage: keep the I-9 separate from the personnel file; keep medical/benefits records separate from general personnel records.
- Federal retention minimums:
  - Job applications, resumes & interview notes: 1 year
  - Hiring records: 1 year
  - Promotion / transfer / termination records: 1 to 3 years
  - Performance evaluations: 2 to 3 years
  - Background checks: 1 year (5 years recommended)
  - Payroll records: 3 years
  - Form I-9: 3 years after hire or 1 year after termination, whichever is later
  - Timecards & attendance: 2 years
  - Benefit & retirement plan records: 6 years
  - COBRA notices: 6 years
  - FMLA leave records: 3 years
  - ADA accommodation requests: 1 year
  - Medical & exposure records: duration of employment + 30 years
  - Workplace injury logs: 5 years
  - Drug/alcohol test results: 5 years
  - Tax records: 5 years
  - EEOC complaints: 1 year or until resolution
  - Separation & exit interviews: 1 to 3 years
  - Whistleblower / retaliation complaints: 3 years after resolution
  - Affirmative action plans: 2 to 3 years
  - Union contracts: 3 years
  - Military leave records: indefinitely
- Related: Onboarding; Offboarding; Legal agent (state retention overlays).
- Last updated: 2026-07-03

### SOP: Offboarding
- Status: [ACTIVE]
- Owner: COO / President (termination decision) / Office Manager (executes) / HR agent (checklist & records)
- Trigger / frequency: On resignation or termination
- Purpose: Exit cleanly, revoke access, recover property, capture feedback, and preserve required records.
- Steps:
  1. Confirm the decision and effective date (the President owns termination decisions).
  2. Set up and conduct an exit interview (use the form in the shared folders).
  3. Revoke access across all systems: Rippling, Microsoft 365, Confluence, Expensify, GitHub, AllegroGraph/Spark, and any government/subsidiary accounts.
  4. Recover property: office/hall keys and devices; settle the device-purchase-assistance position if relevant.
  5. Remove from the staff plan (page, chart, capacity) and reassign active projects.
  6. If the person is a coach, reassign those they coached (typically at the next coaches meeting).
  7. Remove from newsletter/distribution lists and update the website team page.
  8. Process final pay per the employee's work-state rules (timing varies by state; route questions to Legal).
  9. Retain personnel records per the retention schedule (see Personnel file & records retention).
- Related: Personnel file & records retention; IT & Access Management; Legal agent (final-pay timing by state).
- Last updated: 2026-07-03

**Backlog (to write):** Recruiting & interview process · Performance review cycle (annual; COO administers 360) · PTO & leave administration (unlimited PTO) · Benefits administration & open enrollment · Multi-state employment compliance · Contractor vs. employee classification · Training-budget administration · Employee handbook maintenance.

---

## 5. Administration (Office Management & Facilities)

*Scope: office, facilities, vendors, travel, procurement, records, Team Summit logistics.*

**Backlog (to write):** Vendor & contract management · Insurance review & renewals (annual) · Travel & expense policy · Procurement (see Finance approval thresholds) · Records retention & destruction · Facilities & lease management · Team Summit logistics (annual).

---

## 6. IT & Access Management

*Scope: accounts, devices, tools, data, and security. Authority note: COO oversees; some items may be delegated or outsourced.*

**Physical IT resources (reference).**
- QuickBooks server: named "Plotter"; its login password is stored in LastPass (not recorded here).
- VPN and network switch: Meraki, administered through its web interface.
- All other office servers are managed internally by Jamie and are out of scope for this document.

**Backlog (to write):** Account provisioning & deprovisioning (joiner/mover/leaver; tie to HR onboarding/offboarding) · SaaS & tool inventory · Equipment & device management (incl. device-purchase-assistance) · Data backup & retention · IT security & incident response (incl. staff security advisories; a phishing staff-warning template exists from recent work, to be folded in — deferred per COO) · Acceptable use & access policy.

---

## 7. Finance

*Scope: bookkeeping, cash, AP/AR, payroll, billing, reporting, budgeting, tax. Authority note: COO handles day-to-day cash, bookkeeping, and approvals under $2,500; President holds bank signing authority, P&L responsibility, and joint approval at $2,500+; CEO approves new debt over $100K.*

### SOP: Expense reimbursement
- Status: [ACTIVE]
- Owner: COO (reviews and approves reports); Operations Manager (Amanda) (reconciles approved PDFs into the Expense Master Spreadsheet and the payroll run)
- Trigger / frequency: Every pay cycle (every 4 weeks). COO approval on the Monday of the payroll-run week; Operations Manager reconciliation on the Wednesday before period end (see the "2026 pay periods" table in the Company Calendar for exact dates).
- Approval rules: the firm's Travel & Expense Policy on Confluence is the source of truth for what is reimbursable and any limits. Review every report against it: https://semarts.atlassian.net/wiki/spaces/AD/pages/2250997793/Travel+Expense+Policy
- Related: Payroll processing SOP (the Expense Master Spreadsheet feeds the payroll spreadsheet); Company Calendar (pay-period schedule); Administration (travel & expense policy).
- Process:
  1. Staff submit expense reports in Expensify.
  2. The COO reviews each report for approval against the Travel & Expense Policy (link above).
  3. If a report has violations or raises questions, the COO contacts the staff member directly to rectify before approving.
  4. Once the COO approves a report, save it as a PDF into the Expenses folder on SharePoint.
  5. On the Wednesday before payroll, the Operations Manager reviews the PDFs and confirms every approved report is captured in the Expense Master Spreadsheet.
  6. The Expense Master Spreadsheet is added to the payroll spreadsheet so approved expenses are reimbursed with that payroll run (see the Payroll processing SOP).
- Last updated: 2026-07-14

### SOP: Payroll processing
- Status: [NEEDS REVIEW] (has content; formalize the full step list)
- Owner: COO (processes) / President (approves)
- Trigger / frequency: Per pay cycle (every 4 weeks; 13 periods/year — see the Company Calendar pay-period table)
- Related: Company Calendar (941 / payroll-tax deadlines); Governance (Trust interaction & trustee relations)
- Payroll-finance task: at each payroll, calculate 3% of earned revenue (gross) as the trust contribution and accrue it. Accrued amounts are remitted to the trust quarterly (see Governance: Trust interaction & trustee relations).
- Last updated: 2026-07-07

### SOP: Financial Evaluation Dashboard weekly update
- Status: [ACTIVE]
- Owner: COO (provides the numbers and reviews the result); Otto (rolls the week forward, edits the inputs, syntax-checks, syncs, and presents)
- Trigger / frequency: Every Monday, alongside the Cash & Staff Plan update
- Purpose: Roll the Financial Evaluation Dashboard forward one week and refresh every live input so it reflects the latest cash, AR, utilization, margin, and pipeline.
- File: `Financial_Evaluation_Dashboard_PROTOTYPE.html` (in the `Agents/` folder, the repo root). All figures live in the `REAL INPUTS` block near the top of the script and are keyed by absolute week number. Round every dollar figure to a whole number.
- How Otto runs it: when the COO asks to update the dashboard, Otto checks the date, computes the new week, and prompts the COO with the checklist of values below in one consolidated ask (the COO can answer "no change" to any line). Otto then edits only the `REAL INPUTS` block, advances the week, syntax-checks the script, keeps the working copy in sync, sanity-checks (within-range AR not negative, no missing values in the KPI row), and presents the updated file.
- Metrics required to fully update (every week):
  1. Cash on hand (cash minus line of credit), Monday bank pull, into `cashByWeek`
  2. Overdue AR as of today, into `arByWeek`
  3. Total AR as of today, into `arTotalByWeek` (within-range is computed as total minus overdue)
  4. Firm-wide billable utilization percent, into `utilByWeek` (entered as a decimal, e.g. 0.75)
  5. Actual revenue for each newly closed week, into `actualRevenueByWeek`
  6. Actual labor for each newly closed week, into `actualLaborByWeek` (pairs with revenue to produce actual margin)
  7. Anticipated wages for the current and upcoming weeks, into `anticipatedWagesByWeek` (drives projected margin)
  8. Updated predicted-cash forecast by week, into `predictedCashByWeek`
- As needed (confirm each week, change only if different):
  9. Renewals added, removed, or repriced or rescheduled, in `renewals`
  10. New-work deals that have reached the Converged Proposal stage, in `newWork`
  11. Planned-revenue forecast changes, in `plannedRevenueByWeek`
- Mechanical roll-forward (Otto): set `CURRENT_WEEK` to the new week and `WK_START` to that week's Friday. Weeks run Friday to Thursday and the number increments by one each week.
- Fixed assumptions (change only on the COO's instruction): renewals weighted 75%, new work 50%, 60-day (about 9-week) payable lag, $1,000,000 cash buffer goal, $10,000 weekly margin target.
- Tools / templates: operator card with the exact prompt and variable map (`Agents/Otto/Work/Financial_Dashboard_Update_Checklist.md`).
- Related: Cash & Staff Plan SOP (same Monday cadence); Company Calendar (weekly Monday dashboard update).
- Last updated: 2026-07-13

### SOP: Project setup (operational onboarding)
- Status: [ACTIVE]
- Owner: COO (operational and financial setup); Operations Manager (Amanda) supports; President owns delivery
- Trigger / frequency: When a new project or engagement is won, before work starts
- Purpose: Stand up a new project cleanly across systems, billing, risk, and staffing so it starts on solid footing.
- Steps:
  1. Set up the project in Spark (project record and code, budget, and assignments).
  2. Set up the project in QuickBooks for billing and accounting.
  3. Confirm the invoice procedure for this client (how and when to invoice; any client portal or format).
  4. Use a purchase order where the client requires one; capture the PO before billing against it.
  5. Add the project to the AR Schedule.
  6. Verify insurance requirements are met; add the client as an additional insured where required.
  7. Update the staff plan (assignments and capacity).
- Related: Project closing (financial close); Cash & Staff Plan; Expense reimbursement; Client/Delivery engagement kickoff (backlog).
- Last updated: 2026-07-15

### SOP: Project closing (financial close)
- Status: [ACTIVE]
- Owner: COO (executes the close); project leader (confirms the project is finished); President (coordinates on write-offs and any non-standard RCE handling)
- Trigger / frequency: When a project has finished, ad hoc
- Purpose: Close a finished project cleanly in Spark and QuickBooks: capture all time, handle any budget overage, confirm all invoices are billed, and zero out the unbilled and unearned balances. ("RCE" and "ER" are used here as the firm's own terms.)
- Steps:
  1. Confirm with the project leader that the project is finished.
  2. In Spark, set the project end date so the project goes inactive once all time charges have been entered.
  3. Check budget status and handle any overage:
     - At or below budget: the project is ready for close in QuickBooks.
     - Above budget: write off the overage using an RCE in Spark. Generally apply the RCE in the current period and divide the overage evenly across all staff on the project. This varies in some cases; coordinate with the President.
  4. Close in QuickBooks:
     1. Ensure all project ER is entered in QuickBooks. If entering for the current period, set the date to the same date as the other ER for this period.
     2. On the Balance Sheet, open Unbilled Contracts, filter by the project name, and confirm all invoices for the project have been submitted.
        - For a T&M project, it may not have burned all the budget, so you may need to modify the total unbilled/unearned entry.
     3. Once the project is fully billed, return to the Balance Sheet and open Unearned Revenue.
     4. If the unbilled/unearned and the total project earned revenue have been resolved properly, this should be a small number. If so, use the memorized transaction to write it up or down and zero out the item.
- Tools / systems: Spark (project end date; RCE); QuickBooks (Balance Sheet: Unbilled Contracts and Unearned Revenue; memorized transaction).
- Related: Payroll processing (RCE lands in the current period); Expense reimbursement (project ER); Cash & Staff Plan (staff allocations roll off); Client/Delivery "Project closeout & lessons learned" (the delivery-side closeout, still in backlog).
- Last updated: 2026-07-14

**Backlog (to write):** Accounts payable & purchasing approvals (thresholds: COO <$2,500; President+COO $2,500+; CEO debt >$100K) · Accounts receivable & invoicing · Time tracking & billing · Project profitability & utilization · Collections / AR follow-up · Monthly close & cash-flow projection · Financial & operational reporting (quarterly to GC) · Budgeting (annual) · Tax & compliance coordination · Annual audit & tax-prep coordination.

---

## 8. Legal & Compliance

*Scope: contracts, privacy, multi-state and international compliance, retention, filings. Authority note: ties to the Legal agent (issue-spotting and boundary-flagging only, not legal advice); the President and CEO meet with outside counsel as needed.*

**Backlog (to write):** Contract intake & review workflow · NDA handling (mutual/one-way) · Data protection & privacy (GDPR / DPAs) · Multi-state & international compliance monitoring · Records retention & legal hold · Regulatory & filing tracking.

---

## 9. Knowledge Management

*Scope: the firm's methodology and intellectual capital. Especially important for a semantics firm where the methodology is core IP.*

**Backlog (to write):** gist & ontology asset stewardship (President oversight) · Reusable templates & methodology library · Internal documentation / knowledge base · Client deliverable archive & reuse (respect confidentiality) · Onboarding knowledge base.

---

## 10. Governance & Risk

*Scope: governance operations, authority, risk, and continuity. Authority note: the Governance Committee governs itself, selects and assesses the President, and owns the bonus program; the COO administers committee elections.*

### SOP: Trust interaction & trustee relations
- Status: [ACTIVE]
- Owner: COO (administers); Governance Committee (owns the trustee relationship)
- Trigger / frequency: 3% accrued each payroll; remittance and stipends paid quarterly; standing quarterly trustee meeting
- Payment method: KeyNavigator
- Related: Company Calendar (quarterly trust items; GC reports to trustees); Finance (Payroll processing accrual)
- Key facts:
  - Trust funding: the trust receives 3% of all earned revenue (gross). The 3% is calculated at each payroll and accrued (see Payroll processing), then remitted quarterly.
  - Trustee stipends: $500 per trustee, per quarter. There are three trustees.
  - Hold on Abhishek: Abhishek is working toward citizenship and cannot be paid at this time, so his payments are on hold. Create the bill in QuickBooks so the liability is recorded, but do not remit it until he is cleared to be paid.
- Quarterly financials for the trustees:
  - At the beginning of each quarter, the Operations Manager (Amanda) prepares the financial information for the COO to review.
  - Once the COO has reviewed it, the package is shared with the Governance Committee.
  - A standing quarterly meeting is held where the Governance Committee shares a fixed set of financials with the trustees and answers their questions.
- Quarterly payment process:
  1. Sum the trust contributions accrued at each payroll during the quarter.
  2. Create the QuickBooks bills: the trust remittance, plus a $500 stipend for each of the three trustees.
  3. Pay the trust remittance and the eligible trustee stipends via KeyNavigator.
  4. For Abhishek, leave the bill created but unpaid (held) until he is cleared to be paid.
  5. Record the payments and update the cash plan.
- Last updated: 2026-07-07

### SOP: Cash & Staff Plan
- Status: [ACTIVE]
- Owner: COO (updates and maintains the plan to inform the President and CEO)
- Trigger / frequency: Every Monday, and additionally as needed
- Files: Operations Team folder
- Related: Company Calendar (weekly Monday cash & staff plan); AR schedule (to be documented in a future Finance SOP); Financial Evaluation Dashboard (update steps: `Agents/Otto/Work/Financial_Dashboard_Update_Checklist.md`)
- Cash Plan:
  1. Monday morning, pull the bank balance from the bank accounts.
  2. Copy the predictions and paste them into the appropriate tab.
  3. Review the AR tab for any known changes to current or future bills or invoices.
  4. Change the date in the filename to today.
- Staff Plan:
  1. Pull the current project assignments from Spark, along with the actual weekly utilization.
  2. Update SP-Raw with the current project-assignment information.
  3. Update SP-Cap with any changes to consultant availability (vacations, extended absence). New hires or terminations also require allocations to be updated.
  4. Update SP-Actual with the actual consumption numbers.
  5. Review the Staff Plan tab to confirm it pulls the current week, move the red arrow in the chart, and double-check for accuracy.
  6. Change the filename to reflect today's date.
- Note: the accounts receivable process referenced in the AR tab will be documented separately in a future Finance SOP.
- Last updated: 2026-07-07

**Backlog (to write):** Governance Committee operations · Decision & authority matrix maintenance (source of truth: Executive Job Descriptions) · Risk register · Business continuity & disaster recovery · Policy management & review cadence (incl. the forthcoming connector/data policy).

---

## Index of active SOPs

Written and in use:

- **Client / Delivery:** Mid-contract client satisfaction check-in (keep/stop/start)
- **HR:** Candidate sourcing & talent-pool channels · Job offer & offer letter · Onboarding new hires · Compensation review & salary surveys · Coaching program · Personnel file & records retention · Offboarding
- **Finance:** Expense reimbursement · Payroll processing (needs review) · Financial Evaluation Dashboard weekly update · Project setup (operational onboarding) · Project closing (financial close)
- **Governance & Risk:** Trust interaction & trustee relations · Cash & Staff Plan

Everything else is captured in the per-section **Backlog (to write)** lists above.

## Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-06-30 | Initial scaffold across Sales, Marketing, HR, Administration, Finance with SOP placeholders and authority notes from the governance matrix. |
| 1.1 | 2026-06-30 | Populated HR → "Compensation review & salary surveys" SOP with the multi-source benchmarking methodology, marked [ACTIVE]. |
| 1.2 | 2026-06-30 | Added five sections (Client/Delivery Operations, IT & Access Management, Legal & Compliance, Knowledge Management, Governance & Risk) and expanded SOP placeholders across all sections. Moved IT security and equipment/device management from Administration to IT & Access Management. |
| 1.3 | 2026-07-02 | Added HR → "Candidate sourcing & talent-pool channels" SOP ([ACTIVE]) with open-source ecosystems, posting venues, and positioning strategy for ontology/KG talent. Created the Talent Sourcing Tracker and a weekly sourcing scheduled task. |
| 1.4 | 2026-07-02 | Added HR → "Job offer & offer letter" SOP ([NEEDS REVIEW]) with required elements, standard contingencies, at-will/FLSA/multi-state cautions, and an SA-specific section for JT to customize. |
| 1.5 | 2026-07-03 | Added Client/Delivery → "Mid-contract client satisfaction check-in (keep/stop/start)" SOP ([ACTIVE]), owned by the Operations Manager; email template to be drafted. |
| 1.6 | 2026-07-03 | Job Offer SOP set to use SA's standard Consultant offer template ([ACTIVE]); added a flags/recommended-changes list (at-will, FLSA, I-9, IP agreement, expiration, attachments, cleanup). Noted the HR agent supports/executes HR SOPs on command. |
| 1.7 | 2026-07-03 | Populated Onboarding and Offboarding SOPs ([ACTIVE]) from the internal Onboarding Checklist; added a "Personnel file & records retention" SOP ([ACTIVE]) from the Personnel File Checklist (federal retention minimums, I-9 stored separately). |
| 1.8 | 2026-07-10 | Trimmed the empty [DRAFT] SOP placeholders into compact per-section "Backlog (to write)" lists, keeping all [ACTIVE] SOPs verbatim. Reduces document size while preserving the roadmap. Added an "Index of active SOPs". |
| 1.9 | 2026-07-13 | Added Finance SOP "Financial Evaluation Dashboard weekly update" ([ACTIVE]): the metric list required to fully update the dashboard each Monday and the operating rule that Otto prompts the COO for those numbers, edits the inputs, verifies, and presents. Points to the operator card checklist. |
| 2.0 | 2026-07-14 | Expanded the Expense reimbursement SOP with the full flow: approval against the Confluence Travel & Expense Policy, direct rectification of violations with staff, saving approved reports as PDFs to the SharePoint Expenses folder, and the Operations Manager reconciling PDFs into the Expense Master Spreadsheet (Wednesday before payroll) which feeds the payroll spreadsheet. |
| 2.3 | 2026-07-15 | Added Finance SOP "Project setup (operational onboarding)" ([ACTIVE]): Spark and QuickBooks setup, invoice procedure, PO where the client requires it, add to the AR Schedule, verify insurance and add the client as additional insured, and update the staff plan. Pairs with Project closing. |
| 2.2 | 2026-07-15 | Added a "Physical IT resources" reference note under IT & Access Management: QuickBooks server ("Plotter", password in LastPass), Meraki VPN/switch via web interface, other office servers managed by Jamie (out of scope). |
| 2.1 | 2026-07-14 | Added Finance SOP "Project closing (financial close)" ([ACTIVE]): confirm finish with the project leader, set the Spark end date, handle any over-budget overage via an RCE (evenly across project staff, President coordinates exceptions), then close in QuickBooks (project ER entered, Unbilled Contracts billed, Unearned Revenue zeroed via the memorized transaction; T&M caveat noted). |
