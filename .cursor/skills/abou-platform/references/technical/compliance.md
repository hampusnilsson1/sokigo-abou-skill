# Compliance, hosting, browsers, eIDAS

Read 2026-08-25. High-level only.

## Protocols (pageId `60096956`)

From **2022.8**, HTTPS to external systems: **TLS 1.3** and **TLS 1.2**. TLS 1.1 / 1.0 not supported. SSL3 not enabled by default.

## Browsers (pageId `60096958`)

Latest **Edge, Firefox, Chrome, Safari**. Older versions only as long as they are not a security hole.

## GDPR (*Information om GDPR*)

Sokigo documents GDPR approach, internal systems, planned work, and customer responsibilities. Person data in Abou is plugin-backed ([citizeninfo.md](citizeninfo.md)). Do not store extra person fields in Python. Scheduled **Synkronisera personuppgifter** and soft/permanent delete are the operational tools ([../scheduling.md](../scheduling.md)).

## eIDAS (*Vad är EIDAS*, pageId `60096954`)

EU e-ID: foreign e-leg in Swedish public services. Identifier is **not** always a Swedish personnummer — country codes + id. No new Abou version required; municipality talks to their e-leg IdP, Sokigo maps metadata (may patch).

Citizen flow: pick service → IdP → BankID / Mobilt BankID / **eIDAS** → back to Abou.

Per service, the municipality chooses what a foreign-id user may do (info page, English variant, or full flow). **Integrerat personnummerfält** should become **integrerat användarnamnsfält** (or branching logic) if foreign ids must submit. Min sida then works like BankID.

## Accessibility (*Tillgänglighetsredogörelse*, pageId `60096950`)

Law: SFS 2018:1937. Sokigo targets **WCAG 2.1 AA** and **EN 301 549**. Useit reviews. Known remaining deviations (fix in product; also depend on how you build the e-tjänst):

- Maps: not screen-reader/keyboard — always offer address/coordinate input
- **Rullista med sök** not usable with screen readers
- Error messages for radio/checkbox **groups** not correctly associated
- Table layout can confuse some screen readers
- Graphic captcha on e-förslag — **do not use**
- **Lägg till rad** not accessibility-adapted — avoid when a11y is required
- Failed-submit error not presented correctly; after reload focus jumps to top

2019-03-11 Useit findings on the Lyckebo theme were addressed in **2021.2**. Customer content (images, PDFs) is the municipality’s a11y duty.

## Penetration tests

Confluence *Penetrationstester av Abou* records that tests exist. **Do not copy exploit detail into this skill.**

## Hosting PDFs (not transcribed)

- Ansvarsfördelning vid drift On Prem (`161742875`)
- Teknisk kravspecifikation - Abou Intern Hosting
