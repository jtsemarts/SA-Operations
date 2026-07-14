# AI Usage Policy — Compliance Reference & Flagging Checklist

**Maintained by:** Legal · **Last updated:** July 3, 2026 · Living document · *General information, not legal advice.*
**Source:** Semantic Arts AI Usage Policy v1.1 (Effective June 7, 2026; Owner: Rebecca Younes, President). Copy preserved at `Agents/_Shared/Semantic_Arts_AI_Usage_Policy_v1.1.pdf`.

Legal folds this policy into its knowledge base and screens every proposed agent action against it. If a proposed action trips any check in Section B, Legal flags it to Otto for the COO's review **before** it proceeds.

## A. Policy at a glance (what it requires)

- **Approved tools.** Company-managed Claude (incl. Claude Code and Cowork) and ChatGPT/Codex are the only tools permitted for client data, internal IP, or client deliverables. Non-company and personal AI accounts may not be used for client work, internal company work, or anything confidential/proprietary.
- **Data handling.** Sensitive information (client data; ontologies, schemas, taxonomies, semantic models; internal methodologies; proprietary code and private GitHub contents; NDA-covered info) goes only into company tools, minimum necessary. Highly sensitive information (PII; company or client financial data; regulated data such as HIPAA) requires heightened caution: anonymize, avoid bulk/full records, never enter into non-company tools. Rule of thumb: if you would not share it in a public forum, do not enter it unless using an approved tool per policy.
- **Discouraged uses.** AI must not be relied on to design ontologies, schemas, or data models; define core domain structures; make decisions needing deep domain or client-specific context; or make business, strategic, or organizational decisions. AI supports these; humans decide. Do not use AI as a substitute for initial problem framing and independent thinking.
- **Tools with system/resource access (Section 9 — names Cowork explicitly).** Company accounts only; least-privilege scope; human oversight of outputs **and actions**; no direct access to sensitive, production, or business-critical systems; run in isolated environments; **do not store API keys, credentials, or sensitive configuration in locations accessible to AI tools**; connectors/MCP configured with minimum permissions. GitHub: "propose, don't execute" — may open PRs, must not push to protected branches or trigger deployments; a human reviews and merges.
- **System integrations.** Non-company tools must never be connected to company systems. Connections to company systems are established only via company-managed tools and are approved at the company level, not by individuals.
- **Client work.** AI use in client work must be disclosed; approval obtained where a contract or client requires it; no AI where a client prohibits it.
- **Responsibility & ownership.** Humans review, validate, and remain fully responsible for all work product; AI-assisted work is company work product.

## B. Legal's flagging checklist (screen every proposed action)

Flag to Otto/COO before proceeding if a proposed action would:

1. Use a **non-company or personal AI account** for client data, internal company work, IP, or confidential material.
2. Enter **sensitive or highly sensitive data** (client data, SA ontologies/methodologies/proprietary code/private-repo contents, PII, financial, regulated) into any tool beyond the minimum necessary, or into a non-company tool at all.
3. Have AI **design an ontology, schema, or data model**, define core domain structures, or make a business/strategic/organizational decision (rather than support one).
4. **Connect an AI tool to a company system** (SharePoint, Slack/Teams, email, code hosts, SaaS) without a company-managed, company-approved integration; or connect any non-company tool to a company system at all.
5. Grant an AI tool **more than least-privilege** access, or access to sensitive, production, or business-critical systems.
6. **Push to a protected GitHub branch, merge without human review, or trigger a deployment** (AI stays in propose-don't-execute mode).
7. Store or expose **API keys, credentials, or secrets in a location the AI tool can access**.
8. Produce or touch a **client deliverable** without confirming client disclosure/approval of AI use.
9. **Send, publish, post, transact, or take any irreversible external action** without explicit human approval (reinforces the firm's draft-only posture).
10. Treat AI output as final **without human review and validation**.
11. **Adopt or use a pre-built skill / plugin / toolkit** (for example Anthropic's Productivity, HR, Operations, or Finance plugins) that either (a) includes a **connector or MCP / system access** — this requires a company-managed, company-approved setup with least privilege (Sec. 9.1, 9.4), so the connector piece must be disabled or approved before use; (b) would **ingest highly sensitive data** such as PII or financial records — apply Sec. 7.3 (minimize, anonymize, company tools only); or (c) is used to **make decisions or design ontologies/models** rather than to draft and support (Sec. 5.3, 8). Skill/workflow plugins that only draft, organize, or analyze non-sensitive internal work on the company account are permitted and encouraged (Sec. 3, 4.2); the connector, sensitive-data, and decision-making elements are the gates.

## C. Compliance review of what we have built (as of July 3, 2026)

Overall: strongly aligned. The agent team runs on the **company Claude/Cowork account**, is **connector-free**, **draft-only with the COO approving every action**, least-privilege, and partitioned from personal accounts. That matches the policy's highest-risk section (9) closely. Specifics:

| Area | Policy | Status |
|---|---|---|
| Tool & account | Company Claude/Cowork only | Compliant — company account |
| Human oversight of actions | Required (Sec. 9.1) | Compliant — draft-only, COO approves; "draft, don't dispatch" |
| System/connector access | None without company approval | Compliant — connector-free by design |
| GitHub | Propose, don't execute | Compliant — no repo actions taken; codify in IT SOP |
| Ontology/model design | Discouraged | Compliant — no ontology/schema work done here |
| Client deliverables | Disclosure/approval | Compliant — all work here is internal, not client-facing |
| Data entered | Minimize; company tools; anonymize | Compliant — public/benchmark data and internal ops docs; no client data or SA IP entered. (Talent tracker holds public professional info on external individuals; privacy caution still applies.) |
| Personal-account partition | Personal accounts barred from company work (Sec. 6.3) | Compliant by design — Stan (personal) is partitioned; **must not** receive company-confidential material |

### Items to remediate or confirm

1. **Service-account key stored in an AI-accessible folder (Sec. 9.2) — RESOLVED (2026-07-03).** JT deleted the entire `fs-sa-tasks-kit` folder, including `fs-service-account.json`. No credential remains in the workspace. Recommended follow-up for full hygiene: revoke that key in the Faithful Steward project's Google Cloud / Firebase console (IAM & Admin → Service Accounts → Keys) so it cannot be reused even if a copy leaked.
2. **Faithful Steward task integration (Sec. 6.3 and 9.4) — RESOLVED (2026-07-03).** The integration is retired; the kit that connected the company-workspace agent to the personal-account app was removed. If a task-management integration is revisited, it must be company-managed and company-approved per Section 9.4 (not a personal-account app), and any credential kept out of the AI-accessible workspace.
3. **Future connectors/MCP — confirm at approval time.** When the connector policy enables connectors, follow Section 9: company-managed, company-approved, least-privilege, propose-don't-execute for GitHub. Our current connector-free stance is compliant.

## D. Sources

- Semantic Arts AI Usage Policy v1.1 (June 7, 2026) — `Agents/_Shared/Semantic_Arts_AI_Usage_Policy_v1.1.pdf`
