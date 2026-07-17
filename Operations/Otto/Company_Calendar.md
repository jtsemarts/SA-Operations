# Semantic Arts — Company Calendar

**Maintained by:** Otto (for JT Metcalf, COO)
**Type:** Living document · **Version:** 1.8 · **Last updated:** July 6, 2026

A recurring calendar of deadlines and standing reminders: tax and compliance dates plus annual operating rituals (review job descriptions, run salary surveys, refresh insurance, etc.). Otto will suggest new entries as they come up in our work; JT confirms before anything is added.

## How to use this

- Entries are grouped two ways: a **recurring-cadence overview** (annual / quarterly / monthly) and a **month-by-month** list of dated deadlines.
- Tags: `[TAX]` `[PAYROLL]` `[COMPLIANCE]` `[HR]` `[OPS]` `[FINANCE]` `[CLIENT]` `[BENEFITS]`.
- **Dates roll:** when a federal deadline falls on a weekend or holiday, it moves to the next business day. Confirm the exact day each year.

## Assumptions (confirm / correct)

- Entity: **S-corporation** (Form 1120-S), **calendar tax year**.
- HQ: Fort Collins, Colorado; operations and/or payroll touch **many US states** (state deadlines vary — see the state section).
- Some items (retirement-plan Form 5500, ACA reporting, state annual reports) apply only if relevant to the firm. They are marked *(if applicable)*.
- These dates are general scheduling reminders, not tax advice. Confirm specifics with the firm's accountant (the COO coordinates with the firm accountant per the governance matrix).

---

## Recurring-Cadence Overview

### Annual rituals (HR / Ops — suggested timing, set by JT)

| Item | Tag | Suggested timing | Owner (per governance matrix) |
|---|---|---|---|
| Review and refresh executive & staff job descriptions | [HR] | Q1 (Jan–Feb) | President + COO |
| Run salary / compensation surveys | [HR] | Before annual comp review | COO (input), President (sets rates) |
| Annual performance review cycle | [HR] | Set by JT | President + COO |
| Benefits open enrollment | [HR] | Q4 (typical) | COO |
| Review & update employee handbook | [HR] | Annual | COO |
| Review business insurance coverage & seek bids | [OPS] | Annual | COO |
| Review incentive / bonus program & profit distribution | [FINANCE] | Year-end | Governance Committee + President |
| Team Summit | [OPS] | Annual | COO coordinates |
| Annual budget setting | [FINANCE] | Q4 for next year | CEO/President/COO |
| Review agent charters (Otto, Legal, Brand) | [OPS] | Quarterly (also annual) | COO |
| Review & update Operations Playbook | [OPS] | Quarterly | COO |
| HR end-of-year checklist | [HR] | Dec 1 | COO / HR agent |
| Vacation / PTO analysis | [HR] | End of December | COO |
| Review all recurring meeting invites & build next year's calendar | [OPS] | Dec 1 | COO |
| Update HR/payroll in Spark (positions, rates) | [HR] | Jan 1 | COO |
| Insurance audit | [OPS] | Jan 6 | COO |

### Quarterly

| Item | Tag | Due |
|---|---|---|
| Form 941 (employer payroll tax) | [PAYROLL] | Apr 30, Jul 31, Oct 31, Jan 31 |
| Estimated tax payments (shareholders / individual) | [TAX] | Apr 15, Jun 15, Sep 15, Jan 15 |
| Financial & operational reporting to Governance Committee | [FINANCE] | End of each quarter (cadence set by JT) |
| Operations Playbook + charter review | [OPS] | Each quarter |
| Trust distributions (3% of gross earned revenue; accrued each payroll, remitted via KeyNavigator) | [GOVERNANCE] | Quarterly |
| Trustee stipends ($500 each, 3 trustees; Abhishek held) | [GOVERNANCE] | Quarterly |
| Standing GC–trustee meeting: GC shares a fixed set of financials with the trustees and answers questions | [GOVERNANCE] | Quarterly |
| Prepare quarterly trustee-meeting financials (Amanda prepares, COO reviews, shared to GC) | [GOVERNANCE] | Start of each quarter |

### Monthly

| Item | Tag | Timing |
|---|---|---|
| Payroll runs & payroll-tax deposits | [PAYROLL] | Per schedule (monthly/semiweekly per IRS deposit rules) |
| Bookkeeping close & cash-flow projection | [FINANCE] | Month-end |
| Spending vs. budget review | [FINANCE] | Month-end |
| Review clients due for a 1:1 satisfaction check-in call (flag contracts near their midpoint) | [CLIENT] | 1st of month — Ops Manager (Amanda) |
| **Reminder to JT:** check which satisfaction calls need coordinating/scheduling | [CLIENT] | 1st of month |
| Prepare trustee financial reports | [FINANCE] | 1st of month |
| Otto reviews the calendar for recurring tasks due this week and adds them to the task board | [OPS] | Weekly (Monday, recurring task) |
| **Manual backup of the Agents workspace to SharePoint** (added redundancy; iCloud is the primary backup) | [OPS] | Monthly — 28th — JT / IT |

### Benefits & health-plan compliance (if applicable)

These apply to employers offering group health / prescription-drug coverage; several are handled by the insurer or TPA, but confirming the deadlines is the firm's responsibility. Note: employer ACA 1094-C/1095-C filing applies only to Applicable Large Employers (50+ full-time-equivalent employees); at ~30 people Semantic Arts is likely below that threshold, so confirm ALE status before relying on the ACA filing dates.

| Item | Tag | Timing |
|---|---|---|
| Medicare Part D creditable-coverage disclosure to CMS | [BENEFITS] | Within 60 days of plan-year start (Mar 1 for calendar-year plans) |
| ACA 1095-C / 1095-B furnished to employees | [BENEFITS] | Early March (~Mar 3) — if applicable |
| ACA 1094 / 1095 filing to IRS | [BENEFITS] | Feb 28 (paper) / Mar 31 (electronic) — if an ALE |
| RxDC prescription-drug data collection reporting | [BENEFITS] | June 1 |
| Form 5500 (retirement plan) | [COMPLIANCE] | July 31 (calendar-year plans) — if applicable |

Subsidiary-specific: **CAN 2200 forms** (Canada) — March. UK National Insurance is deducted automatically from pay. Confirm regional filings per subsidiary.

### Recurring operational tasks (migrated from Faithful Steward, July 2026)

Migrated from JT's Faithful Steward list per the July 2026 task migration. Owner is JT unless noted. Otto's weekly Monday review surfaces the ones due that week into the task board.

Each item has a hard-date anchor so it lands on the board with a real deadline. Weekdays follow the Thursday-to-Friday workweek.

**Weekly**

| Item | Tag | When (hard date) | Owner |
|---|---|---|---|
| QuickBooks (QB) export | [FINANCE] | Weekly — Thursday | JT |
| Email Pride — planned remit | [FINANCE] | Weekly — Monday | JT |
| Update the evaluation spreadsheet | [OPS] | Weekly — Monday | JT |
| Archive the cash plan | [FINANCE] | Weekly — Monday | JT |
| Update the cash & staff plan | [GOVERNANCE] | Weekly — Monday | JT (includes the AR-schedule bank info) |
| Update the Financial Evaluation Dashboard | [FINANCE] | Weekly — Monday | JT (Otto prompts for the numbers; see the dashboard SOP) |
| Verify the SA-Operations nightly backup ran | [IT] | Weekly — Friday | JT (glance at `~/Library/Logs/sa-ops-backup.log`; Otto helps interpret) |

**Daily (weekday)**

| Item | Tag | When (hard date) | Owner |
|---|---|---|---|
| Check Zoho for tasks | [SALES] | Weekday (Mon-Fri) | JT |

**Every 4 weeks** (exact dates in the "2026 pay periods" table below)

| Item | Tag | When (hard date) | Owner |
|---|---|---|---|
| Check and approve Expensify expense reports | [FINANCE] | Monday of the payroll-run week (Run payroll Fri − 4 days) | JT |
| Enter approved expense reports into the spreadsheet | [FINANCE] | Wednesday before period end — the "Expense review (Wed)" column | Amanda |
| Move approved expenses into the payroll spreadsheet | [PAYROLL] | At payroll run — the "Run payroll (Fri)" column | Amanda |
| Run payroll (President approves) | [PAYROLL] | Day after period end — the "Run payroll (Fri)" column | JT |
| Payroll finishing tasks | [PAYROLL] | Monday after period end — the "Payroll finishing (Mon)" column | JT |

**Monthly**

| Item | Tag | When (hard date) | Owner |
|---|---|---|---|
| Send Amanda the Key Bank line-of-credit payment amount | [FINANCE] | Monthly — 15th | JT → Amanda |
| Send Amanda the Canada bank statement | [FINANCE] | Monthly — 24th | JT → Amanda |
| Send Amanda the MS invoices | [FINANCE] | Monthly — 24th | JT → Amanda |
| Review upcoming monthly invoices | [FINANCE] | Monthly — 25th | JT |
| Coaches meeting | [HR] | Monthly — 3rd Friday | JT (chairs) |
| Ask a coach to prepare 2 discussion questions | [HR] | Monthly — Monday before the 3rd Friday | JT |
| Email the coaches agenda | [HR] | Monthly — Thursday before the 3rd Friday | JT |
| Prep the AI & Cyber Task Force agenda | [IT] | Monthly — Monday before the 3rd Thursday (meeting is the 3rd Thursday; next prep 2026-08-17) | JT |

**Quarterly** (note: overlaps the existing quarterly lines above — treat as the same obligations, not duplicates)

| Item | Tag | When (hard date) | Owner |
|---|---|---|---|
| Remit trust & trustee payments ($500 ACH per trustee; Dave may fund the trust) | [FINANCE] | Quarterly — 6th (next 2026-10-06) | JT |
| GC financial report | [GOVERNANCE] | Quarterly — early (next 2026-10-02) | Amanda |
| Quarterly checklist tasks | [OPS] | Quarterly (next 2026-10-02) | JT |
| Review lost deals for potential nurturing | [SALES] | Quarterly — 15th (Feb / May / Aug / Nov; next 2026-08-15) | JT |

### 2026 pay periods (payroll runs every 4 weeks; 13 periods)

Payroll is **every 4 weeks, not monthly (13 periods/year)**. The **workweek runs Thursday to Friday** — a week ends Thursday at midnight and starts Friday morning — so each period **starts on a Friday and ends on a Thursday**. Action dates key off the period-end Thursday: **JT approves Expensify expense reports** = the **Monday of the payroll-run week** (Run payroll Fri − 4 days); **Amanda enters the approved reports into the spreadsheet** = the **Wednesday before** the period ends (the Expense review column); **Run payroll** = the **day after** the period ends (the Friday Process date), when **Amanda also moves the approved expenses into the payroll spreadsheet**; **Payroll finishing tasks** = the **Monday after** the period ends. Pay lands ~10-11 days after the period ends. All exact dates are in the table below (use these hard dates, not a generic cadence).

| Period | Start (Fri) | End (Thu) | Expense review (Wed) | Run payroll (Fri) | Payroll finishing (Mon) | Paid |
|---|---|---|---|---|---|---|
| 1 | 2025-12-12 | 2026-01-08 | 2026-01-07 | 2026-01-09 | 2026-01-12 | 2026-01-19 |
| 2 | 2026-01-09 | 2026-02-05 | 2026-02-04 | 2026-02-06 | 2026-02-09 | 2026-02-16 |
| 3 | 2026-02-06 | 2026-03-05 | 2026-03-04 | 2026-03-06 | 2026-03-09 | 2026-03-16 |
| 4 | 2026-03-06 | 2026-04-02 | 2026-04-01 | 2026-04-03 | 2026-04-06 | 2026-04-13 |
| 5 | 2026-04-03 | 2026-04-30 | 2026-04-29 | 2026-05-01 | 2026-05-04 | 2026-05-11 |
| 6 | 2026-05-01 | 2026-05-28 | 2026-05-27 | 2026-05-29 | 2026-06-01 | 2026-06-08 |
| 7 | 2026-05-29 | 2026-06-25 | 2026-06-24 | 2026-06-26 | 2026-06-29 | 2026-07-06 |
| 8 | 2026-06-26 | 2026-07-23 | 2026-07-22 | 2026-07-24 | 2026-07-27 | 2026-08-03 |
| 9 | 2026-07-24 | 2026-08-20 | 2026-08-19 | 2026-08-21 | 2026-08-24 | 2026-08-31 |
| 10 | 2026-08-21 | 2026-09-17 | 2026-09-16 | 2026-09-18 | 2026-09-21 | 2026-09-28 |
| 11 | 2026-09-18 | 2026-10-15 | 2026-10-14 | 2026-10-16 | 2026-10-19 | 2026-10-26 |
| 12 | 2026-10-16 | 2026-11-12 | 2026-11-11 | 2026-11-13 | 2026-11-16 | 2026-11-23 |
| 13 | 2026-11-13 | 2026-12-10 | 2026-12-09 | 2026-12-11 | 2026-12-14 | 2026-12-21 |

---

## Month-by-Month Deadlines (calendar-year S-corp)

### January

- **Jan 15** — `[TAX]` Q4 (prior year) estimated tax payment due (individual shareholders).
- **Jan 31** — `[PAYROLL]` W-2s furnished to employees and filed with the SSA; 1099-NEC furnished to contractors and filed with the IRS.
- **Jan 31** — `[PAYROLL]` Form 940 (FUTA) annual return; Form 941 for Q4 (prior year).
- **Jan 1** — `[HR]` Update HR/payroll in Spark (positions, rates) for the new year.
- **Jan 6** — `[OPS]` Insurance audit.
- ACA employee forms are due in early March, not January (see Benefits & health-plan compliance) — *if applicable*.

### February

- `[HR]` Suggested window to **review job descriptions** ahead of the comp cycle.
- `[OPS]` Confirm state annual-report / registered-agent renewal dates for the year *(see state section)*.

### March

- **Mar 15** — `[TAX]` **Form 1120-S** (S-corporation return) due, with **Schedule K-1s** to shareholders. File **Form 7004** for a 6-month extension (to Sep 15) if needed.
- `[HR]` Suggested window to **run salary surveys** before setting rates.

### April

- **Apr 15** — `[TAX]` Individual returns (Form 1040) for shareholders; **Q1 estimated tax** payment.
- **Apr 30** — `[PAYROLL]` Form 941 for Q1.

### May

- `[OPS]` Mid-year insurance / vendor contract check-in (placeholder).

### June

- **Jun 15** — `[TAX]` **Q2 estimated tax** payment.

### July

- **Jul 31** — `[PAYROLL]` Form 941 for Q2.
- **Jul 31** — `[COMPLIANCE]` Form 5500 (retirement plan) for calendar-year plans *(if applicable)*.

### August

- `[OPS]` Suggested planning window for Q4 benefits open enrollment.

### September

- **Sep 15** — `[TAX]` Extended **Form 1120-S** due (if extension filed); **Q3 estimated tax** payment.

### October

- **Oct 31** — `[PAYROLL]` Form 941 for Q3.
- `[HR]` Benefits open-enrollment window (typical).

### November

- `[FINANCE]` Begin **annual budget** setting for next year.
- `[FINANCE]` Begin **bonus / profit-distribution** review (Governance Committee + President).

### December

- **Dec 1** — `[HR]` HR end-of-year checklist.
- **Dec 1** — `[OPS]` Review all recurring meeting invites and build next year's calendar/events.
- `[FINANCE]` Year-end financial close prep; confirm W-9s on file for all contractors before January 1099 filing.
- `[HR]` Finalize comp decisions and any year-end bonuses.
- `[HR]` Vacation / PTO analysis (end of month).

---

## State & Multi-Jurisdiction (placeholders — confirm per registration)

Because Semantic Arts operates across many states, several recurring obligations vary by jurisdiction. Fill these in per the states where the firm is registered, has employees, or has tax nexus. (Legal can help flag which states create obligations; the COO coordinates filings.)

- `[COMPLIANCE]` **Colorado periodic report** (Secretary of State) — due in the anniversary month of formation; confirm exact month.
- `[COMPLIANCE]` **Foreign-qualification annual reports** in each registered state — dates vary.
- `[COMPLIANCE]` **Registered-agent renewals** per state.
- `[TAX]` **State S-corp / pass-through entity returns** (incl. any PTE-tax elections) — dates vary, many mirror the federal Mar 15 / Sep 15.
- `[PAYROLL]` **State payroll withholding & unemployment** filings for each state with employees.
- `[TAX]` **State sales/use tax** filings where economic nexus is triggered *(if applicable)*.

---

## Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-06-30 | Initial scaffold: S-corp federal deadlines, recurring HR/Ops rituals, state placeholders. |
| 1.1 | 2026-07-03 | Added monthly (1st) client satisfaction check-in review (Ops Manager) and a monthly reminder to JT to coordinate calls. Added the [CLIENT] tag. Linked to the mid-contract check-in SOP. |
| 1.2 | 2026-07-03 | Added: 1st-of-month trustee financial reports; first-Monday task-suggestion review; quarterly trust distributions/stipends/GC-to-trustees; annual items from the internal checklist (HR EOY, vacation analysis, recurring-invite/next-year setup on Dec 1, Spark update Jan 1, insurance audit Jan 6); a Benefits & health-plan compliance section (Medicare Part D/creditable coverage, ACA, RxDC, 5500) with ALE caveat; and subsidiary (CAN 2200) note. Added [BENEFITS] tag. |
| 1.3 | 2026-07-06 | Migrated 15 recurring tasks from Faithful Steward into a new "Recurring operational tasks" section (weekly, every-4-weeks, monthly, quarterly). Changed Otto's review from first-Monday-monthly to weekly (surfaces recurring items due that week into the task board). |
| 1.4 | 2026-07-06 | Added a monthly manual SharePoint backup of the Agents workspace (redundancy; iCloud remains the primary backup while SharePoint use is not yet permitted). |
| 1.5 | 2026-07-06 | Documented that payroll runs every 4 weeks (13 periods/year, not monthly) and the Thursday-to-Friday workweek; added the dated 2026 pay-period schedule (Start/End/Process/Paid). Payroll actions key off the Process date. |
| 1.6 | 2026-07-06 | Assigned hard dates to the payroll-cycle tasks: Review expense reports = Wednesday before period end; Run payroll = day after period end (Friday); Payroll finishing = Monday after period end. Added these as columns in the pay-period table. |
| 1.7 | 2026-07-06 | Split the expense-reimbursement flow across the pay cycle: JT approves Expensify reports on the Monday of the payroll-run week; Amanda enters approved reports into the spreadsheet the Wednesday before period end; Amanda moves approved expenses into the payroll spreadsheet at the Friday payroll run. |
| 1.7 | 2026-07-06 | Gave every recurring task a hard-date anchor (a "When" column): weekly items pinned to a weekday (Thu/Mon), monthly items to a day-of-month (LOC 15th; Canada statement & MS invoices 24th; SharePoint backup 28th), quarterly items to an anchor date. So each lands on the board with a real deadline. |
| 1.8 | 2026-07-06 | Moved "Update bank info in the AR schedule" to Monday (grouped with the Monday cash & staff work); added a monthly "Review upcoming monthly invoices" on the 25th. |
| 1.9 | 2026-07-13 | Deduped: removed the standalone weekly "Update bank info in the AR schedule" (it duplicates the Monday cash & staff plan work); folded the note into the cash & staff plan row. |
| 2.0 | 2026-07-13 | Added weekly Monday "Update the Financial Evaluation Dashboard" (new Finance SOP; Otto prompts the COO for the required numbers). |
| 2.1 | 2026-07-14 | Added quarterly "Review lost deals for potential nurturing" on the 15th (Feb / May / Aug / Nov; next 2026-08-15). |
| 2.2 | 2026-07-14 | Added weekly Friday "Verify the SA-Operations nightly backup ran" (glance at the backup log; Otto interprets). |
| 2.3 | 2026-07-16 | Added monthly "Prep the AI & Cyber Task Force agenda" (Monday before the 3rd Thursday; next 2026-08-17). The meeting is the 3rd Thursday monthly and stays in JT's own calendar. |
