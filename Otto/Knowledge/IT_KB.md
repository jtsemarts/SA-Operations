# Knowledge Base — IT (COO reference and professional development)

**Maintained by:** Otto (for the COO) · **Living document** · **Last updated:** 2026-07-15
**Sensitivity:** Internal
**Related:** AI & Cyber Task Force KB (`AI_Cyber_Taskforce_KB.md`); IT specialist agent (`Agents/IT/`); Operations Playbook (IT & Access Management).

## Purpose

A personal reference and learning hub for the COO on IT and security, since the COO is the firm's IT and compliance function. It holds the reference materials and a running list of topics to understand.

This is **distinct from the AI & Cyber Task Force KB**: that one is the working-group record (agendas, recommendations, action items, members). This one is for building the COO's own understanding and keeping the source documents in one place. The two cross-reference each other but serve different purposes.

## Reference documents

These live in the Documents folder.

| Document | What it covers |
|---|---|
| `SA_Information_Security_and_Device_Policy_DRAFT.docx` | The firm's employee-facing BYOD security policy, with a setup-instructions appendix. |
| `Personal_Computer_Security_Software_Guide.docx` | The types of security software, essential vs. high-security, PC and Mac. |
| `Password_Manager_Vendor_Research_and_Policy.docx` | Six-vendor comparison plus a draft password policy (Dashlane preferred). |
| `VPN_Vendor_Research_and_Policy.docx` | Six-vendor comparison plus a draft VPN policy (ExpressVPN for Teams preferred). |
| `Microsoft_Defender_Capabilities_and_Priorities.docx` | The Defender product family, licensing paths, and what to prioritize. |

## Admin consoles and tools

- **Microsoft 365 security and privacy settings (bulk updates):** https://admin.cloud.microsoft/?#/Settings/SecurityPrivacy
- Microsoft 365 admin center: https://admin.microsoft.com
- Microsoft Defender portal (if/when licensed): https://security.microsoft.com
- **Box (box.com):** stores archived and sensitive information.

## Open items

- **Backup procedures (to document):** work with **Jason** (external IT help) to document backup procedures for Microsoft 365 and Box.

## Runbooks

### Releasing a restricted (blocked) account

Use when an employee is hacked and Microsoft blocks their account from sending email (a restricted entity).

1. Open the blocked list and confirm the account: https://security.microsoft.com/restrictedentities
2. Attackers usually create hidden inbox "rules" in the mailbox, so delegate yourself access to it.
3. Go to the settings wheel and delete all the (malicious) rules.
4. Release the account: use the link in the original lock email, and follow the Microsoft guide: https://learn.microsoft.com/en-us/defender-office-365/outbound-spam-restore-restricted-users
5. Test that the account can send email again.

## Topics to understand (learning backlog)

- Password managers and secure sharing (company-managed vaults).
- VPN vs. zero-trust network access (ZTNA) and SASE.
- The zero-trust security model (verify explicitly, least privilege, assume breach).
- Microsoft 365 security: Defender for Business, Defender for Office 365, Intune, Entra ID.
- Endpoint protection and EDR (detection and response beyond antivirus).
- MFA and phishing-resistant sign-in (authenticator apps, passkeys, hardware keys).
- Disk encryption and the device security baseline.
- Backups and ransomware resilience.

## How this connects to the agents

Otto routes IT and security questions to the **IT specialist agent** (`Agents/IT/`), which can research topics and draft guidance (advisory, draft-only). This KB is where the COO keeps the resulting reference materials and personal learning notes.

## Change log

| Date | Change |
|---|---|
| 2026-07-15 | Created. Linked the five cyber reference documents, the Microsoft 365 security-settings console, and a topics-to-understand backlog. Cross-referenced the AI & Cyber Task Force KB and the IT agent. |
| 2026-07-15 | Added Box (box.com) as the store for archived/sensitive information; noted the open item to document Microsoft 365 and Box backup procedures with Jason (external IT). |
| 2026-07-15 | Added a runbook for releasing a restricted (blocked) account after an employee is hacked: check the restricted-entities list, delete malicious inbox rules, release via the lock email and Microsoft guide, then test. |
