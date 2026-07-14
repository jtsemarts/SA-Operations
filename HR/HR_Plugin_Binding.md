# HR Plugin — Semantic Arts binding

**Purpose:** Tie the Anthropic HR plugin's generic skills to Semantic Arts' actual templates, SOPs, and methodology so its output matches how we operate. Trial only; connector-free; draft-only; PII handled per AI Usage Policy Sec. 7.3 (minimize, anonymize, company account only). The President signs offers; the COO approves.

| HR plugin skill | Bind to our asset | Notes |
|---|---|---|
| `draft-offer` | `HR/Templates/OntologistOfferTemplate` + Job Offer SOP flags (Operations Playbook) | Use our exact Consultant offer template and the flagged items (at-will, FLSA, I-9, IP agreement). Consultant pay = billing rate x chargeability. President signs. |
| `onboarding` | Onboarding SOP (Operations Playbook) | Our real tools and steps (Rippling, M365, Confluence, GitHub, Expensify, AllegroGraph/Spark; CO new-hire reporting; go-to person; coach). |
| `comp-analysis` | Compensation review & salary-survey SOP + `HR/Work/` salary surveys | Our method: BLS actual-wage anchor + multi-source triangulation + affordability + benefits offset. Do not lean on a single source. Anonymized/sample inputs only. |
| `policy-lookup` | Employee handbook (Confluence), AI Usage Policy, PTO/leave SOP | Unlimited PTO; multi-state nuances; route legal questions to Legal. |
| `recruiting-pipeline` | Candidate Sourcing SOP + `HR/Recruiting/Talent_Sourcing_Tracker` | Public-source sourcing only; LinkedIn not accessible; President makes final hire/fire calls. |
| `performance-review` | Performance review SOP | President conducts reviews with COO (360 feedback); coaching program via GC strategy. |
| `interview-prep` | Recruiting & interview SOP | Structured, consistent scorecards. |
| `org-planning` / `people-report` | Governance Functions matrix + shared context | Reflect the CEO/President/COO/GC structure; ~30 people; multi-state. |

**Guardrails:** no external-data connectors during the trial; keep PII/comp data in the company account; every output is a draft for human review; the President approves offers.
