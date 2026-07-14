# IT — Knowledge Base: SMB IT & Security

**Maintained by:** IT · **Last updated:** July 3, 2026 · Living document

## 1. Overview & why it matters for Semantic Arts

A ~30-person firm has an enterprise-sized attack surface relative to its headcount: cloud accounts, many SaaS tools, remote staff, and client data. This knowledge base captures the current baseline for identity, access, and phishing defense — the areas that matter most for a firm this size.

## 2. Current landscape & key trends (2025–2026)

Identity is the front line. **MFA blocks ~99.9% of automated credential attacks**, yet many businesses still have not enforced it everywhere ([miniOrange](https://www.miniorange.com/blog/multi-factor-authentication-mfa-best-practices/)). The 2026 emphasis is **phishing-resistant MFA** — FIDO2 hardware keys and passkeys — because the credential is cryptographically bound to the real domain, defeating fake login pages and the device-code/token-theft attacks we flagged earlier ([CISA](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf)). The recommended rollout order: enforce phishing-resistant MFA for sensitive systems starting with **admins, finance, and executives**; deploy SSO to cut the number of credentials; and add privileged-access management for elevated accounts.

Phishing itself has leveled up: attackers use LLMs to produce grammatically perfect, personalized lures. The countermeasure that works is continuous training — **monthly micro-sessions, quarterly simulations, role-specific training** — with organizations running continuous programs seeing **~70% fewer successful phishing attacks** than annual-only training ([Gray Group](https://www.graygroupintl.com/blog/cybersecurity-best-practices-2026/)).

## 3. Best practices

Enforce phishing-resistant MFA (start with privileged/finance/exec accounts). Consolidate logins behind SSO. Apply least privilege and deprovision access promptly at offboarding. Maintain a current SaaS/tool and access inventory. Run continuous, short security training plus simulations. Keep an incident-response runbook and issue verified staff advisories when threats emerge. Never handle credentials or secrets in plain text.

## 4. Application to Semantic Arts

SA runs on cloud tools (Microsoft 365, Rippling, Confluence, GitHub, Expensify, AllegroGraph/Spark) with remote and multi-state staff, so identity hygiene and prompt joiner/mover/leaver access control are the highest-leverage controls — which is exactly why the IT SOPs tie access provisioning to HR onboarding/offboarding. The device-code phishing advisory we drafted is a live example of the advisory function. IT is draft-only and connector-free today, so its value is in checklists, inventory, policy drafts, and verified advisories a human executes.

## 5. Recommendations / opportunities

Prioritize phishing-resistant MFA for admin, finance, and executive accounts and consider org-wide passkeys. Stand up and maintain the SaaS/access inventory. Formalize the joiner/mover/leaver checklist with HR. Start a monthly micro-training + quarterly simulation cadence. Keep the incident-response and staff-advisory templates ready. Feed the eventual connector/data policy with these controls.

## 6. Sources

- [MFA Best Practices 2026 — miniOrange](https://www.miniorange.com/blog/multi-factor-authentication-mfa-best-practices/)
- [Implementing Phishing-Resistant MFA — CISA](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf)
- [Four Cybersecurity Essentials for Businesses — CISA](https://www.cisa.gov/resources-tools/resources/four-cybersecurity-essentials-businesses)
- [Cybersecurity Best Practices for 2026 — Gray Group](https://www.graygroupintl.com/blog/cybersecurity-best-practices-2026/)
- [Multi-Factor Authentication — NIST Small Business Cyber](https://www.nist.gov/itl/smallbusinesscyber/guidance-topic/multi-factor-authentication)
