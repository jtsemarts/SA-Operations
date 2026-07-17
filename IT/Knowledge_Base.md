# IT — Knowledge Base: SMB IT & Security

**Maintained by:** IT · **Last updated:** July 15, 2026 · Living document

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

## 7. Microsoft 365 administration (working knowledge)

Semantic Arts runs on Microsoft 365, so IT should know the admin surfaces the COO operates and be able to draft step-by-step guidance for each. IT is advisory and draft-only: it explains where to go and what to do; the COO executes in the consoles.

**Admin consoles and what each is for:**

- **Microsoft 365 admin center** (`admin.microsoft.com`): users, groups, license assignment, domains, service health, and billing. The day-to-day console.
- **Security and privacy settings** (`admin.cloud.microsoft/?#/Settings/SecurityPrivacy`): a place for several bulk security and privacy toggles; useful for org-wide setting changes.
- **Microsoft Entra ID** (identity): users and groups, multi-factor authentication and Conditional Access, single sign-on app registrations, sign-in logs, and license assignment. Identity is the front line, so this is where MFA and access policy live.
- **Microsoft Defender portal** (`security.microsoft.com`): endpoint protection (Defender for Business), email protection (Defender for Office 365), alerts and incidents, Safe Links and Safe Attachments, and threat policies. (Requires the relevant Defender licensing; see the Defender briefing in `Operations/Otto/Knowledge/IT_KB.md`.)
- **Microsoft Intune** (device management): device enrollment, compliance policies, configuration profiles, and app management. This is what enforces the device baseline and onboards bring-your-own-device and mobile devices.
- **Exchange admin center**: mail flow rules, shared mailboxes, distribution lists, and anti-spam settings.
- **SharePoint and OneDrive admin**: site and library management and external-sharing controls (ties to the file-storage policy).
- **Microsoft Purview / compliance**: retention policies, data loss prevention, and the audit log (ties to the records-retention work).

**Common admin duties IT can draft steps for:**

- Onboard a user: create the account, assign a license, add to the right groups and distribution lists, and confirm MFA enrollment (ties to the HR onboarding SOP).
- Offboard a user: block sign-in, convert or delegate the mailbox, remove licenses, and revoke access (ties to Offboarding).
- Reset or re-enroll MFA for a user; enforce MFA and Conditional Access.
- Manage distribution lists and shared mailboxes.
- Review sign-in and audit logs when something looks off.
- Assign and reclaim licenses, and understand what each Microsoft 365 plan includes (Business Basic, Standard, Premium).

**Note:** no live administrative access while the connector policy is pending; IT drafts the steps and the COO carries them out. Keep this section current as Microsoft renames or moves consoles.
