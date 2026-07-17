# Financial Evaluation Dashboard — Update Checklist

**Maintained by:** Otto (for JT, COO) · **Type:** Living checklist · **Last updated:** 2026-07-13

**File:** `Financial_Evaluation_Dashboard_PROTOTYPE.html` (in the `Finance & Accounting/` folder).
**What it is:** a self-contained HTML dashboard (opens offline in any browser). All figures are driven by one editable block; there is no build step — you edit the block, save, and reopen the file.

## How it works (read once)

- All inputs live in a single block near the top of the `<script>`, marked `/* ===== REAL INPUTS (edit here) ===== */`. **Edit only inside that block**; everything below it is calculated automatically.
- Data is keyed by **absolute week number** (e.g., `916`), so history stays correct when the week advances. Weeks run **Friday → Thursday**; the number increments by 1 each Friday. (Week 916 = Fri Jul 10 – Thu Jul 16, 2026.)
- Edit by **variable name**, not line number — line numbers shift as data grows.
- Before doing any week math, check the real date: `TZ=America/Denver date +"%Y-%m-%d %A"`.

## A. Every week (at the Friday rollover)

Advance the "as-of" week so the dashboard centers on the new current week.

- [ ] `CURRENT_WEEK` — increment by 1 (e.g., `915` → `916`).
- [ ] `WK_START` — set to the **Friday** that starts the new current week, as `new Date(YYYY, M, D)` where **M is zero-based** (January = 0, July = 6). Example: Fri Jul 10, 2026 → `new Date(2026,6,10)`.
- [ ] Update the footer note's example if the convention line still cites the old week ("Week 916 = Fri Jul 10 to Thu Jul 16, 2026").
- [ ] Save, reopen the file, confirm the current-week tab is highlighted and reads "· current".

## B. Every Monday (data pull — from the Cash & Staff Plan routine)

- [ ] `cashByWeek` — add an entry for the week just pulled: `WEEK: <cash on hand minus line of credit>`. (Pulled from the bank accounts Monday morning; see the Cash & Staff Plan SOP.)
- [ ] `arByWeek` — add the week's **overdue** AR: `WEEK: <overdue $>`.
- [ ] `arTotalByWeek` — add the week's **total** AR: `WEEK: <total $>`. (Within-range AR = total − overdue, computed automatically.)
- [ ] `utilByWeek` — add the week's firm-wide billable utilization as a **decimal**: `WEEK: 0.75` for 75%. (The box shows the latest week at or before the selected week.)
- [ ] `predictedCashByWeek` — refresh/extend the predicted-cash series if the predictions changed (this drives the trajectory chart). Add new future weeks as the horizon rolls forward.

## C. As weeks close (actuals)

- [ ] `actualRevenueByWeek` — add actual earned revenue for each newly closed week.
- [ ] `actualLaborByWeek` — add actual burdened labor for each newly closed week (from Spark/payroll). Actual margin is then computed automatically for any week that has **both** revenue and labor.
- [ ] Update the three prose notes that cite specific closed weeks (they don't auto-update):
  - "actual margin (revenue minus labor, through wk **NNN**)"
  - "Still needed: anticipated wages (to project margin for wk **NNN+**)"
  - the chart note: "Actual margin = ... through wk **NNN**; ... actual labor for wk **NN–NN** isn't in yet."

## D. As needed (pipeline & assumptions)

- [ ] `plannedRevenueByWeek` — update planned revenue when the plan changes; extend to cover future weeks shown.
- [ ] `renewals` — keep the list current: `{ name, monthly, start:'YYYY-MM-DD' }`. Each renewal enters the pipeline at its start date, weighted by `RENEWAL_WEIGHT` (currently 0.75).
- [ ] `newWork` — add a deal **only once it reaches Converged Proposal**: `{ name, monthly, start:'YYYY-MM-DD', stage:'Converged Proposal' }`, weighted by `NEWWORK_WEIGHT` (currently 0.50).
- [ ] `anticipatedWagesByWeek` — **known gap:** currently empty (`{}`). Projected margin for current/future weeks stays blank until this is filled. Add anticipated wages per week when available.
- [ ] Targets/assumptions (rarely change): `WEEKLY_MARGIN_TARGET`, `CASH_BUFFER_GOAL`, `PAYABLE_LAG_DAYS`.

## E. Every time — verify before finishing

- [ ] Save the file and reopen it in a browser.
- [ ] Confirm the current week tab shows "· current" and the title reads the right week.
- [ ] Spot-check that the newest cash/AR values appear on the charts and no figure shows "—" where you just entered data (a "—" means a value is missing or miskeyed).
- [ ] Check the browser console for errors if anything looks blank (a stray comma or missing brace in the inputs block will stop rendering).

## Notes

- This is a **prototype** file (`_PROTOTYPE`); if it's promoted to a permanent dashboard, rename it and update this checklist's file reference.
- Draft-only: this dashboard is an internal reporting view. Figures come from JT's own pulls (bank, Spark, AR); no connector is involved.
- Related: Operations Playbook → Governance & Risk → "Cash & Staff Plan" SOP (the Monday pull) and "Trust interaction & trustee relations"; Company Calendar (weekly Monday cash & staff plan).
