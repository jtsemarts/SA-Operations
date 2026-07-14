# DRAFT — Staff Security Warning (for COO review before sending)

**Status:** Draft prepared by Otto. Not sent. Review, edit, and send from your own account.
**Suggested To:** All Staff
**Suggested From:** JT Metcalf, COO
**Subject:** Security alert: new Microsoft 365 scam that gets past your password and MFA — what to watch for

---

Team,

The FBI issued a public warning (May 21, 2026) about a fast-spreading scam targeting Microsoft 365 users across **Outlook, Teams, and OneDrive**. I want everyone aware of it because it is designed to slip past the two things we normally rely on: your password and your multi-factor authentication (MFA).

**Please take two minutes to read this.**

## What's happening

Attackers are using a phishing kit (nicknamed "Kali365") that steals access to your Microsoft account **without ever needing your password and without triggering an MFA prompt you'd recognize as suspicious.**

Here's the trick that makes it dangerous:

1. You receive an email that looks like a normal document share or cloud-service notification. It includes a short **"device code"** and asks you to go to a Microsoft verification page and enter it.
2. The page is **the real Microsoft page** — not a fake — so it looks completely legitimate. You may even sign in and complete your normal MFA.
3. But by entering that code, you are unknowingly **authorizing the attacker's device** to log into your account.
4. The attacker then has ongoing access to your Outlook, Teams, and OneDrive. Because they hold a valid access token, **changing your password later does not necessarily lock them out.**

The reason this works is that you're being asked to approve a login that *someone else started*. The code is real, the Microsoft page is real — but the session you're approving isn't yours.

## What to watch for

Treat any of these as a red flag:

- An email, Teams message, or text asking you to **enter a "device code," "verification code," or "pairing code"** on a Microsoft sign-in page — especially if **you didn't just start a sign-in yourself**.
- A **document-share or file notification** (OneDrive, SharePoint, "you've received a document") that pushes you to "verify" by entering a code.
- A sense of **urgency** — "verify within 10 minutes," "your access will be suspended," etc.
- A code that **arrives unexpectedly** when you weren't trying to log in to anything.
- Messages aimed at people with sensitive access — **finance, leadership, and anyone with admin rights are prime targets.**

The simplest rule: **if you did not personally start a login, do not enter any code anyone sends you.** A legitimate device code only ever appears on a screen *you* are actively signing in from (like setting up a new app or device) — it never arrives by email or chat for you to type in.

## What to do

- **Don't enter the code.** Don't click "approve" or "continue."
- **Report it** — forward the message to me (or reply here) so we can flag it for others. Better to over-report than miss one.
- **Verify out-of-band.** If a "shared document" looks like it might be real, confirm with the sender by a separate channel (call, separate message) before doing anything.
- **If you think you already entered a code or approved a login you didn't start:** tell me immediately. Don't wait. We'll get your account sessions revoked and re-secured right away — and note that a password reset alone may not be enough, so prompt reporting matters.

## What we're doing on our end

We're reviewing our Microsoft sign-in settings, including the option to **block "device code" logins** organization-wide (the FBI's top recommendation), with exceptions only where a real business process needs it. I'll follow up as we finalize that.

Thanks for staying sharp on this. When in doubt, slow down and ask — that instinct is our best defense.

[Name]

---

## Notes for the sender (remove before sending)

- **Source:** FBI/IC3 Public Service Announcement I-052126-PSA, "Kali365 Phishing-as-a-Service Kit Hijacks Microsoft 365 Access Tokens," May 21, 2026 — https://www.ic3.gov/PSA/2026/PSA260521
- **Accuracy check:** The technical description (OAuth *device code flow* abuse, tokens surviving a password reset, real Microsoft domain used) is consistent with the FBI PSA and independent security analyses. Note Dan's summary said "without the need for a password" — confirmed accurate.
- **Tailoring:** I kept this non-technical for general staff. If our actual M365 footprint is limited (given we've held off on most connectors), you may want to add a line clarifying which tools we do/don't use so people aren't confused. Happy to adjust.
- **Follow-ups I can prepare on request:** (1) a short separate note to anyone with admin/finance access; (2) a one-page "how to spot a device-code request" graphic; (3) talking points for IT on the conditional-access policy to block device code flow.
